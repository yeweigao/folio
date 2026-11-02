#!/usr/bin/env python3
"""folio-check — deterministic gates for a skeleton and its exports.

Usage:
  folio-check.py DESIGN.md [export.html|export.pptx ...]

Skeleton (DESIGN.md):
  S1 a ## Tokens section with a yaml block holding colors and typography
  S2 the sections a skeleton needs: Overview, Images, Layout, Typography,
     Colors, Forms, Do's and Don'ts, Tokens, Record
  S3 no template placeholders left (<...>) anywhere in the file
  S4 the Overview opens with an invocation line and names World and Method
  S5 Layout names its grid system
  S6 Record names the Folio version and the template version
  S7 sizes are relative: the file states its reference (S = <n>)
  T1 every pair reference resolves; every color is used by a
     component or named in the prose
  T2 text pairs meet 4.5:1 (append "-large" to a pair's
     name to hold it to the 3:1 large-text floor instead)

Exports (when given):
  E1 every color in the export is a declared token
     (#rgb, #rrggbb, #rrggbbaa, rgb()/rgba(); pptx srgbClr and theme colors used)
  E2 every font family in the export appears in a type stack
  E3 no pie or doughnut charts in a pptx (dual axes warn)
  E4 no copy tells from craft's blacklist in the visible text
  E5 pictures present: captions and sources need a human check (warning)

Exit 0 = pass, 1 = failures listed. Stdlib only.
"""
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from folio_lib import parse_tokens, resolve, contrast

fail, warn = [], []
GENERIC = {"serif", "sans-serif", "monospace", "system-ui", "cursive", "fantasy",
           "ui-sans-serif", "ui-serif", "ui-monospace", "inherit", "initial", "-apple-system",
           "blinkmacsystemfont"}
TELLS = ["elevate", "seamless", "unleash", "empower", "revolutionize", "cutting-edge",
         "game-changing", "赋能", "一站式", "打造", "引领", "闭环", "抓手", "颠覆"]


def section(prose, name):
    m = re.search(r"^## " + re.escape(name) + r"\s*$(.*?)(?=^## |\Z)", prose, re.S | re.M)
    return m.group(1) if m else None


def check_design(path):
    text = Path(path).read_text(encoding="utf-8")
    tokens, prose = parse_tokens(text)
    if not tokens or "colors" not in tokens or "typography" not in tokens:
        fail.append("S1 no ## Tokens yaml block with colors and typography")
        return tokens or {}
    for s in ("Overview", "Images", "Layout", "Typography", "Colors", "Forms", "Do's and Don'ts", "Tokens", "Record"):
        if section(text, s) is None:
            fail.append(f"S2 missing section ## {s}")
    holes = re.findall(r"<[^<>\n]{2,80}>", text)
    holes = [h for h in holes if not re.match(r"</?[a-z][a-z0-9]*[\s>/]", h + ">")]
    if holes:
        fail.append(f"S3 template placeholders left: {', '.join(sorted(set(holes))[:5])}")
    ov = section(prose, "Overview") or ""
    first = next((l for l in ov.strip().splitlines() if l.strip()), "")
    if not re.search(r"\b(make|set|build|draw|compose|work)\b", first, re.I) or len(first) < 40:
        fail.append("S4 Overview does not open with an invocation (school, hand, work, method as an imperative, ban)")
    for label in ("World:", "Method:"):
        if label not in ov:
            fail.append(f"S4 Overview has no '{label}' line")
    if not re.search(r"grid system:\s*\S+", section(prose, "Layout") or "", re.I):
        fail.append("S5 Layout does not name its grid system ('Grid system: …')")
    if not re.search(r"\bS\s*=\s*\d+", text):
        fail.append("S7 no reference format stated ('S = 1000'): sizes must derive from the format")
    rec = section(prose, "Record") or ""
    if not re.search(r"folio version:?\s*\d+\.\d+", rec, re.I):
        fail.append("S6 Record does not name a Folio version")
    if not re.search(r"template version:?\s*\d+", rec, re.I):
        fail.append("S6 Record does not name a template version")

    colors = tokens.get("colors", {})
    comps = tokens.get("pairs", {}) or {}
    used = set()
    for name, c in comps.items():
        if not isinstance(c, dict):
            continue
        for key in ("backgroundColor", "textColor"):
            ref = str(c.get(key, ""))
            m = re.fullmatch(r"\{colors\.([\w-]+)\}", ref)
            if m:
                used.add(m.group(1))
                if m.group(1) not in colors:
                    fail.append(f"T1 pair {name} refers to missing color {m.group(1)}")
            elif ref.startswith("{"):
                fail.append(f"T1 pair {name} has an unresolvable reference {ref}")
        bg = resolve(c.get("backgroundColor", ""), tokens)
        fg = resolve(c.get("textColor", ""), tokens)
        if bg and fg and str(bg).startswith("#") and str(fg).startswith("#"):
            r = contrast(fg, bg)
            floor = 3.0 if name.endswith("-large") else 4.5
            if r and r < floor:
                fail.append(f"T2 pair {name}: {fg} on {bg} is {r:.2f}:1 (< {floor}:1)")
    low = prose.lower()
    for cname, cval in colors.items():
        if cname not in used and str(cval).lower() not in low and cname.lower() not in low:
            fail.append(f"T1 color '{cname}' is declared but never used or named")
    return tokens


