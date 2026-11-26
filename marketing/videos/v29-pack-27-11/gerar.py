import json, sys, pathlib
here = pathlib.Path(__file__).parent
ZE = (here / 'ze.svg').read_text()
BASE = (here / 'base.html').read_text()
COMENTA = dict(el='Veja quanto <span class="grn">sobrou</span><br>de verdade', ep='Comenta APP', es='R$ 24,90 por mês · 7 dias de garantia')
AB = dict(el='O que o Zé faz?', ep='Comenta A ou B', es='Amanhã: a conta')

V = {}
# ---------------- V19 "3 jeitos" (anúncio) ----------------
V['v19'] = dict(TOT=42.0, ft=[6, 35.7], end=dict(a=38.4), endtxt=dict(el='Saiba quanto <span class="grn">sobra</span><br>em cada frete', ep='Toque em Saiba mais', es='R$ 24,90 por mês · 7 dias de garantia'),
 ze=[],
 ph=[[0, 2.33, 'Três jeitos de sobrar mais no frete.'], [2.71, 4.85, 'O segundo quase ninguém faz.'], [5.43, 5.65, 'Um:'],
     [6.15, 10.27, 'saiba quanto custa cada quilômetro do seu caminhão antes de fechar.'], [10.69, 14.5, 'Se custa três e cinquenta, frete abaixo disso é prejuízo.'],
     [15.1, 15.62, 'Dois:'], [15.99, 17.55, 'coloque a volta na conta.'], [18.02, 21.45, 'Frete de oito mil por mil e duzentos km parece bom.'],
     [21.82, 25.06, 'Voltando vazio, são dois mil e quatrocentos km.'], [25.43, 27.96, 'Custa oito mil quatrocentos e setenta.'], [28.32, 29.63, 'Você paga pra trabalhar.'],
     [30.2, 30.69, 'Três:'], [31.03, 32.77, 'lance a parcela e o seguro.'], [33.15, 35.46, 'Senão você acha que sobrou mais do que sobrou.'],
     [35.85, 38.12, 'O Diário de Bordo faz essa conta pra você.'], [38.48, 41.95, 'Toque em Saiba mais e teste com sete dias de garantia.']],
 html='''
<div class="abs tag" id="h0" style="top:300px">3 jeitos</div>
<div class="abs big" id="h1" style="top:430px;font-size:190px">Sobrar <span class="grn">mais</span><br>no frete</div>
<div class="abs chip r" id="h2" style="top:900px">O 2º quase ninguém faz</div>
<div class="abs" id="pin" style="left:40px;top:150px;font:800 44px BC;text-transform:uppercase;color:#ff6b5b;border:4px solid #ff6b5b;border-radius:14px;padding:6px 18px 0">o 2º quase ninguém faz</div>
<div class="abs n" id="n1" style="top:330px">1</div><div class="abs nt" id="t1" style="top:360px">Custo<br>por km</div>
<div class="abs cm by" id="c1" style="top:620px"><div class="l">Seu custo</div><div class="v yel">R$ 3,50<span style="font-size:60px">/km</span></div></div>
<div class="abs cm br" id="c2" style="top:880px"><div class="l">Frete abaixo<br>disso</div><div class="v red">prejuízo</div></div>
<div class="abs n" id="n2" style="top:300px">2</div><div class="abs nt" id="t2" style="top:330px">A volta<br>entra na conta</div>
<div class="abs cm" id="c3" style="top:560px"><div class="l">Frete<br>1.200 km</div><div class="v">R$ 8.000</div></div>
<div class="abs" id="rt" style="left:70px;right:70px;top:810px;height:120px;display:flex;gap:10px;font:800 50px BC;text-transform:uppercase;color:#16181b">
 <div id="ida" style="background:#f2b705;border-radius:20px 0 0 20px;display:flex;align-items:center;justify-content:center;width:0;overflow:hidden;white-space:nowrap">ida 1.200 km</div>
 <div id="vol" style="background:#6b6e73;color:#f4f3ee;border-radius:0 20px 20px 0;display:flex;align-items:center;justify-content:center;width:0;overflow:hidden;white-space:nowrap">volta vazia 1.200</div></div>
<div class="abs cm br" id="c4" style="top:980px"><div class="l">Custo<br>2.400 km</div><div class="v red" id="c4v">R$ 0</div></div>
<div class="abs badge r" id="b2" style="top:1195px">−R$ 470: paga pra trabalhar</div>
<div class="abs n" id="n3" style="top:330px">3</div><div class="abs nt" id="t3" style="top:360px">Parcela<br>e seguro</div>
<div class="abs row" id="r1" style="top:640px"><span>Parcela</span><span class="red">−R$ 4.800</span></div>
<div class="abs row" id="r2" style="top:760px"><span>Seguro</span><span class="red">−R$ 900</span></div>
<div class="abs big" id="q3" style="top:960px;font-size:120px">Sobrou <span class="red">menos</span><br>do que parece</div>
<div class="abs ph" id="ph"><img src="app-sobrou.png"></div>''',
 anim='''
 vis('#h0',0,5.3);pop('#h0',0,.9,X);vis('#h1',0,5.3);pop('#h1',0,.85);vis('#h2',2.71,5.3);pop('#h2',2.71,.7,X);
 vis('#pin',5.45,15.0);
 vis('#n1',5.43,14.9);pop('#n1',5.43,.6);vis('#t1',5.6,14.9);vis('#c1',6.6,14.9);pop('#c1',6.6,.9);vis('#c2',10.69,14.9);pop('#c2',10.69,.85);
 vis('#n2',15.1,29.95);pop('#n2',15.1,.6);vis('#t2',15.99,29.95);vis('#c3',18.02,29.95);pop('#c3',18.02,.9);
 vis('#rt',21.82,29.95);$('#ida').style.width=(470*eo((t-21.82)/.7))+'px';$('#vol').style.width=(470*eo((t-22.9)/.7))+'px';
 vis('#c4',25.43,29.95);pop('#c4',25.43,.9);cnt('#c4v',25.6,1.4,0,8470,'R$ ');
 vis('#b2',28.32,29.95);pop('#b2',28.32,.7,X);
 vis('#n3',30.2,35.7);pop('#n3',30.2,.6);vis('#t3',30.3,35.7);slide('#r1',31.03,35.7);slide('#r2',31.8,35.7);vis('#q3',33.15,35.7);pop('#q3',33.15,.8);
 vis('#ph',35.85,38.45);pop('#ph',35.85,.92);''')

