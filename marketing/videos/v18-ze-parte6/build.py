# Zé Parte 6: cenas desenhadas (pátio, videochamada, estrada, relógio, A/B) + Zé narrando num círculo.
import json, numpy as np
from ze_svg import ze_svg
W=json.load(open('words.json'))
db=np.array(json.load(open('env.json'))['db']); mx=db.max()
FPS=30; TOT=27.0
mouth=''
for f in range(int(TOT*FPS)+2):
    t=f/FPS; a=int(max(0,(t-0.02)*100)); b=int((t+0.02)*100)+1
    v=db[a:b].mean() if a<len(db) else -99
    mouth+= '2' if v>mx-15 else ('1' if v>mx-27 else '0')

from art import DEFS, truck, hills, road, VIG
HAZ='<g class="haz"><circle cx="282" cy="76" r="10" fill="#ffb300"/><circle cx="282" cy="76" r="30" fill="#ffb300" opacity=".35" filter="url(#glow)"/><circle cx="12" cy="96" r="9" fill="#ffb300"/><circle cx="12" cy="96" r="28" fill="#ffb300" opacity=".35" filter="url(#glow)"/></g>'
GIRL='''<g id="girl" filter="url(#sh)">
<path d="M-118 -10 C-130 -120 130 -120 118 -10 L132 220 Q0 250 -132 220Z" fill="#3b2a22"/>
<path d="M-110 190 Q0 160 110 190 L150 330 L-150 330Z" fill="#ff8fa3"/><path d="M-60 180 Q0 230 60 180" stroke="#fff" stroke-width="10" fill="none"/>
<rect x="-26" y="120" width="52" height="60" rx="20" fill="#d9a07a"/>
<path d="M-84 20 C-84 -60 84 -60 84 20 C84 100 46 150 0 150 C-46 150 -84 100 -84 20Z" fill="#e8b48e"/>
<path d="M-92 30 C-100 -90 100 -90 92 30 C84 -10 60 -40 0 -36 C-40 -34 -80 -20 -92 30Z" fill="#3b2a22"/>
<path d="M-92 30 C-100 -40 -60 -70 -10 -64 C-40 -40 -60 -10 -70 24Z" fill="#4e382d"/>
<path d="M-20 -78 C20 -82 56 -66 70 -40" stroke="#6b4a3a" stroke-width="7" fill="none" stroke-linecap="round"/>
<ellipse cx="-30" cy="44" rx="10" ry="12" fill="#2a1f19"/><ellipse cx="30" cy="44" rx="10" ry="12" fill="#2a1f19"/>
<circle cx="-26" cy="40" r="4" fill="#fff"/><circle cx="34" cy="40" r="4" fill="#fff"/>
<path d="M-44 36 l-8 -6 M44 36 l8 -6" stroke="#2a1f19" stroke-width="4" stroke-linecap="round"/>
<path d="M-46 18 Q-30 10 -16 16" stroke="#3b2a22" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M16 16 Q30 10 46 18" stroke="#3b2a22" stroke-width="5" fill="none" stroke-linecap="round"/>
<circle cx="-52" cy="80" r="14" fill="#f08e86" opacity=".45"/><circle cx="52" cy="80" r="14" fill="#f08e86" opacity=".45"/>
<path d="M-3 66 Q0 74 5 66" stroke="#c48a66" stroke-width="4" fill="none" stroke-linecap="round"/>
<path d="M-22 96 Q0 116 22 96" stroke="#9a3b37" stroke-width="7" fill="none" stroke-linecap="round"/>
<g transform="translate(58,-56) rotate(20)"><path d="M0 0 L-22 -14 L-22 14Z M0 0 L22 -14 L22 14Z" fill="#ff7a66"/><circle r="7" fill="#e5604c"/></g>
<path d="M-40 -64 L0 -176 L40 -62Z" fill="#5fd39a"/><path d="M-26 -100 L28 -102 M-14 -136 L16 -138" stroke="#f2b705" stroke-width="9" stroke-linecap="round"/><circle cx="0" cy="-180" r="15" fill="#f2b705"/></g>'''

