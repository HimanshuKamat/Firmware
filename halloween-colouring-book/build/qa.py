import numpy as np, csv
from PIL import Image
from scipy import ndimage
rows=[]
for p,m,f in csv.reader(open('media.tsv'),delimiter='\t'):
    if p=='cover': continue
    a=np.asarray(Image.open(f'previews/page-{p}.jpg').convert('RGB')).astype(int); g=a.mean(2)
    ink=g<128
    lab,n=ndimage.label(~ink); s=np.bincount(lab.ravel())[1:]
    tiny=int((s<6).sum())
    solid=ndimage.binary_opening(ink,iterations=2)  # ink blobs >~5px thick at 200px => >~5mm at 8in
    grey=((g>70)&(g<185)).mean()
    rows.append((p,m,round(ink.mean()*100,1),n,tiny,round(solid.mean()*100,2),round(grey*100,1),int((a.max(2)-a.min(2)).max())))
print("page media ink% regions tiny solid% grey% colour")
for r in rows: print(*r)
import json; json.dump(rows,open('qa_metrics.json','w'))
