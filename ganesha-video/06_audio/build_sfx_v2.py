#!/usr/bin/env python3
"""SFX track v2 (mono, 48 kHz) on the NO-INTRO timeline (shot 02 = 0 s, 274 s long).
Real-length looping ambience beds (seamless crossfaded loops), slowed big-bird wing flaps, foley, varied squeaks and
pitch-stepped counting pops. Levels are set per file from measured peaks/loudness so nothing is loud or sudden.
Outputs sfx_track_v2.wav and sfx_cues_v2.json."""
import subprocess, json, numpy as np
from scipy.io import wavfile
from scipy.signal import resample_poly
SR=48000; TOTAL=274.5
D='/home/user/Firmware/ganesha-video/06_audio/'
def load(path):
    raw=subprocess.run(['ffmpeg','-v','error','-i',path,'-ac','1','-ar',str(SR),'-f','f32le','-'],capture_output=True,check=True).stdout
    return np.frombuffer(raw,dtype=np.float32).copy()
def pk_db(x): return 20*np.log10(np.abs(x).max()+1e-9)
def lufs(x):
    # integrated loudness via ffmpeg ebur128 (mono file)
    import tempfile, os
    f=tempfile.mktemp(suffix='.wav'); wavfile.write(f,SR,x.astype(np.float32))
    out=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',f,'-af','ebur128','-f','null','-'],capture_output=True,text=True).stderr
    os.remove(f); import re; return float(re.findall(r'I:\s+(-?[\d.]+) LUFS',out)[-1])
stem=np.zeros(int(TOTAL*SR),dtype=np.float32); cues=[]
def fade(n,fi,fo):
    g=np.ones(n,dtype=np.float32)
    a=int(fi*SR); b=int(fo*SR)
    if a>0: a=min(a,n); g[:a]=np.sin(np.linspace(0,np.pi/2,a))**1
    if b>0: b=min(b,n); g[n-b:]*=np.cos(np.linspace(0,np.pi/2,b))**1
    return g
def place(x,t,gain_db,fi=0.01,fo=0.05,name='',note=''):
    n=len(x); g=10**(gain_db/20)*fade(n,fi,fo); i=int(round(t*SR)); j=min(i+n,len(stem))
    stem[i:j]+=(x*g)[:j-i]; cues.append({'file':name,'t':round(t,2),'gain_db':round(float(gain_db),1),'dur':round(n/SR,2),'note':note})
def to_peak(x,target): return target-pk_db(x)
def make_loop(x,xf=1.0):
    x=x[:int(30.0*SR)]; N=len(x); o=int(xf*SR)
    th=np.linspace(0,np.pi/2,o); cross=x[N-o:]*np.cos(th)+x[:o]*np.sin(th)
    return np.concatenate([cross,x[o:N-o]]).astype(np.float32)
def bed(unit,t0,t1,lufs_target,src_lufs,fi,fo,name,note=''):
    n=int((t1-t0)*SR); reps=n//len(unit)+2; x=np.tile(unit,reps)[:n]
    place(x,t0,lufs_target-src_lufs,fi,fo,name,note)
S1=D+'sfx/'; S2=D+'sfx_v2/'
# ---------- ambience beds (loudness-targeted, mono LUFS ~20 dB under narration) ----------
amb={k:load(S2+k+'.mp3') for k in ('AMB_MORNING','AMB_SKY','AMB_EVENING')}
L={k:lufs(v) for k,v in amb.items()}; U={k:make_loop(v) for k,v in amb.items()}
bed(U['AMB_MORNING'],0,88.5,-37,L['AMB_MORNING'],2.0,4.5,'AMB_MORNING','shots 02-12')
bed(U['AMB_SKY'],84.0,107.0,-35,L['AMB_SKY'],4.0,4.5,'AMB_SKY','flight, shots 12-14')
bed(U['AMB_MORNING'],102.5,220.5,-37,L['AMB_MORNING'],4.5,4.5,'AMB_MORNING','shots 15-28')
bed(U['AMB_EVENING'],216.0,274.5,-37,L['AMB_EVENING'],4.5,5.0,'AMB_EVENING','shots 29-33, fades with the end screen')
# ---------- foley ----------
fl=load(S2+'WING_FLAPS.mp3'); fl_slow=resample_poly(fl,1,2).astype(np.float32)        # half speed: ~2 flaps/s, deeper, bigger bird
for t in (88.8,96.6,100.2):
    place(fl_slow,t,to_peak(fl_slow,-21),0.5,1.2,'WING_FLAPS(0.5x)','peacock wing beats')
