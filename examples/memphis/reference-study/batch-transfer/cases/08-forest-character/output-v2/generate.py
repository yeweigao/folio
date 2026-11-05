#!/usr/bin/env python3
"""Create the original native geometry and editable text; embed supplied fonts."""
from pathlib import Path
from html import escape
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'output-v2'
OUT.mkdir(exist_ok=True)
C = dict(yellow='#FFE840', blue='#4B53E6', pink='#F4A2C9', green='#20A90D', paper='#FFFFFF', ink='#000000')
parts = ['''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1200" viewBox="0 0 900 1200" role="img" aria-labelledby="title description">
<title id="title">forest — After Hours, 2027</title>
<desc id="description">Forest music event poster. July 3 through July 24, 18:30–22:00 at Riverside Forest Stage. A blue three-layer character with adjoining white eyes fills a yellow field inside a black-and-white checker frame.</desc>
<!-- FONTS -->
''']
def rect(x,y,w,h,color,**attrs):
    more=''.join(f' {key}="{value}"' for key,value in attrs.items())
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}"{more}/>\n')
def ellipse(cx,cy,rx,ry,color):
    parts.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{color}"/>\n')
def text(x,y,content,size,weight=400,color=C['paper'],extra=''):
    parts.append(f'<text x="{x}" y="{y}" font-family="Study Sans" font-size="{size}" font-weight="{weight}" fill="{color}"{extra}>{escape(content)}</text>\n')
# Two adjoining fields.
rect(0,0,900,720,C['yellow'])
rect(0,720,900,480,C['blue'])
# A substantial, continuous, two-edge checker frame.
parts.append('<g id="checker-frame" shape-rendering="crispEdges">\n')
for col in range(10):
    rect(col*90,0,90,90,C['ink'] if col%2==0 else C['paper'])
for row in range(7):
    for col in range(2):
        rect(col*90,90+row*90,90,90,C['ink'] if (row+col)%2==1 else C['paper'])
parts.append('</g>\n')
text(224,220,'forest',137,900,C['ink'],extra=' letter-spacing="-4"')
# The three equally wide soft layers form a 615 × 410 body.
parts.append('<g id="forest-character">\n')
for cy in (400,495,590):
    ellipse(535.5,cy,307.5,110,C['blue'])
# The adjoining eyes deliberately differ in size and sit above the body.
ellipse(510,345,88,108,C['paper'])
ellipse(680,349,86,99,C['paper'])
ellipse(499,348,26,59,C['ink'])
ellipse(669,353,25,55,C['ink'])
parts.append('</g>\n')
# Main information stays on one reading axis in the blue field.
parts.append('<g id="event-information">\n')
text(34,825,'After Hours',90,900,extra=' letter-spacing="-2.5"')
text(36,918,'Riverside Forest Stage',28,700)
text(36,958,'18:30–22:00',28,700)
parts.append('<text x="36" y="1036" font-family="Study Sans" font-size="25" font-weight="400" fill="#FFFFFF">\n')
for i,line in enumerate([
    'Open-air music returns to the riverside forest.',
    'Bring your friends, follow the lights, and spend',
    'a summer evening among the trees.'
]):
    parts.append(f'<tspan x="36" dy="{0 if i==0 else 35}">{escape(line)}</tspan>\n')
parts.append('</text>\n</g>\n')
# The date occupies its own upright capsule.
rect(620,754,104,412,C['pink'],rx=52)
text(0,0,'07.03–07.24',46,700,C['ink'],extra=' text-anchor="middle" dominant-baseline="central" transform="translate(672 960) rotate(-90)"')
# The green tree has its own black vertical surface, adjacent to the blue.
parts.append('<g id="tree-panel">\n')
rect(756,720,144,480,C['ink'])
text(828,792,'2027',32,700,extra=' text-anchor="middle"')
parts.append('''<path fill="#20A90D" d="M 828 844 L 850 888 L 839 888 L 863 936 L 850 936 L 877 990 L 859 990 L 886 1044 L 841 1044 L 841 1118 L 815 1118 L 815 1044 L 770 1044 L 797 990 L 779 990 L 806 936 L 793 936 L 817 888 L 806 888 Z"/>
</g>
</svg>
''')
raw=OUT/'raw.svg'
raw.write_text(''.join(parts))
subprocess.run([sys.executable, str(ROOT/'input-v2/embed_fonts.py'), str(ROOT/'input-v2/fonts'), str(raw), str(OUT/'poster.svg')], check=True)
