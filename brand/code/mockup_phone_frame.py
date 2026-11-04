from PIL import Image, ImageDraw, ImageFilter
import numpy as np
def phone(screen, w=420):
    # screen: PIL image 390x844 aspect; returns RGBA phone w wide
    h=int(w*2.06); r=int(w*0.15)
    body=Image.new('RGBA',(w,h),(0,0,0,0)); d=ImageDraw.Draw(body)
    d.rounded_rectangle((0,0,w-1,h-1),radius=r,fill=(42,42,44,255))
    d.rounded_rectangle((3,3,w-4,h-4),radius=r-3,fill=(18,18,19,255))
    b=int(w*0.035); sw,sh=w-2*b,h-2*b
    scr=screen.convert('RGB').resize((sw,sh),Image.LANCZOS)
    m=Image.new('L',(sw,sh),0);ImageDraw.Draw(m).rounded_rectangle((0,0,sw-1,sh-1),radius=r-b,fill=255)
    body.paste(scr,(b,b),m)
    iw,ih=int(w*0.28),int(w*0.075); d.rounded_rectangle(((w-iw)//2,b+int(w*0.03),(w+iw)//2,b+int(w*0.03)+ih),radius=ih//2,fill=(8,8,8,255))
    # subtle edge highlight
    hl=Image.new('RGBA',(w,h),(0,0,0,0));ImageDraw.Draw(hl).rounded_rectangle((1,1,w-2,h-2),radius=r-1,outline=(255,255,255,40),width=2)
    return Image.alpha_composite(body,hl)
def place(bg,ph,xy,shadow=0.45):
    x,y=xy; a=ph.split()[3]
    sh=Image.new('L',bg.size,0); sh.paste(a,(x+18,y+34)); sh=sh.filter(ImageFilter.GaussianBlur(38))
    bg=Image.composite(Image.new('RGB',bg.size,(10,14,14)),bg,sh.point(lambda v:int(v*shadow)))
    bg.paste(ph,(x,y),ph); return bg
