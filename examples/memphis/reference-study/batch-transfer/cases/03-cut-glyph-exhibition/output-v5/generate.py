#!/usr/bin/env python3
"""Construct the exhibition poster as editable SVG, then embed supplied fonts."""
from pathlib import Path
import subprocess
import sys
import xml.etree.ElementTree as ET

from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "input-v5"
C = dict(green="#07964F", ink="#050505", paper="#FFFFFF", pink="#F3579D",
         yellow="#FFF035", blue="#0759FD", orange="#FF7829", purple="#9B38ED")


def hook(x):
    # A 70 px stem, a 133 px outer bend, and a 63 px inner bend.
    return (f"M{x-20} 520 H{x+70} V699 "
            f"A63 63 0 0 0 {x+133} 762 V832 "
            f"A133 133 0 0 1 {x} 699 V547 H{x-20} Z")


svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1200" viewBox="0 0 900 1200" role="img" aria-labelledby="poster-title poster-desc">
<title id="poster-title">共生设计展 — COEXIST DESIGN EXHIBITION</title>
<desc id="poster-desc">虚构展览海报。共与生的白色切割字形在绿场相接，黑场承接粉色曲笔、紫色并列弯钩和橙色双碗腰体。日期、策展、展名与地点进入字形开口。</desc>
<defs><!-- FONTS --></defs>
<g id="continuous-fields">
  <path id="green-field" fill="{C['green']}" d="M0 0H470V1200H0Z"/>
  <path id="ink-field" fill="{C['ink']}" d="M470 0H900V1200H470Z"/>
</g>
<g id="shared-life-white-glyphs" fill="{C['paper']}">
  <g id="glyph-gong" aria-label="共" data-module="410" data-stroke="92">
    <path id="gong-uprights-and-split-crossbar" d="M82 20H174V265H276V20H368V110H430V202H368V265H430V357H20V265H82V202H20V110H82Z"/>
    <path id="gong-left-curved-foot" d="M225 325A155 155 0 0 1 70 480H20V388H70A63 63 0 0 0 133 325Z"/>
    <path id="gong-right-curved-foot" d="M225 325A155 155 0 0 0 380 480H430V388H380A63 63 0 0 1 317 325Z"/>
  </g>
  <path id="shared-left-spine" d="M20 388H108V861H20Z"/>
  <g id="glyph-sheng" aria-label="生" data-module="410" data-stroke="92">
    <path id="sheng-falling-curve" d="M151 720H245A141 141 0 0 1 104 861H22V770H104A50 50 0 0 0 154 720Z"/>
    <path id="sheng-stem-and-three-crossbars" d="M224 720H318V800H430V891H318V950H430V1041H318V1089H430V1180H20V1089H224V1041H20V950H224V891H104V800H224Z"/>
  </g>
</g>
<g id="segmented-right-glyphs">
  <path id="pink-open-shared-shoulder" fill="{C['pink']}" data-module="400" data-stroke="88" d="M490 20H714A186 186 0 0 1 900 206V420H772V333H812V206A98 98 0 0 0 714 108H490Z"/>
  <g id="joined-arc-teeth-and-nodes">
    <path id="pink-quarter-tooth" fill="{C['pink']}" d="M490 333H570A80 80 0 0 1 490 413Z"/>
    <path id="blue-quarter-joint" fill="{C['blue']}" d="M570 333H650V413A80 80 0 0 1 570 333Z"/>
    <circle id="upper-node" fill="{C['paper']}" cx="683" cy="354" r="21"/>
    <circle id="lower-node" fill="{C['yellow']}" cx="683" cy="399" r="21"/>
    <path id="short-bars" fill="{C['paper']}" d="M722 358H731.75V420H722Z M741.5 358H751.25V420H741.5Z M761 358H770.75V420H761Z"/>
  </g>
  <g id="purple-parallel-hooks" fill="{C['purple']}" data-module="390" data-stroke="70">
    <path id="hook-one" d="{hook(500)}"/>
    <path id="hook-two" d="{hook(616)}"/>
    <path id="hook-three" d="{hook(732)}"/>
  </g>
  <path id="orange-double-bowl-waist" fill="{C['orange']}" fill-rule="evenodd" data-module="390" d="M490 851H880A117 117 0 0 1 763 968H742V1007A138 138 0 0 1 880 1145V1178H490V1145A138 138 0 0 1 628 1007V968H607A117 117 0 0 1 490 851Z M734 1118A49 22 0 1 0 636 1118A49 22 0 1 0 734 1118Z"/>
