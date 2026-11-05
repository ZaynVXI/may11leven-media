import asyncio
from playwright.async_api import async_playwright
FPS=30; DUR=14.0
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':390,'height':844},device_scale_factor=2.5)
    await pg.goto('file:///home/claude/autoreel/chat_anim.html'); await pg.wait_for_timeout(400)
    import os; os.makedirs('/home/claude/autoreel/scr',exist_ok=True)
    for i in range(int(FPS*DUR)):
      await pg.evaluate(f'setT({i/FPS})'); await pg.screenshot(path=f'/home/claude/autoreel/scr/{i:04d}.png')
    await b.close()
asyncio.run(m()); print('ok')
