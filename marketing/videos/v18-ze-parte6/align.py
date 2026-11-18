import numpy as np, subprocess, json, re, sys
# áudio mono 16 kHz
raw = subprocess.run(['ffmpeg','-v','error','-i','narracao.mp3','-ac','1','-ar','16000','-f','f32le','-'],capture_output=True,check=True).stdout
x = np.frombuffer(raw,dtype='<f4'); sr=16000
hop=160  # 10 ms
n=len(x)//hop
env=np.array([np.sqrt(np.mean(x[i*hop:(i+1)*hop+160]**2)+1e-12) for i in range(n)])
db=20*np.log10(env+1e-9)
thr=db.max()-38
speech=db>thr
# regiões de fala (fecha buracos < 0.12 s)
regs=[];i=0
while i<n:
    if speech[i]:
        j=i
        while j<n and (speech[j] or (j+12<n and speech[j:j+12].any())): j+=1
        regs.append([i/100,(j)/100]); i=j
    else: i+=1
# remove fim silencioso
print(len(regs),'trechos');
for r in regs: print(round(r[0],2),round(r[1],2),round(r[1]-r[0],2))
json.dump({'regs':regs,'db':db.tolist()},open('env.json','w'))
