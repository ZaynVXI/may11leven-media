import sys,json,math;sys.path.insert(0,'/home/claude/remake/v3');sys.path.insert(0,'/home/claude/bathu2')
from mm import *
from sole import outline
PAPER=(241,241,239);INK=(20,20,19);KERB=(122,120,115);HAIR=(200,200,197);GUM=(168,114,63);CONC=(214,212,207)
T=7;out='/home/claude/bathu2/out/'
import os;os.makedirs(out,exist_ok=True)
def save(im,n): grain(im,2.0,60+n).save(out+f'bathu-{n}.jpg',quality=94)
def labels(d,n,col): mono(d,M,56,'May11Leven Labs × Bathu (concept)',col,17);mono(d,W-M,56,f'{n:02d}/{T:02d}',col,17,'r')
def gridframe(d,x0,y0,x1,y1,col,dot):
    for x in (x0,x1): d.line((x,0,x,H),fill=col,width=2)
    for y in (y0,y1): d.line((0,y,W,y),fill=col,width=2)
    for x in (x0,x1):
        for y in (y0,y1): d.ellipse((x-7,y-7,x+7,y+7),fill=dot)
def sole_poly(cx,cy,s,mirror,dx=0,dy=0):
    return [(cx+(-y)*s+dx, cy+(-x)*s+dy) for x,y in outline(mirror=mirror)]
