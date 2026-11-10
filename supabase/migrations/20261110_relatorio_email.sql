-- Relatório por e-mail: registro de envios (limite por dia por pessoa)
create table if not exists public.relatorios_enviados (
  id bigint generated always as identity primary key,
  user_id uuid not null references auth.users on delete cascade,
  mes text not null,
  enviado_em timestamptz not null default now()
);
create index if not exists relatorios_enviados_user on public.relatorios_enviados (user_id, enviado_em);
alter table public.relatorios_enviados enable row level security;
revoke all on public.relatorios_enviados from anon, authenticated;
