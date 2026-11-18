# Arte detalhada para as cenas do Zé (SVG): defs comuns, caminhão com acabamento, fundos em camadas.
DEFS='''<defs>
<filter id="sh" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="14" stdDeviation="12" flood-color="#000" flood-opacity=".35"/></filter>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="14"/></filter>
<filter id="soft"><feGaussianBlur stdDeviation="3"/></filter>
<radialGradient id="vig" cx="50%" cy="45%" r="75%"><stop offset="60%" stop-color="#000" stop-opacity="0"/><stop offset="100%" stop-color="#000" stop-opacity=".55"/></radialGradient>
<linearGradient id="trl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fbf8f1"/><stop offset=".75" stop-color="#e3ddcf"/><stop offset="1" stop-color="#c9c2b2"/></linearGradient>
<linearGradient id="chrome" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4f6f8"/><stop offset=".5" stop-color="#9aa3ad"/><stop offset="1" stop-color="#dfe4ea"/></linearGradient>
<linearGradient id="glass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8fc1d9"/><stop offset=".45" stop-color="#2b4f66"/><stop offset="1" stop-color="#16303f"/></linearGradient>
<radialGradient id="rim" cx="45%" cy="40%"><stop offset="0" stop-color="#e9edf1"/><stop offset=".7" stop-color="#9aa3ad"/><stop offset="1" stop-color="#5d656e"/></radialGradient>
<linearGradient id="road" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4a5058"/><stop offset="1" stop-color="#23272c"/></linearGradient>
<radialGradient id="lamp" cx="50%" cy="50%"><stop offset="0" stop-color="#ffe7a3" stop-opacity=".9"/><stop offset="1" stop-color="#ffe7a3" stop-opacity="0"/></radialGradient>
<pattern id="corr" width="24" height="10" patternUnits="userSpaceOnUse"><rect width="24" height="10" fill="#4b5560"/><rect width="12" height="10" fill="#56616d"/></pattern>
<pattern id="slat" width="10" height="26" patternUnits="userSpaceOnUse"><rect width="10" height="26" fill="#2d3238"/><rect y="22" width="10" height="4" fill="#1f2327"/></pattern>
</defs>'''

def _grad(id_, c1, c2):
    return f'<linearGradient id="{id_}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>'

CABS={'y':('#ffd23f','#d79a00'),'r':('#ef6b5e','#b8352b')}

def truck(id_, cab='y', x=0, y=0, s=1.0, extra='', lights=False):
    c1,c2=CABS[cab]; g=f'cab{cab}'
    wheel=lambda cx:(f'<g><circle cx="{cx}" cy="108" r="19" fill="#141518"/><circle cx="{cx}" cy="108" r="11" fill="url(#rim)"/>'
                     f'<circle cx="{cx}" cy="108" r="4" fill="#3b4048"/></g>')
    glow=('<ellipse cx="300" cy="90" rx="70" ry="26" fill="url(#lamp)"/>' if lights else '')
    return f'''<g id="{id_}" transform="translate({x},{y}) scale({s})"><defs>{_grad(g,c1,c2)}</defs>
<ellipse cx="150" cy="128" rx="160" ry="10" fill="#000" opacity=".35" filter="url(#soft)"/>
<rect x="8" y="14" width="176" height="88" rx="6" fill="url(#trl)"/>
{''.join(f'<rect x="{14+i*17}" y="18" width="3" height="80" fill="#000" opacity=".06"/>' for i in range(10))}
<rect x="8" y="64" width="176" height="7" fill="{c1}"/><rect x="8" y="94" width="176" height="8" fill="#9a9384"/>
<rect x="30" y="100" width="120" height="8" fill="#2a2d31"/>
<path d="M186 40 Q186 34 192 34 L238 34 Q246 34 250 40 L278 74 Q286 82 286 92 L286 104 L186 104Z" fill="url(#{g})"/>
<path d="M226 42 L240 42 Q244 42 247 46 L268 74 L226 74Z" fill="url(#glass)"/><path d="M230 46 L240 46 L250 60 L236 70Z" fill="#fff" opacity=".18"/>
<rect x="194" y="42" width="26" height="30" rx="3" fill="url(#glass)"/>
<rect x="186" y="78" width="100" height="5" fill="#000" opacity=".15"/>
<rect x="198" y="84" width="22" height="16" rx="3" fill="url(#chrome)"/>
<rect x="276" y="80" width="12" height="20" rx="2" fill="url(#chrome)"/><rect x="280" y="74" width="8" height="6" rx="2" fill="#fff7d6"/>
<rect x="222" y="30" width="5" height="22" rx="2" fill="#2a2d31"/><rect x="219" y="28" width="9" height="16" rx="2" fill="#2a2d31"/>
<rect x="184" y="100" width="104" height="8" rx="2" fill="#1d1f22"/>
<path d="M196 108 a20 20 0 0 1 40 0" fill="#1d1f22"/><path d="M240 108 a20 20 0 0 1 40 0" fill="#1d1f22"/>
{wheel(48)}{wheel(88)}{wheel(126)}{wheel(216)}{wheel(260)}{glow}{extra}</g>'''

def hills(c=('#6b4a45','#4f3a3c','#3a2e33'), y0=560):
    a,b,cc=c
    return (f'<path d="M0 {y0} C160 {y0-90} 320 {y0-70} 480 {y0-20} C640 {y0+30} 820 {y0-110} 1080 {y0-40} L1080 {y0+260} L0 {y0+260}Z" fill="{a}"/>'
            f'<path d="M0 {y0+70} C200 {y0+10} 360 {y0+40} 540 {y0+80} C720 {y0+120} 900 {y0+30} 1080 {y0+70} L1080 {y0+260} L0 {y0+260}Z" fill="{b}"/>'
            + ''.join(f'<g transform="translate({x},{y0+100+ (i%2)*12})"><rect x="-4" y="0" width="8" height="40" fill="{cc}"/><circle cx="0" cy="-6" r="{22+(i%3)*6}" fill="{cc}"/></g>' for i,x in enumerate(range(40,1080,110))))

def road(y=760, shoulder='#8a7a62'):
    return (f'<rect y="{y}" width="1080" height="{1200-y}" fill="url(#road)"/><rect y="{y}" width="1080" height="64" fill="{shoulder}"/>'
            f'<rect y="{y+60}" width="1080" height="6" fill="#f4f3ee" opacity=".7"/>')

VIG='<rect width="1080" height="1200" fill="url(#vig)" pointer-events="none"/>'