# ---------------- R1 "o que o dono esquece" (orgânico) ----------------
V['r1'] = dict(TOT=32.2, ft=[1.4, 23.4], end=dict(a=30.0), endtxt=COMENTA, ze=[],
 ph=[[0, 0.91, 'Dono de caminhão:'], [1.42, 4.49, 'você acha que sobrou oito mil e quatrocentos esse mês?'], [4.92, 7.38, 'Tirou diesel, pedágio e o motorista.'],
     [7.91, 9.62, 'Mas esqueceu a parcela do caminhão:'], [10.05, 11.38, 'quatro mil e oitocentos.'], [11.82, 12.36, 'O seguro:'], [12.71, 13.42, 'novecentos.'],
     [13.89, 14.48, 'Imposto:'], [14.85, 15.68, 'seiscentos.'], [16.11, 16.69, 'Contador:'], [16.97, 18.15, 'trezentos e cinquenta.'],
     [18.61, 21.6, 'Sobrou de verdade mil setecentos e cinquenta.'], [21.98, 23.35, 'Um quinto do que parecia.'],
     [24.03, 29.63, 'No Diário de Bordo você lança essas contas mesmo fora de viagem e vê a sobra certa do mês.'], [30.07, 31.87, 'Comenta APP que eu te mando o link.']],
 html='''
<div class="abs tag" id="h0" style="top:300px">Dono de caminhão</div>
<div class="abs big" id="h1" style="top:480px;font-size:150px">Sobrou<br><span class="grn">R$ 8.400</span><br>esse mês?</div>
<div class="abs tag" id="k0" style="top:300px;background:#5fd39a">Você tirou</div>
<div class="abs row" id="k1" style="top:470px"><span>Diesel</span><span class="grn">OK</span></div>
<div class="abs row" id="k2" style="top:590px"><span>Pedágio</span><span class="grn">OK</span></div>
<div class="abs row" id="k3" style="top:710px"><span>Motorista</span><span class="grn">OK</span></div>
<div class="abs" id="tot" style="left:70px;right:70px;top:250px;display:flex;justify-content:space-between;align-items:baseline;font:800 70px BC;text-transform:uppercase"><span class="gr">Sobra</span><span id="totv" style="font-size:130px" class="grn">R$ 8.400</span></div>
<div class="abs tag" id="e0" style="top:440px;background:#ff6b5b">Mas esqueceu</div>
<div class="abs row" id="e1" style="top:580px"><span>Parcela</span><span class="red">−R$ 4.800</span></div>
<div class="abs row" id="e2" style="top:700px"><span>Seguro</span><span class="red">−R$ 900</span></div>
<div class="abs row" id="e3" style="top:820px"><span>Imposto</span><span class="red">−R$ 600</span></div>
<div class="abs row" id="e4" style="top:940px"><span>Contador</span><span class="red">−R$ 350</span></div>
<div class="abs big" id="s1" style="top:440px;font-size:130px">Sobrou de<br>verdade</div>
<div class="abs big grn" id="s2" style="top:720px;font-size:260px">R$ 1.750</div>
<div class="abs chip r" id="s3" style="top:1040px">1/5 do que parecia</div>
<div class="abs ph" id="ph"><div class="app"><div class="hd"><small>SCANIA R 450 · ABC 1D23</small><b>Gastei</b></div><div class="bd">
 <div style="font:700 30px B;margin-bottom:20px;color:#6b6e73">Fora de viagem · escolha o dia</div>
 <div class="btn" id="g1" style="background:#c4410f">Parcela do caminhão</div><div class="btn" id="g2" style="background:#c4410f">Seguro</div>
 <div class="btn" id="g3" style="background:#c4410f">Imposto</div><div class="btn" id="g4" style="background:#c4410f">Contador</div>
 <div class="fld" style="margin-top:26px">Sobra do mês<b style="color:#1f7a4d">R$ 1.750,00</b></div></div></div></div>''',
 anim='''
 vis('#h0',0,4.7);pop('#h0',0,.9,X);vis('#h1',1.42,4.7);pop('#h1',1.42,.8);
 vis('#k0',4.92,7.75);pop('#k0',4.92,.9,X);slide('#k1',5.0,7.75);slide('#k2',5.7,7.75);slide('#k3',6.4,7.75);
 vis('#tot',7.91,18.4);
 const v=8400-4800*eo((t-10.05)/.6)-900*eo((t-12.71)/.5)-600*eo((t-14.85)/.5)-350*eo((t-16.97)/.5);$('#totv').textContent='R$ '+fmi(v);
 $('#totv').className=v<5000?'red':'grn';
 vis('#e0',7.91,18.4);pop('#e0',7.91,.9,X);slide('#e1',10.05,18.4);slide('#e2',12.71,18.4);slide('#e3',14.85,18.4);slide('#e4',16.97,18.4);
 vis('#s1',18.61,23.6);vis('#s2',19.4,23.6);pop('#s2',19.4,.6);vis('#s3',21.98,23.6);pop('#s3',21.98,.7,X);
 vis('#ph',24.03,29.95);pop('#ph',24.03,.92);
 ['#g1','#g2','#g3','#g4'].forEach((id,i)=>{const a=25.2+i*0.7;$(id).style.outline=(t>a&&t<a+0.7)?'8px solid #f2b705':'none'});''')

