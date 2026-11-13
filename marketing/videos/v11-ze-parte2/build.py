# Parte 2 do Zé: gera index.html (render(t) quadro a quadro) e cues.json (efeitos).
# Estilo novo: uma cena a cada 2-3 s, legenda pequena no alto, câmera que se mexe.
import json, numpy as np
from ze_svg import ze_svg
W = json.load(open('words.json'))
db = np.array(json.load(open('env.json'))['db']); mx = db.max()
FPS = 30; TOT = 59.6
def ws(i): return W[i]['start']
def we(i): return W[i]['end']
mouth = ''
for f in range(int(TOT*FPS)+2):
    t = f/FPS; a = int(max(0, (t-.02)*100)); b = int((t+.02)*100)+1
    v = db[a:b].mean() if a < len(db) else -99
    mouth += '2' if v > mx-15 else ('1' if v > mx-27 else '0')

def truck(load='cheia', cab='#f2b705'):
    trl = {'cheia': '<rect x="10" y="18" width="172" height="84" rx="8" fill="#e8e3d6"/><rect x="10" y="62" width="172" height="10" fill="#f2b705" opacity=".85"/>',
           'vazia': '<rect x="10" y="74" width="172" height="12" rx="4" fill="#5a6370"/><rect x="10" y="18" width="172" height="84" rx="8" fill="none" stroke="#8a8f98" stroke-width="4" stroke-dasharray="14 10"/>'}[load]
    return f'''<svg viewBox="0 0 300 140" xmlns="http://www.w3.org/2000/svg">{trl}
<path d="M188 44 L242 44 L278 80 L284 102 L188 102Z" fill="{cab}"/><path d="M226 52 L248 52 L266 78 L226 78Z" fill="#2b4553"/><rect x="186" y="98" width="100" height="8" fill="#16181b"/>
<circle cx="280" cy="92" r="6" fill="#fff6c8"/>
<g fill="#16181b"><circle cx="48" cy="108" r="17"/><circle cx="88" cy="108" r="17"/><circle cx="126" cy="108" r="17"/><circle cx="216" cy="108" r="17"/><circle cx="256" cy="108" r="17"/></g>
<g fill="#8a8f98"><circle cx="48" cy="108" r="7"/><circle cx="88" cy="108" r="7"/><circle cx="126" cy="108" r="7"/><circle cx="216" cy="108" r="7"/><circle cx="256" cy="108" r="7"/></g></svg>'''

def small_truck(color, w):  # caminhão toco/truck genérico
    return f'''<svg viewBox="0 0 220 140" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="30" width="{w}" height="72" rx="8" fill="#e8e3d6"/>
<path d="M{w+16} 44 L{w+60} 44 L{w+86} 78 L{w+90} 102 L{w+16} 102Z" fill="{color}"/><path d="M{w+48} 52 L{w+64} 52 L{w+78} 78 L{w+48} 78Z" fill="#2b4553"/>
<g fill="#16181b"><circle cx="44" cy="108" r="17"/><circle cx="{w+60}" cy="108" r="17"/></g><g fill="#8a8f98"><circle cx="44" cy="108" r="7"/><circle cx="{w+60}" cy="108" r="7"/></g></svg>'''

PUMP = '''<svg viewBox="0 0 220 330" xmlns="http://www.w3.org/2000/svg"><rect x="20" y="20" width="140" height="290" rx="18" fill="#f4f3ee"/><rect x="20" y="20" width="140" height="44" rx="18" fill="#f2b705"/><rect x="20" y="44" width="140" height="20" fill="#f2b705"/>
<rect x="40" y="86" width="100" height="70" rx="8" fill="#16181b"/><rect x="40" y="176" width="100" height="14" rx="4" fill="#c9c5ba"/><rect x="40" y="200" width="100" height="14" rx="4" fill="#c9c5ba"/>
<rect x="8" y="300" width="164" height="22" rx="8" fill="#8a8f98"/><path d="M160 90 L190 90 Q206 90 206 108 L206 230 Q206 250 188 250 Q174 250 174 236 L174 120 L160 120Z" fill="#16181b"/></svg>'''
TOLL = '''<svg viewBox="0 0 600 420" xmlns="http://www.w3.org/2000/svg"><rect x="40" y="60" width="520" height="40" fill="#f2b705"/><rect x="40" y="60" width="520" height="40" fill="url(#st)"/>
<defs><pattern id="st" width="60" height="40" patternUnits="userSpaceOnUse"><path d="M0 40 L30 0 L60 0 L30 40Z" fill="#16181b"/></pattern></defs>
<rect x="60" y="100" width="40" height="300" fill="#c9c5ba"/><rect x="500" y="100" width="40" height="300" fill="#c9c5ba"/>
<rect x="390" y="190" width="110" height="210" rx="10" fill="#f4f3ee"/><rect x="408" y="212" width="74" height="54" rx="6" fill="#2b4553"/><circle cx="445" cy="300" r="14" fill="#5fd39a" id="tollight"/>
<g id="bar" style="transform-origin:390px 330px"><rect x="110" y="320" width="280" height="22" rx="10" fill="#f4f3ee"/><rect x="150" y="320" width="40" height="22" fill="#e04b3a"/><rect x="230" y="320" width="40" height="22" fill="#e04b3a"/><rect x="310" y="320" width="40" height="22" fill="#e04b3a"/></g></svg>'''
CLOCK = '''<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><circle cx="100" cy="100" r="84" fill="#f4f3ee" stroke="#16181b" stroke-width="10"/><circle cx="100" cy="100" r="7" fill="#16181b"/>
<path class="hand" d="M100 100 L100 40" stroke="#16181b" stroke-width="10" stroke-linecap="round" style="transform-origin:100px 100px"/><path d="M100 100 L140 118" stroke="#f2b705" stroke-width="10" stroke-linecap="round"/></svg>'''
COIN = '<svg viewBox="0 0 200 200"><circle cx="100" cy="100" r="90" fill="#f2b705"/><circle cx="100" cy="100" r="70" fill="none" stroke="#c99400" stroke-width="10"/><text x="100" y="128" text-anchor="middle" font-family="BC" font-weight="800" font-size="90" fill="#16181b">R$</text></svg>'

