#!/usr/bin/env python3
"""Original, editable SVG composition built from the supplied written brief."""
from pathlib import Path
from html import escape
from math import sqrt
from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen
import subprocess

HERE = Path(__file__).resolve().parent
INPUT = HERE.parent / 'input-v2'
P = {'paper':'#EAE8E6','ink':'#19191D','blue':'#008BCD','green':'#087C4A',
     'pink':'#F68CBC','yellow':'#FFDE00','red':'#F52B20','purple':'#76258D'}
W,H,U = 900,1200,150
pieces=[]
def emit(s): pieces.append(s)
def rect(x,y,w,h,c): emit(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{P.get(c,c)}"/>')
def group(label): emit(f'<g aria-label="{escape(label)}">')
def end(): emit('</g>')
def concave_star(x,y,size,c):
 r=size/2
 emit(f'<path d="M {x+r},{y} A {r},{r} 0 0 1 {x},{y+r} A {r},{r} 0 0 1 {x+r},{y+size} A {r},{r} 0 0 1 {x+size},{y+r} A {r},{r} 0 0 1 {x+r},{y} Z" fill="{P[c]}"/>')
def diamond(cx,cy,span,c):
 r=span/2
 emit(f'<path d="M {cx},{cy-r} L {cx+r},{cy} L {cx},{cy+r} L {cx-r},{cy} Z" fill="{P[c]}"/>')
def chevron(x,y,c,left=False):
 # The two diagonals meet at a right angle. Arms retain the full 0.22u thickness.
 h=.70*U; run=h/2; tail=.22*U*sqrt(2); w=run+tail
 d=f'M 0,0 L {tail},0 L {w},{run} L {tail},{h} L 0,{h} L {run},{run} Z'
 tr=f'translate({x+w},{y}) scale(-1,1)' if left else f'translate({x},{y})'
 emit(f'<path d="{d}" transform="{tr}" fill="{P[c]}"/>')
def window_grid(x,y,w,h):
 group('Coarse four-window grid per base module')
 rect(x,y,w,h,'paper')
 emit(f'<g clip-path="url(#grid-{x}-{y})" stroke="{P["ink"]}" stroke-width="{.045*U}">')
 for i in range(round(w/(.25*U))+1):
  xx=x+i*.25*U
  emit(f'<path d="M {xx},{y} V {y+h}"/>')
 for j in range(round(h/(.25*U))+1):
  yy=y+j*.25*U
  emit(f'<path d="M {x},{yy} H {x+w}"/>')
 emit('</g>');end()
fonts={}
def bounds(text,family,weight):
 fn = 'NotoSansSC-variable.ttf' if family=='Study CJK' else f'Inter-{weight}.ttf'
 if fn not in fonts: fonts[fn]=TTFont(INPUT/'fonts'/fn)
 font=fonts[fn]
 glyphs=font.getGlyphSet(location={'wght':weight}) if 'fvar' in font else font.getGlyphSet()
 cmap=font.getBestCmap(); advance=0; box=None
 for char in text:
  g=glyphs[cmap[ord(char)]]; pen=BoundsPen(glyphs);g.draw(pen)
  if pen.bounds:
   a,b,c,d=pen.bounds; q=(a+advance,b,c+advance,d)
   box=q if box is None else (min(box[0],q[0]),min(box[1],q[1]),max(box[2],q[2]),max(box[3],q[3]))
  advance+=g.width
 return [v/font['head'].unitsPerEm for v in box]
def text_at(text,left,top,size,weight=400,family='Study CJK',label=None):
 a,b,c,d=bounds(text,family,weight)
 x=left-a*size; y=top+d*size
 emit(f'<text x="{x:.4f}" y="{y:.4f}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{P["ink"]}"'+(f' aria-label="{escape(label)}"' if label else '')+f'>{escape(text)}</text>')
 return (left,top,left+(c-a)*size,top+(d-b)*size)

def main():
 emit('<?xml version="1.0" encoding="UTF-8"?>')
 emit('<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1200" viewBox="0 0 900 1200" role="img" aria-labelledby="poster-title poster-desc">')
 emit('<title id="poster-title">集合散步 — CITY WALKS</title>')
 emit('<desc id="poster-desc">在城里发现。Small discoveries, shared streets. 2027.05.14–05.16，河岸街区。一起走进街角的日常。</desc>')
 emit('<!-- FONTS -->')
 emit('<defs>')
 for x,y,w,h in [(300,0,300,150),(0,900,300,300)]:
  emit(f'<clipPath id="grid-{x}-{y}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath>')
 emit('<clipPath id="diagonal-district"><rect x="300" y="600" width="600" height="300"/></clipPath>')
 emit('</defs>')
 # Neighbouring fields touch. Reading fields are integral districts of the grid.
 group('Unequal modular street districts')
 rect(0,0,300,150,'blue')
 rect(600,0,300,300,'purple')
 rect(600,300,300,225,'green')
 rect(600,525,300,75,'paper')
 rect(0,150,600,450,'paper')
 rect(0,600,300,300,'red')
 rect(300,600,600,300,'blue')
 rect(300,900,600,150,'yellow')
 rect(300,1050,600,150,'green')
 end()
 group('Rightward movement across the first street')
 chevron(33,22.5,'ink');chevron(173,22.5,'ink');end()
 window_grid(300,0,300,150)
 group('Solid shapes crossing the upper right district seam')
 concave_star(675,0,150,'yellow')
 emit(f'<circle cx="750" cy="300" r="150" fill="{P["pink"]}"/>')
 end()
 group('Half-module band of broad vertical stripes')
 for x in range(600,900,30): rect(x,525,15,75,'ink')
 end()
 group('A diagonal pair of full-size diamonds')
 diamond(75,675,142.5,'paper');diamond(225,825,142.5,'ink');end()
 group('Wide diagonal bars at the same module scale')
 # Explicit polygons maintain a precise 18 px perpendicular width at 45 degrees.
 emit('<g clip-path="url(#diagonal-district)">')
 step=.24*U*sqrt(2); band=.12*U*sqrt(2)
 for start in [(-900+i*step) for i in range(45)]:
  # x-y is constant along each downward-right diagonal.
  emit(f'<path d="M {start+600:.4f},600 L {start+600+band:.4f},600 L {start+900+band:.4f},900 L {start+900:.4f},900 Z" fill="{P["yellow"]}"/>')
 emit('</g>');end()
 window_grid(0,900,300,300)
 group('Returning leftward movement at the foot of the poster')
 for x in [340,520,700]: chevron(x,1072.5,'paper',True)
 end()
 group('Primary reading district')
 text_at('集合散步',30,185,99,900)
 text_at('在城里发现',30,296,93.6,300)
 text_at('CITY WALKS',30,414,37.8,900,'Study Sans')
 # Both English lines use one normal-width face, with actual ink gaps checked.
 text_at('Small discoveries,',30,471.6,37.8,400,'Study Sans')
 text_at('shared streets.',30,517.5,37.8,400,'Study Sans')
 end()
 group('Participation facts')
 text_at('2027.05.14–05.16',330,928,23.4,700,'Study Sans')
 text_at('河岸街区',330,964,23.4,700)
 text_at('一起走进街角的日常',330,1000,23.4,400)
 end()
 emit('</svg>')
 (HERE/'raw.svg').write_text('\n'.join(pieces)+'\n')
 subprocess.run(['/private/tmp/folio-memphis-tools/bin/python',str(INPUT/'embed_fonts.py'),str(INPUT/'fonts'),str(HERE/'raw.svg'),str(HERE/'poster.svg')],check=True)

if __name__=='__main__':main()
