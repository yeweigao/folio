---
version: alpha
name: The Grid, evening series of the Museum of Design · Swiss, ma 間 (Kenya Hara)
description: Posters and print for a museum's evening series on the systems behind modern design, set in one soft ink on a cool white stock, with the white itself as the subject.
colors:
  primary: "#20242A"
  secondary: "#5C626B"
  neutral: "#F3F4F2"
typography:
  display: { fontFamily: "Source Serif 4, Noto Serif SC, serif", fontSize: 88, fontWeight: 300, lineHeight: 1 }
  display-zh: { fontFamily: "Noto Serif SC, Source Serif 4, serif", fontSize: 80, fontWeight: 200, lineHeight: 1.15 }
  title: { fontFamily: "Source Serif 4, Noto Serif SC, serif", fontSize: 56, fontWeight: 300, lineHeight: 1.1 }
  body: { fontFamily: "Hanken Grotesk, Noto Sans SC, sans-serif", fontSize: 30, fontWeight: 400, lineHeight: 1.4 }
  label: { fontFamily: "Hanken Grotesk, Noto Sans SC, sans-serif", fontSize: 22, fontWeight: 400, lineHeight: 1.45 }
spacing:
  module: 71.4
  margin: 71.4
  ladder: 214
  group: 16
rounded:
  none: 0
components:
  ink-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.primary}" }
  muted-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.secondary}" }
---

## Overview

Swiss, ma 間 — Kenya Hara's *White* (2008) and the paper works: make the stock and the interval the medium, set a few lines of Song and quiet sans where the white is most felt, and let equal intervals of white do the measuring; never draw a horizon, a stone, a paper grain or any object in code.

World: The Grid, the Museum of Design's evening series on the systems behind modern design. Two or three talks, a foyer poster exhibition, Chinese and English of equal status. One evening's facts live in its brief.

Method:
1. Stock first: uncoated cool white (`neutral`), one soft graphite ink (`primary`), one muted tone (`secondary`). No accent.
2. Modules: M = width ÷ 14 across, height ÷ round(height ÷ M) down (1000 × 1414 is 14 × 20, M ≈ 71 px). One module is the margin; one module down is 15 minutes.
3. Keep one large interval whole: the 4-module field left of module 7, between title block and colophon.
4. Ladder, not list: talk top row = 6 + (start − first start) ÷ 15 min. A 45-minute pitch is 3 modules of equal white.
5. Hang everything from three axes (L = module 1, T = module 5, C = module 7); set type last, never below the floors.
6. A real photograph switches to Horizon (Variations); without one, interval and type are the image.

Amplitude: Reduced. Few wide size steps (none below 1.35), ink and one muted tone, motion only down the ladder.

Anti-reference: The template timetable poster (bold title, coloured band, three equal cards, tracked small capitals) and the Zen costume (stones, bamboo, brush ink, rendered bowl on beige).

## Colors

- **neutral `#F3F4F2`**: the ground, at least 90% of the sheet; cool uncoated white for night windows. Touches every foreground.
- **primary `#20242A`**: graphite ink for display, talk titles, names, every fact (14.1:1). Never a field.
- **secondary `#5C626B`**: times and the status line (5.6:1). Never carries a fact alone.
- No accent, no line colour; a new accent needs this file changed first.

## Typography

Faces from Google Fonts (OFL 1.1); fallbacks Noto Serif CJK SC, Noto Sans CJK SC, then system serif and sans.

- **Display and titles: Source Serif 4 weight 300 with Noto Serif SC 300 (200 for display-zh).** Open Song cut with light weights; display-zh runs 80 px against 88 px Latin to read as one size.
- **Body and label: Hanken Grotesk 400 with Noto Sans SC 400.** Weight 400 for distance; the lightness lives in the serif.
- **Ramp: 88, 56, 30, 22 px** at a 1000 px master (A1, 1 px = 0.594 mm, seen at 2–5 m). Title cap height 59 px = 35 mm, over the 25 mm floor. Never below 22 px (13 mm). Other widths: scale by width ÷ 1000 and re-check floors.
- Flush left, ragged right. CJK breaks at phrase boundaries (after ——); Latin by meaning. Tabular figures for times. No tracking on display.

## Layout

Grid system: Modular — the field is cut both ways into whole modules; the programme is a ladder on its rows.

- **Module:** M = width ÷ 14, height ÷ rows, rows = round(height ÷ width × 14). Margin 1 module. 1000 × 1414: 14 × 20, 71.4 × 70.7 px.
- **Axes:** L = module 1 (title block, colophon left). T = module 5 (times, 2 modules, left-aligned). C = module 7 to 13 (tagline, talks, colophon right). Nothing else aligns.
- **Rows:** title block from row 1; tagline at C from row 1 to about row 4; first talk row 6; 3 rows per 45 minutes; colophon from row 15 on L and C (two talks keep row 15).
- **Interval:** the block between L and T, from title block to colophon, is never entered.
- **Other formats:** landscape swaps width and height, M from the short side, axes keep module numbers from the left, ladder in the first two thirds of the short field. Recompose, don't scale.
- **Print:** 3 mm bleed, 5 mm safe area outside the margin; ground runs to bleed.

## Shapes

None. No rules, boxes, dots, radius, shadow, grain or gradient (rounded: 0). The grid is read in the white between talks. A photograph, if any, runs edge to edge, no frame or scrim, nothing drawn beside it.

## Components

- **Title block (display, display-zh):** series name and Chinese name stacked at L from row 1. Ban: third line, tracking, rule.
- **Tagline (body):** English then Chinese at C from row 1, as given, same size. Ban: shortening, smaller translation.
- **Talk entry (title, body, label):** time at T in muted body; title at C on the same baseline; speaker below in ink body. Ban: number, icon, bar, rule.
- **Colophon (body, label):** from row 15. Left: date, hours, doors (body), foyer line (label). Right: hall and entry in English and Chinese (body), status line (label, muted). Ban: boxing, facts moved into the ladder.
- **Status line (label, secondary):** the declared note on whether the evening is real, at the foot. Ban: removal, stamp styling.
- **Photograph (if any):** one real photograph with source and place in a Bildlegende at label size. Ban: drawn, generated or stock image.

## Do's and Don'ts

- **One interval, whole.** The 4-module field stays unbroken.
- **Equal time is equal white.** Position comes from start time at 15 minutes per module; measure the pitch.
- **Quiet is not small.** Nothing below 22 px; title cap height over 5 mm per metre of distance.
- **Nothing drawn stands in for the real.** No code-made horizon, texture or object; with no photograph, report none and print no placeholder.
- **One ink, one muted tone.**

Test: the emptiness changes how the subject is felt, and the subject rewards the attention.

Caricature: Zen props, stones, bamboo, brush ink; a rendered bowl on beige; an empty page; unreadable type; a timetable with a coloured header band.

Defaults refused: warm cream with one vermilion accent; tracked uppercase kickers, 01/02/03 numbers, hairline rules over a footer; a drawn grid.

## Variations

- **Horizon (real photograph as the interval).** Once per evening: photograph fills the 4-module field or the full sheet edge to edge; title stays live type, small on its horizon line; ladder keeps its rows. Re-measure contrast on the composite; Bildlegende with source and place; unknown licence stays out.
- **Pause (Hara, ma).** Quiet card in a set: title block and colophon only, ladder removed, 1 per set, white at full height. Every fact appears on at least one unit of the set.

## Record

Folio version: 1.0.0. Template version: 13. Date: 2026-11-02.
Pieces: the-grid/brief.md.
