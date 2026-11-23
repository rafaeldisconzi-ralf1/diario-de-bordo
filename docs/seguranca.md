# Segurança — revisão de 23/11/2026

Revisão feita com o método da skill `security-audit` da Cloudflare (github.com/cloudflare/security-audit-skill),
rodada por um agente só, de forma **parcial**. Só leitura: nada do app foi alterado.

## O que foi olhado
- Banco: as 6 migrações em `supabase/migrations/` (regras de acesso, funções)
- Servidor: `supabase/functions/pix`, `avisos`, `relatorio`
- Telas: `nuvem/index.html`, `assinar/index.html`, `sw.js`, `.htaccess`
- Fora do alcance: `index.html` da raiz (app do pai, não mexer), painel do Supabase (Auth, limites), bibliotecas em `vendor/`

## Achados (do mais grave ao menos)

### 1. ALTA — Um pagamento pode liberar vários meses (CONFIRMADO) — CORRIGIDO em 23/11
- Onde: função `aplicar_pagamentos` em `20261109_pagamentos.sql`.
- Problema: se duas confirmações do mesmo pagamento chegam ao mesmo tempo, as duas somam os dias.
  Isso acontece de verdade: o aviso do Mercado Pago e a consulta `status` que a tela de venda faz a cada 4 s.
  Quem paga o Pix recebe o id do pagamento e pode repetir `status` em paralelo.
- Prova (banco de teste local, dados inventados): 8 confirmações simultâneas de um pagamento de 30 dias
  deram 60 a 240 dias em 150 de 150 rodadas.
- Correção (testada: 150 de 150 rodadas deram 30 dias; dois pagamentos diferentes somam certo, 30+365=395):
  na função, trocar o `select ... order by aprovado_em nulls last loop` por
  `select ... order by aprovado_em nulls last for update loop`.
  Migração `supabase/migrations/20261123_seguranca.sql`, aplicada no Supabase em 23/11 (conferido: a função tem o `for update`).
- Conferência feita no banco depois: nenhuma conta tem mais dias do que pagou (3 contas pagas; 365 pagos → 352 restantes; 30 pagos → 17 restantes).

### 2. MÉDIA — Qualquer conta pode travar os avisos (CONFIRMADO no código) — CORRIGIDO em 23/11
- Onde: tabela `push_inscricoes` (`20261109_notificacoes.sql`) e função `avisos`.
- Problema: a inscrição aceita qualquer endereço https escolhido pela pessoa. A função manda os avisos em fila,
  sem tempo limite (a biblioteca `web-push` 3.6.7 só limita se pedirem). Um endereço que não responde pode travar
  o lembrete de vencimento das 9h e o "aviso para todos". Cadastro é livre (e-mail + código).
  O servidor também manda para esse endereço uma assinatura assinada com a chave de push.
- Correção (feita em 23/11): (a) no banco, trava `push_endereco_conhecido` aceita só fcm.googleapis.com,
  updates.push.services.mozilla.com, *.notify.windows.com e web.push.apple.com (vale para inscrições novas; as antigas não foram mexidas);
  (b) função `avisos` publicada com `timeout: 10000` no `sendNotification`.
  Falta só testar o aviso num celular real (já era pendência) para ver que o Chrome, o Firefox e o Safari continuam se inscrevendo.

### 3. BAIXA — Sem trava global no e-mail de envio (PRECISA CONFIRMAR)
- Onde: função `relatorio`.
- Problema: o limite de 5 por dia é por conta, e a contagem é feita antes de gravar (várias chamadas juntas passam).
  O mesmo e-mail `nao-responda@` manda os códigos de login. Se a Hostinger bloquear o remetente por excesso,
  ninguém recebe o código. Não consegui ver o limite de envio da Hostinger.
- Correção: gravar o envio antes de mandar e limitar o total por hora; ver o limite da Hostinger.

### 4. BAIXA — Criar cobrança e consultar status sem limite
- Onde: função `pix` (`criar`, `cartao`, `status`).
- Problema: qualquer pessoa pode gerar muitos Pix pendentes e consultas ao Mercado Pago. Não gera cobrança falsa nem
  libera conta (o servidor sempre confere no Mercado Pago). Nomes de plano como `constructor` passam na checagem,
  mas o Mercado Pago recusa a cobrança.
- Correção: limite por IP/e-mail; usar `Object.hasOwn(PLANOS, plano)`.

### 5. INFORMATIVO
- A trava de "acesso vencido" do app é só na tela. O banco aceita gravar lançamentos mesmo vencido
  (o relatório por e-mail já confere no servidor). Se quiser travar de verdade: regra no banco só para gravar,
  deixando ler (para o motorista ver o que lançou).
- Cada e-mail novo ganha 7 dias de teste (decisão de negócio). Os lançamentos não têm limite de tamanho:
  precisa confirmar se a cota do plano grátis do Supabase aguenta abuso.
- Sem cabeçalhos de segurança (CSP) no `.htaccess`. Hoje não há falha de texto injetado, então não é urgente.

## Checado e sem problema
- Regras de acesso do banco: cada pessoa só lê e grava os próprios dados; `admin`, `pago_ate` e `teste_ate` não podem ser editados por ela.
- `liberar_dias` só roda para admin; `aplicar_pagamentos` só para o servidor.
- Aviso do Mercado Pago: o servidor sempre consulta o pagamento lá antes de liberar.
- Sem senha, token ou chave secreta no código. A chave `sb_publishable_...` no app é pública por desenho.
- Textos digitados (nome, e-mail, origem, destino, categoria) saem com proteção na tela do admin, no login e na página de vendas;
  o e-mail que vem no endereço (`?email=`) também.
- O service worker só abre endereços do próprio site. O lembrete diário só aceita a chave `x-cron`.

## Pendente
- [x] Correção do achado 1 aplicada e conferida (23/11)
- [x] Correção do achado 2 aplicada (trava no banco + função publicada) (23/11)
- [ ] Testar "Ativar notificações" num celular (se algum celular for recusado pela trava, avisar o Claude)
- [ ] Achados 3 e 4 (baixos): limite global de e-mail e limite em criar cobrança; ver o limite de envio da Hostinger
- [ ] Rodar a revisão de novo depois dessas
