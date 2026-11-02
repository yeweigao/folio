#!/usr/bin/env python3
"""fontcheck.py page.html "Family One" ["Family Two" ...]

Opens the page in headless Chromium and verifies each named family actually
RENDERED, by measuring a probe string on canvas: set in the family over a
generic fallback, then in the fallback alone. Different widths against every
generic fallback mean the named face drew the glyphs; identical widths mean
the browser silently substituted — the failure folio-check cannot see in
code. Exit 0 only if every named family rendered.

Requires Playwright (the render environment's Chromium).
"""
import pathlib
import sys

PROBE_JS = """
(family) => {
  const text = 'mmmmmmmmmmlliWW@#%&';
  const c = document.createElement('canvas').getContext('2d');
  const width = (stack) => { c.font = stack; return c.measureText(text).width; };
  for (const fb of ['serif', 'sans-serif', 'monospace']) {
    const withFam = width(`80px "${family}", ${fb}`);
    const plain = width(`80px ${fb}`);
    if (Math.abs(withFam - plain) > 0.5) return true;
  }
  return false;
}
"""


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    page = pathlib.Path(argv[1]).resolve()
    families = argv[2:]
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("fontcheck: Playwright is not available in this Python.")
        return 2
    failed = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        tab = browser.new_page()
        tab.goto(page.as_uri())
        tab.wait_for_timeout(600)
        for fam in families:
            loaded = tab.evaluate(PROBE_JS, fam)
            print(f"{'RENDERED' if loaded else 'FALLBACK'}  {fam}")
            if not loaded:
                failed.append(fam)
        browser.close()
    if failed:
        print(f"fontcheck: FAIL — fell back silently: {', '.join(failed)}")
        return 1
    print("fontcheck: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
