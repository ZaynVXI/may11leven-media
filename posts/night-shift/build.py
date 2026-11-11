# "while you sleep." word-drum loop. 1080x1350, 30 fps, 6 s seamless loop.
from PIL import Image, ImageDraw, ImageFont
import math, os, subprocess, numpy as np
HERE=os.path.dirname(os.path.abspath(__file__)); FONTS=os.path.join(HERE,'../../brand/fonts')
W,H,FPS=1080,1350,30
BG=(244,243,240); INK=(17,17,17); MID=(122,119,114)
WORDS=['Sell','Book','Reply','Get paid','Grow']; DWELL,TURN=0.85,0.35; SEG=DWELL+TURN; T=SEG*len(WORDS)
it=ImageFont.truetype(f'{FONTS}/InterTight-Medium.ttf',255); se=ImageFont.truetype(f'{FONTS}/InstrumentSerif-Italic.ttf',140)
pm=ImageFont.truetype(f'{FONTS}/PlexMono.ttf',22)
def word_img(w):
    bb=it.getbbox(w); im=Image.new('L',(bb[2]-bb[0]+20,380),0); ImageDraw.Draw(im).text((10-bb[0],24),w,font=it,fill=255); return im
WI=[word_img(w) for w in WORDS]
def ease(x): return 0.5-0.5*math.cos(math.pi*x)
def pos(t):
    k=int(t//SEG); f=t-k*SEG; e=0 if f<DWELL else ease((f-DWELL)/TURN); return k+e
CY=610; R=215; STEP=math.radians(64)
def tracked(d,xy,s,col,anchor='l'):
    x,y=xy; w=sum(d.textlength(c,font=pm)+2.6 for c in s)-2.6
    if anchor=='r': x-=w
    for c in s: d.text((x,y),c,font=pm,fill=col); x+=d.textlength(c,font=pm)+2.6
def frame(t):
    im=Image.new('RGB',(W,H),BG); p=pos(t)%len(WORDS)
    for i,wi in enumerate(WI):
        a=(i-p); a=(a+len(WORDS)/2)%len(WORDS)-len(WORDS)/2; th=a*STEP
        if abs(th)>=math.pi/2*0.98: continue
        c=math.cos(th); h=max(1,int(wi.height*c)); sq=wi.resize((wi.width,h),Image.LANCZOS)
        y=int(CY+R*math.sin(th)-h/2); x=(W-wi.width)//2
        alpha=sq.point(lambda v:int(v*min(1,c**1.6)))
        im.paste(Image.new('RGB',sq.size,INK),(x,y),alpha)
    # soft fade top/bottom of the drum so words dissolve into the paper
    d=ImageDraw.Draw(im)
    tw=d.textlength('while you sleep.',font=se); d.text(((W-tw)/2,905),'while you sleep.',font=se,fill=INK)
    tracked(d,(64,64),'MAY11LEVEN LABS',MID); tracked(d,(W-64,64),'AFTER 6 PM',MID,'r')
    tracked(d,(64,H-90),'BRAND · WEB · APPS · AI ASSISTANTS',MID); tracked(d,(W-64,H-90),'@MAY11LEVEN.LABS',MID,'r')
    return im
os.makedirs('/tmp/ns',exist_ok=True)
N=int(T*FPS)
for n in range(N): frame(n/FPS).save(f'/tmp/ns/{n:04d}.png')
frame(0).save(os.path.join(HERE,'cover.jpg'),quality=95)
subprocess.run(['ffmpeg','-v','0','-y','-framerate',str(FPS),'-i','/tmp/ns/%04d.png','-stream_loop','1','-f','lavfi','-t',str(T*2),'-i','anullsrc=r=48000:cl=stereo','-filter_complex','[0:v]loop=1:%d:0,format=yuv420p[v]'%N,'-map','[v]','-map','1:a','-t',str(T*2),'-c:v','libx264','-crf','16','-preset','slow','-c:a','aac','-shortest',os.path.join(HERE,'night-shift.mp4')],check=True)
print(N,'frames')
