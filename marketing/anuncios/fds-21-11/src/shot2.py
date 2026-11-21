import pathlib
from playwright.sync_api import sync_playwright
here=pathlib.Path(__file__).parent.resolve(); out=here.parent/'imagens'
for f in out.glob('*.png'): f.unlink()
ids=['sobrou','papel','toque','preco','diaria','depo']
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--allow-file-access-from-files'])
    for f,h in [('45',1350),('916',1920)]:
        pg=b.new_page(viewport={'width':1080,'height':h})
        for i,k in enumerate(ids,1):
            pg.goto((here/'foto.html').as_uri()+f'?id={k}&f={f}'); pg.wait_for_timeout(600)
            pg.screenshot(path=str(out/f'img{i}-{k}-{"4x5" if f=="45" else "9x16"}.jpg'),type='jpeg',quality=92)
    b.close()
