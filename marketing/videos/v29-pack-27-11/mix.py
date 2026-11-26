import numpy as np, wave, re, sys, subprocess, json
sys.path.insert(0,'.')
import importlib.util
spec=importlib.util.spec_from_file_location('g','gerar.py'); 
src=open('gerar.py',encoding='utf-8').read().split('def build')[0]
ns={'__file__':'gerar.py'}; exec(src,ns); V=ns['V']
SR=44100; rng=np.random.default_rng(7)
def tone(f,dur,d=0.1,a=0.004):
    n=int(dur*SR); tt=np.arange(n)/SR; return np.sin(2*np.pi*f*tt)*np.minimum(1,tt/a)*np.exp(-tt/d)
def whoosh():
    n=int(0.3*SR); w=np.convolve(rng.standard_normal(n),np.ones(5)/5,'same'); return w*np.sin(np.pi*np.arange(n)/n)**2
def kick():
    kt=np.arange(int(0.3*SR))/SR; return np.sin(2*np.pi*(45+110*np.exp(-kt/0.03))*kt)*np.exp(-kt/0.13)
for k in sys.argv[1:]:
    s=V[k]; TOT=s['TOT']; N=int(SR*TOT); out=np.zeros(N)
    def add(sig,t0,g=1.0):
        i=int(t0*SR); j=min(N,i+len(sig))
        if i<N: out[i:j]+=g*sig[:j-i]
    ts=sorted(set(float(x) for x in re.findall(r"pop\('#[\w]+',([\d.]+)",s['anim'])))
    prev=-9
    for x in ts:
        if x-prev>0.8: add(whoosh(),max(0,x-0.05),0.45)
        else: add(tone(1800,0.06,0.015),x,0.35)
        prev=x
    add(kick(),0.08,0.9); add(whoosh(),s['end']['a']-0.05,0.5)
    out/=np.max(np.abs(out))*1.1
    st=np.stack([out,out],1)
    with wave.open(f'/tmp/sfx_{k}.wav','wb') as wf:
        wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes((st*32767).astype('<i2').tobytes())
    subprocess.run(['ffmpeg','-v','error','-y','-i',f'/tmp/video{k}.mp4','-i',f'{k}.mp3','-i',f'/tmp/sfx_{k}.wav','-filter_complex',
      '[1:a]apad[v];[2:a]volume=0.22[s];[v][s]amix=inputs=2:duration=longest:normalize=0,loudnorm=I=-16:TP=-1.5[a]',
      '-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','160k','-shortest',f'out/{k}.mp4'],check=True)
    print(k,'ok')
