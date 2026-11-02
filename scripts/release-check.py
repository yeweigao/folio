#!/usr/bin/env python3
"""release-check — a release is consistent and its evidence holds.

Usage: release-check.py

1. SKILL.md's frontmatter version is the single source; README carries
   "(v<version>)" and the template version matches design-md.md.
2. Routing: every file under references/ and scripts/ is reached from
   SKILL.md (links, backticked paths, folders, Python imports); SKILL.md
   links only from Routes and Themes; no link is broken.
   CONTRIBUTING.md may reach maintenance scripts.
3. Every skeleton under examples/ (any DESIGN.md) passes folio-check.
4. Every piece under examples/ (a brief.md with an .html beside it)
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

LINK = re.compile(r"\]\(([^)#\s]+)")
PATH = re.compile(r"(?<![\w/.])((?:references|scripts)/[\w./<>-]*\w/?)")
IMPORT = re.compile(r"^\s*(?:from|import)\s+(\w+)", re.M)

def targets(f):
    if f.suffix not in (".md", ".py"):
        return []
    text = f.read_text(encoding="utf-8")
    found = []
    if f.suffix == ".md":
        for m in LINK.findall(text):
            if "://" in m or m.startswith("mailto:"):
                continue
            found.append((m, (f.parent / m).resolve()))
        for m in PATH.findall(" ".join(re.findall(r"`([^`]+)`", text))):
            if "<" not in m:
                found.append((m, (ROOT / m).resolve()))
    elif f.suffix == ".py":
        for m in IMPORT.findall(text):
            mod = f.parent / f"{m}.py"
            if mod.exists():
                found.append((m, mod.resolve()))
    return found

def reach(start):
    seen, todo = set(), [start.resolve()]
    while todo:
        f = todo.pop()
        if f in seen:
            continue
        seen.add(f)
        for raw, t in targets(f):
            if t.is_dir():
                todo += [x for x in t.rglob("*") if x.is_file() and "__pycache__" not in x.parts and not x.name.startswith(".")]
            elif t.is_file():
                todo.append(t)
            elif f.is_relative_to(ROOT / "references") or f.name in ("SKILL.md", "CONTRIBUTING.md"):
                problems.append(f"broken link in {f.relative_to(ROOT)}: {raw}")
    return seen

body = skill.split("\n---", 2)[-1]
for sec in re.split(r"^## ", body, flags=re.M)[1:]:
    name = sec.splitlines()[0].strip()
    if name not in ("Routes", "Themes") and LINK.search(sec):
        problems.append(f"SKILL.md links from '{name}'; only Routes and Themes route")
agent = reach(ROOT / "SKILL.md")
maint = reach(ROOT / "CONTRIBUTING.md") if (ROOT / "CONTRIBUTING.md").exists() else set()
shipped = [x for d in ("references", "scripts") for x in (ROOT / d).rglob("*")
           if x.is_file() and "__pycache__" not in x.parts and not x.name.startswith(".")]
for x in sorted(shipped):
    r = x.resolve()
    if r in agent:
        continue
    if x.is_relative_to(ROOT / "scripts") and r in maint:
        continue
    problems.append(f"unreached from SKILL.md: {x.relative_to(ROOT)}")

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

print(f"version {version} · template v{template} · {len(agent)} files routed · {len(skeletons)} skeletons · {len(pieces)} briefs")
if problems:
    print("RELEASE CHECK FAILED")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print("RELEASE CHECK PASS")
