#!/usr/bin/env python3
"""Culture Monsters: a new, native-vector 900 × 1200 activity poster.

Input authority: the adjacent input-v3/DESIGN.md and brief.md only.
All artwork below is authored here. Text stays as live SVG text.
"""
from pathlib import Path
from html import escape
from math import sin, cos, pi
import subprocess
import sys
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
INPUT = HERE.parent / 'input-v3'
W, H = 900, 1200
P = {'paper':'#FFFFFF', 'ink':'#030303', 'red':'#FF354A',
     'pink':'#FD8CE5', 'yellow':'#FFE42C', 'blue':'#1768F6'}
parts = []


def add(s):
    parts.append(s)


def rect(x, y, w, h, color):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{P[color]}"/>')


def circle(x, y, r, color):
    add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{P[color]}"/>')


def path(d, color):
    add(f'<path d="{d}" fill="{P[color]}"/>')


def eye(x, y, diameter, pupil):
    circle(x, y, diameter / 2, 'paper')
    circle(x, y, pupil / 2, 'ink')


def text(x, y, size, weight, value, ident):
    add(f'<text id="{ident}" x="{x}" y="{y}" font-size="{size}" '
        f'font-weight="{weight}" fill="{P["ink"]}" '
        f'font-family="Study Sans, Study CJK, sans-serif">{escape(value)}</text>')


def ring(cx, cy, radius, count, dot, color):
    for i in range(count):
        a = 2 * pi * i / count - pi / 2
        circle(round(cx + radius * cos(a), 4),
               round(cy + radius * sin(a), 4), dot / 2, color)


def badge(cx, cy, rx, ry, color):
    # Seven rounded lobes; broad horizontal proportions, without spines.
    pts = []
    n = 112
    for i in range(n):
        a = 2 * pi * i / n
        r = 1 + 0.11 * cos(7 * a)
        pts.append((cx + rx * r * cos(a), cy + ry * r * sin(a)))
    d = f'M {pts[0][0]:.4f},{pts[0][1]:.4f} '
    # A periodic cubic interpolation keeps the outline fully editable and soft.
    for i in range(n):
        p0, p1 = pts[(i-1) % n], pts[i]
        p2, p3 = pts[(i+1) % n], pts[(i+2) % n]
        c1 = (p1[0] + (p2[0]-p0[0])/6, p1[1] + (p2[1]-p0[1])/6)
        c2 = (p2[0] - (p3[0]-p1[0])/6, p2[1] - (p3[1]-p1[1])/6)
        d += f'C {c1[0]:.4f},{c1[1]:.4f} {c2[0]:.4f},{c2[1]:.4f} {p2[0]:.4f},{p2[1]:.4f} '
    path(d + 'Z', color)


add('<?xml version="1.0" encoding="UTF-8"?>')
add('<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1200" viewBox="0 0 900 1200" role="img" aria-labelledby="poster-title poster-description">')
add('<title id="poster-title">TTXC 2027 · 城市游乐场 · City Play!</title>')
add('<desc id="poster-description">Flat, unequal creature and pattern modules surround a white activity-title crossing; a smaller module run continues beside the red event information.</desc>')
# Preserve the readable license notices with the embedded font document.
licenses = '\n\n'.join((INPUT / 'fonts' / name).read_text() for name in ('Inter-OFL.txt', 'Noto-OFL.txt'))
add('<metadata id="font-licenses">' + escape(licenses) + '</metadata>')
add('<!-- FONTS -->')
add('<defs>')
add('<clipPath id="top-cyclops-clip"><rect width="337.5" height="450"/></clipPath>')
add('<clipPath id="poster-trim"><rect width="900" height="1200"/></clipPath>')
add('</defs>')
add('<g clip-path="url(#poster-trim)">')
rect(0, 0, W, H, 'red')

# The dominant single-eye silhouette is taller, rather than wider, than peers.
add('<g id="large-stacked-cyclops" clip-path="url(#top-cyclops-clip)">')
rect(0, 0, 337.5, 450, 'blue')
circle(168.75, 94.5, 94.5, 'pink')
circle(168.75, 211.5, 105, 'pink')
circle(168.75, 351, 135, 'pink')
eye(168.75, 350, 124, 70)
add('</g>')

# Red remains a reading region within the collage, not only a bottom footer.
add('<g id="description-field">')
rect(337.5, 0, 337.5, 225, 'red')
add('<text id="description" x="359.1" y="86" font-size="27" font-weight="700" fill="#030303" font-family="Study Sans, Study CJK, sans-serif">ART × SOUND × <tspan x="359.1" y="124">TECHNOLOGY</tspan></text>')
add('</g>')

# Coarse elliptical petals occupy a full single-u module.
add('<g id="petal-pattern">')
rect(337.5, 225, 225, 225, 'yellow')
for i in range(8):
    add(f'<ellipse cx="450" cy="282.5" rx="23.5" ry="55" fill="{P["ink"]}" transform="rotate({45*i} 450 337.5)"/>')
