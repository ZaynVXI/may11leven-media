import sys,os
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch()
    for src in sys.argv[1:]:
        pg=b.new_page(viewport={'width':470,'height':924},device_scale_factor=3)
        pg.goto('file://'+os.path.abspath(src));pg.wait_for_timeout(1500)
        pg.screenshot(path=src.replace('.html','.png'));pg.close()
    b.close()
