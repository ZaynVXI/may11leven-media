from PIL import Image, ImageDraw, ImageFont
import os
F=os.environ.get('M11_FONTS','brand/fonts/')
INK=(20,18,19);BONE=(236,234,228);IR=(255,74,28);ASH=(140,136,132)
def font(name,sz,axes=None):
    f=ImageFont.truetype(F+name,sz)
    if axes: f.set_variation_by_axes(axes)
    return f
def SANS(sz,w='Regular'): return font(f'InterTight-{w}.ttf',sz)
def SERIF(sz,it=True): return font('InstrumentSerif-Italic.ttf' if it else 'InstrumentSerif-Regular.ttf',sz)
def MONO(sz): return font('PlexMono.ttf',sz)
def tlen(f,s,track):  # track in em fraction
    return f.getlength(s)+max(0,len(s)-1)*track*f.size
def ttext(d,xy,s,f,fill,track=0.0):
    x,y=xy
    if not track: d.text((x,y),s,font=f,fill=fill); return
    for i,ch in enumerate(s):
        d.text((x+f.getlength(s[:i])+i*track*f.size,y),ch,font=f,fill=fill)
def label(d,xy,s,fill,sz=19,anchor='l',W=1080):
    f=MONO(sz);s=s.upper();x,y=xy
    if anchor=='r': x=W-x-tlen(f,s,0.12)
    ttext(d,(x,y),s,f,fill,0.12)
def rich(d,x,y,lines,sz,fill,accent=None,lead=1.08,track=-0.025,maxw=None):
    """lines: list of lists of (text, style) where style 's' sans or 'i' serif italic"""
    for line in lines:
        cx=x
        for txt,st in line:
            if st=='i': f=SERIF(int(sz*1.12)); tr=-0.01; col=accent or fill; dy=-int(sz*0.06)
            else: f=SANS(sz); tr=track; col=fill; dy=0
            ttext(d,(cx,y+dy),txt,f,col,tr); cx+=tlen(f,txt,tr)+ (0)
        y+=sz*lead
    return y
def para(d,x,y,text,sz,fill,maxw,lead=1.45,w='Regular'):
    f=SANS(sz,w);words=text.split(' ');line=''
    for wd in words:
        t=(line+' '+wd).strip()
        if f.getlength(t)>maxw: d.text((x,y),line,font=f,fill=fill); y+=sz*lead; line=wd
        else: line=t
    d.text((x,y),line,font=f,fill=fill); return y+sz*lead
def mark(d,x,y,h=120,col=IR):
    w=int(h*0.17);g=int(h*0.13)
    d.rectangle((x,y,x+w,y+h),fill=col);d.rectangle((x+w+g,y+int(h*0.22),x+2*w+g,y+h),fill=col)
