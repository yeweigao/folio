#!/usr/bin/env python3
"""measure — field shares from rendered unit thumbnails (theme grammar:
paper >= 50%, accent <= 10%, <= 20% on a statement unit).

Usage: measure.py DESIGN.md thumb1.png [thumb2.png ...] [--statement thumb2.png]
Reports each image's share of the DESIGN.md neutral (paper) and tertiary
(accent) colors, within a per-channel tolerance. Needs Pillow; without it,
prints how to install and exits 2 — an unmeasured claim is reported, not faked.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from folio_lib import parse_front_matter

def hex2rgb(h):
    h = h.lstrip("#"); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def main():
    if "--statement" in sys.argv:
        k = sys.argv.index("--statement"); statement = sys.argv[k+1]; files = [a for a in sys.argv[1:] if a not in ("--statement", statement)]
    else:
        statement, files = None, sys.argv[1:]
    md, files = Path(files[0]), files[1:]
    try:
        from PIL import Image
    except ImportError:
        print("Pillow not installed: pip install pillow — field shares unmeasured"); return 2
    tokens, _ = parse_front_matter(md.read_text(encoding="utf-8"))
    paper, accent = hex2rgb(tokens["colors"]["neutral"]), hex2rgb(tokens["colors"]["tertiary"])
    TOL = 26
    def near(px, target): return all(abs(int(a) - b) <= TOL for a, b in zip(px[:3], target))
    bad = 0
    for f in files:
        im = Image.open(f).convert("RGB"); im.thumbnail((400, 400))
        px = list(im.getdata()); n = len(px)
        ps = sum(1 for p in px if near(p, paper)) / n * 100
        ac = sum(1 for p in px if near(p, accent)) / n * 100
        limit = 20 if statement and Path(f).name == Path(statement).name else 10
        okp, oka = ps >= 50, ac <= limit
        bad += (not okp) + (not oka)
        print(f"{Path(f).name}: paper {ps:.0f}% ({'ok' if okp else 'FAIL <50%'}), accent {ac:.0f}% ({'ok' if oka else f'FAIL >{limit}%'})")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
