# Decisions where the inputs left room

- The brief fixes the eight facts and the 900 × 1200 canvas, but leaves their positions and the number of building volumes open. I chose a stepped stage: the date and venue form the crown, the four artists occupy two structural tiers, and the event name forms a continuous white foreground beam.
- The input gives the two projection slopes but no world-space dimensions. All volumes were drawn from one projection, `(400 + x − y, 625 + 0.425(x + y) − z)`. Shared corners are computed once per block; no images, pre-projected artwork, shadows, or clipped lettering are used.
- The exact color assignment is open. Yellow is the field; the title uses ink on paper; artists use the permitted yellow-on-blue and ink-on-green pairs. Red is reserved for empty roofs and one foundation face.
- The title is split only between KONBIN and STAGE. OPEN AIR wraps at its space. Date, slogan, and each artist remain intact. No year, address, time, ticket details, or other event facts were supplied or invented.
- Type sizes are calculated from the supplied Oswald 700 font's advances, with approximately 3% face-width safety margins. The unequal title face widths give KONBIN and STAGE similar cap heights; artist face widths likewise follow the lengths of the names.
- English-only content needs no CJK glyphs. Study Condensed / Oswald 700 is subset-embedded in the final SVG with the supplied neutral utility.

# Self-check

- Rendered the final SVG in headless Chrome at 900 × 1200 and viewed `preview.png`.
- Chrome confirmed that the embedded Study Condensed font loaded.
- Parsed the final SVG and checked all eight facts, nine live text elements, canvas dimensions, native geometry, and embedded font data.
- Measured actual glyph outlines against every assigned face; all visible ink remains within its face. Details are in `qa.json`.
