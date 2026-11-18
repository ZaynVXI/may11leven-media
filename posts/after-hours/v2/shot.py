import asyncio,os
from playwright.async_api import async_playwright
H=os.path.dirname(os.path.abspath(__file__))
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350})
        await pg.goto('file://'+H+'/slides.html'); await pg.wait_for_timeout(800)
        for s in ['s2','s3','s4','s6','s7','s8']:
            await pg.locator('#'+s).screenshot(path=f'{H}/{s}.png')
        await b.close()
asyncio.run(main())
