import * as THREE from 'three';
import { RoundedBoxGeometry } from './addons/RoundedBoxGeometry.js';
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const cl=x=>Math.max(0,Math.min(1,x)), eo=x=>1-Math.pow(1-cl(x),3), eio=x=>{x=cl(x);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2};
const back=x=>{x=cl(x);const c=1.6;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
const ws=i=>WORDS.find(w=>w.id==i).start, we=i=>WORDS.find(w=>w.id==i).end;
await document.fonts.load('800 80px BC'); await document.fonts.load('700 40px B');
const cv=$('#gl');
const R=new THREE.WebGLRenderer({canvas:cv,antialias:true,alpha:true,preserveDrawingBuffer:true});
R.setPixelRatio(1);R.setSize(cv.width,cv.height,false);R.shadowMap.enabled=true;R.shadowMap.type=THREE.PCFSoftShadowMap;
R.outputColorSpace=THREE.SRGBColorSpace;R.toneMapping=THREE.ACESFilmicToneMapping;R.toneMappingExposure=1.05;
const S=new THREE.Scene();S.fog=new THREE.Fog(0xd8ecf6,80,190);
const cam=new THREE.PerspectiveCamera(34,cv.width/cv.height,0.1,500);
S.add(new THREE.HemisphereLight(0xcfeaff,0x5f7f45,1.15));
const sun=new THREE.DirectionalLight(0xffe9c7,2.8);sun.castShadow=true;sun.shadow.mapSize.set(4096,4096);
Object.assign(sun.shadow.camera,{left:-45,right:45,top:45,bottom:-45,near:1,far:220});sun.shadow.bias=-0.0004;sun.shadow.normalBias=0.03;sun.shadow.radius=4;S.add(sun);S.add(sun.target);
const fill=new THREE.DirectionalLight(0xbfd8ff,.6);fill.position.set(-30,20,-20);S.add(fill);
const key=new THREE.DirectionalLight(0xfff4e6,.9);S.add(key);S.add(key.target);

// ---------- helpers ----------
const MC={};
const M=(c,o={})=>{const k=c+JSON.stringify(o);if(!MC[k])MC[k]=new THREE.MeshStandardMaterial(Object.assign({color:c,roughness:.72,metalness:0},o));return MC[k]};
const MET=c=>M(c,{roughness:.3,metalness:.85});
function add(geo,mat,x,y,z,p,sh=true){const m=new THREE.Mesh(geo,mat);m.position.set(x,y,z);m.castShadow=sh;m.receiveShadow=true;p.add(m);return m}
const rbox=(w,h,d,r,c,x,y,z,p,mat)=>add(new RoundedBoxGeometry(w,h,d,3,Math.min(r,w/2-.001,h/2-.001,d/2-.001)),mat||M(c),x,y,z,p);
const cyl=(rt,rb,h,c,x,y,z,p,seg=24,mat)=>add(new THREE.CylinderGeometry(rt,rb,h,seg),mat||M(c),x,y,z,p);
const sph=(r,c,x,y,z,p,mat,ws=24,hs=18)=>add(new THREE.SphereGeometry(r,ws,hs),mat||M(c),x,y,z,p);
const cap=(r,l,c,x,y,z,p,mat)=>add(new THREE.CapsuleGeometry(r,l,6,16),mat||M(c),x,y,z,p);
function tex(w,h,draw){const c=document.createElement('canvas');c.width=w;c.height=h;draw(c.getContext('2d'),w,h);const t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;t.anisotropy=8;return t}
function signTex(txt,bg,fg,w=1024,h=256){return tex(w,h,(g,W,H)=>{g.fillStyle=bg;g.fillRect(0,0,W,H);g.fillStyle=fg;let fs=H*.68;g.font='800 '+fs+'px BC';while(g.measureText(txt).width>W*.86){fs-=4;g.font='800 '+fs+'px BC'}g.textAlign='center';g.textBaseline='middle';g.fillText(txt,W/2,H*.56)})}
function sign(txt,w,h,bg,fg,x,y,z,p,ry=0){const g=new THREE.Group();g.position.set(x,y,z);g.rotation.y=ry;p.add(g);rbox(w+.3,h+.3,.25,.1,0x2a2d33,0,0,-.05,g);
 const pl=add(new THREE.PlaneGeometry(w,h),new THREE.MeshStandardMaterial({map:signTex(txt,bg,fg,1024,Math.round(1024*h/w)),roughness:.6}),0,0,.09,g,false);return g}

// ---------- chão ----------
const gGeo=new THREE.PlaneGeometry(460,460,120,120);gGeo.rotateX(-Math.PI/2);
{const col=[];const p=gGeo.attributes.position;const a=new THREE.Color(0x86c45f),b=new THREE.Color(0x6aae4c),c2=new THREE.Color();
 for(let i=0;i<p.count;i++){const x=p.getX(i),z=p.getZ(i);const n=(Math.sin(x*.21)+Math.sin(z*.17+x*.05)+Math.sin((x+z)*.09))/3*.5+.5;c2.copy(a).lerp(b,n);col.push(c2.r,c2.g,c2.b)}
 gGeo.setAttribute('color',new THREE.Float32BufferAttribute(col,3))}
const ground=new THREE.Mesh(gGeo,new THREE.MeshStandardMaterial({vertexColors:true,roughness:.95}));ground.receiveShadow=true;ground.position.x=60;S.add(ground);
// estrada
const asph=tex(1024,256,(g,W,H)=>{g.fillStyle='#4b5059';g.fillRect(0,0,W,H);for(let i=0;i<5000;i++){const v=60+Math.random()*40;g.fillStyle=`rgba(${v},${v+4},${v+10},.35)`;g.fillRect(Math.random()*W,Math.random()*H,2,2)}
 g.fillStyle='#f4f1ea';g.fillRect(0,18,W,10);g.fillRect(0,H-28,W,10);g.fillStyle='#f2c230';for(let x=0;x<W;x+=128)g.fillRect(x,H/2-6,72,12)});
asph.wrapS=THREE.RepeatWrapping;asph.repeat.set(30,1);
const road=add(new THREE.PlaneGeometry(420,8),new THREE.MeshStandardMaterial({map:asph,roughness:.9}),60,.03,0,S,false);road.rotation.x=-Math.PI/2;road.receiveShadow=true;
for(const z of [-4.6,4.6]){const c=rbox(420,.3,1.2,.1,0xd8d2c2,60,.15,z,S);c.castShadow=false}
// postes e cercas
for(let x=-40;x<180;x+=14){const g=new THREE.Group();g.position.set(x,0,-6.2);S.add(g);cyl(.12,.15,6,0x8a8f98,0,3,0,g,10);rbox(1.6,.2,.3,.08,0x8a8f98,.6,5.9,0,g);add(new THREE.SphereGeometry(.22,12,10),M(0xfff4d0,{emissive:0xfff0b0,emissiveIntensity:.4}),1.3,5.75,0,g)}
for(let x=-40;x<180;x+=2.4){if(x>12&&x<70)continue;rbox(.18,1.1,.18,.05,0xb98a5a,x,.55,7.2,S);}
for(const y of [.45,.85]){rbox(220,.12,.08,.03,0xb98a5a,70,y,7.2,S)}
// natureza
const rnd=(s=>()=>(s=(s*16807)%2147483647)/2147483647)(11);
const leaf=[0x4f9e4a,0x5cae4f,0x3e8a45,0x6dbb54];
function tree(x,z,s=1){const g=new THREE.Group();g.position.set(x,0,z);g.scale.setScalar(s);S.add(g);cyl(.22,.32,2.2,0x7a5532,0,1.1,0,g,10);
 const k=new THREE.IcosahedronGeometry(1.5,1);const m=M(leaf[Math.floor(rnd()*4)],{flatShading:true,roughness:.85});
 add(k,m,0,3.1,0,g);add(new THREE.IcosahedronGeometry(1.1,1),m,.8,2.6,.3,g);add(new THREE.IcosahedronGeometry(1.0,1),m,-.7,2.8,-.2,g);return g}
for(let i=0;i<110;i++){const x=-40+rnd()*200;const side=rnd()<.5?-1:1;const z=side*(15+rnd()*45);if(side<0&&z>-16)continue;tree(x,z,.8+rnd()*.7)}
for(let i=0;i<60;i++){const x=-40+rnd()*200,z=(rnd()<.5?-1:1)*(9+rnd()*30);add(new THREE.IcosahedronGeometry(.5+rnd()*.5,1),M(0x5aa84e,{flatShading:true}),x,.35,z,S)}
for(let i=0;i<30;i++){const x=-40+rnd()*200,z=(rnd()<.5?-1:1)*(8+rnd()*30);add(new THREE.DodecahedronGeometry(.3+rnd()*.4,0),M(0x9a9690,{flatShading:true}),x,.2,z,S)}
// montanhas e nuvens
for(let i=0;i<14;i++){const m=add(new THREE.ConeGeometry(18+rnd()*14,22+rnd()*16,7),M(0x8fb7a8,{flatShading:true,roughness:1}),-60+i*22,9,-110-rnd()*20,S,false)}
const CLOUDS=[];for(let i=0;i<14;i++){const g=new THREE.Group();g.position.set(-40+i*16+rnd()*8,26+rnd()*10,-50-rnd()*40);S.add(g);for(let k=0;k<5;k++)add(new THREE.IcosahedronGeometry(2+rnd()*2,1),M(0xffffff,{flatShading:true,roughness:1,emissive:0xffffff,emissiveIntensity:.25}),k*2.4-5,rnd()*1.2,rnd()*1.5,g,false);CLOUDS.push(g)}

// ---------- caminhão ----------
const WHEELS=[];
function wheel(x,z,p){const g=new THREE.Group();g.position.set(x,.68,z);p.add(g);const t=cyl(.68,.68,.55,0x1a1c1f,0,0,0,g,28);t.rotation.x=Math.PI/2;
 const r=cyl(.38,.38,.57,0,0,0,0,g,20,MET(0xc9ccd2));r.rotation.x=Math.PI/2;const h=cyl(.14,.14,.6,0x5a5e66,0,0,0,g,12);h.rotation.x=Math.PI/2;
 for(let k=0;k<5;k++){const b=sph(.05,0x2a2d33,Math.cos(k*1.256)*.24,Math.sin(k*1.256)*.24,(z>0?.29:-.29),g)}WHEELS.push(g);return g}
function truck(){const g=new THREE.Group();
 rbox(13,.35,1.4,.1,0x24272d,.4,1.05,0,g);
 // carreta
 rbox(9.4,3.3,2.9,.18,0xf6f4ee,-2.1,3.0,0,g);
 for(let x=-6.4;x<=2.2;x+=.72){rbox(.08,3.0,2.96,.03,0xe1ded6,x,3.0,0,g)}
 rbox(9.5,.32,2.95,.08,0xf2b705,-2.1,1.5,0,g);rbox(9.5,.12,2.95,.04,0xe04b3a,-2.1,1.3,0,g);
 rbox(2.2,.5,.15,.05,0x8a8f98,-5,1.0,1.3,g);rbox(2.2,.5,.15,.05,0x8a8f98,-5,1.0,-1.3,g);
 // cavalo
 const Y=0xf2b705;
 rbox(2.8,2.9,2.8,.35,Y,4.7,2.75,0,g);rbox(2.4,.7,2.6,.3,Y,4.5,4.45,0,g);
 rbox(1.4,1.5,2.7,.3,Y,6.6,1.95,0,g);
 const glass=M(0x2a4a63,{roughness:.15,metalness:.4});
 add(new RoundedBoxGeometry(.12,1.15,2.3,2,.05),glass,6.1,3.35,0,g).rotation.z=-.12;
 for(const z of [1.41,-1.41])add(new RoundedBoxGeometry(1.3,.95,.06,2,.03),glass,5.0,3.4,z,g);
 rbox(.12,1.0,1.9,.05,0x1d1f23,7.3,1.95,0,g);for(let y=1.6;y<=2.35;y+=.18)rbox(.14,.06,1.8,.02,0,7.32,y,0,g,MET(0xd0d3d8));
 for(const z of [.95,-.95]){add(new THREE.SphereGeometry(.2,16,12),M(0xfff6c8,{emissive:0xfff2b0,emissiveIntensity:1.2}),7.28,1.45,z,g).scale.set(.5,1,1.3)}
 rbox(.4,.45,2.9,.15,0,7.35,1.0,0,g,MET(0xb8bcc4));
 for(const z of [1.55,-1.55]){rbox(.1,.7,.35,.06,0x1d1f23,6.0,3.4,z*1.02,g);rbox(.5,.06,.06,.03,0x1d1f23,6.0,3.4,z*.95,g)}
 for(const z of [1.15,-1.15]){cyl(.13,.13,2.6,0,3.15,4.3,z,g,14,MET(0xd0d3d8))}
 rbox(1.6,.08,2.85,.04,0x2a2d33,4.7,1.3,0,g);
 for(const z of [1.45,-1.45]){rbox(1.5,.6,.12,.05,0x2a2d33,4.0,1.6,z,g)}
 for(const x of [-5.7,-4.4,-3.1])for(const z of [1.25,-1.25])wheel(x,z,g);
 for(const x of [3.9,6.3])for(const z of [1.25,-1.25])wheel(x,z,g);
 return g}
const T=truck();S.add(T);
// dinheiro
const bandTex=tex(256,128,(g,W,H)=>{const gr=g.createLinearGradient(0,0,0,H);gr.addColorStop(0,'#5cc483');gr.addColorStop(1,'#3e9e64');g.fillStyle=gr;g.fillRect(0,0,W,H);g.strokeStyle='#2c7a4a';g.lineWidth=8;g.strokeRect(12,12,W-24,H-24);g.fillStyle='#2c7a4a';g.font='800 64px BC';g.textAlign='center';g.fillText('R$',W/2,H*.68);g.fillStyle='#f4f1ea';g.fillRect(W*.62,0,26,H)});
const billM=new THREE.MeshStandardMaterial({map:bandTex,roughness:.7});
function bundle(p,x,y,z){const m=add(new RoundedBoxGeometry(1.6,.34,2.0,2,.06),billM,x,y,z,p);return m}
const MON=new THREE.Group();MON.position.set(-2.1,4.68,0);T.add(MON);const LAY=[];
for(let i=0;i<16;i++){const l=new THREE.Group();l.position.y=i*.36;MON.add(l);bundle(l,-.85,0,0);bundle(l,.85,0,0);LAY.push(l)}
// ---------- Zé ----------
const SKIN=0xe2a97c, BLUE=0x2f6fb5, JEANS=0x34507a;
function ze(){const g=new THREE.Group();
 for(const x of [-.3,.3]){rbox(.55,.36,.85,.15,0x4a3222,x,.18,.12,g);cap(.25,.75,JEANS,x,.95,0,g)}
 rbox(1.4,1.55,.95,.42,BLUE,0,2.2,0,g);rbox(1.42,.18,.97,.08,0x3a2a1c,0,1.48,0,g);rbox(.22,.14,.1,.04,0,0,1.48,.5,g,MET(0xd8c070));
 rbox(.75,.22,.5,.1,0xf4f1ea,0,2.95,.18,g);rbox(.08,.5,.06,.03,0xf4f1ea,0,2.65,.48,g);
 const arms=[];for(const s of [-1,1]){const a=new THREE.Group();a.position.set(s*.86,2.75,0);g.add(a);cap(.22,.75,BLUE,0,-.5,0,a);sph(.2,SKIN,0,-1.05,0,a);arms.push(a)}
 cyl(.2,.22,.3,SKIN,0,3.05,0,g,16);
 const hd=new THREE.Group();hd.position.y=3.65;g.add(hd);
 sph(.72,SKIN,0,0,0,hd).scale.set(1,1.04,.95);
 for(const s of [-1,1]){sph(.17,SKIN,s*.7,0,0,hd).scale.set(.6,1,1);sph(.1,0x9a9a9a,s*.66,.22,-.05,hd).scale.set(.6,1.6,1.4)}
 const eyes=[];for(const s of [-1,1]){const e=new THREE.Group();e.position.set(s*.24,.1,.6);hd.add(e);sph(.13,0xffffff,0,0,0,e).scale.set(1,1.15,.55);sph(.075,0x1a1a1a,0,0,.05,e);sph(.025,0xffffff,.03,.04,.1,e);eyes.push(e);
  const b=rbox(.3,.08,.08,.04,0x3a2a1c,s*.25,.36,.62,hd);b.rotation.z=-s*.1}
 sph(.14,0xc4875c,0,-.08,.7,hd);
 for(const s of [-1,1]){const m=cap(.065,.24,0x5a3a26,s*.15,-.27,.66,hd);m.rotation.z=Math.PI/2+s*.3}
 const mouth=sph(.09,0x8a3f35,0,-.45,.6,hd);mouth.scale.set(1.4,.6,.6);
 // boné
 const dome=add(new THREE.SphereGeometry(.75,28,14,0,Math.PI*2,0,Math.PI/2),M(0xf2b705),0,.36,-.04,hd);dome.scale.set(1,.62,1);
 rbox(1.5,.14,.04,.03,0xe0a800,0,.2,0,hd).visible=false;
 const brim=cyl(.5,.5,.06,0xe8ad00,0,.38,.62,hd,28);brim.scale.set(1.2,1,.85);brim.rotation.x=.08;
 const logo=rbox(.3,.2,.04,.03,0x16181b,0,.62,.7,hd);logo.rotation.x=-.45;
 sph(.07,0xf2b705,0,.82,-.04,hd);
 g.userData={hd,arms,eyes,mouth};return g}
const Z=ze();Z.position.set(-1.8,0,3.4);Z.rotation.y=.18;S.add(Z);
const Z2=ze();Z2.position.set(68.5,0,1.8);Z2.rotation.y=-.35;S.add(Z2);
const PH3=rbox(.32,.58,.06,.04,0x16181b,0,-1.25,.25,Z2.userData.arms[1]);
// ---------- posto ----------
const P=new THREE.Group();P.position.set(18,0,-9);S.add(P);rbox(14,.3,8,.12,0xd9d4c4,0,.15,0,P);
for(const x of [-5,5])for(const z of [-2.5,2.5])cyl(.28,.28,5,0xf4f1ea,x,2.65,z,P,16);
rbox(13,1.0,7.6,.25,0xe04b3a,0,5.6,0,P);rbox(13.1,.3,7.7,.1,0xf4f1ea,0,5.0,0,P);
for(const x of [-4,0,4])add(new THREE.PlaneGeometry(2.2,.6),M(0xfffbe8,{emissive:0xfff3c0,emissiveIntensity:.8}),x,4.84,0,P,false).rotation.x=Math.PI/2;
sign('DIESEL',5,1.2,'#16181b','#f2b705',0,5.65,3.82,P);
for(const x of [-2.4,2.4]){const d=new THREE.Group();d.position.set(x,.3,0);P.add(d);rbox(1.3,2.4,.9,.15,0xf4f1ea,0,1.2,0,d);rbox(1.32,.45,.92,.12,0xf2b705,0,2.25,0,d);
 add(new THREE.PlaneGeometry(.9,.55),M(0x16181b,{emissive:0x1b3a2a,emissiveIntensity:.6}),0,1.6,.46,d,false);for(const s of [-1,1]){const h=cap(.06,.6,0x1d1f23,s*.7,1.1,0,d);}}
const tot=new THREE.Group();tot.position.set(-8.5,0,2.5);P.add(tot);cyl(.22,.22,7.2,0x9aa0a8,0,3.6,0,tot,12);sign('R$ 7,00',3,1.2,'#16181b','#f4f1ea',0,6.8,0,tot);sign('DIESEL S10',3,.7,'#e04b3a','#ffffff',0,5.8,0,tot);
rbox(4.5,3.2,4,.25,0xf4f1ea,0,1.75,-6.5,P);rbox(4.7,.4,4.2,.15,0xe04b3a,0,3.5,-6.5,P);add(new THREE.PlaneGeometry(2.6,1.4),M(0x2a4a63,{roughness:.2,metalness:.3}),0,1.9,-4.48,P,false);
// ---------- pedágio ----------
const Q=new THREE.Group();Q.position.set(32,0,0);S.add(Q);
const stripe=tex(512,64,(g,W,H)=>{for(let i=-2;i<18;i++){g.fillStyle=i%2?'#16181b':'#f2b705';g.beginPath();g.moveTo(i*32,H);g.lineTo(i*32+32,0);g.lineTo(i*32+64,0);g.lineTo(i*32+32,H);g.fill()}});
for(const z of [-6,6])rbox(1.4,6,1.4,.2,0xd9d4c4,0,3,z,Q);
rbox(2.2,1.3,13.4,.25,0xf2b705,0,6.4,0,Q);const bandM=new THREE.MeshStandardMaterial({map:stripe});add(new THREE.PlaneGeometry(13.2,.55),bandM,1.12,6.1,0,Q,false).rotation.y=Math.PI/2;
sign('PEDÁGIO',4.2,1.1,'#16181b','#f2b705',1.2,7.65,0,Q,Math.PI/2);
const booth=new THREE.Group();booth.position.set(0,0,-7.6);Q.add(booth);rbox(2.2,3,2.4,.25,0xf4f1ea,0,1.5,0,booth);rbox(2.4,.3,2.6,.12,0xe04b3a,0,3.15,0,booth);add(new THREE.PlaneGeometry(1.5,.9),M(0x2a4a63,{roughness:.2}),1.11,1.9,0,booth,false).rotation.y=Math.PI/2;
const TL=sph(.18,0xe04b3a,1.15,2.75,.7,booth,M(0xe04b3a,{emissive:0xe04b3a,emissiveIntensity:1}));
const arm=new THREE.Group();arm.position.set(1.0,1.3,-6.3);Q.add(arm);const armTex=tex(512,32,(g,W,H)=>{for(let i=0;i<8;i++){g.fillStyle=i%2?'#e04b3a':'#f4f1ea';g.fillRect(i*64,0,64,H)}});
add(new RoundedBoxGeometry(.24,.24,5.2,2,.08),new THREE.MeshStandardMaterial({map:armTex}),0,0,2.6,arm);
// ---------- borracharia ----------
const BR=new THREE.Group();BR.position.set(46,0,-10);S.add(BR);rbox(9,4.6,6,.25,0xeae4d4,0,2.3,0,BR);rbox(9.6,.5,6.6,.2,0x2b4553,0,4.85,0,BR);
sign('BORRACHARIA',7.2,1.3,'#16181b','#f2b705',0,3.75,3.02,BR);rbox(4,2.6,.1,.05,0x2a2d33,-1.6,1.3,3.0,BR);
const TIRES=[];const tireM=M(0x1d1f22,{roughness:.9});for(let i=0;i<7;i++){const tt=add(new THREE.TorusGeometry(.8,.36,14,28),tireM,6.3,.36+i*.74,1.8,BR);tt.rotation.x=Math.PI/2;TIRES.push(tt)}
const roll=add(new THREE.TorusGeometry(.8,.36,14,28),tireM,3.4,1.16,3.6,BR);roll.rotation.y=0;
// placa de pneu
const bigT=new THREE.Group();bigT.position.set(-5.4,0,2.6);BR.add(bigT);cyl(.15,.15,5,0x8a8f98,0,2.5,0,bigT,10);const bt2=add(new THREE.TorusGeometry(1.1,.45,14,28),tireM,0,5.6,0,bigT);
// ---------- oficina ----------
const OF=new THREE.Group();OF.position.set(60,0,-10.5);S.add(OF);rbox(13,6,7,.25,0xd9d4c4,0,3,0,OF);rbox(13.6,.6,7.6,.2,0xe04b3a,0,6.3,0,OF);sign('OFICINA',6.5,1.5,'#e04b3a','#ffffff',0,5.0,3.52,OF);
rbox(6,4,.12,.05,0x23262b,-2.5,2,3.5,OF);const doorTex=tex(256,256,(g,W,H)=>{g.fillStyle='#a9aeb6';g.fillRect(0,0,W,H);g.fillStyle='#8e939b';for(let y=0;y<H;y+=24)g.fillRect(0,y,W,6)});
const door=add(new THREE.PlaneGeometry(6,4),new THREE.MeshStandardMaterial({map:doorTex,metalness:.4,roughness:.5}),-2.5,2,3.58,OF,false);
for(const [x,z,c] of [[3.4,4.6,0xe04b3a],[4.5,4.4,0x2f6fb5],[3.9,5.6,0xf2b705]]){const d=cyl(.48,.48,1.4,c,x,.7,z,OF,20);cyl(.5,.5,.08,0x2a2d33,x,.4,z,OF,20);cyl(.5,.5,.08,0x2a2d33,x,1.0,z,OF,20)}
rbox(1.4,1,.7,.1,0xe04b3a,5.6,.5,4.4,OF);
const WR=new THREE.Group();WR.position.set(2.8,5.0,3.7);OF.add(WR);rbox(.35,1.6,.2,.08,0,0,0,0,WR,MET(0xc0c4ca));rbox(.9,.35,.2,.08,0,0,.75,0,WR,MET(0xc0c4ca));
// alerta
const AL=new THREE.Group();S.add(AL);const alT=tex(256,256,(g)=>{g.fillStyle='#e04b3a';g.beginPath();g.moveTo(128,14);g.lineTo(244,232);g.lineTo(12,232);g.closePath();g.fill();g.lineWidth=14;g.strokeStyle='#fff';g.stroke();g.fillStyle='#fff';g.font='800 160px BC';g.textAlign='center';g.fillText('!',128,212)});
const alS=new THREE.Sprite(new THREE.SpriteMaterial({map:alT}));alS.scale.set(3.2,3.2,1);AL.add(alS);
const SMK=[];for(let i=0;i<8;i++){const s=new THREE.Mesh(new THREE.IcosahedronGeometry(.6,1),new THREE.MeshStandardMaterial({color:0x6d6d6d,transparent:true,opacity:.6,flatShading:true}));S.add(s);SMK.push(s)}
// trajetória
const TK=[[0,0],[9.6,0],[11.2,15],[12.9,15],[13.5,23],[15.3,30.5],[17.8,44.5],[20.3,44.5],[20.6,57.5],[44.3,57.5],[47.6,96]];
function lerpK(K,t){for(let i=0;i<K.length-1;i++){const [a,va]=K[i],[b,vb]=K[i+1];if(t<=b)return va+(vb-va)*eio((t-a)/(b-a))}return K[K.length-1][1]}
const EV=[[ws(29),5520,new THREE.Vector3(18,2.4,-9)],[ws(34),1200,new THREE.Vector3(32,3,-7.6)],[ws(46),300,new THREE.Vector3(52.3,2.5,-8.2)],[ws(53),200,new THREE.Vector3(57.5,2.5,-7)],[ws(57),200,new THREE.Vector3(57.5,2.5,-7)]];
const FLY=EV.map(e=>{const n=Math.max(1,Math.round(e[1]/500));const g=new THREE.Group();for(let i=0;i<n;i++){bundle(g,-.85,i*.36,0);bundle(g,.85,i*.36,0)}g.visible=false;S.add(g);return g});
function money(t){let v=8000;EV.forEach(e=>{if(t>=e[0]+.15)v-=e[1]});return v}
// câmera
const V=(x,y,z)=>new THREE.Vector3(x,y,z);
const CK=[[0,V(2.4,3.9,15.5),V(-1.6,2.3,2.4)],[4.9,V(1.6,3.8,13.5),V(-1.7,2.4,2.4)],[5.6,V(1.4,3.9,13.2),V(-1.7,2.5,2.4)],[7.6,V(8,22,34),V(3,2.5,-2)],[9.4,V(5,17,28),V(0,3.5,-1)],
 [11.0,V(25,15,27),V(15.5,3,-4)],[12.9,V(26,15,26),V(16.5,3,-4)],[13.6,V(40,14,26),V(30,3,-2)],[15.2,V(41,15,26),V(31,3,-2)],[17.6,V(56,23,36),V(44,1,-3)],
 [18.4,V(54,14,26),V(45,3,-4)],[20.4,V(55,14,25),V(46,3,-4)],[21.0,V(67,14,27),V(57,3,-4)],[24.3,V(68,13.5,26),V(57,3,-4)],[25.2,V(62,9.5,12.5),V(55.5,4.8,0)],[27.6,V(61,9,12),V(55.5,4.8,0)],
 [30.4,V(65,11,18),V(57,3.5,0)],[32.4,V(67,13,24),V(58,2.5,0)],[44.0,V(69,14,28),V(58,2.5,0)],[47.6,V(94,12,30),V(98,2.5,0)]];
function camAt(t){for(let i=0;i<CK.length-1;i++){const [a,pa,ta]=CK[i],[b,pb,tb]=CK[i+1];if(t<=b){const k=eio((t-a)/(b-a));return [pa.clone().lerp(pb,k),ta.clone().lerp(tb,k)]}}const l=CK[CK.length-1];return [l[1].clone(),l[2].clone()]}
function zeAnim(z,t,talk){const d=z.userData;const b=(t%3.1)<.12?.1:1;d.eyes.forEach(e=>e.scale.y=b);d.mouth.scale.y=talk?.6+.5*Math.abs(Math.sin(t*14)):.6;
 d.hd.rotation.y=Math.sin(t*.9)*.12;z.position.y=Math.abs(Math.sin(t*2.2))*.03}
window.__scene={S,cam,R,sun,T,Z,Z2,MON,LAY,FLY,EV,TK,arm,TL,TIRES,roll,door,WR,AL,alS,SMK,CLOUDS,WHEELS,lerpK,camAt,money,zeAnim};
window.render3d=function(t){
 const x=lerpK(TK,t);T.position.x=x;const moving=Math.abs(lerpK(TK,t+.05)-x)>.005;
 WHEELS.forEach(w=>w.rotation.z=-x/.68);T.position.y=moving?Math.abs(Math.sin(t*16))*.035:0;
 const d=Z.userData;zeAnim(Z,t,false);d.hd.rotation.z=(t>ws(11)&&t<we(14)+.6)?.22*eo((t-ws(11))/.3):Math.sin(t*1.7)*.04;
 d.arms.forEach((a,i)=>{a.rotation.x=-1.05+Math.sin(t*2+i)*.04;a.rotation.z=(i?-1:1)*.25});Z.visible=t<9.6;
 zeAnim(Z2,t,false);Z2.userData.arms[1].rotation.x=-1.2;Z2.userData.arms[0].rotation.z=.15;Z2.visible=t>30;
 const v=money(t);const n=v/500;LAY.forEach((l,i)=>{l.visible=i<Math.ceil(n-1e-6);l.scale.y=(i==Math.ceil(n)-1&&n%1>0)?Math.max(.3,n%1):1});
 MON.scale.setScalar(t<ws(15)?0.001:0.4+0.6*back((t-ws(15))/.5));
 EV.forEach((e,k)=>{const g=FLY[k];const u=(t-e[0]-.15)/1.1;if(u<0||u>1){g.visible=false;return}g.visible=true;const st=new THREE.Vector3(T.position.x-2.1,4.68+n*.36,0);
  const p=st.clone().lerp(e[2],eo(u));p.y+=Math.sin(u*Math.PI)*6;g.position.copy(p);g.rotation.y=u*5;g.rotation.z=Math.sin(u*9)*.3;g.scale.setScalar(1-.6*u)});
 const up=cl((t-13.7)/.5)-cl((t-15.0)/.5);arm.rotation.x=-1.35*eo(up);TL.material.color.setHex(up>.5?0x5fd39a:0xe04b3a);TL.material.emissive.setHex(up>.5?0x5fd39a:0xe04b3a);
 roll.position.x=3.4+Math.sin(Math.max(0,t-18)*1.5)*1.2;roll.rotation.y=Math.max(0,t-18)*1.5;door.position.y=2+3.4*eo((t-20.4)/.9);
 WR.rotation.z=Math.sin(t*10)*(t>20.8&&t<24.3?.6:0);
 CLOUDS.forEach((c,i)=>c.position.x+=0);CLOUDS.forEach((c,i)=>c.position.x=-40+i*16+((t*.6)%16));
 const al=t>=ws(78)&&t<we(80)+1.2;AL.visible=al;AL.position.set(T.position.x-1,9.3+Math.sin(t*6)*.3,0);AL.scale.setScalar(al?back((t-ws(78))/.4):1);
 SMK.forEach((s,i)=>{const u=((t*0.8+i/8)%1);s.visible=al;s.position.set(T.position.x+3.15,5.6+u*4,1.15*(i%2?1:-1));s.scale.setScalar(.4+u*1.6);s.material.opacity=.55*(1-u)});
 let [cp,ct]=camAt(t);cp.x+=Math.sin(t*.7)*.25;cp.y+=Math.sin(t*.53)*.15;cam.position.copy(cp);cam.lookAt(ct);
 sun.position.set(ct.x+25,45,32);key.position.copy(cp);key.target.position.copy(ct);sun.target.position.set(ct.x,0,ct.z);
 R.render(S,cam);
};
window.__ready3d=true;
