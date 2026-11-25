import asyncio,os
from playwright.async_api import async_playwright
H=os.path.dirname(os.path.abspath(__file__))
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1400,'height':2000},device_scale_factor=3)
        await pg.goto(f'file://{H}/screens.html'); await pg.wait_for_timeout(600)
        for i in ['chat','pay','console']:
            await (await pg.query_selector('#'+i)).screenshot(path=f'{H}/scr_{i}.png')
        await b.close()
asyncio.run(main())
