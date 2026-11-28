import numpy as np, wave, subprocess, os, sys, json
from PIL import Image, ImageDraw, ImageFont
W,H=1080,1920
HERE=os.path.dirname(os.path.abspath(__file__))
F=HERE+'/barlow-condensed-latin-800-normal.ttf'
YEL=(242,183,5); WH=(244,243,238); GR=(95,211,154)
COL={'Y':YEL,'G':GR}
def caption(text,hl,path,size=100,y0=1600):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); f=ImageFont.truetype(F,size)
    lines=[];cur=[]
    for w in text.split():
        if d.textlength(' '.join(cur+[w]),font=f)>980 and cur: lines.append(cur);cur=[w]
        else: cur.append(w)
    lines.append(cur); y=y0
    for ln in lines:
        x=(W-d.textlength(' '.join(ln),font=f))/2
        for w in ln:
            col=COL.get(hl.get(w),WH)
            for dx in range(-6,7,2):
                for dy in range(-6,7,2): d.text((x+dx,y+dy),w,font=f,fill=(0,0,0,255))
            d.text((x,y),w,font=f,fill=col+(255,)); x+=d.textlength(w+' ',font=f)
        y+=size
    im.save(path)
def label(text,path,y,size=64,color=YEL):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); f=ImageFont.truetype(F,size)
    tw=d.textlength(text,font=f); x=(W-tw)/2
    d.rounded_rectangle((x-28,y-10,x+tw+28,y+size+16),radius=16,fill=(22,24,27,235))
    d.text((x,y),text,font=f,fill=color+(255,)); im.save(path)
def outro(lines,path,icon):
    im=Image.new('RGBA',(W,H),(22,24,27,255)); d=ImageDraw.Draw(im)
    ic=Image.open(icon).convert('RGBA').resize((300,300)); im.paste(ic,(390,430),ic)
    y=800
    for t,s,c in lines:
        f=ImageFont.truetype(F,s); d.text(((W-d.textlength(t,font=f))/2,y),t,font=f,fill=c); y+=s+34
    im.save(path)
def sfx(events,path,T=10.5):
    sr=44100;n=int(sr*T);out=np.zeros(n);rng=np.random.default_rng(7)
    def add(s,x):
        i=int(s*sr);j=min(n,i+len(x));
        if i<n: out[i:j]+=x[:j-i]
    def whoosh(s,d=.28):
        t=np.arange(int(d*sr))/sr;x=rng.standard_normal(len(t));y=np.cumsum(x);y=y-np.convolve(y,np.ones(60)/60,'same')
        add(s,0.35*y/np.abs(y).max()*np.sin(np.pi*t/d)**2)
    def pop(s):
        t=np.arange(int(.12*sr))/sr;add(s,0.5*np.sin(2*np.pi*(700-400*t/.12)*t)*np.exp(-t*35))
    def click(s):
        t=np.arange(int(.05*sr))/sr;add(s,0.4*rng.standard_normal(len(t))*np.exp(-t*120)+0.3*np.sin(2*np.pi*1800*t)*np.exp(-t*90))
    def ding(s):
        t=np.arange(int(.9*sr))/sr;add(s,0.45*(np.sin(2*np.pi*1318*t)+0.5*np.sin(2*np.pi*1975*t)+0.25*np.sin(2*np.pi*2637*t))*np.exp(-t*5)/1.75)
    def coin(s):
        t=np.arange(int(.5*sr))/sr;add(s,0.4*np.sin(2*np.pi*np.where(t<.08,988,1319)*t)*np.exp(-t*7))
    def thud(s):
        t=np.arange(int(.35*sr))/sr;add(s,0.8*np.sin(2*np.pi*(60+80*np.exp(-t*25))*t)*np.exp(-t*9))
    fn=dict(whoosh=whoosh,pop=pop,click=click,ding=ding,coin=coin,thud=thud)
    for k,t in events: fn[k](t)
    out=out/np.abs(out).max()*0.8
    w=wave.open(path,'wb');w.setnchannels(1);w.setsampwidth(2);w.setframerate(44100)
    w.writeframes((out*32767).astype(np.int16).tobytes());w.close()
def build(cfg):
    d=cfg['dir'];os.makedirs(d,exist_ok=True)
    ins=['-i',cfg['video']];fc=[];idx=1;layers=[]
    for i,(t,hl,a,b) in enumerate(cfg['caps']):
        p=f'{d}/cap{i}.png';caption(t,hl,p);layers.append((p,0,0,a,b))
    for o in cfg.get('overlays',[]): layers.append((o['png'],o.get('x',0),o.get('y',0),o['a'],o['b']))
    for o in cfg.get('labels',[]):
        p=f"{d}/lab{abs(hash(o['text']))%9999}.png";label(o['text'],p,o['y']);layers.append((p,0,0,o['a'],o['b']))
    for p,*_ in layers: ins+=['-i',p]
    ins+=['-loop','1','-t','10','-i',f'{d}/outro.png']
    outro(cfg['outro'],f'{d}/outro.png',cfg['icon'])
    ins=['-i',cfg['video']]+sum([['-i',p] for p,*_ in layers],[])+['-loop','1','-t','10','-i',f'{d}/outro.png']
    chain=['[0:v]scale=1080:-2:flags=lanczos,crop=1080:1920,setsar=1[b]'];prev='b'
    for i,(p,x,y,a,b) in enumerate(layers):
        chain.append(f"[{prev}][{i+1}]overlay={x}:{y}:enable='between(t,{a},{b})'[v{i}]");prev=f'v{i}'
    o=len(layers)+1;T=cfg['outro_at']
    chain.append(f"[{o}:v]format=rgba,fade=t=in:st={T}:d=0.25:alpha=1[o]")
    chain.append(f"[{prev}][o]overlay=eof_action=pass,format=yuv420p[v]")
    sfx(cfg['sfx'],f'{d}/sfx.wav')
    vid=f'{d}/video.mp4'
    subprocess.run(['ffmpeg','-v','error','-y']+ins+['-filter_complex',';'.join(chain),'-map','[v]','-an','-c:v','libx264','-crf','20','-preset','veryfast','-r','30','-t','10',vid],check=True)
    mus=cfg.get('music',HERE+'/music.wav')
    af="[1:a]volume=0.5,lowpass=f=5000[m];[m][0:a]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=300[md];[2:a]volume=0.45[sx];[0:a][md][sx]amix=inputs=3:normalize=0:duration=first,loudnorm=I=-16:TP=-1.5[a]"
    subprocess.run(['ffmpeg','-v','error','-y','-i',cfg['video'],'-i',mus,'-i',f'{d}/sfx.wav','-i',vid,'-filter_complex',af,'-map','3:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','160k','-t','10',cfg['out']],check=True)
