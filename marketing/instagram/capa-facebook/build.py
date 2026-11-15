import sys; sys.path.insert(0,'../../videos/v15-ze-parte4')
from ze_svg import ze_svg
z=ze_svg().replace('id="ex_happy" style="display:none"','id="ex_happy"').replace('id="mo_happy" style="display:none"','id="mo_happy"')
html=f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:BC;src:url(fonts/barlow-condensed-latin-800-normal.woff2)}}
@font-face{{font-family:B;src:url(fonts/barlow-latin-700-normal.woff2)}}
html,body{{margin:0}}
#c{{width:1640px;height:856px;position:relative;overflow:hidden;background:#16181b}}
.sky{{position:absolute;inset:0;background:linear-gradient(#1d2733 0%,#2b3a4a 55%,#c98a3a 100%)}}
.sun{{position:absolute;left:250px;top:250px;width:280px;height:280px;border-radius:50%;background:#f2b705}}
.hills{{position:absolute;left:0;bottom:0;width:1640px;height:420px}}
#ze{{position:absolute;left:170px;top:190px;width:430px}}
.t{{position:absolute;left:610px;top:215px;width:560px;color:#f4f3ee}}
.t h1{{font:800 92px/0.95 BC;text-transform:uppercase;margin:0}}
.y{{color:#f2b705}} .g{{color:#5fd39a}}
.t p{{font:700 30px/1.25 B;margin:18px 0 0;color:#e8e4da}}
.pill{{display:inline-block;margin-top:22px;background:#f2b705;color:#16181b;font:800 42px/1 BC;text-transform:uppercase;padding:16px 26px 10px;border-radius:18px}}
.ph{{position:absolute;left:1185px;top:165px;width:240px;height:520px;border-radius:38px;background:#0d0e10;padding:12px;box-shadow:0 30px 60px rgba(0,0,0,.5)}}
.ph img{{width:100%;height:100%;object-fit:cover;object-position:top;border-radius:28px}}
</style></head><body><div id="c">
<div class="sky"></div><div class="sun"></div>
<svg class="hills" viewBox="0 0 1640 420" preserveAspectRatio="none"><path d="M0 220 Q300 120 620 210 T1240 190 T1640 170 V420 H0Z" fill="#26323d"/><path d="M0 300 Q400 220 820 300 T1640 270 V420 H0Z" fill="#1d252d"/><path d="M0 360 Q500 320 1000 360 T1640 350 V420 H0Z" fill="#16181b"/></svg>
<div id="ze">{z}</div>
<div class="t"><h1>Quanto <span class="y">sobrou</span><br>da sua viagem?</h1>
<p>Frete, diesel, gastos e diárias<br>anotados no celular.</p>
<div class="pill">Diário de Bordo</div></div>
<div class="ph"><img src="07-sobrou.png"></div>
</div></body></html>'''
open('index.html','w').write(html)
