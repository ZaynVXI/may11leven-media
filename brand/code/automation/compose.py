"""Composite the recorded chat into the rendered phone, one continuous take with a slow push-in, plus type.
out: /home/claude/autoreel/automation.mp4"""
import json, os, subprocess, numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
D = '/home/claude/autoreel/'; W, H = 1080, 1920; FPS = 30; N = 420
base = np.asarray(Image.open(D + 'f_phone.png').convert('RGB')).astype(np.float32) / 255
C = np.array(json.load(open(D + 'f_phone.png.json')), np.float32)
scr0 = Image.open(D + 'scr/0000.png'); sw, sh = scr0.size
# rounded-corner mask in screen space (radius from the glass bevel: 0.0086 / 0.0669 of width)
rad = int(sw * .0086 / .0669)
mk = Image.new('L', (sw, sh), 0); ImageDraw.Draw(mk).rounded_rectangle((0, 0, sw - 1, sh - 1), radius=rad, fill=255)
mk = np.asarray(mk).astype(np.float32) / 255
Hm = cv2.getPerspectiveTransform(np.float32([[0, 0], [sw, 0], [sw, sh], [0, sh]]), C)
mask = cv2.warpPerspective(mk, Hm, (W, H), flags=cv2.INTER_LINEAR)
mask = cv2.GaussianBlur(mask, (0, 0), .7)[..., None]
inside = base[mask[..., 0] > .9]; dark = np.median(inside, axis=0)   # glass black level -> keep only reflections
refl = np.clip(base - dark, 0, 1)
F = '/home/claude/kit/fonts/'; HK = '/home/claude/fonts-lab/node_modules/@fontsource/hanken-grotesk/files/'
def ttf(p, s):
    return ImageFont.truetype(p, s)
from fontTools.ttLib import TTFont
def woff(p):
    q = '/tmp/claude-0/-home-claude/9bb6ffdd-e2cc-582d-b0a9-f807871f658c/scratchpad/' + os.path.basename(p) + '.ttf'
    if not os.path.exists(q): t = TTFont(p); t.flavor = None; t.save(q)
    return q
IT = F + 'InterTight-Regular.ttf'; PM = '/home/claude/kit/fonts2/PlexMono.ttf'; HKR = woff(HK + 'hanken-grotesk-latin-400-normal.woff2')
INK = (20, 18, 19); ASH = (78, 84, 76); MOSS = (63, 86, 46)
def ez(x): x = min(1, max(0, x)); return 1 - (1 - x) ** 3
def text_layer(t):
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    def put(x, y, s, f, col, a0, a1=None, rise=14):
        k = ez((t - a0) / .7) * (1 - (ez((t - a1) / .4) if a1 else 0))
        if k <= 0: return
        d.text((x, y + (1 - k) * rise), s, font=f, fill=col + (int(255 * k),))
    lab = ttf(PM, 24)
    put(72, 236, 'MAY11LEVEN LABS', lab, ASH, .1);
    tw = d.textlength('AI AUTOMATION', font=lab); put(W - 72 - tw, 236, 'AI AUTOMATION', lab, MOSS, .1)
    h = ttf(IT, 58)
    put(72, 300, 'The clinic closed at 18:00.', h, INK, .2, 11.2)
    put(72, 372, 'This booking came in at 21:47.', h, ASH, 1.3, 11.2)
    put(72, 300, 'Booked, paid, reminded.', h, INK, 11.5)
    put(72, 372, 'Staff take over any time.', h, ASH, 11.8)
    put(72, 470, 'Comment 11 for a free chat flow sketch.', ttf(HKR, 30), INK, 12.2)
    return L
os.makedirs(D + 'fr', exist_ok=True)
cx, cy = C[:, 0].mean(), C[:, 1].mean()
for i in range(N):
    t = i / FPS
    s = np.asarray(Image.open(D + f'scr/{i:04d}.png').convert('RGB')).astype(np.float32) / 255
    s = cv2.GaussianBlur(s, (0, 0), .45)
    warped = cv2.warpPerspective(s, Hm, (W, H), flags=cv2.INTER_AREA)
    img = base * (1 - mask) + np.clip(warped * .94 + refl * .9, 0, 1) * mask
    # slow push-in toward the phone (1.00 -> 1.045), eased
    z = 1 + .045 * (0.5 - 0.5 * np.cos(np.pi * min(1, t / 14)))
    M = np.float32([[z, 0, (1 - z) * cx], [0, z, (1 - z) * (cy - 120)]])
    img = cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    rng = np.random.default_rng(i); img = np.clip(img + rng.normal(0, .006, (H, W, 1)), 0, 1)
    fr = Image.fromarray((img * 255).astype(np.uint8)).convert('RGBA')
    fr = Image.alpha_composite(fr, text_layer(t)).convert('RGB')
    fr.save(D + f'fr/{i:04d}.jpg', quality=93)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', D + 'fr/%04d.jpg', '-i', D + 'reel.wav',
                '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', D + 'automation.mp4'], check=True)
Image.open(D + 'fr/0390.jpg').save(D + 'cover_src.jpg'); print('ok')
