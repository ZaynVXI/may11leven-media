from PIL import Image, ImageDraw, ImageFilter, ImageFont
import numpy as np
W,H=1080,1440; K=3
PAPER=(242,238,232)
FM='/home/claude/may11leven-media/brand/fonts/PlexMono.ttf'
def tracked(d,xy,text,font,fill,track,anchor='l'):
    x,y=xy; text=text.upper()
    w=sum(d.textlength(ch,font=font)+track for ch in text)-track
    if anchor=='r': x-=w
    for ch in text: d.text((x,y),ch,font=font,fill=fill); x+=d.textlength(ch,font=font)+track
cover=Image.open('trio.png').convert('RGB')
bg=cover.resize((W,H)).filter(ImageFilter.GaussianBlur(16))
bg=Image.blend(bg,Image.new('RGB',(W,H),(40,36,32)),0.38)
def phone(screen_path,S):
    s=Image.open(screen_path).convert('RGB'); S*=K
    sh=int(S*844/390); s=s.resize((S,sh),Image.LANCZOS)
    b=int(S*0.038); rim=int(S*0.012)
    Wd,Hd=S+2*(b+rim),sh+2*(b+rim)
    rs=int(S*0.142); rb=rs+b; ro=rb+rim
    img=Image.new('RGBA',(Wd+40*K,Hd),(0,0,0,0)); d=ImageDraw.Draw(img); ox=20*K
    # side buttons (titanium)
    btn=(118,116,112,255)
    d.rounded_rectangle((ox-4*K,int(Hd*.20),ox+2*K,int(Hd*.245)),radius=2*K,fill=btn)  # action
    d.rounded_rectangle((ox-4*K,int(Hd*.29),ox+2*K,int(Hd*.355)),radius=2*K,fill=btn)  # vol up
    d.rounded_rectangle((ox-4*K,int(Hd*.375),ox+2*K,int(Hd*.44)),radius=2*K,fill=btn)  # vol down
    d.rounded_rectangle((ox+Wd-2*K,int(Hd*.31),ox+Wd+4*K,int(Hd*.41)),radius=2*K,fill=btn) # power
    # titanium rim with soft vertical gradient
    g=np.linspace(0,1,Hd)[:,None]
    col=(np.array([168,165,160])[None,None,:]*(1-g[:,:,None])+np.array([120,117,112])[None,None,:]*g[:,:,None])
    rimimg=Image.fromarray(np.dstack([np.repeat(col[:,:,i],Wd,1) for i in range(3)]).astype(np.uint8))
    mask=Image.new('L',(Wd,Hd),0); ImageDraw.Draw(mask).rounded_rectangle((0,0,Wd-1,Hd-1),radius=ro,fill=255)
    img.paste(rimimg,(ox,0),mask)
    d.rounded_rectangle((ox+rim,rim,ox+Wd-1-rim,Hd-1-rim),radius=rb,fill=(10,10,11,255))
    sm=Image.new('L',(S,sh),0); ImageDraw.Draw(sm).rounded_rectangle((0,0,S-1,sh-1),radius=rs,fill=255)
    img.paste(s,(ox+rim+b,rim+b),sm)
    # dynamic island
    iw,ih=int(S*0.32),int(S*0.095); ix=ox+Wd//2-iw//2; iy=rim+b+int(S*0.028)
    d.rounded_rectangle((ix,iy,ix+iw,iy+ih),radius=ih//2,fill=(6,6,7,255))
    d.ellipse((ix+iw-ih+int(ih*.28),iy+int(ih*.28),ix+iw-int(ih*.28),iy+ih-int(ih*.28)),fill=(22,24,32,255))
    hw=int(S*0.35);hh=max(int(S*0.013),6);hx=ox+Wd//2-hw//2;hy=rim+b+sh-int(S*0.024)
    d.rounded_rectangle((hx,hy,hx+hw,hy+hh),radius=hh//2,fill=(20,18,16,255))
    return img.resize((img.width//K,img.height//K),Image.LANCZOS)
def place(ph,x,y):
    a=ph.split()[3]; shadow=Image.new('L',(W,H),0); shadow.paste(a.point(lambda v:int(v*.55)),(x+14,y+28)); shadow=shadow.filter(ImageFilter.GaussianBlur(30))
    global bg; bg=Image.composite(Image.new('RGB',(W,H),(14,12,10)),bg,shadow); bg.paste(ph,(x,y),ph)
p1=phone('mp.png',392); p2=phone('mb.png',392)
place(p1,64,214); place(p2,560,318)
d=ImageDraw.Draw(bg); f=ImageFont.truetype(FM,17); f2=ImageFont.truetype(FM,16)
tracked(d,(80,60),'May11Leven Labs · Imisozi (concept)',f,PAPER,2.2); tracked(d,(1000,60),'03/06',f,PAPER,2.2,'r')
tracked(d,(104,214+p1.height+30),'Product',f2,PAPER,2.4); tracked(d,(600,318+p2.height+30),'Bag · MoMo checkout',f2,PAPER,2.4)
a=np.asarray(bg).astype(float); rng=np.random.default_rng(83); a+=rng.normal(0,2.0,a.shape)
Image.fromarray(np.clip(a,0,255).astype(np.uint8)).save('imisozi-3.jpg',quality=94)
print(p1.size,p2.size)
