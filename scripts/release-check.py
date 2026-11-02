#!/usr/bin/env python3
"""release-check — a release is consistent and its evidence holds.

Usage: release-check.py

1. SKILL.md's frontmatter version is the single source; README carries
   "(v<version>)" and the template version matches design-md.md.
2. Every skeleton under examples/ (any DESIGN.md) passes folio-check.
3. Every piece under examples/ (a brief.md with an .html beside it)
   passes factcheck against its own brief.
Exit 0 only when all of it holds. Stdlib only.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
problems = []

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
m = re.search(r"^version:\s*(\S+)\s*$", skill, re.M)
version = m.group(1) if m else None
if not version:
    problems.append("SKILL.md frontmatter carries no version")
readme = (ROOT / "README.md").read_text(encoding="utf-8")
if version and f"(v{version})" not in readme:
    problems.append(f"README does not carry (v{version})")
tmpl = re.search(r"folio-template-version:\s*(\d+)", (ROOT / "references/design-md.md").read_text(encoding="utf-8"))
template = tmpl.group(1) if tmpl else None

def run(*args):
    return subprocess.run([sys.executable, *map(str, args)], capture_output=True, text=True)

skeletons = sorted(p for p in (ROOT / "examples").rglob("DESIGN.md") if "archived" not in p.parts)
for d in skeletons:
    r = run(ROOT / "scripts/folio-check.py", d)
    if r.returncode != 0:
        problems.append(f"folio-check FAIL {d.relative_to(ROOT)}: {r.stdout.strip().splitlines()[0]}")
    rec = re.search(r"template version:?\s*(\d+)", d.read_text(encoding="utf-8"), re.I)
    if template and rec and rec.group(1) != template:
        problems.append(f"{d.relative_to(ROOT)} records template {rec.group(1)}, current is {template}")

pieces = sorted(p for p in (ROOT / "examples").rglob("brief.md") if "archived" not in p.parts)
for b in pieces:
    for h in sorted(b.parent.glob("*.html")):
        r = run(ROOT / "scripts/factcheck.py", b, h)
        if r.returncode != 0:
            problems.append(f"factcheck FAIL {h.relative_to(ROOT)}: {r.stdout.strip().splitlines()[-1]}")

print(f"version {version} · template v{template} · {len(skeletons)} skeletons · {len(pieces)} briefs")
if problems:
    print("RELEASE CHECK FAILED")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print("RELEASE CHECK PASS")
