# Rotinas

## Toda semana (segunda)
- Contas novas, quem vence nos próximos 7 dias, pagamentos aprovados da semana (Clientes no app / tabela `pagamentos`).
- Qual vídeo foi postado e quantas visitas/vendas trouxe.
- Atualizar "onde paramos".

## Todo mês
- Receita do mês (Pix + cartão), taxas pagas, assinantes ativos, cancelamentos/reembolsos.
- Conferir se o lembrete de vencimento rodou (tabela `avisos_enviados`).
- Revisar o Advisor de segurança do Supabase.

## Quando mudar o app
1. Editar `nuvem/` (ou `assinar/`), subir a versão no meta `app-version` e o `CACHE` do `sw.js` se mexer nele.
2. Testar com Playwright (celular 390 px) e olhar prints.
3. Commit na `main` → conferir no site.
4. Atualizar `docs/app.md`.
