-- Correções da revisão de segurança de 23/11/2026 (ver docs/seguranca.md)

-- 1) Um pagamento não pode ser somado duas vezes quando duas confirmações chegam juntas.
--    "for update" faz a segunda confirmação esperar a primeira e depois pular o pagamento já aplicado.
--    (Testado: 8 confirmações simultâneas dão 30 dias, não até 240.)
create or replace function public.aplicar_pagamentos(alvo_email text) returns void
language plpgsql security definer set search_path = public as
$$ declare p record; uid uuid; begin
  select id into uid from perfis where lower(email) = lower(alvo_email) limit 1;
  if uid is null then return; end if;
  for p in select * from pagamentos
           where lower(email) = lower(alvo_email) and status = 'approved' and not aplicado
           order by aprovado_em nulls last
           for update loop
    update perfis set pago_ate = greatest(coalesce(pago_ate, current_date), current_date) + p.dias where id = uid;
    update pagamentos set aplicado = true where id = p.id;
  end loop;
end $$;
revoke all on function public.aplicar_pagamentos(text) from public, anon, authenticated;
grant execute on function public.aplicar_pagamentos(text) to service_role;

-- 2) Aviso (push) só para os serviços de notificação conhecidos.
--    "not valid": não mexe nas inscrições que já existem, vale para as novas.
alter table public.push_inscricoes drop constraint if exists push_endereco_conhecido;
alter table public.push_inscricoes add constraint push_endereco_conhecido check (
  endpoint ~ '^https://(fcm\.googleapis\.com|updates\.push\.services\.mozilla\.com|web\.push\.apple\.com|[a-z0-9-]+\.notify\.windows\.com)/'
) not valid;
