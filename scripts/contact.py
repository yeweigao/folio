#!/usr/bin/env python3
"""contact — every unit as a thumbnail on one sheet.

Usage:
  contact.py out.png [--height 420] [--cols 0] label=img.png [label=img.png ...]
  contact.py out.png --row "Row label" a.png b.png --row "Next" c.png ...

The sheet is where rhythm, monotony and sameness across works are judged:
units scaled to one height, labelled underneath, in the order given.
With --row, each row gets its own label. Needs Pillow.
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

PAD, LABEL = 24, 34


def font(size):
    for f in ("/usr/share/fonts/opentype/inter/Inter-Medium.otf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        if Path(f).exists():
            return ImageFont.truetype(f, size)
    return ImageFont.load_default()


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    out, rest = Path(argv[0]), argv[1:]
    height, rows, cur, cols = 420, [], None, 0
    i = 0
    while i < len(rest):
        a = rest[i]
        if a == "--height":
            height = int(rest[i + 1]); i += 2; continue
        if a == "--cols":
            cols = int(rest[i + 1]); i += 2; continue
        if a == "--row":
            cur = (rest[i + 1], []); rows.append(cur); i += 2; continue
        if cur is None:
            cur = ("", []); rows.append(cur)
        label, _, path = a.rpartition("=") if "=" in a else (Path(a).stem, "", a)
        cur[1].append((label or Path(path).stem, Path(path)))
        i += 1
    f_small, f_row = font(18), font(22)
    laid = []
    for title, items in rows:
        thumbs = []
        for label, p in items:
            im = Image.open(p).convert("RGB")
            w = round(im.width * height / im.height)
            thumbs.append((label, im.resize((w, height), Image.LANCZOS)))
        if cols > 0 and len(thumbs) > cols:
            for k in range(0, len(thumbs), cols):
                laid.append((title if k == 0 else "", thumbs[k:k + cols]))
        else:
            laid.append((title, thumbs))
    width = max(PAD + sum(t.width + PAD for _, t in th) for _, th in laid)
    row_h = height + LABEL + PAD
    title_h = 36
    total = PAD + sum((title_h if t else 0) + row_h for t, _ in laid)
    sheet = Image.new("RGB", (width, total), (232, 232, 230))
    d = ImageDraw.Draw(sheet)
    y = PAD
    for title, thumbs in laid:
        if title:
            d.text((PAD, y), title, fill=(30, 30, 30), font=f_row)
            y += title_h
        x = PAD
        for label, t in thumbs:
            sheet.paste(t, (x, y))
            d.text((x, y + height + 8), label, fill=(60, 60, 60), font=f_small)
            x += t.width + PAD
        y += row_h
    sheet.save(out)
    print(out, sheet.size)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
