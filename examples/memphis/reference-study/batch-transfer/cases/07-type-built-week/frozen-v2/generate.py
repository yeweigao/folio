#!/usr/bin/env python3
"""Native, editable letter-wall poster; artwork and layout authored here."""
from pathlib import Path
from html import escape
from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'output-v2'
FONT = TTFont(ROOT / 'input-v2/fonts/Inter-900.ttf')
CMAP = FONT.getBestCmap()
UPM = FONT['head'].unitsPerEm
CAP = FONT['OS/2'].sCapHeight
GS = FONT.getGlyphSet()
C = dict(paper='#F6F0E5', ink='#1C1A1B', blue='#258CB4', purple='#554699',
         green='#005B32', orange='#FF5205', yellow='#FDC442', pink='#F5AAA4', glyph='#F54D05')

def advance(text):
    return sum(FONT['hmtx'][CMAP[ord(c)]][0] for c in text)

def bounds(text):
    pos=0; bb=[]
    for ch in text:
        pen=BoundsPen(GS); GS[CMAP[ord(ch)]].draw(pen)
        if pen.bounds:
            x0,y0,x1,y1=pen.bounds;bb.append((x0+pos,y0,x1+pos,y1))
        pos+=FONT['hmtx'][CMAP[ord(ch)]][0]
    return min(b[0] for b in bb),min(b[1] for b in bb),max(b[2] for b in bb),max(b[3] for b in bb)

parts=[]
def emit(v): parts.append(v)
def rect(x,y,w,h,fill,**attrs):
    a=' '.join(f'{k.replace("_","-")}="{escape(str(v))}"' for k,v in attrs.items())
    emit(f'<rect x="{x:.3f}" y="{y:.3f}" width="{w:.3f}" height="{h:.3f}" fill="{fill}" {a}/>')
def text(txt,x,y,size,weight=400,fill=None,**attrs):
    a=' '.join(f'{k.replace("_","-")}="{escape(str(v))}"' for k,v in attrs.items())
    emit(f'<text x="{x:.3f}" y="{y:.3f}" font-size="{size:.3f}" font-weight="{weight}" fill="{fill or C["ink"]}" {a}>{escape(txt)}</text>')

def wall(word, top, cap_height, id_, mask=None):
    lo,bot,hi,high=bounds(word)
    k=cap_height/CAP
    sx=844/((hi-lo)*k)
    tx=28-lo*k*sx
    baseline=top+cap_height
    kw=f' mask="url(#{mask})"' if mask else ''
    emit(f'<g id="{id_}" transform="translate({tx:.5f} {baseline:.5f}) scale({sx:.6f} 1)">')
    emit(f'<text x="0" y="0" font-size="{k*UPM:.5f}" font-weight="900" fill="{C["ink"]}"{kw}>{word}</text>')
    emit('</g>')
    return lambda x,y:(tx+x*k*sx,baseline-y*k),k,sx

emit('<?xml version="1.0" encoding="UTF-8"?>')
emit('<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1200" viewBox="0 0 900 1200" role="img" aria-labelledby="poster-title poster-desc">')
emit('<title id="poster-title">TAIPEI DESIGN WEEK 2027</title>')
emit('<desc id="poster-desc">October 4–10. Architecture, craft, food, music and public space. City Design Museum with Open City Lab. taipeidesignweek.example.</desc>')
emit('<!-- FONTS -->')
emit('<style>text{font-family:"Study Sans",sans-serif;font-kerning:none;font-variant-ligatures:none} </style>')
rect(0,0,900,1200,C['paper'])

# Four compact, full-width rows. Horizontal fitting is restricted to display type.
wall('TAIPEI',28,190,'city')
dpos,dk,dsx=wall('DESIGN',231,190,'theme')
# A two-tone square occupies the D counter, attached to its left interior edge.
# Its size follows the available counter, not a page ornament grid.
x0,y0=dpos(500,976)
side=54
emit('<g id="d-counter-square">')
rect(x0,y0,side,side,C['blue'])
emit(f'<path d="M{x0:.3f} {y0:.3f}h{side}v{side}z" fill="{C["purple"]}"/>')
emit('</g>')

wpos,wk,wsx=wall('WEEK',434,190,'event-type')
# Replace the first E's middle arm with three parallel colored strokes;
# the black spine, top and lower arms preserve the complete letter.
e_origin=advance('W')
x1,y1=wpos(e_origin+500,912)
x2,y2=wpos(e_origin+1114,594)
rect(x1,y1,x2-x1,y2-y1,C['paper'])
barh=(y2-y1)/3
for i,col in enumerate((C['orange'],C['yellow'],C['pink'])):
    rect(x1,y1+i*barh,x2-x1,barh,col)

# The zero is a true circular glyph substitution. Its underlying full text
# remains editable; the local mask removes only the zero's ink shape.
ycap=240; ytop=639; yk=ycap/CAP
zero_start=advance('2')
emit('<defs><mask id="zero-substitution" maskUnits="userSpaceOnUse" x="-100" y="-1800" width="6200" height="2200">')
emit('<rect x="-100" y="-1800" width="6200" height="2200" fill="white"/>')
emit(f'<rect x="{zero_start*yk:.5f}" y="{-1530*yk:.5f}" width="{1456*yk:.5f}" height="{1570*yk:.5f}" fill="black"/>')
emit('</mask></defs>')
ypos,_,ysx=wall('2027',ytop,ycap,'year','zero-substitution')
cx,cy=ypos(zero_start+728,745)
emit(f'<circle cx="{cx:.4f}" cy="{ytop+ycap/2:.4f}" r="120" fill="{C["glyph"]}"/>')

# The small programme list uses a shared baseline and unscaled live type.
emit('<g id="programme" aria-label="Programme categories">')
text('ARCHITECTURE',29,935,22)
text('CRAFT',29,966,22)
text('FOOD',337,935,22)
text('MUSIC',337,966,22)
text('PUBLIC SPACE',595,935,22)
emit('</g>')

# One quiet rule and an independent fact band complete the poster.
rect(28,1000,844,1.5,C['ink'])
emit('<g id="event-facts">')
text('OCTOBER 4–10',28,1053,31.5,700)
text('TAIPEIDESIGNWEEK.EXAMPLE',28,1093,23.5,700)
text('City Design Museum',28,1170,24.5,400)
text('Open City Lab',595,1170,24.5,400)
emit('</g>')
emit('</svg>')
OUT.mkdir(exist_ok=True)
(OUT/'raw.svg').write_text('\n'.join(parts)+'\n')
