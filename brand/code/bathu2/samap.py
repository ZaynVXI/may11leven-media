import json,numpy as np
from PIL import Image,ImageDraw
t=json.load(open('package/countries-10m.json'))
sx,sy=t['transform']['scale'];tx,ty=t['transform']['translate']
arcs=[]
for a in t['arcs']:
    x=y=0;pts=[]
    for dx,dy in a: x+=dx;y+=dy;pts.append((x*sx+tx,y*sy+ty))
    arcs.append(pts)
def ring(idx):
    out=[]
    for i in idx:
        p=arcs[i] if i>=0 else arcs[~i][::-1]
        out+=p if not out else p[1:]
    return out
def geom(cid):
    for g in t['objects']['countries']['geometries']:
        if g.get('id')==cid: return g
def polys(g):
    if g['type']=='Polygon': return [[ring(r) for r in g['arcs']]]
    return [[ring(r) for r in p] for p in g['arcs']]
za=polys(geom('710'));ls=polys(geom('426'))
json.dump({'za':za,'ls':ls},open('za.json','w'))
print(len(za),[len(p[0]) for p in za][:5])
