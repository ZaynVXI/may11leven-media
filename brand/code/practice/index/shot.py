import sys,asyncio
from playwright.async_api import async_playwright
async def m(src,out,sc):
    async with async_playwright() as p:
        b=await p.chromium.launch();pg=await b.new_page(viewport={'width':1440,'height':900},device_scale_factor=sc)
        await pg.goto('file://'+src);await pg.wait_for_timeout(400);await pg.screenshot(path=out,type='jpeg',quality=90);await b.close()
asyncio.run(m(sys.argv[1],sys.argv[2],float(sys.argv[3])))
