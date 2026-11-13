# Vídeo 3D "Eu sei que você anota no caderninho": maquete 3D (Three.js) + legendas e cartões em HTML.
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
#subs .w{display:inline-block;margin:0 9px;opacity:0;border:4px solid transparent;border-radius:8px;padding:0 6px}
#subs .w.k.on{border-color:#f2b705}
#wm{position:absolute;font:700 38px B;color:#fff;opacity:.85;letter-spacing:1px;text-shadow:0 2px 6px rgba(0,0,0,.6);z-index:60;top:150px}
#ex{position:absolute;left:0;right:0;top:1500px;text-align:center;font:700 30px B;color:#fff;letter-spacing:2px;z-index:55;text-shadow:0 2px 6px rgba(0,0,0,.8)}
.chip{position:absolute;left:0;right:0;top:470px;text-align:center;z-index:40;opacity:0}
.chip span{display:inline-block;background:#16181b;color:#f4f3ee;font:800 92px/1 BC;text-transform:uppercase;padding:22px 44px 12px;border-radius:26px;box-shadow:0 14px 0 rgba(0,0,0,.3);white-space:nowrap}
.chip b{color:#ff7a66}
#note{position:absolute;left:170px;top:880px;width:740px;height:620px;background:#fbf6e6;border-radius:14px;box-shadow:0 24px 0 rgba(0,0,0,.25);padding:34px 56px;color:#203a63;z-index:30;opacity:0;
 background-image:repeating-linear-gradient(180deg,transparent 0 92px,#b9d3ea 92px 96px);background-position:0 40px;transform-origin:50% 50%}
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
<script type="module">
import * as THREE from './three.module.min.js';
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const cl=x=>Math.max(0,Math.min(1,x)), eo=x=>1-Math.pow(1-cl(x),3), eio=x=>{x=cl(x);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2};
const back=x=>{x=cl(x);const c=1.6;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
const ws=i=>WORDS.find(w=>w.id==i).start, we=i=>WORDS.find(w=>w.id==i).end;
await document.fonts.load('800 80px BC'); await document.fonts.load('700 40px B');
const cv=$('#gl');
const R=new THREE.WebGLRenderer({canvas:cv,antialias:true,alpha:true,preserveDrawingBuffer:true});
R.setPixelRatio(1); R.setSize(cv.width,cv.height,false); R.shadowMap.enabled=true; R.shadowMap.type=THREE.PCFSoftShadowMap;
R.outputColorSpace=THREE.SRGBColorSpace;
const S=new THREE.Scene(); S.fog=new THREE.Fog(0xcfe6f2,70,160);
const cam=new THREE.PerspectiveCamera(38,cv.width/cv.height,0.1,400);
S.add(new THREE.HemisphereLight(0xffffff,0x6a8a5a,1.35));
const sun=new THREE.DirectionalLight(0xfff2d6,2.1); sun.position.set(30,50,30); sun.castShadow=true;
sun.shadow.mapSize.set(2048,2048); Object.assign(sun.shadow.camera,{left:-60,right:60,top:60,bottom:-60,near:1,far:200}); sun.shadow.bias=-0.0005; S.add(sun); S.add(sun.target);
const M=c=>new THREE.MeshStandardMaterial({color:c,roughness:.85,metalness:0});
function box(w,h,d,c,x=0,y=0,z=0,p=S){const m=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),M(c));m.position.set(x,y,z);m.castShadow=true;m.receiveShadow=true;p.add(m);return m}
function cyl(r,h,c,x,y,z,p=S,seg=20){const m=new THREE.Mesh(new THREE.CylinderGeometry(r,r,h,seg),M(c));m.position.set(x,y,z);m.castShadow=true;m.receiveShadow=true;p.add(m);return m}
function sign(txt,w,h,bg,fg,x,y,z,p=S,ry=0){const c=document.createElement('canvas');c.width=512;c.height=Math.round(512*h/w);const g=c.getContext('2d');g.fillStyle=bg;g.fillRect(0,0,c.width,c.height);g.fillStyle=fg;
 let fs=c.height*.72;g.font='800 '+fs+'px BC';while(g.measureText(txt).width>c.width*.9){fs-=4;g.font='800 '+fs+'px BC'}g.textAlign='center';g.textBaseline='middle';g.fillText(txt,c.width/2,c.height*.56);
 const t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;const m=new THREE.Mesh(new THREE.BoxGeometry(w,h,.2),[M(bg),M(bg),M(bg),M(bg),new THREE.MeshStandardMaterial({map:t,roughness:.8}),M(bg)]);m.position.set(x,y,z);m.rotation.y=ry;m.castShadow=true;p.add(m);return m}
// chão e estrada
const gr=new THREE.Mesh(new THREE.PlaneGeometry(400,400),M(0x7cbf5a));gr.rotation.x=-Math.PI/2;gr.receiveShadow=true;S.add(gr);
const rd=new THREE.Mesh(new THREE.PlaneGeometry(400,7),M(0x4a4f57));rd.rotation.x=-Math.PI/2;rd.position.set(60,0.02,0);rd.receiveShadow=true;S.add(rd);
for(let x=-60;x<200;x+=5){const d=box(2.4,.05,.35,0xf2d14b,x,.05,0);d.castShadow=false}
for(const z of [-3.7,3.7]){const c=box(400,.25,.5,0xd9d4c4,60,.12,z);c.castShadow=false}
// árvores
const rnd=(s=>()=>(s=(s*16807)%2147483647)/2147483647)(7);
for(let i=0;i<70;i++){const x=-30+rnd()*130,z=(rnd()<.5?-1:1)*(14+rnd()*30);const g=new THREE.Group();g.position.set(x,0,z);S.add(g);cyl(.25,1.4,0x7a5532,0,.7,0,g,8);
 const k=new THREE.Mesh(new THREE.ConeGeometry(1.3+rnd()*.6,3+rnd()*1.5,7),M([0x3f8f4a,0x4fa458,0x2f7a3f][i%3]));k.position.y=2.8;k.castShadow=true;g.add(k)}
// caminhão
function truck(){const g=new THREE.Group();
 box(9,3,2.8,0xf4f1ea,-1.6,2.6,0,g); box(9,.35,2.8,0xf2b705,-1.6,1.25,0,g);
 const cab=new THREE.Group();cab.position.x=4.3;g.add(cab);box(2.6,2.9,2.8,0xf2b705,0,2.5,0,cab);box(.1,1.2,2.2,0x2b4553,1.31,3.1,0,cab);box(.9,1.1,2.8,0xf2b705,1.5,1.6,0,cab);
 box(.15,.4,.5,0xfff6c8,1.98,1.6,.95,cab);box(.15,.4,.5,0xfff6c8,1.98,1.6,-.95,cab);box(2.6,.3,2.9,0x16181b,0,1.0,0,cab);
 for(const x of [-5,-3.8,-2.6,3.6,5.2]) for(const z of [1.35,-1.35]){const w=cyl(.62,.5,0x16181b,x,.62,z,g,18);w.rotation.x=Math.PI/2;const h=cyl(.28,.52,0x9aa0a8,x,.62,z,g,12);h.rotation.x=Math.PI/2}
 return g}
const T=truck();T.traverse(o=>{if(o.isMesh)o.castShadow=true});S.add(T);T.position.set(0,0,0);
// pilha de dinheiro em cima da carreta
const MON=new THREE.Group();MON.position.set(-1.6,4.1,0);T.add(MON);const LAY=[];
const bill=()=>{const c=document.createElement('canvas');c.width=256;c.height=128;const g=c.getContext('2d');g.fillStyle='#4fb070';g.fillRect(0,0,256,128);g.strokeStyle='#2f7a4a';g.lineWidth=10;g.strokeRect(10,10,236,108);g.fillStyle='#2f7a4a';g.font='800 70px BC';g.textAlign='center';g.fillText('R$',128,90);const t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;return t};
const BT=bill();const billMat=[M(0x3f9a5e),M(0x3f9a5e),new THREE.MeshStandardMaterial({map:BT}),M(0x3f9a5e),M(0x58b97a),M(0x58b97a)];
for(let i=0;i<16;i++){const m=new THREE.Mesh(new THREE.BoxGeometry(3.4,.32,2.0),billMat);m.position.y=i*.34;m.castShadow=true;MON.add(m);LAY.push(m)}
// pedaços que voam
const FLY=[];
// Zé
function ze(){const g=new THREE.Group();
 box(.42,1.5,.5,0x2c3e66,-.27,.75,0,g);box(.42,1.5,.5,0x2c3e66,.27,.75,0,g);box(.5,.25,.7,0x3a2a1c,-.27,.12,.1,g);box(.5,.25,.7,0x3a2a1c,.27,.12,.1,g);
 box(1.25,1.4,.75,0x3b6db3,0,2.2,0,g);
 const aL=new THREE.Group();aL.position.set(-.78,2.8,0);g.add(aL);box(.36,1.3,.42,0x3b6db3,0,-.55,0,aL);box(.34,.32,.38,0xc98d62,0,-1.3,0,aL);
 const aR=new THREE.Group();aR.position.set(.78,2.8,0);g.add(aR);box(.36,1.3,.42,0x3b6db3,0,-.55,0,aR);box(.34,.32,.38,0xc98d62,0,-1.3,0,aR);
 const hd=new THREE.Group();hd.position.y=3.35;g.add(hd);box(.95,.95,.9,0xc98d62,0,0,0,hd);
 box(.13,.16,.05,0x1b1b1b,-.2,.08,.46,hd);box(.13,.16,.05,0x1b1b1b,.2,.08,.46,hd);box(.55,.12,.06,0x3a2a1c,0,-.16,.47,hd);box(.3,.1,.05,0x8a4a3a,0,-.32,.46,hd);
 box(1.0,.32,.95,0xf2b705,0,.6,0,hd);box(1.0,.08,.55,0xf2b705,0,.46,.7,hd);box(.3,.2,.04,0x16181b,0,.62,.48,hd);
 box(.12,.4,.6,0x6b6b6b,-.5,.1,0,hd);box(.12,.4,.6,0x6b6b6b,.5,.1,0,hd);
 g.userData={aL,aR,hd};return g}
const Z=ze();Z.position.set(-2.5,0,3.6);Z.rotation.y=.25;S.add(Z);
// posto
const P=new THREE.Group();P.position.set(18,0,-7.5);S.add(P);box(10,.3,6,0xd9d4c4,0,.15,0,P);
for(const x of [-4,4])for(const z of [-2,2])cyl(.25,4.6,0xe8e3d6,x,2.4,z,P,10);box(10.5,.8,6.5,0xe04b3a,0,4.9,0,P);box(10.5,.25,6.5,0xf4f1ea,0,4.4,0,P);
sign('DIESEL',4,1.1,'#16181b','#f2b705',0,4.9,3.31,P);for(const x of [-2,2]){box(1,2,.8,0xf4f1ea,x,1.3,0,P);box(1,.4,.8,0xf2b705,x,2.2,0,P)}
const tot=new THREE.Group();tot.position.set(-6.5,0,1);P.add(tot);cyl(.2,6,0x9aa0a8,0,3,0,tot,8);sign('R$ 7,00',2.8,1.2,'#16181b','#f4f3ee',0,5.6,0,tot);
// pedágio
const Q=new THREE.Group();Q.position.set(32,0,0);S.add(Q);
for(const z of [-5.3,5.3])box(1.2,5.5,1.2,0xc9c5ba,0,2.75,z,Q);
const band=document.createElement('canvas');band.width=512;band.height=64;{const g=band.getContext('2d');for(let i=0;i<16;i++){g.fillStyle=i%2?'#16181b':'#f2b705';g.beginPath();g.moveTo(i*32,64);g.lineTo(i*32+32,0);g.lineTo(i*32+64,0);g.lineTo(i*32+32,64);g.fill()}}
const bt=new THREE.CanvasTexture(band);bt.colorSpace=THREE.SRGBColorSpace;const bm=new THREE.Mesh(new THREE.BoxGeometry(1.6,1,12),[M(0xf2b705),M(0xf2b705),M(0xf2b705),M(0xf2b705),new THREE.MeshStandardMaterial({map:bt}),new THREE.MeshStandardMaterial({map:bt})]);bm.rotation.y=Math.PI/2;bm.rotation.y=0;bm.position.set(0,5.9,0);bm.castShadow=true;Q.add(bm);
sign('PEDÁGIO',4.4,1.2,'#f2b705','#16181b',0,7.1,0,Q,Math.PI/2);
box(2,3,2.2,0xf4f1ea,0,1.5,-6.8,Q);box(2.1,.3,2.4,0xe04b3a,0,3.1,-6.8,Q);
const arm=new THREE.Group();arm.position.set(-1.2,1.3,-4.6);Q.add(arm);box(.3,.3,4.4,0xf4f1ea,0,0,2.2,arm);for(const z of [1,2.6,4])box(.32,.32,.6,0xe04b3a,0,0,z,arm);
// borracharia
const BR=new THREE.Group();BR.position.set(46,0,-8.5);S.add(BR);box(8,4.2,5,0xe8e3d6,0,2.1,0,BR);box(8.4,.4,5.4,0x2b4553,0,4.4,0,BR);sign('BORRACHARIA',6.6,1.3,'#16181b','#f2b705',0,3.3,2.61,BR);
const TIRES=[];for(let i=0;i<6;i++){const tt=new THREE.Mesh(new THREE.TorusGeometry(.8,.35,10,20),M(0x1d1f22));tt.rotation.x=Math.PI/2;tt.position.set(5.6,.35+i*.72,1.5);tt.castShadow=true;BR.add(tt);TIRES.push(tt)}
// oficina
const OF=new THREE.Group();OF.position.set(60,0,-9);S.add(OF);box(11,5.5,6,0xd9d4c4,0,2.75,0,OF);box(11.4,.5,6.4,0xe04b3a,0,5.75,0,OF);sign('OFICINA',6,1.4,'#e04b3a','#f4f3ee',0,4.6,3.05,OF);
box(5.6,3.6,.1,0x2b2f36,-1.6,1.8,3.0,OF);const door=box(5.6,3.6,.2,0x9aa0a8,-1.6,1.8,3.12,OF);
for(const [x,c] of [[3.6,0xe04b3a],[4.6,0x3b6db3],[4.1,0xf2b705]]){cyl(.45,1.3,c,x,.65,3.8+(x==4.1?1:0),OF,14)}
const WR=new THREE.Group();WR.position.set(2.4,4.2,3.4);OF.add(WR);box(.3,1.4,.2,0x9aa0a8,0,0,0,WR);box(.8,.3,.2,0x9aa0a8,0,.7,0,WR);
// alerta (caminhão cobra depois)
const AL=new THREE.Group();S.add(AL);{const c=document.createElement('canvas');c.width=256;c.height=256;const g=c.getContext('2d');g.fillStyle='#e04b3a';g.beginPath();g.moveTo(128,10);g.lineTo(246,236);g.lineTo(10,236);g.fill();g.fillStyle='#fff';g.font='800 170px BC';g.textAlign='center';g.fillText('!',128,220);
 const t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;const sp=new THREE.Sprite(new THREE.SpriteMaterial({map:t}));sp.scale.set(3,3,1);AL.add(sp)}
const SMK=[];for(let i=0;i<6;i++){const s=new THREE.Mesh(new THREE.SphereGeometry(.6,10,8),new THREE.MeshStandardMaterial({color:0x777777,transparent:true,opacity:.6}));S.add(s);SMK.push(s)}
// trajetória do caminhão
const TK=[[0,0],[9.6,0],[11.2,16],[12.9,16],[13.5,24],[15.3,30.5],[17.8,44],[20.3,44],[20.6,58.5],[44.3,58.5],[47.6,95]];
function lerpK(K,t){for(let i=0;i<K.length-1;i++){const [a,va]=K[i],[b,vb]=K[i+1];if(t<=b){return va+(vb-va)*eio((t-a)/(b-a))}}return K[K.length-1][1]}
// eventos de dinheiro: [tempo, valor, destino]
const EV=[[ws(29),5520,new THREE.Vector3(18,2,-7.5)],[ws(34),1200,new THREE.Vector3(32,3,-6.8)],[ws(46),300,new THREE.Vector3(51.6,2,-7)],[ws(53),200,new THREE.Vector3(58,2,-6)],[ws(57),200,new THREE.Vector3(58,2,-6)]];
for(const e of EV){const n=Math.max(1,Math.round(e[1]/500));const g=new THREE.Group();for(let i=0;i<n;i++){const m=new THREE.Mesh(new THREE.BoxGeometry(3.4,.32,2.0),billMat);m.position.y=i*.34;m.castShadow=true;g.add(m)}g.visible=false;S.add(g);FLY.push(g)}
function money(t){let v=8000;EV.forEach(e=>{if(t>=e[0]+.15)v-=e[1]});return v}
// câmera: [t, pos, alvo]
const V=(x,y,z)=>new THREE.Vector3(x,y,z);
const CK=[[0,V(2.5,3.6,17),V(-1.6,1.8,2.6)],[4.9,V(1.6,3.5,15),V(-1.7,1.9,2.6)],[5.6,V(1.6,3.6,15),V(-1.7,2.0,2.6)],[7.6,V(8,22,32),V(4,2,-2)],[9.4,V(6,18,28),V(1,3,-1)],
 [11.0,V(26,16,26),V(17,2,-4)],[12.9,V(27,16,25),V(18,2,-4)],[13.6,V(40,15,25),V(31,2,-2)],[15.2,V(41,16,25),V(31,2,-2)],[17.6,V(56,24,34),V(44,1,-3)],
 [18.4,V(54,15,25),V(45,2,-4)],[20.4,V(55,15,24),V(46,2,-4)],[21.0,V(68,15,25),V(58,2,-4)],[24.3,V(69,14,24),V(58,2,-4)],[25.2,V(63,10,13),V(56.5,3.8,0)],[27.6,V(62,9.5,12.5),V(56.5,3.8,0)],
 [30.4,V(66,12,18),V(58,3,0)],[32.4,V(68,14,22),V(58,2,0)],[44.0,V(70,15,26),V(58,2,0)],[47.6,V(96,14,28),V(98,2,0)]];
function camAt(t){for(let i=0;i<CK.length-1;i++){const [a,pa,ta]=CK[i],[b,pb,tb]=CK[i+1];if(t<=b){const k=eio((t-a)/(b-a));return [pa.clone().lerp(pb,k),ta.clone().lerp(tb,k)]}}const l=CK[CK.length-1];return [l[1].clone(),l[2].clone()]}
// legenda
const PH=[];(()=>{let g=[];WORDS.forEach(w=>{g.push(w);if(/[.,:?]$/.test(w.text)&&g.length>=3||/[.:?]$/.test(w.text)){PH.push(g);g=[]}});if(g.length)PH.push(g)})();
const subs=$('#subs');let cur=-1;
const show=(el,a,b,t,mode)=>{const on=t>=a&&t<=b;const u=t-a;const o=on?Math.min(cl(u/.15),cl((b-t)/.2)):0;el.style.opacity=o;if(on&&mode!='none')el.style.transform='scale('+(0.7+0.3*back(u/.35))+')';return on};
window.render=function(t){
 // caminhão e Zé
 const x=lerpK(TK,t);T.position.x=x;const moving=Math.abs(lerpK(TK,t+.05)-x)>.01;
 T.children.forEach(c=>{if(c.geometry&&c.geometry.type=='CylinderGeometry')c.rotation.y=-x*1.6});
 T.position.y=moving?Math.abs(Math.sin(t*18))*.04:0;
 const zd=Z.userData;zd.hd.rotation.z=(t>ws(11)&&t<we(14)+.6)?.25*eo((t-ws(11))/.3):Math.sin(t*1.7)*.05;zd.aR.rotation.x=t<5?-.9-Math.sin(t*9)*.2:-0.1*Math.sin(t*2);zd.aL.rotation.z=Math.sin(t*1.3)*.05;Z.position.y=Math.abs(Math.sin(t*2.2))*.03;
 Z.visible=t<9.5;
 // dinheiro
 const v=money(t);const n=v/500;LAY.forEach((m,i)=>{m.visible=i<Math.ceil(n-1e-6);m.scale.y=1;if(i==Math.ceil(n)-1&&n%1>0){m.scale.y=Math.max(.25,n%1)}});
 const pop=cl((t-ws(15))/.5);MON.scale.setScalar(t<ws(15)?0.001:0.4+0.6*back((t-ws(15))/.5));
 EV.forEach((e,k)=>{const g=FLY[k];const u=(t-e[0]-.15)/1.1;if(u<0||u>1){g.visible=false;return}g.visible=true;
  const st=new THREE.Vector3(T.position.x-1.6,4.1+n*.34,0);const p=st.clone().lerp(e[2],eo(u));p.y+=Math.sin(u*Math.PI)*6;g.position.copy(p);g.rotation.y=u*6;g.scale.setScalar(1-.6*u)});
 // cenário animado
 arm.rotation.x=0;arm.rotation.z=0;arm.rotation.y=0;const up=cl((t-13.7)/.5)-cl((t-15.0)/.5);arm.rotation.x=-1.3*eo(up);
 TIRES.forEach((tt,i)=>{tt.rotation.z=(t>18?(t-18):0)*(i%2?1:-1)*.6});door.position.y=1.8+3.2*eo((t-20.4)/.8);door.scale.y=1-.9*eo((t-20.4)/.8);
 WR.rotation.z=Math.sin(t*10)*(t>20.8&&t<24.3?.6:0);
 // alerta
 const al=t>=ws(78)&&t<we(80)+1.2;AL.visible=al;AL.position.set(T.position.x-1,9+Math.sin(t*6)*.3,0);AL.scale.setScalar(al?back((t-ws(78))/.4):1);
 SMK.forEach((s,i)=>{const u=((t*0.8+i/6)%1);s.visible=al;s.position.set(T.position.x+5.4-u*2,3+u*4,1.2);s.scale.setScalar(.5+u*1.4);s.material.opacity=.6*(1-u)});
 // câmera
 const [cp,ct]=camAt(t);cam.position.copy(cp);cam.lookAt(ct);sun.position.set(cp.x+20,50,30);sun.target.position.set(cp.x,0,0);
 R.render(S,cam);
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