foot=load(S2+'FOOTSTEPS.mp3'); fu=make_loop(foot,0.5)
n=int((160.8-139.2)*SR); x=np.tile(fu,n//len(fu)+2)[:n]; place(x,139.2,to_peak(foot,-21),1.2,1.5,'FOOTSTEPS','Ganesha walks round his parents (shots 19-21)')
sc=load(S2+'MOUSE_SCAMPER.mp3'); place(sc,140.0,to_peak(sc,-19),0.05,0.2,'MOUSE_SCAMPER','Mooshak scampers beside Ganesha, shot 19')
place(sc,197.9,to_peak(sc,-21),0.05,0.2,'MOUSE_SCAMPER','Mooshak dances, shot 26')
hop=load(S2+'HOP_FEATHER.mp3'); place(hop,84.35,to_peak(hop,-20),0.02,0.1,'HOP_FEATHER','Kartikeya hops on the peacock (L22)')
gg=load(S2+'GIGGLE.mp3'); place(gg,117.15,to_peak(gg,-19),0.02,0.15,'GIGGLE','Ganesha giggles (shot 16)')
ms=load(S2+'MANGO_SHIMMER.mp3')
place(ms,66.2,to_peak(ms,-20),0.02,0.5,'MANGO_SHIMMER','golden mango (shot 10)')
place(ms,191.0,to_peak(ms,-20),0.02,0.5,'MANGO_SHIMMER','Baba gives the mango (L47)')
ch=load(S2+'CHEER.mp3'); place(ch,195.3,to_peak(ch,-17),0.03,0.7,'CHEER','Hooray for Ganesha (L48)')
cl=load(S2+'CLAPS.mp3'); place(cl,195.6,to_peak(cl,-27),0.4,1.5,'CLAPS','soft applause under the celebration, shot 26')
place(cl,241.2,to_peak(cl,-27),0.8,1.8,'CLAPS','soft applause under the song, shot 31')
fs=load(S2+'FRUIT_SPLIT.mp3'); place(fs,204.5,to_peak(fs,-18),0.01,0.1,'FRUIT_SPLIT','mango is broken (shot 27)')
# ---------- squeaks: four different ones ----------
for f,t,nm in ((S2+'SQUEAK_A.mp3',4.29,'SQUEAK_A'),(S2+'SQUEAK_B.mp3',60.97,'SQUEAK_B'),(S2+'SQUEAK_C.mp3',115.69,'SQUEAK_C'),(S1+'S12_mouse_squeak.mp3',256.78,'S12')):
    x=load(f); place(x,t,to_peak(x,-14),0.005,0.08,nm,'Mooshak squeak under L02/L16/L30/L63')
# ---------- carried-over v1 effects (levels = target peak dBFS) ----------
def v1(name,t,target,off=0,fi=0.01,fo=0.1):
    x=load(S1+name+'.mp3'); place(x,t,to_peak(x,target)+off,fi,fo,name)
for t in (0.15,124.9): v1('S02_sparkle_chime',t,-15)
for t in (18.14,142.58,199.9): v1('S01_temple_bell',t,-13)
v1('S01_temple_bell',230.41,-13,-2)
pop=load(S1+'S03_count_pop.mp3')[:int(0.6*SR)]
def pitch(x,up,down): return resample_poly(x,up,down).astype(np.float32)
for base,times in ((57.47,(57.47,58.8,60.03)),(153.5,(153.5,154.78,156.06))):
    for k,(t,(u,d)) in enumerate(zip(times,((1,1),(8,9),(4,5)))):
        x=pitch(pop,u,d) if u!=d else pop
        place(x,t,to_peak(x,-15),0.005,0.12,'S03_count_pop','count %d (pitch step)'%(k+1))
for t in (41.6,84.8,161.8): v1('S05_peacock_call',t,-16)
v1('S06_whoosh',86.2,-21); v1('S08_soft_landing',164.6,-17); v1('S09_petal_sparkle',195.2,-16); v1('S10_nibbling',216.36,-19)
# ---------- finish ----------
stem=np.clip(stem,-0.97,0.97)
wavfile.write(D+'sfx_track_v2.wav',SR,(stem*32767).astype(np.int16))
json.dump({'timebase':'no-intro seconds (shot 02 = 0)','ambience_lufs_src':L,'cues':sorted(cues,key=lambda c:c['t'])},open(D+'sfx_cues_v2.json','w'),indent=1)
print('cues',len(cues),'peak dBFS',round(pk_db(stem),1),'ambience src LUFS',{k:round(v,1) for k,v in L.items()})
