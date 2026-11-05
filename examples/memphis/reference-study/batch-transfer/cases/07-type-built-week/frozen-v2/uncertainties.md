# Production decisions

- The brief does not mandate title line breaks. The four semantic rows are TAIPEI / DESIGN / WEEK / 2027, with the programme and event facts below.
- The document gives relative scales. I used a 28 px side margin and tuned each display row horizontally to the same 844 px ink width; all reading text retains its original proportions.
- The D counter contains the blue/purple diagonal square. The first E in WEEK has its middle arm replaced by three adjoining horizontal color strokes. A solid orange-glyph circle replaces the zero in 2027.
- The brief gives host and partner names without requiring printed role labels. They share the lowest baseline, in the supplied host/partner order.
- No external imagery, facts, references, or supplementary typefaces were used.

# Access inventory

Read: input-v2/DESIGN.md; input-v2/brief.md; input-v2/TECHNICAL.md; input-v2/embed_fonts.py; input-v2/fonts directory listing; input-v2/fonts/Inter-900.ttf. Font embedding also reads Inter-400.ttf and Inter-700.ttf through the supplied neutral helper.

Created/read: output-v2/generate.py, output-v2/raw.svg, output-v2/poster.svg, output-v2/uncertainties.md. Self-rendering created and inspected output-v2/preview.png and output-v2/qa.json. Generic libraries used: fontTools, Python standard library, Playwright and Google Chrome. No other artwork, design files, skills, cases, evaluations or reference assets were accessed.

# Verification

- SVG parsed successfully; canvas is 900 × 1200.
- All 13 supplied fixed facts are present as live SVG text.
- Three Study Sans weights are embedded as data-URL WOFF2 faces.
- No raster images or external asset references are present.
- The poster was rendered in headless Google Chrome, fonts reported loaded, and the full-canvas PNG was visually inspected.
