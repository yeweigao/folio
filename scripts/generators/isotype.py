#!/usr/bin/env python3
"""isotype — Isotype rows as SVG (Neurath & Arntz, per references/signature.md).

Usage: isotype.py data.csv out.svg [--unit 10000] [--symbol circle|square] [--color #C83024]
CSV: label,value per line. One symbol = --unit; remainders are cut, never shrunk.
Stdlib only."""
import csv, sys
from pathlib import Path

def main():
    args = sys.argv[1:]
    unit, symbol, color = 1.0, "circle", "#111111"
    pos = []
    i = 0
    while i < len(args):
        if args[i] == "--unit": unit = float(args[i+1]); i += 2
        elif args[i] == "--symbol": symbol = args[i+1]; i += 2
        elif args[i] == "--color": color = args[i+1]; i += 2
        else: pos.append(args[i]); i += 1
    rows = [(r[0], float(r[1])) for r in csv.reader(open(pos[0])) if len(r) >= 2]
    S, GAP, ROW, LABEL = 18, 6, 34, 190
    maxsym = max(v / unit for _, v in rows)
    W = int(LABEL + (int(maxsym) + 1) * (S + GAP) + 10); H = len(rows) * ROW + 44
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    out.append(f'<text x="0" y="18" font-family="Inter, sans-serif" font-size="12">1 symbol = {unit:g}</text>')
    for ri, (label, v) in enumerate(rows):
        y = 34 + ri * ROW
        out.append(f'<text x="0" y="{y + S - 4}" font-family="Inter, sans-serif" font-size="13">{label}</text>')
        full, frac = int(v / unit), (v / unit) % 1
        for k in range(full):
            x = LABEL + k * (S + GAP)
            out.append(_sym(symbol, x, y, S, color))
        if frac > 0.02:
            x = LABEL + full * (S + GAP); cid = f"c{ri}"
            out.append(f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{S * frac:.1f}" height="{S}"/></clipPath>')
            out.append(f'<g clip-path="url(#{cid})">{_sym(symbol, x, y, S, color)}</g>')
    out.append("</svg>")
    Path(pos[1]).write_text("\n".join(out)); print(f"wrote {pos[1]}: {len(rows)} rows, unit {unit:g}")

def _sym(kind, x, y, s, color):
    if kind == "square":
        return f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="{color}"/>'
    return f'<circle cx="{x + s/2}" cy="{y + s/2}" r="{s/2}" fill="{color}"/>'

if __name__ == "__main__":
    main()
