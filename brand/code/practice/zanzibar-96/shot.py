import sys
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=float(sys.argv[3]) if len(sys.argv)>3 else 1)
    pg.goto('file://'+sys.argv[1]);pg.wait_for_timeout(300);pg.screenshot(path=sys.argv[2],type='jpeg',quality=92);b.close()
