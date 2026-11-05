#!/usr/bin/env python3
"""Native, editable isometric stage; geometry authored for this brief."""
from pathlib import Path
from html import escape
from fontTools.ttLib import TTFont
import subprocess

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent
C = dict(paper='#FFFFF3', ink='#000000', yellow='#FFDF06', blue='#2836B5', red='#FF2E05', green='#22B88A')
SVG=[]

def fmt(n):
    return f'{n:.5f}'.rstrip('0').rstrip('.')

def project(x,y,z):
    return (500+x-y, 820+.425*(x+y)-z)

def polygon(points,color,label):
    ps=' '.join(f'{fmt(x)},{fmt(y)}' for x,y in points)
    SVG.append(f'<polygon id="{label}" points="{ps}" fill="{C[color]}"/>')

def world_poly(points,color,label):
    polygon([project(*p) for p in points],color,label)

def box(x0,x1,y0,y1,z0,z1,roof,left,right,label):
    # The roof and both visible walls use precisely the same four top vertices.
    a=(x0,y0,z1); b=(x1,y0,z1); c=(x1,y1,z1); d=(x0,y1,z1)
    world_poly([d,c,(x1,y1,z0),(x0,y1,z0)],left,label+'-left')
    world_poly([c,b,(x1,y0,z0),(x1,y1,z0)],right,label+'-right')
    world_poly([a,b,c,d],roof,label+'-roof')

def face_text(text,x,y,z,u,v,size,color,label,direction='left'):
    # u, v are coordinates IN the wall. All placement precedes projection.
    px,py=project(x,y,z)
    slope=.425 if direction=='left' else -.425
    matrix=f'matrix(1 {slope} 0 1 {fmt(px)} {fmt(py)})'
    SVG.append(f'<text id="{label}" transform="{matrix}" x="{fmt(u)}" y="{fmt(v)}" font-family="Study Condensed" font-size="{fmt(size)}" font-weight="700" fill="{C[color]}" font-kerning="none">{escape(text)}</text>')

SVG.append('<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1200" viewBox="0 0 900 1200" role="img" aria-labelledby="poster-title poster-desc">')
SVG.append('<title id="poster-title">KONBIN STAGE — 17.07 — OPEN AIR</title>')
SVG.append('<desc id="poster-desc">WE MAKE NOISE. RINA VEIL, LAGO, MOTIF CLUB, NEON PALMS. An isometric stage of colored blocks, with the event name across a white bridge.</desc>')
SVG.append('<!-- FONTS -->')
SVG.append('<rect width="900" height="1200" fill="'+C['yellow']+'"/>')

# Three separated piers make the title beam read as a bridge, with open air beneath.
box(-450,-340,-50,0,-300,-168,'ink','ink','blue','west-pier')
box(-50,0,-360,-250,-300,-168,'ink','red','ink','east-pier')
box(-90,0,-90,0,-300,-168,'ink','ink','blue','center-pier')

# Rear tier: broad black/blue stage body with a red roof.
box(-360,-70,-300,-90,180,370,'red','ink','blue','rear-stage')
face_text('WE MAKE',-360,-90,370,11,70,73,'yellow','slogan-one')
face_text('NOISE',-360,-90,370,11,163,110,'yellow','slogan-two')

# The smallest and farthest tower stands on the rear-stage roof.
box(-280,-110,-260,-100,370,508,'green','ink','blue','date-tower')
face_text('17.07',-280,-100,508,8,96,74.8,'yellow','date')
# A semantic line break keeps the complete OPEN AIR fact comfortably within its wall.
px,py=project(-110,-100,508)
SVG.append(f'<text id="venue-type" transform="matrix(1 -.425 0 1 {fmt(px)} {fmt(py)})" font-family="Study Condensed" font-size="52" font-weight="700" fill="{C["yellow"]}" font-kerning="none"><tspan x="10" y="56">OPEN </tspan><tspan x="10" y="116">AIR</tspan></text>')

# The artist tier is a single V-shaped structure. The roof consists of two
# rectangular world planes; both walls share the front vertical at (-50,-50).
world_poly([(-410,-140,150),(-140,-140,150),(-140,-50,150),(-410,-50,150)],'green','artist-roof-left')
world_poly([(-140,-50,150),(-140,-380,150),(-50,-380,150),(-50,-50,150)],'red','artist-roof-right')
world_poly([(-410,-50,150),(-50,-50,150),(-50,-50,0),(-410,-50,0)],'blue','artist-wall-left')
world_poly([(-50,-50,150),(-50,-380,150),(-50,-380,0),(-50,-50,0)],'green','artist-wall-right')
face_text('RINA VEIL',-410,-50,150,12,63,60,'yellow','artist-rina')
face_text('LAGO',-410,-50,150,12,127,60,'yellow','artist-lago')
face_text('MOTIF CLUB',-50,-50,150,10,63,60,'ink','artist-motif','right')
face_text('NEON PALMS',-50,-50,150,10,127,60,'ink','artist-neon','right')

# Narrow top deck of the front bridge, folded in plan around the artist tier.
# The joint is a real shared edge, not a screen-positioned decorative overlap.
world_poly([(-450,-50,0),(-50,-50,0),(-50,0,0),(-450,0,0)],'ink','bridge-deck-left')
world_poly([(-50,0,0),(-50,-360,0),(0,-360,0),(0,0,0)],'ink','bridge-deck-right')
world_poly([(-450,0,0),(0,0,0),(0,0,-168),(-450,0,-168)],'paper','title-wall-left')
world_poly([(0,0,0),(0,-360,0),(0,-360,-168),(0,0,-168)],'paper','title-wall-right')

# Equal cap height on the two faces. Natural glyph advances, with safe margins.
f=TTFont(ROOT/'input/fonts/Oswald-700.ttf')
cmap=f.getBestCmap(); metrics=f['hmtx'].metrics; upm=f['head'].unitsPerEm

def advance(t,size):
    return sum(metrics[cmap[ord(c)]][0] for c in t)*size/upm

size=133.25
face_text('KONBIN',-450,0,0,(450-advance('KONBIN',size))/2,132,size,'ink','event-konbin')
face_text('STAGE',0,0,0,(360-advance('STAGE',size))/2,132,size,'ink','event-stage','right')
SVG.append('</svg>')
(OUT/'raw.svg').write_text('\n'.join(SVG)+'\n')
subprocess.run(['/private/tmp/folio-memphis-tools/bin/python',str(ROOT/'input/embed_fonts.py'),str(ROOT/'input/fonts'),str(OUT/'raw.svg'),str(OUT/'poster.svg')],check=True)
