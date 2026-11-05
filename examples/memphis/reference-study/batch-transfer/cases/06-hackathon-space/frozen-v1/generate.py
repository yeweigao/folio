#!/usr/bin/env python3
"""Original, editable 900 × 1200 SVG for the supplied transfer brief."""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent
PAPER = '#FFFFF2'
BLUE = '#1900F5'
GREEN = '#00ECA9'
PINK = '#FA4EF5'
YELLOW = '#FBFF08'
VIOLET = '#7C42FF'

parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1200" viewBox="0 0 900 1200" role="img" aria-labelledby="poster-title poster-description">
<title id="poster-title">BUILD-ATHON</title>
<desc id="poster-description">A developer event poster with stacked interface windows on a drawing grid. TYO, SEL, SIN, SYD. 06.18.27 and 06.19.27. Remote teams welcome. Make what connects us. stripe.</desc>
<!-- FONTS -->
<defs>
  <pattern id="drawing-grid" width="50" height="50" patternUnits="userSpaceOnUse">
    <path d="M 50 0 L 0 0 0 50" fill="none" stroke="{BLUE}" stroke-width="0.85" opacity="0.3"/>
  </pattern>
</defs>
<rect width="900" height="1200" fill="{PAPER}"/>
<rect width="900" height="1200" fill="url(#drawing-grid)"/>
''']

def frame(x, y, w, h, fill, header=None, bar=48, weight=2.3):
    """A rectangular surface with a shared, thin window boundary."""
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{BLUE}" stroke-width="{weight}"/>')
    if header:
        parts.append(f'<path d="M{x},{y+bar} V{y} H{x+w} V{y+bar} Z" fill="{header}" stroke="{BLUE}" stroke-width="{weight}"/>')
    else:
        parts.append(f'<path d="M{x},{y+bar} H{x+w}" fill="none" stroke="{BLUE}" stroke-width="{weight}"/>')

def text(content, x, y, size, family='Study Condensed', weight=700, fill=BLUE, anchor='start', tracking=0):
    parts.append(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" letter-spacing="{tracking}">{escape(content)}</text>')

# The organizer is part of the poster, set as editable type.
text('stripe', 75, 81, 43, 'Study Sans', 900, tracking=-1.9)

# One principal window. Copies retreat in equal fourteen-pixel increments.
parts.append('<g id="main-window-stack">')
for x, y, fill in [
    (145, 135, PAPER),
    (131, 149, PINK),
    (117, 163, YELLOW),
    (103, 177, PAPER),
    (89, 191, GREEN),
]:
    frame(x, y, 630, 470, fill)
frame(75, 205, 630, 470, VIOLET, GREEN, bar=50)
text('REMOTE TEAMS WELCOME', 106, 238, 24, 'Study Sans', 700, tracking=0.15)
# Window controls use geometry; no fact is converted to an outline.
parts.append(f'<path d="M644,229 H657 M675,222 L689,236 M689,222 L675,236" fill="none" stroke="{BLUE}" stroke-width="2.3"/>')
parts.append(f'''<text font-family="Study Condensed" font-size="150" font-weight="700" fill="{PAPER}" letter-spacing="0.3"><tspan x="109" y="421">BUILD-</tspan><tspan x="254" y="587">ATHON</tspan></text>''')
parts.append('</g>')

# City panel: a secondary window connected by overlap to the main surface.
parts.append('<g id="city-window-stack">')
for x, y, fill in [
    (568, 662, PAPER),
    (556, 674, YELLOW),
    (544, 686, PINK),
    (532, 698, PAPER),
]:
    frame(x, y, 250, 400, fill, bar=40)
frame(520, 710, 250, 400, GREEN, PINK, bar=40)
parts.append(f'<path d="M538,724 H550 V736 H538 Z M561,724 H573 V736 H561 Z M584,724 H596 V736 H584 Z M736,730 H752" fill="none" stroke="{BLUE}" stroke-width="2"/>')
for city, baseline in [('TYO', 824), ('SEL', 901), ('SIN', 978), ('SYD', 1055)]:
    text(city, 645, baseline, 70, anchor='middle', tracking=1.1)
parts.append('</g>')

# Dates share the same axis and level in a small foreground window.
parts.append('<g id="date-window-stack">')
for x, y, fill in [(119, 621, PAPER), (107, 633, PINK)]:
    frame(x, y, 330, 185, fill, bar=30)
frame(95, 645, 330, 185, YELLOW, VIOLET, bar=30)
parts.append(f'<path d="M112,660 H125 M133,660 H146 M392,654 L404,666 M404,654 L392,666" fill="none" stroke="{PAPER}" stroke-width="2"/>')
text('06.18.27', 260, 735, 44, anchor='middle', tracking=1.4)
text('06.19.27', 260, 796, 44, anchor='middle', tracking=1.4)
parts.append('</g>')

# An independent reading group has one full line-height of breathing room.
parts.append(f'''<text font-family="Study Condensed" font-size="45" font-weight="700" fill="{BLUE}" letter-spacing="0.5"><tspan x="75" y="1009">MAKE WHAT</tspan><tspan x="75" y="1063">CONNECTS US</tspan></text>''')
parts.append('</svg>')
(OUT / 'raw.svg').write_text('\n'.join(parts) + '\n')
print(OUT / 'raw.svg')
