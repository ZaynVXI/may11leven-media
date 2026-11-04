from PIL import Image,ImageDraw,ImageFont
IT='/home/claude/kit/fonts/InterTight-Medium.ttf';PM='/home/claude/kit/fonts/PlexMono.ttf'
def label(out,bag,ink,name,region,notes):
    W,H=1200,1800;im=Image.new('RGB',(W,H),bag);d=ImageDraw.Draw(im)
    f=ImageFont.truetype(IT,190);t='imisozi';d.text(((W-f.getlength(t))/2,560),t,font=f,fill=ink)
    m=ImageFont.truetype(PM,44)
    for i,s in enumerate([name.upper(),region.upper()]):
        d.text(((W-m.getlength(s))/2,820+i*64),s,font=m,fill=ink)
    # hills line motif: three arcs
    import math
    for k in range(3):
        cx=W/2-180+k*180;r=150
        d.arc((cx-r,1150-r,cx+r,1150+r),200,340,fill=ink,width=6)
    s=ImageFont.truetype(PM,36)
    for i,n in enumerate(notes): d.text(((W-s.getlength(n))/2,1350+i*56),n,font=s,fill=ink)
    d.text(((W-s.getlength('250 G · WHOLE BEAN'))/2,1620),'250 G · WHOLE BEAN',font=s,fill=ink)
    im.save(out)
label('tex/huye.png',(30,26,23),(239,234,226),'Huye Mountain','Southern Province',['washed · 1,800 m','red plum, black tea'])
label('tex/nyam.png',(150,68,46),(246,238,228),'Nyamasheke','Lake Kivu',['natural · 1,700 m','hibiscus, cacao'])
label('tex/gak.png',(92,104,78),(240,236,226),'Gakenke','Northern Province',['honey · 1,900 m','brown sugar, citrus'])
