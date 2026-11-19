"""Hero loop: Kusi House chat composited into a free Unsplash photo (David Monje, UjFMiozp51E).
Screen corners measured at 4x zoom on the 2400x3600 source."""
import asyncio, sys, os, numpy as np, cv2, subprocess
from playwright.async_api import async_playwright
HERE=os.path.dirname(os.path.abspath(__file__))
SRC=os.path.join(HERE,'../img/hand_dusk_full.jpg')
CROP=(510,1020,1810,2645)          # 1300x1625 -> 1080x1350
S=1080/1300
corners_src=np.float32([[920,1298],[1411,1294],[1400,2360],[920,2370]])
dst=(corners_src-np.float32([CROP[0],CROP[1]]))*S
FPS,DUR=30,8.0
OUT=os.path.join(HERE,'frames_hero'); os.makedirs(OUT,exist_ok=True)
SS=2  # supersample the warp
def base():
    im=cv2.imread(SRC)[CROP[1]:CROP[3],CROP[0]:CROP[2]]
    im=cv2.resize(im,(1080*SS,1350*SS),interpolation=cv2.INTER_AREA)
    # night grade: cooler, darker, lifted blacks slightly
    f=im.astype(np.float32)/255
    f=f*np.array([1.02,0.93,0.86])*0.82   # BGR: keep blue, pull red/green a little
    f=np.clip(f,0,1)
    return f
def comp(bg,scr_rgba):
    h,w=scr_rgba.shape[:2]
    M=cv2.getPerspectiveTransform(np.float32([[0,0],[w,0],[w,h],[0,h]]),dst*SS)
    warped=cv2.warpPerspective(scr_rgba,M,(1080*SS,1350*SS),flags=cv2.INTER_LINEAR,borderValue=(0,0,0,0)).astype(np.float32)/255
    a=warped[...,3:4]
    col=warped[...,:3]
    # screen in the photo: a touch cooler and dimmer than the raw UI, plus a soft sheen
    col=col*np.array([1.0,0.97,0.94])*0.93
    yy,xx=np.mgrid[0:1350*SS,0:1080*SS].astype(np.float32)
    sheen=np.clip(1-((xx-dst[0,0]*SS)/(400*SS)+(yy-dst[0,1]*SS)/(900*SS)),0,1)[...,None]*0.07
    col=np.clip(col+sheen,0,1)
    out=bg*(1-a)+col*a
    return out
async def main():
    bg=base()
    rng=np.random.default_rng(11)
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':432,'height':964},device_scale_factor=3)
        await pg.goto('file://'+os.path.join(HERE,'phone.html')); await pg.wait_for_timeout(600)
        n=int(FPS*DUR)
        only=[float(a) for a in sys.argv[1:]]
        ts=[x for x in only] if only else [i/FPS for i in range(n)]
        for i,t in enumerate(ts):
            await pg.evaluate(f'render({t})')
            png=await pg.screenshot(omit_background=True,type='png')
            scr=cv2.imdecode(np.frombuffer(png,np.uint8),cv2.IMREAD_UNCHANGED)
            out=comp(bg,scr)
            out=cv2.resize(out,(1080,1350),interpolation=cv2.INTER_AREA)
            out=np.clip(out+rng.normal(0,0.012,out.shape[:2])[...,None],0,1)  # film grain
            name=f'still_{t:.2f}.png' if only else f'f{i:04d}.png'
            cv2.imwrite(os.path.join(OUT,name),(out*255).astype(np.uint8))
        await b.close()
asyncio.run(main())
