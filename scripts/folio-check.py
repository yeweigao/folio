#!/usr/bin/env python3
"""folio-check — deterministic gates for a Folio deliverable.

Usage:
  folio-check.py DESIGN.md [export.pptx|export.html ...]

DESIGN.md checks (completeness + its own floors):
  C1 Record names a Folio version and a template version
  C2 colors define a focus token; a soft field exists beside neutral
  C3 every field (neutral / soft / accent / dark) has a text-on component pair
  C4 every typography fontFamily stack carries a CJK face
     (Han / Noto Sans SC / PingFang / YaHei / Songti)
  C5 component text pairs meet WCAG contrast (normal text >= 4.5:1)
  C6 no orphan tokens: every color is referenced by a component or named
     in the prose; every component reference resolves
  C9 a speaking deliverable names a signature programme (references/
     signature.md) or records 'Signature: none' with a reason
  C7 Folio sections filled: Directions records a choice, Sequence has at
     least one filled row, Coverage and Gaps sections are present
Export checks (when files are given):
  E1 every hex color used in a .pptx/.html export is a DESIGN.md token
     (within the file's own palette; unknown colors are failures)
  E2 every font family named in the export appears in a DESIGN.md type stack
  E3 banned chart forms in .pptx: pieChart / doughnutChart / dual axes
  E4 craft Copy blacklist words in the export's text (pptx and html)
  E5 (warning) pictures present: captions/sources need a human check
Exit code 0 = pass, 1 = failures listed. Stdlib only.
"""
import re, sys, zipfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from folio_lib import parse_front_matter, resolve, contrast, HEX

fail, warn = [], []

def check_design(md_path):
    text = Path(md_path).read_text(encoding="utf-8")
    tokens, prose = parse_front_matter(text)
    if not tokens:
        fail.append("C0 no YAML front matter found"); return tokens, prose
    colors = tokens.get("colors", {})
    typo = tokens.get("typography", {})
    comps = tokens.get("components", {})
    # C1
    rec = prose.split("## Record")[-1] if "## Record" in prose else ""
    if not re.search(r"folio\s*(version)?\s*[:：]?\s*\d+\.\d+", rec, re.I):
        fail.append("C1 Record does not name a Folio version (e.g. 'Folio version: 0.4.0')")
    if not re.search(r"template\s*(version)?\s*[:：]?\s*\d+", rec, re.I):
        fail.append("C1 Record does not name a template version")
    # C2
    if "focus" not in colors:
        fail.append("C2 colors has no focus token (web surface requires a visible focus color)")
    if "soft" not in colors:
        fail.append("C2 colors has no soft field beside neutral (theme grammar: every field carries a palette)")
    # C3
    fields = {"neutral": "paper", "soft": "soft", "tertiary": "accent", "dark": "dark"}
    for tok in fields:
        if tok in colors and not any(
            isinstance(c, dict) and resolve(c.get("backgroundColor", ""), tokens) == colors[tok]
            and c.get("textColor") for c in comps.values()):
            fail.append(f"C3 field '{tok}' has no text-on component pair")
    # C4
    cjk = re.compile(r"Han|Noto Sans SC|Noto Serif SC|PingFang|YaHei|Songti|Heiti|Source Han", re.I)
    for name, t in typo.items():
        fam = t.get("fontFamily", "") if isinstance(t, dict) else ""
        if fam and not cjk.search(fam):
            fail.append(f"C4 typography.{name} fontFamily has no CJK face in its stack: {fam}")
    # C5 + C6
    used_colors = set()
    for name, c in comps.items():
        if not isinstance(c, dict):
            continue
        bg = resolve(c.get("backgroundColor", ""), tokens)
        fg = resolve(c.get("textColor", ""), tokens)
        for ref in (c.get("backgroundColor"), c.get("textColor")):
            m = re.fullmatch(r"\{colors\.([\w-]+)\}", str(ref or ""))
            if m: used_colors.add(m.group(1))
            elif ref and str(ref).startswith("{"):
                fail.append(f"C6 component {name} has an unresolvable reference {ref}")
        if bg and fg and str(bg).startswith("#") and str(fg).startswith("#"):
            r = contrast(fg, bg)
            if r and r < 4.5:
                fail.append(f"C5 component {name}: text {fg} on {bg} is {r:.2f}:1 (< 4.5:1)")
    for cname, cval in colors.items():
        if cname not in used_colors and str(cval).lower() not in prose.lower():
            fail.append(f"C6 color '{cname}' is defined but never used by a component or named in prose")
    # C7
    if "## Directions" in prose and not re.search(r"chosen", prose, re.I):
        fail.append("C7 Directions does not record a choice ('Chosen: ...')")
    if "## Sequence" in prose:
        rows = [l for l in prose.split("## Sequence")[-1].split("##")[0].split("\n")
                if l.strip().startswith("|") and "---" not in l and "Unit" not in l and l.count("|") >= 4 and l.replace("|", "").replace(" ", "")]
        if not rows:
            fail.append("C7 Sequence table has no filled rows")
    # C8 monotony gate: a speaking sequence of 4+ units with no variation
    # taken does not lock (reference-majority sequences excepted). The
    # variation is the row's last cell; continuity rows say so.
    if "## Sequence" in prose:
        sec_text = prose.split("## Sequence")[-1].split("##")[0]
        rows = []
        for l in sec_text.split("\n"):
            if l.strip().startswith("|") and "---" not in l and "Unit" not in l:
                cells = [c.strip() for c in l.strip().strip("|").split("|")]
                if len(cells) >= 5 and cells[0]:
                    rows.append(cells)
        if len(rows) >= 4:
            ref = sum(1 for r in rows if "reference" in r[1].lower())
            turns = sum(1 for r in rows if not r[-1].lower().startswith("continuity"))
            if turns == 0 and ref <= len(rows) / 2:
                fail.append("C8 monotony: Sequence has 4+ units and no variation taken — a rhythm failure, not a style (SKILL.md step 6)")
    # C9 signature gate
    SIG = ["graphic scale", "scale contrast", "grid alphabet", "exposed grid", "isotype",
           "becher", "route line", "cut-out", "programme", "close-up", "calligram", "photo-essay"]
    if "## Sequence" in prose:
        sec_text = prose.split("## Sequence")[-1].split("##")[0]
        n_rows = len([l for l in sec_text.split("\n") if l.strip().startswith("|") and "---" not in l and "Unit" not in l])
        has_sig = any(k in prose.lower() for k in SIG)
        none_declared = re.search(r"signature[^\n:]*:\s*none\b.{12,}", prose, re.I)
        if n_rows >= 4 and not has_sig and not none_declared:
            fail.append("C9 no signature programme: no signature method (references/signature.md) is used and no 'Signature: none — <reason>' is recorded")
    for sec in ("## Coverage", "## Gaps"):
        if sec not in prose:
            fail.append(f"C7 missing Folio section {sec}")
    return tokens, prose

