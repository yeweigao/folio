#!/usr/bin/env python3
"""render — see the work, not the file that describes it.

Usage:
  render.py page.html [out-dir]

Loads the page in Chromium (Playwright), waits for fonts and the network,
then writes one PNG per element with class `unit` (the whole page when
there is none) and <stem>.txt: the text a reader actually sees, as
rendered (CSS text-transform applied, SVG <text> included). That text
file is what factcheck.py reads.

Needs: pip install playwright (with its Chromium). Every other Folio
script stays stdlib-only; seeing is worth one dependency.
"""
import sys
from pathlib import Path


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    page_path = Path(sys.argv[1]).resolve()
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else page_path.parent / "render"
    out.mkdir(parents=True, exist_ok=True)
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 2000, "height": 1200})
        try:
            page.goto(page_path.as_uri(), wait_until="networkidle", timeout=30000)
        except Exception:
            page.goto(page_path.as_uri(), wait_until="load")
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(500)
        units = page.query_selector_all(".unit")
        shots = []
        if units:
            for i, u in enumerate(units, 1):
                f = out / f"{page_path.stem}-{i:02d}.png"
                u.screenshot(path=str(f))
                shots.append(f)
        else:
            f = out / f"{page_path.stem}-01.png"
            page.screenshot(path=str(f), full_page=True)
            shots.append(f)
        text = page.evaluate(
            """() => {
              const svg = [...document.querySelectorAll('svg text')]
                .map(t => t.textContent).join('\\n');
              return document.body.innerText + '\\n' + svg;
            }"""
        )
        fonts = page.evaluate(
            """() => [...document.fonts].filter(f => f.status === 'loaded')
                 .map(f => f.family.replace(/["']/g, '') + ' ' + f.weight)"""
        )
        (out / f"{page_path.stem}.txt").write_text(text, encoding="utf-8")
        browser.close()
    for s in shots:
        print(s)
    print(f"text: {out / (page_path.stem + '.txt')}")
    print("fonts loaded: " + (", ".join(sorted(set(fonts))) or "none (system fallbacks)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
