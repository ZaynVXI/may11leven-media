"""Designed sound for Try to break it No. 01, synthesised (no samples, nothing AI). 48 kHz stereo."""
import numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt
SR=48000; DUR=31.0; N=int(SR*DUR); rng=np.random.default_rng(1)
out=np.zeros((N,2))
def bp(x,lo,hi): return sosfilt(butter(2,[lo,hi],btype='band',fs=SR,output='sos'),x)
def lp(x,f): return sosfilt(butter(2,f,btype='low',fs=SR,output='sos'),x)
def add(t,sig,g=1.0,pan=0.0):
    i=int(t*SR); j=min(N,i+len(sig)); s=sig[:j-i]*g; out[i:j,0]+=s*(1-pan); out[i:j,1]+=s*(1+pan)
def env(n,a,d): e=np.ones(n); A=max(1,int(a*SR)); D=max(1,int(d*SR)); e[:A]=np.linspace(0,1,A); e[-D:]*=np.linspace(1,0,D); return e
# night room tone + far sea wash (slow-modulated low noise)
room=lp(rng.standard_normal(N),700)*0.004; tt=np.arange(N)/SR
sea=lp(rng.standard_normal(N),300)*(0.5+0.5*np.sin(2*np.pi*tt/7.5))**2*0.006
out+=(room+sea)[:,None]
def key(t,g=.16,pan=0):  # a soft phone-keyboard tap
    n=int(.03*SR); c=bp(rng.standard_normal(n),1200,4200)*np.exp(-np.linspace(0,9,n)); add(t,c,g,pan)
def printer(t,dur,g=.05):  # thermal printer: buzzy stepper whine
    n=int(dur*SR); u=np.arange(n)/SR
    x=np.sign(np.sin(2*np.pi*190*u))*.3+bp(rng.standard_normal(n),900,3500)*.6
    x=bp(x,300,5000)*(0.6+0.4*np.sin(2*np.pi*34*u))*env(n,.04,.08); add(t,x,g)
def stamp(t,g=.6):
    n=int(.35*SR); u=np.arange(n)/SR
    s=np.sin(2*np.pi*62*u)*np.exp(-u*18)+lp(rng.standard_normal(n),700)*np.exp(-u*30)*.6
    add(t,s,g); add(t,bp(rng.standard_normal(int(.01*SR)),3000,8000)*.5,.2)
def slide(t,g=.07,pan=0):
    n=int(.32*SR); u=np.linspace(0,1,n); add(t,bp(rng.standard_normal(n),600,4000)*np.sin(np.pi*u)**2,g,pan)
def tick(t,g=.06):
    n=int(.02*SR); add(t,bp(rng.standard_normal(n),2500,7000)*np.exp(-np.linspace(0,7,n)),g)
# A
for i in range(7): key(max(0.02,i*.16-.3)+.02,.15,.2*np.sin(i))
printer(2.1,.9); stamp(3.3)
# C
slide(4.82,.09); 
# D: four attempts of 3 s
for k in range(4):
    b=7.2+3*k; slide(b+.01,.05,(k%2)*.4-.2)
    nw=[7,7,5,8][k]
    for i in range(nw): key(b+i*.12+.02,.13,.25*np.sin(i+k))
    printer(b+.8,.6); stamp(b+1.9,.55)
# E
slide(19.2,.08)
for k in range(13): tick(19.5+k*.28)
# F + G: low chord swells under the point and the end, fades into the loop
n=int((DUR-23.8)*SR); u=np.arange(n)/SR
ch=sum(np.sin(2*np.pi*f*u+ph)*g for f,ph,g in [(98,0,1),(146.8,1,.6),(196,2,.35),(246.9,.5,.2)])
add(23.8,lp(ch,1100)*env(n,1.4,1.0)*0.05)
out=np.clip(out,-1,1); out=out/np.max(np.abs(out))*0.7
sf.write('reel_sound.wav',out,SR); print('ok')
