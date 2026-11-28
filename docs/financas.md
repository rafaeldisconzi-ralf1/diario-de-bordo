# Finanças

## Conversa de finanças
Desde 10/11/2026 existe uma conversa só para finanças e Mercado Pago no Project "Diário de Bordo".
Ela cuida de: vendas e receitas, taxas, pagamentos (Pix e cartão), reembolsos, conta e token do Mercado Pago,
tabela `pagamentos`, resumo semanal/mensal de `rotinas.md` e as pendências abaixo (MEI, nome no Pix, renovação automática).
Mudanças no código de pagamento (`supabase/functions/pix`, janela de pagamento em `assinar/`) também passam por ela.

## Preços
- Mensal: R$ 24,90 (30 dias) — **preço de lançamento**; depois do lançamento passa para R$ 49,90 (data a definir) · Anual: R$ 179,90 (365 dias; equivale a R$ 14,99/mês; até 12x no cartão)
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

## Vendas
| Data | Plano | Valor | Forma | Situação |
|---|---|---|---|---|
| 21/11/2026 21:06 | mensal | R$ 24,90 | Pix | **1ª venda real.** Aprovado; conta ainda não criada na hora da conferência (os 30 dias entram no 1º login) |

Para conferir uma venda: SQL Editor do Supabase, `pagamentos` junto com `perfis` pelo e-mail.
`aplicado = false` e sem perfil = pagou mas ainda não entrou no app (normal); os dias somam sozinhos no 1º login.
Não colocar e-mail de cliente aqui (repositório público).

## Gasto com anúncios (Meta) x vendas
| Dia | Gasto | Visitas (anúncio) | Tocou Assinar | Pix gerado | Vendas |
|---|---|---|---|---|---|
| 21/11 | R$ 27,50 | 59 | 4 | 1 | 1 (R$ 24,90) |
| 22/11 (até 22h) | R$ 54,41 | 143 | 2 | 1 (venceu sem pagar) | 0 |
| 27/11 18:30 a 28/11 (~9h) | R$ 21,55 | 36 | 2 | 0 | 0 |

Visitas e cliques vêm da tabela `eventos` (origem `anuncio_meta`); gasto do Gerenciador de Anúncios.
O Meta pode gastar até ~75% acima do orçamento diário num dia (R$ 40 → R$ 54).

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

## Black Friday 2026 (27/11 a 30/11)
- Mensal **R$ 19,90** (de R$ 24,90) até segunda 30/11 às 23h59 de Brasília. Anual continua R$ 179,90.
- Desconto real, decidido pelo Rafael em 27/11 (não usar "preço de Black Friday" sem baixar preço: risco de propaganda enganosa).
- Servidor (`supabase/functions/pix/index.ts`, `BF_FIM`) cobra R$ 19,90 até `2026-12-01T03:00Z` e volta sozinho para R$ 24,90. Pagamento aberto durante a Black Friday vale o preço dela, mesmo se pago depois.
- Página de vendas: faixa preta no topo, quadro "Black Friday" com relógio e cartão do mensal "de R$ 24,90 por R$ 19,90". Tudo some sozinho depois do prazo (mesmo `BF_FIM` no `assinar/index.html`).
- Depois de 01/12 pode apagar o código da Black Friday (não é obrigatório: ele não faz nada fora do prazo).

## Preço de lançamento: mensagem retirada (27/11/2026)
- A pedido do Rafael, saiu da página de vendas o quadro "Preço de lançamento" ("o app vale R$ 49,90… depois do lançamento passa para R$ 49,90") e a linha "Depois do lançamento: R$ 49,90" do cartão mensal (virou "Sem fidelidade. Pague mês a mês."). Não há mais promessa de aumento para R$ 49,90 na página.
