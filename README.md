# Diário de Bordo

App simples para o motorista lançar viagens, abastecimentos e gastos do caminhão.
No ar em https://frete.trilhanova.shop (deploy automático pela Hostinger a cada push na `main`).

Os lançamentos ficam salvos no celular de quem usa (localStorage, chave `diario-bordo-v1`).
Trocar os arquivos deste repositório não apaga esses dados, desde que o endereço continue o mesmo.

## Versão com conta (em teste)
- `nuvem/index.html`: mesma interface + login por e-mail e sincronização com o Supabase (projeto `diario-de-bordo`, ref `kmaldmypdvapihsxpfmz`).
- Banco: `supabase/migrations/20261108_inicial.sql` (tabelas `perfis` e `registros`, RLS, função `liberar_dias` para o admin).
- Endereço de teste: https://frete.trilhanova.shop/nuvem/
