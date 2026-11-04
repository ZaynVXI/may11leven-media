import sys;sys.path.insert(0,'/home/claude/remake/v3')
from mm import *
INKB=(17,16,15);BONE=(236,232,224);OR=(255,84,34);MID=mix(INKB,BONE,0.55);FADE=mix(INKB,BONE,0.24)
T=6;out='/home/claude/remake/v3/out/'
def save(im,n): grain(im,2.6,20+n).save(out+f'app-{n}.jpg',quality=94)
Image.open('/home/claude/remake/cov/app-0.jpg').convert('RGB').save(out+'app-1.jpg',quality=95)
# 2 the tray, clean, one caption
b=Image.open('/home/claude/remake/barber.png').convert('RGB')
im=cover_crop(b.crop((0,0,1240,1620)),W,H,0.5,0.5)
sh=Image.new('L',(W,H),0);sd=ImageDraw.Draw(sh)
for y in range(1120,H): sd.line((0,y,W,y),fill=int(170*((y-1120)/320)**1.3))
im=Image.composite(Image.new('RGB',(W,H),INKB),im,sh);d=ImageDraw.Draw(im)
frame_labels(d,2,T,BONE,'The app we\'d build')
mono(d,M,1330,'Saturday · Westlands · queue no. 07',BONE,19)
save(im,2)
# 3 statement
im=Image.new('RGB',(W,H),INKB);d=ImageDraw.Draw(im);frame_labels(d,3,T,MID,'The app we\'d build')
tag(d,M,250,'11.01','The problem',BONE,INKB)
head(d,M,420,'',78,BONE,lines=['Every walk-out is','a cut you lost.'])
head(d,M,600,'',78,MID,lines=['So we sketched','the app that','keeps them.'])
body(d,620,1170,'Concept for "fade.", an invented barbershop in Westlands, Nairobi. Not a client.',24,MID,396)
save(im,3)
# 4 the number that matters
im=Image.new('RGB',(W,H),INKB);d=ImageDraw.Draw(im);frame_labels(d,4,T,MID,'The app we\'d build')
tag(d,M,250,'11.02','Live queue',BONE,INKB)
CX,CY,R=W//2,720,330
ring(d,CX,CY,R,150,FADE,16,2,hi=set(range(0,32)),hicol=OR)
f=SANS(330);s='2';tt(d,CX-f.getlength(s)/2-6,CY-250,s,f,BONE,-0.03)
mono(d,CX,CY+120,'people ahead of you',MID,19,'c')
mono(d,CX+R+0,CY-R-10,'≈ 12 min',OR,19,'r')
body(d,M,1170,'They see their place from home,',30,BONE,900,w='Medium')
body(d,M,1212,'and tap "I\'m on my way" when it\'s close.',30,MID,900,w='Medium')
save(im,4)
# 5 features with the screen
im=Image.new('RGB',(W,H),INKB);d=ImageDraw.Draw(im);frame_labels(d,5,T,MID,'The app we\'d build')
scr=Image.open('/home/claude/remake/app_screen.png').convert('RGB')
sw=430;scr=scr.resize((sw,int(scr.height*sw/scr.width)),Image.LANCZOS)
ph=Image.new('RGB',(sw+24,scr.height+24),(40,38,36));round_paste(ph,scr,(12,12),54)
round_paste(im,ph,(W-M-ph.width+40,250),64,shadow=True)
d=ImageDraw.Draw(im)
tag(d,M,250,'11.03','What it does',BONE,INKB)
items=['Live queue','"I\'m on my way"','Quiet-hour bookings','M-Pesa payments','Reminders']
y=470
for i,s in enumerate(items):
    mono(d,M,y,f'0{i+1}',MID,17);head(d,M,y+30,'',40,BONE if i==0 else mix(INKB,BONE,0.78),lines=[s],tr=-0.025);y+=128
body(d,M,1170,'Not a barber? The same idea works for salons, clinics, restaurants, schools and delivery.',24,MID,470)
save(im,5)
# 6 close
im=Image.new('RGB',(W,H),INKB);d=ImageDraw.Draw(im);frame_labels(d,6,T,MID,'The app we\'d build')
mark(d,M,250,92,OR)
head(d,M,520,'',80,BONE,lines=['Your customers','already have a phone.'])
head(d,M,686,'',80,MID,lines=['Give them a reason.'])
body(d,M,860,'Comment 11 for a free app idea for your business.',28,MID,760)
body(d,M,960,'hello@may11levenlabs.com',28,BONE,900,w='Medium');body(d,M,1002,'may11leven.labs@gmail.com',28,BONE,900,w='Medium')
mono(d,M,1340,'Your taste. Our machines.',FADE,17)
save(im,6)
