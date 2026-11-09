// Faz o app abrir sem sinal na estrada. Os dados do motorista ficam no celular (localStorage), não aqui.
const CACHE='bordo-v4';
const BASE=['/','/index.html','/manifest.json','/icon-32.png','/icon-180.png','/icon-192.png','/icon-512.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(BASE)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{
  const r=e.request;if(r.method!=='GET')return;
  const u=new URL(r.url);
  // Página do app: tenta a versão nova primeiro; sem sinal, usa a guardada.
  if(r.mode==='navigate'){
    // cada endereço guarda a própria página (/ e /nuvem/ não se misturam)
    const chave=u.pathname.startsWith('/nuvem')?'/nuvem/':'/';
    e.respondWith(fetch(r).then(res=>{if(res.ok){const cp=res.clone();caches.open(CACHE).then(c=>c.put(chave,cp))}return res}).catch(()=>caches.match(chave).then(h=>h||caches.match('/'))));
    return;
  }
  // Ícones, manifesto e fontes: usa o guardado e atualiza por trás.
  if(u.origin===location.origin||/fonts\.(googleapis|gstatic)\.com$/.test(u.hostname)){
    e.respondWith(caches.match(r).then(hit=>{const net=fetch(r).then(res=>{if(res.ok||res.type==='opaque'){const cp=res.clone();caches.open(CACHE).then(c=>c.put(r,cp))}return res}).catch(()=>hit);return hit||net}));
  }
});
// Notificações: mostra o aviso e, ao tocar, abre o app.
self.addEventListener('push',e=>{
  let d={};try{d=e.data?e.data.json():{}}catch(x){d={texto:e.data&&e.data.text()}}
  e.waitUntil(self.registration.showNotification(d.titulo||'Diário de Bordo',{body:d.texto||'',icon:'/icon-192.png',badge:'/icon-192.png',data:{url:d.url||'/nuvem/'},lang:'pt-BR'}));
});
self.addEventListener('notificationclick',e=>{
  e.notification.close();
  const alvo=new URL((e.notification.data&&e.notification.data.url)||'/nuvem/',location.origin).href;
  e.waitUntil(clients.matchAll({type:'window',includeUncontrolled:true}).then(ws=>{
    for(const w of ws){if(w.url.split('#')[0]===alvo.split('#')[0]&&'focus' in w)return w.focus()}
    return clients.openWindow(alvo);
  }));
});
