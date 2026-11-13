import sys, subprocess, pathlib, time
from playwright.sync_api import sync_playwright
here = pathlib.Path(__file__).parent.resolve()
mode = sys.argv[1] if len(sys.argv) > 1 else 'video'
FPS = 30
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--allow-file-access-from-files', '--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'])
    pg = b.new_page(viewport={'width': 1080, 'height': 1920})
    pg.on('pageerror', lambda e: print('ERR', e))
    pg.goto((here / 'index.html').as_uri())
    pg.wait_for_function('window.__ready===true', timeout=60000)
    tot = pg.evaluate('TOT')
    if mode == 'stills':
        for s in sys.argv[2:]:
            pg.evaluate(f'render({float(s)})'); pg.screenshot(path=str(here / f'still_{float(s):05.2f}.png'))
    else:
        ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'image2pipe', '-framerate', str(FPS), '-i', '-',
                               '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', str(here / 'video.mp4')], stdin=subprocess.PIPE)
        t0 = time.time(); N = int(tot * FPS)
        for f in range(N):
            pg.evaluate(f'render({f / FPS})')
            ff.stdin.write(pg.screenshot(type='jpeg', quality=92))
            if f % 300 == 0: print(f, N, round(time.time() - t0), flush=True)
        ff.stdin.close(); ff.wait()
    b.close()
