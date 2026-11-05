#!/usr/bin/env python3
"""Evidence views only; never changes generated artwork."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,sys
R=Path(__file__).resolve().parent;S=R.parent
FONT=ImageFont.truetype('/Users/vicoye/Library/Fonts/NotoSansCJKsc-Medium.otf',27)
META=json.loads((R/'cases.json').read_text());SYSTEMS={x['id']:x for x in json.loads((S/'systems.json').read_text())}
def fit(im,w,h):
 im=im.convert('RGB');im.thumbnail((w,h),Image.Resampling.LANCZOS);return im
def reference(id):
 if id.startswith('01'):return Image.open(S/'previews/01-slides.png').convert('RGB')
 if id.startswith('10'):return Image.open(S/'previews/03-brand.png').convert('RGB')
 pieces=SYSTEMS[id]['pieces'];ims=[Image.open(S/'renders'/(Path(p).parent.name+'-'+Path(p).stem+'.png')).convert('RGB') for p in pieces]
 if len(ims)==1:return ims[0]
 c=Image.new('RGB',(900,1200),'#444444')
 for i,im in enumerate(ims):c.paste(fit(im,450,1200),(i*450,300))
 return c
def make(stage):
 dest=R/'evaluation'/stage;dest.mkdir(parents=True,exist_ok=True);found=[]
 stages=json.loads((R/'evaluation/final-case-stages.json').read_text()) if stage=='final' else {}
 for case in META:
  folder=R/'cases'/case['id']/('frozen-'+stages.get(case['id'],stage))
  if not (folder/'poster.png').exists():continue
  im=Image.open(folder/'poster.png').convert('RGB');ref=reference(case['id'])
  c=Image.new('RGB',(1800,1240),'#555555');d=ImageDraw.Draw(c);d.text((22,4),'REFERENCE',fill='white',font=FONT);d.text((922,4),'TRANSFER',fill='white',font=FONT)
  a=fit(ref,900,1200);b=fit(im,900,1200);c.paste(a,((900-a.width)//2,40+(1200-a.height)//2));c.paste(b,(900+(900-b.width)//2,40+(1200-b.height)//2))
  c.save(dest/(case['id']+'.png'));c.convert('L').save(dest/(case['id']+'-gray.png'));found.append((case,im))
 canvas=Image.new('RGB',(1800,max(1,(len(found)+2)//3)*850),'#333333');d=ImageDraw.Draw(canvas)
 for i,(case,im) in enumerate(found):
  x=(i%3)*600;y=(i//3)*850;d.text((x+18,y+8),case['id'].split('-')[0]+' / '+case['title'],font=FONT,fill='white')
  p=fit(im,580,790);canvas.paste(p,(x+(600-p.width)//2,y+48+(790-p.height)//2))
 canvas.save(dest/'overview.png');print('Proofs',stage,len(found))
if __name__=='__main__':make(sys.argv[1] if len(sys.argv)>1 else 'v1')
