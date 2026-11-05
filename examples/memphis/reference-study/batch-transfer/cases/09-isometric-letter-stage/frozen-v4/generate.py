#!/usr/bin/env python3
"""Generate the v4 native, editable isometric lettering poster."""
from pathlib import Path
import json
import subprocess
import sys
import xml.etree.ElementTree as ET
from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent
FONT = ROOT / 'input-v4/fonts/Oswald-700.ttf'
C = dict(yellow='#FFDF06', ink='#000000', paper='#FFFFF3',
         blue='#2836B5', red='#FF2E05', green='#22B88A')
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)

def tag(name):
    return '{' + NS + '}' + name

def el(parent, name, **attrs):
    return ET.SubElement(parent, tag(name), {k.replace('_', '-'): str(v) for k, v in attrs.items()})

def n(value):
    return f'{value:.5f}'.rstrip('0').rstrip('.')

font = TTFont(FONT)
cmap = font.getBestCmap()
units = font['head'].unitsPerEm
hmtx = font['hmtx'].metrics
glyphs = font.getGlyphSet()
cap = font['OS/2'].sCapHeight / units

def width(text, size=1):
    return sum(hmtx[cmap[ord(ch)]][0] for ch in text) / units * size

def ink_bounds(text, size, spacing=0):
    cursor = 0
    boxes = []
    for ch in text:
        name = cmap[ord(ch)]
        pen = BoundsPen(glyphs)
        glyphs[name].draw(pen)
        if pen.bounds:
            x0, y0, x1, y1 = pen.bounds
            boxes.append((cursor + x0 / units * size, -y1 / units * size,
                          cursor + x1 / units * size, -y0 / units * size))
        cursor += hmtx[name][0] / units * size + spacing
    return (min(b[0] for b in boxes), min(b[1] for b in boxes),
            max(b[2] for b in boxes), max(b[3] for b in boxes))

# One world projection is used for every block and every letter-bearing plane.
# u = (1, .425), v = (-1, .425), vertical z points upwards.
def point(u, v, z):
    return (440 + u - v, 730 + .425 * (u + v) - z)

def polygon(parent, points, fill):
    return el(parent, 'polygon', points=' '.join(f'{n(x)},{n(y)}' for x, y in points), fill=C[fill])

root = ET.Element(tag('svg'), dict(width='900', height='1200', viewBox='0 0 900 1200',
                                  version='1.1', role='img', **{'aria-labelledby': 'poster-title poster-description'}))
el(root, 'title', id='poster-title').text = 'KONBIN STAGE — 17.07'
el(root, 'desc', id='poster-description').text = (
    'An isometric open-air stage made from editable type and shared-edge colored architecture. '
    'KONBIN STAGE. 17.07. OPEN AIR. WE MAKE NOISE. RINA VEIL. LAGO. MOTIF CLUB. NEON PALMS.')
root.append(ET.Comment(' FONTS '))
el(root, 'rect', x='0', y='0', width='900', height='1200', fill=C['yellow'])
architecture = el(root, 'g', id='isometric-architecture', **{'shape-rendering': 'geometricPrecision'})
audit = []

# Cuboids share their calculated vertices exactly. Every roof and wall is a
# native polygon, and every word remains a native SVG text element.
def block(identifier, u0, u1, v0, v1, z0, z1, top, front, side):
    g = el(architecture, 'g', id=identifier)
    A, B, Cc, D = [point(u, v, z1) for u, v in [(u0,v0),(u1,v0),(u1,v1),(u0,v1)]]
    Ab, Bb, Cb, Db = [point(u, v, z0) for u, v in [(u0,v0),(u1,v0),(u1,v1),(u0,v1)]]
    polygon(g, [A,B,Cc,D], top)
    polygon(g, [D,Cc,Cb,Db], front)
    polygon(g, [Cc,B,Bb,Cb], side)
    front_g = el(g, 'g', id=identifier+'-front', transform=f'matrix(1 .425 0 1 {n(D[0])} {n(D[1])})')
    side_g = el(g, 'g', id=identifier+'-side', transform=f'matrix(1 -.425 0 1 {n(Cc[0])} {n(Cc[1])})')
    top_g = el(g, 'g', id=identifier+'-roof', transform=f'matrix(1 .425 -1 .425 {n(A[0])} {n(A[1])})')
    return dict(front=front_g, side=side_g, top=top_g, width=u1-u0, depth=v1-v0, height=z1-z0)

def text(parent, value, x, y, size, color, face_width, face_height, identifier, spacing=0, rotate=False):
    attrs = dict(id=identifier, fill=C[color], font_family='Study Condensed', font_weight='700',
                 font_size=n(size), **{'xml:space': 'preserve'})
    if spacing:
        attrs['letter_spacing'] = n(spacing)
    if rotate:
        attrs['transform'] = f'translate({n(x)} {n(y)}) rotate(-90)'
        attrs['x'] = '0'
        attrs['y'] = '0'
    else:
        attrs['x'] = n(x)
        attrs['y'] = n(y)
    t = el(parent, 'text', **attrs)
    t.text = value
    bx0, by0, bx1, by1 = ink_bounds(value, size, spacing)
    if rotate:
        box = (x + by0, y - bx1, x + by1, y - bx0)
    else:
        box = (x + bx0, y + by0, x + bx1, y + by1)
    # Bounds are tested in the unprojected coordinates of their own face.
    assert box[0] >= 0 and box[1] >= 0, (identifier, box)
    assert box[2] <= face_width and box[3] <= face_height, (identifier, box)
    audit.append(dict(id=identifier, text=value, font_size=round(size,5),
                      local_ink_bounds=[round(v,5) for v in box],
                      local_face=[face_width, face_height]))
    return t

