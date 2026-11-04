import sys
from PIL import Image, ImageOps
def thumb(p,w=360):
    im=Image.open(p).convert('RGB'); return ImageOps.fit(im,(w,int(w*4/3)),Image.LANCZOS)
def grid(paths,out,w=360,gap=3,bg=(0,0,0)):
    rows=(len(paths)+2)//3;H=int(w*4/3)
    G=Image.new('RGB',(3*w+2*gap,rows*H+(rows-1)*gap),bg)
    for i,p in enumerate(paths): G.paste(thumb(p,w),((i%3)*(w+gap),(i//3)*(H+gap)))
    G.save(out,quality=90);return G
if __name__=='__main__':
    grid(sys.argv[2:],sys.argv[1])
