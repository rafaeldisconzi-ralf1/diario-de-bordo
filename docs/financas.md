# Finanças

## Conversa de finanças
Desde 10/11/2026 existe uma conversa só para finanças e Mercado Pago no Project "Diário de Bordo".
Ela cuida de: vendas e receitas, taxas, pagamentos (Pix e cartão), reembolsos, conta e token do Mercado Pago,
tabela `pagamentos`, resumo semanal/mensal de `rotinas.md` e as pendências abaixo (MEI, nome no Pix, renovação automática).
Mudanças no código de pagamento (`supabase/functions/pix`, janela de pagamento em `assinar/`) também passam por ela.

## Preços
- Mensal: R$ 24,90 (30 dias) · Anual: R$ 179,90 (365 dias; equivale a R$ 14,99/mês; até 12x no cartão)
- Concorrência pesquisada: R$ 20–30/mês, com promoção anual.

## Taxas (Mercado Pago)
- Pix: 0,99% por venda, dinheiro na hora.
- Cartão: 4,98% à vista (parcelado tem acréscimo).

## Custos fixos
- Supabase: plano grátis (não usar recurso pago sem aprovação).
- Hostinger: já paga (site trilhanova.shop + e-mail).
- ElevenLabs: conta do Rafael (créditos).

## Onde ver as vendas
- Mercado Pago → atividades (Pix e cartão).
- No app, Perfil → Clientes: quem pagou e até quando.
- Tabela `pagamentos` no Supabase (status, valor, plano, quando foi aprovado).

## Pendências
- **Compra de teste com cartão**: Pix real já testado (10/11/2026, aprovou e liberou a conta); falta o cartão.
- **MEI/CNPJ**: hoje o Pix mostra o nome pessoal do Rafael. Com MEI, passar a conta do Mercado Pago para o CNPJ
  e trocar o token no Supabase.
- **Marca**: escolher nome novo e registrar no INPI (classes 9 e 42). Ver `decisoes.md`.
- Futuro: assinatura com renovação automática no cartão.

## Acessos de cortesia
Liberados pelo SQL Editor do Supabase: uma linha em `pagamentos` com id `cortesia-<email>`, valor 0, status `approved`.
Se a conta ainda não existe, vale no primeiro login (gatilho `novo_usuario` → `aplicar_pagamentos`); se já existe,
rodar `select aplicar_pagamentos('<email>')`. Não entram como venda (valor 0).
- 10/11/2026: luiscarlosdisconzi2529@gmail.com e leandrobomfim16089912@gmail.com — 365 dias (pedido do Rafael).
