# efeitos sonoros gerados (numpy). python3 audio.py g1|g2|g3 -> /tmp/sfx_<v>.wav
import numpy as np, wave, sys
SR=44100; rng=np.random.default_rng(5)
def tone(f,dur,d=0.1,a=0.004):
    n=int(dur*SR); t=np.arange(n)/SR; return np.sin(2*np.pi*f*t)*np.minimum(1,t/a)*np.exp(-t/d)
def whoosh():
    n=int(0.32*SR); w=np.convolve(rng.standard_normal(n),np.ones(6)/6,'same'); return w*np.sin(np.pi*np.arange(n)/n)**2
def boom():
    kt=np.arange(int(0.8*SR))/SR; return np.sin(2*np.pi*(38+80*np.exp(-kt/0.05))*kt)*np.exp(-kt/0.35)
def kick():
    kt=np.arange(int(0.3*SR))/SR; return np.sin(2*np.pi*(45+110*np.exp(-kt/0.03))*kt)*np.exp(-kt/0.13)
def cash():
    return np.concatenate([tone(2637,0.08,0.03),tone(3520,0.4,0.12)])
def buzz():
    n=int(0.45*SR); t=np.arange(n)/SR; return np.sign(np.sin(2*np.pi*110*t))*0.5*np.exp(-t/0.25)
H={
 'g1':dict(TOT=27.3,beat=(4.5,24.3),boom=[0.0,2.74,12.55],whoosh=[4.4,11.1,14.55,17.7,21.0,24.3],tick=[0.2*i for i in range(12)],cash=[4.6],buzz=[7.3,8.05,8.8,9.55,10.3],ch=[24.55]),
 'g2':dict(TOT=21.6,beat=(2.7,18.7),boom=[0.0,11.6],whoosh=[2.6,7.8,13.6,18.7],tick=[4.7,6.38,10.83,16.1],cash=[2.75],buzz=[6.45,11.65],ch=[18.95]),
 'g3':dict(TOT=23.1,beat=(3.4,20.3),boom=[0.0,1.6,16.35],whoosh=[3.4,11.6,15.0,17.5,20.3],tick=[8.0,8.8,9.6,10.4],cash=[3.6,13.3],buzz=[6.6,8.0],ch=[20.45]),
}[sys.argv[1]]
TOT=H['TOT']; N=int(SR*TOT); out=np.zeros(N); tt=np.arange(N)/SR
def add(sig,t0,g=1.0):
    i=int(t0*SR); j=min(N,i+len(sig))
    if i<N: out[i:j]+=g*sig[:j-i]
bed=np.zeros(N); bar=2.0; ch=[[110,130.8,164.8],[87.3,110,130.8],[98,123.5,146.8],[82.4,103.8,123.5]]
for k in range(int(TOT/bar)+1):
    for f in ch[k%4]:
        n=int(bar*SR); t=np.arange(n)/SR; env=np.minimum(1,t/0.3)*np.minimum(1,(bar-t)/0.4)
        i=int(k*bar*SR); j=min(N,i+n)
        if i<N: bed[i:j]+=((0.5*np.sin(2*np.pi*f*t)+0.25*np.sin(4*np.pi*f*t))*env)[:j-i]
bed/=np.max(np.abs(bed))
beat=np.zeros(N); kk=kick(); a,b=H['beat']
for x in np.arange(a,b,0.5):
    i=int(x*SR); j=min(N,i+len(kk)); beat[i:j]+=kk[:j-i]*(0.8 if round(x*2)%2==0 else 0.4)
out+=(0.45*bed+0.4*beat)*np.minimum(1,tt/0.4)*np.minimum(1,(TOT-tt)/1.0)*0.5
for x in H['boom']: add(boom(),x,1.0)
for x in H['whoosh']: add(whoosh(),x,0.5)
for x in H['tick']: add(tone(1600,0.06,0.015),x,0.4)
for x in H['cash']: add(cash(),x,0.35)
for x in H['buzz']: add(buzz(),x,0.25)
for x in H['ch']:
    for f,dt in [(1319,0),(1568,0.09),(1976,0.18)]: add(tone(f,0.8,0.3),x+dt,0.35)
out/=np.max(np.abs(out))*1.1
st=np.stack([out,out],1)
with wave.open(f'/tmp/sfx_{sys.argv[1]}.wav','wb') as wf:
    wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes((st*32767).astype('<i2').tobytes())