# Feet make the large white object a bridge. They remain beneath its reading faces.
block('left-ink-pier', 0, 105, 292, 390, -65, 0, 'ink', 'ink', 'blue')
block('right-red-pier', 325, 430, 282, 390, -65, 0, 'red', 'red', 'ink')

bridge = block('white-title-bridge', 0, 430, 0, 390, 0, 190, 'green', 'paper', 'paper')
bridge['front'].set('aria-label', 'KONBIN')
bridge['side'].set('aria-label', 'STAGE')
bridge['top'].set('aria-label', 'WE MAKE NOISE')
text(bridge['front'], 'KONBIN', 13, 146, 126.5, 'ink', 430, 190, 'title-konbin')
stage_size = 126.5
stage_spacing = (364 - width('STAGE', stage_size)) / 4
text(bridge['side'], 'STAGE', 13, 146, stage_size, 'ink', 390, 190, 'title-stage', spacing=stage_spacing)

# A two-line slogan fills the clear portion of the bridge roof.
for value, baseline, identifier in [('WE MAKE',250,'slogan-we-make'), ('NOISE',348,'slogan-noise')]:
    size = 217 / width(value)
    text(bridge['top'], value, 202, baseline, size, 'ink', 430, 390, identifier)

# The rear tower carries two vertical performances and an inhabited date roof.
tower = block('high-letter-tower', 0, 110, 0, 120, 190, 620, 'green', 'blue', 'ink')
text(tower['front'], 'RINA VEIL', 96, 350, 80, 'yellow', 110, 430, 'artist-rina-veil', rotate=True)
text(tower['side'], 'LAGO', 113, 243, 105, 'yellow', 120, 430, 'artist-lago', rotate=True)
text(tower['top'], '17.07', 6, 88, 47.5, 'ink', 110, 120, 'date')

# A lower, wider counterweight is offset to the right rather than nested centrally.
right = block('wide-blue-stage', 210, 430, 0, 150, 190, 430, 'ink', 'blue', 'red')
name_size = 206 / max(width('MOTIF'), width('CLUB'))
right['front'].set('aria-label', 'MOTIF CLUB')
text(right['front'], 'MOTIF', 7, 112, name_size, 'yellow', 220, 240, 'artist-motif')
text(right['front'], 'CLUB', 7, 112 + name_size * cap + 16, name_size, 'yellow', 220, 240, 'artist-club')
open_size = 206 / width('OPEN AIR')
text(right['top'], 'OPEN AIR', 7, 112, open_size, 'yellow', 220, 150, 'venue-type')

# The low left stage meets the front bridge edge exactly; its roof is an unlettered red plane.
left = block('low-green-stage', 0, 170, 250, 390, 190, 325, 'red', 'green', 'blue')
left['front'].set('aria-label', 'NEON PALMS')
name_size = 158 / max(width('NEON'), width('PALMS'))
text(left['front'], 'NEON', 6, 53, name_size, 'ink', 170, 135, 'artist-neon')
text(left['front'], 'PALMS', 6, 117, name_size, 'ink', 170, 135, 'artist-palms')

OUT.mkdir(exist_ok=True)
raw = OUT / 'raw.svg'
ET.indent(root, space='  ')
raw.write_text('<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root, encoding='unicode') + '\n')
subprocess.run([sys.executable, str(ROOT/'input-v4/embed_fonts.py'), str(ROOT/'input-v4/fonts'),
                str(raw), str(OUT/'poster.svg')], check=True)

# Required-content and native-format checks, without making rendering claims.
final = ET.parse(OUT/'poster.svg').getroot()
texts = [''.join(e.itertext()) for e in final.iter(tag('text'))]
expected = ['KONBIN', 'STAGE', 'WE MAKE', 'NOISE', 'RINA VEIL', 'LAGO', '17.07',
            'MOTIF', 'CLUB', 'OPEN AIR', 'NEON', 'PALMS']
assert texts == expected, texts
assert final.attrib['viewBox'] == '0 0 900 1200'
assert final.attrib['width'] == '900' and final.attrib['height'] == '1200'
assert not list(final.iter(tag('image')))
assert not list(final.iter(tag('path')))
styles = ''.join(e.text or '' for e in final.iter(tag('style')))
assert '@font-face' in styles and 'data:font/woff2;base64,' in styles
assert 'Study Condensed' in styles
assert 'clipPath' not in (OUT/'poster.svg').read_text()
print(json.dumps(dict(xml='valid', dimensions='900 × 1200', editable_text_nodes=len(texts),
                      native_polygons=len(list(final.iter(tag('polygon')))),
                      embedded_font='Study Condensed 700', fixed_text=texts,
                      face_bounds_checks=len(audit)), ensure_ascii=False, indent=2))
