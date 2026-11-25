import asyncio,os
from playwright.async_api import async_playwright
H=os.path.dirname(os.path.abspath(__file__))
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350})
        await pg.goto(f'file://{H}/slides.html'); await pg.wait_for_timeout(900)
        for i in [2,3,5,6,8]:
            await (await pg.query_selector(f'#s{i}')).screenshot(path=f'{H}/s{i}.png')
        await b.close()
asyncio.run(main())
