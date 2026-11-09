-- Pagamentos por Pix (Mercado Pago) e liberação automática do acesso
create table if not exists public.pagamentos (
  id text primary key,                 -- id do pagamento no Mercado Pago
  email text not null,
  plano text not null check (plano in ('mensal','anual')),
  valor numeric(10,2) not null,
  dias int not null,
  status text not null default 'pending',
  aplicado boolean not null default false,
  criado_em timestamptz not null default now(),
  aprovado_em timestamptz
);
alter table public.pagamentos enable row level security;
revoke all on public.pagamentos from anon, authenticated;
create index if not exists pagamentos_email on public.pagamentos (lower(email));
drop policy if exists "admin le pagamentos" on public.pagamentos;
create policy "admin le pagamentos" on public.pagamentos for select to authenticated using (public.eh_admin());
grant select on public.pagamentos to authenticated;

-- soma os dias dos Pix aprovados que ainda não foram aplicados à conta daquele e-mail
create or replace function public.aplicar_pagamentos(alvo_email text) returns void
language plpgsql security definer set search_path = public as
$$ declare p record; uid uuid; begin
  select id into uid from perfis where lower(email) = lower(alvo_email) limit 1;
  if uid is null then return; end if;
  for p in select * from pagamentos
           where lower(email) = lower(alvo_email) and status = 'approved' and not aplicado
           order by aprovado_em nulls last loop
    update perfis set pago_ate = greatest(coalesce(pago_ate, current_date), current_date) + p.dias where id = uid;
    update pagamentos set aplicado = true where id = p.id;
  end loop;
end $$;
revoke all on function public.aplicar_pagamentos(text) from public, anon, authenticated;
grant execute on function public.aplicar_pagamentos(text) to service_role;

-- conta nova: já aplica o Pix que a pessoa pagou antes de entrar no app
create or replace function public.novo_usuario() returns trigger
language plpgsql security definer set search_path = public as
$$ begin
  insert into perfis (id, email, admin) values (new.id, new.email, lower(new.email) = 'rafaeldisconzi@gmail.com')
  on conflict (id) do nothing;
  perform aplicar_pagamentos(new.email);
  return new;
end $$;

-- sem teste grátis: a conta só fica liberada depois do Pix
alter table public.perfis alter column teste_ate set default (current_date - 1);