def norm_hex(h):
    h = h.lower().lstrip("#")
    if len(h) in (3, 4):
        h = "".join(ch * 2 for ch in h[:3])
    return "#" + h[:6]


def rgb_to_hex(r, g, b):
    return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))


def stacks_of(tokens):
    fams = set()
    for t in (tokens.get("typography") or {}).values():
        if isinstance(t, dict):
            for f in str(t.get("fontFamily", "")).split(","):
                f = f.strip().strip("'\"").lower()
                if f:
                    fams.add(f)
    return fams


def check_export(path, tokens):
    declared = {norm_hex(v) for v in (tokens.get("colors") or {}).values() if str(v).startswith("#")}
    fams = stacks_of(tokens)
    if path.suffix == ".pptx":
        with zipfile.ZipFile(path) as z:
            names = z.namelist()
            slides = " ".join(z.read(n).decode("utf-8", "ignore") for n in names
                              if n.startswith(("ppt/slides/slide", "ppt/charts/chart")))
            charts = " ".join(z.read(n).decode("utf-8", "ignore") for n in names if n.startswith("ppt/charts/chart"))
            theme = " ".join(z.read(n).decode("utf-8", "ignore") for n in names if n.startswith("ppt/theme/theme"))
        scheme = {k: "#" + v.lower() for k, v in re.findall(
            r"<a:(dk1|lt1|dk2|lt2|accent\d|hlink|folHlink)>\s*<a:srgbClr val=\"([0-9A-Fa-f]{6})\"", theme)}
        found = {"#" + h.lower() for h in re.findall(r'srgbClr val="([0-9A-Fa-f]{6})"', slides)}
        alias = {"tx1": "dk1", "bg1": "lt1", "tx2": "dk2", "bg2": "lt2"}
        for s in set(re.findall(r'schemeClr val="(\w+)"', slides)):
            s = alias.get(s, s)
            if s in scheme:
                found.add(scheme[s])
        for h in sorted(found - declared):
            fail.append(f"E1 {path.name}: color {h} is not a declared token")
        for fam in sorted(set(re.findall(r'typeface="([^"+][^"]*)"', slides))):
            if fam.strip().lower() not in fams:
                fail.append(f"E2 {path.name}: font '{fam}' is not in any type stack")
        if re.search(r"pieChart|doughnutChart|ofPieChart", charts):
            fail.append(f"E3 {path.name}: pie or doughnut chart")
        if len(re.findall(r"<c:valAx>", charts)) > 1:
            warn.append(f"E3 {path.name}: more than one value axis; check for a dual-axis chart")
        text = " ".join(re.findall(r"<a:t>([^<]*)</a:t>", slides))
        n_pics = len(re.findall(r"<p:pic>", slides))
    else:
        data = path.read_text(encoding="utf-8", errors="ignore")
        found = set()
        for h in re.findall(r"(?<![&\w])#[0-9A-Fa-f]{3,8}\b", data):
            if len(h) - 1 in (3, 4, 6, 8):
                found.add(norm_hex(h))
        for r, g, b in re.findall(r"rgba?\(\s*([\d.]+)[\s,]+([\d.]+)[\s,]+([\d.]+)", data):
            found.add(rgb_to_hex(r, g, b))
        for h in sorted(found - declared):
            fail.append(f"E1 {path.name}: color {h} is not a declared token")
        css_fams = set()
        for decl in re.findall(r"font-family\s*:\s*([^;}\"]+)", data):
            for f in decl.split(","):
                f = f.strip().strip("'\"").lower()
                if f and not f.startswith("var("):
                    css_fams.add(f)
        for fam in re.findall(r"fonts\.googleapis\.com/css2?\?([^\"'>]+)", data):
            for part in re.findall(r"family=([^:&]+)", fam):
                css_fams.add(part.replace("+", " ").lower())
        for f in sorted(css_fams - fams - GENERIC):
            fail.append(f"E2 {path.name}: font '{f}' is not in any type stack")
        body = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", data, flags=re.S | re.I)
        text = re.sub(r"<[^>]+>", " ", body)
        n_pics = len(re.findall(r"<img\b", data, re.I))
    for w in TELLS:
        if re.search(r"(?<![\w-])" + re.escape(w) + r"(?![\w-])", text, re.I):
            fail.append(f"E4 {path.name}: copy tell '{w}'")
    if n_pics:
        warn.append(f"E5 {path.name}: {n_pics} picture(s); check each caption and source by eye")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    tokens = check_design(Path(sys.argv[1]))
    for f in sys.argv[2:]:
        check_export(Path(f), tokens)
    for w in warn:
        print(f"WARN  {w}")
    for f in fail:
        print(f"FAIL  {f}")
    if fail:
        print(f"\n{len(fail)} failure(s)")
        return 1
    print("PASS  folio-check: all gates hold")
    return 0


if __name__ == "__main__":
    sys.exit(main())
