#!/usr/bin/env python3
"""Composite a rendered overlay (MOV with alpha) on the real 1080p picture and write a contact sheet.
usage: preview.py OVERLAY.mov START_NOINTRO OUT.png T1 T2 ...     (T = seconds from the overlay's own start)
The picture is 08_edit/work/base_picture_1080_v1.mp4 (shot 02 starts at 0). Each tile is 960x540."""
import subprocess, sys, os
from PIL import Image, ImageDraw
BASE='/home/user/Firmware/ganesha-video/08_edit/work/base_picture_1080_v1.mp4'
ov, start, out = sys.argv[1], float(sys.argv[2]), sys.argv[3]
ts=[float(x) for x in sys.argv[4:]]
tmp=os.path.join(os.path.dirname(os.path.abspath(out)),'.prev_tmp'); os.makedirs(tmp,exist_ok=True)
tiles=[]
for i,t in enumerate(ts):
    f=os.path.join(tmp,f'p{i}.png')
    cmd=['ffmpeg','-y','-v','error','-ss',f'{start+t:.3f}','-i',BASE,'-ss',f'{t:.3f}','-i',ov,
         '-filter_complex','[0:v][1:v]overlay=format=auto,scale=960:540','-frames:v','1',f]
    subprocess.run(cmd,check=True)
    im=Image.open(f).convert('RGB'); d=ImageDraw.Draw(im); d.rectangle((0,0,150,26),fill=(0,0,0)); d.text((6,6),f't={t:.2f}s (+{start:.1f})',fill=(255,255,255))
    tiles.append(im)
cols=2 if len(tiles)>1 else 1; rows=(len(tiles)+cols-1)//cols
sheet=Image.new('RGB',(960*cols,540*rows))
for i,im in enumerate(tiles): sheet.paste(im,((i%cols)*960,(i//cols)*540))
sheet.save(out); print('wrote',out,sheet.size)
