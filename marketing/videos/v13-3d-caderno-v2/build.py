# Vídeo 3D v2 (qualidade melhor) "Eu sei que você anota no caderninho": maquete 3D (Three.js) + legendas e cartões em HTML.
import json, numpy as np
W = json.load(open('words.json'))
TOT = 47.6
def ws(i): return next(w['start'] for w in W if w['id'] == i)
def we(i): return next(w['end'] for w in W if w['id'] == i)
KW = [4, 7, 14, 19, 23, 24, 26, 29, 32, 42, 45, 53, 55, 57, 59, 68, 69, 71, 75, 79, 80, 82, 83, 84, 89, 92, 96, 98, 103, 104, 105, 107, 109, 113]

HTML = r'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>
@font-face{font-family:B;src:url(fonts/barlow-latin-700-normal.woff2);font-weight:700}
@font-face{font-family:BC;src:url(fonts/barlow-condensed-latin-800-normal.woff2);font-weight:800}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#8fc7e8;font-family:B;color:#f4f3ee}
#sky{position:absolute;inset:0;background:linear-gradient(180deg,#5fa8d8 0%,#a8d6ee 45%,#f3e2b8 70%)}
canvas#gl{position:absolute;left:0;top:0;width:1080px;height:1920px}
.abs{position:absolute}
#subs{position:absolute;left:60px;right:60px;top:226px;text-align:center;z-index:58;font:700 58px/1.3 B;text-shadow:0 3px 10px rgba(0,0,0,.8),0 0 2px #000}
#subs .w{display:inline-block;margin:4px 5px;opacity:0;border:4px solid transparent;border-radius:12px;padding:0 10px;background:rgba(16,18,22,.62)}
#subs .w.k.on{border-color:#f2b705}
#wm{position:absolute;font:700 38px B;color:#fff;opacity:.85;letter-spacing:1px;text-shadow:0 2px 6px rgba(0,0,0,.6);z-index:60;top:150px}
#ex{position:absolute;left:0;right:0;top:1500px;text-align:center;font:700 30px B;color:#fff;letter-spacing:2px;z-index:55;text-shadow:0 2px 6px rgba(0,0,0,.8)}
.chip{position:absolute;left:0;right:0;top:470px;text-align:center;z-index:40;opacity:0}
.chip span{display:inline-block;background:#16181b;color:#f4f3ee;font:800 92px/1 BC;text-transform:uppercase;padding:22px 44px 12px;border-radius:26px;box-shadow:0 14px 0 rgba(0,0,0,.3);white-space:nowrap}
.chip b{color:#ff7a66}
#note{position:absolute;left:170px;top:880px;width:740px;height:620px;background:#fbf6e6;border-radius:14px;box-shadow:0 24px 0 rgba(0,0,0,.25);padding:34px 56px;color:#203a63;z-index:30;opacity:0;
 background-image:repeating-linear-gradient(180deg,transparent 0 92px,#b9d3ea 92px 96px);background-position:0 40px;transform-origin:50% 50%}
#note:after{content:'';position:absolute;left:40px;right:40px;top:-22px;height:44px;background:repeating-linear-gradient(90deg,transparent 0 30px,#6b7280 30px 42px,transparent 42px 60px);border-radius:8px}
#note:before{content:'';position:absolute;left:110px;top:0;bottom:0;width:4px;background:#e8a0a0}
#note .nl{font:700 56px/96px B;padding-left:90px;display:flex;justify-content:space-between;opacity:0}
#note .nl b{font-weight:700}
#note .q{color:#c0392b}
#note .tot{border-top:5px solid #203a63;margin-top:8px}
#note .drop{position:absolute;width:60px;height:80px;border-radius:50% 50% 50% 50%/60% 60% 40% 40%;background:rgba(80,150,220,.55);opacity:0}
#tear{position:absolute;left:0;right:0;top:0;bottom:0;pointer-events:none}
.phone{position:absolute;width:540px;height:1000px;left:270px;top:430px;border-radius:70px;background:#0d0f12;padding:26px;box-shadow:0 30px 0 rgba(0,0,0,.35);z-index:35;opacity:0}
.scr{width:100%;height:100%;border-radius:48px;background:#16181b;overflow:hidden;position:relative}
.ah{background:#f2b705;color:#16181b;padding:56px 34px 22px;font:800 52px/1 BC;text-transform:uppercase}
.ah small{display:block;font:700 26px B;letter-spacing:1px;margin-top:8px}
.li{display:flex;justify-content:space-between;align-items:center;margin:18px 26px 0;padding:20px 26px;background:#22252a;border-radius:22px;font:700 32px B;text-transform:uppercase;opacity:0}
.li b{font:800 50px BC}.li.hl{outline:5px solid #f2b705}
.grn{color:#5fd39a}.red{color:#ff7a66}.yel{color:#f2b705}
#sob{margin:30px 26px 0;padding:26px;border-radius:26px;background:#123526;text-align:center;opacity:0}
#sob div{font:700 30px B;color:#bfe9d3;text-transform:uppercase}#sob b{font:800 110px/1 BC;color:#5fd39a}
#ok{position:absolute;right:120px;top:380px;width:170px;height:170px;border-radius:50%;background:#5fd39a;color:#16181b;font:800 130px/170px BC;text-align:center;z-index:36;opacity:0}
#end{position:absolute;left:70px;right:70px;top:420px;text-align:center;z-index:45;opacity:0;background:rgba(22,24,27,.88);border-radius:44px;padding:50px 20px 60px}
#end .ic{width:280px;height:280px;border-radius:62px;overflow:hidden;margin:0 auto;box-shadow:0 18px 0 rgba(0,0,0,.3)}
#end .nm{font:800 124px/1 BC;text-transform:uppercase;margin-top:30px;text-shadow:0 6px 0 rgba(0,0,0,.35)}
#end .pill{display:inline-block;margin-top:36px;background:#f2b705;color:#16181b;font:800 80px/1 BC;text-transform:uppercase;padding:22px 46px 12px;border-radius:999px;box-shadow:0 14px 0 rgba(0,0,0,.3)}
</style></head><body>
<div id="sky"></div><canvas id="gl" width="__CW__" height="__CH__"></canvas>
<div class="chip" id="c0"><span>R$ 8.000 · frete</span></div>
<div class="chip" id="c1"><span><b>− R$ 5.520</b> · diesel</span></div>
<div class="chip" id="c2"><span><b>− R$ 1.200</b> · pedágio</span></div>
<div class="chip" id="c3"><span><b>− R$ 300</b> · pneu</span></div>
<div class="chip" id="c4"><span><b>− R$ 200</b> · óleo e filtro</span></div>
<div class="chip" id="c5"><span><b>− R$ 200</b> · freio e revisão</span></div>
<div class="chip" id="c6"><span>Sobrou <span style="background:none;padding:0;box-shadow:none;color:#5fd39a;font:inherit">R$ 580</span></span></div>
<div id="note">
 <div class="nl" data-n="0"><span>Frete</span><b>8.000</b></div>
 <div class="nl" data-n="1"><span>Diesel</span><b>5.520</b></div>
 <div class="nl" data-n="2"><span>Pedágio</span><b>1.200</b></div>
 <div class="nl q" data-n="3"><span>Manutenção</span><b>???</b></div>
 <div class="nl tot" data-n="4"><span>Sobra</span><b>1.280 ☺</b></div>
 <div class="drop" style="left:120px;top:150px"></div><div class="drop" style="left:420px;top:320px"></div><div class="drop" style="left:600px;top:120px"></div><div class="drop" style="left:250px;top:520px"></div><div class="drop" style="left:540px;top:600px"></div>
 <svg id="tear" viewBox="0 0 780 780"><path id="tearp" d="M0 0" fill="none" stroke="#7a6a50" stroke-width="6"/></svg>
</div>
<div class="phone" id="ph"><div class="scr"><div class="ah">Viagem do Zé<small>exemplo</small></div>
 <div class="li" data-l="0"><span>Frete</span><b class="grn">+ 8.000</b></div>
 <div class="li" data-l="1"><span>Diesel</span><b class="red">− 5.520</b></div>
 <div class="li" data-l="2"><span>Pedágio</span><b class="red">− 1.200</b></div>
 <div class="li hl" data-l="3"><span>Manutenção</span><b class="red">− 700</b></div>
 <div id="sob"><div>Sobrou de verdade</div><b>R$ 580</b></div>
</div></div>
<div id="ok">✓</div>
<div id="end"><div class="ic"><img src="icon-512.png" style="width:100%;height:100%"></div><div class="nm">Diário <span class="yel">de Bordo</span></div><div class="pill">Toque no link do perfil</div></div>
<div id="subs"></div><div id="wm">@appdiariodebordo</div><div id="ex">NÚMEROS DE EXEMPLO</div>
<script>
window.TOT=__TOT__; window.WORDS=__WORDS__; window.KW=new Set(__KW__);
</script>
<script type="importmap">{"imports":{"three":"./three.module.min.js"}}</script>
<script type="module">
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const cl=x=>Math.max(0,Math.min(1,x)), eo=x=>1-Math.pow(1-cl(x),3), eio=x=>{x=cl(x);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2};
const back=x=>{x=cl(x);const c=1.6;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
const ws=i=>WORDS.find(w=>w.id==i).start, we=i=>WORDS.find(w=>w.id==i).end;
await import('./scene.js');
const EV=window.__scene.EV;
// legenda
const PH=[];(()=>{let g=[];WORDS.forEach(w=>{g.push(w);if(/[.,:?]$/.test(w.text)&&g.length>=3||/[.:?]$/.test(w.text)){PH.push(g);g=[]}});if(g.length)PH.push(g)})();
const subs=$('#subs');let cur=-1;
const show=(el,a,b,t,mode)=>{const on=t>=a&&t<=b;const u=t-a;const o=on?Math.min(cl(u/.15),cl((b-t)/.2)):0;el.style.opacity=o;if(on&&mode!='none')el.style.transform='scale('+(0.7+0.3*back(u/.35))+')';return on};
window.render=function(t){
 window.render3d(t);
 // HTML: cartões
 show($('#c0'),ws(21)+.1,ws(26)-.1,t);show($('#c1'),EV[0][0]+.3,ws(31)-.1,t);show($('#c2'),EV[1][0]+.3,ws(37)-.1,t);show($('#c3'),EV[2][0]+.3,we(49)+.2,t);
 show($('#c4'),EV[3][0]+.3,we(55)+.1,t);show($('#c5'),EV[4][0]+.3,we(59)+.4,t);show($('#c6'),ws(66),we(69)+.4,t);
 // caderno
 const nt=$('#note');let no=0,ntr='';
 if(t<we(14)+.8){no=cl((t-.05)/.25)*cl((we(14)+.8-t)/.3);ntr='rotate(-3deg) translateY('+(1-eo(t/.5))*200+'px)'}
 else if(t>=ws(70)-.1&&t<ws(76)-.05){const u=t-ws(70)+.1;no=cl(u/.25)*cl((ws(76)-.05-t)/.2);ntr='rotate(2deg) translateY('+(1-eo(u/.4))*300+'px)'}
 else if(t>=ws(102)-.1&&t<we(107)+.4){const u=t-ws(102)+.1;no=cl(u/.2)*cl((we(107)+.4-t)/.3);const fall=cl((t-ws(107))/.6);ntr='rotate('+(2+fall*25)+'deg) translateY('+fall*700+'px) scale('+(1-fall*.2)+')'}
 nt.style.opacity=no;nt.style.transform=ntr;
 const lines=[ws(8),ws(9),ws(10),ws(14)];$$('#note .nl').forEach(e=>{const k=+e.dataset.n;let vis;if(k<4){vis=t<we(14)+.8?t>=lines[k]-.05:t>=ws(70)}else vis=t>=ws(73);e.style.opacity=vis?1:0});
 $$('#note .drop').forEach((d,i)=>{d.style.opacity=t>=ws(104)+i*.06&&t<we(107)+.4?.9:0;d.style.transform='scale('+(0.6+0.4*cl((t-ws(104)-i*.06)/.2))+')'});
 $('#tearp').setAttribute('d',t>=ws(105)?'M390 0 L360 120 L420 230 L350 360 L430 500 L370 640 L400 780':'M0 0');
 $('#note').style.filter=t>=ws(104)&&t<we(107)+.4?'saturate(.7) brightness(.92)':'none';
 // celular
 const ph=$('#ph');const pa=ws(81)-.2,pb=ws(102)-.2;const pon=t>=pa&&t<pb||t>=ws(108)-.1&&t<ws(111)-.1;
 const pu=t<ws(108)?t-pa:t-ws(108)+.1;ph.style.opacity=pon?cl(pu/.2):0;ph.style.transform='translateY('+(1-eo(pu/.4))*800+'px)';
 const li=[ws(86),ws(87),ws(89)-.1,ws(90)];$$('#ph .li').forEach(e=>{const l=+e.dataset.l;const on=t>=li[l]||t>=ws(108);e.style.opacity=on?1:0});
 $('#sob').style.opacity=(t>=ws(96)||t>=ws(108))?1:0;$('#sob').style.transform='scale('+(t>=ws(96)&&t<ws(102)?back((t-ws(96))/.35):1)+')';
 show($('#ok'),ws(109),ws(111)-.1,t);
 // final
 const eo2=cl((t-ws(111)+.1)/.3);$('#end').style.opacity=eo2;$('#end').style.transform='scale('+(0.8+0.2*back((t-ws(111)+.1)/.4))+')';
 // marca d'água
 const wm=$('#wm');const pos=Math.floor(t/8)%2;wm.style.left=pos?'auto':'48px';wm.style.right=pos?'48px':'auto';
 // legenda
 let pi=-1;PH.forEach((g,i)=>{if(t>=g[0].start-.05)pi=i});
 if(pi!=cur){cur=pi;subs.innerHTML=pi<0?'':PH[pi].map(w=>'<span class="w'+(KW.has(w.id)?' k':'')+'" data-i="'+w.id+'">'+w.text+'</span>').join(' ')}
 subs.querySelectorAll('.w').forEach(sp=>{const i=+sp.dataset.i;const s=ws(i);sp.style.opacity=t>=s-.03?1:0;sp.classList.toggle('on',t>=s)});
 const last=PH[pi];subs.style.opacity=last&&t>last[last.length-1].end+0.6?0:1;
};
window.render(0);window.__ready=true;
</script></body></html>'''
CW, CH = 1080, 1920
HTML = (HTML.replace('__TOT__', str(TOT)).replace('__WORDS__', json.dumps(W, ensure_ascii=False)).replace('__KW__', json.dumps(KW))
        .replace('__CW__', str(CW)).replace('__CH__', str(CH)))
open('index.html', 'w').write(HTML)
ev = lambda i: ws(i)
cues = [dict(t=0.02, k='slam')]
for c in [7.1, 10.6, 13.05, 15.37, 17.96, 20.74, 24.44, 28.08, 32.79, 40.58, 44.47]: cues.append(dict(t=c, k='whoosh'))
for i in (8, 9, 10): cues.append(dict(t=round(ws(i), 3), k='tap'))
cues.append(dict(t=round(ws(14), 3), k='thud'))
cues.append(dict(t=round(ws(15), 3), k='cash'))
for i in (29, 34, 46, 53, 57): cues.append(dict(t=round(ws(i)+.15, 3), k='pop'))
cues.append(dict(t=13.8, k='beep'))
cues.append(dict(t=round(ws(78), 3), k='slam'))
for i in (86, 87, 89, 90): cues.append(dict(t=round(ws(i), 3), k='tap'))
cues.append(dict(t=round(ws(96), 3), k='cash'))
cues.append(dict(t=round(ws(105), 3), k='thud'))
cues.append(dict(t=round(ws(109), 3), k='ding'))
json.dump(cues, open('cues.json', 'w'))
print('ok', len(HTML)//1024, 'KB')
