import sys, subprocess, pathlib
from playwright.sync_api import sync_playwright
here = pathlib.Path(__file__).parent.resolve()
mode = sys.argv[1] if len(sys.argv) > 1 else 'video'
FPS = 30
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--allow-file-access-from-files'])
    pg = b.new_page(viewport={'width': 1080, 'height': 1920})
    pg.goto((here / 'index.html').as_uri())
    pg.wait_for_timeout(800)
    tot = pg.evaluate('TOT')
    if mode == 'stills':
        ts = [float(x) for x in sys.argv[2:]]
        n = int(max(ts) * FPS) + 1
        for f in range(n):
            t = f / FPS
            pg.evaluate(f'render({t})')
            for s in ts:
                if abs(t - s) < 0.5 / FPS:
                    pg.screenshot(path=str(here / f'still_{s:05.2f}.png'))
    else:
        ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'image2pipe', '-framerate', str(FPS), '-i', '-',
                               '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p',
                               str(here / 'video.mp4')], stdin=subprocess.PIPE)
        for f in range(int(tot * FPS)):
            pg.evaluate(f'render({f / FPS})')
            ff.stdin.write(pg.screenshot(type='jpeg', quality=92))
        ff.stdin.close(); ff.wait()
    b.close()
