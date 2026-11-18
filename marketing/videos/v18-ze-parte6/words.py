import json, numpy as np
d=json.load(open('env.json')); db=np.array(d['db'])
regs=[r for r in d['regs'] if r[1]-r[0]>0.05]
chunks=[
 [("Vocês",2),("escolheram",3),("A.",1)],
 [("O",1),("Zé",1),("esperou",3),("os",1),("dois",2),("dias",2),("e",1),("cobrou",2),("a",1),("diária.",2)],
 [("Ligou",2),("pra",1),("filha",2),("por",1),("vídeo",2),("e",1),("prometeu",3),("um",1),("presente.",3)],
 [("Agora,",2),("voltando",3),("pra",1),("casa,",2)],
 [("viu",1),("um",1),("colega",2),("parado",2),("com",1),("o",1),("pneu",2),("furado.",2)],
 [("Ajudar",2),("leva",2),("duas",2),("horas,",2),("e",1),("o",1),("Zé",1),("prometeu",3),("chegar",2),("pro",1),("jantar.",2)],
 [("A:",1)],
 [("ele",1),("para",2),("e",1),("ajuda.",2)],
 [("B:",1),("ele",1),("segue",2),("viagem.",2)],
 [("O",1),("que",1),("o",1),("Zé",1),("faz?",1)],
 [("Comenta",3),("A",1)],
 [("ou",1),("B.",1)]
]
assert len(chunks)==len(regs),(len(chunks),len(regs))
sm=np.convolve(db,np.ones(3)/3,'same'); out=[]; wid=0
for (s,e),ws in zip(regs,chunks):
    w=np.array([c[1]+0.4 for c in ws],float); cum=np.concatenate([[0],np.cumsum(w)])/w.sum()
    t=[s+(e-s)*c for c in cum]
    for i in range(1,len(ws)):
        c=int(round(t[i]*100)); lo,hi=max(c-7,0),min(c+8,len(sm)); t[i]=(lo+int(np.argmin(sm[lo:hi])))/100
    for i in range(1,len(ws)): t[i]=max(t[i],t[i-1]+0.08)
    t[-1]=e
    for i,(txt,_) in enumerate(ws):
        out.append({"id":wid,"text":txt,"start":round(t[i],3),"end":round(t[i+1],3)}); wid+=1
json.dump(out,open('words.json','w'),ensure_ascii=False,indent=0)
for i,w in enumerate(out): print(i,w['text'],w['start'],end=' | ')
