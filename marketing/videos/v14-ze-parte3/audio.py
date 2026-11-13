# Mixa narração + cama suave + efeitos (cues.json). Saída: audio.wav (loudnorm feito no ffmpeg final).
import numpy as np, wave, json, subprocess
SR=44100; TOT=20.6; N=int(SR*TOT); out=np.zeros(N); rng=np.random.default_rng(7)
def add(sig,t0,g=1.0):
    i=int(t0*SR); j=min(N,i+len(sig))
    if 0<=i<N: out[i:j]+=g*sig[:j-i]
def tone(f,dur,d=0.1,a=0.004):
    n=int(dur*SR); tt=np.arange(n)/SR; return np.sin(2*np.pi*f*tt)*np.minimum(1,tt/a)*np.exp(-tt/d)
def whoosh():
    n=int(0.35*SR); w=np.convolve(rng.standard_normal(n),np.ones(6)/6,'same'); return w*np.sin(np.pi*np.arange(n)/n)**2
def slam():
    kt=np.arange(int(0.35*SR))/SR; return np.sin(2*np.pi*(50+120*np.exp(-kt/0.03))*kt)*np.exp(-kt/0.12)
def ring():
    n=int(1.0*SR); tt=np.arange(n)/SR; m=(np.sin(2*np.pi*20*tt)>0)*1.0
    return (np.sin(2*np.pi*1400*tt)+np.sin(2*np.pi*1700*tt))*m*np.exp(-tt/1.2)*0.5
K={'whoosh':(whoosh,0.16),'slam':(slam,0.5),'ring':(ring,0.22),'tick':(lambda:tone(2200,0.04,0.01),0.12),
   'pop':(lambda:tone(700,0.1,0.04),0.3),'ding':(lambda:tone(1319,0.5,0.2)+tone(1568,0.5,0.2),0.14),'thud':(lambda:slam()*0.7,0.3)}
for c in json.load(open('cues.json')):
    f,g=K[c['k']]; add(f(),c['t'],g)
# cama: pulso grave suave
for b in range(int(TOT/0.6)):
    tb=b*0.6; kt=np.arange(int(0.25*SR))/SR
    add(np.sin(2*np.pi*(48+60*np.exp(-kt/0.03))*kt)*np.exp(-kt/0.1),tb,0.09)
    add(tone([196,247,294,247][(b//2)%4],0.5,0.3),tb,0.025)
fx=out/(np.max(np.abs(out))+1e-9)*0.45
subprocess.run(['ffmpeg','-v','error','-y','-i','narracao.mp3','-ar',str(SR),'-ac','1','/tmp/voz.wav'],check=True)
w=wave.open('/tmp/voz.wav'); v=np.frombuffer(w.readframes(w.getnframes()),'<i2')/32768.0
vo=np.zeros(N); vo[:min(N,len(v))]=v[:N]
# abaixa efeitos quando a voz fala (ducking simples)
env=np.convolve(np.abs(vo),np.ones(2205)/2205,'same'); duck=1-0.55*np.clip(env/0.05,0,1)
mix=vo*0.95+fx*duck
mix/=max(1,np.max(np.abs(mix))*1.05)
fade=int(0.6*SR); mix[-fade:]*=np.linspace(1,0,fade)
st=np.stack([mix,mix],1)
with wave.open('audio.wav','wb') as wf:
    wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes((st*32767).astype('<i2').tobytes())
print('audio ok')
