# Verification

- Parsed poster.svg as XML and confirmed 900 × 1200 dimensions and matching viewBox.
- Asserted the ten brief facts in live SVG text. The event name and slogan use semantic line breaks.
- Confirmed six embedded WOFF2 font faces and no external image, font, or linked-asset references.
- Rendered poster.svg at native dimensions in local headless Google Chrome through Playwright; inspected poster.png.
- Inspected all content for clipping and overlap. All supplied facts were visible.
- The initial browser launch was blocked by the filesystem sandbox. The same local rendering command succeeded with the required sandbox escalation.
- No changes were made after the first complete SVG was rendered.
