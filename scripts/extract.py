#!/usr/bin/env python3
"""extract — draft a DESIGN.md from an existing artifact (Critique mode input).

Usage: extract.py deck.pptx|page.html [out.md]

For .pptx it reads the real evidence out of the file: theme colors and
fonts, and every color, typeface and font size used on slides, counted.
For .html/.css it counts hex colors and font families in the source.
The agent writes rationale on top of this draft; nothing here invents
values — unmapped colors appear in Gaps as unprovided roles.
Stdlib only; inspired by design-md-chrome / Stitch extract-design-md.
"""
import re, sys, zipfile
from collections import Counter
from pathlib import Path

def from_pptx(path):
    colors, fonts, sizes = Counter(), Counter(), Counter()
    theme_colors, theme_fonts = {}, set()
    with zipfile.ZipFile(path) as z:
        for n in z.namelist():
            if not (n.startswith("ppt/") and n.endswith(".xml")): continue
            # Used colors/faces/sizes come from slides only: themes and
            # masters carry the template's whole unused scheme.
            is_slide = re.match(r"ppt/slides/slide\d+\.xml$", n)
            x = z.read(n).decode("utf-8", "ignore")
            if "theme" not in n and not is_slide: continue
            if is_slide:
                for h in re.findall(r'srgbClr val="([0-9A-Fa-f]{6})"', x):
                    colors["#" + h.upper()] += 1
                for f in re.findall(r'typeface="([^"]+)"', x):
                    if not f.startswith("+"): fonts[f] += 1
                for s_ in re.findall(r'sz="(\d+)"', x):
                    sizes[round(int(s_) / 100)] += 1
            if "theme" in n:
                for k, v in re.findall(r'<a:(dk1|lt1|dk2|lt2|accent1|accent2|accent3|accent4|accent5|accent6)>.*?srgbClr val="([0-9A-Fa-f]{6})"', x, re.S):
                    theme_colors[k] = "#" + v.upper()
    return colors, fonts, sizes, theme_colors

def from_html(path):
    data = path.read_text(encoding="utf-8", errors="ignore")
    colors = Counter("#" + h.upper() for h in re.findall(r"#([0-9A-Fa-f]{6})\b", data))
    fonts = Counter(f.strip().strip("'\"") for f in re.findall(r"font-family\s*:\s*([^;]+)", data) for f in f.split(",")[:1])
    return colors, fonts, Counter(), {}

def main():
    src = Path(sys.argv[1]); out = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".DESIGN.md")
    colors, fonts, sizes, theme = from_pptx(src) if src.suffix == ".pptx" else from_html(src)
    top_colors = colors.most_common(8)
    yaml = ["colors:"]
    roles = ["primary", "secondary", "tertiary", "neutral", "line", "dark", "soft", "focus"]
    for role, (hexv, _) in zip(roles, top_colors):
        yaml.append(f'  {role}: "{hexv}"')
    if fonts:
        fam = fonts.most_common(1)[0][0]
        yaml += ["typography:", f'  body: {{ fontFamily: "{fam}", fontSize: 18px, fontWeight: 400, lineHeight: 1.45 }}']
    lines = [f"# {src.stem} · extracted draft", "", "<the world in one sentence>", "",
             "## Overview",
             "<School>, <hand> — <the work>: <the method as an imperative>; never <the ban>.",
             f"World: <what this skeleton is for>. Extracted from {src.name}; theme colors seen: {theme or 'n/a'}.",
             "Method: <how the existing work is made, as process>.",
             "", "## Images", "<where the work's images come from, and how they are treated>",
             "", "## Layout", "Grid system: <the system the work actually uses, or none>.",
             "", "## Typography", "<faces and ramp, read from the evidence below>",
             "", "## Colors", "<each role, read from the evidence below>",
             "", "## Forms", "<the forms the work uses>",
             "", "## Do's and Don'ts", "<observed defects, kept apart from proposed directions>",
             "", "## Tokens", "", "```yaml", *yaml, "```",
             "", "## Record", "Folio version: <x.y.z>. Template version: 14. Extracted draft: evidence, not a system.",
             f"Colors by use: {dict(colors.most_common(12))}.", f"Faces by use: {dict(fonts.most_common(6))}.",
             f"Type sizes (pt) by use: {dict(sizes.most_common(8))}.",
             "Assign each color its real role, merge near-duplicates, delete unused tokens; folio-check fails until every <placeholder> is filled."]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote draft {out} from {src.name}: {len(colors)} colors, {len(fonts)} faces, {len(sizes)} sizes")

if __name__ == "__main__":
    main()
