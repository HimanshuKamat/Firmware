#!/usr/bin/env python3
"""Final assembly: intro + picture timeline + HyperFrames overlays + final audio -> 09_final/Ganesha_Big_Race_1080p.mp4
H.264 High, 1920x1080, 24 fps, ~12 Mbps, AAC 320 kbps 48 kHz, BT.709. Overlay start times come from 07_graphics/timing.json (start_final).
usage: build_final.py [--preview N]   (--preview N renders only the first N seconds with a fast preset for checking)"""
import json, os, subprocess, sys
R='/home/user/Firmware/ganesha-video/'
T=json.load(open(R+'07_graphics/timing.json'))['overlays']
G=R+'07_graphics/renders/'
preview=None
if '--preview' in sys.argv: preview=float(sys.argv[sys.argv.index('--preview')+1])
# (render file, timing key(s) -> list of start_final times)
plan=[('title_card.mov',[T['title_card']['start_final']]),
      ('counter_modaks.mov',[T['counter_modaks']['start_final']]),
      ('flap_prompt.mov',[T['flap_prompt']['start_final']]),
      ('chant.mov',[T['chant_04']['start_final'],T['chant_19']['start_final'],T['chant_26']['start_final']]),
      ('counter_circles.mov',[T['counter_circles']['start_final']]),
      ('lesson_card.mov',[T['lesson_card']['start_final']]),
      ('lyrics.mov',[T['lyrics']['start_final']]),
      ('end_screen.mov',[T['end_screen']['start_final']])]
intro=G+'intro.mp4'
inputs=['-i',intro,'-i',R+'08_edit/work/base_picture_1080_v1.mp4']
parts=['[0:v]fps=24,format=yuv420p[intro]','[1:v]fps=24,format=yuv420p[base]',
       '[intro][base]xfade=transition=fade:duration=0.5:offset=6.0[v0]']
idx=2; cur='v0'; used=[]
for fn,starts in plan:
    path=G+fn
    if not os.path.exists(path): print('MISSING overlay',fn,'-> skipped'); continue
    dur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',path]).decode().strip())
    for s in starts:
        inputs+=['-i',path]
        parts.append(f'[{idx}:v]format=yuva420p,setpts=PTS-STARTPTS+{s:.3f}/TB[o{idx}]')
        parts.append(f'[{cur}][o{idx}]overlay=format=auto:eof_action=pass:enable=\'between(t,{s:.3f},{s+dur:.3f})\'[v{idx}]')
        cur=f'v{idx}'; idx+=1; used.append((fn,s,dur))
inputs+=['-i',R+'09_final/audio_final_48k.wav']; aidx=idx
parts.append(f'[{cur}]format=yuv420p[vout]')
open(R+'08_edit/final_filter.txt','w').write(';\n'.join(parts))
out=R+('08_edit/work/final_preview.mp4' if preview else '09_final/Ganesha_Big_Race_1080p.mp4')
cmd=['ffmpeg','-y','-hide_banner','-loglevel','error','-nostats']+inputs+['-filter_complex_script',R+'08_edit/final_filter.txt','-map','[vout]','-map',f'{aidx}:a']
if preview: cmd+=['-t',str(preview),'-c:v','libx264','-preset','veryfast','-crf','20']
else: cmd+=['-c:v','libx264','-profile:v','high','-level','4.2','-preset','slow','-b:v','12M','-maxrate','16M','-bufsize','24M','-g','48','-bf','3']
cmd+=['-pix_fmt','yuv420p','-r','24','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-c:a','aac','-b:a','320k','-ar','48000','-ac','2','-movflags','+faststart','-shortest',out]
print('overlays used:',len(used)); [print(' ',u) for u in used]
subprocess.run(cmd,check=True); print('wrote',out)
