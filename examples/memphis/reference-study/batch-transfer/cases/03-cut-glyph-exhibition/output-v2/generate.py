#!/usr/bin/env python3
"""Native, editable exhibition poster. Geometry and composition authored here."""
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
CASE = HERE.parent
C = dict(green='#07964F', ink='#050505', paper='#FFFFFF', pink='#F3579D',
         purple='#9B38ED', orange='#FF7829', blue='#0759FD', yellow='#FFF035')

def path(id, d, fill):
    return f'<path id="{id}" d="{d}" fill="{C[fill]}"/>'

def rect(id, x, y, w, h, fill):
    return f'<rect id="{id}" x="{x}" y="{y}" width="{w}" height="{h}" fill="{C[fill]}"/>'

def text(id, x, y, content, family, size, weight, color, anchor='start'):
    return (f'<text id="{id}" x="{x}" y="{y}" font-family="{family}" '
            f'font-size="{size}" font-weight="{weight}" fill="{C[color]}" '
            f'text-anchor="{anchor}">{content}</text>')

svg = ['''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1200" viewBox="0 0 900 1200" role="img" aria-labelledby="poster-title poster-description">
<title id="poster-title">共生设计展 — COEXIST DESIGN EXHIBITION</title>
<desc id="poster-description">12 JUNE to 28 AUGUST, 09:00–18:00. 城市设计馆。策展：林岚。</desc>
<!-- FONTS -->
<style>text{font-kerning:normal;text-rendering:geometricPrecision}path,rect,circle{shape-rendering:geometricPrecision}</style>
''']
svg += [rect('green-field', 0, 0, 450, 1200, 'green'), rect('ink-field', 450, 0, 450, 1200, 'ink')]

# Module g = 414; principal stroke = 92. Outer bends = 182, inner bends = 90.
# The green counters are actual openings between joined strokes, not overlays.
svg.append('<g id="display-gong" aria-label="共">')
svg += [
    rect('gong-upper-left-upright', 142, 32, 92, 245, 'paper'),
    rect('gong-upper-right-upright', 340, 32, 92, 540, 'paper'),
    path('gong-first-cross-stroke-and-turn',
         'M18 480 V367 A182 182 0 0 1 200 185 H432 V277 H200 A90 90 0 0 0 110 367 V480 Z', 'paper'),
    rect('gong-second-cross-stroke', 18, 480, 414, 92, 'paper'),
    path('gong-left-leg',
         'M110 572 H202 V950 A182 182 0 0 1 20 1132 V1040 A90 90 0 0 0 110 950 Z', 'paper'),
    path('gong-right-leg',
         'M250 572 H342 V950 A90 90 0 0 0 432 1040 V1132 A182 182 0 0 1 250 950 Z', 'paper')
]
svg.append('</g>')

svg.append('<g id="display-sheng" aria-label="生">')
svg += [
    path('sheng-upper-curved-stroke',
         'M468 214 A182 182 0 0 1 650 32 H766 V124 H650 A90 90 0 0 0 558 214 Z', 'purple'),
    rect('sheng-top-central-upright', 674, 124, 92, 247, 'pink'),
    rect('sheng-first-cross-stroke', 468, 214, 414, 92, 'pink'),
    path('sheng-blue-junction', 'M766 124 A90 90 0 0 1 856 214 H766 Z', 'blue'),
    rect('sheng-central-stroke-return', 674, 596, 92, 50, 'pink'),
    path('sheng-middle-cross-stroke-and-return',
         'M468 646 H700 A182 182 0 0 1 882 828 V950 H790 V828 A90 90 0 0 0 700 738 H468 Z', 'pink'),
    path('sheng-lower-cross-stroke-and-turn',
         'M882 950 A182 182 0 0 1 700 1132 H468 V1040 H700 A90 90 0 0 0 790 950 Z', 'orange')
]
svg.append('</g>')

# The whole exhibition name is live type in the broad curved counter.
svg.append('<g id="exhibition-title-cjk" aria-label="共生设计展">')
svg += [text('title-cjk-line-one', 328, 353, '共生', 'Study CJK', 68.4, 900, 'ink', 'end'),
        text('title-cjk-line-two', 328, 446, '设计展', 'Study CJK', 68.4, 900, 'ink', 'end')]
svg.append('</g>')

# Venue occupies the upper, open-ended slot between the two uprights.
svg.append('<g id="venue" aria-label="城市设计馆">')
svg += [text('venue-line-one', 250, 95, '城市', 'Study CJK', 22, 400, 'ink'),
        text('venue-line-two', 250, 132, '设计馆', 'Study CJK', 22, 400, 'ink')]
svg.append('</g>')

# Curatorial credit runs in reading order down the long slot between the legs.
svg.append('<g id="curator" aria-label="策展：林岚">')
for index, char in enumerate('策展：林岚'):
    svg.append(text(f'curator-{index + 1}', 215, 700 + 38 * index, char,
                    'Study CJK', 22, 400, 'ink'))
svg.append('</g>')
svg.append(f'<circle id="notch-node" cx="226" cy="923" r="19" fill="{C["yellow"]}"/>')

# Latin title spans the first horizontal cut, with normal-width letterforms.
svg.append('<g id="exhibition-title-latin" aria-label="COEXIST DESIGN EXHIBITION">')
for index, (line, y) in enumerate([('COEXIST', 426), ('DESIGN', 497), ('EXHIBITION', 568)]):
    svg.append(text(f'title-latin-line-{index + 1}', 490, y, line,
                    'Study Sans', 53.1, 900, 'paper'))
svg.append('</g>')

# Calendar and time inhabit the lower break, enclosed by the curved main stroke.
svg.append('<g id="date-range" aria-label="12 JUNE – 28 AUGUST">')
svg += [text('start-date', 490, 818, '12 JUNE', 'Study Sans', 43.2, 700, 'paper'),
        text('end-date', 490, 886, '28 AUGUST', 'Study Sans', 43.2, 700, 'paper')]
svg.append('</g>')
svg.append(text('opening-hours', 490, 978, '09:00–18:00', 'Study Sans', 43.2, 700, 'paper'))
svg.append('</svg>')
raw = HERE / 'raw.svg'
raw.write_text('\n'.join(svg), encoding='utf-8')
subprocess.run([sys.executable, str(CASE / 'input-v2' / 'embed_fonts.py'),
                str(CASE / 'input-v2' / 'fonts'), str(raw), str(HERE / 'poster.svg')], check=True)
