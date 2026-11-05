#!/usr/bin/env python3
"""Draw this poster from native SVG primitives and live text."""
from pathlib import Path
from math import sin, cos, pi
from html import escape
import subprocess
import shutil

HERE = Path(__file__).resolve().parent
INPUT = HERE.parent / 'input-v2'
C = dict(paper='#FFFFFF', ink='#080808', blue='#276DB3', orange='#F04D1B',
         yellow='#F6C333', pink='#EDC6C0', lightblue='#CAE5F4', red='#FF3235',
         amber='#F6AD1A', tangerine='#FF9218', cream='#FFF5D6')
parts = []
def put(s): parts.append(s)
def rect(x,y,w,h,fill):
    put(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{C.get(fill,fill)}"/>')
def circle(x,y,r,fill,stroke=None,sw=None):
    a=f'<circle cx="{x:.3f}" cy="{y:.3f}" r="{r:.3f}" fill="{C.get(fill,fill)}"'
    if stroke: a+=f' stroke="{C.get(stroke,stroke)}" stroke-width="{sw}"'
    put(a+'/>')
def path(d,fill): put(f'<path d="{d}" fill="{C.get(fill,fill)}"/>')
def text(s,x,y,size,family='Study Sans',weight=400,fill='ink',spacing=None):
    attrs=f'x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{C[fill]}"'
    if spacing is not None: attrs+=f' letter-spacing="{spacing}"'
    put(f'<text {attrs}>{escape(s)}</text>')
def arcs(x,y,size,bg,fg,corner):
    ident=f'arc-{x}-{y}'
    rect(x,y,size,size,bg)
    put(f'<clipPath id="{ident}"><rect x="{x}" y="{y}" width="{size}" height="{size}"/></clipPath>')
    put(f'<g clip-path="url(#{ident})" fill="none" stroke="{C[fg]}" stroke-width="{size*.04}">')
    cx=x+(size if corner[0] else 0); cy=y+(size if corner[1] else 0)
    for k in [0.19,0.44,0.69,0.94,1.19]:
        put(f'<circle cx="{cx}" cy="{cy}" r="{size*k}"/>')
    put('</g>')
def dual(x,y,size,bg='pink'):
    rect(x,y,size,size,bg)
    cy=y+size/2
    for cx,r1,r2,c1,c2,sign in [(x,size*.5,size*.37,'orange','blue',1),(x+size,size*.5,size*.37,'blue','lightblue',-1)]:
        for r,fill in [(r1,c1),(r2,c2)]:
            # Straight diameter stays on the outside edge; circular sides face inward.
            sweep=1 if sign>0 else 0
            path(f'M {cx} {cy-r} A {r} {r} 0 0 {sweep} {cx} {cy+r} Z',fill)
def red_flower(cx,cy,r):
    put('<g aria-label="Six-petal red flower with yellow centre and six black dots">')
    for k in range(6):
        a=-pi/2+k*pi/3
        circle(cx+.48*r*cos(a),cy+.48*r*sin(a),.52*r,'red')
    circle(cx,cy,.30*r,'yellow')
    for k in range(6):
        a=-pi/2+k*pi/3
        circle(cx+.70*r*cos(a),cy+.70*r*sin(a),.10*r,'ink')
    put('</g>')
def yellow_flower(cx,cy,r):
    # Four diagonal circular lobes at each scale; all internal contours remain rounded.
    put('<g aria-label="Layered yellow four-petal flower">')
    for scale,fill in [(1,'yellow'),(.81,'amber'),(.62,'tangerine'),(.43,'orange')]:
        rr=r*scale
        for dx,dy in [(-1,-1),(1,-1),(-1,1),(1,1)]:
            circle(cx+dx*.36*rr,cy+dy*.36*rr,.58*rr,fill)
    circle(cx,cy,.115*r,'cream')
    put('</g>')

put('<?xml version="1.0" encoding="UTF-8"?>')
put('<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1528" viewBox="0 0 1080 1528" role="img" aria-labelledby="poster-title poster-description">')
put('<title id="poster-title">MOLLY — 艺术在场 日常发光</title>')
put('<desc id="poster-description">ART IN EVERYDAY LIFE. 2027.04.17—05.05，10:00–20:00，城市艺术中心 · 一层展厅，免费入场。把街角的颜色、声音与相遇，变成每个人都能参与的艺术现场。</desc>')
put('<!-- FONTS -->')
rect(0,0,1080,1528,'paper')

# Continuous white reading field; every text line remains a live SVG text element.
put('<g id="brand">')
text('MOLLY',78,114,42,weight=900,spacing=-1.2)
put('</g>')
put('<g id="chinese-title">')
text('艺术在场',76,311,119,'Study Pixel',spacing=-2.38)
text('日常发光',76,430,119,'Study Pixel',spacing=-2.38)
put('</g>')
put('<g id="english-title">')
text('ART IN',80,551,48,'Study Pixel',fill='blue')
text('EVERYDAY LIFE',80,608,48,'Study Pixel',fill='blue')
put('</g>')
put('<g id="event-facts">')
text('2027.04.17—05.05',80,785,34,weight=700,spacing=-.35)
text('10:00–20:00',80,830,28)
text('城市艺术中心 · 一层展厅',80,919,28,'Study CJK')
text('免费入场',80,964,28,'Study CJK',weight=700)
put('</g>')
put('<g id="event-description">')
text('把街角的颜色、声音与相遇，',80,1073,27,'Study CJK')
text('变成每个人都能参与的艺术现场。',80,1115,27,'Study CJK')
put('</g>')

# The landscape grows from a blue foundation into an asymmetric stepped edge.
put('<g id="module-landscape">')
rect(0,1348,1080,180,'blue')

# Left shoulder, clipped concentric quarter circles.
arcs(0,1168,180,'pink','orange',(False,True))
# A round-corner folded block rises by a half-module beside it.
path('M180 1348 V1258 H270 A90 90 0 0 1 360 1348 Z','orange')
# Two-colour diamond sits flush in the lower left module.
path('M0 1438 L90 1348 L180 1438 Z','orange')
path('M0 1438 L90 1528 L180 1438 Z','pink')
dual(180,1348,180,'lightblue')
arcs(360,1348,180,'orange','pink',(False,True))

# The warm focal flower rises out of the foundation on the central step.
rect(540,1258,180,270,'blue')
yellow_flower(612,1258,112.5)
# Lower half-module gives the flower a blue margin and paired round-pointed leaves.
path('M540 1462 C540 1412 577 1394 625 1394 C625 1438 592 1462 540 1462 Z','lightblue')
path('M720 1462 C720 1412 683 1394 635 1394 C635 1438 668 1462 720 1462 Z','pink')

# Interior stair: one large rounded corner, then a complete six-ring module.
path('M720 1168 V1078 A90 90 0 0 1 810 988 H900 V1168 Z','orange')
path('M810 1084 C771 1084 756 1055 756 1020 C793 1020 810 1047 810 1084 Z','pink')
path('M810 1084 C849 1084 864 1055 864 1020 C827 1020 810 1047 810 1084 Z','lightblue')
rect(720,1168,180,180,'pink')
for yy in [1219,1297]:
    for xx in [750,810,870]: circle(xx,yy,21,'none','orange',4.2)
arcs(720,1348,180,'lightblue','blue',(True,True))

# Outer spine: double semicircles, corner arcs, a complete red flower and fold.
dual(900,628,180,'pink')
arcs(900,808,180,'orange','cream',(True,True))
rect(900,988,180,180,'lightblue')
red_flower(990,1078,90)
dual(900,1168,180,'pink')
rect(900,1348,180,180,'pink')
path('M900 1348 H1080 V1528 H990 A90 90 0 0 1 900 1438 Z','blue')
# A single connected triangular edge stays inside its half-height module.
path('M900 1348 L945 1393 L990 1348 L1035 1393 L1080 1348 Z','red')
put('</g>')
put('</svg>')
(HERE/'raw.svg').write_text('\n'.join(parts)+'\n')
subprocess.run(['/private/tmp/folio-memphis-tools/bin/python',str(INPUT/'embed_fonts.py'),str(INPUT/'fonts'),str(HERE/'raw.svg'),str(HERE/'poster.svg')],check=True)
licenses=HERE/'font-licenses'
licenses.mkdir(exist_ok=True)
for name in ['Inter-OFL.txt','Noto-OFL.txt','Pixel-OFL.txt']:
    shutil.copyfile(INPUT/'fonts'/name,licenses/name)
(HERE/'uncertainties.md').write_text('''# Input decisions\n\n- The brief fixes a portrait canvas but does not select a white or blue reading field. This version uses paper with ink text, and blue English lettering.\n- No authorized MOLLY logo asset is supplied. The brand is rebuilt as live Inter 900 text, as permitted by DESIGN.md.\n- The documents do not prescribe an exact module map, text alignment, or motif order. The landscape uses a bottom foundation, a low left shoulder, and a taller stepped right edge, with a larger layered yellow flower as its focus.\n- The description is split at its existing comma into two editable lines; the English title is split after “ART IN”. Neither changes the supplied wording.\n- No additional event facts or decorative text have been introduced.\n''')
