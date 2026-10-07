#!/usr/bin/env python3
"""Make captions.srt from the narration timings (final timeline = no-intro time + 6 s intro)."""
import json, textwrap, sys
SHIFT=6.0
ROOT='/home/user/Firmware/ganesha-video'
lines={l['id']:l for l in json.load(open(f'{ROOT}/06_audio/lines.json'))}
dur={d[0]:d[3] for d in json.load(open(f'{ROOT}/06_audio/line_durations.json'))}
place=json.load(open(f'{ROOT}/06_audio/placement_v2_noIntro.json'))
cues=[]   # (start,end,text)
for lid,start,tempo,who in place:
    cues.append([start, start+dur[lid]/tempo, lines[lid]['text']])
# sung lines come from the song, timed from the Scribe transcript (see 07_graphics/timing.json)
T=json.load(open(f'{ROOT}/07_graphics/timing.json'))['overlays']['lyrics']['lines_abs_noIntro']
song=['Hold your family, hold them near,','They are your whole world, dear!','Ganpati Bappa… Morya!','Ganpati Bappa… Morya!']
for words,txt in zip(T,song):
    cues.append([words[0][1], words[-1][2]+0.2, '♪ '+txt+' ♪'])
cues.sort(key=lambda c:c[0])
# readability: hold each caption a little past the voice, but never into the next one
for i,c in enumerate(cues):
    nxt=cues[i+1][0] if i+1<len(cues) else 1e9
    c[1]=min(max(c[1]+0.3,c[0]+1.2),nxt-0.04)
def fmt(t):
    t=max(0,t+SHIFT); ms=int(round(t*1000)); h,ms=divmod(ms,3600000); m,ms=divmod(ms,60000); s,ms=divmod(ms,1000)
    return f'{h:02d}:{m:02d}:{s:02d},{ms:03d}'
def wrap(txt):
    if len(txt)<=42: return txt
    parts=textwrap.wrap(txt,width=max(21,len(txt)//2+4),break_long_words=False)
    return '\n'.join(parts[:2])
out=[]
for i,(a,b,txt) in enumerate(cues,1):
    out.append(f'{i}\n{fmt(a)} --> {fmt(b)}\n{wrap(txt)}\n')
open(f'{ROOT}/09_final/captions.srt','w',encoding='utf-8').write('\n'.join(out))
print(len(cues),'captions; last ends',fmt(cues[-1][1]))
