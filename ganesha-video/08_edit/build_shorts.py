#!/usr/bin/env python3
"""60-second 9:16 Shorts teaser (1080x1920) cut from the FINAL video: ten strongest moments on a blurred background with the
branded frame (07_graphics/shared/shorts_frame.png), big Fredoka captions from captions.srt, and a 4 s "full story on the channel" end card.
usage: build_shorts.py [--noendcard]"""
import re, os, subprocess, sys, textwrap
R='/home/user/Firmware/ganesha-video/'
FINAL=R+'09_final/Ganesha_Big_Race_1080p.mp4'
FRAME=R+'07_graphics/shared/shorts_frame.png'
END=R+'07_graphics/renders/shorts_endcard.mp4'
FONT=R+'07_graphics/shared/fonts/Fredoka-Bold.ttf'
OUT=R+'09_final/Ganesha_Big_Race_Shorts_9x16.mp4'
WORK=R+'08_edit/work/shorts/'; os.makedirs(WORK,exist_ok=True)
XF=0.25
# (start,end) on the FINAL timeline (seconds)
SEGS=[(6.0,11.8),(20.3,26.2),(62.9,68.5),(94.3,99.9),(146.2,149.9),(159.2,165.2),(183.3,187.9),(201.2,207.0),(234.3,239.8),(251.8,257.9)]
END_AUDIO=(260.3,264.3)   # "Bye-bye, little friend! Squeak-squeak!" over the hummed tail
use_end=os.path.exists(END) and '--noendcard' not in sys.argv
def tsec(s): h,m,r=s.split(':'); sec,ms=r.split(','); return int(h)*3600+int(m)*60+int(sec)+int(ms)/1000
cues=[]
for blk in open(R+'09_final/captions.srt',encoding='utf-8').read().strip().split('\n\n'):
    ln=blk.split('\n'); a,b=ln[1].split(' --> '); cues.append((tsec(a),tsec(b),' '.join(ln[2:])))
lens=[e-s for s,e in SEGS]
offs=[sum(lens[:i])-i*XF for i in range(len(lens))]
story_len=sum(lens)-(len(lens)-1)*XF
# ---- step 1: one 9:16 clip per segment (blurred background + branded frame + captions), small memory footprint
segfiles=[]; n=0
for i,(s,e) in enumerate(SEGS):
    dur=e-s; f=[]
    f.append('[0:v]fps=24,split=2[b1][b2]')
    f.append('[b1]scale=270:480:force_original_aspect_ratio=increase,crop=270:480,gblur=sigma=8,scale=1080:1920,eq=saturation=1.3:brightness=-0.05[bg]')
    f.append('[b2]scale=1080:608,format=yuv420p[fg]')
    f.append('[bg][fg]overlay=0:656[c1]')
    f.append('[c1][1:v]overlay=0:0:format=auto[c2]')
    cur='c2'
    for (ca,cb,txt) in cues:
        a=max(ca,s); b=min(cb,e)
        if b-a<0.5: continue
        lines=textwrap.wrap(txt.replace('\u266a','').strip(),width=24,break_long_words=False)[:3]
        fn=f'{WORK}cap{n}.txt'; open(fn,'w',encoding='utf-8').write('\n'.join(lines))
        f.append(f"[{cur}]drawtext=fontfile={FONT}:textfile={fn}:reload=0:fontsize=72:fontcolor=0xFFF3DC:borderw=10:bordercolor=0x7A1F16:line_spacing=8:x=(w-text_w)/2:y=1330:enable='between(t,{a-s:.3f},{b-s:.3f})'[cap{n}]")
        cur=f'cap{n}'; n+=1
    f.append(f'[{cur}]format=yuv420p[vo]')
    f.append(f'[0:a]asetpts=PTS-STARTPTS,afade=t=in:d=0.1,afade=t=out:st={dur-0.2:.2f}:d=0.2[ao]')
    fsc=f'{WORK}seg{i}.txt'; open(fsc,'w').write(';\n'.join(f))
    out=f'{WORK}seg{i}.mov'
    cmd=['ffmpeg','-y','-hide_banner','-loglevel','error','-nostats','-ss',f'{s}','-t',f'{dur}','-i',FINAL,'-loop','1','-framerate','24','-t',f'{dur}','-i',FRAME,
         '-filter_complex_script',fsc,'-map','[vo]','-map','[ao]','-c:v','libx264','-crf','12','-preset','fast','-pix_fmt','yuv420p','-r','24','-c:a','pcm_s16le','-ar','48000','-shortest',out]
    subprocess.run(cmd,check=True); segfiles.append(out); print('segment',i,'done',flush=True)
