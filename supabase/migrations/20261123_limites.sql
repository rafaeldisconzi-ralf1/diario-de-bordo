-- Limites contra abuso (achados 3 e 4 da revisão de 23/11/2026; ver docs/seguranca.md)

-- 3) Relatório por e-mail: reserva o envio ANTES de mandar, de forma atômica
--    (várias chamadas juntas não passam do limite) e com um teto geral por hora,
--    porque o mesmo e-mail nao-responda@ também manda os códigos de login.
create or replace function public.reservar_relatorio(uid uuid, mes_ text, max_dia int, max_hora_geral int)
returns jsonb language plpgsql security definer set search_path = public as
$$ declare novo bigint; begin
  perform pg_advisory_xact_lock(hashtext('reservar_relatorio'));
  if (select count(*) from relatorios_enviados where user_id = uid and enviado_em > now() - interval '24 hours') >= max_dia
    then return jsonb_build_object('ok', false, 'motivo', 'dia'); end if;
  if (select count(*) from relatorios_enviados where enviado_em > now() - interval '1 hour') >= max_hora_geral
    then return jsonb_build_object('ok', false, 'motivo', 'geral'); end if;
  insert into relatorios_enviados (user_id, mes) values (uid, mes_) returning id into novo;
  return jsonb_build_object('ok', true, 'id', novo);
end $$;
revoke all on function public.reservar_relatorio(uuid, text, int, int) from public, anon, authenticated;
grant execute on function public.reservar_relatorio(uuid, text, int, int) to service_role;

create or replace function public.cancelar_relatorio(rid bigint) returns void
language sql security definer set search_path = public as
$$ delete from relatorios_enviados where id = rid $$;
revoke all on function public.cancelar_relatorio(bigint) from public, anon, authenticated;
grant execute on function public.cancelar_relatorio(bigint) to service_role;

-- 4) Criar cobrança / consultar status: limite por IP numa janela de minutos
create table if not exists public.limite_cobranca (
  ip text not null,
  acao text not null,
  em timestamptz not null default now()
);
create index if not exists limite_cobranca_ip on public.limite_cobranca (ip, acao, em);
alter table public.limite_cobranca enable row level security;
revoke all on public.limite_cobranca from anon, authenticated;

create or replace function public.limitar_cobranca(ip_ text, acao_ text, max_ int, janela_min int)
returns boolean language plpgsql security definer set search_path = public as
$$ begin
  perform pg_advisory_xact_lock(hashtext(ip_ || '|' || acao_));
  if (select count(*) from limite_cobranca where ip = ip_ and acao = acao_ and em > now() - make_interval(mins => janela_min)) >= max_
    then return false; end if;
  insert into limite_cobranca (ip, acao) values (ip_, acao_);
  if random() < 0.02 then delete from limite_cobranca where em < now() - interval '1 day'; end if;
  return true;
end $$;
revoke all on function public.limitar_cobranca(text, text, int, int) from public, anon, authenticated;
grant execute on function public.limitar_cobranca(text, text, int, int) to service_role;
