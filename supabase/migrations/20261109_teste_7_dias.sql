-- Teste grátis de 7 dias para contas novas
alter table public.perfis alter column teste_ate set default (current_date + 7);
