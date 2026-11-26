import json
# dados inventados: Carlos, Scania R 450, ABC 1D23
T=lambda **k:k
fechada=dict(id='t1',origem='Chapecó',destino='Curitiba',kmIni=182400,kmFim=182880,tipo='km',distancia=480,valorKm=9.5,valorFechado=0,comissao=0,
  inicio='2026-11-03',fim='2026-11-04',status='fechada',itens=[
  dict(id='i1',tipo='diesel',litros=180,preco=6.19,valor=1114.2,data='2026-11-03',obs='',criado=1),
  dict(id='i2',tipo='gasto',cat='Pedágio',valor=187.8,data='2026-11-03',obs='',criado=2),
  dict(id='i3',tipo='gasto',cat='Comida',valor=60,data='2026-11-04',obs='',criado=3),
  dict(id='i5',tipo='gasto',cat='Manutenção',valor=332.4,data='2026-11-04',obs='Troca de lona',criado=5)])
ativa=dict(id='t2',origem='Curitiba',destino='Santos',kmIni=182880,tipo='km',distancia=420,valorKm=9.0,valorFechado=0,comissao=0,
  inicio='2026-11-24',fim=None,status='aberta',itens=[
  dict(id='i4',tipo='gasto',cat='Pedágio',valor=92.4,data='2026-11-24',obs='',criado=4)])
S=dict(exemplo=False,trips=[fechada,ativa],avulsos=[],perfil=dict(nome='Carlos',modelo='Scania R 450',placa='ABC 1D23',ano='2021',patrao=''),sync=dict(h={},ultimo=None))
json.dump(S,open('estado.json','w'),ensure_ascii=False)
f=480*9.5; print('frete t1',f,'sobra t1',f-1114.2-187.8-60-332.4)
