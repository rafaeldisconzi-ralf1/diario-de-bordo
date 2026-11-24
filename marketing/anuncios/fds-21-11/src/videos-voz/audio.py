import numpy as np, wave, sys
V=sys.argv[1]; TOT={'A':22.3,'B':18.8,'C':16.2,'D':21.6}[V]
CUTS={'A':[0.0,3.55,9.6,12.3,16.5,20.35],'B':[0.0,1.75,7.0,10.3,13.1,16.65],'C':[0.0,1.75,7.0,10.3,13.1],'D':[0.0,3.55,9.6,12.3,16.5,18.6]}[V]
POPS={'A':[5.2,6.4,7.2,7.8,10.9,12.6,14.6,16.6],'B':[2.4,3.3,4.3,8.0,10.4,11.3,13.2],'C':[2.4,3.3,4.3,8.0,10.4,11.3,13.4],'D':[5.2,6.4,7.2,7.8,10.9,12.6,14.6,16.6,18.9]}[V]
SR=44100;N=int(SR*TOT);out=np.zeros(N);rng=np.random.default_rng(3);tt=np.arange(N)/SR
def add(sig,t0,g=1.0):
    i=int(t0*SR);j=min(N,i+len(sig))
    if i<N: out[i:j]+=g*sig[:j-i]
def tone(f,dur,d=0.1,a=0.004):
    n=int(dur*SR);t=np.arange(n)/SR;return np.sin(2*np.pi*f*t)*np.minimum(1,t/a)*np.exp(-t/d)
# fundo: acordes suaves + batida leve
chords=[[220,277.2,329.6],[196,246.9,293.7],[174.6,220,261.6],[196,246.9,293.7]]
bed=np.zeros(N);bar=2.0
for k in range(int(TOT/bar)+1):
    for f in chords[k%4]:
        n=int(bar*SR);t=np.arange(n)/SR;env=np.minimum(1,t/0.3)*np.minimum(1,(bar-t)/0.4)
        seg=0.5*np.sin(2*np.pi*f*t)+0.2*np.sin(2*np.pi*2*f*t)
        i=int(k*bar*SR);j=min(N,i+n)
        if i<N: bed[i:j]+=(seg*env)[:j-i]
bed/=np.max(np.abs(bed))
kt=np.arange(int(0.25*SR))/SR;kick=np.sin(2*np.pi*(50+90*np.exp(-kt/0.03))*kt)*np.exp(-kt/0.12)
beat=np.zeros(N)
for b in np.arange(0,TOT,0.5):
    i=int(b*SR);j=min(N,i+len(kick));beat[i:j]+=kick[:j-i]*(1 if (b*2)%2==0 else 0.5)
mus=0.6*bed+0.5*beat
fade=np.minimum(1,tt/0.8)*np.minimum(1,(TOT-tt)/1.0)
out+=mus*fade*0.45
n=int(0.3*SR);w=np.convolve(rng.standard_normal(n),np.ones(6)/6,'same')*np.sin(np.pi*np.arange(n)/n)**2
for c in CUTS[1:]: add(w,c-0.12,0.5)
for p in POPS: add(tone(1700,0.06,0.015),p,0.45)
out/=np.max(np.abs(out))*1.1
st=np.stack([out,out],1)
with wave.open(f'fundo_{V}.wav','wb') as wf:
    wf.setnchannels(2);wf.setsampwidth(2);wf.setframerate(SR);wf.writeframes((st*32767).astype('<i2').tobytes())
