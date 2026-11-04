import sys;sys.path.insert(0,'/home/claude/remake/v3')
from mm import *
PAP=(241,233,221);DEEP=(52,27,15);RED=(204,48,5);MID=mix(PAP,DEEP,0.55);FADE=mix(PAP,DEEP,0.2)
T=9;out='/home/claude/remake/v3/out/'
import os;os.makedirs(out,exist_ok=True)
def save(im,n): grain(im,2.4,n).save(out+f'clinic-{n}.jpg',quality=94)
# 1 cover: clean sign
Image.open('/home/claude/remake/cov/clinic-0.jpg').convert('RGB').save(out+'clinic-1.jpg',quality=95)
# 2 statement
im=Image.new('RGB',(W,H),PAP);d=ImageDraw.Draw(im);frame_labels(d,2,T,MID,'Brand clinic')
tag(d,M,250,'11.01','The problem',DEEP,PAP)
head(d,M,420,'',76,DEEP,lines=['Nothing is wrong','with your business.','Maybe your logo just','hasn\'t caught up','with it.'])
body(d,620,1170,'Brand clinic is our free, honest look at one logo: five tests and a short note on what to keep and what to fix.',24,MID,396)
save(im,2)
# 3 street photo, small caption only
wall=Image.open('/home/claude/remake/wall.png').convert('RGB')
im=cover_crop(wall.crop((0,0,1700,1620)),W,H,0.35,0.5);d=ImageDraw.Draw(im)
sh=Image.new('L',(W,H),0);sd=ImageDraw.Draw(sh)
for y in range(1100,H): sd.line((0,y,W,y),fill=int(150*((y-1100)/340)**1.4))
im=Image.composite(Image.new('RGB',(W,H),DEEP),im,sh);d=ImageDraw.Draw(im)
frame_labels(d,3,T,DEEP,'Brand clinic')
mono(d,M,1330,'From a passing moto, your sign gets one look.',PAP,19)
save(im,3)
# 4-8 the five tests
tests=['16 px','One colour','Across the street','Black and white','Three seconds']
notes=['Still readable as a phone tab icon?','Does it survive a single-colour stamp?','Readable on a shopfront from a moving moto?','Does it hold on a cheap receipt print?','Could someone sketch it after one look?']
CX,CY,R=W-M-260,470,250
def illo(d,k):
    ring(d,CX,CY,R,120,FADE,12,2)
    if k==0:
        s=16;d.rectangle((CX-s//2,CY-s//2,CX+s//2,CY+s//2),fill=RED)
        dashed(d,CX-150,CY-150,CX+150,CY-150,MID);dashed(d,CX-150,CY+150,CX+150,CY+150,MID)
        dashed(d,CX-150,CY-150,CX-150,CY+150,MID);dashed(d,CX+150,CY-150,CX+150,CY+150,MID)
        for sx,sy in [(-1,-1),(1,-1),(-1,1),(1,1)]: dashed(d,CX+sx*8,CY+sy*8,CX+sx*150,CY+sy*150,FADE,6,6)
        mono(d,CX,CY+R+30,'16 × 16 PX',MID,17,'c')
    if k==1:
        d.ellipse((CX-130,CY-130,CX+130,CY+130),fill=DEEP);mono(d,CX,CY+R+30,'1 ink · no gradients',MID,17,'c')
    if k==2:
        y=CY;d.line((CX-200,y,CX+170,y),fill=MID,width=2)
        d.ellipse((CX-210,y-10,CX-190,y+10),fill=DEEP);d.rectangle((CX+150,y-34,CX+210,y+4),fill=RED)
        for j in range(1,8): d.line((CX-200+j*46,y-8,CX-200+j*46,y+8),fill=MID,width=2)
        mono(d,CX-200,y+30,'you',MID,17);mono(d,CX+210,y+30,'≈ 18 m · 1 sec',MID,17,'r')
    if k==3:
        d.pieslice((CX-130,CY-130,CX+130,CY+130),90,270,fill=DEEP);d.ellipse((CX-130,CY-130,CX+130,CY+130),outline=DEEP,width=2)
        mono(d,CX,CY+R+30,'k 100 · thermal print',MID,17,'c')
    if k==4:
        ring(d,CX,CY,R,120,FADE,12,2,hi=set(range(0,6)),hicol=RED)
        f=SANS(190);s='3';tt(d,CX-f.getlength(s)/2-8,CY-125,s,f,DEEP,-0.03);mono(d,CX,CY+80,'seconds',MID,17,'c')
for k in range(5):
    im=Image.new('RGB',(W,H),PAP);d=ImageDraw.Draw(im);frame_labels(d,4+k,T,MID,'Brand clinic')
    tag(d,M,250,f'11.0{k+2}','Test 0'+str(k+1),DEEP,PAP)
    illo(d,k)
    mono(d,M,880,'Five tests for every logo',MID,18)
    olist(d,M,930,tests,k,62,DEEP,FADE,1.1)
    body(d,M,1300,notes[k],26,DEEP,600,w='Medium')
    save(im,4+k)
# 9 close
im=Image.new('RGB',(W,H),DEEP);d=ImageDraw.Draw(im);frame_labels(d,9,T,mix(DEEP,PAP,0.5),'Brand clinic')
mark(d,M,250,92,RED)
head(d,M,520,'',80,PAP,lines=['Send us your logo.','We\'ll tell you the','truth, kindly.'])
body(d,M,840,'Comment 11, then send it to our DMs or email.',28,mix(DEEP,PAP,0.62),700)
body(d,M,950,'hello@may11levenlabs.com',28,PAP,900,w='Medium');body(d,M,992,'may11leven.labs@gmail.com',28,PAP,900,w='Medium')
mono(d,M,1340,'Posted only with your permission',mix(DEEP,PAP,0.45),17)
save(im,9)
