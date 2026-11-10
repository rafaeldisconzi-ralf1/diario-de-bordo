# App — como funciona

## Endereços
- frete.trilhanova.shop — app sem conta (o pai usa; dados só no celular, localStorage `diario-bordo-v1`)
- frete.trilhanova.shop/nuvem/ — app com conta (login por código no e-mail, dados na nuvem) — **é o produto**
- frete.trilhanova.shop/assinar/ — página de vendas com Pix e cartão

## Arquivos
| Arquivo | O que é |
|---|---|
| `index.html` | app sem conta (não mexer sem aprovação) |
| `nuvem/index.html` | app com conta; meta `app-version` diz a versão |
| `assinar/index.html` | página de vendas (efeitos, planos, janela de pagamento, FAQ). `VIDEO_YOUTUBE=''` mostra o vídeo quando preenchido |
| `sw.js` | service worker: funciona sem sinal; recebe notificações. Ao mudar, subir `CACHE` (bordo-vN) |
| `vendor/` | supabase-js 2.118.0 e xlsx-js-style 1.2.0 (planilha do relatório com cores; licença Apache 2.0) — locais, sem CDN |
| `supabase/migrations/*.sql` | banco (já aplicados pelo SQL Editor do Supabase) |
| `supabase/functions/pix` | cria Pix, link do cartão, recebe aviso do Mercado Pago e libera a conta |
| `supabase/functions/relatorio` | manda a planilha do mês para o e-mail da própria conta (só quando a pessoa pede; limite 5 por dia; tabela `relatorios_enviados`) |
| `supabase/functions/avisos` | notificações (Web Push): chave, teste, aviso do admin, lembrete de vencimento |

## Supabase (projeto `diario-de-bordo`, ref `kmaldmypdvapihsxpfmz`, plano grátis, Organização 2)
- Login: e-mail com código de 6 dígitos (o app corrige erros comuns de digitação, como gmail.comll / gmail.con, e pede
  para tocar de novo — `sugestaoEmail`); SMTP da Hostinger (`nao-responda@trilhanova.shop`).
- Tabelas: `perfis` (teste_ate, pago_ate, admin, visto_em), `registros` (viagens e lançamentos em JSON, apagado,
  atualizado_em), `pagamentos`, `push_inscricoes`, `config_privada` (chaves VAPID, só o servidor lê), `avisos_enviados`.
- Admin: rafaeldisconzi@gmail.com → no app, Perfil → **Clientes** (liberar +30 dias) e **Mandar aviso para todos**.
- Sem teste grátis: conta nova nasce vencida; o pagamento aprovado soma os dias (`aplicar_pagamentos`).
- Lembrete de vencimento: `pg_cron` todo dia 12:00 UTC (9h Brasília) chama a função `avisos` (3 dias antes, no dia, 1 dia depois).
- Funções com "Verify JWT" **desligado** (elas checam o login no código). Deploy pelo editor do painel.
- Segredos: `MP_ACCESS_TOKEN` e `SMTP_PASS` (senha do nao-responda@trilhanova.shop, usada pelo relatório por e-mail; SMTP smtp.hostinger.com:465). Ficam em Edge Functions → Secrets. Nunca no código.

## Mercado Pago
- Pix: `/v1/payments`, vence em 30 min, a tela confere o status a cada 4 s.
- Cartão: Checkout Pro (anual em até 12x), volta para `/assinar/?pago=cartao`.
- O aviso (webhook) só é aceito do tipo `payment`; o servidor sempre consulta o pagamento no MP antes de liberar.

## Recursos do app com conta
Sincronização automática (funciona sem sinal e sobe depois), relatório do mês em planilha (aba Viagens: baixar/compartilhar ou "Mandar para meu e-mail"; cada viagem conta no mês em que
TERMINOU (em andamento: mês atual), igual às telas de Início e Viagens — `mesViagem(t)`; mês marcado: o anterior se hoje é dia 1–5 e ele tem dados, senão o atual, senão o mais recente com dados;
mostra uma prévia do mês escolhido, avisa viagem em andamento e não deixa gerar mês vazio),
notificações (Perfil → Ativar notificações; no iPhone só com o app na Tela de Início), bloqueio quando vence com botão de Pix,
"Colocar o app na tela do celular" (Perfil e uma vez logo após o primeiro login): no Android abre a instalação do
próprio celular (`beforeinstallprompt`); no iPhone e quando o Android não oferece, um guia de 3 passos animados.
Some quando o app já está instalado. No Samsung Internet
o "Instalar" pode falhar ("Não foi possível instalar o aplicativo web"), então lá o guia ensina o atalho: menu ≡ →
Adicionar página a → Tela inicial. A versão com conta tem manifesto próprio (`nuvem/manifest.json`, abre em `/nuvem/`).

## Proteção contra erro de digitação (app com conta)
- Campos de valor mostram o número por extenso embaixo enquanto digita (`= R$ 2.000,00`, `= 350 L`, `= 15 %`):
  atributos `data-moeda` / `data-un` no input, tratados em `open()`.
- Ao salvar, `confere()` pergunta "está certo?" quando o valor foge do normal; se o número foi digitado sem vírgula e
  dividido por 100 fica normal, oferece o botão "Corrigir para R$ X" (`dividido`, `fixVal`). Não bloqueia: "Sim, está certo" salva.
- Faixas: diesel R$ 3–15/L, 5–1.500 L; gastos por categoria em `LIMITE_GASTO`; diária R$ 30–2.500; R$/km 0,5–40;
  frete fechado ≥ R$ 200 e ≤ 100 mil; distância ≤ 6.000 km; comissão ≤ 50% (acima de 100% é erro);
  "Cheguei": rodou ≤ 6.000 km e entre 0,4× e 2,5× a distância combinada.
- Lançamento igual (tipo + categoria + valor) nos últimos 10 min pergunta se quer lançar de novo (campo `criado`).
- Login corrige erros comuns no e-mail (`sugestaoEmail`).
- Todo lançamento tem "editar" (ao lado de "apagar"): abre o mesmo formulário preenchido (`editar()` → `abasteci/gastei/diaria(ed)`).
  Viagem: "Corrigir dados da viagem" no Início e no detalhe (`novaViagem(viagem)`), inclusive km de chegada se encerrada.

## Como testar
- Servidor local: `python3 -m http.server 8765` na pasta do repo.
- Supabase falso para Playwright: um script que substitui `/vendor/supabase-2.118.0.js` (login com código 123456,
  admin = admin@x.com). Recriar se não existir.
- A rede do ambiente do Claude não alcança supabase.co nem o site: testes reais pelo navegador do Rafael (Brave).

## Deploy
Hostinger → site trilhanova.shop → Avançado → GIT, branch `main`, pasta `public_html/frete`. Push = no ar.
`.htaccess` impede cache de html/js/json e bloqueia acesso a `docs/`, `marketing/` e arquivos `.md`.
