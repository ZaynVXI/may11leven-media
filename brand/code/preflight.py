"""May11Leven preflight. Usage: python3 preflight.py --caption caption.txt slide1.jpg slide2.jpg ...
Writes qa_report.txt and qa_zoom_<n>.jpg (100% crops) for a human-eye pass. Exit code 1 if any hard FAIL."""
import sys,re,os,argparse
from PIL import Image
import numpy as np
ap=argparse.ArgumentParser();ap.add_argument('--caption');ap.add_argument('--out',default='qa');ap.add_argument('files',nargs='+');a=ap.parse_args()
os.makedirs(a.out,exist_ok=True);R=[];fail=False
def rep(level,msg):
    global fail; R.append(f'{level}: {msg}'); fail|=(level=='FAIL')
try:
    import pytesseract; from spellchecker import SpellChecker; sp=SpellChecker(); 
    sp.word_frequency.load_words(['may11leven','inzu','kivu','karongi','rubavu','westlands','mpesa','m-pesa','momo','kes','instagram','dms','ai','ui','ux','logofolio','nairobi','kigali','johannesburg','lagos','abuja','dubai','agaseke','pirogue','hanken','cormorant','garamond','papyrus','basalt','fade','infrared','wcag','px'])
except Exception as e: pytesseract=None; rep('WARN',f'OCR/spell unavailable: {e}')
BAN=[r'\bZayn\b',r'\bYusuf\b',r'run by (an )?ai',r'ai[- ]run',r'automated (page|account)',r'\bas an ai\b']
for i,f in enumerate(a.files,1):
    if f.endswith(('.mp4','.mov')):
        rep('INFO',f'{os.path.basename(f)}: video - check frames by eye (use ffmpeg tile sheet)'); continue
    im=Image.open(f).convert('RGB');w,h=im.size
    if (w,h) not in [(1080,1440),(1080,1350),(1080,1080),(1080,1920)]: rep('FAIL',f'{os.path.basename(f)} size {w}x{h} not an IG size')
    if os.path.getsize(f)>8_000_000: rep('WARN',f'{os.path.basename(f)} over 8MB')
    arr=np.array(im).astype(int)
    # edge bleed: text/marks touching the 40px safe margin
    gray=arr.mean(2);edges=np.abs(np.diff(gray,axis=1))
    if pytesseract:
        d=pytesseract.image_to_data(im,output_type=pytesseract.Output.DICT)
        words=[]
        for t,x,y,ww,hh,c in zip(d['text'],d['left'],d['top'],d['width'],d['height'],d['conf']):
            t=t.strip()
            if not t or float(c)<70: continue
            words.append(t)
            if (x<40 or y<40 or x+ww>w-40 or y+hh>h-40) and hh>14: rep('WARN',f'{os.path.basename(f)}: text "{t}" within 40px of the edge')
        clean=[re.sub(r"[^a-zA-Z'\-]","",x).lower() for x in words];clean=[x for x in clean if len(x)>3 and '-' not in x and not x.startswith('mayleven')]
        bad=sp.unknown(clean)
        if bad: rep('WARN',f'{os.path.basename(f)}: check spelling {sorted(bad)}')
        txt=' '.join(words)
        for b in BAN:
            if re.search(b,txt,re.I): rep('FAIL',f'{os.path.basename(f)}: banned phrase {b}')
        if re.search(r'\b(19|20)\d\d\b',txt): rep('WARN',f'{os.path.basename(f)}: a year appears on the slide - no dates on documents (ok if it is UI content)')
    # zoom crops for the eye pass: 4 quadrants at 100%
    tiles=[im.crop((0,0,w//2+60,h//2+60)),im.crop((w//2-60,0,w,h//2+60)),im.crop((0,h//2-60,w//2+60,h)),im.crop((w//2-60,h//2-60,w,h))]
    sheet=Image.new('RGB',(tiles[0].width*2+10,tiles[0].height*2+10),'white')
    for k,t in enumerate(tiles): sheet.paste(t,((k%2)*(tiles[0].width+10),(k//2)*(tiles[0].height+10)))
    sheet.save(f'{a.out}/qa_zoom_{i}.jpg',quality=88)
if a.caption:
    c=open(a.caption).read()
    for b in BAN:
        if re.search(b,c,re.I): rep('FAIL',f'caption: banned phrase {b}')
    if 'comment 11' not in c.lower(): rep('WARN','caption: no "comment 11" ask')
    for e in ['hello@may11levenlabs.com','may11leven.labs@gmail.com']:
        if e not in c: rep('WARN',f'caption: missing {e}')
    tags=re.findall(r'#\w+',c)
    if len(tags)>5: rep('FAIL',f'caption: {len(tags)} hashtags (max 5)')
    if '#may11levenlabs' not in tags: rep('WARN','caption: missing #may11levenlabs')
    if re.search(r'concept|invented',c,re.I) is None and re.search(r'\bclient\b',c,re.I): rep('WARN','caption: mentions a client but no concept/invented label - confirm it is real')
    if re.search(r'\b(pidgin|abeg|wahala|oya)\b',c,re.I): rep('FAIL','caption: pidgin')
    if len(c)>2200: rep('FAIL','caption over 2200 chars')
open(f'{a.out}/qa_report.txt','w').write('\n'.join(R) or 'PASS: no issues found')
print('\n'.join(R) or 'PASS'); sys.exit(1 if fail else 0)
