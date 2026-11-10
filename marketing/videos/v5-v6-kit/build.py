import json,os,subprocess
W=json.load(open('n3_words.json'))
FIX={'1.100':'1.100','km,':'km,','diário':'Diário','bordo,':'Bordo,','bordo':'Bordo'}
def words(a,b,off):
    out=[]
    for w in W:
        if a<=w[1]<b:
            out.append({'id':'w%d'%len(out),'text':FIX.get(w[0],w[0]),'start':round(w[1]-off,3),'end':round(w[2]-off,3)})
    return out
HEAD=open('head.html').read()
def page(eid,dur,ws,body,js,skip):
    return HEAD.replace('__DUR__',str(dur)) + f'''
<div id="root" data-composition-id="main" data-start="0" data-duration="{dur}" data-width="1080" data-height="1920">
  <div id="bg">{ROAD}</div>
  <div id="stage">{body}</div>
  <div id="caps" class="hf-captions" data-track-kind="captions" data-layout-allow-caption-zone></div>
  <div id="flash"></div>
  <audio id="mix" data-start="0" data-duration="{dur}" data-track-index="2" src="mix.wav" data-volume="1"></audio>
</div>
<script>
window.__timelines=window.__timelines||{{}};
(function(){{
const K=window.HFKIT, f=(n)=>n/30, $=(s)=>document.querySelector(s);
const W={json.dumps(ws,ensure_ascii=False)};
const at=(i)=>W[i].start, root=$('#stage');
const tl=gsap.timeline({{paused:true}});
// a estrada: faixas descendo, farol respirando
tl.fromTo('.lane',{{y:-360}},{{y:0,duration:0.9,ease:'none',repeat:Math.max(0,Math.floor({dur}/0.9)-1)}},0);
tl.fromTo('#glowR',{{opacity:.55,scale:.95}},{{opacity:.9,scale:1.05,duration:2.4,ease:'sine.inOut',yoyo:true,repeat:Math.max(0,Math.floor({dur}/2.4)-1)}},0);
{js}
K.captions($('#caps'),W,{{'diesel':'object','pedágio':'object','comida':'object','caderninho':'object','caderninho,':'object','sobrou':'good','celular':'good','diária':'object','diárias':'object','dinheiro':'object','lucro':'good','hora':'good'}},tl,{{full:true,skip:{json.dumps(skip)}}});
tl.to('#fade',{{opacity:1,duration:.4,ease:'power1.in'}},{dur}-0.45);
window.__timelines['main']=tl;
}})();
</script></body></html>'''
ROAD='''<svg id="road" viewBox="0 0 1080 1920" width="1080" height="1920">
<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="var(--night-deep)"/><stop offset=".55" stop-color="var(--night)"/><stop offset="1" stop-color="var(--night-panel-dim)"/></linearGradient>
<radialGradient id="hl"><stop offset="0" stop-color="var(--flame)" stop-opacity=".35"/><stop offset="1" stop-color="var(--flame)" stop-opacity="0"/></radialGradient></defs>
<rect width="1080" height="1920" fill="url(#sky)"/>
<path d="M 470 760 L 610 760 L 1180 1920 L -100 1920 Z" fill="var(--night-panel)"/>
<path d="M 470 760 L 480 760 L -60 1920 L -100 1920 Z" fill="var(--night-line)"/>
<path d="M 600 760 L 610 760 L 1180 1920 L 1140 1920 Z" fill="var(--night-line)"/>
<rect x="0" y="752" width="1080" height="10" fill="var(--night-line)" opacity=".5"/>
<ellipse id="glowR" cx="540" cy="1500" rx="700" ry="520" fill="url(#hl)"/>
</svg>
<div class="lanes"><div class="lane"></div></div><div id="fade"></div>'''
CTA_BLOCK='''<div id="endc" class="endc"><img id="eico" src="icon-512.png"><div id="ename">DIÁRIO DE BORDO</div><div id="epill"><span class="hf-pill hf-pill--amber">TOQUE NO LINK</span></div><div id="esub">E COMECE HOJE</div></div>'''

