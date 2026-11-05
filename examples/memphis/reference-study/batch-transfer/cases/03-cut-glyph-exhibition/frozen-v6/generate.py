#!/usr/bin/env python3
"""Native SVG composition derived only from the frozen input-v6 brief."""
from pathlib import Path
from xml.sax.saxutils import escape
import json
import subprocess
import sys
import xml.etree.ElementTree as ET
from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen
from fontTools.varLib.instancer import instantiateVariableFont

HERE = Path(__file__).resolve().parent
CASE = HERE.parent
INPUT = CASE / 'input-v6'
C = {
    'green': '#07964F', 'ink': '#050505', 'paper': '#FFFFFF',
    'pink': '#F3579D', 'purple': '#9B38ED', 'orange': '#FF7829',
    'blue': '#0759FD', 'yellow': '#FFF035',
}
svg = []
def add(s):
    svg.append(s)
def path(name, d, color):
    add(f'<path id="{name}" d="{d}" fill="{C[color]}"/>')
def rect(name, x, y, w, h, color):
    add(f'<rect id="{name}" x="{x}" y="{y}" width="{w}" height="{h}" fill="{C[color]}"/>')
def circle(name, cx, cy, r, color):
    add(f'<circle id="{name}" cx="{cx}" cy="{cy}" r="{r}" fill="{C[color]}"/>')
def text(name, x, y, value, family, size, weight, color):
    add(f'<text id="{name}" x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{C[color]}" xml:space="preserve">{escape(value)}</text>')

add('<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1200" viewBox="0 0 900 1200" role="img" aria-labelledby="poster-title poster-description">')
add('<title id="poster-title">共生设计展 — COEXIST DESIGN EXHIBITION</title>')
add('<desc id="poster-description">共生主题的切割字形海报，绿色与黑色双场。左侧为连笔白色共、生构字；右侧以小拼块、日期切口、紫色弯钩和橙色双碗腰体组成另一组共生结构。</desc>')
add('<!-- FONTS -->')
add('<g id="continuous-color-fields">')
rect('green-field', 0, 0, 450, 1200, 'green')
rect('ink-field', 450, 0, 450, 1200, 'ink')
add('</g>')

# The left compound keeps the two upper posts and a shared bar of 共,
# then repeats the upright and three cross-strokes of 生 below the title cut.
add('<g id="continuous-coexist-glyphs" aria-label="共、生的连笔构字">')
path('gong-left-curved-shoulder', 'M105 24 H158 V250 H0 V129 A105 105 0 0 1 105 24 Z', 'paper')
path('gong-right-curved-shoulder', 'M292 24 H345 A105 105 0 0 1 450 129 V250 H292 Z', 'paper')
rect('gong-shared-crossbar', 0, 250, 450, 95, 'paper')
path('gong-left-arc-foot', 'M100 320 H205 V330 A150 150 0 0 1 55 480 H0 V375 H55 A45 45 0 0 0 100 330 Z', 'paper')
path('gong-right-arc-foot', 'M245 320 H350 V330 A45 45 0 0 0 395 375 H450 V480 H395 A150 150 0 0 1 245 330 Z', 'paper')
rect('continuous-left-spine', 0, 345, 60, 855, 'paper')
rect('sheng-central-upright', 200, 780, 100, 350, 'paper')
path('sheng-upper-curved-stroke', 'M30 970 A150 150 0 0 1 180 820 H450 V920 H180 A50 50 0 0 0 130 970 Z', 'paper')
rect('sheng-middle-crossbar', 60, 980, 390, 100, 'paper')
path('sheng-lower-curved-baseline', 'M0 1095 H345 A105 105 0 0 1 450 1200 H0 Z', 'paper')
add('</g>')

