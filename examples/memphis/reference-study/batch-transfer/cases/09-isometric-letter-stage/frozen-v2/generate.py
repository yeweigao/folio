#!/usr/bin/env python3
"""A native, shared-edge isometric stage; all lettering stays editable."""
from pathlib import Path
from html import escape
from fontTools.ttLib import TTFont

HERE = Path(__file__).resolve().parent
FONT = HERE.parent / 'input-v2' / 'fonts' / 'Oswald-700.ttf'
font = TTFont(FONT)
units = font['head'].unitsPerEm
cmap = font.getBestCmap()
cap = font['OS/2'].sCapHeight / units

C = dict(yellow='#FFDF06', ink='#000000', paper='#FFFFF3',
         blue='#2836B5', red='#FF2E05', green='#22B88A')
parts = []

def number(v):
    return f'{v:.4f}'.rstrip('0').rstrip('.')

def pt(x, y, z):
    return 400 + x - y, 625 + .425 * (x + y) - z

def polygon(points, color):
    points = ' '.join(f'{number(x)},{number(y)}' for x, y in points)
    parts.append(f'<polygon points="{points}" fill="{C[color]}"/>')

def block(name, x, y, w, d, bottom, top, roof, left, right):
    # Every visible edge comes from the same four world-space corners.
    back = pt(x, y, top)
    l = pt(x, y+d, top)
    front = pt(x+w, y+d, top)
    r = pt(x+w, y, top)
    lb = pt(x, y+d, bottom)
    fb = pt(x+w, y+d, bottom)
    rb = pt(x+w, y, bottom)
    parts.append(f'<g id="{name}" aria-label="{name.replace("-", " ")}">')
    polygon([l, front, fb, lb], left)
    polygon([front, r, rb, fb], right)
    polygon([back, r, front, l], roof)
    parts.append('</g>')
    return {'left': (l, w, top-bottom, .425),
            'right': (front, d, top-bottom, -.425)}

def advance(text):
    return sum(font['hmtx'].metrics[cmap[ord(ch)]][0] for ch in text) / units

def face_type(face, text, color, size=None, baseline=None, ident=None):
    (tx, ty), width, height, slope = face
    margin = .03 * width
    size = size or (width - 2*margin) / advance(text)
    baseline = baseline if baseline is not None else (height + cap*size) / 2
    # There is no horizontal type distortion: the face's affine map alone
    # determines the skew. Font size comes from the real font advances.
    attrs = f' id="{ident}"' if ident else ''
    parts.append(f'<g transform="matrix(1 {number(slope)} 0 1 {number(tx)} {number(ty)})">')
    parts.append(f'<text{attrs} x="{number(margin)}" y="{number(baseline)}" '
                 f'font-size="{number(size)}" fill="{C[color]}">{escape(text)}</text>')
    parts.append('</g>')
    return size

parts.append('''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1200" viewBox="0 0 900 1200" role="img" aria-labelledby="poster-title poster-description">
<title id="poster-title">KONBIN STAGE</title>
<desc id="poster-description">An open-air stage built from stacked isometric letter-bearing blocks. 17.07. OPEN AIR. RINA VEIL, LAGO, MOTIF CLUB, NEON PALMS. WE MAKE NOISE.</desc>
<!-- FONTS -->
<style>text{font-family:"Study Condensed",sans-serif;font-weight:700;font-kerning:none}</style>
<rect width="900" height="1200" fill="#FFDF06"/>
''')

# The narrow foundation is deliberately recessed under the white bridge.
foundation = block('foundation', 55, 40, 330, 260, -200, 0,
                   'ink', 'blue', 'red')
face_type(foundation['left'], 'WE MAKE NOISE', 'yellow', baseline=166,
          ident='slogan')

# A single continuous bright beam, with its reading surfaces meeting at
# the front vertical edge. The two title sizes yield nearly equal cap heights.
bridge = block('title-bridge', 0, 0, 440, 340, 0, 175,
               'ink', 'paper', 'paper')
face_type(bridge['left'], 'KONBIN', 'ink', ident='event-name-one')
face_type(bridge['right'], 'STAGE', 'ink', ident='event-name-two')

# The two rows of artists are distinct structural tiers. Their face widths
# track name length so their visible letter heights remain comparable.
artists_lower = block('lower-lineup', 55, 0, 330, 340, 175, 290,
                      'red', 'blue', 'green')
face_type(artists_lower['left'], 'MOTIF CLUB', 'yellow', ident='artist-three')
face_type(artists_lower['right'], 'NEON PALMS', 'ink', ident='artist-four')

artists_upper = block('upper-lineup', 80, 70, 260, 140, 290, 400,
                      'ink', 'green', 'blue')
face_type(artists_upper['left'], 'RINA VEIL', 'ink', ident='artist-one')
face_type(artists_upper['right'], 'LAGO', 'yellow', ident='artist-two')

# The uppermost small block carries the date and the type of venue.
crown = block('date-and-venue', 100, 75, 180, 130, 400, 540,
              'red', 'ink', 'blue')
face_type(crown['left'], '17.07', 'yellow', ident='date')
(tx, ty), width, height, slope = crown['right']
margin = .03 * width
open_size = (width-2*margin) / advance('OPEN')
air_size = (width-2*margin) / advance('AIR')
ink_height = cap*(open_size+air_size)
gap = 9
start = (height-ink_height-gap)/2
parts.append(f'<g transform="matrix(1 {number(slope)} 0 1 {number(tx)} {number(ty)})">')
parts.append(f'<text id="venue-type" fill="{C["yellow"]}" aria-label="OPEN AIR">'
             f'<tspan x="{number(margin)}" y="{number(start+cap*open_size)}" font-size="{number(open_size)}">OPEN</tspan> '
             f'<tspan x="{number(margin)}" y="{number(start+ink_height+gap)}" font-size="{number(air_size)}">AIR</tspan>'
             '</text></g>')

parts.append('</svg>')
HERE.mkdir(parents=True, exist_ok=True)
(HERE / 'raw.svg').write_text('\n'.join(parts))
print(HERE / 'raw.svg')
