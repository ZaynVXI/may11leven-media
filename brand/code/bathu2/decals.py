import sys;sys.path.insert(0,'/home/claude/bathu2')
from sole import outline
from PIL import Image,ImageDraw,ImageFont
IT='/home/claude/kit/fonts/InterTight-Medium.ttf';PM='/home/claude/kit/fonts/PlexMono.ttf'
def mark(d,cx,cy,s,cA,cB):
    for mirror,dx,dy,col,rot in ((-1,-0.2,0.25,cA,0),(1,0.2,-0.25,cB,0)):
        pts=outline(mirror=mirror)
        # rotate 90deg so toe points up
        P=[(cx+(-y+dx*0.28)*s, cy+(-x+dy*0.28)*s) for x,y in pts]
        d.polygon(P,fill=col)
def lid(out,ink,gum):
    im=Image.new('RGBA',(2048,1304),(0,0,0,0));d=ImageDraw.Draw(im)
    mark(d,1024,640,2600,ink,gum);im.save(out)
def front(out,ink):
    im=Image.new('RGBA',(2048,460),(0,0,0,0));d=ImageDraw.Draw(im)
    d.text((70,120),'bathu',font=ImageFont.truetype(IT,190),fill=ink)
    f=ImageFont.truetype(PM,54);t='EVERY STEP IS A STORY';d.text((2048-70-f.getlength(t),190),t,font=f,fill=ink)
    im.save(out)
lid('tex/lid_black.png',(236,234,229,255),(168,114,63,255));front('tex/front_black.png',(236,234,229,255))
lid('tex/lid_orange.png',(12,12,11,255),(140,88,42,255));front('tex/front_orange.png',(20,20,19,255))
