// Gera o Pix no Mercado Pago, consulta o status e recebe o aviso de pagamento (webhook).
// Segredo necessário: MP_ACCESS_TOKEN (colado no painel do Supabase, nunca no código).
import { createClient } from "jsr:@supabase/supabase-js@2";

const PLANOS: Record<string, { valor: number; dias: number; nome: string }> = {
  mensal: { valor: 24.9, dias: 30, nome: "Diário de Bordo - Mensal" },
  anual: { valor: 179.9, dias: 365, nome: "Diário de Bordo - Anual" },
};
const SB_URL = Deno.env.get("SUPABASE_URL")!;
const sb = createClient(SB_URL, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "content-type, authorization, apikey, x-client-info",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
const json = (b: unknown, s = 200) =>
  new Response(JSON.stringify(b), { status: s, headers: { ...CORS, "Content-Type": "application/json" } });

async function mp(path: string, init: RequestInit = {}) {
  const token = Deno.env.get("MP_ACCESS_TOKEN");
  if (!token) throw new Error("MP_ACCESS_TOKEN não configurado");
  const r = await fetch("https://api.mercadopago.com" + path, {
    ...init,
    headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/json", ...(init.headers || {}) },
  });
  const j = await r.json().catch(() => ({}));
  if (!r.ok) throw new Error(`Mercado Pago ${r.status}: ${JSON.stringify(j).slice(0, 400)}`);
  return j;
}

// Busca o pagamento no Mercado Pago (fonte da verdade) e libera a conta se aprovado.
async function atualizar(id: string) {
  if (!/^\d+$/.test(id)) return null;
  let { data: linha } = await sb.from("pagamentos").select("*").eq("id", id).maybeSingle();
  const p = await mp(`/v1/payments/${id}`);
  if (!linha) {
    // pagamento com cartão (Checkout Pro): o id só existe depois que a pessoa paga
    const [plano, email] = String(p.external_reference || "").split("|");
    const P = PLANOS[plano];
    if (!P || !email || Number(p.transaction_amount) + 0.001 < P.valor) return null;
    const nova = { id, email, plano, valor: P.valor, dias: P.dias, status: p.status };
    await sb.from("pagamentos").upsert(nova, { onConflict: "id", ignoreDuplicates: true });
    ({ data: linha } = await sb.from("pagamentos").select("*").eq("id", id).maybeSingle());
    if (!linha) return null;
  }
  const novo: Record<string, unknown> = { status: p.status };
  if (p.status === "approved" && !linha.aprovado_em) novo.aprovado_em = new Date().toISOString();
  await sb.from("pagamentos").update(novo).eq("id", id);
  if (p.status === "approved") await sb.rpc("aplicar_pagamentos", { alvo_email: linha.email });
  return p.status as string;
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  const url = new URL(req.url);
  let body: any = {};
  try { body = await req.json(); } catch { /* aviso pode vir sem corpo */ }
  try {
    if (body.acao === "criar") {
      const email = String(body.email || "").trim().toLowerCase();
      const plano = PLANOS[body.plano];
      if (!/^\S+@\S+\.\S+$/.test(email) || !plano) return json({ erro: "Confira o e-mail." }, 400);
      const vence = new Date(Date.now() + 30 * 60_000).toISOString().replace("Z", "+00:00");
      const p = await mp("/v1/payments", {
        method: "POST",
        headers: { "X-Idempotency-Key": crypto.randomUUID() },
        body: JSON.stringify({
          transaction_amount: plano.valor,
          description: plano.nome,
          payment_method_id: "pix",
          payer: { email },
          external_reference: `${body.plano}|${email}`,
          notification_url: `${SB_URL}/functions/v1/pix`,
          date_of_expiration: vence,
        }),
      });
      await sb.from("pagamentos").insert({
        id: String(p.id), email, plano: body.plano, valor: plano.valor, dias: plano.dias, status: p.status,
      });
      const td = p.point_of_interaction?.transaction_data || {};
      return json({ id: String(p.id), copia_e_cola: td.qr_code, qr_base64: td.qr_code_base64, valor: plano.valor });
    }
    if (body.acao === "cartao") {
      const email = String(body.email || "").trim().toLowerCase();
      const plano = PLANOS[body.plano];
      if (!/^\S+@\S+\.\S+$/.test(email) || !plano) return json({ erro: "Confira o e-mail." }, 400);
      const volta = `https://frete.trilhanova.shop/assinar/?email=${encodeURIComponent(email)}&pago=cartao`;
      const pref = await mp("/checkout/preferences", {
        method: "POST",
        body: JSON.stringify({
          items: [{ title: plano.nome, quantity: 1, unit_price: plano.valor, currency_id: "BRL" }],
          payer: { email },
          external_reference: `${body.plano}|${email}`,
          notification_url: `${SB_URL}/functions/v1/pix`,
          back_urls: { success: volta, pending: volta, failure: volta },
          auto_return: "approved",
          statement_descriptor: "DIARIODEBORDO",
          payment_methods: {
            excluded_payment_types: [{ id: "ticket" }, { id: "atm" }],
            installments: body.plano === "anual" ? 12 : 1,
          },
        }),
      });
      return json({ url: pref.init_point });
    }
    if (body.acao === "status") {
      return json({ status: await atualizar(String(body.id || "")) });
    }
    // Aviso do Mercado Pago: ?data.id=123&type=payment ou {"data":{"id":"123"}}
    const tipo = body?.type || url.searchParams.get("type") || url.searchParams.get("topic");
    const id = body?.data?.id || url.searchParams.get("data.id") || url.searchParams.get("id");
    if (tipo === "payment" && id) await atualizar(String(id));
    return json({ ok: true });
  } catch (e) {
    console.error(e);
    return json({ erro: "Não deu para continuar agora. Tente de novo em instantes." }, 500);
  }
});
