# CLAUDE.md — Diário de Bordo

Leia isto antes de qualquer tarefa. O dono é o Rafael: fale com ele em português simples, frases curtas.
Ele usa muito pelo celular, então mande resultados prontos (link, vídeo, arquivo) e não peça para ele rodar comandos.

## O que é
App web (PWA) para caminhoneiro lançar viagens, frete, diesel, gastos e diárias e ver **quanto sobrou**.
Vendido por assinatura (R$ 24,90/mês ou R$ 179,90/ano) via Pix e cartão no Mercado Pago, com liberação automática.
Público: motoristas e donos de caminhão com pouca familiaridade com tecnologia — tudo simples, botões grandes.

## Mapa do manual
- `docs/app.md` — como o app funciona por dentro: arquivos, Supabase, pagamentos, notificações, deploy
- `docs/marketing.md` — página de vendas, vídeos, roteiros, como fazer vídeo novo
- `docs/instagram.md` — manual do Instagram: algoritmo, Reels, carrossel, legenda, horários, rotina
- `docs/financas.md` — preços, taxas, como acompanhar vendas, pendências (MEI, marca)
- `docs/decisoes.md` — decisões já tomadas e por quê (não reabrir sem o Rafael pedir)
- `docs/rotinas.md` — o que fazer toda semana / todo mês
- Conversas do Project: uma por assunto. Finanças e Mercado Pago têm conversa própria (ver `docs/financas.md`).
- Documento vivo "Diário de Bordo: onde paramos": https://claude.ai/artifact/8AwH8QNM59JcqFtv26xUGq

## Regras que valem sempre
1. **O app sem conta saiu do ar** (10/11/2026, pedido do Rafael). `index.html` na raiz agora só manda para `/nuvem/`
   (login obrigatório). Não voltar o app aberto sem o Rafael pedir.
2. **Nunca colocar senha, token ou chave em código, chat ou documento.** Segredos ficam só nos painéis
   (Supabase → Edge Functions → Secrets). Quem digita senha é o Rafael.
3. **Nada que custe dinheiro sem perguntar** (ex.: não criar projeto pago no Supabase; ElevenLabs só com aprovação).
4. Mudanças sempre por código: commit na `main` → a Hostinger publica sozinha em segundos.
5. Antes de entregar, testar (Playwright com o Supabase falso, ou no navegador) e olhar as telas.
6. **Dados reais de pessoas nunca aparecem em vídeo ou exemplo** (placa, nome do pai etc.). Use dados inventados
   (motorista "Carlos", Scania R 450, placa ABC 1D23).
7. Ao terminar uma tarefa, atualize o arquivo de `docs/` correspondente e o documento "onde paramos".

## Situação (atualize aqui)
- Nome "Diário de Bordo" **em revisão**: existe marca "Diário de Bordo" registrada no INPI (KUAU, classe 42,
  em vigor até 2030). Opções livres na busca: "Conta da Boleia", "Sobrou na Estrada". Ver `docs/decisoes.md`.
- Compra real por Pix testada em 10/11/2026: aprovou, liberou a conta e o login funcionou.
- Falta: compra de teste com cartão, testar notificações num celular, liberar a conta do pai, vídeo real com o pai. Depoimentos (4 prints) já na página de vendas.
