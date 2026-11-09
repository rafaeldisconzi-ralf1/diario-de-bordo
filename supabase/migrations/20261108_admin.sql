-- Rafael vira administrador ao entrar pela primeira vez
create or replace function public.novo_usuario() returns trigger
language plpgsql security definer set search_path = public as
$$ begin
  insert into perfis (id, email, admin) values (new.id, new.email, lower(new.email) = 'rafaeldisconzi@gmail.com')
  on conflict (id) do nothing;
  return new;
end $$;
update perfis set admin = true where lower(email) = 'rafaeldisconzi@gmail.com';
