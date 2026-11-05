#!/usr/bin/env python3
"""Draw a native, editable SVG from this case's DESIGN.md and brief only."""
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
CASE = HERE.parent
C = {
    'paper': '#FFFFFF',
    'ink': '#000000',
    'pink': '#F4A2C9',
    'blue': '#4B53E6',
    'yellow': '#FFE840',
    'green': '#20A90D',
}

parts = ['''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1200" viewBox="0 0 900 1200" role="img" aria-labelledby="poster-title poster-description">
<title id="poster-title">forest — After Hours, 2027</title>
<desc id="poster-description">An open-air music poster with a pink, three-lobed forest character, large asymmetric eyes, a pink and black checkerboard, a yellow upper field, and a blue information field with a green tree.</desc>
<!-- FONTS -->
<defs>
  <clipPath id="checker-clip"><path d="M0 0H252V126H900V252H252V800H0Z"/></clipPath>
</defs>
''']

def add(markup):
    parts.append(markup)

# Large unbroken color fields establish the vertical rhythm.
add(f'<rect id="upper-yellow-field" width="900" height="800" fill="{C["yellow"]}"/>')
add(f'<rect id="lower-blue-field" y="800" width="900" height="400" fill="{C["blue"]}"/>')

# Two full-size cells across the left column; the same grid turns across the top.
# The final row and final column meet the outer edge without squeezing the cells.
add('<g id="checkerboard-frame" clip-path="url(#checker-clip)">')
for row in range(7):
    for col in range(8):
        color = C['pink'] if (row + col) % 2 == 0 else C['ink']
        add(f'<rect x="{col * 126}" y="{row * 126}" width="126" height="126" fill="{color}"/>')
add('</g>')

# All lettering remains SVG text; the provided support utility embeds the fonts.
add(f'''<g id="masthead" fill="{C['ink']}" font-family="Study Sans, sans-serif" font-weight="900">
  <text id="brand" x="289" y="105" font-size="112" letter-spacing="-5">forest</text>
  <text id="event-theme" x="291" y="359" font-size="86" letter-spacing="-3.4">After Hours</text>
</g>''')

# Three overlapping flattened ovals make one soft character with an uneven gaze.
add(f'''<g id="forest-character">
  <g id="three-lobed-body" fill="{C['pink']}">
    <ellipse cx="614" cy="486" rx="216" ry="82"/>
    <ellipse cx="612" cy="584" rx="255" ry="88"/>
    <ellipse cx="615" cy="684" rx="232" ry="80"/>
  </g>
  <g id="asymmetric-eyes" fill="{C['paper']}">
    <ellipse cx="565" cy="475" rx="49" ry="61"/>
    <ellipse cx="674" cy="465" rx="33" ry="44"/>
  </g>
  <g id="pupils" fill="{C['ink']}">
    <ellipse cx="579" cy="477" rx="19" ry="30"/>
    <ellipse cx="685" cy="467" rx="12" ry="22"/>
  </g>
</g>''')

# Reading information, rotated date, and tree occupy three distinct lower zones.
add(f'''<g id="event-information" fill="{C['paper']}" font-family="Study Sans, sans-serif">
  <text id="event-time" x="35" y="859" font-size="35" font-weight="700" letter-spacing="-0.6">18:30–22:00</text>
  <text id="event-location" x="35" y="904" font-size="26" font-weight="700" letter-spacing="-0.5">Riverside Forest Stage</text>
  <text id="event-description" font-size="24" font-weight="400"><tspan x="35" y="956">Open-air music returns to the </tspan><tspan x="35" y="990">riverside forest. Bring your friends, </tspan><tspan x="35" y="1024">follow the lights, and spend a </tspan><tspan x="35" y="1058">summer evening among the trees.</tspan></text>
  <text id="event-year" x="31" y="1180" font-size="104" font-weight="900" letter-spacing="-6">2027</text>
</g>
<g id="vertical-date-capsule">
  <rect x="521" y="840" width="78" height="330" rx="39" fill="{C['pink']}"/>
  <text id="event-date" transform="translate(560 1005) rotate(-90)" x="0" y="0" dy="0.36em" text-anchor="middle" fill="{C['ink']}" font-family="Study Sans, sans-serif" font-size="44" font-weight="700" letter-spacing="-1.2">07.03–07.24</text>
</g>
<g id="forest-tree">
  <rect x="755" y="1090" width="33" height="110" fill="{C['ink']}"/>
  <path d="M771 835 L824 910 H801 L851 974 H826 L879 1043 H850 L900 1114 H867 L900 1161 H642 L675 1114 H642 L692 1043 H663 L716 974 H691 L741 910 H718 Z" fill="{C['green']}"/>
</g>
</svg>''')

raw = HERE / 'raw.svg'
raw.write_text('\n'.join(parts), encoding='utf-8')
subprocess.run([sys.executable, str(CASE / 'input' / 'embed_fonts.py'), str(CASE / 'input' / 'fonts'), str(raw), str(HERE / 'poster.svg')], check=True)
print(raw)
