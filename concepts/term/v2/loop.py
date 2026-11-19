import asyncio,os,sys
from playwright.async_api import async_playwright
H=os.path.dirname(os.path.abspath(__file__))
page,out,dur=sys.argv[1],sys.argv[2],float(sys.argv[3]); only=[float(x) for x in sys.argv[4:]]
os.makedirs(H+'/'+out,exist_ok=True)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350})
        await pg.goto('file://'+H+'/'+page); await pg.wait_for_timeout(600)
        ts=only or [i/30 for i in range(int(dur*30))]
        for i,t in enumerate(ts):
            await pg.evaluate(f'render({t})')
            await pg.screenshot(path=f'{H}/{out}/'+(f't{t:.2f}.png' if only else f'f{i:04d}.png'))
        await b.close()
asyncio.run(main())
