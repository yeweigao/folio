#!/usr/bin/env python3
"""Build one editable street-collage poster from this case's isolated inputs."""
from pathlib import Path
import math
import subprocess
import sys
import xml.etree.ElementTree as ET
from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen

BASE = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent
FONTS = BASE / 'input-v3' / 'fonts'
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)
W, H, U = 900, 1200, 150
C = {
    'paper': '#EAE8E6', 'ink': '#19191D', 'blue': '#008BCD',
    'green': '#087C4A', 'pink': '#F68CBC', 'yellow': '#FFDE00',
    'red': '#F52B20', 'purple': '#76258D',
}
root = ET.Element(f'{{{NS}}}svg', {
    'width': str(W), 'height': str(H), 'viewBox': '0 0 900 1200',
    'version': '1.1', 'role': 'img', 'aria-labelledby': 'poster-title poster-desc',
})

def el(name, attrs=None, parent=None, text=None):
    node = ET.SubElement(root if parent is None else parent, f'{{{NS}}}{name}',
                         {k.replace('_', '-'): str(v) for k, v in (attrs or {}).items()})
    if text is not None:
        node.text = text
    return node

el('title', {'id': 'poster-title'}, text='集合散步 — CITY WALKS')
el('desc', {'id': 'poster-desc'}, text='在城里发现。Small discoveries, shared streets. 2027.05.14–05.16，河岸街区。一起走进街角的日常。')
metadata = el('metadata')
for license_file in ['Inter-OFL.txt', 'Noto-OFL.txt']:
    el('license', {'source': f'input-v3/fonts/{license_file}'}, metadata,
       (FONTS / license_file).read_text())
defs = el('defs')
root.append(ET.Comment(' FONTS '))


def group(label, **attrs):
    return el('g', {'id': label, **attrs})


def rect(parent, x, y, width, height, color):
    return el('rect', {'x': x, 'y': y, 'width': width, 'height': height,
                       'fill': C.get(color, color)}, parent)


def path(parent, d, color, **attrs):
    return el('path', {'d': d, 'fill': C.get(color, color), **attrs}, parent)


def clip_box(label, x, y, width, height):
    cp = el('clipPath', {'id': label}, defs)
    rect(cp, x, y, width, height, 'paper')
    return f'url(#{label})'


def circle(parent, x, y, diameter, color):
    return el('circle', {'cx': x, 'cy': y, 'r': diameter / 2,
                         'fill': C[color]}, parent)


def window_grid(label, x, y, width, height):
    g = group(label, clip_path=clip_box(label + '-clip', x, y, width, height))
    rect(g, x, y, width, height, 'paper')
    for i in range(int(width / (U / 4)) + 1):
        el('line', {'x1': x + i * U / 4, 'y1': y,
                    'x2': x + i * U / 4, 'y2': y + height,
                    'stroke': C['ink'], 'stroke-width': U * .045}, g)
    for i in range(int(height / (U / 4)) + 1):
        el('line', {'x1': x, 'y1': y + i * U / 4,
                    'x2': x + width, 'y2': y + i * U / 4,
                    'stroke': C['ink'], 'stroke-width': U * .045}, g)


def stripes(label, x, y, width, height, direction, background, foreground):
    g = group(label, clip_path=clip_box(label + '-clip', x, y, width, height))
    rect(g, x, y, width, height, background)
    if direction in ('vertical', 'horizontal'):
        breadth = U * .10
        extent = width if direction == 'vertical' else height
        for k in range(math.ceil(extent / (breadth * 2))):
            if direction == 'vertical':
                rect(g, x + k * breadth * 2, y, breadth, height, foreground)
            else:
                rect(g, x, y + k * breadth * 2, width, breadth, foreground)
    else:
        # x-y is constant along each 45-degree stripe. Its projected width
        # is sqrt(2) times the specified perpendicular width of 0.12u.
        breadth = U * .12 * math.sqrt(2)
        lower, upper = x - (y + height), x + width - y
        k0 = math.floor(lower / (breadth * 2)) - 1
        k1 = math.ceil(upper / (breadth * 2)) + 1
        for k in range(k0, k1):
            t = k * breadth * 2
            path(g, f'M {t + y:g} {y:g} L {t + y + breadth:g} {y:g} '
                    f'L {t + y + height + breadth:g} {y + height:g} '
                    f'L {t + y + height:g} {y + height:g} Z', foreground)


