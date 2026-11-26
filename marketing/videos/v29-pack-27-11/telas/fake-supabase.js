(function(){
 const user={id:'u-carlos',email:'carlos@exemplo.com'};
 const session={access_token:'fake',user};
 const perfil={id:'u-carlos',email:'carlos@exemplo.com',admin:true,nome:'Carlos',modelo:'Scania R 450',placa:'ABC 1D23',ano:'2021',patrao:'',teste_ate:null,pago_ate:'2027-12-31',visto_em:null,criado_em:'2026-10-01'};
 function q(table){const b={_t:table,select(){return b},order(){return b},limit(){return b},gt(){return b},eq(){return b},delete(){return b},
   update(){return b},upsert(){return Promise.resolve({error:null})},maybeSingle(){return Promise.resolve({data:table==='perfis'?perfil:null,error:null})},
   then(ok,er){return Promise.resolve({data:table==='perfis'?[perfil]:[],error:null}).then(ok,er)}};return b}
 window.supabase={createClient(){return {auth:{getSession:async()=>({data:{session}}),onAuthStateChange(){return {data:{subscription:{unsubscribe(){}}}}},
   signInWithOtp:async()=>({error:null}),verifyOtp:async()=>({data:{session},error:null}),signOut:async()=>({error:null})},
   from:q,rpc:async()=>({data:[],error:null})}}};
})();
