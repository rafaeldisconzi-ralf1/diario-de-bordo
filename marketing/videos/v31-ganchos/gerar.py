# Gera index-g1/g2/g3.html (ganchos fortes para anúncio). Rodar: python3 gerar.py
import json, pathlib
here = pathlib.Path(__file__).parent

BASE = r'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>
@font-face{font-family:B;src:url(fonts/barlow-latin-700-normal.woff2);font-weight:700}
@font-face{font-family:BC;src:url(fonts/barlow-condensed-latin-800-normal.woff2);font-weight:800}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#121418;font-family:B;color:#f4f3ee}
#bg{position:absolute;inset:-100px;background:repeating-linear-gradient(-45deg,rgba(255,255,255,.035) 0 3px,transparent 3px 44px)}
#glow{position:absolute;left:-200px;top:150px;width:1480px;height:1400px;background:radial-gradient(ellipse,var(--gc,rgba(255,80,60,.22)),transparent 62%)}
#flash{position:absolute;inset:0;background:#d7261e;opacity:0}
.abs{position:absolute;opacity:0}
.yel{color:#f2b705}.grn{color:#5fd39a}.red{color:#ff5a45}
#wm{position:absolute;left:0;right:0;top:80px;text-align:center;font:700 36px B;opacity:.7;z-index:4}
.big{left:40px;right:40px;text-align:center;font:800 150px/.95 BC;text-transform:uppercase;text-shadow:0 8px 30px rgba(0,0,0,.5)}
.mid{left:40px;right:40px;text-align:center;font:800 104px/1 BC;text-transform:uppercase}
.chip{font:800 92px/1 BC;text-transform:uppercase;background:#22252a;border:5px solid #3a3e45;border-radius:26px;padding:22px 40px 12px;white-space:nowrap}
.num{left:0;right:0;text-align:center;font:800 230px/1 BC;font-variant-numeric:tabular-nums}
.lbl{left:0;right:0;text-align:center;font:800 64px BC;text-transform:uppercase;letter-spacing:3px;color:#c9c5ba}
.gasto{left:140px;right:140px;display:flex;justify-content:space-between;font:800 76px BC;text-transform:uppercase;background:#22252a;border-left:12px solid #ff5a45;border-radius:18px;padding:18px 36px 8px}
.gasto b{color:#ff5a45}
.ph{left:280px;top:300px;width:520px;height:1125px;border-radius:64px;background:#0b0c0e;border:12px solid #2b2e34;box-shadow:0 30px 70px rgba(0,0,0,.6);overflow:hidden}
.ph img{position:absolute;left:0;top:0;width:496px}
.hl{position:absolute;border:7px solid #f2b705;border-radius:20px;box-shadow:0 0 0 2000px rgba(0,0,0,.45);opacity:0}
.tape{position:absolute;left:-60px;right:-60px;height:90px;background:repeating-linear-gradient(-45deg,#f2b705 0 60px,#16181b 60px 120px);opacity:0}
.card{width:470px;border-radius:30px;background:#22252a;border:6px solid #3a3e45;padding:30px 20px 26px;text-align:center}
.card .t{font:800 54px BC;text-transform:uppercase;color:#c9c5ba;letter-spacing:2px}
.card .v{font:800 120px/1 BC;margin:10px 0}
.card .k{font:800 58px BC;text-transform:uppercase}
.card .s{font:800 44px BC;text-transform:uppercase;color:#c9c5ba;margin-top:26px}
.card .r{font:800 104px/1 BC;white-space:nowrap;font-variant-numeric:tabular-nums}
.stamp{font:800 96px BC;text-transform:uppercase;border:10px solid;border-radius:18px;padding:16px 34px 6px;white-space:nowrap}
#sub{position:absolute;left:30px;right:30px;top:1470px;height:220px;display:flex;align-items:center;justify-content:center;text-align:center;font:800 88px/1 BC;text-transform:uppercase;-webkit-text-stroke:12px #080a09;paint-order:stroke fill;opacity:0;flex-wrap:wrap;z-index:5}
#sub span{display:inline-block;margin:0 .13em;color:#f4f3ee}
#sub span.on{color:#f2b705;transform:scale(1.08)}
#ft{left:0;right:0;top:1700px;text-align:center;font:700 28px B;color:#c9c5ba;text-transform:uppercase;letter-spacing:2px;z-index:5}
#end{position:absolute;inset:0;background:#16181b;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;padding-top:280px;gap:34px;opacity:0;z-index:6}
#ico{width:220px;height:220px;border-radius:48px}
#en{font:800 112px BC;text-transform:uppercase}
#el{font:800 82px/1.05 BC;text-transform:uppercase;text-align:center}
#ep{background:#f2b705;color:#16181b;font:800 96px BC;padding:24px 70px 16px;border-radius:999px;text-transform:uppercase}
%%CSS%%
</style></head><body>
<div id="bg"></div><div id="glow"></div><div id="flash"></div><div id="wm">@appdiariodebordo</div>
%%HTML%%
<div class="abs" id="ft">%%FT%%</div>
<div id="end"><img id="ico" src="icon-512.png"><div id="en">Diário de Bordo</div>
 <div id="el">%%EL%%</div><div id="ep">Toque em Saiba mais</div>
 <div style="font:700 42px B;text-transform:uppercase;color:#c9c5ba;letter-spacing:1px">R$ 24,90/mês · 7 dias de garantia</div></div>
<div id="sub"></div>
<script>
const TOT=%%TOT%%,END=%%END%%,$=s=>document.querySelector(s);
const cl=x=>Math.max(0,Math.min(1,x)),eo=x=>1-Math.pow(1-cl(x),3);
const back=x=>{x=cl(x);const c=1.7;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
let T=0;
function vis(id,a,b,fi,fo){fi=fi||.12;fo=fo||.12;const o=a<=0&&T<=0?1:cl((T-a)/fi)*(1-cl((T-b)/fo));$(id).style.opacity=o;return o}
function pop(id,a,s0,tx){const p=a<=0?1:back((T-a)/.35);s0=s0||.85;$(id).style.transform=(tx||'')+' scale('+(s0+(1-s0)*p)+')'}
function shake(id,a,d,tx){const k=(T>=a&&T<a+d)?(1-(T-a)/d):0;const x=Math.sin(T*90)*22*k,y=Math.cos(T*77)*12*k;$(id).style.transform=(tx||'')+' translate('+x+'px,'+y+'px)'}
function brl(v){const s=Math.round(Math.abs(v)).toString().replace(/\B(?=(\d{3})+(?!\d))/g,'.');return (v<0?'−':'')+'R$ '+s}
function cnt(a,b,v0,v1){return v0+(v1-v0)*eo((T-a)/(b-a))}
const X='translateX(-50%)';
const SEG=%%SEG%%;
const CH=[];
SEG.forEach(([a,b,s])=>{const tk=s.split(' ').filter(x=>x!=='/');const tw=tk.reduce((q,x)=>q+(+x.split(':').pop()),0);let acc=0,cur=null;const d=b-a;
 s.split(' ').forEach(x=>{if(x==='/'){cur=null;return}const k=+x.split(':').pop();const w=x.slice(0,x.lastIndexOf(':'));const ws=a+d*acc/tw;acc+=k;const we=a+d*acc/tw;
  if(!cur){cur={w:[],a:ws,b:we};CH.push(cur)}cur.w.push({t:w.replace(/_/g,' '),a:ws,b:we});cur.b=we;});});
CH.forEach((c,i)=>{const n=CH[i+1];c.s0=Math.max(0,c.a-0.1);c.s1=(n&&n.a-c.b<0.4)?n.a-0.04:c.b+0.15;});
let last=-1;
function sub(t){const el=$('#sub');const i=CH.findIndex(c=>t>=c.s0&&t<c.s1);
 if(i<0||t>=END){el.style.opacity=0;last=-1;return}
 if(i!==last){el.innerHTML=CH[i].w.map(w=>'<span>'+w.t+'</span>').join('');last=i}
 el.style.opacity=1;[...el.children].forEach((s,k)=>{const w=CH[i].w[k];s.className=(t>=w.a&&t<w.b)?'on':''});}
window.render=function(t){T=t;
 $('#bg').style.transform='translate('+(-(t*14)%62)+'px,'+(-(t*14)%62)+'px)';
%%ANIM%%
 $('#ft').style.opacity=(t>%%FT0%%&&t<END)?.85:0;
 const e=$('#end');e.style.opacity=cl((t-END)/.3);e.style.transform='scale('+(.94+.06*eo((t-END)/.5))+')';
 $('#wm').style.opacity=t<END?.7:0;
 sub(t);
};
window.render(0);
</script></body></html>'''

V = {}

# ---------- G1: Pagou pra trabalhar ----------
GASTOS = [('Diesel', 15800, 7.3), ('Pedágio', 3100, 8.05), ('Parcela', 7200, 8.8), ('Pneu', 2300, 9.55), ('Diária', 4000, 10.3)]
g1html = '''
<div class="abs big" id="h0" style="top:300px;font-size:120px">Rodou o mês<br>inteiro...</div>
<div class="abs num yel" id="dia" style="top:640px;font-size:300px">DIA 1</div>
<div class="abs lbl" id="dl" style="top:960px">de 30</div>
<div class="abs big" id="h1" style="top:640px;font-size:180px"><span class="red">e pagou<br>pra<br>trabalhar</span></div>
<div class="abs lbl" id="l2" style="top:420px">Faturou no mês</div>
<div class="abs num grn" id="n2" style="top:500px">R$ 0</div>
''' + ''.join(f'<div class="abs gasto" id="gs{i}" style="top:{800+i*120}px"><span>{n}</span><b>−R$ {v:,}</b></div>'.replace(',', '.') for i, (n, v, _) in enumerate(GASTOS)) + '''
<div class="abs lbl" id="l3" style="top:540px">No fim do mês sobrou</div>
<div class="abs num red" id="n3" style="top:650px;font-size:300px">−R$ 400</div>
<div class="abs ph" id="ph"><img id="s1" src="telas/01-inicio-ia.png"><img id="s6" src="telas/06-chat-frete.png">
 <div class="hl" id="hlb" style="left:248px;top:592px;width:240px;height:126px"></div></div>
<div class="abs big" id="h5" style="top:560px;font-size:130px">Veja quanto<br><span class="grn">sobrou</span><br>de verdade</div>
'''
g1anim = '''
 $('#flash').style.opacity=(t>=2.74&&t<4.2)?0.55*(1-cl((t-2.74)/1.2)):0;
 vis('#h0',0,2.7);pop('#h0',0,.9);
 vis('#dia',0,2.7);vis('#dl',0,2.7);$('#dia').textContent='DIA '+Math.max(1,Math.round(1+29*cl(t/2.3)));
 vis('#h1',2.74,4.3);pop('#h1',2.74,1.6);if(t>3.1)shake('#h1',3.1,.6);
 pop('#n2',4.5,.7);
 $('#l2').textContent=t<7.2?'Faturou no mês':'Sobrando';
 const G=%s;let bal=cnt(4.6,6.2,0,32000);
 G.forEach((g,i)=>{vis('#gs'+i,g[2],11.1);$('#gs'+i).style.transform='translateX('+(400*(1-eo((t-g[2])/.3)))+'px)';bal-=g[1]*eo((t-g[2]-.15)/.45)});
 $('#n2').textContent=brl(bal);$('#n2').className='abs num '+(bal<0?'red':(t>7.3?'yel':'grn'));
 vis('#l2',4.5,11.1);vis('#n2',4.5,11.1);
 vis('#l3',11.2,14.45);vis('#n3',12.55,14.45);pop('#n3',12.55,1.8);if(t>12.85)shake('#n3',12.85,.7);
 $('#flash').style.opacity=Math.max(+$('#flash').style.opacity,(t>=12.55&&t<13.6)?0.45*(1-cl((t-12.55)/1)):0);
 vis('#ph',14.6,21.0);$('#ph').style.transform='translateY('+(60*(1-eo((t-14.6)/.4)))+'px)';
 $('#s1').style.opacity=t<17.7?1:0;$('#s6').style.opacity=t>=17.7?1:0;
 $('#hlb').style.opacity=cl((t-17.0)/.2)*(t<17.7?1:0);
 vis('#h5',21.05,24.4);pop('#h5',21.05,.85);
''' % json.dumps(GASTOS)
V['g1'] = dict(TOT=27.3, END=24.4, FT0=4.4, FT='números de exemplo', EL='Lance tudo.<br>Veja quanto <span class="grn">sobrou</span><br>de verdade.', css='', html=g1html, anim=g1anim, SEG=[
 [0.08, 2.34, "Esse:2 caminhoneiro:5 / rodou:2 o:1 mês:1 inteiro:3"], [2.74, 4.11, "e:1 pagou:2 pra:1 trabalhar:3"],
 [4.52, 6.73, "Faturou:3 / R$_32_mil:6"], [7.13, 10.82, "Diesel:2 pedágio:3 / parcela:3 pneu:2 / diária:3"],
 [11.22, 14.32, "No:1 fim:1 do:1 mês:1 / menos:2 R$_400:6"], [14.67, 17.4, "E:1 ele:2 só:1 descobriu:3 / porque:2 lançou:2 / tudo:2 no:1 app:1"],
 [17.78, 20.68, "Agora:3 ele:2 pergunta:3 pra:1 IA:2 / antes:2 de:1 aceitar:3 frete:2"], [21.11, 22.0, "Diário_de_Bordo:5"],
 [22.34, 24.17, "veja:2 quanto:2 sobrou:2 / de:1 verdade:3"], [24.52, 25.9, "Toque:2 em:1 Saiba:2 mais:2"]])

# ---------- G2: Para! Não aceita esse frete ----------
g2css = '''#stop{left:50%;top:330px;width:620px;height:620px;background:#d7261e;clip-path:polygon(29.3% 0,70.7% 0,100% 29.3%,100% 70.7%,70.7% 100%,29.3% 100%,0 70.7%,0 29.3%);display:flex;align-items:center;justify-content:center}
#stop:before{content:"";position:absolute;inset:22px;background:#fff;clip-path:inherit}
#stop:after{content:"";position:absolute;inset:36px;background:#d7261e;clip-path:inherit}
#stop span{position:relative;z-index:2;font:800 220px/1 BC;color:#fff;margin-top:24px}'''
g2html = '''
<div class="abs" id="stop"><span>PARA!</span></div>
<div class="abs mid" id="h0" style="top:1030px">Não aceita<br><span class="red">esse frete</span> ainda</div>
<div class="abs num grn" id="n1" style="top:380px;font-size:260px">R$ 6.000</div>
<div class="abs mid" id="h1" style="top:650px">parece bom, né?</div>
<div class="abs chip" id="k1" style="left:120px;top:820px">1.000 km</div>
<div class="abs chip" id="k2" style="left:420px;top:1030px;border-color:#ff5a45"><span class="red">Volta vazio</span></div>
<div class="abs ph" id="ph"><img id="s6" src="telas/06-chat-frete.png"><img id="s1" src="telas/01-inicio-ia.png">
 <div class="hl" id="hl6" style="left:14px;top:540px;width:468px;height:100px"></div>
 <div class="hl" id="hlb" style="left:248px;top:592px;width:240px;height:126px"></div></div>
<div class="abs stamp" id="st" style="left:50%;top:1180px;color:#ff5a45;border-color:#ff5a45;background:rgba(18,20,24,.92)">−R$ 1.060</div>
<div class="abs mid" id="h4" style="top:240px;font-size:92px">Pergunta pro Diário<br><span class="yel">antes de fechar</span></div>
'''
g2anim = '''
 $('#flash').style.opacity=t<1.2?0.35*(1-cl(t/1.2)):0;
 vis('#stop',0,2.6);pop('#stop',0,.6,X);if(t<0.9)shake('#stop',0,0.9,X);
 vis('#h0',0.75,2.6);pop('#h0',0.75,.8);
 vis('#n1',2.72,7.8);pop('#n1',2.72,.7);vis('#h1',3.3,4.6);
 const bad=cl((t-6.4)/.3);$('#n1').style.color=bad>0?'#f2b705':'#5fd39a';
 vis('#k1',4.7,7.8);pop('#k1',4.7,.6);vis('#k2',6.38,7.8);pop('#k2',6.38,.6);if(t>6.6)shake('#k2',6.6,.5);
 vis('#ph',7.9,18.7);$('#ph').style.transform='translateY('+(60*(1-eo((t-7.9)/.4)))+'px) scale('+(t<13.6?1+0.05*eo((t-10.8)/.5):.86)+')';$('#ph').style.transformOrigin='50% 0';
 $('#s6').style.opacity=t<13.6?1:0;$('#s1').style.opacity=t>=13.6?1:0;
 $('#hl6').style.opacity=cl((t-10.83)/.2)*(t<13.5?1:0);
 vis('#st',11.6,13.6);pop('#st',11.6,1.7,X);if(t>11.9)shake('#st',11.9,.6,X);
 $('#flash').style.opacity=Math.max(+$('#flash').style.opacity,(t>=11.6&&t<12.6)?0.35*(1-cl((t-11.6)/1)):0);
 vis('#h4',13.7,18.7);pop('#h4',13.7,.85);
 if(t>=13.6){$('#ph').style.top='420px'}else{$('#ph').style.top='300px'}
 $('#hlb').style.opacity=cl((t-16.1)/.2)*(t<18.6?1:0);
'''
V['g2'] = dict(TOT=21.6, END=18.8, FT0=2.6, FT='números de exemplo · a IA pode errar, confira os valores', EL='Pergunta pra <span class="yel">IA</span><br>antes de aceitar.<br>Veja quanto <span class="grn">sobra</span>.', css=g2css, html=g2html, anim=g2anim, SEG=[
 [0.05, 2.25, "Para!:2 / Não:1 aceita:3 esse:2 / frete:2 ainda:3"], [2.72, 4.36, "R$_6_mil:5 / parece:3 bom,:1 né?:1"],
 [4.68, 6.1, "Mas:1 são:1 / 1.000_km:5"], [6.38, 7.5, "e:1 você:2 volta:2 vazio:3"], [7.94, 9.56, "Perguntei:3 pra:1 / IA:2 do:1 app:1"],
 [9.93, 10.49, "Resposta:3"], [10.83, 13.11, "você:2 perderia:4 / R$_1.060:7"], [13.7, 15.67, "Antes:2 de:1 fechar:2 / pergunta:3 pro:1 Diário:3"],
 [16.1, 18.47, "Ele:2 olha:2 os:1 seus:1 números:3 / e:1 responde:3 na:1 hora:2"], [18.9, 20.25, "Toque:2 em:1 Saiba:2 mais:2"]])

# ---------- G3: Frete bonito é armadilha ----------
g3html = '''
<div class="tape" id="tp1" style="top:200px;transform:rotate(-4deg)"></div>
<div class="tape" id="tp2" style="top:1330px;transform:rotate(3deg)"></div>
<div class="abs big" id="h0" style="top:380px;font-size:140px">Frete bonito<br>é a maior<br><span class="red">armadilha</span><br><span style="font-size:96px">do caminhoneiro</span></div>
<div class="abs card" id="cB" style="left:300px;top:400px;border-color:#ff5a45"><div class="t">Frete B</div><div class="v">R$ 10.000</div><div class="k">1.600 km</div><div class="s" id="sBl">sobra</div><div class="r" id="rB">R$ 10.000</div></div>
<div class="abs card" id="cA" style="left:560px;top:400px;border-color:#5fd39a"><div class="t">Frete A</div><div class="v">R$ 7.000</div><div class="k">600 km</div><div class="s">sobra</div><div class="r grn" id="rA">R$ 4.882</div></div>
<div class="abs stamp" id="ok" style="left:50%;top:1060px;color:#5fd39a;border-color:#5fd39a;transform:rotate(-6deg)">Parece ótimo</div>
<div class="abs mid" id="cs" style="top:1060px;font-size:68px;color:#ff5a45">− diesel − pedágio<br>− diária − desgaste</div>
<div class="abs stamp" id="mais" style="left:590px;top:1060px;color:#5fd39a;border-color:#5fd39a;font-size:70px;background:rgba(18,20,24,.92)">Sobra mais</div>
<div class="abs big" id="h3" style="top:420px;font-size:130px">Quem não<br>faz a conta,<br><span class="red">escolhe<br>errado</span></div>
<div class="abs ph" id="ph"><img id="s1" src="telas/01-inicio-ia.png"></div>
'''
g3anim = '''
 vis('#tp1',0,3.3);vis('#tp2',0,3.3);
 $('#tp1').style.transform='rotate(-4deg) translateX('+(-(t*80)%120)+'px)';$('#tp2').style.transform='rotate(3deg) translateX('+((t*80)%120)+'px)';
 vis('#h0',0,3.3);pop('#h0',0,.9);if(t>1.6&&t<2.4)shake('#h0',1.6,.6);
 vis('#cB',3.5,14.95);vis('#ok',6.51,7.85);pop('#ok',6.51,1.6,X+' rotate(-6deg)');
 const mv=eo((t-11.6)/.45);$('#cB').style.left=(305-255*mv)+'px';
 $('#rB').textContent=brl(cnt(8.0,11.3,10000,4352));$('#rB').style.color=t>8?'#ff5a45':'#f4f3ee';
 vis('#cs',7.93,11.5);
 vis('#cA',11.69,14.95);$('#cA').style.transform='translateX('+(500*(1-eo((t-11.69)/.4)))+'px)';
 vis('#mais',13.3,14.95);pop('#mais',13.3,1.6);
 vis('#h3',15.05,17.45);pop('#h3',15.05,.85);if(t>16.35)shake('#h3',16.35,.5);
 vis('#ph',17.5,20.35);$('#ph').style.transform='translateY('+(60*(1-eo((t-17.5)/.4)))+'px)';
'''
V['g3'] = dict(TOT=23.1, END=20.35, FT0=3.4, FT='exemplo: custo de R$ 3,53 por km rodado', EL='O app faz a conta.<br>Você escolhe<br>o frete <span class="grn">certo</span>.', css='', html=g3html, anim=g3anim, SEG=[
 [0.1, 3.15, "Frete:2 bonito:3 é:1 / a:1 maior:2 armadilha:4 / do:1 caminhoneiro:5"], [3.5, 6.13, "R$_10_mil:5 pra:1 / 1.600_km:9"],
 [6.51, 7.5, "Parece:3 ótimo:3"], [7.93, 11.35, "Mas:1 tira:2 o:1 diesel:2 / o:1 pedágio:3 a:1 diária:3 / e:1 o:1 desgaste:3"],
 [11.69, 14.5, "sobra:2 menos:2 que:1 / um:1 frete:2 de:1 R$_7_mil:4 / pra:1 600_km:6"], [15.12, 16.09, "Quem:1 não:1 faz:1 a:1 conta:2"],
 [16.35, 17.08, "escolhe:3 errado:3"], [17.53, 19.98, "O:1 Diário_de_Bordo:5 / faz:1 essa:2 conta:2 pra:1 você:2"], [20.42, 21.66, "Toque:2 em:1 Saiba:2 mais:2"]])

for k, s in V.items():
    h = (BASE.replace('%%CSS%%', s['css']).replace('%%HTML%%', s['html']).replace('%%ANIM%%', s['anim'])
         .replace('%%TOT%%', str(s['TOT'])).replace('%%END%%', str(s['END'])).replace('%%FT0%%', str(s['FT0']))
         .replace('%%FT%%', s['FT']).replace('%%EL%%', s['EL']).replace('%%SEG%%', json.dumps(s['SEG'], ensure_ascii=False)))
    (here / f'index-{k}.html').write_text(h)
print('ok', list(V))
