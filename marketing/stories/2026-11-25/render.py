import sys,os
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    for n in ['story1-enquete','story2-app']:
        pg.goto('file://'+os.path.abspath(n+'.html')); pg.wait_for_timeout(600)
        pg.screenshot(path=n+'.png')
    b.close()
