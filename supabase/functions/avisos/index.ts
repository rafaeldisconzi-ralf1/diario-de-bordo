// Notificações do Diário de Bordo (Web Push).
// acao 'chave'       → chave pública para o celular se inscrever (gera as chaves na 1ª vez)
// acao 'teste'       → manda uma notificação de teste para quem pediu (precisa estar logado)
// acao 'enviar'      → admin manda um aviso para todos
// acao 'vencimentos' → chamada pelo banco todo dia: avisa quem vence em 3 dias, hoje, ou venceu ontem
import { createClient } from "jsr:@supabase/supabase-js@2";
import webpush from "npm:web-push@3.6.7";

const sb = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "content-type, authorization, apikey, x-client-info, x-cron",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
const json = (b: unknown, s = 200) =>
  new Response(JSON.stringify(b), { status: s, headers: { ...CORS, "Content-Type": "application/json" } });

async function config(chave: string) {
  const { data } = await sb.from("config_privada").select("valor").eq("chave", chave).maybeSingle();
  return data?.valor as string | undefined;
}
async function chaves() {
  let pub = await config("vapid_publica"), priv = await config("vapid_privada");
  if (!pub || !priv) {
    const k = webpush.generateVAPIDKeys();
    await sb.from("config_privada").upsert([
      { chave: "vapid_publica", valor: k.publicKey },
      { chave: "vapid_privada", valor: k.privateKey },
      { chave: "cron_key", valor: crypto.randomUUID() + crypto.randomUUID() },
    ], { onConflict: "chave", ignoreDuplicates: true });
    pub = await config("vapid_publica"); priv = await config("vapid_privada");
  }
  webpush.setVapidDetails("mailto:nao-responda@trilhanova.shop", pub!, priv!);
  return pub!;
}
async function usuario(req: Request) {
  const t = (req.headers.get("authorization") || "").replace(/^Bearer\s+/i, "");
  if (!t) return null;
  const { data } = await sb.auth.getUser(t);
  return data?.user || null;
}
async function mandar(userIds: string[] | null, msg: { titulo: string; texto: string; url?: string }) {
  await chaves();
  let q = sb.from("push_inscricoes").select("endpoint,p256dh,auth,user_id");
  if (userIds) q = q.in("user_id", userIds);
  const { data: subs } = await q;
  let ok = 0;
  for (const s of subs || []) {
    try {
      await webpush.sendNotification(
        { endpoint: s.endpoint, keys: { p256dh: s.p256dh, auth: s.auth } },
        JSON.stringify({ titulo: msg.titulo, texto: msg.texto, url: msg.url || "/nuvem/" }),
        { TTL: 60 * 60 * 24 },
      );
      ok++;
    } catch (e: any) {
      if (e?.statusCode === 404 || e?.statusCode === 410) await sb.from("push_inscricoes").delete().eq("endpoint", s.endpoint);
      else console.error("push", e?.statusCode, e?.body);
    }
  }
  return ok;
}
const dia = (d: Date) => d.toISOString().slice(0, 10);
const brt = () => new Date(Date.now() - 3 * 3600_000); // data de Brasília

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  let body: any = {};
  try { body = await req.json(); } catch { /* sem corpo */ }
  try {
    if (body.acao === "chave") return json({ chave: await chaves() });

    if (body.acao === "teste") {
      const u = await usuario(req);
      if (!u) return json({ erro: "Entre na sua conta." }, 401);
      const n = await mandar([u.id], { titulo: "Diário de Bordo", texto: "Notificações ativadas. Você vai ser avisado por aqui." });
      return json({ enviadas: n });
    }

    if (body.acao === "enviar") {
      const u = await usuario(req);
      const { data: p } = u ? await sb.from("perfis").select("admin").eq("id", u.id).maybeSingle() : { data: null };
      if (!p?.admin) return json({ erro: "Só o administrador pode mandar avisos." }, 403);
      const titulo = String(body.titulo || "Diário de Bordo").slice(0, 60);
      const texto = String(body.texto || "").slice(0, 180);
      if (!texto) return json({ erro: "Escreva a mensagem." }, 400);
      return json({ enviadas: await mandar(null, { titulo, texto }) });
    }

    if (body.acao === "vencimentos") {
      if (!req.headers.get("x-cron") || req.headers.get("x-cron") !== (await config("cron_key"))) return json({ erro: "não autorizado" }, 401);
      const hoje = brt(), d = (n: number) => { const x = new Date(hoje); x.setUTCDate(x.getUTCDate() + n); return dia(x); };
      const alvos: Record<string, { tipo: string; titulo: string; texto: string }> = {
        [d(3)]: { tipo: "vence3", titulo: "Seu acesso vence em 3 dias", texto: "Renove pelo Pix para não parar de lançar suas viagens." },
        [d(0)]: { tipo: "vence0", titulo: "Seu acesso vence hoje", texto: "Toque aqui para renovar. Seus lançamentos continuam guardados." },
        [d(-1)]: { tipo: "venceu", titulo: "Seu acesso venceu", texto: "Renove pelo Pix e continue de onde parou." },
      };
      const { data: perfis } = await sb.from("perfis").select("id,email,teste_ate,pago_ate,admin");
      let n = 0;
      for (const p of perfis || []) {
        if (p.admin) continue;
        const ate = [p.teste_ate, p.pago_ate].filter(Boolean).sort().pop();
        const a = ate && alvos[ate];
        if (!a) continue;
        const { error } = await sb.from("avisos_enviados").insert({ user_id: p.id, tipo: a.tipo, dia: dia(hoje) });
        if (error) continue; // já avisado hoje
        n += await mandar([p.id], { ...a, url: `/assinar/?email=${encodeURIComponent(p.email || "")}#preco` });
      }
      return json({ enviadas: n });
    }
    return json({ erro: "ação desconhecida" }, 400);
  } catch (e) {
    console.error(e);
    return json({ erro: "Não deu agora. Tente de novo." }, 500);
  }
});