# ---------------- Zé "qual posto?" (orgânico A ou B) ----------------
V['posto'] = dict(TOT=30.5, ft=[4.0, 26.6], end=dict(a=26.8), endtxt=AB, ze=[[0, 3.55, 'calm'], [24.0, 26.6, 'worried', 0, .9]],
 ph=[[0, 1.6, 'O Zé vai encher o tanque.'], [2.09, 3.51, 'Qual posto sai mais barato?'], [4.06, 6.25, 'O posto A fica na beira da estrada.'],
     [6.62, 8.13, 'Diesel a sete e trinta.'], [8.7, 10.88, 'O posto B vende a seis e oitenta,'], [11.1, 13.7, 'mas fica sessenta km fora do caminho,'],
     [13.91, 14.57, 'ida e volta.'], [15.12, 17.48, 'O Zé precisa de quatrocentos litros.'], [17.92, 20.53, 'O caminhão faz dois km e meio por litro.'],
     [21.02, 23.57, 'Parece que o B economiza duzentos reais.'], [24.06, 26.39, 'Mas e o diesel que ele gasta no desvio?'],
     [26.87, 28.14, 'Comenta A ou B.'], [28.53, 29.86, 'Amanhã eu mostro a conta.']],
 html='''
<div class="abs tag" id="h0" style="top:230px">Pergunta do Zé</div>
<div class="abs big" id="h1" style="top:1000px;font-size:150px">Qual posto<br>sai mais <span class="yel">barato?</span></div>
<div class="abs cm by" id="pa" style="top:330px"><div class="l"><span class="yel" style="font-size:110px">A</span><br>Beira da<br>estrada</div><div class="v yel" id="pav">R$ 7,30</div></div>
<div class="abs cm" id="pb" style="top:680px;border:5px solid #c9c5ba"><div class="l"><span style="font-size:110px;color:#f4f3ee">B</span><br>60 km fora<br>do caminho</div><div class="v">R$ 6,80</div></div>
<div class="abs chip" id="d1" style="top:330px">400 litros</div>
<div class="abs chip" id="d2" style="top:520px">2,5 km por litro</div>
<div class="abs big" id="e1" style="top:760px;font-size:130px">B economiza<br><span class="grn">R$ 200?</span></div>
<div class="abs big" id="q1" style="top:1000px;font-size:140px">E o diesel<br>do <span class="red">desvio?</span></div>''',
 anim='''
 vis('#h0',0,3.55);pop('#h0',0,.9,X);vis('#h1',2.09,3.55);pop('#h1',2.09,.8);
 vis('#pa',4.06,14.9);pop('#pa',4.06,.9);vis('#pb',8.7,14.9);pop('#pb',8.7,.9);
 vis('#d1',15.12,23.8);pop('#d1',15.12,.7,X);vis('#d2',17.92,23.8);pop('#d2',17.92,.7,X);
 vis('#e1',21.02,23.8);pop('#e1',21.02,.8);vis('#q1',24.06,26.7);pop('#q1',24.06,.8);''')

