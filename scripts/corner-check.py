#!/usr/bin/env python3
"""corner-check — is the delivered contour continuous, or only rounded?

Usage:
  corner-check.py <file.html|file.svg|--d "M ... Z">  [--r 64] [--tol 0.08]

Reads an SVG path (a literal `d` string, or the first one in a file) and
measures curvature on every cubic segment, then compares the two sides of
each junction. A continuous corner ramps its curvature from 0 to 1/R and
back, so its junctions are quiet. A circular arc starts at 0 and jumps to
1/R the moment the straight edge ends: that step is what this script is
for, and it is the difference the eye reads as "slightly wrong" on a card.

  FAIL  an edge join — where a straight run meets the shoulder — carries a
        curvature step above the tolerance share of 1/R (default 8%). A
        circular corner fails here at 100%: that is the whole test.
  NOTE  internal joins between the shoulder's own segments are reported but
        not failed. The supplied three-cubic path is a fit of the native
        contour, so its internal joins are C0 rather than analytic G2; a
        circular arc, by contrast, cannot pass the edge join at all.

`--r` normalises the report to 1/R; without it, curvature is printed raw.
Stdlib only.
"""
import math
import re
import sys
from pathlib import Path

NUM = re.compile(r"[MLCZmlcz]|-?\d*\.?\d+(?:[eE][-+]?\d+)?")


def read_path(arg):
    if re.match(r"^\s*[Mm]\s*-?\d", arg):
        return arg, "(literal)"
    p = Path(arg)
    try:
        exists = p.exists()
    except OSError:
        return arg, "(literal)"
    if exists:
        raw = p.read_text(encoding="utf-8", errors="ignore")
        if re.match(r"^\s*[Mm]\s*-?\d", raw) and "<" not in raw:
            return raw.strip(), str(p)
        for m in re.finditer(r'\sd="([^"]+)"', raw):
            if "C" in m.group(1) or "A" in m.group(1):
                return m.group(1), str(p)
        raise SystemExit("no path with C or A found in " + str(p))
    return arg, "(literal)"


def parse(d):
    toks = [t for t in NUM.findall(d)]
    segs, i, cur, start = [], 0, (0.0, 0.0), (0.0, 0.0)
    while i < len(toks):
        c = toks[i].upper()
        if toks[i] != c and c in "MLCZ":
            raise SystemExit("relative commands are not analysed; convert to absolute first")
        i += 1
        if c == "M":
            cur = (float(toks[i]), float(toks[i + 1])); start = cur; i += 2
        elif c == "L":
            nxt = (float(toks[i]), float(toks[i + 1])); i += 2
            segs.append(("L", cur, nxt)); cur = nxt
        elif c == "C":
            p1 = (float(toks[i]), float(toks[i + 1]))
            p2 = (float(toks[i + 2]), float(toks[i + 3]))
            p3 = (float(toks[i + 4]), float(toks[i + 5])); i += 6
            segs.append(("C", cur, p1, p2, p3)); cur = p3
        elif c == "A":
            raise SystemExit("an arc (`A`) is a circular corner — the case this check catches")
        elif c == "Z":
            if cur != start:
                segs.append(("L", cur, start)); cur = start
    return segs


def cubic_at(p0, p1, p2, p3, t):
    u = 1 - t
    return (u**3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t**3 * p3[0],
            u**3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t**3 * p3[1])


def derivs(p0, p1, p2, p3, t):
    u = 1 - t
    dx = 3 * u * u * (p1[0] - p0[0]) + 6 * u * t * (p2[0] - p1[0]) + 3 * t * t * (p3[0] - p2[0])
    dy = 3 * u * u * (p1[1] - p0[1]) + 6 * u * t * (p2[1] - p1[1]) + 3 * t * t * (p3[1] - p2[1])
    ddx = 6 * u * (p2[0] - 2 * p1[0] + p0[0]) + 6 * t * (p3[0] - 2 * p2[0] + p1[0])
    ddy = 6 * u * (p2[1] - 2 * p1[1] + p0[1]) + 6 * t * (p3[1] - 2 * p2[1] + p1[1])
    return dx, dy, ddx, ddy


def curvature(seg, t):
    if seg[0] == "L":
        return 0.0
    dx, dy, ddx, ddy = derivs(*seg[1:], t)
    den = (dx * dx + dy * dy) ** 1.5
    return abs(dx * ddy - dy * ddx) / den if den else 0.0


def tangent(seg, t):
    if seg[0] == "L":
        a, b = seg[1], seg[2]
        return math.atan2(b[1] - a[1], b[0] - a[0])
    dx, dy, _, _ = derivs(*seg[1:], t)
    return math.atan2(dy, dx)


def main(argv):
    if not argv:
        print(__doc__); return 2
    arg, r, tol = None, None, 0.08
    i = 0
    while i < len(argv):
        if argv[i] == "--r":
            r = float(argv[i + 1]); i += 2; continue
        if argv[i] == "--tol":
            tol = float(argv[i + 1]); i += 2; continue
        if argv[i] == "--d":
            arg = argv[i + 1]; i += 2; continue
        arg = argv[i]; i += 1
    if arg is None:
        print(__doc__); return 2
    d, src = read_path(arg)
    segs = parse(d)
    if not segs:
        print("no segments"); return 1

    peak = 0.0
    for s in segs:
        for k in range(41):
            peak = max(peak, curvature(s, k / 40))

    rows, worst_edge, worst_inner, tang_edge = [], 0.0, 0.0, 0
    for j in range(1, len(segs)):
        a, b = segs[j - 1], segs[j]
        ka, kb = curvature(a, 1.0), curvature(b, 0.0)
        step = abs(kb - ka)
        edge = (a[0] == "L") != (b[0] == "L")
        if edge:
            worst_edge = max(worst_edge, step)
        else:
            worst_inner = max(worst_inner, step)
        ta, tb = tangent(a, 1.0), tangent(b, 0.0)
        dt = abs(math.atan2(math.sin(tb - ta), math.cos(tb - ta)))
        if edge and dt > math.radians(0.5):
            tang_edge += 1
        scale = (1.0 / r) if r else (peak or 1.0)
        rows.append((j, f"{a[0]}→{b[0]}", ka, kb, step / scale, math.degrees(dt), edge))

    cubics = sum(1 for s in segs if s[0] == "C")
    print(f"path: {src}")
    print(f"{len(segs)} segments ({cubics} cubic, {len(segs) - cubics} line), peak curvature "
          + (f"{peak:.6f} = {peak * r:.3f} × 1/R" if r else f"{peak:.6f}"))
    print()
    print(f"{'junction':>8}  {'pair':<6} {'k left':>9} {'k right':>9} {'step / (1/R)':>13} {'tangent':>8}  kind")
    for j, pair, ka, kb, rel, deg, edge in rows:
        print(f"{j:>8}  {pair:<6} {ka:>9.5f} {kb:>9.5f} {rel * 100:>12.2f}% {deg:>7.2f}°  "
              + ("edge" if edge else "inner"))

    scale = 1.0 / r if r else (peak or 1.0)
    verdict = "PASS" if worst_edge <= tol * scale and not tang_edge else "FAIL"
    print()
    print(f"edge joins: worst step {worst_edge / scale * 100:.2f}% of 1/R, tangent breaks {tang_edge}")
    print(f"inner joins: worst step {worst_inner / scale * 100:.2f}% of 1/R (reported, not failed)")
    print(verdict)
    if verdict == "FAIL":
        print("a circular corner steps 100% of 1/R the moment its straight edge ends; "
              "rebuild the contour from the shoulder path, not from border-radius.")
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