# ---- step 2: crossfade the segments and the end card
inputs=[]
for sf in segfiles: inputs+=['-i',sf]
if use_end: inputs+=['-i',END,'-ss',f'{END_AUDIO[0]}','-t',f'{END_AUDIO[1]-END_AUDIO[0]}','-i',FINAL]
p2=[]
N=len(segfiles); L=lens[0]
for i in range(N): p2.append(f'[{i}:v]fps=24,settb=1/24,setpts=PTS-STARTPTS,format=yuv420p[nv{i}]')
cur='nv0'; acur='0:a'
for i in range(1,N):
    p2.append(f'[{cur}][nv{i}]xfade=transition=fade:duration={XF}:offset={L-XF:.3f}[xv{i}]'); cur=f'xv{i}'; L=L+lens[i]-XF
    p2.append(f'[{acur}][{i}:a]acrossfade=d={XF}:c1=tri:c2=tri[xa{i}]'); acur=f'xa{i}'
if use_end:
    p2.append(f'[{N}:v]fps=24,settb=1/24,setpts=PTS-STARTPTS,scale=1080:1920,format=yuv420p[ec]')
    p2.append(f'[{cur}]settb=1/24,format=yuv420p[sv]')
    p2.append(f'[sv][ec]xfade=transition=fade:duration=0.3:offset={L-0.3:.3f}[vout]')
    p2.append(f'[{N+1}:a]asetpts=PTS-STARTPTS,afade=t=in:d=0.1,afade=t=out:st=3.4:d=0.6[ea]')
    p2.append(f'[{acur}][ea]acrossfade=d=0.3:c1=tri:c2=tri[aout]')
else:
    p2.append(f'[{cur}]format=yuv420p[vout]'); p2.append(f'[{acur}]anull[aout]')
open(R+'08_edit/shorts_filter.txt','w').write(';\n'.join(p2))
cmd=['ffmpeg','-y','-hide_banner','-loglevel','error','-nostats']+inputs+['-filter_complex_script',R+'08_edit/shorts_filter.txt','-map','[vout]','-map','[aout]',
     '-c:v','libx264','-profile:v','high','-preset','slow','-b:v','10M','-maxrate','14M','-bufsize','20M','-pix_fmt','yuv420p','-r','24','-g','48',
     '-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-c:a','aac','-b:a','320k','-ar','48000','-ac','2','-movflags','+faststart',OUT]
print('story length %.2f s, captions drawn: %d, end card: %s'%(story_len,n,use_end),flush=True)
subprocess.run(cmd,check=True); print('wrote',OUT)

# ---- step 3: normalise the Shorts audio to -14 LUFS (two-pass) and remux
import json, tempfile
tmp=tempfile.mkdtemp(); wa=tmp+'/a.wav'; wn=tmp+'/an.wav'
subprocess.run(['ffmpeg','-y','-v','error','-i',OUT,'-vn','-c:a','pcm_s24le','-ar','48000',wa],check=True)
t=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',wa,'-af','loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json','-f','null','-'],capture_output=True,text=True).stderr
j=json.loads(re.search(r'\{[^{}]*"input_i"[^{}]*\}',t,re.S).group(0))
ln=f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_LRA={j['input_lra']}:measured_TP={j['input_tp']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true,aresample=48000"
subprocess.run(['ffmpeg','-y','-v','error','-i',wa,'-af',ln,'-c:a','pcm_s24le',wn],check=True)
subprocess.run(['ffmpeg','-y','-v','error','-i',OUT,'-i',wn,'-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','320k','-ar','48000','-movflags','+faststart',tmp+'/o.mp4'],check=True)
os.replace(tmp+'/o.mp4',OUT); print('normalised to -14 LUFS')
