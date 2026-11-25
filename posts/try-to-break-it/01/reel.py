"""Try to break it No. 01 reel: renders reel.html frame by frame (render(t)), loop crossfade to frame 0."""
import asyncio, os, sys, numpy as np, cv2
from playwright.async_api import async_playwright
H=os.path.dirname(os.path.abspath(__file__)); FPS=30; DUR=31.0; LOOP=0.5
od=H+'/frames_reel'; os.makedirs(od,exist_ok=True)
async def main():
    only=[float(a) for a in sys.argv[1:]]
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':1080,'height':1920}); await pg.goto('file://'+H+'/reel.html'); await pg.wait_for_timeout(900)
        async def frame(t):
            await pg.evaluate(f'render({t})'); buf=await pg.screenshot()
            return cv2.imdecode(np.frombuffer(buf,np.uint8),cv2.IMREAD_COLOR)
        first=await frame(0.0)
        ts=only or [i/FPS for i in range(int(FPS*DUR))]
        for i,t in enumerate(ts):
            im=await frame(t)
            if t>DUR-LOOP: a=(t-(DUR-LOOP))/LOOP; im=cv2.addWeighted(im,1-a,first,a,0)
            cv2.imwrite(f'{od}/'+(f'still_{t:.2f}.png' if only else f'f{i:04d}.png'),im)
        await b.close()
asyncio.run(main())