# ---------------- R2 Zé "mão suja" (IA, guardar) ----------------
V['r2'] = dict(TOT=18.9, ft=[0, 0], end=dict(a=17.3), endtxt=COMENTA | dict(el='Fala que o<br><span class="yel">Diário</span> anota'), ze=[[0, 3.5, 'calm'], [3.85, 6.1, 'worried']],
 ph=[[0, 1.72, 'O Zé acabou de abastecer.'], [2.04, 3.46, 'Mão preta de graxa.'], [3.9, 4.95, 'Digitar no celular?'], [5.2, 6.06, 'Nem pensar.'],
     [6.54, 8.25, 'Ele aperta o microfone e fala:'], [8.69, 11.47, 'abasteci trezentos litros a seis e dezenove.'], [12.04, 13.03, 'O Diário preenche tudo.'],
     [13.24, 15.44, 'Ele só confere e salva.'], [15.91, 16.98, 'Fala que o Diário anota.'], [17.43, 18.34, 'Comenta APP.']],
 html='''
<div class="abs tag" id="h0" style="top:230px">Zé no posto</div>
<div class="abs big" id="h1" style="top:1000px;font-size:150px">Mão preta<br>de <span class="yel">graxa</span></div>
<div class="abs big" id="h2" style="top:1000px;font-size:150px">Digitar?<br><span class="red">Nem pensar</span></div>
<div class="abs ph" id="ph" style="left:220px;top:190px;width:640px;height:1200px"><img id="s1" src="telas/01-inicio-ia.png" style="position:absolute;left:0;top:0;width:100%;opacity:0"><img id="s2" src="telas/02-ouvindo.png" style="position:absolute;left:0;top:0;width:100%;opacity:0"><img id="s3" src="telas/03-form-preenchido.png" style="position:absolute;left:0;top:-180px;width:100%;opacity:0"></div>
<div class="abs" id="hl" style="width:280px;height:136px;border:8px solid #f2b705;border-radius:26px;left:255px;top:942px"></div>''',
 anim='''
 vis('#h0',0,3.5);pop('#h0',0,.9,X);vis('#h1',2.04,3.5);pop('#h1',2.04,.8);vis('#h2',3.9,6.1);pop('#h2',3.9,.8);
 vis('#ph',6.54,15.6);pop('#ph',6.54,.92);
 $('#s1').style.opacity=t<8.69?1:0;$('#s2').style.opacity=(t>=8.69&&t<12.04)?1:0;$('#s3').style.opacity=t>=12.04?1:0;
 vis('#hl',7.2,8.6);$('#hl').style.left='255px';$('#hl').style.top='942px';
 if(t>13.24&&t<15.6){$('#hl').style.opacity=1;$('#hl').style.left='452px';$('#hl').style.top='1200px';$('#hl').style.width='376px'}else{$('#hl').style.width='280px'}''')

