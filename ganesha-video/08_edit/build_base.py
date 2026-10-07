"""Build the 1080p, 24 fps, silent picture timeline for shots 02-33 (274 s, 0.5 s crossfades).
Per-shot slow-down / hold / trim values are read from rough_filter_v3.txt so the timing
matches the approved rough cut and the narration placements. Fixed or extended clips replace
the raw ones for shots 21 (baked numerals removed), 31 (redo without the extra girl) and 33 (held push-in)."""
import re, glob, subprocess, sys, os
ROOT='/home/user/Firmware/ganesha-video'
os.chdir(ROOT)
t=open('08_edit/rough_filter_v3.txt').read()
chains=re.findall(r'\[(\d+):v\](.*?)\[c(\d+)\];',t)
xf=re.findall(r'\]\[c(\d+)\]xfade=transition=fade:duration=0.5:offset=([\d.]+)',t)
offsets={int(c):float(o) for c,o in xf}
override={21:'08_edit/work/shot21_fixed.mp4',31:'05_clips/raw/shot31_redo_veo31fast.mp4',33:'08_edit/work/shot33_ext.mp4',
          2:'05_clips/tests/shot02_veo_1080.mp4',4:'05_clips/tests/shot04_seedance_1080.mp4'}
def clipfile(shot):
    if shot in override: return override[shot]
    c=[f for f in sorted(glob.glob(f'05_clips/raw/shot{shot:02d}_*.mp4')) if 'redo' not in f]
    assert len(c)==1,(shot,c); return c[0]
inputs=[]; parts=[]
for i,(idx,body,c) in enumerate(chains):
    shot=i+2
    slow=re.search(r'setpts=PTS\*([\d.]+)',body); tpad=re.search(r'stop_duration=([\d.]+)',body); trim=float(re.search(r'trim=duration=([\d.]+)',body).group(1))
    f=clipfile(shot); inputs+=['-i',f]
    chain=[f'fps=24','scale=1920:1080:force_original_aspect_ratio=increase','crop=1920:1080','setpts=PTS-STARTPTS']
    if shot in (21,):            # already 8 s, treat like the original (slow 1.0625 then trim)
        pass
    if shot==33:
        chain+=[f'trim=duration={trim:.3f}','setpts=PTS-STARTPTS']
    else:
        if slow: chain.append(f'setpts=PTS*{slow.group(1)}')
        if tpad: chain.append(f'tpad=stop_mode=clone:stop_duration={tpad.group(1)}')
        chain+=[f'trim=duration={trim:.3f}','setpts=PTS-STARTPTS']
    chain.append('format=yuv420p')
    parts.append(f'[{i}:v]'+','.join(chain)+f'[c{i}]')
prev='c0'
for i in range(1,len(chains)):
    out=f'x{i}'
    parts.append(f'[{prev}][c{i}]xfade=transition=fade:duration=0.5:offset={offsets[i]:.3f}[{out}]'); prev=out
open('08_edit/work/base_filter_1080.txt','w').write(';\n'.join(parts))
out='08_edit/work/base_picture_1080_v1.mp4'
cmd=['ffmpeg','-y','-hide_banner','-loglevel','error','-stats']+inputs+['-filter_complex_script','08_edit/work/base_filter_1080.txt','-map',f'[{prev}]','-an',
     '-c:v','libx264','-profile:v','high','-crf','12','-preset','medium','-pix_fmt','yuv420p','-r','24',out]
print(' '.join(cmd[:6]),'... inputs',len(chains)); sys.stdout.flush()
subprocess.run(cmd,check=True)
