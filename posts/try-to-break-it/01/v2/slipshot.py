import asyncio,os
from playwright.async_api import async_playwright
H=os.path.dirname(os.path.abspath(__file__))
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':640,'height':800},device_scale_factor=2)
        for v in ['cousin','deal','code','shot','down']:
            await pg.goto(f'file://{H}/slip.html?v={v}'); await pg.wait_for_timeout(400)
            await pg.screenshot(path=f'{H}/slip_{v}.png',full_page=True)
        await b.close()
asyncio.run(main())
