import numpy as np, wave
SR=44100; TOT=29.0; N=int(SR*TOT); out=np.zeros(N); rng=np.random.default_rng(5); tt=np.arange(N)/SR
def add(sig,t0,g=1.0):
    i=int(t0*SR); j=min(N,i+len(sig))
    if i<N: out[i:j]+=g*sig[:j-i]
def tone(f,dur,d=0.1,a=0.004):
    n=int(dur*SR); t=np.arange(n)/SR; return np.sin(2*np.pi*f*t)*np.minimum(1,t/a)*np.exp(-t/d)
def whoosh():
    n=int(0.32*SR); w=np.convolve(rng.standard_normal(n),np.ones(6)/6,'same'); return w*np.sin(np.pi*np.arange(n)/n)**2
def boom():
    kt=np.arange(int(0.8*SR))/SR; return np.sin(2*np.pi*(38+80*np.exp(-kt/0.05))*kt)*np.exp(-kt/0.35)
def kick():
    kt=np.arange(int(0.3*SR))/SR; return np.sin(2*np.pi*(45+110*np.exp(-kt/0.03))*kt)*np.exp(-kt/0.13)
bed=np.zeros(N); bar=2.0; ch=[[220,261.6,329.6],[174.6,220,261.6],[196,246.9,293.7],[164.8,207.7,246.9]]
for k in range(int(TOT/bar)+1):
    for f in ch[k%4]:
        n=int(bar*SR); t=np.arange(n)/SR; env=np.minimum(1,t/0.3)*np.minimum(1,(bar-t)/0.4)
        i=int(k*bar*SR); j=min(N,i+n)
        if i<N: bed[i:j]+=((0.5*np.sin(2*np.pi*f*t)+0.2*np.sin(4*np.pi*f*t))*env)[:j-i]
bed/=np.max(np.abs(bed))
beat=np.zeros(N); kk=kick()
for b in np.arange(5.5,24.6,0.5):
    i=int(b*SR); j=min(N,i+len(kk)); beat[i:j]+=kk[:j-i]*(0.8 if (b*2)%2==0 else 0.4)
out+=(0.5*bed+0.35*beat)*np.minimum(1,tt/0.6)*np.minimum(1,(TOT-tt)/1.0)*0.5
add(boom(),0.0,0.9); add(boom(),1.6,1.0); add(whoosh(),3.4,0.5); add(kick(),3.45,0.9); add(whoosh(),5.5,0.5)
for x in [7.35,9.5,12.9,13.75,15.1]: add(tone(1600,0.06,0.015),x,0.45)
add(tone(1200,0.1,0.03),10.9,0.4)
n=int(0.25*SR); s=np.convolve(rng.standard_normal(n),np.ones(3)/3,'same')*np.linspace(1,0,n); add(s,15.9,0.5)
for f,dt in [(1047,0),(1319,0.08),(1568,0.16)]: add(tone(f,0.7,0.3),16.4+dt,0.4)
add(boom(),18.2,0.9); add(whoosh(),19.25,0.5); add(boom(),21.05,1.0); add(whoosh(),22.5,0.5); add(whoosh(),24.7,0.5)
for f,dt in [(1319,0),(1568,0.09),(1976,0.18)]: add(tone(f,0.8,0.3),24.85+dt,0.35)
out/=np.max(np.abs(out))*1.1
st=np.stack([out,out],1)
with wave.open('/tmp/sfxV.wav','wb') as wf:
    wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes((st*32767).astype('<i2').tobytes())
