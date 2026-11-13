"""Zé (personagem da série): busto vetorial 2D plano. ze_svg() devolve UM svg com grupos que o
index.html liga e desliga: expressões (ex_*), boca fechada (mo_*), boca falando (sp1/sp2) e piscada (blink)."""
EXPR={'calm':dict(br=(0,0),lid=0,mouth='M174 318 Q200 326 226 318',look=(0,0)),
      'worried':dict(br=(-10,4),lid=-2,mouth='M176 324 Q200 312 224 324',look=(0,3)),
      'shock':dict(br=(-14,-10),lid=-5,mouth='O',look=(0,0)),
      'happy':dict(br=(-4,-2),lid=3,mouth='M170 312 Q200 342 230 312 Q200 324 170 312Z',look=(0,0))}
def _eye(cx,lid,lx,ly):
    top=232-9+lid
    return f'''<path d="M{cx-17} 234 Q{cx} {top-6} {cx+17} 234 Q{cx} {246-lid*0.3} {cx-17} 234Z" fill="#f4efe6"/>
<circle cx="{cx+lx}" cy="{235+ly}" r="8.5" fill="#4a3220"/><circle cx="{cx+lx}" cy="{235+ly}" r="4.5" fill="#140d09"/>
<circle cx="{cx+lx+3}" cy="{232+ly}" r="2.2" fill="#fff"/>
<path d="M{cx-18} 234 Q{cx} {top-8} {cx+18} 234 Q{cx} {top-3} {cx-18} 234Z" fill="#9a6440" opacity=".55"/>'''
def _brow(cx,bi,bo):
    s=-1 if cx<200 else 1
    inner=cx-s*16; outer=cx+s*18
    yi=212+bi; yo=208+bo
    return f'<path d="M{inner} {yi} Q{cx} {min(yi,yo)-7} {outer} {yo} L{outer} {yo+6} Q{cx} {min(yi,yo)-1} {inner} {yi+7}Z" fill="#2a1f19"/>'
def _mouth(E):
    if E=='O':
        return '<ellipse cx="200" cy="322" rx="13" ry="17" fill="#4a1f1a"/><ellipse cx="200" cy="330" rx="8" ry="6" fill="#b65a52"/>'
    if E.endswith('Z'):
        return f'<path d="{E}" fill="#4a1f1a"/><path d="M176 315 Q200 324 224 315 L224 318 Q200 327 176 318Z" fill="#f1ece2"/>'
    return f'<path d="{E}" stroke="#6e3a2e" stroke-width="5" fill="none" stroke-linecap="round"/>'
SP1='<ellipse cx="200" cy="321" rx="15" ry="7" fill="#4a1f1a"/><path d="M187 317 Q200 321 213 317 L213 319 Q200 323 187 319Z" fill="#f1ece2"/>'
SP2='<ellipse cx="200" cy="324" rx="17" ry="13" fill="#4a1f1a"/><path d="M185 315 Q200 320 215 315 L215 319 Q200 324 185 319Z" fill="#f1ece2"/><ellipse cx="200" cy="332" rx="9" ry="5" fill="#b65a52"/>'
def ze_svg():
    ex='';mo=''
    for k,E in EXPR.items():
        bi,bo=E['br'];lx,ly=E['look']
        ex+=f'<g id="ex_{k}" style="display:none">{_brow(170,bi,bo)}{_brow(230,bi,bo)}{_eye(170,E["lid"],lx,ly)}{_eye(230,E["lid"],lx,ly)}</g>'
        mo+=f'<g id="mo_{k}" style="display:none">{_mouth(E["mouth"])}</g>'
    blink=''.join(f'<ellipse cx="{cx}" cy="235" rx="21" ry="13" fill="#c98e63"/><path d="M{cx-18} 238 Q{cx} 246 {cx+18} 238" stroke="#2a1f19" stroke-width="3.5" fill="none" stroke-linecap="round"/>' for cx in (170,230))
    return f'''<svg id="zesvg" viewBox="0 0 400 520" xmlns="http://www.w3.org/2000/svg">
<defs>
<linearGradient id="sk" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d9a379"/><stop offset="1" stop-color="#b57a51"/></linearGradient>
<linearGradient id="sh" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4f79b4"/><stop offset="1" stop-color="#2c4f80"/></linearGradient>
<linearGradient id="cap" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f6c22a"/><stop offset="1" stop-color="#d79f00"/></linearGradient>
</defs>
<path d="M70 520 C72 440 110 404 168 392 L200 412 L232 392 C290 404 328 440 330 520Z" fill="url(#sh)"/>
<path d="M168 392 L200 440 L232 392 L222 386 L200 418 L178 386Z" fill="#24466f"/>
<path d="M200 418 L200 470" stroke="#24466f" stroke-width="3"/><circle cx="200" cy="440" r="4" fill="#e9e3d6"/><circle cx="200" cy="460" r="4" fill="#e9e3d6"/>
<path d="M166 340 L166 396 Q200 420 234 396 L234 340Z" fill="#a86f47"/>
<ellipse cx="128" cy="250" rx="14" ry="24" fill="#c08356"/><ellipse cx="272" cy="250" rx="14" ry="24" fill="#c08356"/>
<path d="M132 200 C130 150 160 132 200 132 C240 132 270 150 268 200 C268 262 262 300 244 330 C232 350 216 360 200 360 C184 360 168 350 156 330 C138 300 132 262 132 200Z" fill="url(#sk)"/>
<path d="M140 268 C146 310 168 352 200 356 C232 352 254 310 260 268 C254 300 240 330 222 338 C210 328 190 328 178 338 C160 330 146 300 140 268Z" fill="#3a2e28" opacity=".28"/>
<path d="M132 214 C130 190 134 176 140 170 L146 230 Z" fill="#5a524c"/><path d="M268 214 C270 190 266 176 260 170 L254 230 Z" fill="#5a524c"/>
{ex}
<g id="blink" style="display:none">{blink}</g>
<path d="M200 244 C196 262 188 276 190 284 C194 292 206 292 210 284 C212 276 204 262 200 244Z" fill="#a86f47" opacity=".7"/>
<path d="M168 304 C180 292 194 294 200 298 C206 294 220 292 232 304 C224 310 212 308 200 304 C188 308 176 310 168 304Z" fill="#2f2622"/>
{mo}
<g id="sp1" style="display:none">{SP1}</g><g id="sp2" style="display:none">{SP2}</g>
<path d="M126 196 C122 120 166 92 200 92 C246 92 280 122 274 196 C250 180 150 180 126 196Z" fill="url(#cap)"/>
<path d="M200 92 C176 92 150 104 140 130 L140 190 C160 184 180 182 200 182Z" fill="#f2efe6" opacity=".9"/>
<path d="M150 150 L196 150 L196 176 L150 176Z" fill="#16181b"/><path d="M158 160 l20 0 l6 6 l0 6 l-26 0z" fill="#f2b705"/><circle cx="163" cy="173" r="3" fill="#f2b705"/><circle cx="178" cy="173" r="3" fill="#f2b705"/>
<path d="M118 196 C150 176 250 176 282 196 C296 204 292 214 276 212 C240 202 160 202 124 212 C108 214 104 204 118 196Z" fill="#c99500"/>
<circle cx="200" cy="94" r="7" fill="#c99500"/>
</svg>'''
if __name__=='__main__': print(len(ze_svg()))
