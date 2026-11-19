"""Hero v2b: silhouette hand (Zayn's note on the PXDX style) in front of a Lamu-door arch of warm light.
Hand and phone cut from the free Unsplash photo (David Monje, UjFMiozp51E) with GrabCut, then turned to a silhouette."""
import asyncio,sys,os,numpy as np,cv2
from playwright.async_api import async_playwright
H=os.path.dirname(os.path.abspath(__file__))
x0,y0,x1,y1=510,1020,1810,2645; S=1080/1300; W,Hh=1080,1350; SS=2
src=cv2.imread(H+'/../../../posts/after-hours/img/hand_dusk_full.jpg')[y0:y1,x0:x1]
src=cv2.resize(src,(W*SS,Hh*SS),interpolation=cv2.INTER_AREA).astype(np.float32)/255
m=cv2.resize(cv2.imread(H+'/../../../posts/after-hours/v2/sil_mask.png',0),(W*SS,Hh*SS),interpolation=cv2.INTER_LINEAR).astype(np.float32)/255
corn=(np.float32([[920,1298],[1411,1294],[1400,2360],[920,2370]])-[x0,y0])*S
FPS,DUR=30,8.0
def background():
    yy,xx=np.mgrid[0:Hh*SS,0:W*SS].astype(np.float32)/SS
    t=yy/Hh
    top=np.array([0.17,0.15,0.14]);bot=np.array([0.05,0.045,0.045])   # BGR graphite to near black
    bg=(top*(1-t[...,None])+bot*t[...,None])
    # an exercise-book page of light behind the phone: rounded, ruled, with a margin line
    x0,x1,y0,r=200,912,120,56
    page=np.zeros((Hh*SS,W*SS),np.float32)
    cv2.rectangle(page,(int((x0+r)*SS),int(y0*SS)),(int((x1-r)*SS),Hh*SS),1,-1)
    cv2.rectangle(page,(int(x0*SS),int((y0+r)*SS)),(int(x1*SS),Hh*SS),1,-1)
    for cx in (x0+r,x1-r): cv2.circle(page,(int(cx*SS),int((y0+r)*SS)),int(r*SS),1,-1)
    page=cv2.GaussianBlur(page,(0,0),2.0*SS)
    paper=np.array([0.80,0.89,0.93])                                   # chalk paper, BGR
    d=np.sqrt(((xx-556)/420)**2+((yy-600)/700)**2)
    light=paper*(1-0.22*np.clip(d,0,1))[...,None]
    light=light*(1-0.55*np.clip((yy-900)/450,0,1))[...,None]
    rules=((yy-y0)%34<1.3)&(yy>y0+90)
    light=np.where(rules[...,None],light*np.array([0.93,0.9,0.86]),light)      # faint blue-grey rules
    margin=(np.abs(xx-(x0+96))<1.0)&(yy>y0+20)
    light=np.where(margin[...,None],light*np.array([0.78,0.78,0.95]),light)     # red margin line
    return bg*(1-page[...,None])+light*page[...,None], page
BG,ARCH=background()
def silhouette():
    lum=cv2.cvtColor((src*255).astype(np.uint8),cv2.COLOR_BGR2GRAY).astype(np.float32)/255
    base=np.array([0.055,0.05,0.047])+0.05*lum[...,None]          # near black with a trace of skin texture
    # rim light where the silhouette edge meets the bright arch
    er=cv2.erode(m,np.ones((5*SS,5*SS),np.uint8))
    edge=np.clip(m-er,0,1); edge=cv2.GaussianBlur(edge,(0,0),1.5*SS)
    lit=cv2.erode(ARCH,np.ones((9*SS,9*SS),np.uint8))     # only where bright light sits right behind
    rim=(edge*lit*0.22)[...,None]*np.array([0.62,0.74,0.86])
    return np.clip(base+rim,0,1)
SIL=silhouette()
# phone body drawn in screen space (rounded, 10px bezel, radius 36) and warped with the screen homography
def phone_body():
    sw,sh=432,964; k=4; pad=10
    can=np.zeros(((sh+2*pad)*k,(sw+2*pad)*k),np.uint8)
    r=36*k; x0b,y0b,x1b,y1b=0,0,(sw+2*pad)*k-1,(sh+2*pad)*k-1
    cv2.rectangle(can,(x0b+r,y0b),(x1b-r,y1b),255,-1); cv2.rectangle(can,(x0b,y0b+r),(x1b,y1b-r),255,-1)
    for cx,cy in [(x0b+r,y0b+r),(x1b-r,y0b+r),(x0b+r,y1b-r),(x1b-r,y1b-r)]: cv2.circle(can,(cx,cy),r,255,-1)
    src_q=np.float32([[pad*k,pad*k],[(sw+pad)*k,pad*k],[(sw+pad)*k,(sh+pad)*k],[pad*k,(sh+pad)*k]])
    M=cv2.getPerspectiveTransform(src_q,(corn*SS).astype(np.float32))
    body=cv2.warpPerspective(can,M,(W*SS,Hh*SS),flags=cv2.INTER_LINEAR).astype(np.float32)/255
    ring=np.clip(body-cv2.erode(body,np.ones((3*SS,3*SS),np.uint8)),0,1)
    return body,ring
BODY,RING=phone_body()
def comp(scr):
    mm=np.clip(m,0,1)
    out=BG*(1-mm[...,None])+SIL*mm[...,None]
    bodycol=np.array([0.07,0.065,0.065])+RING[...,None]*np.array([0.20,0.20,0.21])   # dark frame, thin metal edge
    out=out*(1-BODY[...,None])+bodycol*BODY[...,None]
    h,w=scr.shape[:2]
    M=cv2.getPerspectiveTransform(np.float32([[0,0],[w,0],[w,h],[0,h]]),(corn*SS).astype(np.float32))
    wp=cv2.warpPerspective(scr,M,(W*SS,Hh*SS),flags=cv2.INTER_LINEAR,borderValue=(0,0,0,0)).astype(np.float32)/255
    a=wp[...,3:4]; col=wp[...,:3]*np.array([0.98,0.97,0.96])*0.95
    out=out*(1-a)+col*a
    out=cv2.resize(out,(W,Hh),interpolation=cv2.INTER_AREA)
    return out
async def main():
    rng=np.random.default_rng(7)
    only=[float(a) for a in sys.argv[1:]]
    od=H+'/frames_sil'; os.makedirs(od,exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':432,'height':964},device_scale_factor=3)
        await pg.goto('file://'+H+'/phone.html'); await pg.wait_for_timeout(600)
        ts=only or [i/FPS for i in range(int(FPS*DUR))]
        for i,t in enumerate(ts):
            await pg.evaluate(f'render({t})')
            scr=cv2.imdecode(np.frombuffer(await pg.screenshot(omit_background=True,type='png'),np.uint8),cv2.IMREAD_UNCHANGED)
            out=np.clip(comp(scr)+rng.normal(0,0.011,(Hh,W))[...,None],0,1)
            cv2.imwrite(od+'/'+(f'still_{t:.2f}.png' if only else f'f{i:04d}.png'),(out*255).astype(np.uint8))
        await b.close()
asyncio.run(main())
