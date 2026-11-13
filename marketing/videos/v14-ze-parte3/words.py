import json, numpy as np
d=json.load(open('env.json')); db=np.array(d['db'])
regs=[[0.06,1.60],[2.20,3.94],[4.15,5.71],[6.23,6.99],[7.34,9.77],[10.15,10.84],[11.14,14.47],[14.92,16.52],[16.92,18.26],[18.63,19.82]]
chunks=[
 [("Fixo",2),("ou",1),("comissão?",3)],
 [("O",1),("Zé",1),("é",1),("motorista",4),("empregado,",4)],
 [("e",1),("duas",2),("empresas",3),("querem",2),("ele.",2)],
 [("Empresa",3),("A:",1)],
 [("salário",3),("fixo",2),("de",1),("quatro",2),("mil",1),("e",1),("quinhentos.",3)],
 [("Empresa",3),("B:",1)],
 [("dois",1),("mil",1),("e",1),("setecentos,",4),("mais",1),("seis",1),("por",1),("cento",2),("de",1),("cada",2),("frete.",2)],
 [("Qual",1),("paga",2),("mais",1),("no",1),("fim",1),("do",1),("mês?",1)],
 [("Comenta",3),("A",1),("ou",1),("B.",1)],
 [("Amanhã",3),("eu",1),("mostro",2),("a",1),("conta.",2)],
]
assert len(chunks)==len(regs)
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
json.dump(out,open('words.json','w'),ensure_ascii=False,indent=0); print(len(out),'palavras')
