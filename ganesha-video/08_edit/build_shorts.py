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
lens=[e-s for s,e in SEGS]; offs=[]; acc=0.0
for i,l in enumerate(lens): offs.append(acc-i*XF if i else 0.0); acc+=l
offs=[sum(lens[:i])-i*XF for i in range(len(lens))]
story_len=sum(lens)-(len(lens)-1)*XF
inputs=['-i',FINAL,'-loop','1','-framerate','24','-t',f'{story_len+5:.2f}','-i',FRAME]
if use_end: inputs+=['-i',END]
p=[]
for i,(s,e) in enumerate(SEGS):
    p.append(f'[0:v]trim=start={s}:end={e},setpts=PTS-STARTPTS,fps=24,format=yuv420p[sv{i}]')
    p.append(f'[0:a]atrim=start={s}:end={e},asetpts=PTS-STARTPTS,afade=t=in:d=0.1,afade=t=out:st={e-s-0.2:.2f}:d=0.2[sa{i}]')
cur='sv0'; L=lens[0]
for i in range(1,len(SEGS)):
    p.append(f'[{cur}][sv{i}]xfade=transition=fade:duration={XF}:offset={L-XF:.3f}[xv{i}]'); cur=f'xv{i}'; L=L+lens[i]-XF
acur='sa0'
for i in range(1,len(SEGS)):
    p.append(f'[{acur}][sa{i}]acrossfade=d={XF}:c1=tri:c2=tri[xa{i}]'); acur=f'xa{i}'
p.append(f'[{cur}]split=2[b1][b2]')
p.append('[b1]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=34,eq=saturation=1.3:brightness=-0.05[bg]')
p.append('[b2]scale=1080:608,format=yuv420p[fg]')
p.append('[bg][fg]overlay=0:656[c1]')
p.append('[c1][1:v]overlay=0:0:format=auto[c2]')
cur='c2'; n=0
for (ca,cb,txt) in cues:
    for i,(s,e) in enumerate(SEGS):
        a=max(ca,s); b=min(cb+0.15,e)
        if b-a<0.5: continue
        ta=offs[i]+(a-s); tb=offs[i]+(b-s)
        lines=textwrap.wrap(txt.replace('♪','').strip(),width=24,break_long_words=False)[:3]
        if '♪' in txt: lines=['♪ '+lines[0]]+lines[1:]
        fn=f'{WORK}cap{n}.txt'; open(fn,'w',encoding='utf-8').write('\n'.join(lines))
        p.append(f"[{cur}]drawtext=fontfile={FONT}:textfile={fn}:reload=0:fontsize=72:fontcolor=0xFFF3DC:borderw=10:bordercolor=0x7A1F16:line_spacing=8:x=(w-text_w)/2:y=1330:enable='between(t,{ta:.3f},{tb:.3f})'[cap{n}]")
        cur=f'cap{n}'; n+=1
if use_end:
    p.append(f'[2:v]fps=24,scale=1080:1920,format=yuv420p[ec]')
    p.append(f'[{cur}]format=yuv420p[sv]')
    p.append(f'[sv][ec]xfade=transition=fade:duration=0.3:offset={L-0.3:.3f}[vout]')
    p.append(f'[0:a]atrim=start={END_AUDIO[0]}:end={END_AUDIO[1]},asetpts=PTS-STARTPTS,afade=t=in:d=0.1,afade=t=out:st=3.4:d=0.6[ea]')
    p.append(f'[{acur}][ea]acrossfade=d=0.3:c1=tri:c2=tri[aout]')
else:
    p.append(f'[{cur}]format=yuv420p[vout]'); p.append(f'[{acur}]anull[aout]')
open(R+'08_edit/shorts_filter.txt','w').write(';\n'.join(p))
cmd=['ffmpeg','-y','-hide_banner','-loglevel','error','-nostats']+inputs+['-filter_complex_script',R+'08_edit/shorts_filter.txt','-map','[vout]','-map','[aout]',
     '-c:v','libx264','-profile:v','high','-preset','slow','-b:v','10M','-maxrate','14M','-bufsize','20M','-pix_fmt','yuv420p','-r','24','-g','48',
     '-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709','-c:a','aac','-b:a','320k','-ar','48000','-ac','2','-movflags','+faststart','-shortest',OUT]
print('story length %.2f s, captions drawn: %d, end card: %s'%(story_len,n,use_end)); sys.stdout.flush()
subprocess.run(cmd,check=True); print('wrote',OUT)
