import numpy as np, wave, sys
SR=44100; v=sys.argv[1]; TOT={'A':31.4,'B':38.0}[v]; N=int(SR*TOT); out=np.zeros(N); rng=np.random.default_rng(7)
def add(sig,t0,g=1.0):
    i=int(t0*SR); j=min(N,i+len(sig))
    if i<N: out[i:j]+=g*sig[:j-i]
def tone(f,dur,d=0.1,a=0.004):
    n=int(dur*SR); tt=np.arange(n)/SR; return np.sin(2*np.pi*f*tt)*np.minimum(1,tt/a)*np.exp(-tt/d)
def whoosh():
    n=int(0.3*SR); w=np.convolve(rng.standard_normal(n),np.ones(5)/5,'same'); return w*np.sin(np.pi*np.arange(n)/n)**2
def kick():
    kt=np.arange(int(0.3*SR))/SR; return np.sin(2*np.pi*(45+110*np.exp(-kt/0.03))*kt)*np.exp(-kt/0.13)
if v=='A': W=[0.05,5.75,11.5,17.4,21.6,24.5]; P=[0.9,6.0,11.6,19.4,26.4]
else: W=[0.0,5.6,11.1,16.8,21.0,23.7,30.9,35.5]; P=[0.9,5.9,11.3,18.9,24.6,27.2,28.9,33.2,35.7]
for x in W: add(whoosh(),x,0.45)
add(kick(),0.08,0.9)
for x in P: add(tone(1800,0.06,0.015),x,0.35)
out/=np.max(np.abs(out))*1.1
st=np.stack([out,out],1)
with wave.open(f'/tmp/sfx{v}.wav','wb') as wf:
    wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes((st*32767).astype('<i2').tobytes())
