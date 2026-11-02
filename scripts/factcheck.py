#!/usr/bin/env python3
"""factcheck — the facts floor, checked against what the reader sees.

Usage:
  factcheck.py brief.md seen.txt|export.html|export.pptx

Reads the brief's `## Facts` section: every `backticked` string is a fact
that must appear in the work exactly. Compares against the rendered text
(render.py's .txt is best: it is what a reader sees) or, failing that,
the text extracted from an .html or .pptx.

  FAIL  a fact is missing
  WARN  a fact is present only after normalising case, dashes, quotes or
        spacing (a typographic change: check it was meant)
  WARN  a number in the work that appears nowhere in the brief
        (a possible invented fact: check it is derived and labelled)

Exit 0 = every fact present. Stdlib only.
"""
import re
import sys
import unicodedata
import zipfile
from html.parser import HTMLParser
from pathlib import Path


class _Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)


def seen_text(path):
    p = Path(path)
    if p.suffix == ".pptx":
        with zipfile.ZipFile(p) as z:
            xml = " ".join(z.read(n).decode("utf-8", "ignore") for n in z.namelist()
                           if n.startswith("ppt/slides/slide"))
        return " ".join(re.findall(r"<a:t>([^<]*)</a:t>", xml))
    raw = p.read_text(encoding="utf-8", errors="ignore")
    if p.suffix in (".html", ".htm"):
        t = _Text(); t.feed(raw); return " ".join(t.out)
    return raw


def squash(s):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", s)).strip()


def loose(s):
    s = squash(s).lower()
    s = re.sub(r"[‐-―−-]", "-", s)
    s = re.sub(r"[‘’‚‛'`]", "'", s)
    s = re.sub(r"[“”„«»\"]", '"', s)
    return re.sub(r"\s*([-/·,:])\s*", r"\1", s)


def main():
    if len(sys.argv) < 3:
        print(__doc__); return 2
    brief = Path(sys.argv[1]).read_text(encoding="utf-8")
    sec = brief.split("## Facts", 1)[-1].split("\n## ", 1)[0] if "## Facts" in brief else ""
    facts = re.findall(r"`([^`]+)`", sec)
    if not facts:
        print("FAIL  the brief has no `## Facts` section with backticked strings"); return 1
    text = seen_text(sys.argv[2])
    exact, lo = squash(text), loose(text)
    fails = warns = 0
    for f in facts:
        if squash(f) in exact:
            continue
        if loose(f) in lo:
            print(f"WARN  typographic change: {f}"); warns += 1
        else:
            print(f"FAIL  missing: {f}"); fails += 1
    nums = lambda s: set(re.findall(r"\d+(?:[.,:]\d+)*", s))
    extra = sorted(nums(text) - nums(brief), key=lambda n: (len(n), n))
    if extra:
        print("WARN  numbers not in the brief: " + ", ".join(extra[:40]))
        warns += 1
    print(f"\n{len(facts)} facts · {fails} missing · {warns} warning(s)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