</g>
<g id="editable-facts">
  <text id="curator" font-family="Study CJK, sans-serif" font-size="21.6" font-weight="400" fill="{C['ink']}"><tspan x="191" y="131">策展：</tspan><tspan x="202" y="169">林岚</tspan></text>
  <g id="dates" font-family="Study Sans, sans-serif" font-size="43.2" font-weight="700" fill="{C['yellow']}">
    <text id="start-date" x="126" y="531">12 JUNE</text>
    <text id="end-date" x="126" y="588">28 AUGUST</text>
  </g>
  <text id="cjk-title" x="117.5" y="691" font-family="Study CJK, sans-serif" font-size="68.4" font-weight="900" fill="{C['ink']}">共生设计展</text>
  <text id="english-title" font-family="Study Sans, sans-serif" font-size="53.1" font-weight="900" fill="{C['paper']}" xml:space="preserve"><tspan x="486" y="174">COEXIST </tspan><tspan x="486" y="238">DESIGN </tspan><tspan x="486" y="302">EXHIBITION</tspan></text>
  <text id="hours" x="500" y="483" font-family="Study Sans, sans-serif" font-size="43.2" font-weight="700" fill="{C['paper']}">09:00–18:00</text>
  <text id="venue" x="35" y="929" font-family="Study CJK, sans-serif" font-size="21.6" font-weight="400" fill="{C['ink']}">城市设计馆</text>
</g>
</svg>'''

raw = HERE / "raw.svg"
poster = HERE / "poster.svg"
HERE.mkdir(exist_ok=True)
raw.write_text(svg, encoding="utf-8")
subprocess.run([sys.executable, str(SOURCE / "embed_fonts.py"), str(SOURCE / "fonts"), str(raw), str(poster)], check=True)

# Checks use native font glyph bounds, not nominal advances.
font_cache = {}


def ink_bounds(text, x, y, size, filename, weight):
    key = (filename, weight)
    if key not in font_cache:
        font = TTFont(SOURCE / "fonts" / filename)
        glyphs = font.getGlyphSet(location={"wght": weight}) if "fvar" in font else font.getGlyphSet()
        font_cache[key] = font, glyphs
    font, glyphs = font_cache[key]
    scale = size / font["head"].unitsPerEm
    cmap = font.getBestCmap()
    advance = 0
    result = None
    for char in text:
        name = cmap[ord(char)]
        pen = BoundsPen(glyphs)
        glyphs[name].draw(pen)
        if pen.bounds:
            a, b, c, d = pen.bounds
            box = (x + (a + advance) * scale, y - d * scale,
                   x + (c + advance) * scale, y - b * scale)
            result = box if result is None else (min(result[0], box[0]), min(result[1], box[1]), max(result[2], box[2]), max(result[3], box[3]))
        advance += glyphs[name].width
    return result


checks = [
    ("策展：", 191, 131, 21.6, "NotoSansSC-variable.ttf", 400, (174, 20, 276, 265)),
    ("林岚", 202, 169, 21.6, "NotoSansSC-variable.ttf", 400, (174, 20, 276, 265)),
    ("12 JUNE", 126, 531, 43.2, "Inter-700.ttf", 700, (108, 480, 470, 720)),
    ("28 AUGUST", 126, 588, 43.2, "Inter-700.ttf", 700, (108, 480, 470, 720)),
    ("共生设计展", 117.5, 691, 68.4, "NotoSansSC-variable.ttf", 900, (108, 480, 470, 720)),
    ("COEXIST", 486, 174, 53.1, "Inter-900.ttf", 900, (470, 108, 812, 333)),
    ("DESIGN", 486, 238, 53.1, "Inter-900.ttf", 900, (470, 108, 812, 333)),
    ("EXHIBITION", 486, 302, 53.1, "Inter-900.ttf", 900, (470, 108, 812, 333)),
    ("09:00–18:00", 500, 483, 43.2, "Inter-700.ttf", 700, (470, 420, 900, 520)),
    ("城市设计馆", 35, 929, 21.6, "NotoSansSC-variable.ttf", 400, (20, 891, 224, 950)),
]
for text, x, y, size, filename, weight, region in checks:
    box = ink_bounds(text, x, y, size, filename, weight)
    gaps = (box[0] - region[0], box[1] - region[1], region[2] - box[2], region[3] - box[3])
    assert min(gaps) >= 12, (text, box, region, gaps)

ns = {"s": "http://www.w3.org/2000/svg"}
expected = {
    "curator": "策展：林岚", "start-date": "12 JUNE", "end-date": "28 AUGUST",
    "cjk-title": "共生设计展", "english-title": "COEXIST DESIGN EXHIBITION",
    "hours": "09:00–18:00", "venue": "城市设计馆",
}
for path in (raw, poster):
    root = ET.parse(path).getroot()
    assert (root.get("width"), root.get("height"), root.get("viewBox")) == ("900", "1200", "0 0 900 1200")
    texts = {node.get("id"): "".join(node.itertext()) for node in root.findall(".//s:text", ns)}
    assert texts == expected, texts
    assert not root.findall(".//s:image", ns)
    assert not root.findall(".//s:foreignObject", ns)
assert poster.read_text().count("@font-face") == 4
assert "data:font/woff2;base64," in poster.read_text()
print("Verified: XML; 900×1200; seven editable fact objects; exact fixed text; native vectors; four embedded font faces; text-to-cut margins ≥12 px.")
