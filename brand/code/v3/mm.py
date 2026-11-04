"""May11Leven minimal-mode kit (Holographik lessons): one grotesk, mono data labels,
opacity hierarchy, tick rings, dots/lines, rounded cards, one accent per post."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, numpy as np
F='/home/claude/kit/fonts/'
W,H=1080,1440;M=64
def SANS(sz,w='Medium'): return ImageFont.truetype(F+f'InterTight-{w}.ttf',sz)
def MONO(sz,med=False): return ImageFont.truetype(F+('PlexMonoMed.ttf' if med else 'PlexMono.ttf'),sz)
def mix(a,b,t): return tuple(int(a[i]*(1-t)+b[i]*t) for i in range(3))
def tl(f,s,tr): return f.getlength(s)+max(0,len(s)-1)*tr*f.size
def tt(d,x,y,s,f,fill,tr=0.0):
    if not tr: d.text((x,y),s,font=f,fill=fill); return
    for i,ch in enumerate(s): d.text((x+f.getlength(s[:i])+i*tr*f.size,y),ch,font=f,fill=fill)
def mono(d,x,y,s,fill,sz=18,anchor='l',med=False):
    f=MONO(sz,med);s=s.upper()
    if anchor=='r': x=x-tl(f,s,0.1)
    if anchor=='c': x=x-tl(f,s,0.1)/2
    tt(d,x,y,s,f,fill,0.1)
def wrap(f,text,maxw,tr):
    out=[];line=''
    for wd in text.split(' '):
        t=(line+' '+wd).strip()
        if tl(f,t,tr)>maxw and line: out.append(line);line=wd
        else: line=t
    out.append(line);return out
def head(d,x,y,text,sz,fill,maxw=W-2*M,lead=1.04,tr=-0.032,w='Medium',lines=None,indent=0):
    f=SANS(sz,w);ls=lines or wrap(f,text,maxw,tr)
    for i,l in enumerate(ls):
        tt(d,x+(indent if i==0 else 0),y,l,f,fill,tr);y+=sz*lead
    return y
def body(d,x,y,text,sz,fill,maxw,lead=1.32,w='Regular',tr=-0.01):
    f=SANS(sz,w)
    for l in wrap(f,text,maxw,tr): tt(d,x,y,l,f,fill,tr);y+=sz*lead
    return y
def tag(d,x,y,idx,name,ink,paper,sz=17):
    """our section marker: index in a hairline box above a filled tag"""
    f=MONO(sz,True);a=idx.upper();b=name.upper()
    wa=tl(f,a,0.1)+16;d.rounded_rectangle((x,y,x+wa,y+sz+12),radius=4,outline=ink,width=2)
    tt(d,x+8,y+5,a,f,ink,0.1)
    y2=y+sz+18;wb=tl(f,b,0.1)+18
    d.rounded_rectangle((x,y2,x+wb,y2+sz+12),radius=4,fill=ink);tt(d,x+9,y2+5,b,f,paper,0.1)
    return wb
def frame_labels(d,page,total,fill,top='May11Leven Labs'):
    mono(d,M,56,top,fill,17);mono(d,W-M,56,f'{page:02d}/{total:02d}',fill,17,'r')
def ring(d,cx,cy,r,n,fill,ln=14,width=2,hi=None,hicol=None,skip=None):
    for k in range(n):
        a=-math.pi/2+2*math.pi*k/n
        if skip and k in skip: continue
        col=hicol if (hi and k in hi) else fill;l=ln*(1.8 if (hi and k in hi) else 1)
        x1,y1=cx+r*math.cos(a),cy+r*math.sin(a);x2,y2=cx+(r-l)*math.cos(a),cy+(r-l)*math.sin(a)
        d.line((x1,y1,x2,y2),fill=col,width=width)
def dashed(d,x1,y1,x2,y2,fill,dash=10,gap=8,width=2):
    L=math.hypot(x2-x1,y2-y1);n=int(L//(dash+gap))+1
    for k in range(n):
        s=k*(dash+gap)/L;e=min(1,(k*(dash+gap)+dash)/L)
        d.line((x1+(x2-x1)*s,y1+(y2-y1)*s,x1+(x2-x1)*e,y1+(y2-y1)*e),fill=fill,width=width)
def olist(d,x,y,items,active,sz,on,off,lead=1.12,tr=-0.03,w='Medium'):
    f=SANS(sz,w)
    for i,s in enumerate(items):
        tt(d,x,y,s,f,on if i==active else off,tr);y+=sz*lead
    return y
def mark(d,x,y,h,col):
    w=int(h*0.17);g=int(h*0.13)
    d.rectangle((x,y,x+w,y+h),fill=col);d.rectangle((x+w+g,y+int(h*0.22),x+2*w+g,y+h),fill=col)
def round_paste(dst,src,xy,r=28,shadow=False):
    m=Image.new('L',src.size,0);ImageDraw.Draw(m).rounded_rectangle((0,0,src.width-1,src.height-1),radius=r,fill=255)
    if shadow:
        sh=Image.new('RGBA',(src.width+120,src.height+120),(0,0,0,0))
        ImageDraw.Draw(sh).rounded_rectangle((60,70,60+src.width,70+src.height),radius=r,fill=(0,0,0,70))
        sh=sh.filter(ImageFilter.GaussianBlur(30));dst.paste(sh,(xy[0]-60,xy[1]-60),sh)
    dst.paste(src,xy,m)
def cover_crop(im,w,h,fx=0.5,fy=0.5):
    s=max(w/im.width,h/im.height);im=im.resize((int(im.width*s)+1,int(im.height*s)+1),Image.LANCZOS)
    x=int((im.width-w)*fx);y=int((im.height-h)*fy);return im.crop((x,y,x+w,y+h))
def grain(im,amt=3.2,seed=1):
    a=np.array(im).astype(float);r=np.random.default_rng(seed).normal(0,amt,a.shape[:2])[...,None]
    return Image.fromarray(np.clip(a+r,0,255).astype('uint8'))
