import numpy as np, wave
SR=44100; TOT=22.0; N=int(SR*TOT); out=np.zeros(N); rng=np.random.default_rng(11)
def add(sig,t0,g=1.0):
    i=int(t0*SR); j=min(N,i+len(sig))
    if i<N: out[i:j]+=g*sig[:j-i]
def tone(f,dur,d=0.1,a=0.004):
    n=int(dur*SR); tt=np.arange(n)/SR; return np.sin(2*np.pi*f*tt)*np.minimum(1,tt/a)*np.exp(-tt/d)
def kick(g=0.6):
    kt=np.arange(int(0.3*SR))/SR; return g*np.sin(2*np.pi*(45+110*np.exp(-kt/0.03))*kt)*np.exp(-kt/0.13)
def whoosh():
    n=int(0.3*SR); w=np.convolve(rng.standard_normal(n),np.ones(5)/5,'same'); return w*np.sin(np.pi*np.arange(n)/n)**2
beat=0.5; bass=[65.4,65.4,87.3,98]
for b in range(int(TOT/beat)):
    tb=b*beat
    if tb>=3.5: add(kick(),tb)
    n=int(0.08*SR); h=np.diff(rng.standard_normal(n)*np.exp(-np.arange(n)/SR/0.02),prepend=0); add(h,tb+beat/2,0.1)
    bt=np.arange(int(0.4*SR))/SR; add(np.sin(2*np.pi*bass[(b//4)%4]*bt)*np.exp(-bt/0.25),tb,0.2)
    f=[523.3,659.3,784,659.3][b%4]; add(tone(f,0.3,0.1),tb+beat/2,0.05)
for x in [0.02,1.2,4.5,12.4,17.8]: add(whoosh(),x,0.3)
add(kick(1.0),0.1); add(kick(1.0),4.6); add(kick(1.0),13.4); add(kick(1.0),10.4)
for k in range(26): add(tone(1800,0.03,0.01),1.3+k*0.1,0.12)
for x in [5.4,7.6]:  # caixa registradora
    add(tone(2400,0.06,0.015),x,0.35); add(tone(3200,0.5,0.12),x+0.06,0.2)
for f,dt in [(1047,0),(1319,0.09),(1568,0.18)]: add(tone(f,0.8,0.3),11.6+dt,0.3)
for f,dt in [(1319,0),(1568,0.09),(1976,0.18),(2637,0.27)]: add(tone(f,0.9,0.35),14.8+dt,0.3)
add(tone(1568,0.6,0.25),18.0,0.2)
out[int(21.3*SR):]*=np.linspace(1,0,N-int(21.3*SR))
out/=np.max(np.abs(out))*1.1
st=np.stack([out,out],1)
with wave.open('audio.wav','wb') as wf:
    wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes((st*32767).astype('<i2').tobytes())
