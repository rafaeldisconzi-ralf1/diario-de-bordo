import numpy as np, wave
SR=44100; TOT=28.0; N=int(SR*TOT); out=np.zeros(N); rng=np.random.default_rng(11); tt=np.arange(N)/SR
def add(sig,t0,g=1.0):
    i=int(t0*SR); j=min(N,i+len(sig))
    if i<N: out[i:j]+=g*sig[:j-i]
def tone(f,dur,d=0.1,a=0.004):
    n=int(dur*SR); t=np.arange(n)/SR; return np.sin(2*np.pi*f*t)*np.minimum(1,t/a)*np.exp(-t/d)
def whoosh():
    n=int(0.32*SR); w=np.convolve(rng.standard_normal(n),np.ones(6)/6,'same'); return w*np.sin(np.pi*np.arange(n)/n)**2
def kick():
    kt=np.arange(int(0.3*SR))/SR; return np.sin(2*np.pi*(45+110*np.exp(-kt/0.03))*kt)*np.exp(-kt/0.13)
def tick(f=2600):
    n=int(0.04*SR); t=np.arange(n)/SR; return (np.sin(2*np.pi*f*t)+0.5*rng.standard_normal(n)*0.3)*np.exp(-t/0.006)
S1,S2,TA,TB,RV,E=3.0,9.2,10.0,20.0,20.6,24.6
# fundo suave (só até o relógio e depois da revelação)
bed=np.zeros(N); bar=2.0; ch=[[220,277.2,329.6],[196,246.9,293.7],[174.6,220,261.6],[196,246.9,293.7]]
for k in range(int(TOT/bar)+1):
    for f in ch[k%4]:
        n=int(bar*SR); t=np.arange(n)/SR; env=np.minimum(1,t/0.3)*np.minimum(1,(bar-t)/0.4)
        i=int(k*bar*SR); j=min(N,i+n)
        if i<N: bed[i:j]+=((0.5*np.sin(2*np.pi*f*t)+0.2*np.sin(4*np.pi*f*t))*env)[:j-i]
bed/=np.max(np.abs(bed)); duck=np.where((tt>TA-0.2)&(tt<RV),0.25,1.0)
out+=0.35*bed*duck*np.minimum(1,tt/0.6)*np.minimum(1,(TOT-tt)/1.0)
add(whoosh(),0.0,0.6); add(kick(),0.05,0.9); add(tone(1800,0.06,0.015),0.35,0.4); add(tone(1800,0.06,0.015),1.4,0.4)
add(whoosh(),S1-0.1,0.5)
for x in [S1+0.5,S1+1.4,S1+2.4,S1+3.2,S1+4.2]:   # impressora da nota
    for k in range(5): add(tick(1400+200*k),x+k*0.025,0.25)
add(tone(1500,0.08,0.02),S1+5.0,0.4)
add(whoosh(),S2-0.1,0.5)
for x in [S2+0.2,S2+0.45,S2+0.7]: add(tone(1700,0.06,0.015),x,0.4)
for k in range(10):                                # relógio
    hi = k>=7
    add(tick(3200 if hi else 2400),TA+k,0.9 if hi else 0.7); add(tick(1800),TA+k+0.5,0.35)
bz=np.arange(int(0.6*SR))/SR; add(np.sign(np.sin(2*np.pi*110*bz))*np.exp(-bz/0.35)*0.5,TB,0.8)   # campainha
add(kick(),RV,1.0)
for f,dt in [(1047,0),(1319,0.08),(1568,0.16),(2093,0.24)]: add(tone(f,0.9,0.35),RV+dt,0.45)
for k in range(30): add(tick(3000+rng.random()*3000),RV+0.05+rng.random()*1.2,0.12)  # confete
add(tone(1700,0.06,0.015),RV+1.8,0.4); add(whoosh(),E-0.1,0.5)
for f,dt in [(1319,0),(1568,0.09),(1976,0.18)]: add(tone(f,0.8,0.3),E+0.1+dt,0.3)
out/=np.max(np.abs(out))*1.1
st=np.stack([out,out],1)
with wave.open('/tmp/sfxQ.wav','wb') as wf:
    wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes((st*32767).astype('<i2').tobytes())