# Five columns by three levels: all cells meet the edge of the main shoulder.
add('<g id="segmented-glyph-cluster" aria-label="与主字连接的五列三层弧齿拼块">')
path('cluster-r1-c1', 'M470 24 H552 V106 A82 82 0 0 1 470 24 Z', 'pink')
path('cluster-r1-c2', 'M552 24 H634 V106 H593 A41 41 0 0 1 552 65 Z', 'blue')
path('cluster-r1-c3', 'M634 24 H716 A41 41 0 0 1 634 24 Z', 'paper')
rect('cluster-r1-c4-a', 730, 24, 12, 82, 'orange')
rect('cluster-r1-c4-b', 756, 24, 12, 82, 'orange')
rect('cluster-r1-c4-c', 782, 24, 12, 82, 'orange')
path('cluster-r1-c5', 'M798 24 H880 V65 A41 41 0 0 1 798 65 Z', 'pink')
path('cluster-r2-c1', 'M470 106 H511 A41 41 0 0 1 511 188 H470 Z', 'paper')
path('cluster-r2-c2', 'M552 106 H634 V188 A82 82 0 0 1 552 106 Z', 'orange')
path('cluster-r2-c3', 'M634 106 H716 V147 A41 41 0 0 1 634 147 Z', 'pink')
path('cluster-r2-c4', 'M716 106 H798 V188 A82 82 0 0 1 716 106 Z', 'blue')
circle('cluster-r2-c5-dot-a', 819, 127, 17, 'paper')
circle('cluster-r2-c5-dot-b', 859, 167, 17, 'paper')
path('cluster-r3-c1', 'M470 188 H552 V270 A82 82 0 0 1 470 188 Z', 'pink')
path('cluster-r3-c2', 'M552 188 H634 A41 41 0 0 1 552 188 Z', 'paper')
rect('cluster-r3-c3-a', 640, 188, 10, 54, 'paper')
rect('cluster-r3-c3-b', 660, 188, 10, 54, 'paper')
rect('cluster-r3-c3-c', 680, 188, 10, 54, 'paper')
rect('cluster-r3-c3-d', 700, 188, 10, 54, 'paper')
path('cluster-r3-c4', 'M716 188 H798 V270 A82 82 0 0 0 716 188 Z', 'orange')
path('cluster-r3-c5', 'M798 188 H880 V270 H798 Z', 'pink')
add('</g>')

# A right-facing cut is three-sided: the dates rest directly within the glyph.
add('<g id="pink-main-shoulder">')
path('pink-cut-bearing-shoulder', 'M450 242 H900 V540 H450 V500 H850 V325 H450 Z', 'pink')
add('</g>')

# Three distinct quarter-turn hooks, outer R126 / inner R52 / t74.
add('<g id="purple-parallel-hooks" aria-label="三根并列紫色弯钩">')
for i, x in enumerate((475, 597, 719), 1):
    d = (f'M{x} 518 H{x+100} V592 H{x+74} V733 '
         f'A52 52 0 0 0 {x+126} 785 V859 '
         f'A126 126 0 0 1 {x} 733 Z')
    path(f'purple-hook-{i}', d, 'purple')
add('</g>')

# The orange block narrows to a 128px waist and opens again around an ink hole.
add('<g id="orange-double-bowl" aria-label="带窄腰与内孔的橙色双碗体">')
path('orange-upper-bowl-waist-and-lower-bell', 'M470 870 H886 C886 934 817 995 742 995 V1035 C823 1035 886 1107 886 1200 H470 C470 1107 533 1035 614 1035 V995 C539 995 470 934 470 870 Z', 'orange')
add(f'<ellipse id="orange-horizontal-counter" cx="678" cy="1122" rx="51" ry="22" fill="{C["ink"]}"/>')
add('</g>')

add('<g id="editable-facts">')
# Slot 158..292: both full facts use a single editable text node.
text('curator', 170, 145, '策展：林岚', 'Study CJK', 21.6, 400, 'ink')
text('venue', 170, 218, '城市设计馆', 'Study CJK', 21.6, 400, 'ink')
# The title cut is continuous green, open toward the central field boundary.
text('exhibition-cjk', 77, 553, '共生设计展', 'Study CJK', 68.4, 900, 'yellow')
text('exhibition-en-line-1', 78, 627, 'COEXIST', 'Study Sans', 53.1, 900, 'ink')
text('exhibition-en-line-2', 78, 690, 'DESIGN', 'Study Sans', 53.1, 900, 'ink')
text('exhibition-en-line-3', 78, 753, 'EXHIBITION', 'Study Sans', 53.1, 900, 'ink')
text('date-start', 480, 370, '12 JUNE', 'Study Sans', 43.2, 700, 'paper')
text('date-end', 480, 427, '28 AUGUST', 'Study Sans', 43.2, 700, 'paper')
text('opening-hours', 480, 484, '09:00–18:00', 'Study Sans', 43.2, 700, 'paper')
add('</g>')
add('</svg>')
raw = HERE / 'raw.svg'
poster = HERE / 'poster.svg'
raw.write_text('\n'.join(svg) + '\n', encoding='utf-8')
subprocess.run([sys.executable, str(INPUT / 'embed_fonts.py'), str(INPUT / 'fonts'), str(raw), str(poster)], check=True)

