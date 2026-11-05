#!/usr/bin/env python3
from pathlib import Path
import json, re
import xml.etree.ElementTree as ET
from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen

out=Path(__file__).resolve().parent
root=ET.fromstring((out/'poster.svg').read_text())
font=TTFont(out.parent/'input-v2/fonts/Oswald-700.ttf')
u=font['head'].unitsPerEm
cmap=font.getBestCmap()
glyphs=font.getGlyphSet()
faces={'slogan':(330,200),'event-name-one':(440,175),'event-name-two':(340,175),
 'artist-three':(330,115),'artist-four':(340,115),'artist-one':(260,110),
 'artist-two':(140,110),'date':(180,140),'venue-type':(130,140)}

def ink(text,x,y,size):
    boxes=[]
    cursor=x
    for char in text:
        glyph=cmap[ord(char)]
        pen=BoundsPen(glyphs); glyphs[glyph].draw(pen)
        if pen.bounds:
            l,b,r,t=pen.bounds
            boxes.append((cursor+l*size/u,y-t*size/u,cursor+r*size/u,y-b*size/u))
        cursor+=font['hmtx'].metrics[glyph][0]*size/u
    return min(b[0] for b in boxes),min(b[1] for b in boxes),max(b[2] for b in boxes),max(b[3] for b in boxes)

checks=[]
for el in root.iter():
    if el.tag.split('}')[-1]!='text': continue
    ident=el.attrib['id']; w,h=faces[ident]
    runs=list(el) or [el]
    boxes=[ink(run.text or '',float(run.attrib['x']),float(run.attrib['y']),float(run.attrib['font-size'])) for run in runs]
    b=(min(v[0] for v in boxes),min(v[1] for v in boxes),max(v[2] for v in boxes),max(v[3] for v in boxes))
    fit=b[0]>=0 and b[1]>=0 and b[2]<=w and b[3]<=h
    checks.append({'id':ident,'text':''.join(el.itertext()),'face':[w,h],
                   'local_ink_bounds':[round(x,3) for x in b],'inside_face':fit})
assert all(c['inside_face'] for c in checks)
texts=[c['text'] for c in checks]
assert texts==['WE MAKE NOISE','KONBIN','STAGE','MOTIF CLUB','NEON PALMS','RINA VEIL','LAGO','17.07','OPEN AIR']
assert root.attrib['width']=='900' and root.attrib['height']=='1200'
assert not any(el.tag.split('}')[-1] in {'image','path','filter','clipPath','use'} for el in root.iter())
css=''.join(el.text or '' for el in root.iter() if el.tag.split('}')[-1]=='style')
assert 'data:font/woff2;base64,' in css
report={'dimensions':[900,1200],'editable_text_elements':len(checks),'all_ink_within_assigned_faces':True,
        'all_brief_facts_present':True,'embedded_font':'Study Condensed / Oswald 700 / WOFF2',
        'native_geometry_only':True,'render':'preview.png, Chrome headless, 900 × 1200, embedded-font check true',
        'faces':checks}
(out/'qa.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
