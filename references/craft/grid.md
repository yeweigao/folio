# Grid

The grid is a contract: it fixes how things relate before deciding what they look like. Without one, an AI layout falls back to equal thirds and centered stacks.

## Five numbers

Columns, gutter, margin, baseline, content width, with content = n × column + (n − 1) × gutter. Solve the column from the format: column = (content − (n − 1) × gutter) ÷ n; the left edge of column k (from 0) is margin + k × (column + gutter).

| Surface | Format | Columns | Gutter | Margin | Baseline |
|---|---|---|---|---|---|
| Slides | 1280 × 720 | 12 × 73 | 24 | 70 | 8 px |
| Web | content 1296 at a 1440 viewport, capped at 1440 | 12 | 24 | 5vw, min 24 | 8 px |
| A4 handbook | 210 × 297 mm | 6 tracks (12 to subdivide) | 6 mm | 18 / 21 / 19 / 15 mm | 21 pt (28 px) |
| A2 poster | 420 × 594 mm | 12 × 23 | 8 mm | 28 mm | 8 mm |
| Canvas | infinite | 12 inside a frame | 20 | 50 | 8 pt |

The same formula covers variants: A3 poster 12 × 15.92 + 11 × 6 ≈ 257; A4 poster 6 × 25 + 5 × 6 = 180; A5 handbook 6 × 14.5 + 5 × 6 = 117; A4 handbook 6 × 24.33 + 5 × 6 = 176.

## Using twelve columns

- Spans 12 / 8 / 6 / 4 / 3. Every unit has one dominant element spanning 6 or 12.
- Asymmetry carries hierarchy: 8 + 4, 7 + 5, 6 + 4 + 2 all beat 6 + 6. Equal thirds only when the content is truly equal, and then vary height or density.
- Leave one or two columns free of text on reading units: that empty column is what makes the page breathe.
- Image edges, title starts, captions, and source lines share column lines. Rules sit on grid lines; images and rules end on the baseline.

## Optical alignment

Round and pointed forms (O, circles, triangles) overshoot by 1–2% to look aligned; quotation marks and periods may hang into the margin; very large titles may sit 1–2 px left of the text edge to compensate for side bearing.

## Breaks

A deliberate break (bleed, rotation, overprint, crop) happens at most once per unit, its origin still on a grid intersection, and never moves body text off its columns and baseline. Everything else returns to the default, so the break reads as intentional.

## Responsive and infinite

Web columns collapse 12 → 8 → 6 → 4 at 1024 / 768 / 480 and remain identifiable; use `repeat(12, minmax(0, 1fr))` and no `100vw`. Breakpoints are where the content starts to look wrong, not device names. On a canvas, frames sit on an 8 pt grid, groups are made by distance, and connectors run orthogonally.