# Inspect the actual font outlines, using baseline-space bounds.
font_cache = {}
def ink_bounds(filename, weight, value, size, x, baseline):
    key = filename, weight
    if key not in font_cache:
        f = TTFont(INPUT / 'fonts' / filename)
        if 'fvar' in f:
            f = instantiateVariableFont(f, {'wght': weight}, inplace=False)
        font_cache[key] = f
    f = font_cache[key]
    gs, cmap, hmtx = f.getGlyphSet(), f.getBestCmap(), f['hmtx'].metrics
    advance, boxes = 0, []
    for ch in value:
        gn = cmap[ord(ch)]
        p = BoundsPen(gs)
        gs[gn].draw(p)
        if p.bounds:
            a, b, c, d = p.bounds
            boxes.append((a+advance, b, c+advance, d))
        advance += hmtx[gn][0]
    s = size / f['head'].unitsPerEm
    return [round(x+min(b[0] for b in boxes)*s, 2),
            round(baseline-max(b[3] for b in boxes)*s, 2),
            round(x+max(b[2] for b in boxes)*s, 2),
            round(baseline-min(b[1] for b in boxes)*s, 2)]
checks = []
for name, value, fn, wt, sz, x, y, box in [
    ('curator', '策展：林岚', 'NotoSansSC-variable.ttf', 400, 21.6, 170, 145, (158,24,292,250)),
    ('venue', '城市设计馆', 'NotoSansSC-variable.ttf', 400, 21.6, 170, 218, (158,24,292,250)),
    ('title-cjk', '共生设计展', 'NotoSansSC-variable.ttf', 900, 68.4, 77, 553, (60,480,450,780)),
    ('title-latin-1', 'COEXIST', 'Inter-900.ttf', 900, 53.1, 78, 627, (60,480,450,780)),
    ('title-latin-2', 'DESIGN', 'Inter-900.ttf', 900, 53.1, 78, 690, (60,480,450,780)),
    ('title-latin-3', 'EXHIBITION', 'Inter-900.ttf', 900, 53.1, 78, 753, (60,480,450,780)),
    ('date-start', '12 JUNE', 'Inter-700.ttf', 700, 43.2, 480, 370, (450,325,850,500)),
    ('date-end', '28 AUGUST', 'Inter-700.ttf', 700, 43.2, 480, 427, (450,325,850,500)),
    ('time', '09:00–18:00', 'Inter-700.ttf', 700, 43.2, 480, 484, (450,325,850,500)),
]:
    b = ink_bounds(fn, wt, value, sz, x, y)
    clearances = [round(b[0]-box[0], 2), round(b[1]-box[1], 2), round(box[2]-b[2], 2), round(box[3]-b[3], 2)]
    assert min(clearances) >= 12, (name, b, clearances)
    checks.append({'id': name, 'ink_box': b, 'cut_clearances': clearances})

for file in (raw, poster):
    root = ET.fromstring(file.read_text(encoding='utf-8'))
    assert root.attrib['viewBox'] == '0 0 900 1200'
    assert root.attrib['width'] == '900' and root.attrib['height'] == '1200'
    ns = {'s': 'http://www.w3.org/2000/svg'}
    text_values = [''.join(n.itertext()) for n in root.findall('.//s:text', ns)]
    required = ['共生设计展', 'COEXIST', 'DESIGN', 'EXHIBITION', '12 JUNE', '28 AUGUST', '09:00–18:00', '城市设计馆', '策展：林岚']
    assert text_values == ['策展：林岚', '城市设计馆', '共生设计展', 'COEXIST', 'DESIGN', 'EXHIBITION', '12 JUNE', '28 AUGUST', '09:00–18:00']
    assert len(text_values) == 9
    assert all(s in text_values for s in required)
    assert not root.findall('.//s:image', ns)
assert poster.read_text(encoding='utf-8').count('data:font/woff2;base64,') == 4
print(json.dumps({'xml': 'valid', 'dimensions': [900,1200], 'fixed_text_nodes': 9, 'embedded_font_faces': 4, 'ink_measurements': checks}, ensure_ascii=False, indent=2))
