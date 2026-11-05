#!/usr/bin/env python3
"""Create the case 03 composition from the frozen v4 text brief only."""
from pathlib import Path
import json
import subprocess
import sys
import xml.etree.ElementTree as ET

from fontTools.pens.boundsPen import BoundsPen
from fontTools.ttLib import TTFont

HERE = Path(__file__).resolve().parent
CASE = HERE.parent
INPUT = CASE / "input-v4"
FONTS = INPUT / "fonts"

SVG = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1200" viewBox="0 0 900 1200" role="img" aria-labelledby="poster-title poster-description">
  <title id="poster-title">共生设计展 — COEXIST DESIGN EXHIBITION</title>
  <desc id="poster-description">Green and black exhibition poster. Joined white strokes evoke 共; pink, orange and purple strokes recompose 生. Exhibition facts occupy deep vertical and horizontal cuts.</desc>
  <!-- FONTS -->
  <defs>
    <clipPath id="left-field-crop"><path d="M0 0H450V1200H0Z"/></clipPath>
  </defs>

  <g id="continuous-colour-fields">
    <path fill="#07964F" d="M0 0H450V1200H0Z"/>
    <path fill="#050505" d="M450 0H900V1200H450Z"/>
  </g>

  <g id="gong-upper-double-upright" fill="#FFFFFF">
    <!-- The large curved mass and its flat inner slot are one editable path. -->
    <path id="gong-connected-mass" fill-rule="evenodd" d="M52 28H154V192H282V40H392V430H450V530H252A200 200 0 0 1 52 330Z M154 295H282V430H154Z"/>
    <path id="gong-right-return" d="M366 430H450V807H366Z"/>
  </g>

  <g id="gong-diverging-lower-feet" fill="#FFFFFF" clip-path="url(#left-field-crop)">
    <path id="gong-left-foot" d="M60 705H164V886A262 262 0 0 1 -98 1148V1044A158 158 0 0 0 60 886Z"/>
    <path id="gong-right-foot" d="M262 705H366V886A158 158 0 0 0 524 1044V1148A262 262 0 0 1 262 886Z"/>
  </g>

  <g id="sheng-upper-neck-and-cut-bars" fill="#F3579D">
    <path id="sheng-curved-neck" d="M675 40H778V190H885V290H475V190H565A110 110 0 0 0 675 80Z"/>
    <path id="sheng-middle-bar" d="M475 500H885V600H475Z"/>
  </g>

  <g id="small-jointed-glyph-rhythm">
    <!-- Quarter teeth touch the large pink stroke, rather than forming a separate band. -->
    <path id="orange-tooth" fill="#FF7829" d="M475 28H557A82 82 0 0 1 475 110Z"/>
    <path id="blue-joint" fill="#0759FD" d="M565 28H647A82 82 0 0 1 565 110Z"/>
    <path id="pink-tooth" fill="#F3579D" d="M475 112H557A82 82 0 0 1 475 194Z"/>
    <path id="paper-tooth" fill="#FFFFFF" d="M565 112H647A82 82 0 0 1 565 194Z"/>
    <circle id="large-pink-node" fill="#F3579D" cx="851" cy="65" r="22"/>
    <path id="paper-short-bars" fill="#FFFFFF" d="M799 130H809V170H799Z M819.5 130H829.5V170H819.5Z M840 130H850V170H840Z M860.5 130H870.5V170H860.5Z"/>
  </g>

  <g id="sheng-bowl-and-return">
    <path id="orange-main-bowl" fill="#FF7829" d="M464 600H885A210.5 210.5 0 0 1 464 600Z"/>
    <path id="purple-main-return" fill="#9B38ED" d="M464 740H557V1008A92 92 0 0 0 649 1100H885V1193H649A185 185 0 0 1 464 1008Z"/>
  </g>

  <g id="facts-in-glyph-cuts">
    <text id="curator" fill="#050505" font-family="Study CJK" font-size="22" font-weight="400"><tspan x="170" y="103">策展：</tspan><tspan x="170" y="141">林岚</tspan></text>
    <text id="venue" fill="#050505" font-family="Study CJK" font-size="22" font-weight="400"><tspan x="170" y="345">城市</tspan><tspan x="170" y="383">设计馆</tspan></text>

    <text id="exhibition-chinese" x="12" y="642" fill="#FFF035" font-family="Study CJK" font-size="68.4" font-weight="900">共生设计展</text>

    <g id="dates-in-horizontal-break" fill="#FFFFFF" font-family="Study Sans" font-size="43.2" font-weight="700">
      <text id="start-date" x="509" y="350">12 JUNE</text>
      <text id="end-date" x="509" y="409">28 AUGUST</text>
      <text id="opening-hours" x="509" y="468">09:00–18:00</text>
    </g>

    <text id="exhibition-english" fill="#FFFFFF" font-family="Study Sans" font-size="53.1" font-weight="900"><tspan x="570" y="870">COEXIST</tspan> <tspan x="570" y="932">DESIGN</tspan> <tspan x="570" y="994">EXHIBITION</tspan></text>
  </g>
