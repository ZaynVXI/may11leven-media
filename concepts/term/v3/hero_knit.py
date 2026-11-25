"""Term hero (v3 screen): the phone lying top-down on a folded maroon school jumper.
The jumper is the uniform colour of the Form 2 card, so the prop and the product share one world.
Knit photo: Unsplash RZrVd3en1Dc (free licence), recoloured from grey-violet to uniform maroon.
Phone body, shadows and light are drawn by us; the screen is phone.html render(t).
The camera breathes in and out (1.000 -> 1.025 -> 1.000) so the 8 s loop closes on its first frame."""
import asyncio, sys, os, math, numpy as np, cv2
from playwright.async_api import async_playwright
H = os.path.dirname(os.path.abspath(__file__))
W, Hh, SS = 1080, 1350, 2
FPS, DUR = 30, 8.0
SW, SH, PAD, R = 432, 964, 13, 39          # screen size, bezel, outer radius = screen radius 26 + bezel 13
K = 0.86                                   # phone scale in the frame: leaves knit around it
CX, CY, ANG = 540, 680, -6.0               # phone centre and rotation (degrees)

def quad(w, h):
    """corners of a w x h rectangle centred on the phone, rotated, at SS scale"""
    a = math.radians(ANG); ca, sa = math.cos(a), math.sin(a)
    pts = []
    for x, y in [(-w/2, -h/2), (w/2, -h/2), (w/2, h/2), (-w/2, h/2)]:
        pts.append([(CX + K*(x*ca - y*sa))*SS, (CY + K*(x*sa + y*ca))*SS])
    return np.float32(pts)

def rrect(w, h, r, k=4):
    can = np.zeros((h*k, w*k), np.uint8); r *= k
    cv2.rectangle(can, (r, 0), (w*k-1-r, h*k-1), 255, -1)
    cv2.rectangle(can, (0, r), (w*k-1, h*k-1-r), 255, -1)
    for cx, cy in [(r, r), (w*k-1-r, r), (r, h*k-1-r), (w*k-1-r, h*k-1-r)]:
        cv2.circle(can, (cx, cy), r, 255, -1)
    return can

def warp(img, w, h, k=4, dst=None):
    src = np.float32([[0, 0], [w*k, 0], [w*k, h*k], [0, h*k]])
    M = cv2.getPerspectiveTransform(src, dst if dst is not None else quad(w, h))
    return cv2.warpPerspective(img, M, (W*SS, Hh*SS), flags=cv2.INTER_LINEAR)

# --- the set: knit, window light from the top left
knit = cv2.resize(cv2.imread(H + '/../img/knit_maroon.jpg'), (W*SS, Hh*SS), interpolation=cv2.INTER_AREA).astype(np.float32)/255
yy, xx = np.mgrid[0:Hh*SS, 0:W*SS].astype(np.float32)/SS
d = np.sqrt(((xx+120)/1500)**2 + ((yy+160)/1650)**2)
light = (1.18 - 0.62*np.clip(d, 0, 1.2))                               # bright corner, falls off to the bottom right
light *= 1 - 0.28*np.clip(np.sqrt(((xx-540)/760)**2 + ((yy-675)/900)**2) - 0.55, 0, 1)   # soft vignette
SET = np.clip(knit*light[..., None]*np.array([0.97, 0.99, 1.04]), 0, 1)  # a touch warm

# --- phone body (outer), screen area, shadows
OW, OH = SW + 2*PAD, SH + 2*PAD
body = warp(rrect(OW, OH, R), OW, OH).astype(np.float32)/255
inner = warp(rrect(OW-4, OH-4, R-2), OW-4, OH-4).astype(np.float32)/255
edge = np.clip(body - inner, 0, 1)                                     # thin metal band
# light hits the top-left edges of the band
gx, gy = (xx - CX), (yy - CY)
facing = np.clip(-(gx*0.6 + gy*0.8)/600, 0, 1)
BODYCOL = np.array([0.060, 0.058, 0.062])[None, None] + edge[..., None]*(0.10 + 0.40*facing[..., None])*np.array([0.85, 0.88, 0.95])
def shadow(dx, dy, blur, grow):
    s = warp(rrect(OW+grow, OH+grow, R+grow//2), OW+grow, OH+grow)
    M = np.float32([[1, 0, dx*K*SS], [0, 1, dy*K*SS]])
    s = cv2.warpAffine(s, M, (W*SS, Hh*SS)).astype(np.float32)/255
    return cv2.GaussianBlur(s, (0, 0), blur*SS)
SHADOW = 1 - (0.62*shadow(4, 6, 5, 0) + 0.48*shadow(30, 44, 34, 10))   # contact + window shadow
SHADOW = np.clip(SHADOW, 0.18, 1)
# fibres poke up around the phone edge: a few pixels of knit drawn over the frame where it is bright
fib = cv2.GaussianBlur(cv2.cvtColor((knit*255).astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32)/255, (0, 0), 0.6)
halo = np.clip(cv2.dilate(body, np.ones((5, 5), np.uint8)) - cv2.erode(body, np.ones((3, 3), np.uint8)), 0, 1)
FIB = np.clip((fib - 0.32)*4, 0, 1)*halo*0.55

# screen glare: one soft diagonal band, very faint
SQ = quad(SW, SH)
GL = np.clip(1 - np.abs((xx - CX)*0.75 + (yy - CY)*0.66 + 260)/170, 0, 1)*0.05

def comp(scr):
    out = SET*SHADOW[..., None]
    out = out*(1 - body[..., None]) + BODYCOL*body[..., None]
    h, w = scr.shape[:2]
    M = cv2.getPerspectiveTransform(np.float32([[0, 0], [w, 0], [w, h], [0, h]]), SQ)
    wp = cv2.warpPerspective(scr, M, (W*SS, Hh*SS), flags=cv2.INTER_LINEAR, borderValue=(0, 0, 0, 0)).astype(np.float32)/255
    a = wp[..., 3:4]; col = wp[..., :3]*0.96 + GL[..., None]*np.array([0.9, 0.95, 1.0])
    out = out*(1 - a) + col*a
    out = out*(1 - FIB[..., None]) + SET*FIB[..., None]
    return out

def camera(img, t):
    s = 1 + 0.025*(1 - math.cos(2*math.pi*t/DUR))/2
    M = cv2.getRotationMatrix2D((CX*SS, CY*SS), 0, s)
    img = cv2.warpAffine(img, M, (W*SS, Hh*SS), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    return cv2.resize(img, (W, Hh), interpolation=cv2.INTER_AREA)

async def main():
    rng = np.random.default_rng(7)
    only = [float(a) for a in sys.argv[1:]]
    od = H + '/frames_knit'; os.makedirs(od, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': SW, 'height': SH}, device_scale_factor=3)
        await pg.goto('file://' + H + '/phone.html'); await pg.wait_for_timeout(600)
        ts = only or [i/FPS for i in range(int(FPS*DUR))]
        for i, t in enumerate(ts):
            await pg.evaluate(f'render({t})')
            scr = cv2.imdecode(np.frombuffer(await pg.screenshot(omit_background=True, type='png'), np.uint8), cv2.IMREAD_UNCHANGED)
            out = np.clip(camera(comp(scr), t) + rng.normal(0, 0.010, (Hh, W))[..., None], 0, 1)
            cv2.imwrite(od + '/' + (f'still_{t:.2f}.png' if only else f'f{i:04d}.png'), (out*255).astype(np.uint8))
        await b.close()
asyncio.run(main())
