import numpy as np, wave
SR=44100; TOT=34.75; N=int(SR*TOT); out=np.zeros(N); rng=np.random.default_rng(7)
def add(sig,t0,g=1.0):
    i=int(t0*SR); j=min(N,i+len(sig))
    if i<N: out[i:j]+=g*sig[:j-i]
def tone(f,dur,d=0.1,a=0.004):
    n=int(dur*SR); tt=np.arange(n)/SR; return np.sin(2*np.pi*f*tt)*np.minimum(1,tt/a)*np.exp(-tt/d)
def whoosh():
    n=int(0.3*SR); w=np.convolve(rng.standard_normal(n),np.ones(5)/5,'same'); return w*np.sin(np.pi*np.arange(n)/n)**2
def kick():
    kt=np.arange(int(0.3*SR))/SR; return np.sin(2*np.pi*(45+110*np.exp(-kt/0.03))*kt)*np.exp(-kt/0.13)
W=[0.05,3.64,6.8,12.4,15.15,20.5,22.6,24.6,27.45,29.0,32.8]
P=[0.9,4.92,7.7,9.0,10.7,13.2,16.0,17.3,18.7,21.2,22.8,23.5,25.5,26.0,29.5,30.6,33.3]
for x in W: add(whoosh(),x,0.45)
add(kick(),0.08,0.9)
for x in P: add(tone(1800,0.06,0.015),x,0.35)
out/=np.max(np.abs(out))*1.1
st=np.stack([out,out],1)
with wave.open('/tmp/sfxC.wav','wb') as wf:
    wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes((st*32767).astype('<i2').tobytes())
