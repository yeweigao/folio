#!/usr/bin/env python3
"""Shuffle old/new output labels for independent visual review."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,random,shutil,importlib.util
R=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('proofs',R/'make-proofs.py');proof=importlib.util.module_from_spec(spec);spec.loader.exec_module(proof)
keypath=R/'archived/blind-key.json';keys=json.loads(keypath.read_text()) if keypath.exists() else {}
meta=json.loads((R/'cases.json').read_text());dest=R/'evaluation/blind';dest.mkdir(exist_ok=True)
font=ImageFont.truetype('/Users/vicoye/Library/Fonts/NotoSansCJKsc-Medium.otf',27)
for case in meta:
 id=case['id'];root=R/'cases'/id
 if not all((root/f'frozen-{stage}/poster.png').exists() for stage in ['v1','v2']):continue
 if id not in keys:
  stages=['v1','v2'];random.Random('folio-20261105-'+id).shuffle(stages);keys[id]=dict(zip(['P','Q'],stages))
 out=dest/id;out.mkdir(exist_ok=True)
 shutil.copyfile(root/'input-v2/brief.md',out/'brief.md')
 ref=proof.reference(id);ref.save(out/'reference.png')
 items=[ref]
 for label in ['P','Q']:
  src=root/f'frozen-{keys[id][label]}/poster.png';shutil.copyfile(src,out/(label+'.png'));items.append(Image.open(src).convert('RGB'))
 canvas=Image.new('RGB',(2700,1240),'#555555');draw=ImageDraw.Draw(canvas)
 for i,(label,im) in enumerate(zip(['REFERENCE','P','Q'],items)):
  draw.text((900*i+20,3),label,font=font,fill='white');f=proof.fit(im,900,1200);canvas.paste(f,(900*i+(900-f.width)//2,40+(1200-f.height)//2))
 canvas.save(out/'comparison.png');canvas.convert('L').save(out/'gray.png')
keypath.write_text(json.dumps(keys,indent=2))
print('Prepared blinded comparisons:',len(keys))
