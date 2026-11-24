"""Term reel: renders reel.html for paper scenes, and composites the knit hero (C) and the tick loop (D)."""
import asyncio, os, sys, numpy as np, cv2
from playwright.async_api import async_playwright
H=os.path.dirname(os.path.abspath(__file__)); FPS=30; DUR=27.4
C=(5.2,9.6); D=(9.6,14.0); LOOP=0.4
od=H+'/frames_reel'; os.makedirs(od,exist_ok=True)
def hero(th):
    i=min(239,int(round(th*FPS))); im=cv2.imread(f'{H}/frames_knit/f{i:04d}.png')
    im=cv2.resize(im,(1536,1920),interpolation=cv2.INTER_CUBIC); return im[:,228:228+1080]
async def main():
    only=[float(a) for a in sys.argv[1:]]
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pr=await b.new_page(viewport={'width':1080,'height':1920}); await pr.goto('file://'+H+'/reel.html'); await pr.wait_for_timeout(900)
        pt=await b.new_page(viewport={'width':1080,'height':1920}); await pt.goto('file://'+H+'/tick.html'); await pt.wait_for_timeout(700)
        await pt.add_style_tag(content='#c{transform:translateY(250px) scale(1.12);transform-origin:50% 0} .lab{transform:translateY(120px)} body{height:1920px}')
        async def frame(t):
            if C[0]<=t<C[1]: return hero(.6+(t-C[0]))
            if D[0]<=t<D[1]:
                await pt.evaluate(f'render({.8+(t-D[0])})'); buf=await pt.screenshot()
            else:
                await pr.evaluate(f'render({t})'); buf=await pr.screenshot()
            return cv2.imdecode(np.frombuffer(buf,np.uint8),cv2.IMREAD_COLOR)
        first=await frame(0.0)
        ts=only or [i/FPS for i in range(int(FPS*DUR))]
        for i,t in enumerate(ts):
            im=await frame(t)
            if t>DUR-LOOP: a=(t-(DUR-LOOP))/LOOP; im=cv2.addWeighted(im,1-a,first,a,0)
            cv2.imwrite(f'{od}/'+(f'still_{t:.2f}.png' if only else f'f{i:04d}.png'),im)
        await b.close()
asyncio.run(main())
