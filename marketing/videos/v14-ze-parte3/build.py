# Gera index.html (render(t) quadro a quadro) e cues.json (efeitos sonoros) para a Parte 1.
import json, numpy as np
from ze_svg import ze_svg
W=json.load(open('words.json'))
env=json.load(open('/tmp/env.json'))['db'] if False else None
import os
dbf=json.load(open('env.json'))['db'] if os.path.exists('env.json') else json.load(open('/tmp/env.json'))['db']
db=np.array(dbf); mx=db.max()
FPS=30; TOT=20.6
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
#ze{position:absolute;left:260px;top:850px;width:560px;height:728px;transform-origin:50% 90%}
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
.cd{width:470px;height:480px;border-radius:38px;background:#16181b;box-shadow:0 20px 0 rgba(0,0,0,.3);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;padding:18px 14px;outline:0 solid #f2b705}
.cd .badge{width:110px;height:110px;font-size:100px;border-radius:24px;margin-bottom:6px}
.cd .lab{font:700 38px B;text-transform:uppercase;letter-spacing:1px;color:#c9c5ba;text-align:center}
.cd .val{font:800 126px/1 BC;white-space:nowrap}
.cd .sub{font:700 40px/1.1 B;text-transform:uppercase;color:#c9c5ba;text-align:center}
.cd .tot{font:800 62px/1 BC;text-transform:uppercase;margin-top:12px;opacity:0;border-top:6px solid #f2b705;padding-top:12px;width:100%;text-align:center}
</style></head><body>
<div id="sky"></div><div id="sun"></div>

<svg class="hl" id="h1" style="top:1040px" viewBox="0 0 4320 420"><defs><pattern id="p1" width="720" height="420" patternUnits="userSpaceOnUse"><path d="M0 220 C120 120 260 120 360 210 C460 300 600 290 720 220 L720 420 L0 420Z" fill="#26404a"/></pattern></defs><rect width="4320" height="420" fill="url(#p1)"/></svg>
<svg class="hl" id="h2" style="top:1150px" viewBox="0 0 4320 420"><defs><pattern id="p2" width="540" height="420" patternUnits="userSpaceOnUse"><path d="M0 170 C90 100 190 100 270 160 C350 220 450 220 540 170 L540 420 L0 420Z" fill="#1a2c33"/></pattern></defs><rect width="4320" height="420" fill="url(#p2)"/></svg>
<svg class="hl" id="h3" style="top:1290px" viewBox="0 0 4320 420"><defs><pattern id="p3" width="900" height="420" patternUnits="userSpaceOnUse"><path d="M0 120 C150 60 330 60 450 110 C570 160 750 160 900 120 L900 420 L0 420Z" fill="#101d22"/></pattern></defs><rect width="4320" height="420" fill="url(#p3)"/></svg>
<div style="position:absolute;left:0;right:0;top:1600px;bottom:0;background:#101d22"></div><div id="wm">@appdiariodebordo</div>

<!-- cartões -->
<div class="abs" id="ex" style="left:40px;width:1000px;top:196px;text-align:center;font:700 30px B;color:#c9c5ba;text-transform:uppercase;letter-spacing:2px">números de exemplo</div>
<div class="abs" id="title" style="left:40px;width:1000px;top:260px;text-align:center"><div class="big" style="font-size:132px;line-height:1"><span class="yel">Fixo</span> ou <span class="yel">comissão?</span></div></div>
<div class="abs" id="ban" style="left:40px;width:1000px;top:250px;text-align:center"><div class="pill" style="font-size:72px;padding:22px 40px 12px;display:inline-block">O Zé é motorista empregado</div></div>
<div class="abs" id="q" style="left:40px;width:1000px;top:236px;text-align:center"><div class="big" style="font-size:150px;line-height:1">Qual paga <span class="yel">mais?</span></div></div>
<div class="abs" id="cta" style="left:40px;width:1000px;top:262px;text-align:center"><div class="pill" style="display:inline-block">Comente A ou B</div></div>
<div class="abs" id="tz" style="left:40px;width:1000px;top:270px;text-align:center"><div class="pill" style="display:inline-block;font-size:86px;background:#16181b;color:#f4f3ee;box-shadow:0 16px 0 rgba(0,0,0,.3)">Amanhã: <span class="yel">a conta</span></div></div>
<div class="abs cd" id="cA" style="left:50px;top:430px"><div class="badge">A</div><div class="lab">Salário fixo</div><div class="val">R$ <span id="vA">4.500</span></div><div class="sub">todo mês</div><div class="tot" id="tA">no mês: <span class="yel">R$ ?</span></div></div>
<div class="abs cd" id="cB" style="left:560px;top:430px"><div class="badge">B</div><div class="lab">Base + comissão</div><div class="val">R$ 2.700</div><div class="sub yel" style="font-size:54px;font-weight:800;font-family:BC;white-space:nowrap">+ 6% de cada frete</div><div class="tot" id="tB">no mês: <span class="yel">R$ ?</span></div></div>

<div id="ze">__ZE__</div>
<div id="subs"></div>
<script>
const TOT=__TOT__, WORDS=__WORDS__, MOUTH="__MOUTH__";
const $=s=>document.querySelector(s);
const cl=x=>Math.max(0,Math.min(1,x)), eo=x=>1-Math.pow(1-cl(x),3), eio=x=>{x=cl(x);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2};
const back=x=>{x=cl(x);const c=1.6;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
const ws=i=>WORDS[i].start, we=i=>WORDS[i].end;
// [id, início, fim]
const C=[['ex',0.1,TOT],['title',0,ws(3)-.05],['ban',ws(3)-.05,we(12)+.35],['cA',0.12,TOT],['cB',0.3,TOT],
 ['q',ws(35)-.05,ws(42)-.1],['cta',ws(42)-.05,ws(46)-.05],['tz',ws(46)-.05,TOT]];
const HA=[ws(13)-.05,we(21)+.25], HB=[ws(22)-.05,we(34)+.25];
const EXPR=[[0,'calm'],[ws(8),'happy'],[ws(13),'calm'],[ws(35),'worried'],[ws(42),'happy']];
const BLINK=[1.9,4.9,8.4,11.3,15.0,18.6];
const G=[];(function(){let g=[];WORDS.forEach((w,i)=>{g.push(i);const last=/[.?:,]$/.test(w.text)||g.length>=4||g.join('').length>14&&g.length>=3;if(last){G.push(g);g=[]}});if(g.length)G.push(g)})();
const cap=$('#subs');G.forEach((g,gi)=>{const d=document.createElement('div');d.className='g';d.innerHTML=g.map(i=>'<span class="w" data-i="'+i+'">'+WORDS[i].text.replace(/[,]$/,'')+'</span>').join(' ');cap.appendChild(d)});
const GT=G.map((g,gi)=>{const s=ws(g[0])-.04;const ne=gi+1<G.length?ws(G[gi+1][0])-.04:TOT;const e=Math.min(we(g[g.length-1])+.25,ne);return [s,e]});
const lerp=(a,b,t)=>a+(b-a)*t;
function hex(c){return [1,3,5].map(i=>parseInt(c.substr(i,2),16))}
function mix(a,b,t){const A=hex(a),B=hex(b);return 'rgb('+A.map((v,i)=>Math.round(lerp(v,B[i],t))).join(',')+')'}
function act(t,w){if(t<w[0]||t>w[1])return 0;return Math.min(1,(t-w[0])/.18)*Math.min(1,(w[1]-t)/.18)}
window.render=function(t){
 const k=cl((t-9)/6);const c1=mix('#18273a','#101b2a',k),c2=mix('#34516a','#1f3347',k),c3=mix('#d98a3a','#4a6a82',k);
 $('#sky').style.background='linear-gradient(180deg,'+c1+' 0%,'+c2+' 55%,'+c3+' 78%,'+c3+' 100%)';
 const s=$('#sun');s.style.background=mix('#f2b705','#e8ecef',k);s.style.opacity=.9-.25*k;s.style.top=(1000+k*20)+'px';s.style.left=(700-t*3)+'px';
 $('#h1').style.transform='translateX('+(-(t*18)%720)+'px)';$('#h2').style.transform='translateX('+(-(t*34)%540)+'px)';$('#h3').style.transform='translateX('+(-(t*60)%900)+'px)';
 const wm=$('#wm');const pos=Math.floor(t/8)%2;wm.style.top='150px';wm.style.left=pos?'auto':'48px';wm.style.right=pos?'48px':'auto';
 let ex='calm';EXPR.forEach(e=>{if(t>=e[0])ex=e[1]});
 ['calm','worried','shock','happy'].forEach(k=>{$('#ex_'+k).style.display=k==ex?'':'none';});
 const f=Math.min(MOUTH.length-1,Math.round(t*30));const m=+MOUTH[f];
 ['calm','worried','shock','happy'].forEach(k=>{$('#mo_'+k).style.display=(k==ex&&m==0)?'':'none'});
 $('#sp1').style.display=m==1?'':'none';$('#sp2').style.display=m==2?'':'none';
 let bl=false;BLINK.forEach(b=>{if(t>=b&&t<b+.13)bl=true});$('#blink').style.display=bl?'':'none';
 const ze=$('#ze');ze.style.transform='translateY('+(Math.sin(t*2.3)*5-(m>1?4:0))+'px) rotate('+(Math.sin(t*1.4)*1.1)+'deg) scale('+(1+0.012*Math.sin(t*3.1))+')';
 const aA=act(t,HA),aB=act(t,HB);
 C.forEach(([id,a,b])=>{const el=document.getElementById(id);let o=0,sc=1,ty=0;
  if(t>=a&&t<=b){const i=cl((t-a)/.3),ou=cl((b-t)/.22);o=Math.min(1,i*3)*Math.min(1,ou*3+(b>=TOT-.01?1:0));sc=(0.82+0.18*back((t-a)/.38));ty=(1-eo((t-a)/.3))*40;if(id=='title'&&t<.2){o=1;sc=.94+.06*back(t/.2);ty=0}}
  if(id=='cA'||id=='cB'){const me=id=='cA'?aA:aB,other=id=='cA'?aB:aA;sc*=1+.07*me-.02*other;o*=1-.35*other;
    el.style.outlineWidth=(10*me)+'px';ty-=10*me}
  el.style.opacity=o;el.style.transform='translateY('+ty+'px) scale('+sc+')'});
 const tk=eo((t-ws(36))/.3);['tA','tB'].forEach((id,ix)=>{const e=$('#'+id);const kk=eo((t-ws(36)-ix*.15)/.3);e.style.opacity=kk;e.style.transform='scale('+(.9+.1*kk)+')'});
 const bl2=(t>ws(36)&&t<ws(42))?(Math.floor(t*3)%2):1;['tA','tB'].forEach(id=>{$('#'+id).querySelector('.yel').style.opacity=t<ws(42)?(.45+.55*bl2):1});
 const gs=cap.children;for(let gi=0;gi<G.length;gi++){const el=gs[gi],[a,b]=GT[gi];const on=t>=a&&t<=b;el.style.opacity=on?1:0;if(on){el.style.transform='scale('+(0.92+0.08*back((t-a)/.15))+')';el.querySelectorAll('span.w').forEach(sp=>{const i=+sp.dataset.i;sp.className='w'+(t>=ws(i)-.02&&t<we(i)+.04?' on':'')})}}
};
window.render(0);
</script></body></html>'''
HTML=(HTML.replace('__ZE__',ze_svg()).replace('__TOT__',str(TOT)).replace('__WORDS__',json.dumps(W,ensure_ascii=False)).replace('__MOUTH__',mouth))
open('index.html','w').write(HTML)
def ws(i): return W[i]['start']
def we(i): return W[i]['end']
cues=[]
for a in [0.02,0.12,0.3,ws(3)-.05,ws(35)-.05,ws(42)-.05,ws(46)-.05]: cues.append(dict(t=round(a,3),k='whoosh'))
for a in [ws(13)-.05,ws(22)-.05]: cues.append(dict(t=round(a,3),k='pop'))
cues.append(dict(t=round(ws(35)-.05,3),k='slam'))
cues.append(dict(t=round(ws(36),3),k='pop')); cues.append(dict(t=round(ws(36)+.15,3),k='pop'))
cues.append(dict(t=round(ws(42)-.05,3),k='ding')); cues.append(dict(t=round(ws(46)-.05,3),k='ding'))
json.dump(cues,open('cues.json','w'))
print('ok',len(HTML)//1024,'KB',len(cues),'efeitos')
