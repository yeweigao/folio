# Production decisions and uncertainties

- The written world is the only visual authority. No old artwork, other case, reference, evaluation, or other skill was consulted.
- The short edge is 900 px, so the 1000-based tokens use a 0.9 scale: the base module is 150 px; the two Chinese display sizes are 99 px at 900 weight and 93.6 px at 300 weight. Normal-width Latin uses Inter at 37.8 px, with the English explanation wrapping after the comma.
- The main reading district occupies four by three base modules. The separate yellow participation district occupies four by one modules. A half-module-height stripe band supplies the permitted half-step. The relative positions are original production choices.
- Visible ink, rather than font em boxes, determines the shared left edge and the 16 px space between the Chinese display lines. All reading is dark ink on paper or yellow, with at least 23.4 px ink clearance from district edges.
- The prescribed chevron height, width, arm thickness and exact right-angle tip do not give one unique construction. This drawing preserves the 105 px outer height, 33 px perpendicular arm thickness and right-angle tip; its straight horizontal tail cuts result in a 99.17 px outer width, slightly wider than the nominal 93 px.
- The pink circle is a complete 300 px circle crossing exactly the purple/green seam. Window grids keep a 37.5 px center pitch and 6.75 px strokes, including the larger lower grid. Diagonal bars keep 18 px perpendicular widths and 36 px perpendicular periods.

# Self-verification

- Generated `raw.svg` and then embedded font subsets with the unchanged supplied `embed_fonts.py`.
- Parsed the final SVG: 900 × 1200 dimensions, all eight live text nodes and every supplied fact present, four embedded font faces, no raster images.
- Rendered `poster.svg` in headless Chrome using generic Playwright. All four embedded font faces reported loaded. Inspected the 900 × 1200 screenshot for complete text, layout, letter weight, circle and pattern clipping. The rendering and browser text metrics are retained as `self-check.png` and `self-check.json`.
- No independent review result has been consulted or used to revise this output.

# Exact input file content read inventory

- `input-v2/DESIGN.md` — complete.
- `input-v2/brief.md` — complete.
- `input-v2/TECHNICAL.md` — complete.
- `input-v2/embed_fonts.py` — complete and executed unchanged.
- `input-v2/fonts/Inter-400.ttf` — font metrics and embedding.
- `input-v2/fonts/Inter-700.ttf` — font metrics and embedding.
- `input-v2/fonts/Inter-900.ttf` — font metrics and embedding.
- `input-v2/fonts/NotoSansSC-variable.ttf` — font metrics and embedding.

The directory names of all files in `input-v2/fonts/` were listed. The contents of the other font files and OFL text files were not read.
