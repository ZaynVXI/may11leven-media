import sys;sys.path.insert(0,'/home/claude/remake/v3')
from mm import *
K='/home/claude/kivu/'
GREY=(222,224,221);CARD=(255,255,255);PAP=(237,230,214);LAKE=(34,57,58);BAS=(23,22,20);CLAY=(176,96,58);MOSS=(107,116,88)
INK=(24,24,22);MID=(120,122,118);FADE=(190,192,188)
T=6;out='/home/claude/remake/v3/out/'
def save(im,n): grain(im,2.0,40+n).save(out+f'w-{n}.jpg',quality=94)
Image.open('/home/claude/remake/cov/w-0.jpg').convert('RGB').save(out+'w-1.jpg',quality=95)
full=Image.open(K+'desk_full.png').convert('RGB');Y2=int(sys.argv[1]) if len(sys.argv)>1 else 0   # 2880 wide page
def page(y0,h,w=None):
    return full.crop((0,y0,2880,y0+h))
# 2 site board on grey: hero card + two cropped section cards (they bleed off the frame)
im=Image.new('RGB',(W,H),GREY);d=ImageDraw.Draw(im)
hero=page(0,1800).resize((1000,625),Image.LANCZOS);round_paste(im,hero,(40,150),26)
s2=full.crop((0,1800+Y2,2880,1800+Y2+1613)).resize((1000,560),Image.LANCZOS);round_paste(im,s2,(40,800),26)
d=ImageDraw.Draw(im);mono(d,40,90,'Inzu Lake House — concept',INK,17);mono(d,W-40,90,'02/06',INK,17,'r')
save(im,2)
# 3 mobile: three screens as rounded cards, middle one raised
im=Image.new('RGB',(W,H),GREY);d=ImageDraw.Draw(im)
mob=Image.open(K+'mob_full.png').convert('RGB')
cw=320;ch=int(cw*2532/1170)
ys=[0,2532,5200]
xs=[48,380,712];yy=[420,340,420]
for i in range(3):
    c=mob.crop((0,ys[i],1170,ys[i]+2532)).resize((cw,ch),Image.LANCZOS);round_paste(im,c,(xs[i],yy[i]),40,shadow=True)
d=ImageDraw.Draw(im);mono(d,M-16,90,'Built mobile-first · 390',INK,17);mono(d,W-M+16,90,'03/06',INK,17,'r')
save(im,3)
# 4 statement + numbers (sage-white card)
SAGE=(235,240,236)
im=Image.new('RGB',(W,H),SAGE);d=ImageDraw.Draw(im);frame_labels(d,4,T,MID,'Inzu Lake House')
tag(d,M,250,'11.01','The idea',INK,SAGE)
head(d,M,420,'',72,INK,lines=['A hotel website','should sell the','mornings, not the','room count.'])
y=1000
for k,(n,lab) in enumerate([('12','rooms'),('1','lake'),('3','steps to book')]):
    x=M+k*320;d.line((x,y,x+290,y),fill=FADE,width=2)
    tt(d,x,y+24,n,SANS(96),INK,-0.03);mono(d,x,y+150,lab,MID,17)
body(d,M,1290,'Concept identity and website for an invented hotel in Karongi, Rwanda. Not a client.',24,MID,600)
save(im,4)
# 5 brand system page
im=Image.new('RGB',(W,H),CARD);d=ImageDraw.Draw(im);frame_labels(d,5,T,MID,'Inzu Lake House')
tag(d,M,250,'11.02','Brand system',INK,CARD)
CG=lambda s,i=False: ImageFont.truetype(K+'fonts/cormorant-garamond-latin-300-%s.ttf'%('italic' if i else 'normal'),s)
HG=lambda s: ImageFont.truetype(K+'fonts/hanken-grotesk-latin-400-normal.ttf',s)
d.text((M-8,360),'Aa',font=CG(300),fill=INK)
d.text((470,420),'Cormorant',font=CG(78),fill=INK);d.text((472,506),'Garamond, light',font=CG(46,True),fill=MID)
d.text((470,600),'Hanken Grotesk',font=HG(36),fill=INK);d.text((472,648),'prices, dates, booking',font=HG(26),fill=MID)
sw=[('Papyrus',PAP,'#EDE6D6'),('Lake',LAKE,'#22393A'),('Basalt',BAS,'#171614'),('Clay',CLAY,'#B0603A'),('Moss',MOSS,'#6B7458')]
x=M;w=(W-2*M-4*14)//5;y=860
for n,c,hx in sw:
    d.rounded_rectangle((x,y,x+w,y+400),radius=18,fill=c,outline=(220,214,200) if n=='Papyrus' else None,width=2)
    tc=INK if n=='Papyrus' else (240,234,222)
    tt(d,x+18,y+400-74,n,SANS(26),tc,-0.02);mono(d,x+18,y+400-38,hx,tc,15);x+=w+14
body(d,M,1300,'Taken from the lake at dawn, the volcanic stone of the terrace and the clay walls.',24,MID,700)
save(im,5)
# 6 close (lake)
im=Image.new('RGB',(W,H),LAKE);d=ImageDraw.Draw(im);L2=mix(LAKE,PAP,0.55)
frame_labels(d,6,T,L2,'Web design')
mark(d,M,250,92,PAP)
head(d,M,520,'',80,PAP,lines=['Your website is','open 24/7.'])
head(d,M,686,'',80,L2,lines=['Is it selling 24/7?'])
body(d,M,860,'Comment 11 for a free homepage review, or email us.',28,L2,760)
body(d,M,960,'hello@may11levenlabs.com',28,PAP,900,w='Medium');body(d,M,1002,'may11leven.labs@gmail.com',28,PAP,900,w='Medium')
mono(d,M,1340,'Your taste. Our machines.',mix(LAKE,PAP,0.35),17)
save(im,6)
