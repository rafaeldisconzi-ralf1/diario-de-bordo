-- Notificações (Web Push)
create table if not exists public.push_inscricoes (
  endpoint text primary key,
  user_id uuid not null default auth.uid() references auth.users on delete cascade,
  p256dh text not null,
  auth text not null,
  criado_em timestamptz not null default now()
);
alter table public.push_inscricoes enable row level security;
revoke all on public.push_inscricoes from anon, authenticated;
grant select, insert, update, delete on public.push_inscricoes to authenticated;
drop policy if exists "minhas inscricoes" on public.push_inscricoes;
create policy "minhas inscricoes" on public.push_inscricoes for all to authenticated
  using (user_id = auth.uid()) with check (user_id = auth.uid());

-- chaves e segredos gerados pelo próprio servidor (ninguém de fora lê)
create table if not exists public.config_privada (chave text primary key, valor text not null);
alter table public.config_privada enable row level security;
revoke all on public.config_privada from anon, authenticated;

-- para não mandar o mesmo aviso duas vezes no mesmo dia
create table if not exists public.avisos_enviados (
  user_id uuid not null references auth.users on delete cascade,
  tipo text not null,
  dia date not null default current_date,
  primary key (user_id, tipo, dia)
);
alter table public.avisos_enviados enable row level security;
revoke all on public.avisos_enviados from anon, authenticated;

-- aviso diário de vencimento: o banco chama a função 'avisos' todo dia às 9h (Brasília)
create extension if not exists pg_net;
create extension if not exists pg_cron;
create or replace function public.chamar_avisos() returns void
language plpgsql security definer set search_path = public as
$$ declare k text; begin
  select valor into k from config_privada where config_privada.chave = 'cron_key';
  if k is null then return; end if;
  perform net.http_post(
    url := 'https://kmaldmypdvapihsxpfmz.supabase.co/functions/v1/avisos',
    headers := jsonb_build_object('Content-Type','application/json','x-cron', k),
    body := '{"acao":"vencimentos"}'::jsonb);
end $$;
revoke all on function public.chamar_avisos() from public, anon, authenticated;
select cron.unschedule('avisos-diarios') where exists (select 1 from cron.job where jobname = 'avisos-diarios');
select cron.schedule('avisos-diarios', '0 12 * * *', 'select public.chamar_avisos()');
