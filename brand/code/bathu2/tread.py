import sys;sys.path.insert(0,'/home/claude/bathu2')
from sole import outline
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import numpy as np
from scipy.ndimage import distance_transform_edt as edt
SX,SY=2048,768
def tread(mirror,out):
    pts=outline(mirror=mirror);xs=[p[0] for p in pts];ys=[p[1] for p in pts]
    x0,x1,y0,y1=min(xs),max(xs),min(ys),max(ys)
    poly=[((p[0]-x0)/(x1-x0)*(SX-1),(1-(p[1]-y0)/(y1-y0))*(SY-1)) for p in pts]
    mask=Image.new('L',(SX,SY),0);ImageDraw.Draw(mask).polygon(poly,fill=255);mk=np.array(mask)>0
    dist=edt(mk)
    h=Image.new('L',(SX,SY),210);d=ImageDraw.Draw(h)
    for k in range(-20,60):
        x=k*42;d.line([(x,0),(x+90,SY/2),(x,SY)],fill=80,width=13)
    hn=np.array(h).astype(float)
    hn[dist<34]=210                 # smooth outer rim
    hn[(dist>=14)&(dist<22)]=70     # perimeter groove
    xx=np.arange(SX)[None,:].repeat(SY,0)
    arch=(xx>SX*0.36)&(xx<SX*0.50)&(dist>=34);hn[arch]=200
    f=ImageFont.truetype('/home/claude/kivu/fonts/hanken-grotesk-latin-500-normal.ttf',120)
    t=Image.new('L',(520,170),0);ImageDraw.Draw(t).text((10,5),'bathu',font=f,fill=255)

    ta=np.array(t)>0;oy=(SY-ta.shape[0])//2;ox=int(SX*0.08)
    hn[oy:oy+ta.shape[0],ox:ox+ta.shape[1]]=np.where(ta,95,210)
    hn[~mk]=210
    Image.fromarray(hn.astype('uint8')).filter(ImageFilter.GaussianBlur(2.5)).save(out)
tread(1,'tread_r.png');tread(-1,'tread_l.png')
