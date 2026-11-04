import sys;sys.path.insert(0,'/home/claude/remake/v3');sys.path.insert(0,'/home/claude/remake')
import os;os.chdir('/home/claude/remake')
from mm import SANS,MONO,mono,head,body,tt,mark,mix
from PIL import Image,ImageDraw
import numpy as np,math
W,H=1080,1920;FPS=30;TOT=15.0;M=64
INK=(20,18,19);BONE=(236,234,228);IR=(255,74,28)
def prep(p):
    im=Image.open(p).convert('RGB');s=H/im.height
    im=im.resize((int(im.width*s)+2,H),Image.LANCZOS);x=(im.width-W)//2
    return im.crop((x,0,x+W,H))
shots=[prep('flash.png'),prep('window.png'),prep('studio.png')]
a=np.array(shots[1]).astype(float);a=(a-128)*0.82+128+10;a[:,:,0]*=0.94;a[:,:,2]*=1.06
g=a.mean(2,keepdims=True);a=g+(a-g)*0.7;shots[1]=Image.fromarray(np.clip(a,0,255).astype('uint8'))
def zoom(im,t,amt=0.05):
    s=1+amt*t;w,h=int(W/s),int(H/s);x,y=(W-w)//2,(H-h)//2
    return im.crop((x,y,x+w,y+h)).resize((W,H),Image.BILINEAR)
segs=[(0,3.6),(3.6,7.4),(7.4,13.2)]
names=['Phone flash','Window light','Studio light'];says=['quick snap','nice café','luxury brand']
def ease(x): return 0.5-0.5*math.cos(math.pi*max(0,min(1,x)))
def seg(t):
    for i,(a,b) in enumerate(segs):
        if a<=t<b: return i
    return 2
shade=Image.new('L',(W,H),0);sd=ImageDraw.Draw(shade)
for y in range(H):
    v=0
    if y<780: v=int(238*min(1,(780-y)/420)**1.1)
    if y>1240: v=max(v,int(235*min(1,(y-1240)/220)**1.1))
    sd.line((0,y,W,y),fill=v)
inkimg=Image.new('RGB',(W,H),INK);FADE=mix(INK,BONE,0.42)
os.makedirs('fr3',exist_ok=True)
for n in range(int(TOT*FPS)):
    t=n/FPS
    if t>=11.2:
        im=Image.new('RGB',(W,H),INK);d=ImageDraw.Draw(im)
        mono(d,M,150,'May11Leven Labs',FADE,24);mono(d,W-M,150,'Product photography',FADE,24,'r')
        if t<13.2:
            head(d,M,760,'',84,BONE,lines=['The bottle','never changed.'])
            if t>12.0: head(d,M,940,'',84,FADE,lines=['The price people','imagine did.'])
        else:
            mark(d,M,640,110,IR)
            head(d,M,880,'',84,BONE,lines=['Product photos,','lit like they\'re','worth it.'])
            body(d,M,1200,'Comment 11 and send one phone photo. We send back a free shot idea.',32,FADE,820)
            mono(d,M,1400,'@may11leven.labs',FADE,24)
    else:
        i=seg(t);a,b=segs[i]
        im=zoom(shots[i],(t-a)/(b-a) if i<2 else (t-a)/5.8)
        if i>0 and t-a<0.35:
            q=ease((t-a)/0.35);prev=zoom(shots[i-1],1.0);x=int(W*q)
            c=prev.copy();c.paste(im.crop((0,0,x,H)),(0,0));im=c
            ImageDraw.Draw(im).rectangle((x-6,0,x,H),fill=IR)
        im=Image.composite(inkimg,im,shade);d=ImageDraw.Draw(im)
        mono(d,M,150,'May11Leven Labs',BONE,24);mono(d,W-M,150,'Product photography',BONE,24,'r')
        head(d,M,220,'',72,BONE,lines=['Same bottle.'])
        if t>=1.0: head(d,M,296,'',72,BONE,lines=['Three lights.'])
        mono(d,M,1400,f'0{i+1} / 03',BONE,24)
        tt(d,M,1436,names[i],SANS(64),BONE,-0.03)
        mono(d,M,1524,'says: '+says[i],BONE,24)
        if t>=10.9: im=Image.blend(im,inkimg,min(1,(t-10.9)/0.3))
        if t<0.18: im=Image.blend(im,Image.new('RGB',(W,H),(255,255,255)),1-t/0.18)
    im.save(f'fr3/{n:04d}.jpg',quality=90)
