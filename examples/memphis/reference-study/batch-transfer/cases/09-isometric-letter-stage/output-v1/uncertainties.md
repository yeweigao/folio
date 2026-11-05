# Decisions not fixed by DESIGN.md

- The short brief supplies no factual hierarchy beyond the event name. The event is the largest text; the date and slogan occupy a raised rear tier; the four artists use a shared size and paired reading order.
- The poster uses a yellow field. The two faces of the title bridge both use paper, with a black top deck and three structural piers. The open spans are deliberate geometry, not shadows.
- The two projected horizontal axes are `(1, 0.425)` and `(1, -0.425)`; verticals remain vertical. All walls and roofs are constructed in world coordinates before projection.
- `OPEN AIR` is split into two live lines on its own face. Every artist is one line. `KONBIN STAGE` is split at its word space between the two continuous title faces, with equal cap height.
- Oswald 700 (Study Condensed) is used for all visible type. The supplied utility embeds the supplied font subsets. No assertion is made about the unknown original typeface.
- Original-output color pairs: yellow/ink, yellow/blue, ink/green, ink/paper. No small paper/green text is used.
- No reference or earlier artwork was read. This is an independent interpretation of the unchanged supplied DESIGN.md.

# Self-verification

- Rendered the final embedded SVG in headless Google Chrome at 900 × 1200. Study Condensed loaded from the embedded data font. Inspected the rendered image at full size.
- Parsed the SVG to confirm the exact facts remain live text, including the semantic `OPEN AIR` line break; no raster image or outlined type is used.
- Verified all 23 colored faces are parallelograms, with opposite vertices matching and every edge either vertical or at slope ±0.425.
- Calculated actual glyph ink bounds from the supplied Oswald font and confirmed every visible glyph stays inside its assigned wall.
- Confirmed six embedded WOFF2 font faces. Unused supplied faces are embedded but are not loaded by Chrome.
- The initial complete SVG, raw SVG, generator and render are retained in `first-complete/`. Self-QA changed the roof subdivisions into strict parallelograms and inserted a semantic space between OPEN and AIR; the silhouette and hierarchy remained the same.
