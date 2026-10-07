#!/usr/bin/env python3
"""Final audio mix on the FINAL timeline (6 s intro + 274 s story = 280 s).
narration + SFX v2 + music (A story bed, B evening bed + reprise, sung song) + intro sting, then two-pass loudnorm to -14 LUFS / -1 dBTP.
Outputs: 06_audio/final_mix_prenorm.wav and 09_final/audio_final_48k.wav (stereo, 48 kHz, 24-bit)."""
import subprocess, json, re, sys
ROOT='/home/user/Firmware/ganesha-video/'; A=ROOT+'06_audio/'; M=A+'music/'
SH=6.0; TOTAL=280.0
ms=lambda t:int(round((t+SH)*1000))
flt=f"""
[0:a]aresample=48000,adelay={ms(0)}|{ms(0)},pan=stereo|c0=c0|c1=c0[nar];
[0:a]aresample=48000,adelay={ms(0)}|{ms(0)},pan=stereo|c0=c0|c1=c0[key];
[1:a]aresample=48000,adelay={ms(0)}|{ms(0)},pan=stereo|c0=c0|c1=c0[sfx];
[2:a]aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=1.5,volume=-13dB,adelay={ms(0)}|{ms(0)}[mA];
[3:a]aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=1.2,afade=t=out:st=14:d=4,volume=-16dB,adelay={ms(219)}|{ms(219)}[mB1];
[5:a]aresample=48000,aformat=channel_layouts=stereo,atrim=7:20,asetpts=PTS-STARTPTS,afade=t=in:d=3,afade=t=out:st=9:d=3,volume=-10dB,adelay={ms(262)}|{ms(262)}[mB2];
[mA][mB1][mB2]amix=inputs=3:normalize=0:duration=longest[bed];
[bed][key]sidechaincompress=threshold=0.03:ratio=3:attack=20:release=600:makeup=1[bedd];
[4:a]aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.3,volume=-6dB,volume=eval=frame:volume='if(lt(t,16.2),1,if(lt(t,18.2),1-0.25*(t-16.2),0.5))',adelay={ms(235.42)}|{ms(235.42)}[song];
[6:a]aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.05,afade=t=out:st=5.0:d=1.4,volume=-1dB,adelay=550|550[sting];
[nar][sfx][bedd][song][sting]amix=inputs=5:normalize=0:duration=longest,atrim=0:{TOTAL},alimiter=limit=0.89:level=disabled[out]
""".strip()
open(ROOT+'08_edit/audio_final_filter.txt','w').write(flt)
ins=[A+'narration_review_v2_noIntro.mp3',A+'sfx_track_v2.wav',M+'A_story_bed.mp3',M+'B_evening_bed.mp3',M+'C_song_edit.wav',M+'B_evening_bed.mp3',A+'sfx_v2/INTRO_STING.mp3']
cmd=['ffmpeg','-y','-hide_banner','-loglevel','error']
for i in ins: cmd+=['-i',i]
cmd+=['-filter_complex_script',ROOT+'08_edit/audio_final_filter.txt','-map','[out]','-ar','48000','-ac','2','-c:a','pcm_s24le',A+'final_mix_prenorm.wav']
subprocess.run(cmd,check=True)
# two-pass loudnorm
p1=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',A+'final_mix_prenorm.wav','-af','loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json','-f','null','-'],capture_output=True,text=True).stderr
j=json.loads(re.search(r'\{[^{}]*"input_i"[^{}]*\}',p1,re.S).group(0)); print('pass1',j)
ln=(f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_LRA={j['input_lra']}:measured_TP={j['input_tp']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true:print_format=summary,aresample=48000")
subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-i',A+'final_mix_prenorm.wav','-af',ln,'-ar','48000','-c:a','pcm_s24le',ROOT+'09_final/audio_final_48k.wav'],check=True)
r=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',ROOT+'09_final/audio_final_48k.wav','-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True).stderr
print([l.strip() for l in r.splitlines() if re.search(r'^\s+(I:|LRA:|Peak:)',l)])
