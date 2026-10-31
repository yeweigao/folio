#!/usr/bin/env python3
"""ledger — a ledger table as SVG: value, baseline, period, change, aligned
on the decimal, one hairline opens, one ink rule closes (craft, Data).

Usage: ledger.py data.csv out.svg [--ink #111111] [--line #C5C2BC]
CSV header: item,value,baseline,period,change (numbers as plain decimals).
Stdlib only."""
import csv, sys
from pathlib import Path

def main():
    args = sys.argv[1:]; ink, line = "#111111", "#C5C2BC"; pos = []
    i = 0
    while i < len(args):
        if args[i] == "--ink": ink = args[i+1]; i += 2
        elif args[i] == "--line": line = args[i+1]; i += 2
        else: pos.append(args[i]); i += 1
    rows = list(csv.DictReader(open(pos[0])))
    W, RH, X0 = 880, 30, 8
    cols = [("item", X0, "start"), ("value", 430, "end"), ("baseline", 560, "end"), ("period", 700, "start"), ("change", 872, "end")]
    H = 34 + len(rows) * RH + 14
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
         f'<line x1="0" y1="6" x2="{W}" y2="6" stroke="{line}" stroke-width="1"/>']
    hdr = {"item": "Item", "value": "Value", "baseline": "Baseline", "period": "Period", "change": "Change"}
    for k, x, anchor in cols:
        o.append(f'<text x="{x}" y="24" text-anchor="{anchor}" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="{ink}">{hdr[k]}</text>')
    for ri, r in enumerate(rows):
        y = 34 + ri * RH + 18
        for k, x, anchor in cols:
            weight = "700" if k == "value" else "400"
            o.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Inter, sans-serif" font-size="14" font-weight="{weight}" fill="{ink}" font-variant-numeric="tabular-nums">{r[k]}</text>')
    o.append(f'<line x1="0" y1="{34 + len(rows) * RH + 6}" x2="{W}" y2="{34 + len(rows) * RH + 6}" stroke="{ink}" stroke-width="2"/></svg>')
    Path(pos[1]).write_text("\n".join(o)); print(f"wrote {pos[1]}: {len(rows)} ledger rows")

if __name__ == "__main__":
    main()
