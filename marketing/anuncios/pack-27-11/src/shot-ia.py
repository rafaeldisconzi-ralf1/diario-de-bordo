import pathlib
from playwright.sync_api import sync_playwright
here=pathlib.Path(__file__).parent.resolve(); out=here.parent/'imagens'
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    for f,h in [('45',1350),('916',1920)]:
        tag="4x5" if f=="45" else "9x16"
        pg=b.new_page(viewport={'width':1080,'height':h})
        for n,k in [('ia1','fala'),('ia2','frete'),('ia3','sobrou')]:
            pg.goto((here/'ia.html').as_uri()+f'?id={k}&f={f}'); pg.wait_for_timeout(900)
            pg.screenshot(path=str(out/f'{n}-{k}-{tag}.jpg'),type='jpeg',quality=92)
    b.close()
