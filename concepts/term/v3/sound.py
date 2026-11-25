"""Designed sound for the Term reel, synthesised (no samples, nothing AI). 48 kHz stereo."""
import numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt
SR=48000; DUR=27.4; N=int(SR*DUR); rng=np.random.default_rng(11)
out=np.zeros((N,2))
def bp(x,lo,hi): return sosfilt(butter(2,[lo,hi],btype='band',fs=SR,output='sos'),x)
def lp(x,f): return sosfilt(butter(2,f,btype='low',fs=SR,output='sos'),x)
def add(t,sig,gain=1.0,pan=0.0):
    i=int(t*SR); j=min(N,i+len(sig)); s=sig[:j-i]*gain
    out[i:j,0]+=s*(1-pan)/1; out[i:j,1]+=s*(1+pan)/1
def env(n,a,d): e=np.ones(n); A=int(a*SR); D=int(d*SR); e[:A]=np.linspace(0,1,A); e[-D:]*=np.linspace(1,0,D); return e
# room tone
room=lp(rng.standard_normal(N),900)*0.004; out+=room[:,None]
# A: counter ticks speeding up then slowing (0.5-1.7)
for k in range(14):
    u=k/13; t=0.5+1.2*(1-(1-u)**3)
    n=int(.012*SR); c=bp(rng.standard_normal(n),2500,6000)*np.exp(-np.linspace(0,8,n)); add(t,c,0.18,0.15*np.sin(k))
# B: cloth thump as the tape lands (3.1)
n=int(.25*SR); th=lp(rng.standard_normal(n),400)*np.exp(-np.linspace(0,9,n)); add(3.12,th,0.6)
# C: a muted pluck for the notification (5.5)
n=int(.5*SR); tt=np.arange(n)/SR; pl=(np.sin(2*np.pi*660*tt)+.5*np.sin(2*np.pi*990*tt))*np.exp(-tt*9); add(5.5,lp(pl,3000),0.08)
# pen stroke: down-stroke, beat, up-stroke
def pen(dur):
    n=int(dur*SR); x=bp(rng.standard_normal(n),2200,7500)
    u=np.linspace(0,1,n); a=np.where(u<.38,np.sin(np.pi*u/.38)*.8,np.where(u<.48,.05,np.sin(np.pi*(u-.48)/.52)))
    grain=1+.5*bp(rng.standard_normal(n),20,80)/3; return x*a*grain
add(10.0,pen(0.8),0.22,-0.1)                       # D: the tick in close-up
for k in range(5,12): add(14.3+(k-5)*.42,pen(.34),0.16,0.25*((k%3)-1))   # E: the register fills
# F: paper slides
for k in range(4):
    n=int(.3*SR); u=np.linspace(0,1,n); x=bp(rng.standard_normal(n),600,4000)*np.sin(np.pi*u)**2
    add(17.75+k*1.05,x,0.07,0.2*(k%2*2-1))
# G: stamp (23.2): low thud, body, click
n=int(.35*SR); tt=np.arange(n)/SR
st=np.sin(2*np.pi*62*tt)*np.exp(-tt*18)+lp(rng.standard_normal(n),700)*np.exp(-tt*30)*.6
cl=bp(rng.standard_normal(int(.01*SR)),3000,8000)*.5
add(23.2,st,0.7); add(23.2,cl,0.25)
# H: a soft low chord, swelling then fading into the loop
n=int((DUR-24.6)*SR); tt=np.arange(n)/SR
ch=sum(np.sin(2*np.pi*f*tt+ph)*g for f,ph,g in [(110,0,1),(164.8,1,.6),(220,2,.35),(277.2,.5,.25)])
ch=lp(ch,1200)*env(n,1.2,0.6)*0.06; add(24.6,ch,1.0)
out=np.clip(out,-1,1); peak=np.max(np.abs(out)); out=out/peak*0.7
sf.write('reel_sound.wav',out,SR); print('ok',peak)