def chevrons(label, x, y, background, foreground):
    # The 90-degree bend, 0.22u perpendicular arm width and 0.70u height
    # determine the width of a pair of straight, square-cut 45-degree arms.
    g = group(label)
    rect(g, x, y, 2 * U, U, background)
    oh, arm = U * .70, U * .22
    end_projection = arm / math.sqrt(2)
    ow = oh / 2 + end_projection
    run = oh / 2 - end_projection
    for dx in (39, 180):
        xx, yy = x + dx, y + (U - oh) / 2
        path(g, f'M {xx + end_projection:g} {yy:g} '
                f'L {xx + ow:g} {yy + oh/2:g} '
                f'L {xx + end_projection:g} {yy + oh:g} '
                f'L {xx:g} {yy + oh - end_projection:g} '
                f'L {xx + run:g} {yy + oh/2:g} '
                f'L {xx:g} {yy + end_projection:g} Z', foreground)


def concave(label, x, y, background, foreground):
    g = group(label)
    rect(g, x, y, U, U, background)
    path(g, f'M {x + U/2:g} {y:g} '
            f'A {U/2:g} {U/2:g} 0 0 0 {x + U:g} {y + U/2:g} '
            f'A {U/2:g} {U/2:g} 0 0 0 {x + U/2:g} {y + U:g} '
            f'A {U/2:g} {U/2:g} 0 0 0 {x:g} {y + U/2:g} '
            f'A {U/2:g} {U/2:g} 0 0 0 {x + U/2:g} {y:g} Z', foreground)

# Upper edge: a bisected semicircle, a stripe brick, and an arrow street.
g = group('split-upper-semicircle')
rect(g, 0, 0, 150, 150, 'blue')
rect(g, 150, 0, 150, 150, 'purple')
path(g, 'M 0 150 A 150 150 0 0 1 150 0 L 150 150 Z', 'yellow')
path(g, 'M 150 0 A 150 150 0 0 1 300 150 L 150 150 Z', 'pink')
stripes('upper-vertical-stripes', 300, 0, 150, 150, 'vertical', 'paper', 'ink')
chevrons('upper-arrow-street', 450, 0, 'pink', 'ink')
concave('upper-concave-star', 750, 0, 'blue', 'yellow')

# Main title district and the neighboring circle across one color boundary.
g = group('main-reading-district')
rect(g, 0, 150, 450, 450, 'paper')
g = group('circle-across-boundary')
rect(g, 450, 150, 300, 300, 'green')
rect(g, 750, 150, 150, 300, 'red')
circle(g, 750, 300, 300, 'paper')
g = group('diamond-brick')
rect(g, 450, 450, 150, 150, 'purple')
path(g, 'M 525 453 L 597 525 L 525 597 L 453 525 Z', 'yellow')
window_grid('middle-window-street', 600, 450, 300, 150)

# The middle cross-street changes rhythm and direction at each brick.
stripes('red-yellow-diagonal-street', 0, 600, 300, 150, 'diagonal', 'red', 'yellow')
g = group('ring-brick')
rect(g, 300, 600, 150, 150, 'blue')
el('circle', {'cx': 375, 'cy': 675, 'r': 61.5, 'fill': 'none',
              'stroke': C['pink'], 'stroke-width': 27}, g)
g = group('semicircle-brick')
rect(g, 450, 600, 150, 150, 'yellow')
path(g, 'M 450 675 A 75 75 0 0 1 600 675 Z', 'ink')
stripes('purple-horizontal-street', 600, 600, 300, 150, 'horizontal', 'purple', 'paper')

# Lower streets turn toward the second reading district.
concave('lower-concave-star', 0, 750, 'pink', 'ink')
chevrons('lower-arrow-street', 150, 750, 'green', 'yellow')
window_grid('lower-window-district', 0, 900, 300, 300)
g = group('split-lower-curve')
rect(g, 300, 900, 150, 150, 'red')
rect(g, 300, 1050, 150, 150, 'purple')
path(g, 'M 450 900 A 150 150 0 0 0 300 1050 L 450 1050 Z', 'pink')
path(g, 'M 300 1050 A 150 150 0 0 0 450 1200 L 450 1050 Z', 'green')
g = group('second-reading-district')
rect(g, 450, 750, 450, 450, 'yellow')

# Native text. Positions align visible ink rather than font advance boxes.
font_cache = {}
text_boxes = []

