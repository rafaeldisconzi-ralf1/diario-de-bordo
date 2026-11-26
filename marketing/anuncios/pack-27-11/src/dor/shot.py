import asyncio,sys,pathlib
from playwright.async_api import async_playwright
D=pathlib.Path(__file__).parent
NOMES={'1':'dono-sobrou','2':'patrao-acerto','3':'caderninho'}
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch();pg=await b.new_page(viewport={'width':1080,'height':1920})
    for v in sys.argv[1:] or ['1','2','3']:
      for f,h in (('916',1920),('45',1350)):
        await pg.set_viewport_size({'width':1080,'height':h})
        await pg.goto(f'file://{D}/arte.html?v={v}&f={f}');await pg.wait_for_timeout(700)
        out=D.parent/f'arte{v}-{NOMES[v]}-{"9x16" if f=="916" else "4x5"}.jpg'
        await pg.locator('#c').screenshot(path=str(out),type='jpeg',quality=92);print(out.name)
    await b.close()
asyncio.run(main())
