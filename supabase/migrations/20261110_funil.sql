-- Funil da página de vendas: visitas → tocou em Assinar → gerou Pix / abriu cartão → pagou
-- Não guarda nome, e-mail nem IP: só o tipo, a origem (instagram, whatsapp…) e um código aleatório do navegador.
create table if not exists public.eventos (
  id bigserial primary key,
  criado_em timestamptz not null default now(),
  tipo text not null check (tipo in ('visita','assinar','pix','cartao')),
  origem text not null default 'direto' check (length(origem) <= 20),
  visitante text check (length(visitante) <= 40)
);
alter table public.eventos enable row level security;
revoke all on public.eventos from anon, authenticated;
create index if not exists eventos_quando on public.eventos (criado_em);
create index if not exists eventos_visitante on public.eventos (visitante, tipo, criado_em);

-- a página de vendas chama esta função (sem login). Conta cada visitante 1 vez a cada 12 h por tipo.
create or replace function public.registrar_evento(p_tipo text, p_origem text, p_visitante text) returns void
language plpgsql security definer set search_path = public as
$$ declare v text := left(coalesce(p_visitante,''), 40);
begin
  if p_tipo not in ('visita','assinar','pix','cartao') or v = '' then return; end if;
  if exists (select 1 from eventos where visitante = v and tipo = p_tipo and criado_em > now() - interval '12 hours') then return; end if;
  insert into eventos (tipo, origem, visitante)
  values (p_tipo, left(lower(coalesce(nullif(trim(p_origem),''),'direto')), 20), v);
end $$;
revoke all on function public.registrar_evento(text,text,text) from public;
grant execute on function public.registrar_evento(text,text,text) to anon, authenticated;

-- resumo para o admin. dias = 0 → hoje (desde meia-noite de Brasília)
create or replace function public.resumo_funil(dias int) returns json
language plpgsql stable security definer set search_path = public as
$$ declare desde timestamptz; r json;
begin
  if not eh_admin() then raise exception 'Somente o administrador'; end if;
  -- o contador começou em 10/11/2026 22h (Brasília); antes disso só houve testes
  desde := case when dias <= 0 then (date_trunc('day', now() at time zone 'America/Sao_Paulo') at time zone 'America/Sao_Paulo')
                else now() - make_interval(days => dias) end;
  desde := greatest(desde, '2026-11-11 01:00:00+00'::timestamptz);
  select json_build_object(
    'visitas', count(*) filter (where tipo = 'visita'),
    'assinar', count(*) filter (where tipo = 'assinar'),
    'pix',     count(*) filter (where tipo = 'pix'),
    'cartao',  count(*) filter (where tipo = 'cartao'),
    'pagos', (select count(*) from pagamentos p where p.status = 'approved' and p.valor > 0 and p.aprovado_em >= desde
               and lower(p.email) <> 'nao-responda@trilhanova.shop'
               and lower(p.email) not in (select lower(email) from perfis where admin)),
    'nao_pagos', (select count(*) from pagamentos p where p.status <> 'approved' and p.criado_em >= desde
               and lower(p.email) not in (select lower(email) from perfis where admin)),
    'origens', (select coalesce(json_agg(json_build_object('origem', origem, 'n', n) order by n desc), '[]'::json)
                from (select origem, count(*) n from eventos where tipo = 'visita' and criado_em >= desde group by origem) o)
  ) into r from eventos where criado_em >= desde;
  return r;
end $$;
revoke all on function public.resumo_funil(int) from public, anon;
grant execute on function public.resumo_funil(int) to authenticated;
