import sys,os
from playwright.sync_api import sync_playwright
src,out=sys.argv[1],sys.argv[2]
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1440,'height':1024},device_scale_factor=float(sys.argv[3]) if len(sys.argv)>3 else 1)
    pg.goto('file://'+os.path.abspath(src));pg.wait_for_timeout(800)
    pg.screenshot(path=out);b.close()
