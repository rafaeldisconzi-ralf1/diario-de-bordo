import subprocess, os
css = """
@font-face{font-family:BC;src:url(barlow-condensed-latin-800-normal.woff2)}
@font-face{font-family:B;font-weight:600;src:url(barlow-latin-600-normal.woff2)}
@font-face{font-family:B;font-weight:800;src:url(barlow-latin-800-normal.woff2)}
*{margin:0;box-sizing:border-box}
body{width:1080px;height:1350px;background:#16181b;color:#f4f3ee;font-family:B;font-weight:600;position:relative;overflow:hidden}
.road{position:absolute;left:0;right:0;bottom:0;height:70px;background:#22252a}
.road i{position:absolute;top:31px;height:8px;width:110px;background:#f2b705}
.tag{display:inline-block;background:#f2b705;color:#16181b;font-family:BC;font-size:44px;padding:8px 22px;letter-spacing:1px}
h1{font-family:BC;font-size:132px;line-height:.95;text-transform:uppercase}
h2{font-family:BC;font-size:96px;line-height:.98;text-transform:uppercase}
.y{color:#f2b705}.g{color:#5fd39a}
p{font-size:44px;line-height:1.3}
.pad{position:absolute;left:80px;right:80px}
.num{position:absolute;right:60px;top:60px;font-family:BC;font-size:36px;color:#6b6f76}
.phone{position:absolute;left:50%;transform:translateX(-50%);width:560px;height:820px;border-radius:56px;background:#22252a;padding:18px;bottom:110px}
.phone div{width:100%;height:100%;border-radius:40px;overflow:hidden;background-size:100% auto;background-repeat:no-repeat}
li{font-size:50px;list-style:none;padding:14px 0;border-bottom:2px solid #2c3036;display:flex;justify-content:space-between}
"""
road = '<div class="road">' + ''.join(f'<i style="left:{x}px"></i>' for x in range(40,1080,200)) + '</div>'
slides = [
 """<div class="pad" style="top:110px"><span class="tag">CAMINHONEIRO</span></div>
 <div class="pad" style="top:260px"><h1>Você sabe<br>quanto <span class="y">sobrou</span><br>da sua última<br>viagem?</h1></div>
 <div class="pad" style="top:960px"><p>Não o frete. O que <b style="font-weight:800">ficou no bolso</b>.</p></div>
 <div class="pad" style="top:1130px;text-align:right"><p class="y" style="font-weight:800">Arrasta pro lado →</p></div>""",
 """<div class="pad" style="top:110px"><h2>O frete entra.<br><span class="y">Mas olha o que sai:</span></h2></div>
 <ul class="pad" style="top:420px;padding:0">
 <li><span>Diesel</span><span class="y">−</span></li><li><span>Pedágio</span><span class="y">−</span></li>
 <li><span>Comida</span><span class="y">−</span></li><li><span>Borracharia</span><span class="y">−</span></li>
 <li><span>Comissão do motorista</span><span class="y">−</span></li></ul>
 <div class="pad" style="top:1040px"><p>Sem anotar, no fim do mês ninguém sabe<br>se ganhou ou perdeu dinheiro.</p></div>""",
 """<div class="pad" style="top:90px"><h2>Lance tudo<br><span class="y">no celular</span></h2>
 <p style="margin-top:20px">Abasteceu, gastou ou ficou parado? Um toque.</p></div>
 <div class="phone" style="height:780px"><div style="background-image:url(01-inicio.png)"></div></div>""",
 """<div class="pad" style="top:90px"><h2>Chegou?<br><span class="g">Veja o que sobrou</span></h2>
 <p style="margin-top:20px">Frete, diárias, diesel, gastos e comissão. Tudo somado.</p></div>
 <div class="phone" style="height:780px"><div style="background-image:url(07-sobrou.png);background-position:0 -215px"></div></div>""",
 """<div class="pad" style="top:110px"><span class="tag">DIÁRIO DE BORDO</span></div>
 <div class="pad" style="top:250px"><h1>Menos de<br><span class="y">R$ 1 por dia</span></h1></div>
 <ul class="pad" style="top:560px;padding:0">
 <li><span>R$ 24,90 por mês</span><span class="y">✓</span></li>
 <li><span>Pix ou cartão</span><span class="y">✓</span></li>
 <li><span>7 dias de garantia</span><span class="y">✓</span></li>
 <li><span>Simples, botões grandes</span><span class="y">✓</span></li></ul>
 <div class="pad" style="top:1080px"><div style="background:#f2b705;color:#16181b;font-family:BC;font-size:64px;text-align:center;padding:22px;border-radius:16px">TOQUE NO LINK DA BIO</div></div>""",
]
for i,s in enumerate(slides,1):
    html=f'<html><head><meta charset="utf-8"><style>{css}</style></head><body><div class="num">{i}/5</div>{s}{road}</body></html>'
    open(f's{i}.html','w').write(html)
    subprocess.run(['google-chrome','--headless','--no-sandbox','--disable-gpu','--hide-scrollbars','--window-size=1080,1350','--virtual-time-budget=3000',f'--screenshot=slide-{i}.png',f'file://{os.getcwd()}/s{i}.html'],stderr=subprocess.DEVNULL)
from PIL import Image
ims=[Image.open(f'slide-{i}.png').convert('RGB').resize((432,540)) for i in range(1,6)]
c=Image.new('RGB',(432*5+40,540),'white')
for i,im in enumerate(ims): c.paste(im,(i*442,0))
c.save('contato.png')
