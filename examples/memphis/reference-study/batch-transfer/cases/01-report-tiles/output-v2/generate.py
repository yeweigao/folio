#!/usr/bin/env python3
"""Native report composition, drawn only from the supplied written design."""
from pathlib import Path
from math import pi, sin, cos, sqrt
from html import escape
import subprocess
import sys

HERE = Path(__file__).resolve().parent
CASE = HERE.parent
W, H = 1280, 720
S = H / 1000
U = 180
C = dict(blue='#343D9F', pink='#FA0056', orange='#FF7619',
         paper='#F8F6ED', cream='#FFE5A6', ink='#111118')


def n(v):
    return f'{v:.4f}'.rstrip('0').rstrip('.')


def xy(p):
    return ' '.join(n(v) for v in p)


def rounded_radial(count, outer, valley, outer_handle, valley_handle, phase):
    """Alternating radial extrema with continuous, circularly tangent shoulders."""
    anchors, handles = [], []
    for i in range(count * 2):
        a = phase + i * pi / count
        r = outer if i % 2 == 0 else valley
        anchors.append((.5 + r * cos(a), .5 + r * sin(a)))
        handles.append((outer_handle if i % 2 == 0 else valley_handle,
                        -sin(a), cos(a)))
    path = ['M ' + xy(anchors[0])]
    for i in range(len(anchors)):
        j = (i + 1) % len(anchors)
        a, b = anchors[i], anchors[j]
        ah, ax, ay = handles[i]
        bh, bx, by = handles[j]
        path.append('C ' + xy((a[0] + ah * ax, a[1] + ah * ay)) + ' ' +
                    xy((b[0] - bh * bx, b[1] - bh * by)) + ' ' + xy(b))
    return ' '.join(path) + ' Z'


def diagonal_x():
    # Exact union outline of two 0.92 x 0.28 capsules at +45 and -45 degrees.
    c, d = .32 / sqrt(2), .14 / sqrt(2)
    a, b, q = c - d, c + d, .14 * sqrt(2)
    points = [(a, -b), (b, -a), (q, 0), (b, a), (a, b), (0, q),
              (-a, b), (-b, a), (-q, 0), (-b, -a), (-a, -b), (0, -q)]
    points = [(x + .5, y + .5) for x, y in points]
    path = ['M ' + xy(points[0])]
    for i in range(1, len(points)):
        path.append(('A .14 .14 0 0 1 ' if i in (1, 4, 7, 10) else 'L ') + xy(points[i]))
    return ' '.join(path) + ' Z'


SHAPES = {
    'six-petals': rounded_radial(6, .43, .20, .13, .04, -pi/2),
    'eight-petals': rounded_radial(8, .45, .28, .09, .04, -pi/2),
    'sixteen-petals': rounded_radial(16, .46, .39, .037, .025, -pi/2),
    'diagonal-x': diagonal_x(),
    'fold': 'M 0 0 H .32 V .5 A .18 .18 0 0 0 .5 .68 H 1 V 1 H .5 A .5 .5 0 0 1 0 .5 Z',
    'square-leaf': 'M .16 .16 H .56 A .28 .28 0 0 1 .84 .44 V .84 H .44 A .28 .28 0 0 1 .16 .56 Z',
    'quarter-ring': 'M 0 1 A 1 1 0 0 0 1 0 H .52 A .52 .52 0 0 1 0 .52 Z',
}


def tile(col, row, name, bg, fg, rotation=0):
    x, y = 920 + col * U, row * U
    out = [f'<g id="tile-{row+1}-{col+1}" transform="translate({x} {y})">',
           f'<rect width="180" height="180" fill="{C[bg]}"/>',
           f'<g transform="scale(180) rotate({rotation} .5 .5)" fill="{C[fg]}">']
    if name == 'four-circles':
        for cy in (.25, .75):
            for cx in (.25, .75):
                out.append(f'<circle cx="{cx}" cy="{cy}" r=".24"/>')
    else:
        out.append(f'<path d="{SHAPES[name]}"/>')
    return '\n'.join(out + ['</g>', '</g>'])


def text(content, x, y, size, weight=400, family='Study Sans', extra=''):
    return (f'<text x="{n(x)}" y="{n(y)}" font-family="{family}" '
            f'font-size="{n(size)}" font-weight="{weight}" {extra}>'
            f'{escape(content)}</text>')


def paragraph(lines, x, y):
    # Spaces retained across editable tspans preserve the exact supplied sentence.
    tspans = []
    for i, line in enumerate(lines):
        suffix = ' ' if i < len(lines)-1 else ''
        tspans.append(f'<tspan x="{x}" y="{n(y+i*24*S*1.4)}">{escape(line+suffix)}</tspan>')
    return (f'<text font-family="Study Sans" font-size="{n(24*S)}" font-weight="400" '
            'xml:space="preserve">' + ''.join(tspans) + '</text>')


parts = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" '
         'viewBox="0 0 1280 720" role="img" aria-labelledby="poster-title poster-description">',
         '<title id="poster-title">Eksplorasi Ruang Kota</title>',
         '<desc id="poster-description">Laporan Proyek Komunikasi Visual. Nadia Putri, Studio Sekolah, 2027.</desc>',
         '<!-- FONTS -->',
         f'<rect width="1280" height="720" fill="{C["blue"]}"/>',
         '<g id="continuous-tile-field" aria-hidden="true">',
         tile(0, 0, 'fold', 'orange', 'blue'),
         tile(1, 0, 'six-petals', 'blue', 'cream'),
         tile(0, 1, 'square-leaf', 'pink', 'cream', 90),
         tile(1, 1, 'diagonal-x', 'cream', 'blue'),
         tile(0, 2, 'four-circles', 'paper', 'pink'),
         tile(1, 2, 'quarter-ring', 'blue', 'orange', 180),
         tile(0, 3, 'sixteen-petals', 'pink', 'cream'),
         tile(1, 3, 'eight-petals', 'cream', 'blue'),
         '</g>',
         f'<g id="report-reading-field" fill="{C["paper"]}">',
         text('Laporan Proyek Komunikasi Visual', 52, 65, 34*S, 700),
         text('2027', 866, 65, 22*S, extra='text-anchor="end"'),
         '<g id="theme-title">',
         # Font-outline bearings place both visible title edges at x = 52.
         text('Eksplorasi', 42.40384, 188, 136*S, 100, 'Study Light',
              'style="font-variation-settings: &quot;wght&quot; 100, &quot;wdth&quot; 100"'),
         text('Ruang Kota', 47.41, 285.92, 136*S, 900),
         '</g>',
         '<g id="observasi">',
         text('Observasi', 50.7, 391, 34*S, 700),
         paragraph(['Mengamati tanda, warna, dan kebiasaan di',
                    'ruang publik sebagai dasar sistem',
                    'komunikasi visual.'], 52, 433),
         '</g>',
         '<g id="eksperimen">',
         text('Eksperimen', 485, 391, 34*S, 700),
         paragraph(['Menguji bentuk dan bahasa visual melalui',
                    'prototipe yang dekat dengan kehidupan',
                    'sehari-hari.'], 486, 433),
         '</g>',
         '<g id="report-credits">',
         text('Nadia Putri', 52, 656, 24*S),
         text('Studio Sekolah', 486, 656, 24*S),
         '</g>',
         '</g>',
         '</svg>']

raw = HERE / 'raw.svg'
raw.write_text('\n'.join(parts) + '\n')
subprocess.run([sys.executable, str(CASE/'input-v2/embed_fonts.py'),
                str(CASE/'input-v2/fonts'), str(raw), str(HERE/'poster.svg')], check=True)
print(raw)
