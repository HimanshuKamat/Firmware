"""Remove the numerals that Veo baked into the sky of shot 21 (clip time ~4.7-7.9 s).
Colour-key the orange digits, dilate, and replace those pixels with a clean sky plate from t=4.5 s."""
import subprocess, numpy as np
from scipy import ndimage as ndi
SRC='05_clips/raw/shot21_veo.mp4'; OUT='08_edit/work/shot21_fixed.mp4'
W,H,FPS=1920,1080,24
X0,Y0,X1,Y1=1100,110,1400,392          # region the digits live in (keeps Shiva topknot and Ganesha crown out)
dec=subprocess.Popen(['ffmpeg','-v','error','-i',SRC,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
enc=subprocess.Popen(['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
                      '-an','-c:v','libx264','-crf','10','-preset','medium','-pix_fmt','yuv420p',OUT],stdin=subprocess.PIPE)
n=0; plate=None
while True:
    buf=dec.stdout.read(W*H*3)
    if len(buf)<W*H*3: break
    fr=np.frombuffer(buf,dtype=np.uint8).reshape(H,W,3).copy()
    t=n/FPS
    if abs(t-4.5)<0.5/FPS: plate=fr[Y0:Y1,X0:X1].copy()
    if 4.6<=t<=8.0 and plate is not None:
        reg=fr[Y0:Y1,X0:X1].astype(np.float32)/255
        r,g,b=reg[...,0],reg[...,1],reg[...,2]
        mx=reg.max(2); mn=reg.min(2); sat=(mx-mn)/(mx+1e-6)
        # orange/yellow digits: red high, blue low (sky is blue-dominant, leaves green-dominant, clouds neutral)
        m=(r>0.55)&(r>b+0.28)&(r>=g-0.02)&(sat>0.45)
        m=ndi.binary_opening(m,iterations=1)
        m=ndi.binary_dilation(m,iterations=11)
        a=ndi.gaussian_filter(m.astype(np.float32),4)[...,None]
        a=np.clip(a*1.4,0,1)
        # fade the patch in/out around the digit lifetime so nothing pops
        k=min(1,(t-4.6)/0.25,(8.0-t)/0.25)
        a=a*max(0,k)
        out=reg*(1-a)+(plate.astype(np.float32)/255)*a
        fr[Y0:Y1,X0:X1]=(out*255+0.5).astype(np.uint8)
    enc.stdin.write(fr.tobytes()); n+=1
enc.stdin.close(); enc.wait(); dec.wait(); print('frames',n)
