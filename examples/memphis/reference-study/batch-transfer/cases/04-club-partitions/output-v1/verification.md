# Verification performed

- Parsed `poster.svg` as XML and verified exact 900 × 1200 dimensions.
- Verified all 11 supplied facts occur in live SVG text elements (normalizing whitespace in the two-line title).
- Verified six embedded WOFF2 font faces and no image elements.
- Rendered `poster.svg` in headless local Chrome with Playwright at 900 × 1200.
- Inspected `preview.png`; all fixed information is visible, artist panels are unobstructed, and no text is clipped by the frame.
- Captured live browser text bounding boxes and font status in `self-check.json`. The used Study Sans regular and bold faces loaded.
- The first complete artifact is preserved in `first-complete/`; no visual changes followed self-QA.
- No external reference or aesthetic review was consulted.
