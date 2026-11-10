// Manda a planilha do mês para o e-mail da própria conta (só quando a pessoa pede).
// Segredo necessário: SMTP_PASS (senha do nao-responda@trilhanova.shop), colado no painel do Supabase.
import { createClient } from "jsr:@supabase/supabase-js@2";
import nodemailer from "npm:nodemailer@6.9.16";

const sb = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
const DE = "nao-responda@trilhanova.shop";
const LIMITE_DIA = 5;
const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "content-type, authorization, apikey, x-client-info",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
const json = (b: unknown, s = 200) =>
  new Response(JSON.stringify(b), { status: s, headers: { ...CORS, "Content-Type": "application/json" } });
const MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"];
const esc = (s: string) => s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]!));

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  try {
    const token = (req.headers.get("authorization") || "").replace(/^Bearer\s+/i, "");
    const { data: u } = token ? await sb.auth.getUser(token) : { data: null };
    const user = u?.user;
    if (!user?.email) return json({ erro: "Entre na sua conta." }, 401);

    const body = await req.json().catch(() => ({}));
    const mes = String(body.mes || "");
    const arquivo = String(body.arquivo || "");
    if (!/^\d{4}-\d{2}$/.test(mes)) return json({ erro: "Mês inválido." }, 400);
    if (!arquivo || arquivo.length > 3_000_000 || !/^[A-Za-z0-9+/=]+$/.test(arquivo)) return json({ erro: "Planilha inválida." }, 400);
    // a planilha .xlsx é um zip: começa com "PK"
    if (!arquivo.startsWith("UEsD")) return json({ erro: "Planilha inválida." }, 400);

    // só quem tem acesso em dia (ou admin)
    const { data: p } = await sb.from("perfis").select("teste_ate,pago_ate,admin").eq("id", user.id).maybeSingle();
    const hoje = new Date(Date.now() - 3 * 3600_000).toISOString().slice(0, 10);
    const ate = [p?.teste_ate, p?.pago_ate].filter(Boolean).sort().pop();
    if (!p?.admin && (!ate || ate < hoje)) return json({ erro: "Seu acesso venceu. Renove para mandar o relatório." }, 403);

    const desde = new Date(Date.now() - 24 * 3600_000).toISOString();
    const { count } = await sb.from("relatorios_enviados").select("id", { count: "exact", head: true }).eq("user_id", user.id).gte("enviado_em", desde);
    if ((count || 0) >= LIMITE_DIA) return json({ erro: "Você já mandou muitos relatórios hoje. Tente amanhã." }, 429);

    const pass = Deno.env.get("SMTP_PASS");
    if (!pass) return json({ erro: "O envio por e-mail ainda não foi ligado." }, 503);
    const [ano, m] = mes.split("-");
    const nomeMes = `${MESES[+m - 1]} de ${ano}`;
    const nome = String(body.nome || "").slice(0, 60);
    const resumo = String(body.resumo || "").slice(0, 300);

    const t = nodemailer.createTransport({ host: "smtp.hostinger.com", port: 465, secure: true, auth: { user: DE, pass } });
    await t.sendMail({
      from: `"Diário de Bordo" <${DE}>`,
      to: user.email,
      subject: `Seu relatório de ${nomeMes} - Diário de Bordo`,
      text: `Olá${nome ? ", " + nome : ""}!\n\nSegue em anexo a planilha de ${nomeMes}.\n${resumo}\n\nDiário de Bordo`,
      html: `<div style="font-family:Arial,sans-serif;font-size:16px;color:#1d1f22">
        <p>Olá${nome ? ", " + esc(nome) : ""}!</p>
        <p>Segue em anexo a planilha de <b>${nomeMes}</b>, com as viagens, o diesel, os gastos e quanto sobrou.</p>
        ${resumo ? `<p style="background:#f2b705;padding:12px 16px;border-radius:10px;font-weight:bold">${esc(resumo)}</p>` : ""}
        <p style="color:#666;font-size:13px">Você recebeu este e-mail porque pediu o relatório no app Diário de Bordo.</p></div>`,
      attachments: [{ filename: `Diario-de-Bordo-${mes}.xlsx`, content: arquivo, encoding: "base64",
        contentType: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" }],
    });
    await sb.from("relatorios_enviados").insert({ user_id: user.id, mes });
    return json({ ok: true, email: user.email });
  } catch (e) {
    console.error(e);
    return json({ erro: "Não deu para mandar agora. Tente de novo em instantes." }, 500);
  }
});
