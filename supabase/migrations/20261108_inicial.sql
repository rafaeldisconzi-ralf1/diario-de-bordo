-- Diário de Bordo: contas, assinatura e lançamentos sincronizados
-- Cada pessoa só enxerga e altera os próprios dados (RLS).

create table if not exists public.perfis (
  id uuid primary key references auth.users on delete cascade,
  email text,
  nome text, modelo text, placa text, ano text, patrao text,
  teste_ate date not null default (current_date + 30),
  pago_ate date,
  admin boolean not null default false,
  criado_em timestamptz not null default now(),
  atualizado_em timestamptz not null default now(),
  visto_em timestamptz
);
alter table public.perfis enable row level security;

create table if not exists public.registros (
  user_id uuid not null default auth.uid() references auth.users on delete cascade,
  id text not null,
  tipo text not null check (tipo in ('viagem','avulso')),
  dados jsonb not null default '{}'::jsonb,
  apagado boolean not null default false,
  atualizado_em timestamptz not null default now(),
  primary key (user_id, id)
);
alter table public.registros enable row level security;
create index if not exists registros_sync on public.registros (user_id, atualizado_em);

-- quem é admin (consultado sem passar pelo RLS)
create or replace function public.eh_admin() returns boolean
language sql stable security definer set search_path = public as
$$ select coalesce((select admin from perfis where id = auth.uid()), false) $$;

-- perfil criado sozinho no primeiro login
create or replace function public.novo_usuario() returns trigger
language plpgsql security definer set search_path = public as
$$ begin
  insert into perfis (id, email) values (new.id, new.email) on conflict (id) do nothing;
  return new;
end $$;
drop trigger if exists ao_criar_usuario on auth.users;
create trigger ao_criar_usuario after insert on auth.users
  for each row execute function public.novo_usuario();

-- carimbo de data no servidor (o relógio do celular pode estar errado)
create or replace function public.carimbar() returns trigger
language plpgsql as $$ begin new.atualizado_em := now(); return new; end $$;
drop trigger if exists carimbo on public.registros;
create trigger carimbo before insert or update on public.registros
  for each row execute function public.carimbar();
drop trigger if exists carimbo on public.perfis;
create trigger carimbo before update on public.perfis
  for each row execute function public.carimbar();

-- perfis: cada um lê o seu; admin lê todos. Só edita nome/caminhão (nunca datas de pagamento nem admin).
drop policy if exists "ler perfil" on public.perfis;
create policy "ler perfil" on public.perfis for select to authenticated
  using (id = auth.uid() or public.eh_admin());
drop policy if exists "editar perfil" on public.perfis;
create policy "editar perfil" on public.perfis for update to authenticated
  using (id = auth.uid()) with check (id = auth.uid());
revoke all on public.perfis from anon;
revoke insert, update, delete on public.perfis from authenticated;
grant select on public.perfis to authenticated;
grant update (nome, modelo, placa, ano, patrao, visto_em) on public.perfis to authenticated;

-- registros: só os próprios
drop policy if exists "meus registros" on public.registros;
create policy "meus registros" on public.registros for all to authenticated
  using (user_id = auth.uid()) with check (user_id = auth.uid());
revoke all on public.registros from anon;
grant select, insert, update on public.registros to authenticated;

-- admin libera dias de uso (pagamento confirmado)
create or replace function public.liberar_dias(usuario uuid, dias int) returns date
language plpgsql security definer set search_path = public as
$$ declare nova date; begin
  if not eh_admin() then raise exception 'Somente o administrador pode liberar'; end if;
  update perfis set pago_ate = greatest(coalesce(pago_ate, current_date), current_date) + dias
    where id = usuario returning pago_ate into nova;
  return nova;
end $$;
revoke all on function public.liberar_dias(uuid, int) from public, anon;
grant execute on function public.liberar_dias(uuid, int) to authenticated;
