import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width':1080,'height':1350}, device_scale_factor=1)
        await pg.goto('file://' + __import__('os').path.abspath('slides.html'))
        await pg.wait_for_timeout(800)
        for i in range(1,9):
            el = await pg.query_selector(f'#s{i}')
            await el.screenshot(path=f's{i}.jpg', type='jpeg', quality=93)
        # overflow check: any text element wider than its slide
        bad = await pg.evaluate('''()=>{const o=[];document.querySelectorAll('section').forEach(s=>{const r=s.getBoundingClientRect();s.querySelectorAll('*').forEach(e=>{const q=e.getBoundingClientRect();if(q.width&&(q.right>r.right-40||q.left<r.left+40||q.bottom>r.bottom-30)&&e.children.length==0)o.push(s.id+' '+e.tagName+' '+(e.textContent||'').slice(0,30)+' R'+Math.round(q.right-r.left)+' B'+Math.round(q.bottom-r.top))})});return o}''')
        print('\n'.join(bad))
        await b.close()
asyncio.run(main())
