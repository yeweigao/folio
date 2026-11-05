#!/usr/bin/env python3
from pathlib import Path
from PIL import Image,ImageDraw
import json
ROOT=Path(__file__).resolve().parent
units=json.loads((ROOT/'manifest.json').read_text())
def image(group,name):return Image.open(ROOT/'renders'/f'{group}-{name}.png').convert('RGB')
def paste(canvas,im,box):
    x,y,w,h=box;canvas.paste(im.resize((w,h),Image.Resampling.LANCZOS),(x,y))
boards=[]
b=Image.new('RGB',(1440,1920),'#E8E8E8')
for i,u in enumerate(x for x in units if x['group']=='slides'):
    paste(b,image('slides',u['name']),(62+(i%2)*678,153+(i//2)*418,638,359))
boards.append(('01-slides',b))
b=Image.new('RGB',(1440,1920),'#000000')
for i,u in enumerate(x for x in units if x['group']=='posters'):
    paste(b,image('posters',u['name']),(32+(i%3)*465,43+(i//3)*619,446,596))
boards.append(('02-posters',b))
b=Image.new('RGB',(1440,1920),'#666666')
positions=[(130,84,1176,566),(137,708,184,672),(364,708,184,672),(590,708,184,672),(847,711,450,309),(847,1069,450,309),(134,1434,225,376),(394,1434,225,376),(662,1456,168,354),(867,1456,168,354),(1075,1446,219,364)]
for u,box in zip((x for x in units if x['group']=='brand'),positions):paste(b,image('brand',u['name']),box)
boards.append(('03-brand',b))
out=ROOT/'previews';out.mkdir(exist_ok=True)
for i,(name,b) in enumerate(boards):
    b.save(out/(name+'.png'))
    source=Image.open(f'/Users/vicoye/Downloads/IMG_{8102+i}.JPG').convert('RGB').resize((720,960),Image.Resampling.LANCZOS)
    compare=Image.new('RGB',(1440,1000),'#252525');compare.paste(source,(0,40));compare.paste(b.resize((720,960),Image.Resampling.LANCZOS),(720,40))
    ImageDraw.Draw(compare).text((20,12),'REFERENCE',fill='white');ImageDraw.Draw(compare).text((740,12),'VECTOR RECONSTRUCTION',fill='white')
    compare.save(out/(name+'-comparison.png'))
print('Saved three boards and three comparisons.')
