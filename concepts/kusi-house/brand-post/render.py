import asyncio, sys
from playwright.async_api import async_playwright
from PIL import Image
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
        import pathlib; await pg.goto(pathlib.Path('slides.html').resolve().as_uri()); await pg.wait_for_timeout(800)
        for i in range(1,9):
            el=await pg.query_selector(f'#s{i}'); f=f'raw{i}.png'; await el.screenshot(path=f)
            Image.open(f).convert('RGB').resize((1080,1350),Image.LANCZOS).save(f'post/kusi_brand_{i}.jpg',quality=93)
        await b.close()
asyncio.run(main())
