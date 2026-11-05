#!/usr/bin/env python3
"""Build an editable 900 × 1200 exhibition poster from the supplied v3 system."""
from pathlib import Path
import html
import subprocess
import sys
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
CASE = HERE.parent
C = {
    'green': '#07964F', 'ink': '#050505', 'paper': '#FFFFFF',
    'pink': '#F3579D', 'purple': '#9B38ED', 'orange': '#FF7829',
    'yellow': '#FFF035',
}
parts = []

def path(name, d, color, **attrs):
    attr = ' '.join(f'{k.replace("_", "-")}="{html.escape(str(v), quote=True)}"' for k, v in attrs.items())
    parts.append(f'<path id="{name}" d="{d}" fill="{C[color]}" {attr}/>')

def text(name, x, y, content, size, color, weight=400, family='Study Sans', **attrs):
    attr = ' '.join(f'{k.replace("_", "-")}="{html.escape(str(v), quote=True)}"' for k, v in attrs.items())
    parts.append(f'<text id="{name}" x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{C[color]}" {attr}>{html.escape(content)}</text>')

def main():
    license_inter = (CASE / 'input-v3/fonts/Inter-OFL.txt').read_text()
    license_cjk = (CASE / 'input-v3/fonts/Noto-OFL.txt').read_text()
    parts.append('<?xml version="1.0" encoding="UTF-8"?>')
    parts.append('<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1200" viewBox="0 0 900 1200" role="img" aria-labelledby="poster-title poster-description">')
    parts.append('<title id="poster-title">共生设计展 — COEXIST DESIGN EXHIBITION</title>')
    parts.append('<desc id="poster-description">12 JUNE — 28 AUGUST, 09:00–18:00. 城市设计馆。策展：林岚。四个弧形切割构字 C / O / E / X，在绿黑双场中承接全部展览事实。</desc>')
    parts.append('<metadata id="font-licenses">' + html.escape(license_inter + '\n\n' + license_cjk) + '</metadata>')
    parts.append('<!-- FONTS -->')
    parts.append('<g id="continuous-color-fields">')
    parts.append(f'<rect x="0" y="0" width="450" height="1200" fill="{C["green"]}"/>')
    parts.append(f'<rect x="450" y="0" width="450" height="1200" fill="{C["ink"]}"/>')
    parts.append('</g>')

    parts.append('<g id="cut-glyphs" aria-label="COEX：共生主题的构字提取">')
    # C: 405-wide capsule turns, 102-wide tangent stems, right-facing fact cut.
    path('glyph-C', 'M435 30 H232.5 A202.5 202.5 0 0 0 30 232.5 V319.5 A202.5 202.5 0 0 0 232.5 522 H435 V420 H232.5 A100.5 100.5 0 0 1 132 319.5 V232.5 A100.5 100.5 0 0 1 232.5 132 H435 Z', 'paper')
    # Repeated quarter-circle teeth share the C's upper cut edge.
    for i, x in enumerate((216, 289, 362), 1):
        path(f'C-cut-arc-tooth-{i}', f'M{x} 132 H{x+73} V205 A73 73 0 0 0 {x} 132 Z', 'paper')

    # O: tall capsule; the orange lower half is a complete structural bowl.
    path('glyph-O-pink', 'M667.5 30 A202.5 202.5 0 0 1 870 232.5 V319.5 A202.5 202.5 0 0 1 667.5 522 A202.5 202.5 0 0 1 465 319.5 V232.5 A202.5 202.5 0 0 1 667.5 30 Z M667.5 132 A100.5 100.5 0 0 0 567 232.5 V319.5 A100.5 100.5 0 0 0 667.5 420 A100.5 100.5 0 0 0 768 319.5 V232.5 A100.5 100.5 0 0 0 667.5 132 Z', 'pink', fill_rule='evenodd')
    path('glyph-O-orange-bowl', 'M465 319.5 A202.5 202.5 0 0 0 870 319.5 H768 A100.5 100.5 0 0 1 567 319.5 Z', 'orange')
    for i, x in enumerate((611, 667.5, 724), 1):
        parts.append(f'<circle id="O-bowl-node-{i}" cx="{x}" cy="459" r="20.25" fill="{C["paper"]}"/>')

    # E: the same outer/inner radius system as C, with a shared middle stem.
    path('glyph-E', 'M435 640 H232.5 A202.5 202.5 0 0 0 30 842.5 V957.5 A202.5 202.5 0 0 0 232.5 1160 H435 V1058 H232.5 A100.5 100.5 0 0 1 132 957.5 V954 H405 V852 H132 V842.5 A100.5 100.5 0 0 1 232.5 742 H435 Z', 'paper')

    # X: opposed, broad curved forks, interrupted by the full English title.
    # Outer R145 and inner R44 make a thick/negative contrast without rounded-font substitution.
    path('glyph-X-upper-fork', 'M465 640 H566 V672 A44 44 0 0 0 610 716 H725 A44 44 0 0 0 769 672 V640 H870 V672 A145 145 0 0 1 725 817 H610 A145 145 0 0 1 465 672 Z', 'orange')
    path('glyph-X-lower-fork', 'M465 1160 H566 V1128 A44 44 0 0 1 610 1084 H725 A44 44 0 0 1 769 1128 V1160 H870 V1128 A145 145 0 0 0 725 983 H610 A145 145 0 0 0 465 1128 Z', 'purple')
    parts.append('</g>')

    parts.append('<g id="editable-exhibition-facts">')
    parts.append('<g id="date-and-time-in-C" aria-label="12 JUNE — 28 AUGUST, 09:00–18:00">')
    text('start-date', 153, 265, '12 JUNE', 43.2, 'ink', 700)
    text('end-date', 153, 326, '28 AUGUST', 43.2, 'ink', 700)
    text('opening-hours', 153, 387, '09:00–18:00', 43.2, 'ink', 700)
    parts.append('</g>')

    parts.append('<g id="curator-and-venue-in-O" aria-label="策展：林岚；城市设计馆">')
    text('curator-label', 610, 193, '策展：', 21.6, 'paper', family='Study CJK')
    text('curator-name', 610, 228, '林岚', 21.6, 'paper', family='Study CJK')
    text('venue-line-one', 610, 286, '城市', 21.6, 'paper', family='Study CJK')
    text('venue-line-two', 610, 321, '设计馆', 21.6, 'paper', family='Study CJK')
    parts.append('</g>')

    parts.append('<g id="Chinese-title-in-E" aria-label="共生设计展">')
    text('title-Chinese-line-one', 154, 823, '共生', 68.4, 'yellow', 900, 'Study CJK')
    text('title-Chinese-line-two', 192, 1033, '设计展', 68.4, 'yellow', 900, 'Study CJK')
    parts.append('</g>')
    parts.append('<g id="English-title-in-X" aria-label="COEXIST DESIGN EXHIBITION">')
    text('title-English-line-one', 489, 867, 'COEXIST', 53.1, 'paper', 900)
    text('title-English-line-two', 489, 918, 'DESIGN', 53.1, 'paper', 900)
    text('title-English-line-three', 489, 969, 'EXHIBITION', 53.1, 'paper', 900)
    parts.append('</g>')
    parts.append('</g></svg>')

    HERE.mkdir(parents=True, exist_ok=True)
    raw = HERE / 'raw.svg'
    raw.write_text('\n'.join(parts) + '\n')
    root = ET.fromstring(raw.read_text())
    assert root.attrib['viewBox'] == '0 0 900 1200'
    actual = {el.attrib.get('id'): ''.join(el.itertext()) for el in root.iter() if el.tag.endswith('}text')}
    assert actual['start-date'] == '12 JUNE'
    assert actual['end-date'] == '28 AUGUST'
    assert actual['opening-hours'] == '09:00–18:00'
    assert actual['curator-label'] + actual['curator-name'] == '策展：林岚'
    assert actual['venue-line-one'] + actual['venue-line-two'] == '城市设计馆'
    assert actual['title-Chinese-line-one'] + actual['title-Chinese-line-two'] == '共生设计展'
    assert ' '.join(actual[f'title-English-line-{n}'] for n in ('one', 'two', 'three')) == 'COEXIST DESIGN EXHIBITION'
    subprocess.run([sys.executable, str(CASE / 'input-v3/embed_fonts.py'), str(CASE / 'input-v3/fonts'), str(raw), str(HERE / 'poster.svg')], check=True)
    ET.parse(HERE / 'poster.svg')
    print('Verified: 900 × 1200; editable text; all seven fixed fact groups; parseable raw/poster SVG.')

if __name__ == '__main__':
    main()