# ---------- V5 ----------
w5=words(0,26.5,0.0)
D5=30.0
body5='''<div class="pos" style="top:0"><div id="top"></div></div>
<div class="pos ctr" style="top:560px"><div style="scale:1.9;transform-origin:50% 0;width:fit-content"><div id="km"></div></div></div>
<div class="pos ctr" style="top:260px"><div id="cnt"></div></div>
<div class="pos ctr" style="top:640px"><div style="scale:1.3;transform-origin:50% 0"><div id="list"></div></div></div>
<div class="pos ctr" style="top:1060px"><div style="scale:.85"><div id="stp"></div></div></div>
<div class="pos ctr" style="top:300px"><div id="note"></div></div>
<div id="ph" class="phone"><img src="07-sobrou.png"></div>
<div class="pos ctr" style="top:985px"><div style="scale:.72;transform-origin:50% 0"><div id="sob"></div></div></div>
<div class="pos ctr" style="top:1520px"><div style="scale:.68"><div id="mp"></div></div></div>
<div class="pos" style="top:0;bottom:0"><div id="ab"></div></div>'''
js5='''
const top=$('#top');K.topPill(top,{place:'BR-116',time:'05:40'});K.topPillIn(tl,top,{at:0.15,clock:{to:'05:41',at:2.2,duration:0.2},until:at(5)-0.3});
tl.to(top,{opacity:0,duration:.2},at(5)-0.3);
const km=$('#km');K.kmCounter(km,{value:0,label:'RODADOS'});K.kmIn(tl,km,{at:at(3)-0.1,from:0,to:1100,duration:1.3,root});
tl.to(km,{opacity:0,y:-60,duration:.25,ease:'power2.in'},at(6)-0.15);
const c=$('#cnt');K.bigCounter(c,{label:'O FRETE',value:0,format:'money',sub:'A VIAGEM'});
K.bigCounterIn(tl,c,{at:at(6)-0.1,from:0,root,steps:[{to:9000,at:at(8),duration:0.9},{to:4262,at:at(14),duration:0.5,ease:'power3.out'},{to:4038,at:at(16),duration:0.4},{to:4000,at:at(18),duration:0.35}]});
tl.set(c.querySelector('.label'),{textContent:'SOBRANDO'},at(11));
const L=$('#list');K.checklist(L,{items:[{text:'Diesel  − R$ 4.738',ok:false},{text:'Pedágio  − R$ 224',ok:false},{text:'Comida  − R$ 38',ok:false}]});
K.checklistIn(tl,L,{itemsAt:[at(14),at(16),at(18)],root});
const S=$('#stp');K.stampLabel(S,{text:'Diária não anotada',tone:'red'});K.stampIn(tl,S,{at:at(22)-0.05,root,until:at(24)-0.4});
tl.to([c,L,S],{opacity:0,y:-80,duration:.3,ease:'power2.in'},at(24)-0.35);
const N=$('#note');K.noteCard(N,{lines:['frete 9 mil','diesel ???','sobrou ???'],circle:{line:2,word:1},pill:'A conta não fecha'});
K.noteIn(tl,N,{at:at(24)-0.1,pace:0.16,circleAt:at(28)-0.2,pillAt:at(29)-0.1,root});
tl.to(N,{opacity:0,scale:.8,rotation:-6,duration:.3,ease:'power2.in'},at(30)-0.2);
const P=$('#ph');gsap.set(P,{opacity:0});tl.set(P,{opacity:1},at(30));tl.fromTo(P,{y:1400},{y:0,duration:.6,ease:'power3.out',immediateRender:false},at(30));
tl.fromTo(P,{rotation:-3},{rotation:0,duration:1.2,ease:'sine.inOut'},at(30)+0.4);
const sb=$('#sob');K.bigCounter(sb,{label:'SOBROU',value:0,format:'money',sub:'NA HORA'});
K.bigCounterIn(tl,sb,{at:at(45)-0.3,from:0,root,steps:[{to:3147,at:at(46),duration:0.9}]});
const mp=$('#mp');K.stampLabel(mp,{text:'Menos de R$ 1 por dia',tone:'amber'});K.stampIn(tl,mp,{at:at(47),root,flash:'white',until:at(53)-0.3});
tl.to([P,sb,mp],{opacity:0,duration:.25},at(53)-0.2);
const ab=$('#ab');K.abEnd(ab,{q1:'E você, anota no',q2:'caderninho ou no celular?',a:'Caderninho',b:'Celular',ring:false});
const ids=(a,b)=>W.slice(a,b+1).map(w=>w.start);
K.abEndIn(tl,ab,{at:at(53)-0.1,q1:ids(53,56),q2:ids(57,60),aAt:at(63),bAt:at(65),commentAt:at(61),until:%D,root});
'''.replace('%D',str(D5))
skip5=['w%d'%i for i in range(53,len(w5))]
# ---------- V6 ----------
o6=26.82
w6=words(26.6,60,o6)
D6=29.5
body6='''<div class="pos ctr" style="top:330px"><div id="hd"></div></div>
<div id="r1" class="pos rule" style="top:330px"></div><div id="r2" class="pos rule" style="top:330px"></div><div id="r3" class="pos rule" style="top:330px"></div>
<div id="nm" class="pos" style="top:250px;text-align:center"><span class="big">DIÁRIO DE BORDO</span><div class="small">RESOLVE OS TRÊS</div></div>
<div class="pos ctr" style="top:600px"><div style="scale:1.45;transform-origin:50% 0"><div id="list"></div></div></div>
<div class="pos ctr" style="top:1560px"><div style="scale:.72"><div id="stp"></div></div></div>
'''+CTA_BLOCK
js6='''
window.HFSTR.rule.pill='SINAL {n}';
const H=$('#hd');K.headline(H,{text:'3 sinais de que você está perdendo dinheiro na estrada',tag:'Atenção, motorista'});
K.headlineIn(tl,H,{at:0.05,words:W.slice(0,10).map(w=>w.start),root,until:at(10)-0.3});
tl.to(H,{opacity:0,scale:.9,duration:.2},at(10)-0.25);
const ICON={fuel:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" width="70" height="70"><path d="M4 21V5a2 2 0 0 1 2-2h7a2 2 0 0 1 2 2v16"/><path d="M3 21h13"/><path d="M15 9h2a2 2 0 0 1 2 2v6a1.5 1.5 0 0 0 3 0V8l-3-3"/><path d="M7 7h5v4H7z"/></svg>',
clock:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" width="70" height="70"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
cal:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" width="70" height="70"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>'};
const R=[['#r1',1,[['não sabe'],['quanto gastou'],[{w:'de diesel',red:true}]],ICON.fuel,10,[13,15,17],21],['#r2',2,[['esqueceu'],['de cobrar'],[{w:'a diária',red:true}]],ICON.clock,21,[26,27,29],31],['#r3',3,[['só descobre'],['o lucro'],[{w:'no fim do mês',red:true}]],ICON.cal,31,[33,37,38],42]];
R.forEach(([sel,n,lines,icon,a,ws,b])=>{const el=$(sel);el.innerHTML=K.ruleCard({n,lines,icon});const card=el.firstElementChild;
  K.ruleIn(tl,card,{at:at(a)-0.12,numberAt:at(a+1),words:ws.map(at),root,exitAt:at(b)-0.2});});
const nm=$('#nm');tl.fromTo(nm,{opacity:0,scale:1.6},{opacity:1,scale:1,duration:.35,ease:'back.out(2)'},at(42));
const L=$('#list');K.checklist(L,{items:[{text:'Diesel',ok:true},{text:'Gastos',ok:true},{text:'Diárias',ok:true}]});
K.checklistIn(tl,L,{itemsAt:[at(49),at(50),at(52)],root});
const S=$('#stp');K.stampLabel(S,{text:'Conta pronta na hora',tone:'green'});K.stampIn(tl,S,{at:at(58)-0.05,root,flash:'white',until:at(62)-0.3});
tl.to([nm,L,S],{opacity:0,y:-80,duration:.3,ease:'power2.in'},at(62)-0.3);
const E=$('#endc');tl.set(E,{opacity:1},at(62)-0.05);
tl.from('#eico',{scale:0,rotation:-14,duration:.5,ease:'back.out(1.8)'},at(62)-0.05);
tl.from('#ename',{y:70,opacity:0,duration:.4,ease:'expo.out'},at(62)+0.15);
tl.from('#epill',{scale:.5,opacity:0,duration:.4,ease:'back.out(2.4)'},at(62)+0.3);
tl.from('#esub',{y:40,opacity:0,duration:.35,ease:'power3.out'},at(65));
tl.to('#epill',{scale:1.07,duration:.5,ease:'sine.inOut',yoyo:true,repeat:3},at(66)+0.4);
'''
skip6=['w%d'%i for i in range(62,len(w6))]
for eid,dur,ws,body,js,skip in [('v5-imagine',D5,w5,body5,js5,skip5),('v6-sinais',D6,w6,body6,js6,skip6)]:
    os.makedirs(eid,exist_ok=True)
    for l,t in [('kit','/home/claude/kit-serie/kit'),('assets','/home/claude/kit-serie/assets')]:
        if not os.path.islink(f'{eid}/{l}'): os.symlink(t,f'{eid}/{l}')
    for f in ['07-sobrou.png','icon-512.png']: subprocess.run(['cp','/home/claude/proj-bordo/'+f,eid])
    subprocess.run(['cp','/home/claude/kit-serie/scripts/vendor/gsap-3.14.2.min.js',eid+'/gsap.min.js'])
    open(f'{eid}/index.html','w').write(page(eid,dur,ws,body,js,skip))
    json.dump(ws,open(f'{eid}/words.json','w'),ensure_ascii=False)
    print(eid,len(ws),ws[-1])
