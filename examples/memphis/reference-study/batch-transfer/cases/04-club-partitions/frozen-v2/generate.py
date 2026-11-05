#!/usr/bin/env python3
"""Native geometry and live typography for the Club Partitions brief."""
from pathlib import Path
import subprocess
import sys
import xml.etree.ElementTree as ET
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'output-v2'
PAPER, INK, BLUE, RED = '#F9F9F6', '#000000', '#0969F9', '#FF3A06'

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1200" viewBox="0 0 900 1200" role="img" aria-labelledby="poster-title poster-desc">
<title id="poster-title">Night Assembly — 17.07.27 — FORMA CLUB</title>
<desc id="poster-desc">Night Assembly. Rosa Flux, Mika Lo. B2B until dawn. LOWER ROOM: Alba Phase, Dorian East, NEX. 17.07.27, 23:00. FORMA CLUB.</desc>
<!-- FONTS -->
<style>
  text {{ font-family: 'Study Sans', sans-serif; fill: {INK}; font-weight: 700; }}
  .lead {{ font-size: 86.4px; }}
  .names {{ font-size: 54px; }}
  .facts {{ font-size: 48.6px; }}
  .label {{ font-size: 21.6px; }}
  .body {{ font-size: 21.6px; font-weight: 400; }}
</style>
<defs>
  <clipPath id="upper-field"><path d="M560 0H900V640H330V530H560Z"/></clipPath>
  <clipPath id="lower-field"><rect x="0" y="530" width="320" height="670"/></clipPath>
</defs>
<rect id="shared-ink-field" width="900" height="1200" fill="{INK}"/>
<!-- A clipped arc and widening diagonal channel share the upper colour field. -->
<g id="upper-graphic" clip-path="url(#upper-field)">
  <rect x="330" y="0" width="570" height="640" fill="{BLUE}"/>
  <path d="M560 435L900 340V640H330V530H560Z" fill="{INK}"/>
  <path d="M560 540L900 374V640H330V530H560Z" fill="{RED}"/>
  <circle cx="1010" cy="40" r="347" fill="{INK}"/>
  <circle cx="1010" cy="40" r="335" fill="{PAPER}"/>
</g>
<!-- The lower trim carries a different contact: a broad paper cut and a local black lobe. -->
<g id="lower-graphic" clip-path="url(#lower-field)">
  <rect x="0" y="530" width="320" height="670" fill="{RED}"/>
  <circle cx="-85" cy="1120" r="332" fill="{INK}"/>
  <circle cx="-85" cy="1120" r="320" fill="{PAPER}"/>
  <path d="M320 920H260C207.533 920 165 962.533 165 1015C165 1067.467 207.533 1110 260 1110H320Z" fill="{INK}"/>
</g>
<!-- Reading rectangles are cut directly out of the shared ink field. -->
<g id="event-name">
  <rect x="10" y="10" width="540" height="240" fill="{PAPER}"/>
  <text class="lead" x="30" y="112"><tspan x="30" y="112">Night</tspan><tspan x="30" y="202">Assembly</tspan></text>
</g>
<g id="main-artists">
  <rect x="10" y="260" width="540" height="260" fill="{PAPER}"/>
  <text class="names" x="30" y="334"><tspan x="30" y="334">Rosa Flux</tspan><tspan x="30" y="393">Mika Lo</tspan></text>
  <text class="body" x="30" y="467">B2B until dawn</text>
</g>
<g id="lower-room">
  <rect x="330" y="650" width="560" height="300" fill="{PAPER}"/>
  <text class="label" x="350" y="686">LOWER ROOM</text>
  <text class="names" x="350" y="754"><tspan x="350" y="754">Alba Phase</tspan><tspan x="350" y="811">Dorian East</tspan><tspan x="350" y="868">NEX</tspan></text>
</g>
<g id="event-facts">
  <rect x="330" y="960" width="560" height="230" fill="{PAPER}"/>
  <text class="facts" x="350" y="1030">17.07.27</text>
  <text class="facts" x="870" y="1030" text-anchor="end">23:00</text>
  <text class="facts" x="350" y="1120">FORMA CLUB</text>
</g>
</svg>
'''

OUT.mkdir(exist_ok=True)
raw = OUT / 'raw.svg'
raw.write_text(svg)
subprocess.run([sys.executable, str(ROOT / 'input-v2/embed_fonts.py'), str(ROOT / 'input-v2/fonts'), str(raw), str(OUT / 'poster.svg')], check=True)

expected = ['Night', 'Assembly', 'Rosa Flux', 'Mika Lo', 'B2B until dawn', 'LOWER ROOM', 'Alba Phase', 'Dorian East', 'NEX', '17.07.27', '23:00', 'FORMA CLUB']
root = ET.fromstring(svg)
assert root.attrib['viewBox'] == '0 0 900 1200'
texts = [t.text for t in root.iter() if t.tag.rsplit('}', 1)[-1] in ('text', 'tspan') and t.text]
assert sorted(texts) == sorted(expected), texts
assert not any(t.tag.rsplit('}', 1)[-1] == 'image' for t in root.iter())
font = TTFont(ROOT / 'input-v2/fonts/Inter-700.ttf')
cmap = font.getBestCmap()
units = font['head'].unitsPerEm
for content, size, available in [('Assembly', 86.4, 500), ('Rosa Flux', 54, 500), ('Dorian East', 54, 520), ('FORMA CLUB', 48.6, 520)]:
    width = sum(font['hmtx'][cmap[ord(c)]][0] for c in content) / units * size
    assert width <= available, (content, width)
    print(f'{content}: advance {width:.2f}px / {available}px available')
print('Verified: dimensions, exact editable facts, no raster images, key line advances.')