def metrics(content, size, family, weight):
    filename = 'NotoSansSC-variable.ttf' if family == 'Study CJK' else f'Inter-{weight}.ttf'
    if filename not in font_cache:
        font_cache[filename] = TTFont(FONTS / filename)
    font = font_cache[filename]
    location = {'wght': weight} if 'fvar' in font else None
    glyphs = font.getGlyphSet(location=location)
    cmap = font.getBestCmap()
    advance, bounds = 0, []
    for char in content:
        glyph = glyphs[cmap[ord(char)]]
        pen = BoundsPen(glyphs)
        glyph.draw(pen)
        if pen.bounds:
            x0, y0, x1, y1 = pen.bounds
            bounds.append((x0 + advance, y0, x1 + advance, y1))
        advance += glyph.width
    factor = size / font['head'].unitsPerEm
    return tuple(value * factor for value in (
        min(b[0] for b in bounds), min(b[1] for b in bounds),
        max(b[2] for b in bounds), max(b[3] for b in bounds)))


def text_lines(label, lines, size, family, weight, district):
    node = el('text', {'id': label, 'font-family': family,
                      'font-size': size, 'font-weight': weight,
                      'fill': C['ink'], 'xml:space': 'preserve'})
    for content, left, top in lines:
        x0, y0, x1, y1 = metrics(content, size, family, weight)
        xx, baseline = left - x0, top + y1
        el('tspan', {'x': f'{xx:.4f}', 'y': f'{baseline:.4f}'}, node, content)
        bounds = (left, top, left + x1 - x0, top + y1 - y0)
        text_boxes.append((label, content, bounds, district))
    return node

text_lines('main-title', [('集合散步', 26, 187)], 99, 'Study CJK', 900, (0, 150, 450, 600))
text_lines('light-subtitle', [('在城里', 26, 294), ('发现', 26, 393)],
           93.6, 'Study CJK', 300, (0, 150, 450, 600))
text_lines('english-title', [('CITY WALKS', 26, 535)],
           37.8, 'Study Sans', 900, (0, 150, 450, 600))
text_lines('english-description', [('Small discoveries, ', 476, 790), ('shared streets.', 476, 843)],
           37.8, 'Study Sans', 400, (450, 750, 900, 1200))
text_lines('date', [('2027.05.14–05.16', 476, 956)],
           23.4, 'Study Sans', 700, (450, 750, 900, 1200))
text_lines('location', [('河岸街区', 476, 1001)],
           23.4, 'Study CJK', 700, (450, 750, 900, 1200))
text_lines('activity-description', [('一起走进街角的日常', 476, 1110)],
           23.4, 'Study CJK', 400, (450, 750, 900, 1200))

# Verify all seven required strings while preserving their editable text.
expected = {
    'main-title': '集合散步', 'light-subtitle': '在城里发现',
    'english-title': 'CITY WALKS',
    'english-description': 'Small discoveries, shared streets.',
    'date': '2027.05.14–05.16', 'location': '河岸街区',
    'activity-description': '一起走进街角的日常',
}
for node in root.findall(f'{{{NS}}}text'):
    assert ''.join(node.itertext()) == expected[node.attrib['id']]
for label, content, (x0, y0, x1, y1), (dx0, dy0, dx1, dy1) in text_boxes:
    assert x0 >= dx0 + 23.4 and y0 >= dy0 + 23.4, (label, 'leading inset')
    assert x1 <= dx1 - 23.4 and y1 <= dy1 - 23.4, (label, 'trailing inset')
    print(f'{label}: {content.strip()} ink=({x0:.2f},{y0:.2f})–({x1:.2f},{y1:.2f})')

OUT.mkdir(parents=True, exist_ok=True)
raw = OUT / 'raw.svg'
ET.ElementTree(root).write(raw, encoding='utf-8', xml_declaration=True)
ET.parse(raw)
subprocess.run([sys.executable, str(BASE / 'input-v3' / 'embed_fonts.py'),
                str(FONTS), str(raw), str(OUT / 'poster.svg')], check=True)
embedded = ET.parse(OUT / 'poster.svg').getroot()
assert embedded.attrib['viewBox'] == '0 0 900 1200'
assert len(embedded.findall(f'{{{NS}}}text')) == 7
assert not embedded.findall(f'.//{{{NS}}}image')
assert 'data:font/woff2;base64,' in (OUT / 'poster.svg').read_text()
print('Verified XML, seven fixed text strings, ink insets, live text, and embedded fonts.')
