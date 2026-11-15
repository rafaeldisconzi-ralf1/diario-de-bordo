import json, numpy as np
d=json.load(open('env.json')); db=np.array(d['db'])
regs=[r for r in d['regs']]
chunks=[
 [("Fixo",2),("ou",1)],
 [("comissão?",3)],
 [("A",1),("conta",2),("do",1),("Zé.",1)],
 [("A",1),("empresa",3),("A",1),("paga",2),("quatro",2),("mil",1),("e",1),("quinhentos",3),("fixo.",2)],
 [("Na",1),("empresa",3),("B,",1),("cada",2),("frete",2),("de",1),("oito",2),("mil",1),("rende",2),("quatrocentos",4),("e",1),("oitenta",3),("de",1),("comissão.",3)],
 [("Com",1),("três",1),("viagens",3),("no",1),("mês,",1),("a",1),("B",1),("paga",2),("quatro",2),("mil",1),("cento",2),("e",1),("quarenta:",3)],
 [("o",1),("fixo",2),("ganha.",2)],
 [("Com",1),("quatro",2),("viagens,",3),("a",1),("B",1),("paga",2),("quatro",2),("mil",1),("seiscentos",3),("e",1),("vinte:",2)],
 [("a",1),("comissão",3),("ganha.",2)],
 [("Com",1),("cinco,",2),("passa",2),("de",1),("cinco",2),("mil.",1)],
 [("Ou",1),("seja:",2)],
 [("depende",3),("de",1),("quantas",2),("viagens",3),("você",2),("faz.",1)],
 [("E",1),("agora?",3)],
 [("O",1),("Zé",1),("quer",1),("comprar",2),("o",1),("próprio",2),("caminhão,",3),("financiado.",4)],
 [("A:",1)],
 [("ele",1),("compra.",2)],
 [("B:",1)],
 [("continua",3),("empregado.",4)],
 [("Comenta",3),("A",1)],
 [("ou",1),("B.",1)],
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
