#!/usr/bin/env python3
"""Draw this report page as editable text and native SVG geometry."""
from pathlib import Path
from math import sin, cos, pi
from html import escape
import subprocess
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.boundsPen import BoundsPen

HERE = Path(__file__).resolve().parent
INPUT = HERE.parent / 'input'
C = dict(paper='#F8F6ED', blue='#343D9F', pink='#FA0056',
         orange='#FF7619', cream='#FFE5A6')

def font(file, weight=None):
    f = TTFont(INPUT / 'fonts' / file)
    return instantiateVariableFont(f, {'wght': weight}, inplace=True) if weight else f

regular = font('Inter-400.ttf')
light = font('Archivo-variable.ttf', 100)
heavy = font('Inter-900.ttf')

def advance(text, f, size):
    cmap = f.getBestCmap()
    return sum(f['hmtx'].metrics[cmap[ord(c)]][0] for c in text) * size / f['head'].unitsPerEm

def ink_x(left, text, f, size):
    gs = f.getGlyphSet()
    pen = BoundsPen(gs)
    gs[f.getBestCmap()[ord(text[0])]].draw(pen)
    return left - pen.bounds[0] * size / f['head'].unitsPerEm

def wrap(text, width, size=20):
    lines = []
    for word in text.split():
        candidate = (lines[-1] + ' ' + word) if lines else word
        if lines and advance(candidate, regular, size) > width:
            lines.append(word)
        elif lines:
            lines[-1] = candidate
        else:
            lines.append(word)
    return lines

svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720" role="img" aria-labelledby="title desc">',
       '<title id="title">Eksplorasi Ruang Kota — Laporan Proyek Komunikasi Visual</title>',
       '<desc id="desc">A visual communication report by Nadia Putri, Studio Sekolah, 2027. Two study groups appear beside a two-column field of eight geometric tiles.</desc>',
       '<!-- FONTS -->',
       f'<rect width="1280" height="720" fill="{C["blue"]}"/>']

def text(txt, x, y, size, weight=400, family='Study Sans', spacing=None):
    attrs = f'x="{x:.3f}" y="{y}" font-family="{family}, sans-serif" font-size="{size}" font-weight="{weight}" fill="{C["paper"]}"'
    if spacing is not None:
        attrs += f' letter-spacing="{spacing}"'
    svg.append(f'<text {attrs}>{escape(txt)}</text>')

# The report has one reading axis. The light and heavy title inks share it.
text('Laporan Proyek Komunikasi Visual', 52, 64, 23)
text('Eksplorasi', ink_x(52, 'Eksplorasi', light, 110), 210, 110,
     100, 'Study Light', -2.5)
text('Ruang Kota', ink_x(52, 'Ruang Kota', heavy, 112), 326, 112,
     900, 'Study Sans', -4)

groups = [
    ('Observasi', 'Mengamati tanda, warna, dan kebiasaan di ruang publik sebagai dasar sistem komunikasi visual.', 52),
    ('Eksperimen', 'Menguji bentuk dan bahasa visual melalui prototipe yang dekat dengan kehidupan sehari-hari.', 480),
]
for heading, body, x in groups:
    text(heading, x, 430, 32, 700)
    lines = wrap(body, 370)
    svg.append(f'<text x="{x}" y="470" font-family="Study Sans, sans-serif" font-size="20" font-weight="400" fill="{C["paper"]}">')
    for i, line in enumerate(lines):
        svg.append(f'<tspan x="{x}" dy="{0 if i == 0 else 28}">{escape(line)}</tspan>')
    svg.append('</text>')

text('Nadia Putri', 52, 650, 26, 700)
text('Studio Sekolah', 52, 681, 20)
year = '2027'
text(year, 868 - advance(year, light, 76), 681, 76, 100, 'Study Light', -2)

# Closed, smooth polar contours: six broad petals and eight soft points.
def polar_curve(lobes, base, amplitude, phase=0, segments=96):
    def point(t):
        r = base + amplitude * cos(lobes * t + phase)
        dr = -amplitude * lobes * sin(lobes * t + phase)
        return (90 + r*cos(t), 90 + r*sin(t),
                dr*cos(t)-r*sin(t), dr*sin(t)+r*cos(t))
    dt = 2*pi/segments
    p = point(0)
    parts = [f'M{p[0]:.4f},{p[1]:.4f}']
    for i in range(segments):
        a, b = point(i*dt), point((i+1)*dt)
        parts.append(f'C{a[0]+a[2]*dt/3:.4f},{a[1]+a[3]*dt/3:.4f} '
                     f'{b[0]-b[2]*dt/3:.4f},{b[1]-b[3]*dt/3:.4f} '
                     f'{b[0]:.4f},{b[1]:.4f}')
    return ' '.join(parts) + ' Z'

def gear(teeth=24):
    pts = []
    for tooth in range(teeth):
        for fraction, radius in [(0, 77), (.18, 90), (.55, 90), (.73, 77)]:
            t = (tooth + fraction)*2*pi/teeth - pi/2
            pts.append((90+radius*cos(t), 90+radius*sin(t)))
    return 'M' + ' L'.join(f'{x:.4f},{y:.4f}' for x,y in pts) + ' Z'

motifs = [
    ('six-petal flower', 'cream', 'blue', f'<path d="{polar_curve(6, 66, 24)}"/>'),
    ('eight-point soft star', 'pink', 'cream', f'<path d="{polar_curve(8, 62, 28)}"/>'),
    ('cross', 'orange', 'blue', '<path d="M60 0H120V60H180V120H120V180H60V120H0V60H60Z"/>'),
    ('four circles', 'paper', 'pink', ''.join(f'<circle cx="{x}" cy="{y}" r="45"/>' for y in (45,135) for x in (45,135))),
    ('dense-toothed circle', 'pink', 'cream', f'<path d="{gear()}"/>'),
    ('rounded folded block', 'blue', 'orange', '<path d="M0 0H120Q180 0 180 60V180H120V80Q120 60 100 60H0Z"/>'),
    ('leaf block', 'cream', 'blue', '<path d="M0 180C0 80 80 0 180 0C180 100 100 180 0 180Z"/>'),
    ('quarter ring', 'orange', 'pink', '<path d="M180 0A180 180 0 0 1 0 180V108A108 108 0 0 0 108 0Z"/>'),
]

svg.append('<g aria-label="Geometric tile field">')
for i, (name, bg, fg, drawing) in enumerate(motifs):
    x, y = 920 + (i % 2)*180, (i // 2)*180
    svg.append(f'<g transform="translate({x} {y})" fill="{C[fg]}" aria-label="{name}">')
    svg.append(f'<rect width="180" height="180" fill="{C[bg]}"/>')
    svg.append(drawing)
    svg.append('</g>')
svg.append('</g></svg>')

raw = HERE / 'raw.svg'
raw.write_text('\n'.join(svg), encoding='utf-8')
subprocess.run(['/private/tmp/folio-memphis-tools/bin/python', str(INPUT/'embed_fonts.py'),
                str(INPUT/'fonts'), str(raw), str(HERE/'poster.svg')], check=True)
