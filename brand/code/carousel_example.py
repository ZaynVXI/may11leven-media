from type2 import *
from comp import pano, grain
import numpy as np
LINE=(208,204,196)
def corners2(d,left,right,col,bl='@may11leven.labs',br='Your taste. Our machines.'):
    label(d,(64,64),left,col); label(d,(64,64),right,col,anchor='r')
    label(d,(64,1440-84),bl,col); label(d,(64,1440-84),br,col,anchor='r')
def photo_slide(im,lines,sub,col,subcol,n,series,y=930,sz=86,subw=600):
    d=ImageDraw.Draw(im); label(d,(64,64),'May11Leven Labs',col); label(d,(64,64),f'{series} — 0{n}/05',col,anchor='r')
    y2=rich(d,64,y,lines,sz,col); para(d,64,y2+24,sub,29,subcol,subw,w='Medium'); return im
def list_card(title,intro,items,foot,series,n):
    im=Image.new('RGB',(1080,1440),BONE);d=ImageDraw.Draw(im)
    corners2(d,'May11Leven Labs',f'{series} — 0{n}/05',ASH)
    label(d,(64,190),'[11]',IR,sz=22)
    rich(d,64,232,title,78,INK)
    para(d,64,410,intro,28,ASH,800)
    y=530
    for k,(a,b) in enumerate(items):
        d.line((64,y-30,1016,y-30),fill=LINE,width=2)
        label(d,(64,y+6),f'0{k+1}',IR,sz=20)
        ttext(d,(160,y-8),a,SANS(50),INK,-0.02)
        d.text((160,y+56),b,font=SANS(26),fill=ASH); y+=140
    d.line((64,y-30,1016,y-30),fill=LINE,width=2)
    para(d,64,y+6,foot,28,INK,760)
    return im
def close_card(lines,ask,series,n):
    im=Image.new('RGB',(1080,1440),INK);d=ImageDraw.Draw(im)
    corners2(d,'May11Leven Labs',f'{series} — 0{n}/05',ASH)
    mark(d,64,380,150)
    y=rich(d,64,640,lines,92,BONE,accent=IR,lead=1.06)
    para(d,64,y+44,ask,28,ASH,800)
    f=SANS(32,'Medium');d.text((64,y+130),'hello@may11levenlabs.com',font=f,fill=BONE);d.text((64,y+180),'may11leven.labs@gmail.com',font=f,fill=BONE)
    return im
# ---- clinic
S='Brand clinic'
sl,_=pano('wall.png',1.15,470,200)
photo_slide(sl[0],[[('Your logo has','s')],[('one ','s'),('job.','i')]],'Be remembered after one look.',INK,(28,24,23),1,S)
photo_slide(sl[1],[[('Nothing is wrong','s')],[('with your ','s'),('business.','i')]],"Maybe your logo just hasn't caught up with it.",INK,(28,24,23),2,S)
photo_slide(sl[2],[[('The street','s')],[("doesn't ",'s'),('slow down.','i')]],'Your sign gets one look from a passing moto. Make it count.',INK,(28,24,23),3,S)
for i in range(3): grain(sl[i],4).save(f'clinic-{i+1}.jpg',quality=93)
list_card([[('Free brand ','s'),('clinic.','i')]],'Five tests we run on every logo.',
 [('16px','Still readable as a phone tab icon?'),('One colour','Does it survive a single-colour stamp?'),('Across the street','Readable on a shopfront from a moving moto?'),('Black and white','Does it hold on a cheap receipt print?'),('Three seconds','Could someone sketch it after one look?')],
 'You get what already works, what holds you back, and a quick direction if it needs one. Free.',S,4).save('clinic-4.jpg',quality=95)
grain(close_card([[('Send us your logo.','s')],[("We'll tell you the",'s')],[('truth, ','s'),('kindly.','i')]],'Comment 11, then send it to our DMs or email:',S,5),3).save('clinic-5.jpg',quality=95)
# ---- app
S="The app we'd build"
sl,full=pano('barber_app.png',1.0,0,90)
g=Image.new('L',(3240,1440),0);gd=ImageDraw.Draw(g)
for y in range(820,1440): gd.line((0,y,3240,y),fill=int(225*((y-820)/620)**1.3))
full=Image.composite(Image.new('RGB',(3240,1440),INK),full,g)
sl=[full.crop((i*1080,0,i*1080+1080,1440)) for i in range(3)]
sub=(214,208,200)
photo_slide(sl[0],[[('Saturday.','s')],[('Queue no. ','s'),('07.','i')]],'Forty minutes on a plastic chair. Half the room walks out.',BONE,sub,1,S,y=1100,sz=76)
photo_slide(sl[1],[[('The queue,','s')],[('in their ','s'),('pocket.','i')]],"They see their place from home and tap \"I'm on my way\".",BONE,sub,2,S,y=1100,sz=76)
photo_slide(sl[2],[[('Every walk-out is','s')],[('a cut you ','s'),('lost.','i')]],'So we sketched the app that keeps them: bookings, reminders, M-Pesa.',BONE,sub,3,S,y=1100,sz=76,subw=640)
for i in range(3): grain(sl[i],4).save(f'app-{i+1}.jpg',quality=93)
list_card([[("The app we'd ",'s'),('build.','i')]],'Concept for "fade.", an invented barbershop in Westlands.',
 [('Live queue','Customers see their place from home'),("\"I'm on my way\"",'One tap, and the barber knows'),('Quiet-hour bookings','Fill the slow Tuesday mornings'),('M-Pesa payments','No cash, no change, no waiting'),('Reminders','Fewer no-shows, more regulars')],
 'Not a barber? The same idea works for salons, clinics, restaurants, schools and delivery.',S,4).save('app-4.jpg',quality=95)
grain(close_card([[('Your customers','s')],[('already have a phone.','s')],[('Give them a ','s'),('reason.','i')]],'Comment 11 for a free app idea for your business:',S,5),3).save('app-5.jpg',quality=95)
