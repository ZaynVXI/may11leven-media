# Practice reel: hierarchy by opacity (after Holographik's values list). Never posted.
import numpy as np, subprocess, wave, os, sys
from PIL import Image, ImageDraw, ImageFont
W,H,FPS,DUR=1080,1920,30,8.0
F='/home/claude/may11leven-media/brand/fonts/'
INK=(20,18,19);BONE=(236,234,228);IR=(255,74,28)
VER=sys.argv[1] if len(sys.argv)>1 else 'v1'
med=lambda s:ImageFont.truetype(F+'InterTight-Medium.ttf',s)
mono=ImageFont.truetype(F+'PlexMono.ttf',26)
ITEMS=['Brand identity','Websites','Apps','Packaging & 3D','Automation','Content']
FS=92 if VER=='v1' else 104
TRACK=-0.03
DIM=0.18
def mix(a,b,t):return tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3))
def tracked(d,xy,txt,font,fill,tr=TRACK):
    x,y=xy
    for ch in txt:
        d.text((x,y),ch,font=font,fill=fill); x+=font.getlength(ch)+tr*font.size
    return x
def ease(t):t=max(0,min(1,t));return t*t*(3-2*t)
def eo(t):t=max(0,min(1,t));return 1-(1-t)**3
mark=Image.open('/home/claude/may11leven-media/brand/may11leven-logo.png').convert('RGBA')
# key times
T0=0.0;STEP=0.72 if VER=='v1' else 0.62
changes=[T0+i*STEP for i in range(len(ITEMS))]      # item i becomes active
EXIT=changes[-1]+STEP+0.1; MARK=EXIT+(0.5 if VER=='v1' else 0.2); LOOP=DUR-0.45
X0=96; Y0=560; LH=int(FS*1.12)
def frame(t):
    im=Image.new('RGB',(W,H),BONE); d=ImageDraw.Draw(im)
    # hairline grid (visible structure)
    g=mix(BONE,INK,0.10)
    for x in (X0,W-96): d.line([(x,200),(x,H-200)],fill=g,width=1)
    for y in (300,Y0-60,1500): d.line([(X0,y),(W-96,y)],fill=g,width=1)
    for x in (X0,W-96):
        for y in (300,Y0-60,1500): d.ellipse([x-3,y-3,x+3,y+3],fill=mix(BONE,INK,0.35))
    d.text((X0,250),'S.02',font=mono,fill=INK); d.text((X0+120,250),'WHAT WE MAKE',font=mono,fill=mix(BONE,INK,0.5))
    looping=t>=LOOP
    act=0 if looping else max([i for i,c in enumerate(changes) if t>=c] or [0])
    # list exit
    ex=0 if looping else eo((t-EXIT)/0.45)
    lift=int(-260*ex) if VER=='v1' else 0
    if ex<1:
        for i,s in enumerate(ITEMS):
            y=Y0+i*LH+lift
            if looping: a=1 if i==0 else DIM
            else:
                # crossfade over 4 frames on change
                ta=ease((t-changes[i])/(0.13 if VER=='v1' else 0.034)) if t>=changes[i] else 0
                tn=ease((t-changes[i+1])/(0.13 if VER=='v1' else 0.034)) if i+1<len(changes) and t>=changes[i+1] else 0
                a=DIM+(1-DIM)*(ta-tn) if i>0 else DIM+(1-DIM)*(1-tn)
                if VER!='v1' and t>=EXIT: a*=1-ex
            col=mix(BONE,INK,a*(1-ex) if VER=='v1' else a)
            tracked(d,(X0+40,y),s,med(FS),col)
        # accent dot follows active row (6-frame ease)
        if not looping:
            prev=max(act-1,0); k=ease((t-changes[act])/(0.2 if VER=='v1' else 0.1)) if act>0 else 1
            yd=Y0+(prev+(act-prev)*k)*LH+lift+FS*0.55
        else: yd=Y0+FS*0.55
        r=11
        d.ellipse([X0-r+6,yd-r,X0+r+6,yd+r],fill=mix(BONE,IR,1-ex))
        # counter
        n='%02d'%(act+1)
        xe=tracked(d,(X0,1300+lift),n,med(150),mix(BONE,INK,1-ex))
        d.text(((X0+260) if VER=='v1' else xe+18,1385+lift),'/ 06',font=mono,fill=mix(BONE,INK,0.45*(1-ex)))
    if t>=MARK and not looping:
        k=eo((t-MARK)/0.5)
        m=mark.copy(); s=int((300 if VER=='v1' else 440)+40*(1-k)); m=m.resize((s,int(s*m.height/m.width)))
        a=m.split()[3].point(lambda v:int(v*k)); m.putalpha(a)
        im.paste(m,((W-m.width)//2,(H-m.height)//2-80),m)
        if VER!='v1':
            d.text(((W-mono.getlength('comment 11'))//2,(H)//2+180),'comment 11',font=mono,fill=mix(BONE,INK,0.6*k))
    return im
out=f'/home/claude/may11leven-media/brand/practice/reels/opacity-list-{VER}'
# audio first
SR=48000;N=int(SR*DUR);a=np.zeros(N)
def tick(t0,f=2400,amp=0.25,dec=0.025):
    i=int(t0*SR);n=int(0.12*SR);tt=np.arange(n)/SR
    a[i:i+n]+=amp*np.sin(2*np.pi*f*tt)*np.exp(-tt/dec)
def hit(t0):
    i=int(t0*SR);n=int(0.9*SR);tt=np.arange(n)/SR
    a[i:i+n]+=0.5*np.sin(2*np.pi*55*tt)*np.exp(-tt/0.25)+0.15*np.sin(2*np.pi*110*tt)*np.exp(-tt/0.12)
def whoosh(t0,l=0.45):
    i=int(t0*SR);n=int(l*SR);nz=np.random.default_rng(1).standard_normal(n)
    k=np.ones(40)/40; nz=np.convolve(nz,k,'same'); env=np.sin(np.pi*np.arange(n)/n)**2
    a[i:i+n]+=0.5*nz*env
for c in changes[1:]: tick(c-2/FPS)  # sound leads picture by 2 frames
tick(LOOP-2/FPS,1800)
whoosh(EXIT-0.2); hit(MARK)
a=np.clip(a/max(1,np.abs(a).max()/0.7),-1,1)
with wave.open(out+'.wav','wb') as w:
    w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((a*32767).astype('<i2').tobytes())
p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-i',out+'.wav','-c:v','libx264','-pix_fmt','yuv420p','-crf','17','-c:a','aac','-b:a','192k','-shortest',out+'.mp4'],stdin=subprocess.PIPE)
for k in range(int(DUR*FPS)):
    fr=frame(k/FPS); p.stdin.write(fr.tobytes())
    if k in (0,int(2.2*FPS),int(5.0*FPS),int(6.6*FPS)): fr.save(f'{out}-f{k:03d}.jpg',quality=85)
p.stdin.close();p.wait();os.remove(out+'.wav')
print('ok',out)
