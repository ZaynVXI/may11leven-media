import numpy as np
LAT=[(0.02,0.10),(0.10,0.165),(0.25,0.16),(0.45,0.145),(0.62,0.19),(0.76,0.205),(0.88,0.18),(0.96,0.11),(1.0,0.02)]
MED=[(0.985,-0.07),(0.90,-0.15),(0.76,-0.195),(0.62,-0.17),(0.47,-0.085),(0.30,-0.10),(0.15,-0.14),(0.05,-0.12),(0.0,-0.02)]
def chaikin(p,n=6):
    p=np.array(p,float)
    for _ in range(n):
        q=np.roll(p,-1,0);p=np.stack([0.75*p+0.25*q,0.25*p+0.75*q],1).reshape(-1,2)
    return p
def outline(n=None,L=0.28,mirror=1):
    p=chaikin(LAT+MED)
    return [((x-0.5)*L, y*L*0.85*mirror) for x,y in p]