</svg>
'''


def ink_bounds(filename, text, size, x, baseline, weight=None):
    font = TTFont(FONTS / filename)
    location = {"wght": weight} if weight is not None else None
    glyphs = font.getGlyphSet(location=location)
    cmap = font.getBestCmap()
    offset = 0
    box = None
    for character in text:
        glyph = glyphs[cmap[ord(character)]]
        pen = BoundsPen(glyphs)
        glyph.draw(pen)
        if pen.bounds:
            x0, y0, x1, y1 = pen.bounds
            piece = (offset + x0, y0, offset + x1, y1)
            box = piece if box is None else (
                min(box[0], piece[0]), min(box[1], piece[1]),
                max(box[2], piece[2]), max(box[3], piece[3]),
            )
        offset += glyph.width
    scale = size / font["head"].unitsPerEm
    font.close()
    return (x + box[0] * scale, baseline - box[3] * scale,
            x + box[2] * scale, baseline - box[1] * scale)


def self_check():
    expected = {
        "curator": "策展：林岚", "venue": "城市设计馆",
        "exhibition-chinese": "共生设计展", "start-date": "12 JUNE",
        "end-date": "28 AUGUST", "opening-hours": "09:00–18:00",
        "exhibition-english": "COEXIST DESIGN EXHIBITION",
    }
    for filename in ("raw.svg", "poster.svg"):
        root = ET.parse(HERE / filename).getroot()
        assert root.attrib["viewBox"] == "0 0 900 1200"
        assert root.attrib["width"] == "900" and root.attrib["height"] == "1200"
        nodes = {n.attrib.get("id"): n for n in root.iter()}
        for identifier, content in expected.items():
            assert "".join(nodes[identifier].itertext()) == content, (filename, identifier)
        assert not any(n.tag.endswith("image") for n in root.iter())
    final = (HERE / "poster.svg").read_text()
    assert final.count("data:font/woff2;base64,") == 4
    assert "<!-- FONTS -->" not in final

    rows = [
        ("curator-1", "NotoSansSC-variable.ttf", "策展：", 22, 170, 103, 400, (154, 40, 282, 192)),
        ("curator-2", "NotoSansSC-variable.ttf", "林岚", 22, 170, 141, 400, (154, 40, 282, 192)),
        ("venue-1", "NotoSansSC-variable.ttf", "城市", 22, 170, 345, 400, (154, 295, 282, 430)),
        ("venue-2", "NotoSansSC-variable.ttf", "设计馆", 22, 170, 383, 400, (154, 295, 282, 430)),
        ("chinese-title", "NotoSansSC-variable.ttf", "共生设计展", 68.4, 12, 642, 900, (0, 530, 366, 705)),
        ("start-date", "Inter-700.ttf", "12 JUNE", 43.2, 509, 350, None, (475, 290, 885, 500)),
        ("end-date", "Inter-700.ttf", "28 AUGUST", 43.2, 509, 409, None, (475, 290, 885, 500)),
        ("hours", "Inter-700.ttf", "09:00–18:00", 43.2, 509, 468, None, (475, 290, 885, 500)),
        ("english-1", "Inter-900.ttf", "COEXIST", 53.1, 570, 870, None, (557, 810.5, 900, 1008)),
        ("english-2", "Inter-900.ttf", "DESIGN", 53.1, 570, 932, None, (557, 810.5, 900, 1008)),
        ("english-3", "Inter-900.ttf", "EXHIBITION", 53.1, 570, 994, None, (557, 810.5, 900, 1008)),
    ]
    measurements = []
    for name, filename, text, size, x, baseline, weight, cut in rows:
        ink = ink_bounds(filename, text, size, x, baseline, weight)
        gaps = (ink[0]-cut[0], ink[1]-cut[1], cut[2]-ink[2], cut[3]-ink[3])
        assert min(gaps) >= 12, (name, ink, gaps)
        measurements.append({"line": name, "ink": [round(v, 3) for v in ink],
                             "cut_margins": [round(v, 3) for v in gaps]})
    print(json.dumps({"xml": "valid", "fixed_text_groups": len(expected),
                      "embedded_font_faces": 4, "ink_checks": measurements}, ensure_ascii=False, indent=2))


def main():
    HERE.mkdir(parents=True, exist_ok=True)
    (HERE / "raw.svg").write_text(SVG)
    subprocess.run([sys.executable, str(INPUT / "embed_fonts.py"), str(FONTS),
                    str(HERE / "raw.svg"), str(HERE / "poster.svg")], check=True)
    self_check()


if __name__ == "__main__":
    main()
