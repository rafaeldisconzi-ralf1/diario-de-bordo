-- IA do app (Pergunte ao Diário + lançar por voz). Função 'ia'; chave GROQ_API_KEY só em Edge Functions → Secrets.
-- Conta o uso por dia (horário de Brasília) para não estourar o plano grátis.
create table if not exists public.ia_uso (
  user_id uuid not null references auth.users on delete cascade,
  dia date not null,
  tipo text not null check (tipo in ('pergunta','voz')),
  n int not null default 0,
  primary key (user_id, dia, tipo)
);
alter table public.ia_uso enable row level security;
revoke all on public.ia_uso from anon, authenticated;

-- Reserva 1 uso de forma atômica. Devolve ok=false com o motivo: 'pessoa' (limite da conta) ou 'geral' (todo o app no dia).
create or replace function public.usar_ia(uid uuid, tipo_ text, max_pessoa int, max_geral int)
returns jsonb language plpgsql security definer set search_path = public as
$$ declare d date := (now() at time zone 'America/Sao_Paulo')::date; atual int; total int;
begin
  if tipo_ not in ('pergunta','voz') then return jsonb_build_object('ok', false, 'motivo', 'tipo'); end if;
  perform pg_advisory_xact_lock(hashtext('usar_ia'));
  select coalesce(sum(n),0) into total from ia_uso where dia = d;
  if total >= max_geral then return jsonb_build_object('ok', false, 'motivo', 'geral'); end if;
  select n into atual from ia_uso where user_id = uid and dia = d and tipo = tipo_;
  if coalesce(atual,0) >= max_pessoa then return jsonb_build_object('ok', false, 'motivo', 'pessoa'); end if;
  insert into ia_uso (user_id, dia, tipo, n) values (uid, d, tipo_, 1)
    on conflict (user_id, dia, tipo) do update set n = ia_uso.n + 1;
  return jsonb_build_object('ok', true, 'restam', max_pessoa - coalesce(atual,0) - 1);
end $$;
revoke all on function public.usar_ia(uuid, text, int, int) from public, anon, authenticated;
grant execute on function public.usar_ia(uuid, text, int, int) to service_role;

-- devolve o uso quando a IA falhou (para a pessoa não perder a vez)
create or replace function public.devolver_ia(uid uuid, tipo_ text) returns void
language sql security definer set search_path = public as
$$ update ia_uso set n = greatest(n - 1, 0)
   where user_id = uid and dia = (now() at time zone 'America/Sao_Paulo')::date and tipo = tipo_ $$;
revoke all on function public.devolver_ia(uuid, text) from public, anon, authenticated;
grant execute on function public.devolver_ia(uuid, text) to service_role;