SVG=f'''<svg id="sc" viewBox="0 0 1080 1200" xmlns="http://www.w3.org/2000/svg">{DEFS}
<linearGradient id="dusk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a3550"/><stop offset=".55" stop-color="#b8694a"/><stop offset="1" stop-color="#f0a85a"/></linearGradient>
<linearGradient id="night" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0e1626"/><stop offset="1" stop-color="#2c3d5c"/></linearGradient>
<linearGradient id="room" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffe2c2"/><stop offset="1" stop-color="#f3c79a"/></linearGradient>
<!-- S1 pátio -->
<g id="s1">
 <rect width="1080" height="1200" fill="url(#night)"/>{''.join(f'<circle cx="{(i*137)%1080}" cy="{(i*61)%300+20}" r="{1.5+(i%3)}" fill="#fff" opacity=".6"/>' for i in range(40))}
 <rect x="60" y="300" width="960" height="470" fill="url(#corr)"/><path d="M40 304 L540 180 L1040 304Z" fill="#3c454f"/><rect x="40" y="296" width="1000" height="14" fill="#2a3038"/>
 {''.join(f'<g><rect x="{x-50}" y="372" width="100" height="14" rx="4" fill="#20252b"/><ellipse cx="{x}" cy="392" rx="12" ry="6" fill="#fff4cf"/><path d="M{x-14} 394 L{x-140} 770 L{x+140} 770 L{x+14} 394Z" fill="url(#lamp)" opacity=".35"/></g>' for x in (310,710))}
 <g id="doca"><rect x="160" y="430" width="300" height="340" fill="url(#slat)"/><g fill="#f2b705">{''.join(f'<path d="M{160+i*60} 430 l30 0 l-20 22 l-30 0z"/>' for i in range(5))}</g>
  <text x="310" y="530" text-anchor="middle" font-family="BC" font-size="64" fill="#f4f3ee">DOCA 3</text></g>
 <rect x="560" y="430" width="300" height="340" fill="url(#slat)"/><text x="710" y="530" text-anchor="middle" font-family="BC" font-size="64" fill="#f4f3ee" opacity=".6">DOCA 4</text>
 <rect y="770" width="1080" height="430" fill="url(#road)"/>{''.join(f'<rect x="{x}" y="900" width="70" height="10" fill="#f2b705" opacity=".55"/>' for x in range(0,1080,140))}
 {truck('t1',x=230,y=640,s=2.2,lights=True)}
 <g id="cal" transform="translate(830,130)" filter="url(#sh)"><rect x="-120" y="0" width="240" height="240" rx="26" fill="#f4f3ee"/><path d="M-120 26 Q-120 0 -94 0 L94 0 Q120 0 120 26 L120 70 L-120 70Z" fill="#ff7a66"/>
  <circle cx="-60" cy="0" r="10" fill="#16181b"/><circle cx="60" cy="0" r="10" fill="#16181b"/>
  <text id="calTxt" x="0" y="190" text-anchor="middle" font-family="BC" font-size="120" fill="#16181b">1</text><text x="0" y="52" text-anchor="middle" font-family="BC" font-size="44" fill="#fff">DIA</text></g>
 <g id="diaria" transform="translate(540,470)" filter="url(#sh)"><rect x="-250" y="-74" width="500" height="148" rx="74" fill="#5fd39a"/>
  <circle cx="-180" cy="0" r="44" fill="#f2b705"/><text x="-180" y="20" text-anchor="middle" font-family="BC" font-size="60" fill="#8a6400">$</text>
  <text x="40" y="30" text-anchor="middle" font-family="BC" font-size="88" fill="#16181b">+ DIÁRIA</text></g>
 {VIG}
</g>
<!-- S2 videochamada -->
<g id="s2">
 <rect width="1080" height="1200" fill="#1f2b40"/>
 {''.join(f'<rect class="cf" data-i="{i}" x="{(i*97)%1080}" y="0" width="14" height="24" rx="3" fill="{["#f2b705","#5fd39a","#ff7a66","#7fb3ff"][i%4]}"/>' for i in range(36))}
 {''.join(f'<g class="bal" data-i="{i}"><path d="M{x} {y+64} q-14 60 10 140" stroke="#f4f3ee" stroke-width="3" fill="none" opacity=".7"/><ellipse cx="{x}" cy="{y}" rx="56" ry="68" fill="{c}"/><ellipse cx="{x-18}" cy="{y-24}" rx="12" ry="20" fill="#fff" opacity=".35"/></g>' for i,(x,y,c) in enumerate([(120,300,'#ff7a66'),(960,260,'#f2b705'),(140,780,'#5fd39a'),(940,740,'#7fb3ff')]))}
 <g filter="url(#sh)"><rect x="262" y="70" width="556" height="1020" rx="78" fill="#0c0d0e"/><rect x="270" y="78" width="540" height="1004" rx="72" fill="none" stroke="#3a3f45" stroke-width="4"/></g>
 <clipPath id="scr"><rect x="290" y="100" width="500" height="960" rx="56"/></clipPath>
 <g clip-path="url(#scr)"><rect x="290" y="100" width="500" height="960" fill="url(#room)"/>
  <rect x="330" y="200" width="150" height="110" rx="8" fill="#fff" stroke="#e0a87a" stroke-width="8"/><path d="M345 290 L390 240 L420 270 L445 245 L470 290Z" fill="#5fd39a"/><circle cx="450" cy="225" r="14" fill="#f2b705"/>
  <path d="M600 180 l20 -30 l20 30 l20 -30 l20 30 l20 -30 l20 30" stroke="#ff7a66" stroke-width="6" fill="none"/>
  <path d="M290 180 Q540 120 790 180" stroke="#7fb3ff" stroke-width="4" fill="none"/>{''.join(f'<path d="M{330+i*55} {170-((i*55-220)**2)/1500} l14 30 l14 -30z" fill="{["#f2b705","#ff7a66","#5fd39a"][i%3]}"/>' for i in range(8))}
  <g transform="translate(540,540)">{GIRL}</g>
  <rect x="290" y="100" width="500" height="90" fill="rgba(0,0,0,.28)"/><circle cx="330" cy="145" r="10" fill="#5fd39a"/><text x="350" y="160" font-family="B" font-size="38" fill="#fff">Filha · ao vivo</text>
  <g transform="translate(700,930)"><rect x="-70" y="-90" width="140" height="180" rx="22" fill="#2a3a52" stroke="#fff" stroke-width="5"/>
   <circle cx="0" cy="-10" r="40" fill="#c98e63"/><path d="M-44 -22 C-44 -70 44 -70 44 -22Z" fill="#f2b705"/><path d="M-30 40 Q0 90 30 40 L50 90 L-50 90Z" fill="#3a6aa8"/></g>
  <rect x="330" y="980" width="96" height="60" rx="30" fill="#ff5a4a"/><path d="M356 1012 q22 -16 44 0" stroke="#fff" stroke-width="7" fill="none" stroke-linecap="round"/></g>
 <g id="cake" transform="translate(470,870)" filter="url(#sh)"><rect x="-120" y="-40" width="240" height="110" rx="16" fill="#fff5e6"/><path d="M-120 -20 q30 30 60 0 q30 30 60 0 q30 30 60 0 q30 30 60 0 L120 -40 L-120 -40Z" fill="#ff7a66"/>
  {''.join(f'<rect x="{x-6}" y="-100" width="12" height="60" rx="3" fill="#7fb3ff"/><ellipse class="fl" cx="{x}" cy="-112" rx="10" ry="16" fill="#ffcc33"/><circle cx="{x}" cy="-112" r="26" fill="#ffcc33" opacity=".35" filter="url(#glow)"/>' for x in (-60,0,60))}</g>
 <g id="gift" transform="translate(880,1000)" filter="url(#sh)"><rect x="-90" y="-60" width="180" height="140" rx="12" fill="#ff7a66"/><rect x="-100" y="-90" width="200" height="44" rx="10" fill="#e5604c"/>
  <rect x="-14" y="-90" width="28" height="170" fill="#f2b705"/><path d="M0 -90 C-60 -150 -90 -100 0 -90 C90 -100 60 -150 0 -90Z" fill="#f2b705"/></g>
 {VIG}
</g>
<!-- S3 estrada -->
<g id="s3">
 <rect width="1080" height="1200" fill="url(#dusk)"/><circle cx="820" cy="600" r="220" fill="#ffd27a" opacity=".35" filter="url(#glow)"/><circle cx="820" cy="600" r="110" fill="#ffe0a0"/>
 {hills()}
 {road(780)}
 <g id="tri" transform="translate(470,840)"><path d="M0 -70 L60 40 L-60 40Z" fill="#ff5a4a" stroke="#fff" stroke-width="6" stroke-linejoin="round"/><path d="M0 -36 L30 22 L-30 22Z" fill="#fff" opacity=".85"/></g>
 {truck('t3b',cab='r',x=560,y=618,s=1.6,extra=HAZ+'<ellipse cx="48" cy="122" rx="24" ry="8" fill="#141518"/>')}
 <g id="pneu" transform="translate(637,792)"><circle r="80" fill="none" stroke="#f2b705" stroke-width="12"/></g>
 <g id="pneuLab" transform="translate(640,500)" filter="url(#sh)"><rect x="-230" y="-60" width="460" height="100" rx="50" fill="#f2b705"/><text x="0" y="16" text-anchor="middle" font-family="BC" font-size="66" fill="#16181b">PNEU FURADO</text></g>
 {truck('t3a',x=-500,y=900,s=1.6,lights=True)}
 {VIG}
</g>
<!-- S4 tempo x jantar -->
<g id="s4">
 <rect width="1080" height="1200" fill="#18202c"/><circle cx="270" cy="560" r="320" fill="#ff7a66" opacity=".12" filter="url(#glow)"/><circle cx="810" cy="560" r="320" fill="#5fd39a" opacity=".12" filter="url(#glow)"/>
 <g transform="translate(270,560)" filter="url(#sh)"><circle r="214" fill="#2a2d31"/><circle r="196" fill="#f7f4ec"/><circle r="196" fill="none" stroke="#e1dccf" stroke-width="10"/>
  {''.join(f'<rect x="-5" y="-184" width="10" height="{36 if i%3==0 else 20}" rx="4" fill="#16181b" transform="rotate({i*30})"/>' for i in range(12))}
  <g id="hm"><rect x="-8" y="-164" width="16" height="170" rx="8" fill="#16181b"/></g><g id="hh"><rect x="-12" y="-104" width="24" height="110" rx="12" fill="#ff5a4a"/></g><circle r="18" fill="#16181b"/><circle r="7" fill="#f2b705"/>
  <text y="330" text-anchor="middle" font-family="BC" font-size="92" fill="#ff7a66">+2 HORAS</text></g>
 <text x="540" y="580" text-anchor="middle" font-family="BC" font-size="90" fill="#8a8f98">x</text>
 <g transform="translate(810,560)" filter="url(#sh)"><rect x="100" y="-230" width="40" height="90" fill="#7a4a3a"/>
  {''.join(f'<circle class="smk" data-i="{i}" cx="120" cy="-250" r="{18+i*6}" fill="#c9c5ba" opacity=".5"/>' for i in range(3))}
  <path d="M-200 -10 L0 -210 L200 -10Z" fill="#c4553f"/><path d="M-200 -10 L0 -210 L0 -170 L-160 -10Z" fill="#d96a50"/><rect x="-165" y="-20" width="330" height="230" fill="#f4efe4"/>
  <circle cx="-60" cy="64" r="90" fill="url(#lamp)"/><rect id="win" x="-110" y="20" width="100" height="90" rx="6" fill="#ffcf4a" stroke="#7a4a3a" stroke-width="8"/><path d="M-60 20 L-60 110 M-110 65 L-10 65" stroke="#7a4a3a" stroke-width="6"/>
  <rect x="40" y="60" width="80" height="150" rx="6" fill="#8a5a42"/><circle cx="104" cy="140" r="6" fill="#f2b705"/>
  <path id="heart" d="M0 -110 C-30 -150 -80 -120 -50 -80 L0 -40 L50 -80 C80 -120 30 -150 0 -110Z" fill="#ff5a4a" transform="translate(0,-160)"/>
  <text y="330" text-anchor="middle" font-family="BC" font-size="92" fill="#5fd39a">JANTAR</text></g>
 {VIG}
</g>
<!-- S5 A -->
<g id="s5">
 <rect width="1080" height="1200" fill="url(#dusk)"/>{hills(('#5d4542','#463638','#33292e'),600)}{road(780)}
 {truck('t5a',x=-40,y=660,s=1.5,extra=HAZ,lights=True)}
 {truck('t5b',cab='r',x=520,y=618,s=1.6,extra=HAZ)}
 <g id="newT" transform="translate(720,980)"><circle r="30" fill="#141518"/><circle r="18" fill="url(#rim)"/></g>
 <g id="wr" transform="translate(800,950)" filter="url(#sh)"><rect x="-100" y="-14" width="200" height="28" rx="14" fill="url(#chrome)"/><circle cx="-100" cy="0" r="30" fill="none" stroke="#c9ced4" stroke-width="18"/></g>
 <g transform="translate(540,250)" filter="url(#sh)"><rect x="-380" y="-90" width="760" height="180" rx="40" fill="#16181b"/><rect x="-350" y="-62" width="124" height="124" rx="24" fill="#f2b705"/>
  <text x="-288" y="40" text-anchor="middle" font-family="BC" font-size="112" fill="#16181b">A</text><text x="70" y="38" text-anchor="middle" font-family="BC" font-size="96" fill="#f4f3ee">PARA E AJUDA</text></g>
 {VIG}
</g>
<!-- S6 B -->
<g id="s6">
 <rect width="1080" height="1200" fill="url(#night)"/>{''.join(f'<circle cx="{(i*173)%1080}" cy="{(i*53)%380+20}" r="{1.5+(i%3)}" fill="#fff" opacity=".7"/>' for i in range(50))}
 <circle cx="880" cy="320" r="160" fill="#f4f3ee" opacity=".15" filter="url(#glow)"/><circle cx="880" cy="320" r="80" fill="#f4f3ee"/><circle cx="905" cy="300" r="70" fill="#1a2740"/>
 {hills(('#263247','#1c2638','#141c2a'),620)}{road(780,'#5a5048')}
 {truck('t6b',cab='r',x=40,y=700,s=1.1,extra=HAZ)}
 {truck('t6a',x=380,y=890,s=1.6,lights=True)}
 <g transform="translate(900,720)" filter="url(#sh)"><rect x="-8" y="0" width="16" height="150" fill="#9aa3ad"/><rect x="-160" y="-90" width="320" height="100" rx="12" fill="#1f7a46" stroke="#fff" stroke-width="5"/><text y="-22" text-anchor="middle" font-family="BC" font-size="56" fill="#fff">CASA 120 KM</text></g>
 <g transform="translate(540,250)" filter="url(#sh)"><rect x="-380" y="-90" width="760" height="180" rx="40" fill="#16181b"/><rect x="-350" y="-62" width="124" height="124" rx="24" fill="#f2b705"/>
  <text x="-288" y="40" text-anchor="middle" font-family="BC" font-size="112" fill="#16181b">B</text><text x="70" y="38" text-anchor="middle" font-family="BC" font-size="96" fill="#f4f3ee">SEGUE VIAGEM</text></g>
 {VIG}
</g>
<!-- S7 -->
<g id="s7">
 <rect width="1080" height="1200" fill="#14202e"/><circle cx="290" cy="620" r="300" fill="#f2b705" opacity=".08" filter="url(#glow)"/><circle cx="790" cy="620" r="300" fill="#f2b705" opacity=".08" filter="url(#glow)"/>
 <text x="540" y="200" text-anchor="middle" font-family="BC" font-size="120" fill="#f4f3ee">O QUE O <tspan fill="#f2b705">ZÉ</tspan> FAZ?</text>
 <g id="k7a" transform="translate(290,620)"><g filter="url(#sh)"><rect x="-230" y="-300" width="460" height="600" rx="40" fill="#1c1f23"/></g><rect id="k7ao" x="-230" y="-300" width="460" height="600" rx="40" fill="none" stroke="#f2b705" stroke-width="0"/>
  <rect x="-60" y="-260" width="120" height="120" rx="24" fill="#f2b705"/><text y="-162" text-anchor="middle" font-family="BC" font-size="108" fill="#16181b">A</text>
  <g transform="translate(-30,-10)"><circle cx="40" cy="20" r="60" fill="#141518"/><circle cx="40" cy="20" r="34" fill="url(#rim)"/><g transform="rotate(-35)"><rect x="-110" y="-16" width="220" height="32" rx="16" fill="url(#chrome)"/><circle cx="-110" cy="0" r="34" fill="none" stroke="#c9ced4" stroke-width="20"/></g></g>
  <text y="150" text-anchor="middle" font-family="BC" font-size="76" fill="#f4f3ee">PARA E</text><text y="230" text-anchor="middle" font-family="BC" font-size="76" fill="#f2b705">AJUDA</text></g>
 <g id="k7b" transform="translate(790,620)"><g filter="url(#sh)"><rect x="-230" y="-300" width="460" height="600" rx="40" fill="#1c1f23"/></g><rect id="k7bo" x="-230" y="-300" width="460" height="600" rx="40" fill="none" stroke="#f2b705" stroke-width="0"/>
  <rect x="-60" y="-260" width="120" height="120" rx="24" fill="#f2b705"/><text y="-162" text-anchor="middle" font-family="BC" font-size="108" fill="#16181b">B</text>
  {truck('mini',x=-150,y=-80,s=1.0,lights=True)}
  <text y="150" text-anchor="middle" font-family="BC" font-size="76" fill="#f4f3ee">SEGUE</text><text y="230" text-anchor="middle" font-family="BC" font-size="76" fill="#f2b705">VIAGEM</text></g>
 <g id="cta" transform="translate(540,1080)" filter="url(#sh)"><rect x="-400" y="-80" width="800" height="150" rx="75" fill="#f2b705"/><text y="30" text-anchor="middle" font-family="BC" font-size="96" fill="#16181b">COMENTE A OU B</text></g>
</g>
</svg>'''

