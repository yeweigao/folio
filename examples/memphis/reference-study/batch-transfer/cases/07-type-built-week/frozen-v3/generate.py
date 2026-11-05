#!/usr/bin/env python3
"""Build a 900 × 1200 letter-wall poster from the provided v3 brief.

Display text stays live; only E, G and the year-zero use native geometry.
The supplied neutral helper embeds the supplied, OFL-licensed Inter faces.
"""
from pathlib import Path
import html
import subprocess
import sys
import xml.etree.ElementTree as ET

from fontTools.pens.boundsPen import BoundsPen
from fontTools.ttLib import TTFont


CASE = Path(__file__).resolve().parent.parent
SUPPORT = CASE / "input-v3"
OUT = Path(__file__).resolve().parent
FONT = TTFont(SUPPORT / "fonts" / "Inter-900.ttf")
GLYPHS = FONT.getGlyphSet()
CMAP = FONT.getBestCmap()
UPM = FONT["head"].unitsPerEm
CAP = FONT["OS/2"].sCapHeight

PAPER = "#F6F0E5"
INK = "#1C1A1B"
BLUE = "#258CB4"
PURPLE = "#554699"
ORANGE_GLYPH = "#F54D05"


def n(value):
    return f"{value:.6f}".rstrip("0").rstrip(".")


def ink_bounds(word):
    """Unkerned native-font bounds, used only to size editable display text."""
    cursor = 0
    left = float("inf")
    right = float("-inf")
    for char in word:
        name = CMAP[ord(char)]
        pen = BoundsPen(GLYPHS)
        GLYPHS[name].draw(pen)
        if pen.bounds:
            left = min(left, cursor + pen.bounds[0])
            right = max(right, cursor + pen.bounds[2])
        cursor += FONT["hmtx"][name][0]
    return left, right


def display(word, x, top, width, height, element_id):
    size = height * UPM / CAP
    left, right = ink_bounds(word)
    horizontal = width / ((right - left) * size / UPM)
    return (
        f'<g id="{element_id}" transform="translate({n(x)} {n(top + height)}) '
        f'scale({n(horizontal)} 1)">'
        f'<text x="{n(-left * size / UPM)}" y="0" font-size="{n(size)}" '
        f'font-weight="900">{html.escape(word)}</text></g>'
    )


def text(value, x, baseline, size, weight=400, fill=INK, element_id=None):
    ident = f' id="{element_id}"' if element_id else ""
    return (
        f'<text{ident} x="{n(x)}" y="{n(baseline)}" font-size="{n(size)}" '
        f'font-weight="{weight}" fill="{fill}">{html.escape(value)}</text>'
    )


def rect(x, y, width, height, fill):
    return (
        f'<rect x="{n(x)}" y="{n(y)}" width="{n(width)}" '
        f'height="{n(height)}" fill="{fill}"/>'
    )


def circle(cx, cy, radius, fill):
    return f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{n(radius)}" fill="{fill}"/>'


def build():
    license_text = (SUPPORT / "fonts" / "Inter-OFL.txt").read_text()
    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1200" '
        'viewBox="0 0 900 1200" role="img" aria-labelledby="poster-title poster-description">',
        '<title id="poster-title">TAIPEI DESIGN WEEK 2027</title>',
        '<desc id="poster-description">Four tightly stacked letter walls introduce '
        'Taipei Design Week, October 4–10, 2027. Native E bars, a geometric G, and '
        'a circular zero form parts of the lettering. Event details follow below.</desc>',
        '<metadata id="font-license">' + html.escape(license_text) + '</metadata>',
        '<defs><!-- FONTS --></defs>',
        '<g font-family="Study Sans" fill="' + INK + '" '
        'style="font-kerning:none;font-variant-ligatures:none">',
        rect(0, 0, 900, 1200, PAPER),
        '<g id="letter-walls">',
        display("TAIPEI", 26, 26, 848, 178, "city-wall"),
        '<g id="theme-wall" aria-label="DESIGN">',
        display("D", 26, 216, 145, 178, "theme-d"),
        '<g id="theme-e" aria-label="E">',
        rect(181, 216, 124, 35.6, INK),
        rect(181, 287.2, 124, 35.6, PURPLE),
        rect(181, 358.4, 124, 35.6, INK),
        '</g>',
        display("S", 315, 216, 147, 178, "theme-s"),
        display("I", 472, 216, 49, 178, "theme-i"),
        '<g id="theme-g" aria-label="G">',
        circle(620, 305, 89, BLUE),
        circle(620, 305, 43, PAPER),
        rect(620, 278, 89, 45, PAPER),
        rect(620, 305, 89, 34, INK),
        rect(675, 305, 34, 55, INK),
        '</g>',
        display("N", 719, 216, 155, 178, "theme-n"),
        '</g>',
        display("WEEK", 26, 406, 848, 178, "event-wall"),
        '<g id="year-wall" aria-label="2027">',
        display("2", 26, 596, 206, 205, "year-first-two"),
        '<g id="year-zero" aria-label="0">',
        circle(346.5, 698.5, 102.5, ORANGE_GLYPH),
        '</g>',
        display("2", 461, 596, 206, 205, "year-second-two"),
        display("7", 679, 596, 195, 205, "year-seven"),
        '</g></g>',
        '<g id="event-details">',
    ]
    for index, value in enumerate([
        "ARCHITECTURE", "CRAFT", "FOOD", "MUSIC", "PUBLIC SPACE"
    ]):
        parts.append(text(value, 26, 855 + 31 * index, 22))
    parts.extend([
        text("TAIPEI DESIGN WEEK 2027", 385, 855, 24, 700),
        text("OCTOBER 4–10", 385, 914, 33, 700),
        text("HOST", 385, 966, 16, 700),
        text("City Design Museum", 475, 966, 25),
        text("PARTNER", 385, 1013, 16, 700),
        text("Open City Lab", 475, 1013, 25),
        '</g>',
        '<g id="website-band">',
        rect(0, 1074, 900, 126, INK),
        text("TAIPEIDESIGNWEEK.EXAMPLE", 26, 1158, 54, 700, PAPER, "website"),
        '</g></g></svg>',
    ])
    raw = OUT / "raw.svg"
    raw.write_text("\n".join(parts) + "\n")
    subprocess.run([
        sys.executable, str(SUPPORT / "embed_fonts.py"), str(SUPPORT / "fonts"),
        str(raw), str(OUT / "poster.svg")
    ], check=True)
    verify(OUT / "poster.svg")


def verify(path):
    data = path.read_text()
    root = ET.fromstring(data)
    assert root.attrib["viewBox"] == "0 0 900 1200"
    live = "\n".join(
        "".join(node.itertext())
        for node in root.iter()
        if node.tag.rsplit("}", 1)[-1] == "text"
    )
    facts = [
        "TAIPEI", "DESIGN", "WEEK", "2027", "ARCHITECTURE", "CRAFT", "FOOD",
        "MUSIC", "PUBLIC SPACE", "OCTOBER 4–10", "TAIPEIDESIGNWEEK.EXAMPLE",
        "City Design Museum", "Open City Lab",
    ]
    assert all(fact in live for fact in facts)
    assert data.count("@font-face") == 3
    assert data.count("data:font/woff2;base64,") == 3
    assert not any(node.tag.rsplit("}", 1)[-1] == "image" for node in root.iter())
    assert not any("href" in key for node in root.iter() for key in node.attrib)
    print("Verified: 900 × 1200 XML; all 13 facts in live text; 3 embedded font weights; no images or external hrefs.")


if __name__ == "__main__":
    build()
