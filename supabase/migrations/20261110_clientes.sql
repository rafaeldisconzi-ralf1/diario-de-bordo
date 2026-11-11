-- Números de clientes para o admin (Perfil → Visitas e vendas)
-- Não conta: admin e contas de teste.
create or replace function public.resumo_clientes() returns json
language plpgsql stable security definer set search_path = public as
$$ declare hoje date := (now() at time zone 'America/Sao_Paulo')::date; r json;
begin
  if not eh_admin() then raise exception 'Somente o administrador'; end if;
  with c as (
    select p.*, greatest(p.teste_ate, p.pago_ate) as acesso_ate,
      exists (select 1 from pagamentos g where lower(g.email) = lower(p.email) and g.status = 'approved' and g.valor > 0) as pagou
    from perfis p
    where not p.admin
      and lower(coalesce(p.email,'')) not in ('nao-responda@trilhanova.shop','pelecoreana@verdadeoculta.shop')
      and p.email not like '%.comll'
  )
  select json_build_object(
    'total',        count(*),
    'com_acesso',   count(*) filter (where acesso_ate >= hoje),
    'pagantes',     count(*) filter (where acesso_ate >= hoje and pagou),
    'cortesia',     count(*) filter (where acesso_ate >= hoje and not pagou),
    'vencidos',     count(*) filter (where acesso_ate is null or acesso_ate < hoje),
    'vencem_7d',    count(*) filter (where acesso_ate between hoje and hoje + 7),
    'ativos_24h',   count(*) filter (where visto_em > now() - interval '24 hours'),
    'ativos_7d',    count(*) filter (where visto_em > now() - interval '7 days'),
    'novos_7d',     count(*) filter (where criado_em > now() - interval '7 days')
  ) into r from c;
  return r;
end $$;
revoke all on function public.resumo_clientes() from public, anon;
grant execute on function public.resumo_clientes() to authenticated;