HTML=r'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>
@font-face{font-family:B;src:url(fonts/barlow-latin-700-normal.woff2);font-weight:700}
@font-face{font-family:BC;src:url(fonts/barlow-condensed-latin-800-normal.woff2);font-weight:800}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#101820;font-family:B;color:#f4f3ee}
#sc{position:absolute;left:0;top:250px;width:1080px;height:1200px}
#sc text{font-weight:800}
#wm{position:absolute;left:0;right:0;top:120px;text-align:center;font:700 36px B;opacity:.75;letter-spacing:1px;z-index:50}
#ttl{position:absolute;left:0;right:0;top:300px;text-align:center;z-index:30;opacity:0}
.pill{display:inline-block;background:#f2b705;color:#16181b;font:800 100px/1 BC;text-transform:uppercase;padding:24px 54px 12px;border-radius:999px;box-shadow:0 14px 0 rgba(0,0,0,.3)}
#zc{position:absolute;left:40px;top:1490px;width:330px;height:330px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#4f86b0,#1f3c57);overflow:hidden;border:10px solid #f2b705;box-shadow:0 16px 30px rgba(0,0,0,.5);z-index:20}
#ze{position:absolute;left:5px;top:-4px;width:300px;height:390px}
#ze svg{width:100%;height:100%}
#subs{position:absolute;left:390px;right:30px;top:1560px;height:240px;z-index:40}
#subs .g{position:absolute;left:0;right:0;top:0;opacity:0;text-align:left}
#subs span.w{display:inline-block;margin:0 10px 8px 0;font:800 96px/1.02 BC;text-transform:uppercase;color:#f4f3ee;text-shadow:0 6px 0 rgba(0,0,0,.55)}
#subs span.w.on{color:#f2b705}
#ex{position:absolute;left:0;right:0;top:1860px;text-align:center;font:700 28px B;color:#8a8f98;text-transform:uppercase;letter-spacing:2px}
</style></head><body>
__SVG__
<div id="wm">@appdiariodebordo</div>
<div id="ttl"><span class="pill">Vocês escolheram A</span></div>
<div id="zc"><div id="ze">__ZE__</div></div>
<div id="subs"></div>
<script>
const TOT=__TOT__, WORDS=__WORDS__, MOUTH="__MOUTH__";
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const cl=x=>Math.max(0,Math.min(1,x)), eo=x=>1-Math.pow(1-cl(x),3), eio=x=>{x=cl(x);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2};
const back=x=>{x=cl(x);const c=1.6;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
const ws=i=>WORDS[i].start, we=i=>WORDS[i].end;
const SC=[['s1',0,ws(13)-.1],['s2',ws(13)-.1,ws(22)-.1],['s3',ws(22)-.1,ws(34)-.1],['s4',ws(34)-.1,ws(45)-.1],['s5',ws(45)-.1,ws(50)-.1],['s6',ws(50)-.1,ws(54)-.1],['s7',ws(54)-.1,TOT]];
const EXPR=[[0,'happy'],[ws(3),'calm'],[ws(13),'happy'],[ws(22),'calm'],[ws(26),'worried'],[ws(34),'worried'],[ws(45),'calm'],[ws(54),'happy']];
const BLINK=[1.7,4.6,7.9,11.2,14.5,18.0,21.3,24.6];
const G=[];(function(){let g=[];WORDS.forEach((w,i)=>{g.push(i);const last=/[.?:,]$/.test(w.text)||g.length>=3||g.map(j=>WORDS[j].text).join('').length>13;if(last){G.push(g);g=[]}});if(g.length)G.push(g)})();
const cap=$('#subs');G.forEach(g=>{const d=document.createElement('div');d.className='g';d.innerHTML=g.map(i=>'<span class="w" data-i="'+i+'">'+WORDS[i].text.replace(/[,]$/,'')+'</span>').join(' ');cap.appendChild(d)});
const GT=G.map((g,gi)=>{const s=ws(g[0])-.04;const ne=gi+1<G.length?ws(G[gi+1][0])-.04:TOT;return [s,Math.min(we(g[g.length-1])+.25,ne)]});
const tr=(id,s)=>{const e=document.getElementById(id);if(e)e.setAttribute('transform',s)};
const base={};$$('#sc g[id]').forEach(g=>base[g.id]=g.getAttribute('transform')||'');
const T=(id,extra)=>tr(id,base[id]+' '+extra);
window.render=function(t){
 // cenas: corte com leve zoom
 SC.forEach(([id,a,b])=>{const g=document.getElementById(id);const on=t>=a&&t<b;g.style.display=on?'':'none';
  if(on){const k=eo((t-a)/.35);const z=1.06-.06*k+.02*((t-a)/(b-a));g.setAttribute('transform','translate(540 600) scale('+z+') translate(-540 -600)');g.style.opacity=Math.min(1,(t-a)/.15)}});
 // S1
 $('#ttl').style.opacity=cl(t/.15)*(1-cl((t-ws(3)+.1)/.2));$('#ttl').style.transform='scale('+(.85+.15*back(t/.35))+')';
 $('#calTxt').textContent=t<ws(7)?'1':(t<ws(8)+.15?'2':'3');
 T('cal','scale('+(1+.12*Math.max(0,1-Math.abs(t-ws(7))/.25)+.12*Math.max(0,1-Math.abs(t-ws(8)-.15)/.25))+')');
 const dk=cl((t-ws(10))/.35);T('diaria','scale('+(dk?.3+.7*back((t-ws(10))/.4):0.001)+')');
 T('t1','translate(0,'+(Math.sin(t*6)*1.5)+')');
 // S2
 $$('.bal').forEach((b,i)=>b.setAttribute('transform','translate(0,'+(Math.sin(t*1.6+i)*18)+')'));
 $$('.cf').forEach((c,i)=>{const y=((t*(120+(i%5)*30)+i*90)%1300)-60;c.setAttribute('transform','translate(0,'+y+') rotate('+(t*200+i*40)+' '+c.getAttribute('x')+' 12)')});
 $$('.smk').forEach((c,i)=>{const p=((t*.5+i/3)%1);c.setAttribute('cy',-250-p*160);c.setAttribute('cx',120+p*40);c.setAttribute('opacity',.5*(1-p))});
 $$('.fl').forEach((f,i)=>f.setAttribute('ry',14+3*Math.sin(t*14+i*2)));
 const gk=cl((t-ws(19))/.35);T('gift','scale('+(gk?.2+.8*back((t-ws(19))/.45):0.001)+') rotate('+(Math.sin(t*8)*4*gk)+')');
 T('girl','rotate('+(Math.sin(t*2.2)*3)+')');
 // S3
 const a3=ws(22)-.1;const p3=eo((t-a3)/3.2);T('t3a','translate('+(p3*560)+',0)');
 $$('.haz').forEach(h=>h.style.opacity=(Math.floor(t*2.5)%2)?1:.15);
 const pk=cl((t-ws(32))/.3);T('pneu','scale('+(pk?.5+.5*back((t-ws(32))/.4):0.001)+')');$('#pneu').style.opacity=pk;
 T('pneuLab','scale('+(pk?.6+.4*back((t-ws(32))/.4):0.001)+')');
 T('tri','rotate('+(Math.sin(t*3)*2)+')');
 // S4
 const a4=ws(34)-.1;const sp=eio((t-ws(36))/2.2);T('hm','rotate('+(sp*720)+')');T('hh','rotate('+(60+sp*60)+')');
 $('#win').setAttribute('fill',(t>ws(42))?'#ffd24a':'#f2b705');
 const hk=cl((t-ws(43))/.3);T('heart','scale('+(hk?(.6+.4*back((t-ws(43))/.4))*(1+.06*Math.sin(t*9)):0.001)+')');
 // S5
 const a5=ws(45)-.1;T('wr','rotate('+(Math.sin((t-a5)*9)*25)+')');const nt=eo((t-ws(48))/.6);T('newT','translate('+(nt*-123)+','+(nt*-187)+') rotate('+(nt*360)+')');
 // S6
 const a6=ws(50)-.1;const p6=eio((t-a6)/2.2);T('t6a','translate('+(p6*520)+',0)');T('t6b','translate('+(-p6*60)+',0)');
 // S7
 const a7=ws(54)-.1;['a','b'].forEach((k,i)=>{const s=a7+.15+i*.2;const q=cl((t-s)/.3);T('k7'+k,'scale('+(q?.6+.4*back((t-s)/.4):0.001)+')')});
 const hlA=(t>=ws(60)-.05&&t<ws(61)-.05),hlB=t>=ws(62)-.05;$('#k7ao').setAttribute('stroke-width',hlA?14:0);$('#k7bo').setAttribute('stroke-width',hlB?14:0);
 const ck=cl((t-ws(59)+.1)/.3);T('cta','scale('+(ck?.6+.4*back((t-ws(59)+.1)/.4):0.001)+')');
 // Zé
 let ex='calm';EXPR.forEach(e=>{if(t>=e[0])ex=e[1]});
 ['calm','worried','shock','happy'].forEach(k=>{$('#ex_'+k).style.display=k==ex?'':'none'});
 const f=Math.min(MOUTH.length-1,Math.round(t*30));const m=+MOUTH[f];
 ['calm','worried','shock','happy'].forEach(k=>{$('#mo_'+k).style.display=(k==ex&&m==0)?'':'none'});
 $('#sp1').style.display=m==1?'':'none';$('#sp2').style.display=m==2?'':'none';
 let bl=false;BLINK.forEach(b=>{if(t>=b&&t<b+.13)bl=true});$('#blink').style.display=bl?'':'none';
 $('#ze').style.transform='translateY('+(Math.sin(t*2.3)*4-(m>1?4:0))+'px) rotate('+(Math.sin(t*1.4)*1.5)+'deg)';
 const gs=cap.children;for(let gi=0;gi<G.length;gi++){const el=gs[gi],[a,b]=GT[gi];const on=t>=a&&t<=b;el.style.opacity=on?1:0;if(on){el.style.transform='scale('+(0.92+0.08*back((t-a)/.15))+')';el.querySelectorAll('span.w').forEach(sp=>{const i=+sp.dataset.i;sp.className='w'+(t>=ws(i)-.02&&t<we(i)+.04?' on':'')})}}
};
window.render(0);
</script></body></html>'''
HTML=(HTML.replace('__SVG__',SVG).replace('__ZE__',ze_svg()).replace('__TOT__',str(TOT))
      .replace('__WORDS__',json.dumps(W,ensure_ascii=False)).replace('__MOUTH__',mouth))
open('index.html','w').write(HTML)
def ws(i): return W[i]['start']
cues=[]
for a in [0.02,ws(13)-.1,ws(22)-.1,ws(34)-.1,ws(45)-.1,ws(50)-.1,ws(54)-.1]: cues.append(dict(t=round(a,3),k='whoosh'))
for a in [ws(7),ws(8)+.15,ws(19),ws(32),ws(43),ws(54)+.05,ws(54)+.25]: cues.append(dict(t=round(a,3),k='pop'))
cues.append(dict(t=round(ws(10),3),k='ding'))
cues.append(dict(t=round(ws(32),3),k='slam'))
for k in range(8): cues.append(dict(t=round(ws(36)+k*0.27,3),k='tick'))
cues.append(dict(t=round(ws(59)-.1,3),k='ding'))
json.dump(cues,open('cues.json','w'))
print('ok',len(HTML)//1024,'KB')
