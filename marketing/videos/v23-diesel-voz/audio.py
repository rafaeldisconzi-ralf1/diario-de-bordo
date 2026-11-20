import numpy as np, wave
SR=44100; TOT=33.0; N=int(SR*TOT); out=np.zeros(N); rng=np.random.default_rng(7)
def add(sig,t0,g=1.0):
    i=int(t0*SR); j=min(N,i+len(sig))
    if i<N: out[i:j]+=g*sig[:j-i]
def tone(f,dur,d=0.1,a=0.004):
    n=int(dur*SR); tt=np.arange(n)/SR; return np.sin(2*np.pi*f*tt)*np.minimum(1,tt/a)*np.exp(-tt/d)
def kick(g=0.6):
    kt=np.arange(int(0.3*SR))/SR; return g*np.sin(2*np.pi*(45+110*np.exp(-kt/0.03))*kt)*np.exp(-kt/0.13)
def whoosh():
    n=int(0.3*SR); w=np.convolve(rng.standard_normal(n),np.ones(5)/5,'same'); return w*np.sin(np.pi*np.arange(n)/n)**2
for x in [0.02,5.1,11.1,17.5,22.1,25.3,28.35]: add(whoosh(),x,0.5)
add(kick(1.0),0.1); add(kick(1.0),8.8); add(kick(1.0),18.1)
for x in [6.3,11.4,13.2,15.9]: add(tone(1800,0.05,0.012),x,0.4)
for x in [1.7,19.1]:
    add(tone(2400,0.06,0.015),x,0.5); add(tone(3200,0.5,0.12),x+0.06,0.3)
for f,dt in [(1319,0),(1568,0.09),(1976,0.18),(2637,0.27)]: add(tone(f,0.9,0.35),27.3+dt,0.4)
for f,dt in [(1047,0),(1319,0.09),(1568,0.18)]: add(tone(f,0.8,0.3),28.45+dt,0.3)
out/=np.max(np.abs(out))*1.1
st=np.stack([out,out],1)
with wave.open('sfx.wav','wb') as wf:
    wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes((st*32767).astype('<i2').tobytes())
