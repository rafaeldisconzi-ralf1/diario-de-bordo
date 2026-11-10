import numpy as np, wave
SR=44100; TOT=29.5; END=24.9
N=int(SR*TOT); out=np.zeros(N)
rng=np.random.default_rng(7)
def add(sig,t,g=1.0):
    i=int(t*SR); j=min(N,i+len(sig)); out[i:j]+=g*sig[:j-i]
def env(n,a=0.005,d=0.2):
    t=np.arange(n)/SR; return np.minimum(1,t/a)*np.exp(-t/d)
def tone(f,dur,d=0.1,a=0.004):
    n=int(dur*SR); t=np.arange(n)/SR; return np.sin(2*np.pi*f*t)*env(n,a,d)
# --- música: 96 bpm, Am F C G
bpm=96; beat=60/bpm
chords=[[220,261.6,329.6],[174.6,220,261.6],[196,261.6,329.6],[196,246.9,293.7]]
bass=[110,87.3,130.8,98]
t=np.arange(N)/SR
music=np.zeros(N)
bar=beat*4
for k in range(int(TOT/bar)+1):
    c=chords[k%4]; s=int(k*bar*SR); n=int(bar*SR); n=min(n,N-s)
    if n<=0: break
    tt=np.arange(n)/SR
    pad=sum(np.sin(2*np.pi*f*tt)+0.3*np.sin(2*np.pi*2*f*tt+0.5) for f in c)/3
    pad*=np.minimum(1,tt/0.25)*np.minimum(1,(bar-tt)/0.2)
    music[s:s+n]+=0.10*pad
    for b in range(4):
        bs=s+int(b*beat*SR)
        bt=np.arange(int(0.35*SR))/SR
        bl=np.sin(2*np.pi*bass[k%4]*bt)*np.exp(-bt/0.25)
        e=min(N,bs+len(bl)); music[bs:e]+=0.18*bl[:e-bs]
for b in range(int(TOT/beat)+1):
    tb=b*beat
    kt=np.arange(int(0.25*SR))/SR
    kick=np.sin(2*np.pi*(50+90*np.exp(-kt/0.03))*kt)*np.exp(-kt/0.12)
    i=int(tb*SR); e=min(N,i+len(kick)); music[i:e]+=0.45*kick[:e-i]
    h=rng.standard_normal(int(0.05*SR))*np.exp(-np.arange(int(0.05*SR))/SR/0.012)
    h=np.diff(h,prepend=0)
    i=int((tb+beat/2)*SR); e=min(N,i+len(h))
    if i<N: music[i:e]+=0.06*h[:e-i]
fade=np.ones(N); fade[int((TOT-1.2)*SR):]=np.linspace(1,0,N-int((TOT-1.2)*SR))
music*=fade
# baixa a música durante a "leitura" e sobe no final
duck=np.where(t<END,0.55,0.85); out+=music*duck
# --- efeitos
M=[('z',0.25),('c',2.9,1.5),('z',4.7),('z',6.0),('c',9.4,7.9),('c',11.9,10.6),('z',15.3),('c',17.6,16.4),('z',19.1),('c',21.3,20.1),('z',23.0)]
for m in M:
    if m[0]=='z':
        add(tone(1320,0.12,0.04),m[1],0.35); add(tone(1760,0.15,0.05),m[1]+0.05,0.3)
    else:
        add(tone(880,0.15,0.06),m[1],0.4); add(tone(1175,0.2,0.07),m[1]+0.07,0.35)
    if len(m)>2:
        x=m[2]+0.15
        while x<m[1]-0.15:
            n=int(0.02*SR); c=rng.standard_normal(n)*np.exp(-np.arange(n)/SR/0.003)
            add(np.diff(c,prepend=0),x,0.12); x+=rng.uniform(0.07,0.16)
# whoosh + impacto na tela final
n=int(0.6*SR); w=rng.standard_normal(n); 
from numpy.fft import rfft,irfft
w=w*np.sin(np.pi*np.arange(n)/n)**2; add(w*0.15,END-0.3)
kt=np.arange(int(0.6*SR))/SR
add(np.sin(2*np.pi*(40+70*np.exp(-kt/0.05))*kt)*np.exp(-kt/0.3),END+0.1,0.8)
for tt,f in [(END+1.6,660),(END+2.4,990)]: add(tone(f,0.3,0.1),tt,0.3)
out/=np.max(np.abs(out))*1.1
st=np.stack([out,out],1)
with wave.open('audio.wav','wb') as wf:
    wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes((st*32767).astype('<i2').tobytes())
print('ok')