def check_export(path, tokens):
    colors = {str(v).lower() for v in tokens.get("colors", {}).values() if str(v).startswith("#")}
    stacks = " ".join(t.get("fontFamily", "") for t in tokens.get("typography", {}).values() if isinstance(t, dict)).lower()
    data = ""
    if path.suffix == ".pptx":
        # Only slides and charts count as "used": themes and layouts carry
        # the template's unused font scheme and palette, which would flood
        # both checks with false positives.
        with zipfile.ZipFile(path) as z:
            names = z.namelist()
            data = " ".join(z.read(n).decode("utf-8", "ignore") for n in names
                            if n.startswith(("ppt/slides/slide", "ppt/charts/chart")))
            charts = " ".join(z.read(n).decode("utf-8", "ignore") for n in names if n.startswith("ppt/charts/chart"))
            if re.search(r"pieChart|doughnutChart|ofPieChart", charts):
                fail.append(f"E3 {path.name}: pie/doughnut chart present (craft bans them)")
            if charts.count("<c:axId") > 0 and re.search(r"<c:valAx[^>]*>.*<c:valAx", charts, re.S):
                warn.append(f"E3 {path.name}: multiple value axes found; check for a dual-axis chart (craft bans them)")
        BANNED = ["elevate", "seamless", "unleash", "empower", "revolutionize", "cutting-edge",
                  "game-changing", "unlock", "赋能", "一站式", "打造", "引领", "闭环", "抓手", "颠覆"]
        text_all = " ".join(re.findall(r"<a:t>([^<]*)</a:t>", data))
        for w in BANNED:
            if w.lower() in text_all.lower():
                fail.append(f"E4 {path.name}: copy tell '{w}' present (craft, Copy blacklist)")
        n_pics = len(re.findall(r"<p:pic>", data))
        if n_pics:
            warn.append(f"E5 {path.name}: {n_pics} picture(s) present; captions and sources are not machine-verifiable — Inspect must check each against craft, Imagery")
        found = {"#" + h.lower() for h in re.findall(r'srgbClr val="([0-9A-Fa-f]{6})"', data)}
        for h in sorted(found - colors):
            fail.append(f"E1 {path.name}: color {h} is not a DESIGN.md token")
        for fam in sorted(set(re.findall(r'typeface="([^"]+)"', data))):
            base = fam.split(",")[0].strip().lower()
            if base and base not in stacks and not fam.startswith("+"):
                fail.append(f"E2 {path.name}: font '{fam}' is not in any DESIGN.md type stack")
    elif path.suffix in (".html", ".htm", ".css"):
        data = path.read_text(encoding="utf-8", errors="ignore")
        for w in ["elevate", "seamless", "unleash", "empower", "赋能", "一站式", "打造", "引领", "闭环", "抓手", "颠覆"]:
            if w.lower() in data.lower():
                fail.append(f"E4 {path.name}: copy tell '{w}' present (craft, Copy blacklist)")
        found = {h.lower() for h in HEX.findall(data)}
        for h in sorted(found - colors):
            fail.append(f"E1 {path.name}: color {h} is not a DESIGN.md token")

def main():
    if len(sys.argv) < 2:
        print(__doc__); return 2
    tokens, _ = check_design(Path(sys.argv[1]))
    for f in sys.argv[2:]:
        check_export(Path(f), tokens)
    for w in warn: print(f"WARN  {w}")
    if fail:
        for f_ in fail: print(f"FAIL  {f_}")
        print(f"\n{len(fail)} failure(s)"); return 1
    print("PASS  folio-check: all gates hold"); return 0

if __name__ == "__main__":
    sys.exit(main())
