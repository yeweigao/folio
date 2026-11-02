#!/usr/bin/env python3
"""preview — generate a token catalog from a DESIGN.md.

Usage: preview.py DESIGN.md [out-dir]
Writes preview.html (paper field), preview-dark.html (dark field) and
tokens.css (CSS custom properties) into out-dir (default: DESIGN.md's folder).
Stdlib only; borrows VoltAgent awesome-design-md's preview.html convention.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from folio_lib import parse_front_matter, resolve, contrast

def esc(s): return str(s).replace("&", "&amp;").replace("<", "&lt;")

def catalog(tokens, dark=False):
    colors = tokens.get("colors", {}); typo = tokens.get("typography", {})
    comps = tokens.get("components", {})
    ground = colors.get("dark", "#141414") if dark else colors.get("neutral", "#FFFFFF")
    ink = colors.get("neutral", "#FFFFFF") if dark else colors.get("primary", "#111111")
    sw = "".join(f'<div class="sw"><i style="background:{esc(v)}"></i><b>{esc(k)}</b><span>{esc(v)}</span></div>'
                 for k, v in colors.items() if str(v).startswith("#"))
    ty = "".join(f'<p style="font-family:{esc(t.get("fontFamily",""))};font-size:{esc(t.get("fontSize",""))};font-weight:{esc(t.get("fontWeight",""))};line-height:{esc(t.get("lineHeight",""))}">{esc(k)} — The quick brown fox 敏捷的棕色狐狸 0123456789 · 1,234.5% — “quotes” 《标题》</p>'
                 for k, t in typo.items() if isinstance(t, dict))
    pairs = ""
    for k, c in comps.items():
        if not isinstance(c, dict) or not c.get("textColor"): continue
        bg, fg = resolve(c.get("backgroundColor", ""), tokens), resolve(c.get("textColor", ""), tokens)
        r = contrast(fg, bg) if str(bg).startswith("#") and str(fg).startswith("#") else None
        pairs += f'<div class="pair" style="background:{esc(bg)};color:{esc(fg)}">{esc(k)} — text on its ground{f" · {r:.1f}:1" if r else ""}</div>'
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>{esc(tokens.get('name','DESIGN'))} — token catalog{'(dark)' if dark else ''}</title>
<style>body{{background:{ground};color:{ink};font-family:Inter,'Source Han Sans SC',sans-serif;margin:48px}}
.grid{{display:flex;flex-wrap:wrap;gap:16px}}.sw i{{display:block;width:120px;height:56px;border:1px solid #8884}}
.sw b,.sw span{{display:block;font-size:12px}}.pair{{padding:16px;margin:8px 0}}</style></head>
<body><h1>{esc(tokens.get('name','DESIGN'))}</h1><p>{esc(tokens.get('description',''))}</p>
<h2>Colors</h2><div class="grid">{sw}</div><h2>Typography</h2>{ty}<h2>Component pairs</h2>{pairs}
</body></html>"""

def main():
    md = Path(sys.argv[1]); out = Path(sys.argv[2]) if len(sys.argv) > 2 else md.parent
    out.mkdir(parents=True, exist_ok=True)
    tokens, _ = parse_front_matter(md.read_text(encoding="utf-8"))
    (out / "preview.html").write_text(catalog(tokens), encoding="utf-8")
    (out / "preview-dark.html").write_text(catalog(tokens, dark=True), encoding="utf-8")
    css = ":root{\n" + "".join(f"  --{sec}-{k}: {v};\n" for sec in ("colors", "spacing", "rounded")
                               for k, v in tokens.get(sec, {}).items() if not isinstance(v, dict)) + "}\n"
    (out / "tokens.css").write_text(css, encoding="utf-8")
    print(f"wrote preview.html, preview-dark.html, tokens.css to {out}")

if __name__ == "__main__":
    main()
