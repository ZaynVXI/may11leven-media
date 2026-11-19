import cv2,numpy as np
src=cv2.imread('../img/hand_dusk_full.jpg')
x0,y0,x1,y1=510,1020,1810,2645
im=src[y0:y1,x0:x1].copy()
h,w=im.shape[:2]
b,g,r=[im[...,i].astype(np.int32) for i in range(3)]
hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
# background: blue/purple sky and sea, fairly saturated
bg=((b>r+25)&(hsv[...,2]>40))
mask=np.full((h,w),cv2.GC_PR_BGD,np.uint8)
mask[bg]=cv2.GC_BGD
skin=(r>b+15)
mask[skin]=cv2.GC_FGD
# phone quad is foreground
q=(np.float32([[920,1298],[1411,1294],[1400,2360],[920,2370]])-[x0,y0]).astype(np.int32)
qm=np.zeros((h,w),np.uint8);cv2.fillConvexPoly(qm,q,255)
body=cv2.dilate(qm,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(30,30)))
mask[body>0]=cv2.GC_FGD
bgd=np.zeros((1,65),np.float64);fgd=np.zeros((1,65),np.float64)
small=cv2.resize(im,(w//2,h//2));ms=cv2.resize(mask,(w//2,h//2),interpolation=cv2.INTER_NEAREST)
cv2.grabCut(small,ms,None,bgd,fgd,5,cv2.GC_INIT_WITH_MASK)
m=np.where((ms==cv2.GC_FGD)|(ms==cv2.GC_PR_FGD),255,0).astype(np.uint8)
m=cv2.resize(m,(w,h),interpolation=cv2.INTER_LINEAR)
m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((5,5),np.uint8))
# keep largest components only (hand+phone, plus sleeve)
n,lab,st,_=cv2.connectedComponentsWithStats((m>127).astype(np.uint8))
keep=np.zeros_like(m)
for i in range(1,n):
    if st[i,cv2.CC_STAT_AREA]>20000: keep[lab==i]=255
keep[:626,:]=0
keep[qm>0]=0  # screen area handled by the drawn body                      # nothing but the phone above the hand
keep=cv2.GaussianBlur(keep,(0,0),4); keep=np.where(keep>127,255,0).astype(np.uint8)   # smooth jaggies
bodyc=cv2.GaussianBlur(body,(0,0),1.0)
keep=cv2.GaussianBlur(keep,(0,0),1.3)
cv2.imwrite('sil_mask.png',keep)
prev=im.copy();prev[keep<128]=(prev[keep<128]*0.25).astype(np.uint8)
cv2.imwrite('/tmp/claude-0/-home-claude/9bb6ffdd-e2cc-582d-b0a9-f807871f658c/scratchpad/maskprev.jpg',cv2.resize(prev,(650,812)))