# ---------------- R3a Zé "frete compensa?" parte 1 (IA, guardar) ----------------
V['r3a'] = dict(TOT=16.3, ft=[0, 12.6], end=dict(a=12.6), endtxt=AB, ze=[[0, 3.65, 'calm'], [11.3, 12.4, 'worried', 0, .9]],
 ph=[[0, 3.69, 'Ofereceram pro Zé seis mil reais por mil km.'], [4.09, 5.27, 'Só que ele volta vazio.'], [5.95, 6.15, 'A:'], [6.69, 7.71, 'aceita o frete.'],
     [8.35, 8.61, 'B:'], [9.02, 10.69, 'recusa e espera um melhor.'], [11.35, 12.26, 'O que o Zé faz?'], [12.67, 14.04, 'Comenta A ou B.'], [14.4, 15.78, 'Amanhã a gente vê a conta.']],
 html='''
<div class="abs tag" id="h0" style="top:230px">Proposta pro Zé</div>
<div class="abs cm by" id="c1" style="top:1000px"><div class="l">Frete<br>1.000 km</div><div class="v yel">R$ 6.000</div></div>
<div class="abs chip r" id="c2" style="top:420px">Mas volta vazio</div>
<div class="abs cm by" id="a" style="top:620px"><div class="l"><span class="yel" style="font-size:110px">A</span></div><div class="v" style="font-size:90px">Aceita o frete</div></div>
<div class="abs cm" id="b" style="top:900px;border:5px solid #c9c5ba"><div class="l"><span style="font-size:110px;color:#f4f3ee">B</span></div><div class="v" style="font-size:80px;white-space:normal;text-align:right">Recusa e espera<br>um melhor</div></div>
<div class="abs big" id="q" style="top:1000px;font-size:150px">O que o<br>Zé <span class="yel">faz?</span></div>''',
 anim='''
 vis('#h0',0,3.9);pop('#h0',0,.9,X);vis('#c1',0.6,3.9);pop('#c1',0.6,.9);
 vis('#c2',4.09,11.2);pop('#c2',4.09,.7,X);vis('#a',5.95,11.2);pop('#a',5.95,.9);vis('#b',8.35,11.2);pop('#b',8.35,.9);
 vis('#q',11.35,12.5);pop('#q',11.35,.8);''')

# ---------------- R3b resposta: pergunta pro Diário (IA, guardar) ----------------
V['r3b'] = dict(TOT=20.4, ft=[0, 0], end=dict(a=18.75), endtxt=COMENTA | dict(el='Pergunte pro<br>seu <span class="yel">Diário</span>'), ze=[],
 ph=[[0, 1.57, 'O Zé perguntou pro Diário:'], [1.99, 3.27, 'esse frete compensa?'], [3.83, 5.42, 'O Diário olhou os números dele:'],
     [5.94, 8.68, 'com a volta vazia são dois mil km.'], [9.09, 13.12, 'A três e cinquenta e três por km, custa sete mil e sessenta.'],
     [13.59, 15.87, 'Ele perderia mil e sessenta reais.'], [16.35, 18.42, 'Pergunte pro seu Diário antes de aceitar.'], [18.82, 19.93, 'Comenta APP.']],
 html='''
<div class="abs tag" id="pq" style="top:120px;font-size:44px">"Esse frete compensa? Volto vazio"</div>
<div class="abs ph" id="ph" style="left:220px;top:190px;width:640px;height:1200px"><img id="c1" src="telas/04-chat-vazio.png" style="position:absolute;left:0;top:0;width:100%;opacity:0"><img id="c2" src="telas/06-chat-frete.png" style="position:absolute;left:0;top:0;width:100%;opacity:0"></div>
<div class="abs big" id="fim" style="top:700px;font-size:140px">Pergunte<br><span class="yel">antes</span> de<br>aceitar</div>''',
 anim='''
 vis('#ph',0,16.2);pop('#ph',0,.95);vis('#fim',16.35,18.7);pop('#fim',16.35,.8);vis('#pq',0,16.2);pop('#pq',0,.9,X);
 $('#c1').style.opacity=t<3.83?1:0;$('#c2').style.opacity=t>=3.83?1:0;''')

def build(k):
    s = V[k]
    et = s['endtxt']
    h = (BASE.replace('%%ZE%%', ZE).replace('%%HTML%%', s['html']).replace('%%ANIM%%', s['anim'])
         .replace('%%TOT%%', str(s['TOT'])).replace('%%PH%%', json.dumps(s['ph'], ensure_ascii=False))
         .replace('%%ZEV%%', json.dumps(s['ze'])).replace('%%END%%', json.dumps(s['end'])).replace('%%FT%%', json.dumps(s['ft']))
         .replace('%%EL%%', et['el']).replace('%%EP%%', et['ep']).replace('%%ES%%', et['es']))
    (here / f'index-{k}.html').write_text(h)

for k in (sys.argv[1:] or V):
    build(k)
print('ok', list(sys.argv[1:] or V))