def bubbles():
    out = ''
    pos = [(80,520,'A'),(560,470,'A'),(250,700,'A'),(640,760,'A'),(110,930,'A'),(520,1010,'B'),(330,1180,'A'),(700,1220,'A'),(140,1260,'A')]
    for k,(x,y,l) in enumerate(pos):
        out += f'<div class="bub" data-k="{k}" style="left:{x}px;top:{y}px"><div class="av"></div><div class="bl">{l}</div></div>'
    return out

def receipt(rid, rows, sobra, color):
    r = ''.join(f'<div class="rr" data-r="{i}"><span>{a}</span><b class="{c}">{v}</b></div>' for i,(a,v,c) in enumerate(rows))
    return f'''<div class="rcpt" id="{rid}"><div class="rh">A CONTA · FRETE {rid[-1].upper()}</div>{r}
<div class="rr tot" data-r="{len(rows)}"><span>SOBRA</span><b style="color:{color}">{sobra}</b></div></div>'''

caps_kw = {3,4,6,7,11,17,22,29,31,36,39,47,48,51,53,54,55,56,62,73,75,76,77,79,82,86,97,98,99,101,119,133,135,137,138,143}

HTML = r'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>
@font-face{font-family:B;src:url(fonts/barlow-latin-700-normal.woff2);font-weight:700}
@font-face{font-family:BC;src:url(fonts/barlow-condensed-latin-800-normal.woff2);font-weight:800}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#14202e;font-family:B;color:#f4f3ee}
#world{position:absolute;inset:0;transform-origin:50% 45%}
#sky{position:absolute;inset:0}
#sun{position:absolute;width:260px;height:260px;border-radius:50%;left:720px;top:980px}
.hl{position:absolute;left:0;width:4320px;height:420px}
#ground{position:absolute;left:0;right:0;top:1560px;bottom:0;background:#101d22}
#road{position:absolute;left:0;right:0;top:1300px;height:300px;background:#2a2f36;opacity:0}
#road:before{content:'';position:absolute;left:0;right:0;top:142px;height:12px;background:repeating-linear-gradient(90deg,#f2b705 0 80px,transparent 80px 160px)}
.sc{position:absolute;inset:0;opacity:0}
.abs{position:absolute}
.box{background:#16181b;border-radius:36px;box-shadow:0 18px 0 rgba(0,0,0,.3)}
.yel{color:#f2b705}.grn{color:#5fd39a}.red{color:#ff7a66}
.big{font:800 150px/.95 BC;text-transform:uppercase;text-align:center}
.mid{font:800 100px/1 BC;text-transform:uppercase;white-space:nowrap}
.sm{font:700 42px/1.1 B;text-transform:uppercase;letter-spacing:1px}
.badge{flex-shrink:0;width:130px;height:130px;border-radius:30px;background:#f2b705;color:#16181b;font:800 118px/1 BC;display:flex;align-items:center;justify-content:center;padding-top:8px}
.pill{display:inline-block;background:#f2b705;color:#16181b;font:800 84px/1 BC;text-transform:uppercase;padding:22px 48px 12px;border-radius:999px;box-shadow:0 14px 0 rgba(0,0,0,.3);white-space:nowrap}
.chip{display:inline-block;background:#16181b;color:#f4f3ee;font:700 38px B;text-transform:uppercase;letter-spacing:1px;padding:14px 30px 10px;border-radius:999px}
#wm{position:absolute;font:700 38px B;color:#fff;opacity:.8;letter-spacing:1px;text-shadow:0 2px 6px rgba(0,0,0,.5);z-index:60;top:150px}
#ex{position:absolute;left:0;right:0;top:1500px;text-align:center;font:700 30px B;color:#c9c5ba;letter-spacing:2px;z-index:55;text-shadow:0 2px 6px rgba(0,0,0,.6)}
#subs{position:absolute;left:70px;right:70px;top:226px;text-align:center;z-index:58;font:700 58px/1.3 B;text-shadow:0 3px 10px rgba(0,0,0,.75)}
#subs .w{display:inline-block;margin:0 9px;opacity:0;border:4px solid transparent;border-radius:8px;padding:0 6px}
#subs .w.k.on{border-color:#f2b705;color:#fff}
#ze{position:absolute;width:560px;height:728px;z-index:20;opacity:0;transform-origin:50% 90%}
#ze svg{width:100%;height:100%}
.bub{position:absolute;display:flex;align-items:center;gap:18px;background:#f4f3ee;color:#16181b;border-radius:40px;padding:18px 34px 18px 18px;box-shadow:0 12px 0 rgba(0,0,0,.25);opacity:0}
.bub .av{width:76px;height:76px;border-radius:50%;background:#8a8f98}
.bub .bl{font:800 96px/1 BC}
.rcpt{position:absolute;left:150px;top:470px;width:780px;background:#f4f3ee;color:#16181b;border-radius:18px;padding:40px 50px 50px;box-shadow:0 22px 0 rgba(0,0,0,.3)}
.rcpt:after{content:'';position:absolute;left:0;right:0;bottom:-22px;height:24px;background:radial-gradient(circle at 20px -4px,transparent 18px,#f4f3ee 19px) 0 0/40px 24px repeat-x}
.rh{font:700 38px B;letter-spacing:3px;color:#5a6370;border-bottom:4px dashed #c9c5ba;padding-bottom:18px;margin-bottom:12px}
.rr{display:flex;justify-content:space-between;align-items:baseline;font:700 46px/1.7 B;text-transform:uppercase;opacity:0}
.rr b{font:800 76px/1.2 BC}.rr .neg{color:#c0392b}.rr .pos{color:#16181b}
.rr.tot{border-top:6px solid #16181b;margin-top:14px;padding-top:10px}.rr.tot span{font:800 70px BC}.rr.tot b{font-size:120px}
.phone{position:absolute;width:540px;height:1060px;left:270px;top:420px;border-radius:70px;background:#0d0f12;padding:26px;box-shadow:0 30px 0 rgba(0,0,0,.35)}
.scr{width:100%;height:100%;border-radius:48px;background:#16181b;overflow:hidden;position:relative}
.ah{background:#f2b705;color:#16181b;padding:56px 34px 22px;font:800 52px/1 BC;text-transform:uppercase}
.ah small{display:block;font:700 26px B;letter-spacing:1px;margin-top:8px}
.li{display:flex;justify-content:space-between;align-items:center;margin:20px 26px 0;padding:22px 26px;background:#22252a;border-radius:22px;font:700 34px B;text-transform:uppercase;opacity:0}
.li b{font:800 52px BC}
.bar{position:absolute;bottom:0;width:250px;border-radius:24px 24px 0 0}
</style></head><body>
<div id="world">
<div id="sky"></div><div id="sun"></div>
<svg class="hl" id="h1" style="top:1080px" viewBox="0 0 4320 420"><defs><pattern id="p1" width="720" height="420" patternUnits="userSpaceOnUse"><path d="M0 220 C120 120 260 120 360 210 C460 300 600 290 720 220 L720 420 L0 420Z" fill="#26404a"/></pattern></defs><rect width="4320" height="420" fill="url(#p1)"/></svg>
<svg class="hl" id="h2" style="top:1190px" viewBox="0 0 4320 420"><defs><pattern id="p2" width="540" height="420" patternUnits="userSpaceOnUse"><path d="M0 170 C90 100 190 100 270 160 C350 220 450 220 540 170 L540 420 L0 420Z" fill="#1a2c33"/></pattern></defs><rect width="4320" height="420" fill="url(#p2)"/></svg>
<div id="road"></div><div id="ground"></div>

<!-- 0 gancho -->
<div class="sc" id="s0">
 <div class="abs" style="left:0;right:0;top:420px;text-align:center"><span class="chip">Parte 2 · a conta</span></div>
 <div class="abs box" id="h9" style="left:70px;top:560px;width:440px;height:420px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px"><div class="badge">B</div><div class="mid" style="font-size:118px">R$ 9.000</div><div class="sm" id="h9t" style="color:#ff7a66;opacity:0">▼ sobra menos</div></div>
 <div class="abs box" id="h8" style="left:570px;top:560px;width:440px;height:420px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px"><div class="badge">A</div><div class="mid" style="font-size:118px">R$ 8.000</div><div class="sm grn" id="h8t" style="opacity:0">▲ sobra mais</div></div>
</div>
<!-- 1 Zé e propostas -->
<div class="sc" id="s1">
 <div class="abs box" id="pa" style="left:560px;top:470px;width:440px;padding:26px 30px;display:flex;align-items:center;gap:24px"><div class="badge" style="width:96px;height:96px;font-size:86px">A</div><div class="sm">Proposta<br><span class="yel">R$ 8.000</span></div></div>
 <div class="abs box" id="pb" style="left:560px;top:690px;width:440px;padding:26px 30px;display:flex;align-items:center;gap:24px"><div class="badge" style="width:96px;height:96px;font-size:86px">B</div><div class="sm">Proposta<br><span class="yel">R$ 9.000</span></div></div>
</div>
<!-- 2 A: ida cheia, volta vazia -->
<div class="sc" id="s2">
 <div class="abs box" style="left:70px;top:430px;width:940px;padding:30px 40px;display:flex;align-items:center;gap:34px"><div class="badge">A</div><div><div class="mid" style="font-size:110px">R$ 8.000</div><div class="sm" style="color:#c9c5ba">ida cheia · <span class="yel">volta vazia</span></div></div></div>
 <div class="abs" id="t2a" style="top:1160px;width:620px">__TRUCK_CHEIA__</div>
 <div class="abs" id="t2b" style="top:1160px;width:620px;transform:scaleX(-1)">__TRUCK_VAZIA__</div>
 <div class="abs" id="l2a" style="left:0;right:0;top:930px;text-align:center"><span class="pill" style="font-size:70px">→ Ida · cheia</span></div>
 <div class="abs" id="l2b" style="left:0;right:0;top:930px;text-align:center"><span class="pill" style="font-size:70px;background:#8a8f98">← Volta · vazia</span></div>
</div>
<!-- 3 B: espera -->
<div class="sc" id="s3">
 <div class="abs box" style="left:70px;top:430px;width:940px;padding:30px 40px;display:flex;align-items:center;gap:34px"><div class="badge">B</div><div><div class="mid" style="font-size:110px">R$ 9.000</div><div class="sm" style="color:#c9c5ba">mas espera a carga da volta</div></div></div>
 <div class="abs" id="clk3" style="left:120px;top:780px;width:260px;height:260px">__CLOCK__</div>
 <div class="abs" style="left:430px;top:800px"><div class="mid" style="font-size:200px;line-height:1"><span id="dia3">DIA 1</span></div><div class="sm yel" style="font-size:52px">parado no pátio</div></div>
 <div class="abs" style="left:240px;top:1170px;width:620px">__TRUCK_VAZIA__</div>
</div>
<!-- 4 votos -->
<div class="sc" id="s4">__BUBBLES__
 <div class="abs" id="v4" style="left:0;right:0;top:820px;text-align:center"><span class="pill">A maioria votou A</span></div>
</div>
<!-- 5 a conta -->
<div class="sc" id="s5">
 <div class="abs" id="pap5" style="left:190px;top:460px;width:700px;height:900px;background:#f4f3ee;border-radius:18px;box-shadow:0 22px 0 rgba(0,0,0,.3);padding:60px">
  <div style="font:800 150px/1 BC;color:#16181b">A CONTA</div>
  <div style="margin-top:40px;height:10px;background:#c9c5ba;border-radius:5px"></div><div style="margin-top:50px;height:10px;width:80%;background:#c9c5ba;border-radius:5px"></div><div style="margin-top:50px;height:10px;width:60%;background:#c9c5ba;border-radius:5px"></div>
  <div id="pen5" style="position:absolute;right:60px;bottom:120px;width:40px;height:300px;background:#f2b705;border-radius:10px;transform:rotate(30deg)"><div style="position:absolute;bottom:-40px;left:0;border-left:20px solid transparent;border-right:20px solid transparent;border-top:44px solid #16181b"></div></div>
 </div>
</div>
<!-- 6 diesel A -->
<div class="sc" id="s6">
 <div class="abs" id="pump6" style="left:70px;top:560px;width:340px;height:510px">__PUMP__</div>
 <div class="abs" style="left:440px;top:560px"><div class="row" style="display:flex;gap:20px;align-items:center"><div class="badge" style="width:100px;height:100px;font-size:90px">A</div><div class="sm yel" style="font-size:50px">Diesel</div></div>
  <div class="sm" style="color:#c9c5ba;margin-top:20px;font-size:38px">ida cheia + volta vazia</div>
  <div class="mid" style="font-size:150px;margin-top:20px">R$ <span id="d6">0</span></div></div>
</div>
<!-- 7 pedágio A -->
<div class="sc" id="s7">
 <div class="abs" style="left:240px;top:760px;width:600px">__TOLL__</div>
 <div class="abs" style="left:0;right:0;top:470px;text-align:center"><div class="sm yel" style="font-size:56px">Pedágio</div><div class="mid" style="font-size:170px">− R$ 1.200</div></div>
</div>
<!-- 8 recibo A -->
<div class="sc" id="s8">__RCPT_A__</div>
<!-- 9 B cheio nos dois sentidos -->
<div class="sc" id="s9">
 <div class="abs box" style="left:70px;top:430px;width:940px;padding:30px 40px;display:flex;align-items:center;gap:34px"><div class="badge">B</div><div><div class="mid" style="font-size:76px">Cheia nos dois sentidos</div></div></div>
 <div class="abs" id="t9a" style="top:820px;width:520px">__TRUCK_CHEIA__</div>
 <div class="abs" id="t9b" style="top:1160px;width:620px;transform:scaleX(-1)">__TRUCK_CHEIA__</div>
 <div class="abs" style="left:90px;top:760px"><span class="chip">→ ida</span></div><div class="abs" style="right:90px;top:1100px"><span class="chip">volta ←</span></div>
</div>
<!-- 10 custos B -->
<div class="sc" id="s10">
 <div class="abs" style="left:70px;top:430px;display:flex;gap:20px;align-items:center"><div class="badge" style="width:100px;height:100px;font-size:90px">B</div><div class="sm yel" style="font-size:56px">Gastos</div></div>
 <div class="abs box c10" data-c="0" style="left:70px;top:590px;width:940px;padding:26px 40px;display:flex;align-items:center;justify-content:space-between"><div style="width:110px;height:150px">__PUMP__</div><div class="sm" style="flex:1;margin-left:30px">Mais diesel</div><div class="mid red">− 6.360</div></div>
 <div class="abs box c10" data-c="1" style="left:70px;top:820px;width:940px;padding:26px 40px;display:flex;align-items:center;justify-content:space-between"><div style="width:110px;height:110px;background:#f2b705;border-radius:20px;font:800 80px/110px BC;color:#16181b;text-align:center">$</div><div class="sm" style="flex:1;margin-left:30px">Mais pedágio</div><div class="mid red">− 1.200</div></div>
 <div class="abs box c10" data-c="2" style="left:70px;top:1050px;width:940px;padding:26px 40px;display:flex;align-items:center;justify-content:space-between"><div style="width:110px;height:110px">__CLOCK__</div><div class="sm" style="flex:1;margin-left:30px">2 dias parado</div><div class="mid red">− 600</div></div>
</div>
<!-- 11 recibo B -->
<div class="sc" id="s11">__RCPT_B__</div>
<!-- 12 comparação -->
<div class="sc" id="s12">
 <div class="abs" style="left:140px;top:600px;width:800px;height:520px">
  <div class="bar" id="bA" style="left:40px;background:#5fd39a"></div><div class="bar" id="bB" style="left:510px;background:#8a8f98"></div>
  <div class="abs mid" id="vA" style="left:40px;width:250px;text-align:center;font-size:84px">1.280</div><div class="abs mid" id="vB" style="left:510px;width:250px;text-align:center;font-size:84px">840</div>
 </div>
 <div class="abs" style="left:180px;top:1130px;width:250px;text-align:center"><div class="badge" style="margin:0 auto">A</div></div><div class="abs" style="left:650px;top:1130px;width:250px;text-align:center"><div class="badge" style="margin:0 auto">B</div></div>
 <div class="abs" id="rule12" style="left:70px;top:1290px;width:940px;background:#f2b705;color:#16181b;border-radius:28px;padding:22px 34px 14px;font:800 76px/1 BC;text-transform:uppercase;text-align:center;box-shadow:0 16px 0 rgba(0,0,0,.3)">Frete maior nem sempre sobra mais</div>
</div>
<!-- 13 cada caminhão -->
<div class="sc" id="s13">
 <div class="abs t13" data-k="0" style="left:40px;top:640px;width:330px">__T1__</div>
 <div class="abs t13" data-k="1" style="left:380px;top:860px;width:330px">__T2__</div>
 <div class="abs t13" data-k="2" style="left:180px;top:1110px;width:720px">__TRUCK_CHEIA__</div>
 <div class="abs" style="left:780px;top:600px;font:800 200px BC;color:#f2b705" id="q13">?</div>
 <div class="abs" style="left:0;right:0;top:470px;text-align:center"><span class="pill" style="font-size:72px">Cada caminhão, uma conta</span></div>
</div>
<!-- 14 Zé usa o app -->
<div class="sc" id="s14">
 <div class="abs" id="ic14" style="left:650px;top:520px;width:300px;height:300px;border-radius:66px;overflow:hidden;box-shadow:0 18px 0 rgba(0,0,0,.3)"><img src="icon-512.png" style="width:100%;height:100%"></div>
 <div class="abs" id="nm14" style="left:560px;top:860px;width:480px;text-align:center"><div class="mid" style="font-size:96px;line-height:.95">Diário<br><span class="yel">de Bordo</span></div></div>
</div>
<!-- 15 celular: lançamentos -->
<div class="sc" id="s15"><div class="phone" id="ph15"><div class="scr"><div class="ah">Viagem do Zé<small>frete B · exemplo</small></div>
 <div class="li" data-l="0"><span>Frete</span><b class="grn">+ 9.000</b></div>
 <div class="li" data-l="1"><span>Diesel</span><b class="red">− 6.360</b></div>
 <div class="li" data-l="2"><span>Pedágio</span><b class="red">− 1.200</b></div>
 <div class="li" data-l="3"><span>Diárias (2)</span><b class="red">− 600</b></div>
 <div id="tap15" style="position:absolute;width:90px;height:90px;border-radius:50%;background:rgba(242,183,5,.45);left:200px;top:330px"></div>
</div></div></div>
<!-- 16 sobrou -->
<div class="sc" id="s16"><div class="phone" id="ph16"><div class="scr" style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:20px">
 <div class="sm" style="color:#c9c5ba;font-size:44px">Sobrou</div><div class="mid grn" style="font-size:150px">R$ <span id="sb16">0</span></div><div class="sm" style="color:#c9c5ba;font-size:30px">nesta viagem</div>
 <div style="margin-top:40px;width:380px;height:20px;border-radius:10px;background:#22252a;overflow:hidden"><div id="pb16" style="height:100%;width:0;background:#5fd39a"></div></div>
</div></div></div>
<!-- 17 antes de aceitar -->
<div class="sc" id="s17">
 <div class="abs" style="left:560px;top:620px;width:450px"><div class="box" style="padding:30px;display:flex;align-items:center;gap:24px"><div class="badge" style="width:96px;height:96px;font-size:86px">A</div><div class="mid grn" style="font-size:80px">1.280</div><div id="ck17" style="font:800 90px BC;color:#5fd39a;opacity:0">✓</div></div>
  <div class="box" style="margin-top:30px;padding:30px;display:flex;align-items:center;gap:24px"><div class="badge" style="width:96px;height:96px;font-size:86px">B</div><div class="mid" style="font-size:80px;color:#c9c5ba">840</div></div></div>
 <div class="abs" id="t17" style="left:0;right:0;top:440px;text-align:center"><span class="pill" style="font-size:66px">Antes de aceitar, já sabe a conta</span></div>
</div>
<!-- 18 preço -->
<div class="sc" id="s18">
 <div class="abs" id="coin18" style="left:390px;top:470px;width:300px;height:300px">__COIN__</div>
 <div class="abs" style="left:0;right:0;top:830px;text-align:center"><div class="big" style="font-size:120px">Menos de</div><div class="big yel" style="font-size:230px">R$ 1</div><div class="big" style="font-size:120px">por dia</div></div>
</div>
<!-- 19 final -->
<div class="sc" id="s19">
 <div class="abs" style="left:390px;top:440px;width:300px;height:300px;border-radius:66px;overflow:hidden;box-shadow:0 18px 0 rgba(0,0,0,.3)"><img src="icon-512.png" style="width:100%;height:100%"></div>
 <div class="abs" style="left:0;right:0;top:780px;text-align:center"><div class="big" style="font-size:150px">Diário <span class="yel">de Bordo</span></div><div class="sm" style="color:#c9c5ba;margin-top:16px">frete · diesel · gastos · diárias</div></div>
 <div class="abs" id="cta19" style="left:0;right:0;top:1040px;text-align:center"><span class="pill">Toque no link do perfil</span></div>
 <div class="abs" id="t19" style="top:1240px;width:520px">__TRUCK_CHEIA__</div>
</div>
</div>
<div id="ze">__ZE__</div>
<div id="subs"></div><div id="wm">@appdiariodebordo</div><div id="ex">NÚMEROS DE EXEMPLO</div>
<script>
const TOT=__TOT__, WORDS=__WORDS__, MOUTH="__MOUTH__", KW=new Set(__KW__);
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const cl=x=>Math.max(0,Math.min(1,x)), eo=x=>1-Math.pow(1-cl(x),3), eio=x=>{x=cl(x);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2};
const back=x=>{x=cl(x);const c=1.6;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
const ws=i=>WORDS.find(w=>w.id==i).start, we=i=>WORDS.find(w=>w.id==i).end;
const fmt=n=>String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g,'.');
const CUT=__CUTS__;
const pop=(el,u,d=.35)=>{el.style.opacity=cl(u/.12);el.style.transform='scale('+(0.6+0.4*back(u/d))+')'};
// legenda: frases
const PH=[];(()=>{let g=[];WORDS.forEach(w=>{g.push(w);if(/[.,:?]$/.test(w.text)&&g.length>=3||/[.:?]$/.test(w.text)){PH.push(g);g=[]}});if(g.length)PH.push(g)})();
const cap=$('#subs');
function hex(c){return [1,3,5].map(i=>parseInt(c.substr(i,2),16))}
function mix(a,b,t){const A=hex(a),B=hex(b);return 'rgb('+A.map((v,i)=>Math.round(v+(B[i]-v)*t)).join(',')+')'}
let curPh=-1;
window.render=function(t){
 let si=0;while(si<CUT.length-1&&t>=CUT[si+1])si++;
 const u=t-CUT[si];
 $$('.sc').forEach((e,i)=>e.style.opacity=i==si?1:0);
 // câmera: empurrão no corte + zoom lento
 const k=1+0.06*(1-eo(u/.35))*(si>0?1:0)+0.012*u;
 $('#world').style.transform='scale('+k+') translateY('+(-6*u)+'px)';
 // céu: entardecer -> noite ao longo do vídeo, dias rápidos na cena 3
 let night=cl((t-20)/20);let sky=[mix('#20324a','#0f1826',night),mix('#3d5a73','#1b2c3d',night),mix('#d98a3a','#24384a',night)];
 if(si==3){const ph=(Math.sin(u*4.2)+1)/2;sky=[mix('#0b1220','#3b6c94',ph),mix('#14202e','#7fb0cf',ph),mix('#1d2f3d','#e8b25a',ph)]}
 $('#sky').style.background='linear-gradient(180deg,'+sky[0]+' 0%,'+sky[1]+' 55%,'+sky[2]+' 80%)';
 const sn=$('#sun');sn.style.background=mix('#f2b705','#e8ecef',night);sn.style.opacity=[3,12,15,16,18,19].includes(si)?0:.85;sn.style.top=(980+night*40)+'px';sn.style.left=(760-t*2)+'px';
 $('#h1').style.transform='translateX('+(-(t*20)%720)+'px)';$('#h2').style.transform='translateX('+(-(t*40)%540)+'px)';
 $('#road').style.opacity=[2,9,13,19].includes(si)?1:0;
 const wm=$('#wm');const pos=Math.floor(t/8)%2;wm.style.left=pos?'auto':'48px';wm.style.right=pos?'48px':'auto';
 // Zé
 const ZE={1:[60,680,1.0],14:[20,720,1.05],17:[-20,760,1.0]};const ze=$('#ze');
 if(ZE[si]){const [x,y,s]=ZE[si];ze.style.opacity=1;ze.style.left=x+'px';ze.style.top=y+'px';
  const f=Math.min(MOUTH.length-1,Math.round(t*30)),m=+MOUTH[f];
  let ex=si==1?'calm':'happy';['calm','worried','shock','happy'].forEach(q=>{$('#ex_'+q).style.display=q==ex?'':'none';$('#mo_'+q).style.display=(q==ex&&m==0)?'':'none'});
  $('#sp1').style.display=m==1?'':'none';$('#sp2').style.display=m==2?'':'none';
  $('#blink').style.display=(u%2.7<.12&&u>.5)?'':'none';
  ze.style.transform='translateY('+((1-eo(u/.35))*160+Math.sin(t*2.3)*5)+'px) rotate('+Math.sin(t*1.4)*1.2+'deg) scale('+s+')';
 } else ze.style.opacity=0;
 // cenas
 if(si==0){pop($('#h9'),u+.4);pop($('#h8'),u+.3);$('#h9t').style.opacity=cl((t-ws(6))/.2);$('#h8t').style.opacity=cl((t-ws(10))/.2);
  $('#h9').style.transform+=' translateY('+(cl((t-ws(6))/.3)*30)+'px)';$('#h8').style.transform+=' translateY('+(-cl((t-ws(10))/.3)*30)+'px)'}
 if(si==1){pop($('#pa'),t-ws(16));pop($('#pb'),t-ws(17))}
 if(si==2){const a=t-ws(19),b=t-ws(21);$('#t2a').style.left=(-640+eio(a/1.3)*1200)+'px';$('#t2a').style.opacity=b<0?1:0;$('#l2a').style.opacity=b<0&&a>0?1:0;
  $('#t2b').style.left=(1100-eio(b/1.6)*1200)+'px';$('#t2b').style.opacity=b>=0?1:0;$('#l2b').style.opacity=b>=0?1:0}
 if(si==3){$('#clk3 .hand').style.transform='rotate('+u*400+'deg)';$('#dia3').textContent=t<ws(28)+.4?'DIA 1':'DIA 2'}
 if(si==4){$$('.bub').forEach(e=>{const kk=+e.dataset.k;pop(e,u-kk*.11,.3)});pop($('#v4'),t-ws(32))}
 if(si==5){const p=$('#pap5');p.style.transform='translateY('+(1-eo(u/.4))*900+'px) rotate('+(-2+2*eo(u/.4))+'deg)';$('#pen5').style.transform='rotate('+(30+Math.sin(u*14)*6)+'deg)'}
 if(si==6){$('#d6').textContent=fmt(5520*eio((t-ws(44))/(we(47)-ws(44))));$('#pump6').style.transform='rotate('+Math.sin(u*30)*(u<2.5?1:0)+'deg)'}
 if(si==7){$('#bar').style.transform='rotate('+(-75*eo((u-1.0)/.5))+'deg)';$('#tollight').setAttribute('fill',u>1?'#5fd39a':'#e04b3a')}
 if(si==8||si==11){const id=si==8?'#rcptA':'#rcptB';const rc=$(id);rc.style.transform='translateY('+(1-eo(u/.35))*700+'px)';rc.querySelectorAll('.rr').forEach(r=>{const i=+r.dataset.r;const tot=r.classList.contains('tot');const st=tot?(si==8?ws(53):ws(75))-CUT[si]:.25+i*.22;const e=cl((u-st)/.2);r.style.opacity=e;r.style.transform=tot?'scale('+(0.7+0.3*back((u-st)/.35))+')':'translateX('+(1-e)*60+'px)'})}
 if(si==9){$('#t9a').style.left=(-560+(u/3.3)*1650)+'px';$('#t9b').style.left=(1100-(u/3.3)*1750)+'px'}
 if(si==10){$$('.c10').forEach(e=>{const c=+e.dataset.c;const st=[ws(67),ws(69),ws(72)][c]-.1;const q=cl((t-st)/.25);e.style.opacity=q;e.style.transform='translateX('+(1-eo((t-st)/.3))*-200+'px)'});$$('#s10 .hand').forEach(h=>h.style.transform='rotate('+u*300+'deg)')}
 if(si==12){const g=eo(u/.8);$('#bA').style.height=(420*g)+'px';$('#bB').style.height=(276*g)+'px';$('#vA').style.top=(520-420*g-96)+'px';$('#vB').style.top=(520-276*g-96)+'px';pop($('#rule12'),t-ws(81)+.3)}
 if(si==13){$$('.t13').forEach(e=>{const k=+e.dataset.k;const q=eo((u-k*.25)/.4);e.style.opacity=q;e.style.transform='translateX('+(1-q)*(k%2?400:-400)+'px)'});$('#q13').style.transform='rotate('+Math.sin(u*5)*10+'deg)'}
 if(si==14){pop($('#ic14'),t-ws(97)+.2);$('#nm14').style.opacity=cl((t-ws(98))/.2)}
 if(si==15){const ph=$('#ph15');ph.style.transform='translateY('+(1-eo(u/.4))*900+'px)';const st=[ws(105),ws(107),ws(109),ws(112)];$$('#s15 .li').forEach(e=>{const l=+e.dataset.l;const q=cl((t-st[l]+.1)/.2);e.style.opacity=q;e.style.transform='translateY('+(1-q)*30+'px)'});
  let li=0;st.forEach((s,i)=>{if(t>=s-.15)li=i});const tp=$('#tap15');tp.style.top=(150+li*124+60)+'px';tp.style.left='380px';tp.style.opacity=((t-st[li]+.15)%10)<.35?.9:0}
 if(si==16){const q=eio((t-ws(118))/(we(119)-ws(118)+.3));$('#sb16').textContent=fmt(840*q);$('#pb16').style.width=(q*100)+'%';$('#ph16').style.transform='scale('+(1+0.04*back(cl((t-we(119))/.3))-0.04*cl((t-we(119))/.3)*0)+')'}
 if(si==17){$('#ck17').style.opacity=cl((t-ws(131))/.2);pop($('#t17'),t-ws(123))}
 if(si==18){pop($('#coin18'),u);$('#coin18').style.transform+=' rotateY('+u*180+'deg)'}
 if(si==19){$('#t19').style.left=(-560+(u/4)*1700)+'px';pop($('#cta19'),t-ws(141))}
 // legenda
 let pi=-1;PH.forEach((g,i)=>{if(t>=g[0].start-.05)pi=i});
 if(pi!=curPh){curPh=pi;cap.innerHTML=pi<0?'':PH[pi].map(w=>'<span class="w'+(KW.has(w.id)?' k':'')+'" data-i="'+w.id+'">'+w.text+'</span>').join(' ')}
 cap.querySelectorAll('.w').forEach(sp=>{const i=+sp.dataset.i;const s=ws(i);sp.style.opacity=t>=s-.03?1:0;if(t>=s)sp.classList.add('on');else sp.classList.remove('on')});
 const last=PH[pi];cap.style.opacity=last&&t>last[last.length-1].end+0.6?0:1;
};
window.render(0);
</script></body></html>'''

CUTS = [0, 3.6, 6.2, 8.8, 12.3, 14.0, 15.6, 19.3, 21.3, 23.7, 27.05, 30.65, 33.05, 36.0, 38.5, 41.3, 45.8, 49.15, 53.1, 55.5]
rA = receipt('rcptA', [('Frete','+ 8.000','pos'),('Diesel','− 5.520','neg'),('Pedágio','− 1.200','neg')], 'R$ 1.280', '#1f8a55')
rB = receipt('rcptB', [('Frete','+ 9.000','pos'),('Diesel','− 6.360','neg'),('Pedágio','− 1.200','neg'),('2 dias parado','− 600','neg')], 'R$ 840', '#b07d00')
HTML = (HTML.replace('__TRUCK_CHEIA__', truck('cheia')).replace('__TRUCK_VAZIA__', truck('vazia')).replace('__PUMP__', PUMP).replace('__TOLL__', TOLL)
        .replace('__CLOCK__', CLOCK).replace('__COIN__', COIN).replace('__BUBBLES__', bubbles()).replace('__RCPT_A__', rA).replace('__RCPT_B__', rB)
        .replace('__T1__', small_truck('#e04b3a', 110)).replace('__T2__', small_truck('#5fa8d3', 130)).replace('__ZE__', ze_svg())
        .replace('__TOT__', str(TOT)).replace('__WORDS__', json.dumps(W, ensure_ascii=False)).replace('__MOUTH__', mouth)
        .replace('__KW__', json.dumps(sorted(caps_kw))).replace('__CUTS__', json.dumps(CUTS)))
open('index.html', 'w').write(HTML)

cues = []
for c in CUTS[1:]: cues.append(dict(t=round(c, 3), k='whoosh'))
cues.append(dict(t=0.02, k='slam'))
cues += [dict(t=round(ws(16), 3), k='ring'), dict(t=round(ws(16), 3), k='pop'), dict(t=round(ws(17), 3), k='pop')]
cues += [dict(t=round(12.3+k*.11, 3), k='pop') for k in range(9)]
cues += [dict(t=round(ws(44)+k*.07, 3), k='tick') for k in range(int((we(47)-ws(44))/.07))]
cues.append(dict(t=round(19.3+1.0, 3), k='beep'))
for k in range(3): cues.append(dict(t=round(21.3+.25+k*.22, 3), k='tick'))
cues.append(dict(t=round(ws(53), 3), k='cash'))
for k in range(4): cues.append(dict(t=round(30.65+.25+k*.22, 3), k='tick'))
cues.append(dict(t=round(ws(75), 3), k='thud'))
for i in (67, 69, 72): cues.append(dict(t=round(ws(i)-.1, 3), k='pop'))
cues.append(dict(t=round(ws(81)-.3, 3), k='slam'))
for i in (105, 107, 109, 112): cues.append(dict(t=round(ws(i)-.1, 3), k='tap'))
cues.append(dict(t=round(we(119), 3), k='cash'))
cues.append(dict(t=round(ws(131), 3), k='ding'))
cues.append(dict(t=53.1, k='ding'))
json.dump(cues, open('cues.json', 'w'))
print('ok', len(HTML)//1024, 'KB', len(cues))
