import cv2,numpy as np
im=cv2.imread('u1.jpg').astype(np.float32);H,W=im.shape[:2]
dst=(np.array([[88,172],[938,62],[990,650],[118,684]],np.float32)+np.array([600,820],np.float32)).astype(np.float32)
src=cv2.imread('screen_full.png').astype(np.float32);h,w=src.shape[:2]
M=cv2.getPerspectiveTransform(np.array([[0,0],[w,0],[w,h],[0,h]],np.float32),dst)
warp=cv2.warpPerspective(src,M,(W,H),flags=cv2.INTER_AREA)
mask=cv2.warpPerspective(np.ones((h,w),np.float32),M,(W,H));mask=cv2.GaussianBlur(mask,(0,0),0.8)[:,:,None]
# match the photo: softness, tone, white balance, grain
warp=cv2.GaussianBlur(warp,(0,0),1.15)
warp=(warp/255.0)**1.06*255*0.9+8          # slightly lower contrast, lifted blacks like a real panel
warp[:,:,0]*=0.96; warp[:,:,2]*=1.03       # warm cast of the room (BGR)
yy,xx=np.mgrid[0:H,0:W].astype(np.float32)
glare=np.clip(1-((xx-1450)**2/650**2+(yy-1000)**2/420**2),0,1)[:,:,None]*16
warp=warp+glare
rng=np.random.default_rng(7);warp=warp+rng.normal(0,4.2,warp.shape[:2])[:,:,None]
out=im*(1-mask)+warp*mask
spill=cv2.GaussianBlur(mask[:,:,0],(0,0),110)[:,:,None]*np.array([26,20,14],np.float32)
out=np.clip(out+spill*0.3*(1-mask),0,255).astype(np.uint8)
cv2.imwrite('laptop_full.jpg',out,[cv2.IMWRITE_JPEG_QUALITY,95])
cv2.imwrite('m_laptop.jpg',cv2.resize(out[700:2567,500:1900],(1080,1440),interpolation=cv2.INTER_AREA),[cv2.IMWRITE_JPEG_QUALITY,95])
cv2.imwrite('/tmp/claude-0/-home-claude/9bb6ffdd-e2cc-582d-b0a9-f807871f658c/scratchpad/lz.jpg',out[820:1600,600:1700])
