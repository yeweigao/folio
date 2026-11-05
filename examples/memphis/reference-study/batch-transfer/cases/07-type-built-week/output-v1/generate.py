#!/usr/bin/env python3
"""Independent native-SVG composition. Fonts remain editable text."""
from pathlib import Path
from html import escape
import json
import subprocess
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'output-v1'
PAPER = '#F6F0E5'
INK = '#1C1A1B'
GREEN = '#005B32'
BLUE = '#258CB4'
PURPLE = '#554699'
YELLOW = '#FDC442'
PINK = '#F5AAA4'
ORANGE = '#FF5205'
font = TTFont(ROOT / 'input/fonts/Inter-900.ttf')
cmap = font.getBestCmap()
units = font['head'].unitsPerEm
cap = font['OS/2'].sCapHeight / units
advance = lambda ch: font['hmtx'][cmap[ord(ch)]][0] / units

parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1200" viewBox="0 0 900 1200" role="img" aria-labelledby="poster-title poster-description">
<title id="poster-title">Taipei Design Week 2027</title>
<desc id="poster-description">Taipei Design Week. October 4–10, 2027. Architecture, craft, food, music, and public space. Hosted by City Design Museum with Open City Lab. TAIPEIDESIGNWEEK.EXAMPLE.</desc>
<!-- FONTS -->
<rect width="900" height="1200" fill="{PAPER}"/>
<g fill="{INK}" font-family="Study Sans, sans-serif" style="font-kerning:none;font-feature-settings:'kern' 0">''']
metrics = {}

def title_line(word, top, height, ident):
    size = height / cap
    glyphs = [font['glyf'][cmap[ord(c)]] for c in word]
    left = glyphs[0].xMin / units
    right = sum(advance(c) for c in word[:-1]) + glyphs[-1].xMax / units
    sx = 840 / ((right-left)*size)
    x = 30 - left*size*sx
    baseline = top + height
    transform = f'translate({x:.5f} {baseline:.5f}) scale({sx:.8f} 1)'
    attrs = f'font-size="{size:.6f}" font-weight="900" transform="{transform}"'
    parts.append(f'<text id="{ident}" {attrs}>{word}</text>')
    chars=[]
    pen=0
    for ch,glyph in zip(word,glyphs):
        chars.append(dict(char=ch, left=x+(pen+glyph.xMin/units)*size*sx,
            right=x+(pen+glyph.xMax/units)*size*sx,
            top=baseline-glyph.yMax/units*size,
            bottom=baseline-glyph.yMin/units*size,
            stem_left=x+(pen+0.046875)*size*sx,
            stem_right=x+(pen+0.244140625)*size*sx))
        pen += advance(ch)
    metrics[ident] = dict(word=word,attrs=attrs,chars=chars,top=top,bottom=baseline,height=height)
    return metrics[ident]

# Black typographic walls; every title remains a complete, editable text node.
a = title_line('TAIPEI', 30, 210, 'city')
b = title_line('DESIGN', 256, 210, 'theme')
c = title_line('WEEK', 482, 210, 'event')
d = title_line('2027', 708, 210, 'year')
parts.append('</g>')

# A diagonal two-color division is confined to the A's live glyph.
# The shape does not obscure either the counter or the crossbar.
ac = a['chars'][1]
ax, ar = ac['left'], ac['right']
ay, ab = ac['top'], ac['bottom']
parts.append(f'''<defs>
<clipPath id="city-glyphs"><text font-family="Study Sans, sans-serif" {a['attrs']} style="font-kerning:none">TAIPEI</text></clipPath>
<clipPath id="theme-glyphs"><text font-family="Study Sans, sans-serif" {b['attrs']} style="font-kerning:none">DESIGN</text></clipPath>
</defs>
<g clip-path="url(#city-glyphs)">
<rect x="{ax:.4f}" y="{ay:.4f}" width="{ar-ax:.4f}" height="{ab-ay:.4f}" fill="{GREEN}"/>
<path d="M {ax:.4f} {ab:.4f} L {ar:.4f} {ay:.4f} L {ar:.4f} {ab:.4f} Z" fill="{PURPLE}"/>
</g>''')

# Three parallel bars replace the E's horizontal structure. Its live ink stem
# and all remaining letters stay visible, keeping DESIGN unmistakable.
ec = b['chars'][1]
el, er = ec['left'], ec['right']
et, eb = ec['top'], ec['bottom']
bar_h = 45.5
# The colored bars are clipped to the live E, retaining its exact contours.
parts.append(f'<g clip-path="url(#theme-glyphs)">')
for y, color in [(et,PURPLE), (et+(eb-et-bar_h)/2,ORANGE), (eb-bar_h,BLUE)]:
    parts.append(f'<rect x="{el+31:.4f}" y="{y:.4f}" width="{er-el-31:.4f}" height="{bar_h:.4f}" fill="{color}"/>')
parts.append('</g>')

# A proportion-preserving native circle substitutes for the round zero.
# Its cap-scale diameter is independent of the display text's width scaling.
zero = d['chars'][1]
zcx = (zero['left']+zero['right'])/2
zcy = (d['top']+d['bottom'])/2
zr = 105
parts.append(f'<rect x="{zero["left"]-1:.5f}" y="{zero["top"]-1:.5f}" width="{zero["right"]-zero["left"]+2:.5f}" height="{zero["bottom"]-zero["top"]+2:.5f}" fill="{PAPER}"/>')
parts.append(f'<circle cx="{zcx:.5f}" cy="{zcy:.5f}" r="{zr}" fill="{ORANGE}"/>')

# The whitespace left below the four walls is the reading-sized fact field.
parts.append(f'<g fill="{INK}" font-family="Study Sans, sans-serif">')
for item,y in [('ARCHITECTURE',994),('CRAFT',1029),('FOOD',1064),('MUSIC',1099),('PUBLIC SPACE',1134)]:
    parts.append(f'<text x="30" y="{y}" font-size="23" font-weight="400">{escape(item)}</text>')
parts.append('''<text x="380" y="998" font-size="36" font-weight="900">OCTOBER 4–10</text>
<text x="380" y="1041" font-size="22" font-weight="700">TAIPEIDESIGNWEEK.EXAMPLE</text>
<text x="380" y="1112" font-size="23" font-weight="400">City Design Museum</text>
<text x="380" y="1146" font-size="23" font-weight="400">Open City Lab</text>
</g>
</svg>''')

OUT.mkdir(parents=True,exist_ok=True)
(OUT/'raw.svg').write_text('\n'.join(parts))
subprocess.run(['/private/tmp/folio-memphis-tools/bin/python',str(ROOT/'input/embed_fonts.py'),str(ROOT/'input/fonts'),str(OUT/'raw.svg'),str(OUT/'poster.svg')],check=True)
(OUT/'layout-metrics.json').write_text(json.dumps(metrics,ensure_ascii=False,indent=2))
print('Created 900 × 1200 native SVG.')
