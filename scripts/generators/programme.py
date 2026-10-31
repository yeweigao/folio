#!/usr/bin/env python3
"""programme — a Gerstner/Lohse programme field as SVG: a declared cycle,
no hand-tuned states (references/signature.md).

Usage: programme.py out.svg [--cols 8] [--rows 4] [--cycle 0,90,180,270] [--colors #111111,#C83024]
Each cell rotates by the cycle; the color advances every full cycle.
Stdlib only."""
import sys
from pathlib import Path

def main():
    args = sys.argv[1:]; cols, rows = 8, 4; cycle = [0, 90, 180, 270]; colors = ["#111111", "#C83024"]; pos = []
    i = 0
    while i < len(args):
        if args[i] == "--cols": cols = int(args[i+1]); i += 2
        elif args[i] == "--rows": rows = int(args[i+1]); i += 2
        elif args[i] == "--cycle": cycle = [int(x) for x in args[i+1].split(",")]; i += 2
        elif args[i] == "--colors": colors = args[i+1].split(","); i += 2
        else: pos.append(args[i]); i += 1
    CELL = 48; W, H = cols * CELL, rows * CELL
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    for n in range(cols * rows):
        r, c = divmod(n, cols); rot = cycle[n % len(cycle)]
        col = colors[(n // len(cycle)) % len(colors)]
        cx, cy = c * CELL + CELL / 2, r * CELL + CELL / 2
        o.append(f'<g transform="translate({cx} {cy}) rotate({rot})"><path d="M {-CELL/2} {CELL/2} L {CELL/2} {CELL/2} L {CELL/2} {-CELL/2} Z" fill="{col}"/></g>')
    o.append("</svg>")
    Path(pos[0]).write_text("\n".join(o)); print(f"wrote {pos[0]}: programme {cols}x{rows}, cycle {cycle}")

if __name__ == "__main__":
    main()
