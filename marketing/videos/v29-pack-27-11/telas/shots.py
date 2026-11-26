import json, pathlib, subprocess, time, sys
from playwright.sync_api import sync_playwright
REPO='/home/claude/diario-de-bordo'; OUT=pathlib.Path('/home/claude/telas-ia/png'); OUT.mkdir(exist_ok=True)
srv=subprocess.Popen(['python3','-m','http.server','8765'],cwd=REPO,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
S=open('/home/claude/telas-ia/estado.json').read(); FAKE=open('/home/claude/telas-ia/fake-supabase.js').read()
RESP={'voz_lancar':{"texto":"Abasteci 300 litros a 6 e 19 no Posto Graal","lancamento":{"tipo":"diesel","litros":300,"preco":6.19,"obs":"Posto Graal"}},
 'mes':{"resposta":"Em novembro sobrou **R$ 2.865,60** até agora.\n- Chapecó → Curitiba: sobrou R$ 2.865,60 (frete R$ 4.560,00, gastos R$ 1.694,40)\n- Curitiba → Santos ainda em andamento."},
 'frete':{"resposta":"Pelos seus lançamentos, cada km custa uns **R$ 3,53** (diesel, pedágio, comida e manutenção).\n- Ida + volta vazia: **2.000 km**\n- Custo: 2.000 × R$ 3,53 = **R$ 7.060,00**\n- Frete: R$ 6.000,00\n\n**Não compensa:** você perderia uns **R$ 1.060,00**. Só vale se arrumar carga para a volta."}}
estado={'q':'mes'}
def ia(route):
    b=json.loads(route.request.post_data or '{}')
    r=RESP['voz_lancar'] if b.get('acao')=='voz' else RESP[estado['q']]
    route.fulfill(status=200,content_type='application/json',body=json.dumps(r,ensure_ascii=False))
with sync_playwright() as p:
    br=p.chromium.launch(args=['--use-fake-ui-for-media-stream','--use-fake-device-for-media-stream'])
    ctx=br.new_context(viewport={'width':390,'height':844},device_scale_factor=3,permissions=['microphone'])
    ctx.add_init_script(f"try{{if(!localStorage.getItem('diario-bordo-v1'))localStorage.setItem('diario-bordo-v1',{json.dumps(S)});localStorage.setItem('bordo-inst-visto','1')}}catch(e){{}}")
    ctx.route('**/vendor/supabase-2.118.0.js',lambda r:r.fulfill(status=200,content_type='application/javascript',body=FAKE))
    ctx.route('**/functions/v1/ia',ia)
    ctx.route('**/functions/v1/avisos',lambda r:r.fulfill(status=200,content_type='application/json',body='{}'))
    pg=ctx.new_page(); pg.goto('http://localhost:8765/nuvem/'); pg.wait_for_timeout(1500)
    print('sobra t1 pelo app:',pg.evaluate("calc(S.trips[0])"))
    pg.screenshot(path=str(OUT/'01-inicio-ia.png'))
    # Lançar falando
    pg.click('[data-a="voz"]'); pg.wait_for_timeout(2200); pg.screenshot(path=str(OUT/'02-ouvindo.png'))
    pg.click('#ouv-ok'); pg.wait_for_timeout(1500); pg.screenshot(path=str(OUT/'03-form-preenchido.png'))
    pg.keyboard.press('Escape'); pg.wait_for_timeout(300)
    pg.goto('http://localhost:8765/nuvem/'); pg.wait_for_timeout(1200)
    # Pergunte ao Diário
    pg.click('[data-a="ia"]'); pg.wait_for_timeout(800); pg.screenshot(path=str(OUT/'04-chat-vazio.png'))
    estado['q']='mes'; pg.click('text=Quanto sobrou este mês?'); pg.wait_for_timeout(1200); pg.screenshot(path=str(OUT/'05-chat-sobrou.png'))
    pg.goto('http://localhost:8765/nuvem/'); pg.wait_for_timeout(1200); pg.evaluate('IA_MSGS.length=0')
    pg.click('[data-a="ia"]'); pg.wait_for_timeout(600)
    estado['q']='frete'; pg.fill('#ia-txt','Um frete de R$ 6.000 para 1.000 km compensa? Volto vazio.'); pg.click('#ia-env'); pg.wait_for_timeout(1200)
    pg.screenshot(path=str(OUT/'06-chat-frete.png'))
    br.close()
srv.terminate(); print('ok')
