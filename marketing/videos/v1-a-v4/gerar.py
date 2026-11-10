import json,re,subprocess,sys,os
base=open('base.html').read()
G0=json.load(open('groups.json'))
V={
 'v2-caderninho':dict(seg=(0.0,2.66),size=128,lines=[("Ainda anota",0.05,0),("frete e diesel",0.96,0),("no caderninho?",1.71,1)],
   cta=(10.38,14.12),marca=0.05,plate=("Toque no link",1.69),sub=None,pill=("Comece hoje mesmo",2.73)),
 'v3-garantia':dict(seg=(2.98,6.06),size=165,lines=[("Fechou o mês",0.05,0),("e não sabe",0.78,0),("se ganhou",1.29,0),("ou perdeu",1.86,0),("dinheiro?",2.5,1)],
   cta=(14.45,19.70),marca=0.0,plate=("7 dias de garantia",1.41),sub=("Não gostou? Devolvemos seu dinheiro.",1.9),pill=("Toque no link",4.48)),
 'v4-diaria':dict(seg=(6.38,10.02),size=145,lines=[("Ficou parado",0.05,0),("esperando",0.68,0),("descarga e",1.27,0),("perdeu a conta",1.94,0),("das diárias?",3.09,1)],
   cta=(20.0,26.28),marca=0.03,plate=("Menos de R$ 1 por dia",1.33),sub=("Nunca mais perca dinheiro.",3.26),pill=("Toque no link",5.33)),
}
def r2(x):return round(x,2)
for nome,c in V.items():
  Hd=c['seg'][1]-c['seg'][0]; T0=Hd+0.35; O=T0-3.55
  midEnd=24.15+O; Cs=midEnd+0.15; Cd=c['cta'][1]-c['cta'][0]; TOT=r2(Cs+Cd+2.6)
  h=base
  # S1 html
  s1=''.join('<div class="h cond%s" id="s1l%d">%s</div>'%(' y' if y else '',i,t) for i,(t,_,y) in enumerate(c['lines']))
  h=re.sub(r'<div id="s1" class="scene"><div class="scene-content">.*?</div></div>\n','<div id="s1" class="scene"><div class="scene-content">'+s1+'</div></div>\n',h,flags=re.S)
  h=h.replace('#s1 .h{font-size:200px','#s1 .h{font-size:%dpx'%c['size'])
  # S8 html
  sub='<div id="sub8">%s</div>'%c['sub'][0] if c['sub'] else ''
  s8='<img id="ico" src="icon-512.png" alt="">\n    <div id="marca" class="cond">Diário de Bordo</div>\n    <div id="preco" class="cond">%s</div>%s\n    <div id="cta">%s</div>'%(c['plate'][0],sub,c['pill'][0])
  h=re.sub(r'<img id="ico".*?<div id="cta">.*?</div>',s8,h,flags=re.S)
  h=h.replace('#fade{','#sub8{font-size:58px;font-weight:700;color:#f4f3ee;max-width:900px;line-height:1.15}\n#fade{')
  # JS split
  a=h.index('// S1 gancho');b=h.index('// transição S1 -> celular');m=h.index('// S7b -> S8');e=h.index('window.__timelines["main"]=tl;')
  eases=['power3.out','back.out(1.6)','expo.out','power4.out','back.out(1.8)']
  s1js='// S1 gancho\n'+''.join('tl.from("#s1l%d",{y:90,opacity:0,duration:.45,ease:"%s"},%s);\n'%(i,eases[i%5],r2(t+0.0)) for i,(_,t,_) in enumerate(c['lines']))
  mid=h[b:m]
  sh=lambda x:str(r2(float(x)+O))
  mid=re.sub(r'\},(\d+(?:\.\d+)?)\)',lambda g:'},'+sh(g.group(1))+')',mid)
  mid=re.sub(r'toque\((\d+),(\d+),([\d.]+)\)',lambda g:'toque(%s,%s,%s)'%(g.group(1),g.group(2),sh(g.group(3))),mid)
  mid=re.sub(r'troca\(("[^"]+"),("[^"]+"),([\d.]+)\)',lambda g:'troca(%s,%s,%s)'%(g.group(1),g.group(2),sh(g.group(3))),mid)
  mid=re.sub(r'\["(#l\d)",([\d.]+),([\d.]+)\]',lambda g:'["%s",%s,%s]'%(g.group(1),sh(g.group(2)),sh(g.group(3))),mid)
  t=lambda x:r2(Cs+x)
  end='// S7b -> S8\n'
  end+='tl.to("#s7b",{y:-1920,duration:.45,ease:"power3.in"},%s);\n'%r2(24.0+O)
  end+='tl.set("#s8",{opacity:1},%s);\n'%r2(24.1+O)
  end+='tl.from("#ico",{scale:0,rotation:-12,duration:.55,ease:"back.out(1.8)"},%s);\n'%r2(24.2+O)
  end+='tl.from("#marca",{y:80,opacity:0,duration:.45,ease:"expo.out"},%s);\n'%max(r2(24.45+O),t(c['marca']))
  end+='tl.from("#preco",{scale:.6,opacity:0,duration:.45,ease:"back.out(2.2)"},%s);\n'%t(c['plate'][1])
  if c['sub']: end+='tl.from("#sub8",{y:40,opacity:0,duration:.4,ease:"power2.out"},%s);\n'%t(c['sub'][1])
  end+='tl.from("#cta",{y:60,opacity:0,duration:.45,ease:"power3.out"},%s);\n'%t(c['pill'][1])
  end+='tl.to("#cta",{scale:1.06,duration:.5,ease:"sine.inOut",yoyo:true,repeat:3},%s);\n'%t(c['pill'][1]+0.6)
  end+='tl.to("#fade",{opacity:1,duration:.4,ease:"power1.in"},%s);\n'%r2(TOT-0.4)
  h=h[:a]+s1js+'\n'+mid+end+h[e:]
  # legendas
  G=[{'s':r2(g['s']+O),'e':r2(g['e']+O),'w':[[w[0],r2(w[1]+O)] for w in g['w']]} for g in G0]
  h=re.sub(r'var G=\[.*?\];','var G='+json.dumps(G,ensure_ascii=False)+';',h,count=1,flags=re.S)
  h=h.replace('data-duration="30.5"','data-duration="%s"'%TOT).replace('30.5/1.1','%s/1.1'%TOT)
  aud='narr-%s.wav'%nome
  h=re.sub(r'<audio id="vo"[^>]*></audio>','<audio id="vo" data-start="0" data-duration="%s" data-track-index="2" src="%s" data-volume="1"></audio>'%(r2(Cs+Cd),aud),h)
  d='out/'+nome;os.makedirs(d,exist_ok=True)
  for f in os.listdir('.'):
    if f.endswith('.png') or f in('gsap.min.js','hyperframes.json','meta.json','package.json'):
      subprocess.run(['cp',f,d])
  subprocess.run(['cp','-r','fonts',d])
  open(d+'/index.html','w').write(h)
  # áudio
  hs,he=c['seg'];cs,ce=c['cta']
  fc=('[0:a]atrim=%s:%s,asetpts=PTS-STARTPTS,afade=t=out:st=%s:d=0.08,apad=whole_dur=%s[h];'%(hs,he,r2(Hd-0.08),r2(T0))+
      '[1:a]atrim=3.55:24.15,asetpts=PTS-STARTPTS,apad=whole_dur=%s[m];'%r2(Cs-T0)+
      '[0:a]atrim=%s:%s,asetpts=PTS-STARTPTS,afade=t=out:st=%s:d=0.08[c];'%(cs,ce,r2(Cd-0.08))+
      '[h][m][c]concat=n=3:v=0:a=1[o]')
  subprocess.run(['ffmpeg','-v','error','-y','-i','partes.wav','-i','narracao.mp3','-filter_complex',fc,'-map','[o]','-ar','44100','-ac','2',d+'/'+aud],check=True)
  print(nome,'Hd',r2(Hd),'O',r2(O),'Cs',r2(Cs),'TOT',TOT)
