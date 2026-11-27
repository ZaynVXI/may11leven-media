import os,subprocess,sys
from playwright.sync_api import sync_playwright
src=os.path.abspath('after.html'); out=sys.argv[1]; d='/tmp/claude-0/frames'; os.makedirs(d,exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
    pg.goto('file://'+src); pg.wait_for_timeout(500)
    for i in range(240):
        pg.evaluate(f'render({i/30})'); pg.screenshot(path=f'{d}/{i:04d}.png')
    b.close()
subprocess.run(['ffmpeg','-v','error','-y','-framerate','30','-i',f'{d}/%04d.png','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',out],check=True)
