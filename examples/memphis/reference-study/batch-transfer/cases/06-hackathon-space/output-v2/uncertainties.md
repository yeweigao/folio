# Unspecified decisions

- The brief gives no pairing between cities and dates. All four cities share one front face, and both dates share a separate pane; no city/date relationship is implied.
- BUILD-ATHON is broken after its supplied hyphen into two live title lines. The second line is indented within the same paper face.
- The title stack retreats up and left; the date stack retreats up and right. The arrangement, overlap order, and exact solid directions were composed for this 900 × 1200 portrait format.
- The remote-team message occupies the block’s yellow top plane with a single affine projection. The city codes occupy its green front plane.
- No separate organization logo was supplied. “stripe” is live ordinary-width bold type on the title pane.
- The fluorescent disc, cylinder, city block, and cut burst are drawn from native vector geometry. They carry no additional factual meaning.
- Typography and stroke tokens use a 0.9 scale from the reference short side of 1000.

# Own verification

- Rendered `poster.svg` with headless Google Chrome at its native 900 × 1200 dimensions, then visually inspected `preview.png`.
- The required front text is visible; the projected remote-team message remains complete on the top plane.
- Chrome reports embedded Study Condensed 700, Study Sans 400, and Study Sans 700 loaded. The neutral utility also embedded the unused Study Sans 900 face.
- `qa.json` records native text content, font sizes, bounding rectangles, dimensions, and embedded-face count.

# Access inventory

Read inputs:

- `input-v2/DESIGN.md` (full)
- `input-v2/brief.md` (full)
- `input-v2/TECHNICAL.md` (full)
- `input-v2/embed_fonts.py` (full; run only for font embedding)
- `input-v2/fonts/` (directory filenames)
- `input-v2/fonts/Oswald-700.ttf` (metrics and embedding)
- `input-v2/fonts/Inter-400.ttf` (metrics and embedding)
- `input-v2/fonts/Inter-700.ttf` (embedding)
- `input-v2/fonts/Inter-900.ttf` (embedding)

Own output:

- `output-v2/generate.py`
- `output-v2/raw.svg`
- `output-v2/poster.svg`
- `output-v2/uncertainties.md`
- `output-v2/render.cjs`
- `output-v2/preview.png`
- `output-v2/qa.json`

Generic installed tools/libraries:

- `/private/tmp/folio-memphis-tools/bin/python` and standard library
- Pillow (font metrics)
- fontTools and brotli (neutral font subset embedding)
- `/opt/homebrew/bin/node` and standard library
- `/Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright`
- `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`
