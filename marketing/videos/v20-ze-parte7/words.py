import json, numpy as np
d=json.load(open('env.json')); db=np.array(d['db'])
regs=[(0.02,2.16),(2.39,4.64),(5.12,10.53),(10.92,13.41),(14.02,14.5),(14.68,16.88),(17.39,17.85),(18.07,19.01),(19.57,22.38)]
chunks=[
 [("O",1),("Zé",1),("parou",2),("e",1),("ajudou",3),("o",1),("colega.",2)],
 [("Duas",2),("horas",2),("depois,",3),("pneu",2),("trocado.",3)],
 [("O",1),("colega",2),("agradeceu",3),("e",1),("avisou:",3),("tem",1),("um",1),("frete",2),("de",1),("volta,",3),("pagando",3),("bem,",2),("saindo",2),("amanhã",3),("cedo.",2)],
 [("Mas",1),("a",1),("filha",2),("do",1),("Zé",1),("espera",3),("ele",1),("pro",1),("jantar.",3)],
 [("A:",1)],
 [("ele",1),("aceita",3),("o",1),("frete",2),("e",1),("liga",2),("pra",1),("filha.",2)],
 [("B:",1)],
 [("ele",1),("vai",1),("pra",1),("casa.",2)],
 [("O",1),("que",1),("o",1),("Zé",1),("faz?",1),("Comenta",3),("A",1),("ou",1),("B.",1)]
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
print(len(out)); print([ (i,w['text'],w['start']) for i,w in enumerate(out)])
