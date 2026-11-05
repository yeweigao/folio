#!/usr/bin/env python3
"""Draw the native 900 × 1200 SVG; embed provided fonts separately."""
from pathlib import Path
from math import cos, sin, radians
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent
C = {
    'blue': '#1900F5', 'grid': '#796EFF', 'paper': '#FFFFF2',
    'green': '#00ECA9', 'yellow': '#FBFF08', 'pink': '#FA4EF5',
    'coral': '#FF6977', 'violet': '#7C42FF',
}
parts = []

def emit(s):
    parts.append(s)

def polygon(points, fill, **attrs):
    extra = ' '.join(f'{k.replace("_", "-")}="{v}"' for k, v in attrs.items())
    p = ' '.join(f'{x:g},{y:g}' for x, y in points)
    emit(f'<polygon points="{p}" fill="{C[fill]}" {extra}/>')

def text(x, y, value, role='body', **attrs):
    extra = ' '.join(f'{k.replace("_", "-")}="{v}"' for k, v in attrs.items())
    emit(f'<text x="{x}" y="{y}" class="{role}" {extra}>{escape(value)}</text>')

def window(x, y, w, h, fill='paper', header=32, controls=True):
    emit(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{C[fill]}"/>')
    emit(f'<path d="M{x} {y+header}H{x+w}" fill="none"/>')
    if controls:
        for dx in (w-53, w-36, w-19):
            emit(f'<path d="M{x+dx-3} {y+header/2}h6" fill="none" stroke-width="2.7"/>')

emit('''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1200" viewBox="0 0 900 1200" role="img" aria-labelledby="poster-title poster-desc">
<title id="poster-title">BUILD-ATHON</title>
<desc id="poster-desc">BUILD-ATHON. TYO, SEL, SIN, SYD. 06.18.27 and 06.19.27. REMOTE TEAMS WELCOME. MAKE WHAT CONNECTS US. stripe.</desc>
<!-- FONTS -->
<style>
  .display { font-family: "Study Condensed", sans-serif; font-size: 146.7px; font-weight: 700; }
  .facts { font-family: "Study Condensed", sans-serif; font-size: 68.4px; font-weight: 700; }
  .label { font-family: "Study Sans", sans-serif; font-size: 27px; font-weight: 700; }
  .body { font-family: "Study Sans", sans-serif; font-size: 21.6px; font-weight: 400; }
  text { fill: #1900F5; stroke: none; }
</style>''')
emit(f'<rect width="900" height="1200" fill="{C["blue"]}"/>')
emit(f'<g id="drawing-grid" stroke="{C["grid"]}" stroke-width="0.9" fill="none">')
for x in range(0, 901, 50):
    emit(f'<path d="M{x} 0V1200"/>')
for y in range(0, 1201, 50):
    emit(f'<path d="M0 {y}H900"/>')
emit('</g>')

emit(f'<g stroke="{C["blue"]}" stroke-width="1.8" stroke-linejoin="miter">')

# Broad cut disc and closed cylinder: circular planes stay circular/elliptical.
emit('<g id="disc-and-cylinder">')
emit(f'<circle cx="730" cy="355" r="155" fill="{C["green"]}"/>')
emit(f'<path d="M598 153V350 A109 33 0 0 0 816 350V153 Z" fill="{C["coral"]}"/>')
emit(f'<ellipse cx="707" cy="153" rx="109" ry="33" fill="{C["yellow"]}"/>')
emit('</g>')

# Unequal alternating points produce one flat cut shape beneath the city solid.
emit('<g id="cut-burst">')
radii = [118, 58, 98, 55, 113, 61, 105, 52, 120, 59,
         102, 55, 114, 63, 99, 52, 117, 59, 106, 55]
burst = []
for i, r in enumerate(radii):
    a = radians(-96 + i * 18)
    burst.append((585 + cos(a)*r, 1036 + sin(a)*r))
polygon(burst, 'pink')
emit('</g>')

# Shared vertices define the complete top, side and front of one city block.
emit('<g id="city-block">')
polygon([(135,725), (230,630), (540,630), (445,725)], 'yellow')
polygon([(445,725), (540,630), (540,990), (445,1085)], 'violet')
polygon([(135,725), (445,725), (445,1085), (135,1085)], 'green')
emit('<g transform="matrix(1 0 -1 1 230 630)">')
text(22, 37, 'REMOTE TEAMS')
text(22, 65, 'WELCOME')
emit('</g>')
for y, city in [(810,'TYO'), (892,'SEL'), (974,'SIN'), (1056,'SYD')]:
    text(158, y, city, 'facts')
emit('</g>')

# Date echoes turn in the opposite direction from the principal title stack.
emit('<g id="date-stack">')
for x, y in [(466,604), (454,616), (442,628)]:
    window(x, y, 350, 234, controls=False, header=30)
window(430, 640, 350, 234, fill='yellow', header=30)
text(453, 752, '06.18.27', 'facts')
text(453, 836, '06.19.27', 'facts')
emit('</g>')

# The paper title is drawn last so every required front label stays intact.
emit('<g id="title-stack">')
for x, y in [(46,162), (62,178), (78,194)]:
    window(x, y, 560, 404, controls=False)
window(94, 210, 560, 404)
emit('<text class="display" aria-label="BUILD-ATHON"><tspan x="118" y="398">BUILD-</tspan><tspan x="198" y="544">ATHON</tspan></text>')
text(118, 589, 'MAKE WHAT CONNECTS US')
text(544, 589, 'stripe', 'label')
emit('</g>')
emit('</g></svg>')

OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'raw.svg').write_text('\n'.join(parts) + '\n')
print(OUT / 'raw.svg')
