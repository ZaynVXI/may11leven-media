from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':390,'height':824},device_scale_factor=3)
    pg.goto('file:///home/claude/remake/hifi/app.html');pg.wait_for_timeout(500)
    for i in (1,2,3):
        pg.evaluate(f"document.querySelectorAll('.scr').forEach(e=>e.classList.remove('on'));s{i}.classList.add('on')")
        pg.wait_for_timeout(200);pg.screenshot(path=f's{i}.png')
    b.close()