# 1 cover
from PIL import Image as I
I.open('/home/claude/bathu2/hero.png').convert('RGB').save(out+'bathu-1.jpg',quality=95)
# 2 the idea: black card in a visible grid (question -> answer)
im=Image.new('RGB',(W,H),PAPER);d=ImageDraw.Draw(im);labels(d,2,KERB)
x0,y0,x1,y1=150,300,930,1200;gridframe(d,x0,y0,x1,y1,HAIR,HAIR)
d.rounded_rectangle((x0+12,y0+12,x1-12,y1-12),radius=8,fill=INK)
head(d,x0+48,y0+60,'',58,PAPER,lines=['Bathu is township','slang for shoes.','What if the mark','was a step?'])
ax,ay=x0+50,y0+536;d.line((ax,ay,ax+30,ay),fill=PAPER,width=3);d.line((ax+18,ay-11,ax+31,ay),fill=PAPER,width=3);d.line((ax+18,ay+11,ax+31,ay),fill=PAPER,width=3);head(d,x0+96,y0+514,'',36,PAPER,lines=['Two soles, one ahead','of the other. It started in','a small room in Alex, and','now walks the country.'],lead=1.18)
mono(d,x0+48,y1-80,'Unsolicited concept · not affiliated with Bathu',mix(INK,PAPER,0.5),15)
save(im,2)
# 3 the mark, constructed
im=Image.new('RGB',(W,H),PAPER);d=ImageDraw.Draw(im);labels(d,3,KERB)
tag(d,M,150,'11.01','The mark',INK,PAPER)
s=1900;cx,cy=W//2,700
L=sole_poly(cx,cy,s,-1,-115,90);R=sole_poly(cx,cy,s,1,115,-90)
ys=[p[1] for p in L+R];xs=[p[0] for p in L+R]
for y in (min(p[1] for p in R),min(p[1] for p in L),max(p[1] for p in R),max(p[1] for p in L)): dashed(d,M,y,W-M,y,HAIR)
for x in (cx-115,cx+115): dashed(d,x,min(ys)-60,x,max(ys)+60,HAIR)
d.polygon(L,fill=INK);d.polygon(R,fill=GUM)
yA=min(p[1] for p in R);yB=min(p[1] for p in L);xr=W-M-40
d.line((xr,yA,xr,yB),fill=KERB,width=2)
for y in (yA,yB): d.line((xr-10,y,xr+10,y),fill=KERB,width=2)
mono(d,xr-16,(yA+yB)//2-8,'1 step',KERB,16,'r')
mono(d,cx-115,max(ys)+80,'left · ink',KERB,16,'c');mono(d,cx+115,max(ys)+80,'right · gum',KERB,16,'c')
tt(d,M,1170,'bathu',SANS(150),INK,-0.045);mono(d,M+8,1350,'Johannesburg · every step is a story',KERB,17)
save(im,3)
# 4 the map: from Alex across the country
im=Image.new('RGB',(W,H),INK);d=ImageDraw.Draw(im);labels(d,4,mix(INK,PAPER,0.5))
tag(d,M,150,'11.02','Every step',PAPER,INK)
head(d,M,250,'',56,PAPER,lines=['From a small room in Alex,'],tr=-0.03);head(d,M,312,'',56,mix(INK,PAPER,0.55),lines=['across the country.'])
G=json.load(open('/home/claude/bathu2/za.json'))
lon0,lon1,lat0,lat1=16.3,33.0,-35.0,-22.0;kx=math.cos(math.radians(28.5))
mw=W-2*M;sc_=mw/((lon1-lon0)*kx);oy=480
def P(lon,lat): return (M+(lon-lon0)*kx*sc_, oy+(lat1-lat)*sc_)
mask=Image.new('L',(W,H),0);md=ImageDraw.Draw(mask)
for poly in G['za']: md.polygon([P(*p) for p in poly[0]],fill=255)
for poly in G['ls']: md.polygon([P(*p) for p in poly[0]],fill=0)
mk=np.array(mask)
DOT=mix(INK,PAPER,0.22);st=14
for y in range(0,H,st):
    for x in range(0,W,st):
        if mk[y,x]: d.ellipse((x-2.4,y-2.4,x+2.4,y+2.4),fill=DOT)
alex=P(28.10,-26.10)
cities=[('Polokwane',29.45,-23.90),('Durban',31.02,-29.86),('Bloemfontein',26.21,-29.12),('Gqeberha',25.60,-33.96),('Cape Town',18.42,-33.92)]
for n,lo,la in cities:
    c=P(lo,la);dashed(d,alex[0],alex[1],c[0],c[1],mix(INK,GUM,0.55),7,9,2)
    d.ellipse((c[0]-6,c[1]-6,c[0]+6,c[1]+6),fill=PAPER)
    anc='r' if lo<24 else 'l';mono(d,c[0]+(-14 if anc=='r' else 14),c[1]-8,n,mix(INK,PAPER,0.7),15,anc)
for r,a in ((34,60),(22,120)): d.ellipse((alex[0]-r,alex[1]-r,alex[0]+r,alex[1]+r),outline=mix(INK,GUM,a/255),width=2)
d.ellipse((alex[0]-9,alex[1]-9,alex[0]+9,alex[1]+9),fill=GUM)
mono(d,alex[0]+44,alex[1]-26,'Alexandra',GUM,16)
mono(d,M,1360,'Map: South Africa · route lines are illustrative',mix(INK,PAPER,0.45),15)
save(im,4)
# 5 brand system page
im=Image.new('RGB',(W,H),PAPER);d=ImageDraw.Draw(im);labels(d,5,KERB)
tag(d,M,150,'11.03','Brand system',INK,PAPER)
tt(d,M-6,290,'Aa',SANS(300),INK,-0.04)
head(d,470,330,'',56,INK,lines=['Inter Tight'],tr=-0.03);body(d,472,400,'Medium for words, one size step at a time.',24,KERB,520)
mono(d,472,500,'Plex Mono · sizes, codes, prices',INK,18);mono(d,472,536,'UK 3 4 5 6 7 8 9 10 11 12',KERB,18)
sw=[('Concrete',CONC,'#D6D4CF'),('Kerb',KERB,'#7A7873'),('Ink',INK,'#141413'),('Sole white',(250,250,248),'#FAFAF8'),('Gum',GUM,'#A8723F')]
x=M;w=(W-2*M-4*14)//5;y=700
for n,c,hx in sw:
    d.rounded_rectangle((x,y,x+w,y+440),radius=14,fill=c,outline=HAIR if n=='Sole white' else None,width=2)
    tc=INK if n in ('Concrete','Sole white') else PAPER
    tt(d,x+18,y+440-74,n,SANS(24),tc,-0.02);mono(d,x+18,y+440-38,hx,tc,15);x+=w+14
body(d,M,1220,'Taken from the street, not a palette: concrete, the kerb, ink, a white midsole and one gum sole.',24,KERB,820)
save(im,5)
# 6 boxes
I.open('/home/claude/bathu2/boxes.png').convert('RGB').resize((W,H)).save(out+'bathu-6.jpg',quality=95)
# 7 close
im=Image.new('RGB',(W,H),INK);d=ImageDraw.Draw(im);labels(d,7,mix(INK,PAPER,0.5))
mark(d,M,250,92,GUM)
head(d,M,520,'',80,PAPER,lines=['Your brand next?'])
head(d,M,610,'',80,mix(INK,PAPER,0.55),lines=['Every step','is a story.'])
body(d,M,860,'Comment 11 for a free look at your brand, or email us.',28,mix(INK,PAPER,0.55),800)
body(d,M,960,'hello@may11levenlabs.com',28,PAPER,900,w='Medium');body(d,M,1002,'may11leven.labs@gmail.com',28,PAPER,900,w='Medium')
mono(d,M,1340,'Unsolicited concept · not affiliated with Bathu',mix(INK,PAPER,0.4),15)
save(im,7)