add('</g>')

# The half-u modules establish a smaller visual scale.
add('<g id="small-dot-ring">')
rect(562.5, 225, 112.5, 112.5, 'ink')
ring(618.75, 281.25, 34.5, 8, 18, 'pink')
add('</g>')
add('<g id="small-triangle-pattern">')
rect(562.5, 337.5, 112.5, 112.5, 'blue')
for i in range(6):
    a = -pi/2 + i * pi/3
    points = [(618.75 + r*cos(ang), 393.75 + r*sin(ang))
              for r,ang in ((12,a),(54,a-0.22),(54,a+0.22))]
    path('M ' + ' L '.join(f'{x:.4f},{y:.4f}' for x,y in points) + ' Z', 'yellow')
add('</g>')

# Long separated waves make this body distinct from the stacked cyclops.
add('<g id="long-tentacled-companion">')
rect(675, 0, 225, 450, 'pink')
path('M 697.5,163 C 697.5,95 728,55 787.5,55 C 847,55 877.5,95 877.5,163 Z', 'blue')
strand_data = [
    'M 709,157 C 709,192 729,212 717,243 S 697,286 710,316 S 721,345 710,374',
    'M 740,157 C 740,193 753,215 743,246 S 730,288 742,321 S 753,359 742,391',
    'M 771,157 C 771,188 758,215 768,245 S 782,285 771,315 S 758,342 769,369',
    'M 803,157 C 803,189 817,214 807,244 S 793,285 805,318 S 815,353 804,382',
    'M 834,157 C 834,189 822,217 832,247 S 846,287 836,317 S 824,348 835,375',
    'M 866,157 C 866,192 879,217 868,250 S 855,293 866,327 S 877,366 866,397',
]
for d in strand_data:
    add(f'<path d="{d}" fill="none" stroke="{P["blue"]}" stroke-width="9" stroke-linecap="round"/>')
eye(756, 120, 33, 18)
eye(820, 120, 33, 18)
add('</g>')

# The shallow paper crossing remains wide enough for ordinary-width live type.
add('<g id="paper-title-crossing">')
rect(0, 450, 900, 150, 'paper')
text(21.6, 564, 105.3, 900, 'TTXC 2027', 'activity')
add('</g>')

# A narrower continuation reaches the lower trim beside the reading field.
add('<g id="lower-module-run">')
rect(0, 600, 225, 225, 'ink')
badge(112.5, 712.5, 91, 68, 'yellow')
eye(112.5, 700, 31, 17)
for x in (98.5, 112.5, 126.5):
    circle(x, 735, 4, 'ink')
rect(0, 825, 225, 225, 'yellow')
for i in range(8):
    add(f'<rect x="104.5" y="850.5" width="16" height="52" rx="8" fill="{P["blue"]}" transform="rotate({45*i} 112.5 937.5)"/>')
rect(0, 1050, 225, 225, 'pink')
for i in range(3):
    x = i*75
    path(f'M {x},1050 L {x+75},1050 L {x+37.5},1162.5 Z', 'ink')
    path(f'M {x},1275 L {x+75},1275 L {x+37.5},1162.5 Z', 'ink')
add('</g>')

# One secondary theme is paired across two deliberate reading lines.
add('<g id="lower-information">')
text(249, 714, 86.4, 900, '城市游乐场', 'theme-zh')
text(249, 821, 86.4, 900, 'City Play!', 'theme-en')
text(249, 883, 21.6, 400, '一起把城市玩出新花样', 'slogan')
text(249, 986, 54, 900, '2027.09.10–12', 'date')
text(249, 1088, 54, 900, '海岸文化中心', 'venue-zh')
text(249, 1138, 27, 700, 'Coast Culture Center', 'venue-en')
add('</g>')
add('</g></svg>')

raw = '\n'.join(parts) + '\n'
raw_path = HERE / 'raw.svg'
raw_path.write_text(raw)
root = ET.fromstring(raw)
assert root.attrib['viewBox'] == '0 0 900 1200'
fixed = ('TTXC 2027', '城市游乐场', 'City Play!', 'ART × SOUND × TECHNOLOGY',
         '一起把城市玩出新花样', '2027.09.10–12', '海岸文化中心', 'Coast Culture Center')
actual = [''.join(e.itertext()) for e in root.iter() if e.tag.rsplit('}',1)[-1] == 'text']
for value in fixed:
    assert value in actual, (value, actual)
assert not any(e.tag.rsplit('}',1)[-1] == 'image' for e in root.iter())
subprocess.run([sys.executable, str(INPUT / 'embed_fonts.py'), str(INPUT / 'fonts'),
                str(raw_path), str(HERE / 'poster.svg')], check=True)
poster = (HERE / 'poster.svg').read_text()
ET.fromstring(poster)
assert 'data:font/woff2;base64,' in poster
print('Verified XML, 900 × 1200, eight exact editable strings, no raster images, and embedded font data.')
