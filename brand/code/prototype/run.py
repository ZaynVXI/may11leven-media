from playwright.sync_api import sync_playwright
import time
def tap(pg,sel,hold=0.12):
    box=pg.locator(sel).bounding_box();x=box['x']+box['width']/2;y=box['y']+box['height']/2
    pg.evaluate(f"""()=>{{const t=document.getElementById('tap');t.style.left='{x/3}px';t.style.top='{y/3}px';t.classList.remove('go');void t.offsetWidth;t.classList.add('go')}}""")
    pg.evaluate(f"document.querySelector('{sel}').classList.add('p')"); time.sleep(hold); pg.evaluate(f"document.querySelector('{sel}').classList.remove('p')")
def js(pg,s): pg.evaluate(s)
with sync_playwright() as p:
    b=p.chromium.launch(); ctx=b.new_context(viewport={'width':1170,'height':2532},record_video_dir='vid',record_video_size={'width':1170,'height':2532})
    pg=ctx.new_page(); pg.goto('file:///home/claude/kivu/proto/book.html'); time.sleep(2.2)
    tap(pg,'#cta'); time.sleep(0.15); js(pg,"document.getElementById('sheet').classList.add('on');document.getElementById('s1').classList.add('d')"); time.sleep(1.4)
    tap(pg,'#d12'); js(pg,"d12.classList.add('s')"); time.sleep(0.6)
    tap(pg,'#d14'); js(pg,"d14.classList.add('s');d13.classList.add('r')"); time.sleep(1.0)
    tap(pg,'#btn'); js(pg,"p1.classList.add('out');p2.classList.remove('in');s2.classList.add('d')"); time.sleep(1.3)
    tap(pg,'#r1'); js(pg,"r1.classList.add('sel')"); time.sleep(1.1)
    tap(pg,'#btn'); js(pg,"p2.classList.add('out');p3.classList.remove('in');s3.classList.add('d');bl.textContent='Confirm · $480'"); time.sleep(1.2)
    tap(pg,'#py1'); js(pg,"py2.classList.remove('sel');py1.classList.add('sel')"); time.sleep(1.0)
    tap(pg,'#btn'); time.sleep(0.2); js(pg,"done.classList.add('on')"); time.sleep(3.0)
    v=pg.video.path(); ctx.close(); b.close(); print(v)
