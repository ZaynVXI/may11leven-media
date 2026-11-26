import sys,os
from playwright.sync_api import sync_playwright
src,out=sys.argv[1],sys.argv[2]
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=1)
    pg.goto('file://'+os.path.abspath(src));pg.wait_for_timeout(800)
    pg.screenshot(path=out,type='jpeg',quality=92);b.close()
