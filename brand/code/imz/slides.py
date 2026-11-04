import sys;sys.path.insert(0,'/home/claude/remake/v3')
from mm import *
from PIL import ImageFilter
PAPER=(242,238,232);INK=(30,26,23);MID=(138,131,122);LINE=(220,213,202);CLAY=(150,68,46);MOSS=(92,104,78);TILE=(231,225,216)
T=6;out='/home/claude/imz/out/';import os;os.makedirs(out,exist_ok=True)
def save(im,n): grain(im,2.0,80+n).save(out+f'imisozi-{n}.jpg',quality=94)
def labels(d,n,col): mono(d,M,56,'May11Leven Labs · Imisozi (concept)',col,17);mono(d,W-M,56,f'{n:02d}/{T:02d}',col,17,'r')
# 1 cover: the trio render
Image.open('/home/claude/imz/trio.png').convert('RGB').save(out+'imisozi-1.jpg',quality=95)
# 2 two desktop pages stacked on a blurred photo of the hills (Lake Kivu)
bg=cover_crop(Image.open('/home/claude/kivu/hero.png').convert('RGB'),W,H,0.5,0.5).filter(ImageFilter.GaussianBlur(10))
bg=Image.blend(bg,Image.new('RGB',(W,H),(30,30,28)),0.15)
cw=940;ch=int(cw*900/1440)
a=Image.open('/home/claude/imz/dh.png').convert('RGB').resize((cw,ch),Image.LANCZOS)
b=Image.open('/home/claude/imz/ds.png').convert('RGB').resize((cw,ch),Image.LANCZOS)
x=(W-cw)//2;y=(H-2*ch-6)//2
bg.paste(a,(x,y));bg.paste(b,(x,y+ch+6));d=ImageDraw.Draw(bg);labels(d,2,PAPER)
save(bg,2)
# 3 two phone screens floating on the product render
bg=cover_crop(Image.open('/home/claude/imz/huye1.png').convert('RGB'),W,H,0.5,0.45).filter(ImageFilter.GaussianBlur(14))
bg=Image.blend(bg,Image.new('RGB',(W,H),(40,36,32)),0.35)
sw=400;sh=int(sw*844/390)
for i,(f,xx,yy) in enumerate((('mp',110,250),('mb',570,330))):
    s_=Image.open(f'/home/claude/imz/{f}.png').convert('RGB').resize((sw,sh),Image.LANCZOS);round_paste(bg,s_,(xx,yy),34,shadow=True)
d=ImageDraw.Draw(bg);labels(d,3,PAPER)
mono(d,110,250+sh+34,'Product',PAPER,16);mono(d,570,330+sh+34,'Bag · MoMo checkout',PAPER,16)
save(bg,3)
# 4 the idea
im=Image.new('RGB',(W,H),PAPER);d=ImageDraw.Draw(im);labels(d,4,MID)
tag(d,M,250,'11.01','The idea',INK,PAPER)
head(d,M,420,'',74,INK,lines=['Most coffee sites','sell a bag. This one','sells a hill.'])
y=980
for k,(n,lab) in enumerate([('3','origins'),('48 h','to your door'),('MoMo','or card')]):
    x=M+k*320;d.line((x,y,x+290,y),fill=LINE,width=2);tt(d,x,y+24,n,SANS(84),INK,-0.03);mono(d,x,y+140,lab,MID,17)
body(d,M,1290,'Concept identity, packaging and shop for an invented roaster in Kigali. Not a client.',24,MID,640)
save(im,4)
# 5 packaging system: the three labels as flats + named colours
im=Image.new('RGB',(W,H),PAPER);d=ImageDraw.Draw(im);labels(d,5,MID)
tag(d,M,150,'11.02','Packaging system',INK,PAPER)
fw=(W-2*M-2*20)//3;fh=int(fw*1.5)
for i,(f,nm,hx) in enumerate((('huye','Huye ink','#1E1A17'),('nyam','Nyamasheke clay','#96442E'),('gak','Gakenke moss','#5C684E'))):
    fl=Image.open(f'/home/claude/imz/tex/{f}.png').convert('RGB').resize((fw,fh),Image.LANCZOS);xx=M+i*(fw+20);im.paste(fl,(xx,300))
    d=ImageDraw.Draw(im);d.line((xx,300+fh+30,xx+fw,300+fh+30),fill=LINE,width=2)
    tt(d,xx,300+fh+46,nm,SANS(26),INK,-0.02);mono(d,xx,300+fh+86,hx,MID,15)
body(d,M,1230,'One bag, one wordmark, one hills line. Each origin gets the colour of its own place: volcanic soil, the lake shore, the green north.',24,MID,900)
save(im,5)
# 6 close
im=Image.new('RGB',(W,H),INK);d=ImageDraw.Draw(im);L2=mix(INK,PAPER,0.55);labels(d,6,L2)
mark(d,M,250,92,CLAY)
head(d,M,520,'',80,PAPER,lines=['A website that','sells while you sleep.'])
body(d,M,760,'Shops, bookings and leads, built for the phone first. Comment 11 for a free review of your website, or email us.',28,L2,820)
body(d,M,960,'hello@may11levenlabs.com',28,PAPER,900,w='Medium');body(d,M,1002,'may11leven.labs@gmail.com',28,PAPER,900,w='Medium')
mono(d,M,1340,'Imisozi is an invented brand',mix(INK,PAPER,0.4),15)
save(im,6)
