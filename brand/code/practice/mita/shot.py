import sys
from playwright.sync_api import sync_playwright
src,out=sys.argv[1],sys.argv[2]
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    pg.goto('file://'+__import__('os').path.abspath(src));pg.wait_for_timeout(600)
    pg.screenshot(path=out);b.close()
