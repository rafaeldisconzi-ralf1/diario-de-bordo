# Gera index.html (render(t) quadro a quadro) e cues.json (efeitos sonoros) para a Parte 1.
import json, numpy as np
from ze_svg import ze_svg
W=json.load(open('words.json'))
env=json.load(open('/tmp/env.json'))['db'] if False else None
import os
dbf=json.load(open('env.json'))['db'] if os.path.exists('env.json') else json.load(open('/tmp/env.json'))['db']
db=np.array(dbf); mx=db.max()
FPS=30; TOT=36.6
mouth=''
for f in range(int(TOT*FPS)+2):
    t=f/FPS; a=int(max(0,(t-0.02)*100)); b=int((t+0.02)*100)+1
    v=db[a:b].mean() if a<len(db) else -99
    mouth+= '2' if v>mx-15 else ('1' if v>mx-27 else '0')
TRUCK='''<svg viewBox="0 0 300 140" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="18" width="172" height="84" rx="8" class="trl"/><rect x="10" y="62" width="172" height="10" fill="#f2b705" opacity=".85"/>
<path d="M188 44 L242 44 L278 80 L284 102 L188 102Z" fill="#f2b705"/><path d="M226 52 L248 52 L266 78 L226 78Z" fill="#2b4553"/><rect x="186" y="98" width="100" height="8" fill="#16181b"/>
<g fill="#16181b"><circle cx="48" cy="108" r="17"/><circle cx="88" cy="108" r="17"/><circle cx="126" cy="108" r="17"/><circle cx="216" cy="108" r="17"/><circle cx="256" cy="108" r="17"/></g>
<g fill="#8a8f98"><circle cx="48" cy="108" r="7"/><circle cx="88" cy="108" r="7"/><circle cx="126" cy="108" r="7"/><circle cx="216" cy="108" r="7"/><circle cx="256" cy="108" r="7"/></g></svg>'''
PHONE='''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><rect x="62" y="20" width="76" height="150" rx="16" fill="#16181b" stroke="#f4f3ee" stroke-width="7"/><rect x="72" y="36" width="56" height="104" rx="6" fill="#5fd39a"/><circle cx="100" cy="156" r="6" fill="#f4f3ee"/>
<path d="M30 64 Q16 100 30 136" stroke="#f2b705" stroke-width="8" fill="none" stroke-linecap="round"/><path d="M12 48 Q-8 100 12 152" stroke="#f2b705" stroke-width="8" fill="none" stroke-linecap="round"/>
<path d="M170 64 Q184 100 170 136" stroke="#f2b705" stroke-width="8" fill="none" stroke-linecap="round"/><path d="M188 48 Q208 100 188 152" stroke="#f2b705" stroke-width="8" fill="none" stroke-linecap="round"/></svg>'''
PUMP='''<svg viewBox="0 0 160 200" xmlns="http://www.w3.org/2000/svg"><rect x="14" y="20" width="84" height="160" rx="12" fill="#f4f3ee"/><rect x="28" y="36" width="56" height="40" rx="6" fill="#16181b"/><rect x="28" y="92" width="56" height="10" rx="3" fill="#f2b705"/>
<rect x="6" y="176" width="100" height="14" rx="5" fill="#8a8f98"/><path d="M98 54 L128 54 Q146 54 146 72 L146 140 Q146 156 132 156 Q120 156 120 144 L120 76 L98 76Z" fill="#16181b"/></svg>'''
CLOCK='''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><circle cx="100" cy="100" r="84" fill="#f4f3ee" stroke="#16181b" stroke-width="10"/><circle cx="100" cy="100" r="7" fill="#16181b"/>
<path id="hand" d="M100 100 L100 40" stroke="#16181b" stroke-width="10" stroke-linecap="round"/><path d="M100 100 L140 118" stroke="#f2b705" stroke-width="10" stroke-linecap="round"/></svg>'''
HTML=r'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>
@font-face{font-family:B;src:url(fonts/barlow-latin-700-normal.woff2);font-weight:700}
@font-face{font-family:B8;src:url(fonts/barlow-latin-800-normal.woff2);font-weight:800}
@font-face{font-family:BC;src:url(fonts/barlow-condensed-latin-800-normal.woff2);font-weight:800}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#14202e;font-family:B;color:#f4f3ee}
#sky{position:absolute;inset:0}
#sun{position:absolute;width:300px;height:300px;border-radius:50%;left:640px;top:880px}
.hl{position:absolute;left:0;width:4320px;height:420px}
#cloud1,#cloud2{position:absolute;height:70px;border-radius:70px;background:rgba(244,243,238,.16)}
#ze{position:absolute;left:260px;top:800px;width:560px;height:728px;transform-origin:50% 90%}
#ze svg{width:100%;height:100%}
.abs{position:absolute;opacity:0;transform-origin:50% 50%}
.box{background:#16181b;border-radius:40px;box-shadow:0 20px 0 rgba(0,0,0,.3)}
.yel{color:#f2b705}.grn{color:#5fd39a}
.big{font:800 168px/.92 BC;text-transform:uppercase;text-align:center}
.mid{white-space:nowrap;font:800 100px/1 BC;text-transform:uppercase}
.sm{font:700 44px/1.1 B;text-transform:uppercase;letter-spacing:1px}
.badge{flex-shrink:0;width:168px;height:168px;border-radius:34px;background:#f2b705;color:#16181b;font:800 150px/1 BC;display:flex;align-items:center;justify-content:center;padding-top:10px}
.trl{fill:#e8e3d6}.empty .trl{fill:#2b3138;stroke:#8a8f98;stroke-width:4;stroke-dasharray:14 10}
#wm{position:absolute;font:700 38px B;color:#fff;opacity:.78;letter-spacing:1px;text-shadow:0 2px 6px rgba(0,0,0,.5);z-index:50}
#subs{position:absolute;left:40px;right:40px;top:1462px;text-align:center;z-index:40}
#subs .g{position:absolute;left:0;right:0;top:0;opacity:0}
#subs span.w{display:inline-block;margin:0 14px;font:800 104px/1.05 BC;text-transform:uppercase;color:#f4f3ee;
 -webkit-text-stroke:0;text-shadow:0 0 0 #000,0 6px 0 rgba(0,0,0,.55),0 0 18px rgba(0,0,0,.6);background:rgba(22,24,27,.0)}
#subs span.w.on{color:#f2b705}
.rule{width:880px;height:190px;background:#f2b705;color:#16181b;border-radius:30px;box-shadow:0 18px 0 rgba(0,0,0,.3);padding:18px 34px;display:flex;align-items:center;gap:30px}
.rule .n{font:800 70px/1 BC;text-transform:uppercase;writing-mode:horizontal-tb;background:#16181b;color:#f2b705;padding:16px 22px 8px;border-radius:18px;white-space:nowrap}
.rule .t{font:800 74px/.98 BC;text-transform:uppercase}
.row{display:flex;align-items:center;gap:26px}
.ab{width:430px;height:290px;border-radius:36px;background:#16181b;box-shadow:0 20px 0 rgba(0,0,0,.3);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px}
.ab .badge{width:120px;height:120px;font-size:108px;border-radius:26px}
.ab .v{font:800 84px/1 BC}.ab .s{font:700 36px/1.1 B;text-transform:uppercase;letter-spacing:1px;color:#c9c5ba}
.pill{background:#f2b705;color:#16181b;font:800 108px/1 BC;text-transform:uppercase;padding:26px 60px 14px;border-radius:999px;box-shadow:0 16px 0 rgba(0,0,0,.3);white-space:nowrap}
</style></head><body>
<div id="sky"></div><div id="sun"></div>

<svg class="hl" id="h1" style="top:1040px" viewBox="0 0 4320 420"><defs><pattern id="p1" width="720" height="420" patternUnits="userSpaceOnUse"><path d="M0 220 C120 120 260 120 360 210 C460 300 600 290 720 220 L720 420 L0 420Z" fill="#26404a"/></pattern></defs><rect width="4320" height="420" fill="url(#p1)"/></svg>
<svg class="hl" id="h2" style="top:1150px" viewBox="0 0 4320 420"><defs><pattern id="p2" width="540" height="420" patternUnits="userSpaceOnUse"><path d="M0 170 C90 100 190 100 270 160 C350 220 450 220 540 170 L540 420 L0 420Z" fill="#1a2c33"/></pattern></defs><rect width="4320" height="420" fill="url(#p2)"/></svg>
<svg class="hl" id="h3" style="top:1290px" viewBox="0 0 4320 420"><defs><pattern id="p3" width="900" height="420" patternUnits="userSpaceOnUse"><path d="M0 120 C150 60 330 60 450 110 C570 160 750 160 900 120 L900 420 L0 420Z" fill="#101d22"/></pattern></defs><rect width="4320" height="420" fill="url(#p3)"/></svg>
<div style="position:absolute;left:0;right:0;top:1600px;bottom:0;background:#101d22"></div><div id="wm">@appdiariodebordo</div>

<!-- 1 gancho -->
<div class="abs" id="hook1" style="left:40px;width:1000px;top:250px"><div class="big" style="font-size:150px">Tu é<br><span class="yel">caminhoneiro?</span></div></div>
<div class="abs" id="hook2" style="left:90px;width:900px;top:640px;text-align:center"><div class="pill" style="font-size:80px;padding:20px 44px 10px;display:inline-block">Então me ajuda nessa</div></div>
<!-- 2 nome -->
<div class="abs" id="name" style="left:90px;width:900px;top:290px;text-align:center"><div class="big" style="font-size:300px">ZÉ</div><div class="pill" style="font-size:78px;padding:20px 44px 10px;display:inline-block;margin-top:10px">Caminhoneiro autônomo</div></div>
<!-- 3 carreta -->
<div class="abs box" id="truck" style="left:70px;width:940px;top:250px;height:430px;padding:34px 50px">
 <div class="sm yel" style="font-size:52px">Carreta · viagem de</div>
 <div class="mid" style="font-size:210px;line-height:1.05"><span id="km">0</span> <span style="font-size:110px">km</span></div>
 <div id="truckic" style="position:absolute;left:50px;bottom:24px;width:300px">__TRUCK__</div></div>
<!-- 4 propostas -->
<div class="abs box" id="prop" style="left:70px;width:940px;top:250px;height:430px;display:flex;align-items:center;justify-content:center;gap:40px">
 <div id="phone" style="width:230px;height:230px">__PHONE__</div>
 <div><div class="sm" style="font-size:50px;color:#c9c5ba">Ligaram pra ele</div><div class="mid" style="font-size:150px;line-height:1"><span class="yel">2</span> propostas</div></div></div>
<!-- 5 proposta A -->
<div class="abs box" id="cA" style="left:70px;width:940px;top:250px;height:440px;padding:34px 44px">
 <div class="row"><div class="badge">A</div><div><div class="mid" style="font-size:150px;line-height:1">R$ <span id="vA">0</span></div><div class="sm" style="font-size:46px;color:#c9c5ba">Ida · carga cheia</div></div></div>
 <div class="row" id="rowA2" style="margin-top:24px;opacity:0"><div id="emptyT" class="empty" style="width:230px">__TRUCK__</div><div><div class="mid" style="font-size:96px;line-height:1">Volta <span class="yel">vazia</span></div><div class="sm" style="font-size:42px;color:#c9c5ba">sem frete na volta</div></div></div></div>
<!-- regra 1 -->
<div class="abs rule" id="r1" style="left:100px;top:716px"><div class="n">REGRA 1</div><div class="t">Volta vazia perde metade da viagem</div></div>
<!-- 6 proposta B -->
<div class="abs box" id="cB" style="left:70px;width:940px;top:250px;height:450px;padding:30px 44px">
 <div class="row" style="align-items:flex-start"><div class="badge">B</div><div style="flex:1">
  <div class="row" id="b1" style="opacity:0;justify-content:space-between"><div class="sm" style="font-size:38px;color:#c9c5ba;white-space:nowrap">Ida · carga cheia</div><div class="mid" style="font-size:96px">R$ <span id="vB1">0</span></div></div>
  <div class="row" id="b2" style="opacity:0;justify-content:space-between;margin-top:8px"><div class="sm" style="font-size:38px;color:#c9c5ba;white-space:nowrap">Volta · carga cheia</div><div class="mid" style="font-size:100px">+ R$ <span id="vB2">0</span></div></div>
  <div class="row" id="b3" style="opacity:0;justify-content:space-between;margin-top:14px;border-top:6px solid #f2b705;padding-top:12px"><div class="sm yel" style="font-size:50px">No total</div><div class="mid" style="font-size:124px">R$ <span id="vB3">0</span></div></div>
 </div></div></div>
<!-- 7 espera -->
<div class="abs box" id="wait" style="left:70px;width:940px;top:250px;height:440px;padding:30px 44px">
 <div class="sm yel" style="font-size:48px">Carga da volta pronta só em</div>
 <div class="row" style="margin-top:10px"><div id="clock" style="width:170px;height:170px">__CLOCK__</div><div class="mid" style="font-size:190px;line-height:1"><span id="dias">0</span> <span style="font-size:110px">dias</span></div></div>
 <div class="row" style="margin-top:20px;gap:20px"><div id="d1" class="pill" style="font-size:62px;padding:16px 36px 8px;opacity:0;background:#2b3138;color:#f4f3ee;box-shadow:none">Dia 1 · parado</div><div id="d2" class="pill" style="font-size:62px;padding:16px 36px 8px;opacity:0;background:#2b3138;color:#f4f3ee;box-shadow:none">Dia 2 · parado</div></div></div>
<!-- 8 diesel -->
<div class="abs box" id="dsl" style="left:70px;width:940px;top:250px;height:430px;padding:34px 50px;display:flex;align-items:center;gap:44px">
 <div id="pump" style="width:190px;height:240px">__PUMP__</div>
 <div><div class="sm yel" style="font-size:52px">Diesel · litro</div><div class="mid" style="font-size:190px;line-height:1">R$ <span id="dv">0,00</span></div><div class="sm" style="font-size:34px;color:#c9c5ba">perto de sete reais · média do Brasil</div></div></div>
<!-- regra 2 -->
<div class="abs rule" id="r2" style="left:100px;top:716px"><div class="n">REGRA 2</div><div class="t">Parado também se gasta</div></div>
<!-- 9 pergunta final -->
<div class="abs" id="q" style="left:60px;width:960px;top:236px;text-align:center"><div class="big" style="font-size:112px;line-height:1">Qual deixa mais<br><span class="yel">dinheiro</span> no bolso?</div></div>
<div class="abs" id="cta" style="left:60px;width:960px;top:262px;text-align:center"><div class="pill" style="display:inline-block">Comente A ou B</div></div>
<div class="abs" id="fa" style="left:60px;top:500px"><div class="ab"><div class="badge">A</div><div class="v">R$ 8.000</div><div class="s">volta vazia</div></div></div>
<div class="abs" id="fb" style="left:590px;top:500px"><div class="ab"><div class="badge">B</div><div class="v">R$ 9.000</div><div class="s">espera de 2 dias</div></div></div>
<div class="abs" id="tz" style="left:60px;width:960px;top:812px;text-align:center"><div class="sm" style="white-space:nowrap;font-size:38px;background:#16181b;display:inline-block;padding:14px 34px 8px;border-radius:999px;color:#f4f3ee">Parte 2 amanhã: a conta no <span class="yel">Diário de Bordo</span></div></div>
<div class="abs" id="ex" style="left:60px;width:960px;top:196px;text-align:center;font:700 30px B;color:#c9c5ba;text-transform:uppercase;letter-spacing:2px">números de exemplo</div>

<div id="ze">__ZE__</div>
<div id="subs"></div>
<script>
const TOT=__TOT__, WORDS=__WORDS__, MOUTH="__MOUTH__";
const $=s=>document.querySelector(s);
const cl=x=>Math.max(0,Math.min(1,x)), eo=x=>1-Math.pow(1-cl(x),3), eio=x=>{x=cl(x);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2};
const back=x=>{x=cl(x);const c=1.6;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
const ws=i=>WORDS[i].start, we=i=>WORDS[i].end;
const fmt=n=>String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g,'.');
// cartões: [id, início, fim]
const C=[['hook1',0,we(6)+.25],['hook2',ws(3),we(6)+.25],['name',ws(7)-.05,we(10)+.4],['truck',ws(11)-.05,we(15)+.3],['prop',ws(16)-.05,we(21)+.3],
 ['cA',ws(22),we(35)+.45],['r1',ws(31)-.05,we(35)+.5],['cB',ws(36),we(50)+.3],['wait',ws(51),we(63)+.3],['dsl',ws(64)-.05,we(72)+.3],['r2',ws(73)-.05,we(77)+.35],
 ['q',ws(78),ws(89)-.1],['fa',ws(78)+.3,TOT],['fb',ws(78)+.5,TOT],['cta',ws(89)-.05,TOT],['tz',ws(93)-.1,TOT],['ex',ws(36),TOT]];
const EXPR=[[0,'calm'],[ws(16),'happy'],[ws(22),'calm'],[ws(31),'worried'],[ws(36),'calm'],[ws(51),'worried'],[ws(64),'calm'],[ws(73),'shock'],[ws(78),'calm']];
const BLINK=[1.9,4.9,8.4,11.3,15.0,18.6,22.2,26.4,30.1,33.4];
// legenda: grupos de até 4 palavras
const G=[];(function(){let g=[];WORDS.forEach((w,i)=>{g.push(i);const last=/[.?:,]$/.test(w.text)||g.length>=4||g.join('').length>14&&g.length>=3;if(last){G.push(g);g=[]}});if(g.length)G.push(g)})();
const cap=$('#subs');G.forEach((g,gi)=>{const d=document.createElement('div');d.className='g';d.innerHTML=g.map(i=>'<span class="w" data-i="'+i+'">'+WORDS[i].text.replace(/[,]$/,'')+'</span>').join(' ');cap.appendChild(d)});
const GT=G.map((g,gi)=>{const s=ws(g[0])-.04;const ne=gi+1<G.length?ws(G[gi+1][0])-.04:TOT;const e=Math.min(we(g[g.length-1])+.25,ne);return [s,e]});
const SKY=[[0,'#18273a','#34516a','#d98a3a'],[19.3,'#101b2a','#1f3347','#4a6a82'],[28,'#14202e','#14202e','#1d2f3d']];
const lerp=(a,b,t)=>a+(b-a)*t;
function hex(c){return [1,3,5].map(i=>parseInt(c.substr(i,2),16))}
function mix(a,b,t){const A=hex(a),B=hex(b);return 'rgb('+A.map((v,i)=>Math.round(lerp(v,B[i],t))).join(',')+')'}
function skyAt(t){let i=0;while(i<SKY.length-1&&t>=SKY[i+1][0])i++;const a=SKY[i],b=SKY[Math.min(i+1,SKY.length-1)];const k=i<SKY.length-1?eio((t-a[0])/(b[0]+(i==0?0:0)-a[0]>0?Math.min(2.5,(b[0]-a[0]))/1:1)):0;
 const kk=i<SKY.length-1?cl((t-b[0]+2.5)/2.5):0;return [mix(a[1],b[1],kk),mix(a[2],b[2],kk),mix(a[3],b[3],kk)]}
const COUNT={km:[ws(12),we(13)+.1,1000,'#km',n=>fmt(n)],vA:[ws(24),we(26),8000,'#vA',n=>fmt(n)],vB1:[ws(38),we(39),6000,'#vB1',n=>fmt(n)],vB2:[ws(43),we(44),3000,'#vB2',n=>fmt(n)],vB3:[ws(47),we(48)+.15,9000,'#vB3',n=>fmt(n)]};
window.render=function(t){
 const [c1,c2,c3]=skyAt(t);$('#sky').style.background='linear-gradient(180deg,'+c1+' 0%,'+c2+' 55%,'+c3+' 78%,'+c3+' 100%)';
 const night=cl((t-19)/2.5)*(1-cl((t-27.5)/1.5)*0);
 const s=$('#sun');s.style.background=mix('#f2b705','#e8ecef',night);s.style.opacity=.9-.25*night;s.style.top=(1000+night*20)+'px';s.style.left=(700-t*3)+'px';

 $('#h1').style.transform='translateX('+(-(t*18)%720)+'px)';$('#h2').style.transform='translateX('+(-(t*34)%540)+'px)';$('#h3').style.transform='translateX('+(-(t*60)%900)+'px)';
 // marca d'água
 const wm=$('#wm');const pos=Math.floor(t/8)%2;wm.style.top='150px';wm.style.left=pos?'auto':'48px';wm.style.right=pos?'48px':'auto';
 // Zé
 let ex='calm';EXPR.forEach(e=>{if(t>=e[0])ex=e[1]});
 ['calm','worried','shock','happy'].forEach(k=>{$('#ex_'+k).style.display=k==ex?'':'none';});
 const f=Math.min(MOUTH.length-1,Math.round(t*30));const m=+MOUTH[f];
 ['calm','worried','shock','happy'].forEach(k=>{$('#mo_'+k).style.display=(k==ex&&m==0)?'':'none'});
 $('#sp1').style.display=m==1?'':'none';$('#sp2').style.display=m==2?'':'none';
 let bl=false;BLINK.forEach(b=>{if(t>=b&&t<b+.13)bl=true});$('#blink').style.display=bl?'':'none';
 const ze=$('#ze');const nod=(m>0?1:0);ze.style.transform='translateY('+(Math.sin(t*2.3)*5-(m>1?4:0))+'px) rotate('+(Math.sin(t*1.4)*1.1)+'deg) scale('+(1+0.012*Math.sin(t*3.1))+')';
 // cartões
 C.forEach(([id,a,b])=>{const el=document.getElementById(id);let o=0,sc=1,ty=0;
  if(t>=a&&t<=b){const i=cl((t-a)/.3),ou=cl((b-t)/.22);o=Math.min(1,i*3)*Math.min(1,ou*3+(b>=TOT-.01?1:0));sc=(0.82+0.18*back((t-a)/.38));ty=(1-eo((t-a)/.3))*40;if(id=='hook1'&&t<.2){o=1;sc=.94+.06*back(t/.2);ty=0}
   if(/^r/.test(id)){sc=1+.1*Math.max(0,1-(t-a)/.15)}}
  el.style.opacity=o;el.style.transform='translateY('+ty+'px) scale('+sc+')'});
 // contadores
 for(const k in COUNT){const [a,b,v,sel,fn]=COUNT[k];$(sel).textContent=fn(v*eio((t-a)/(b-a)))}
 $('#dv').textContent=(7*eio((t-ws(67))/(we(69)-ws(67)))).toFixed(2).replace('.',',');
 $('#dias').textContent=Math.round(2*eio((t-ws(60))/(we(63)-ws(60))));
 $('#rowA2').style.opacity=eo((t-ws(33)+.2)/.3);
 [['b1',ws(38)-.1],['b2',ws(43)-.1],['b3',ws(47)-.1],['d1',ws(58)],['d2',ws(62)-.05]].forEach(([id,a])=>{const e=$('#'+id);const k=eo((t-a)/.25);e.style.opacity=k;e.style.transform='translateX('+((1-k)*60)+'px)'});
 $('#truckic').style.transform='translateX('+(eo((t-ws(11))/1.8)*560)+'px)';
 $('#phone').style.transform='rotate('+(Math.sin(t*38)*(t>ws(16)&&t<we(21)?7:0))+'deg)';
 $('#clock').querySelector('#hand').style.transform='rotate('+((t-ws(51))*220)+'deg)';$('#clock').querySelector('#hand').style.transformOrigin='100px 100px';
 // legenda
 const gs=cap.children;for(let gi=0;gi<G.length;gi++){const el=gs[gi],[a,b]=GT[gi];const on=t>=a&&t<=b;el.style.opacity=on?1:0;if(on){el.style.transform='scale('+(0.92+0.08*back((t-a)/.15))+')';el.querySelectorAll('span.w').forEach(sp=>{const i=+sp.dataset.i;sp.className='w'+(t>=ws(i)-.02&&t<we(i)+.04?' on':'')})}}
};
window.render(0);
</script></body></html>'''
HTML=(HTML.replace('__TRUCK__',TRUCK).replace('__PHONE__',PHONE).replace('__PUMP__',PUMP).replace('__CLOCK__',CLOCK).replace('__ZE__',ze_svg())
 .replace('__TOT__',str(TOT)).replace('__WORDS__',json.dumps(W,ensure_ascii=False)).replace('__MOUTH__',mouth))
open('index.html','w').write(HTML)
def ws(i): return W[i]['start']
def we(i): return W[i]['end']
cues=[]
for a in [0.02,ws(3),ws(7)-.05,ws(11)-.05,ws(22),ws(36),ws(51),ws(64),ws(78),ws(78)+.3,ws(78)+.5,ws(93)-.1]: cues.append(dict(t=round(a,3),k='whoosh'))
cues.append(dict(t=round(ws(16)-.05,3),k='ring'))
for a in [ws(31)-.05,ws(73)-.05]: cues.append(dict(t=round(a,3),k='slam'))
for a,b in [(ws(12),we(13)+.1),(ws(24),we(26)),(ws(38),we(39)),(ws(43),we(44)),(ws(47),we(50))]:
    n=int((b-a)/0.07)
    for k in range(n): cues.append(dict(t=round(a+k*0.07,3),k='tick'))
for a in [ws(22),ws(36)]: cues.append(dict(t=round(a,3),k='pop'))
cues.append(dict(t=round(we(50)+.05,3),k='ding')); cues.append(dict(t=round(ws(89)-.05,3),k='ding'))
cues.append(dict(t=round(ws(63)+.05,3),k='thud'))
json.dump(cues,open('cues.json','w'))
print('ok',len(HTML)//1024,'KB',len(cues),'efeitos')
