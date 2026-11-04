import sys,os,math,subprocess;sys.path.insert(0,'/home/claude/remake/v3')
from mm import SANS,MONO,mono,head,body,tt,mark,mix,dashed,tag,tl
from PIL import Image,ImageDraw
import numpy as np
D='/home/claude/ata2';W,H=1080,1920;FPS=30;TOT=15.4;M=64
INK=(14,13,13);BONE=(238,234,226);PAPER=(241,239,234);RED=(206,44,30);MID=(120,116,110)
def load(p):
    im=Image.open(f'{D}/{p}').convert('RGB');return im.resize((W,H),Image.LANCZOS) if im.size!=(W,H) else im
close=load('ata_close.png');wide=load('ata_wide.png')
lab=Image.open(f'{D}/ata_label.png').convert('RGB')
bb=Image.open(f'{D}/ata_label.png').convert('L').point(lambda v:255 if v>40 else 0).getbbox();lab=lab.crop(bb)
def zoom(im,s,cy=0.5):
    w,h=int(W/s),int(H/s);x=(W-w)//2;y=int((H-h)*cy);return im.crop((x,y,x+w,y+h)).resize((W,H),Image.BILINEAR)
def ease(x): x=max(0,min(1,x));return x*x*(3-2*x)
shade=Image.new('L',(W,H),0);sd=ImageDraw.Draw(shade)
for y in range(H):
    v=int(190*max(0,(640-y)/640)**1.2) if y<640 else 0
    sd.line((0,y,W,y),fill=v)
inkimg=Image.new('RGB',(W,H),INK)
def top(d,col,right='Product visuals'):
    mono(d,M,120,'May11Leven Labs',col,20);mono(d,W-M,120,right,col,20,'r')
def segA(t):
    im=Image.composite(inkimg,zoom(close,1.0+0.05*t/3.6),shade);d=ImageDraw.Draw(im);top(d,BONE)
    head(d,M,230,'',80,BONE,lines=['This bottle']);
    if t>0.9: head(d,M,314,'',80,BONE,lines=["doesn't exist."])
    return im
def segB(t):
    im=Image.composite(inkimg,zoom(wide,1.06-0.06*ease(t/3.8)),shade);d=ImageDraw.Draw(im);top(d,BONE)
    for k,s in enumerate(['No factory.','No photoshoot.','No studio.']):
        if t>0.3+k*0.7: head(d,M,230+k*84,'',80,BONE,lines=[s])
    return im
def segC(t):
    im=Image.new('RGB',(W,H),PAPER);d=ImageDraw.Draw(im);top(d,MID,'The label')
    tag(d,M,250,'11.01','Spec',INK,PAPER)
    head(d,M,340,'',72,INK,lines=['Designed, lit and','rendered. Never','photographed.'])
    lw=640;l=lab.resize((lw,int(lab.height*lw/lab.width)),Image.LANCZOS);y0=620
    a=ease(t/0.6);im.paste(l,((W-lw)//2,y0));d=ImageDraw.Draw(im)
    y1=y0+l.height-10
    lx0,lx1=(W-lw)//2,(W+lw)//2;dashed(d,lx0,y1+40,lx1,y1+40,MID);d.line((lx0,y1+28,lx0,y1+52),fill=MID,width=2);d.line((lx1,y1+28,lx1,y1+52),fill=MID,width=2)
    mono(d,W//2,y1+60,'label · 210 × 56 mm',MID,18,'c')
    for i,(k,v) in enumerate([('Product','Lagos pepper oil'),('Chilli','Scotch bonnet'),('Volume','180 ml'),('Accent','#CE2C1E')]):
        y=y1+110+i*66;d.line((M,y,W-M,y),fill=(214,210,203),width=2)
        mono(d,M,y+22,k,MID,18);tt(d,420,y+14,v,SANS(32),INK,-0.02)
    d.ellipse((W-M-26,y1+110+3*66+18,W-M,y1+110+3*66+44),fill=RED)
    if a<1: im=Image.blend(Image.new('RGB',(W,H),PAPER),im,a)
    return im
def segD(t):
    im=Image.composite(inkimg,zoom(wide,1.0+0.04*t/2.2,0.55),shade);d=ImageDraw.Draw(im);top(d,BONE)
    head(d,M,230,'',80,BONE,lines=['Launch visuals','before the first','unit ships.'])
    return im
def segE(t):
    im=Image.new('RGB',(W,H),INK);d=ImageDraw.Draw(im);top(d,mix(INK,BONE,0.5))
    mark(d,M,640,110,RED)
    head(d,M,880,'',84,BONE,lines=['Your product next?'])
    body(d,M,1010,'Comment 11 for a free product visual idea, or email us.',32,mix(INK,BONE,0.6),900)
    body(d,M,1130,'hello@may11levenlabs.com',30,BONE,900,w='Medium');body(d,M,1176,'may11leven.labs@gmail.com',30,BONE,900,w='Medium')
    mono(d,M,1300,'ata is an invented brand',mix(INK,BONE,0.45),18)
    return im
SEG=[(0,3.6,segA),(3.6,7.4,segB),(7.4,10.6,segC),(10.6,12.8,segD),(12.8,TOT,segE)]
os.makedirs(f'{D}/fr',exist_ok=True);prev=None
for n in range(int(TOT*FPS)):
    t=n/FPS
    for i,(a,b,f) in enumerate(SEG):
        if a<=t<b: im=f(t-a);
        if a<=t<b:
            if i>0 and t-a<0.25:
                pa,pb,pf=SEG[i-1];im=Image.blend(pf(pb-pa-0.001),im,(t-a)/0.25)
            break
    im.save(f'{D}/fr/{n:04d}.jpg',quality=92)
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i',f'{D}/fr/%04d.jpg','-i',f'{D}/ata.wav','-c:v','libx264','-crf','17','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-shortest',f'{D}/ata-reel.mp4'],check=True)
# cover: clean wide frame, 3:4 safe
c=wide.crop((0,(H-1440)//2,W,(H-1440)//2+1440));c.save(f'{D}/ata-cover.jpg',quality=95)
