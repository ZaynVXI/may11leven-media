import asyncio,os,sys
from playwright.async_api import async_playwright
H=os.path.dirname(os.path.abspath(__file__)); FPS=30; D=7.2
async def main():
    od=H+'/frames_tick'; os.makedirs(od,exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350})
        await pg.goto('file://'+H+'/tick.html'); await pg.wait_for_timeout(700)
        ts=[float(a) for a in sys.argv[1:]] or [i/FPS for i in range(int(FPS*D))]
        for i,t in enumerate(ts):
            await pg.evaluate(f'render({t})'); await pg.screenshot(path=f'{od}/'+(f'still_{t}.png' if len(sys.argv)>1 else f'f{i:04d}.png'))
        await b.close()
asyncio.run(main())
