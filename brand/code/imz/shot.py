from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch()
    for id_,w,h,s in (('dh',1440,900,2),('ds',1440,900,2),('mp',390,844,3),('mb',390,844,3)):
        pg=b.new_page(viewport={'width':w,'height':h},device_scale_factor=s)
        pg.goto(f'file:///home/claude/imz/site.html#{id_}');pg.wait_for_timeout(600);pg.screenshot(path=f'/home/claude/imz/{id_}.png');pg.close()
    b.close()
