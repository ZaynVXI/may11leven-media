import sys, pathlib
from playwright.sync_api import sync_playwright
here = pathlib.Path(__file__).parent.resolve()
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=1)
    pg.goto((here / 'slides.html').as_uri()); pg.wait_for_timeout(800)
    for i in range(1, 7):
        pg.locator(f'#s{i}').screenshot(path=str(here / f'p{i}.png'))
    b.close()
