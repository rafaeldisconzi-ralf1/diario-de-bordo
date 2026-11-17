import json, numpy as np
d=json.load(open('env.json')); db=np.array(d['db'])
regs=[r for r in d['regs']]
chunks=[
 [("Vocês",2),("escolheram",3),("B.",1)],
 [("O",1),("Zé",1),("pegou",2),("a",1),("viagem",2),("mais",2),("curta",2),("e",1),("chegou",2),("no",1),("destino.",3)],
 [("Mas",1),("na",1),("descarga,",3),("o",1),("conferente",3),("avisou:",2)],
 [("só",1),("vão",1),("descarregar",3),("daqui",2),("a",1),("dois",2),("dias.",2)],
 [("E",1),("hoje",2),("é",1),("aniversário",3),("da",1),("filha",2),("do",1),("Zé.",1)],
 [("A:",1)],
 [("ele",1),("espera",2),("os",1),("dois",2),("dias",2),("e",1),("cobra",2),("a",1),("diária.",2)],
 [("B:",1)],
 [("larga",2),("tudo",2),("e",1),("vai",1),("pra",1),("casa.",2)],
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
