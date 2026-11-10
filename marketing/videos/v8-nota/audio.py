import numpy as np, wave
SR=44100; TOT=28.5; END=23.6; STAMP=13.3
N=int(SR*TOT); out=np.zeros(N); rng=np.random.default_rng(3); t=np.arange(N)/SR
def add(sig,t0,g=1.0):
    i=int(t0*SR); j=min(N,i+len(sig))
    if i<N: out[i:j]+=g*sig[:j-i]
def tone(f,dur,d=0.1,a=0.004):
    n=int(dur*SR); tt=np.arange(n)/SR; return np.sin(2*np.pi*f*tt)*np.minimum(1,tt/a)*np.exp(-tt/d)
def lp(x,k=8):
    return np.convolve(x,np.ones(k)/k,'same')
# música: 100 bpm, pluck C G Am F + kick/clap
bpm=100; beat=60/bpm; bar=4*beat
prog=[[261.6,329.6,392],[246.9,293.7,392],[220,261.6,329.6],[220,261.6,349.2]]
bass=[65.4,98,110,87.3]
mus=np.zeros(N)
def madd(sig,t0,g):
    i=int(t0*SR); j=min(N,i+len(sig))
    if i<N: mus[i:j]+=g*sig[:j-i]
nb=int(TOT/beat)+1
for b in range(nb):
    tb=b*beat; ch=prog[(b//4)%4]
    for s in range(2):
        f=ch[(b*2+s)%3]*2
        madd(tone(f,0.35,0.12)+0.3*tone(f*2,0.35,0.05),tb+s*beat/2,0.07)
    kt=np.arange(int(0.25*SR))/SR
    if b%2==0: madd(np.sin(2*np.pi*(48+100*np.exp(-kt/0.03))*kt)*np.exp(-kt/0.12),tb,0.5)
    else:
        n=int(0.12*SR); c=rng.standard_normal(n)*np.exp(-np.arange(n)/SR/0.03); madd(np.diff(c,prepend=0),tb,0.12)
    bt=np.arange(int(0.5*SR))/SR
    madd(np.sin(2*np.pi*bass[(b//4)%4]*bt)*np.exp(-bt/0.3),tb,0.2)
mus[int((TOT-1.2)*SR):]*=np.linspace(1,0,N-int((TOT-1.2)*SR))
mus*=np.where(t<0.9,0.35,np.where(t<END,0.55,0.85))
out+=mus
# gancho: impacto no número
kt=np.arange(int(0.6*SR))/SR
add(np.sin(2*np.pi*(40+80*np.exp(-kt/0.05))*kt)*np.exp(-kt/0.3),0.9,0.7)
# impressora: zumbido picotado por linha
L=[4.2,5.9,7.6,9.3,11.0,12.6]
for x in L:
    n=int(0.4*SR); nz=lp(rng.standard_normal(n),3); tt=np.arange(n)/SR
    buzz=nz*(0.6+0.4*np.sign(np.sin(2*np.pi*55*tt)))*np.minimum(1,tt/0.02)*np.minimum(1,(0.4-tt)/0.05)
    add(buzz,x-0.35,0.10)
# contador: tiques
for x in L[:5]:
    for k in range(9): add(tone(2200+rng.uniform(-200,200),0.03,0.008),x+k*0.075,0.12)
# plim do total
for f,dt in [(1047,0),(1319,0.09),(1568,0.18)]: add(tone(f,0.6,0.25),STAMP+dt,0.25)
# whoosh saída da nota e entrada do final
for x in [16.0,END-0.2]:
    n=int(0.5*SR); w=lp(rng.standard_normal(n),4)*np.sin(np.pi*np.arange(n)/n)**2; add(w,x,0.35)
# pop das legendas e do final
for x in [14.6,18.0,20.8,END+0.2,END+0.55,END+1.1,END+1.8]: add(tone(880,0.12,0.04),x,0.25)
add(np.sin(2*np.pi*(40+70*np.exp(-kt/0.05))*kt)*np.exp(-kt/0.3),END,0.6)
out/=np.max(np.abs(out))*1.1
st=np.stack([out,out],1)
with wave.open('audio.wav','wb') as wf:
    wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes((st*32767).astype('<i2').tobytes())
print('ok')
