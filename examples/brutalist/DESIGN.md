---
version: alpha
name: The Grid · Swiss Brutal, the Construction hand
description: The Museum of Design's evening series on the systems behind modern design, set as a concrete-grey document of record whose row grid is the evening's clock.
colors:
  primary: "#0B0B0B"
  secondary: "#454745"
  tertiary: "#FFD200"
  neutral: "#E3E4E1"
  field: "#C9CBC7"
  line: "#7A7C79"
typography:
  display: { fontFamily: "Inter Display, Inter, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 276, fontWeight: 900, lineHeight: 0.76 }
  title: { fontFamily: "Inter Display, Inter, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 56, fontWeight: 800, lineHeight: 1 }
  time: { fontFamily: "Inter, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 40, fontWeight: 800, lineHeight: 1 }
  body: { fontFamily: "Inter, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 32, fontWeight: 700, lineHeight: 1.6 }
  label: { fontFamily: "Inter, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 32, fontWeight: 500, lineHeight: 1.5 }
spacing:
  row: 48
  column: 78
  margin: 32
  inset: 12
rounded:
  none: 0
components:
  ink-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.primary}" }
  muted-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.secondary}" }
  ink-on-field: { backgroundColor: "{colors.field}", textColor: "{colors.primary}" }
  muted-on-field: { backgroundColor: "{colors.field}", textColor: "{colors.secondary}" }
  ground-on-ink: { backgroundColor: "{colors.primary}", textColor: "{colors.neutral}" }
  ink-on-hazard: { backgroundColor: "{colors.tertiary}", textColor: "{colors.primary}" }
---

## Overview
Swiss Brutal, the Construction hand, after the Modulor cast into the concrete of Le Corbusier's Unité d'Habitation and the grids computed in Müller-Brockmann's *Grid Systems*: compute the rows from the clock of the evening, draw only the rules the schedule uses, and let one word at architectural scale stand on top of them; never a rule that bounds nothing, never a surface effect.
World: the Museum of Design's evening series "The Grid"; two-script title, date, venue, running order, one parallel event, a notice.
Method: 1. Count quarter hours from doors to close: that is N rows of the time field. 2. Cut whole rows and 12 equal columns. 3. Hairline and axis tick per row, longer tick per hour. 4. Each talk: one black cell, one column by one row, on its start row. 5. Parallel event: grey field beside the talks, open at its far end. 6. Title: the Monolith, one word on whole rows, flush left. 7. Dark footer begins on the closing line. Computed, never nudged.
Amplitude: full on the title (two to three times the next element), quiet elsewhere; grid quieter than text.
Anti-reference: neo-brutalist sticker (thick outlines, hard shadows), terminal cosplay, cream and vermilion, a lattice as wallpaper.

## Colors
Concrete, ink, one signal.
- Ground #E3E4E1: cool grey-white, not cream; at least half the poster.
- Ink #0B0B0B: text, Monolith, cells, footer.
- Muted #454745: keys, secondary lines; 4.5:1.
- Field #C9CBC7: the parallel event only.
- Line #7A7C79: grid and ticks, 3:1, never text.
- Hazard #FFD200: the illustrative notice only, ink text, never on text or lines.
Footer flips to ground text.

## Typography
Inter, Display cut for Monolith and titles (OFL; Inter fallback). Noto Sans SC Bold or Black (OFL; CJK fallback), em box 0.9 of Latin. Both scripts same size and weight.
Four steps at 1000 px: 276 Monolith (900, -0.05em), 56 titles, 40 times, 32 body, speakers, notices, label weight 500 for track and key. Nothing below 32; ramp scales with the row. Tabular figures. A text line sits inside one row; blocks use whole rows.

## Layout
Grid system: Modular; rows are the time axis. N = quarter-hour rows plus header, title (cap height plus leading, rounded up), tagline, footer; row = (height - 2 x margin) / N, whole pixels, margin the halved remainder. 12 columns, no gutters, 12 px inset. Axis columns 1-2; cells column 3; talks 4-9; parallel event 10-12. Heavy rules at the field's open and close, verticals at columns 3 and 10, hairline per row. Landscape or web: axis left, rows down. Nothing is centred.

## Shapes
Zero radius, shadow, gradient or outline. Hairlines 1 px; table rules 6 px ink; top edge one 8 px ink rule. Cell one column by one row. Ticks 1 px, 14 px per row, 28 px per hour.

## Components
- Monolith: display step, ink, flush left; Chinese title on the first line. Ban: second monolith, tint.
- Header ledger: date and hours in body step, one row each; venue in both scripts at column 7; hairlines above and below.
- Tagline: two scripts, whole rows, body step.
- Ruler: hairline and tick per row, 6 px rules. Ban: labels at times that are not facts.
- Start cell: column 3, time on the axis in the time step. Ban: a cell on a row that starts nothing.
- Entry: title step, speaker body regular, runs to the next start. Ban: unstated durations.
- Parallel track: field column, ink left rule, label step, hairlines resuming below. Ban: an unstated end mark.
- Footer: ink, bleeding to the edges, ground text, closing line as top edge.
- Notice: hazard cell inside the footer, ink, body size at 800, two lines.
- Key: muted, "1 row = 15 min", once.

## Do's and Don'ts
- Derive every position from rows and clock; change the number, not the position.
- Delete any line that bounds nothing; hazard for the notice only.
- Squint: text reads before rules.
- Refused: sticker brutalism, terminal green, cream with one vermilion accent, tracked kickers, 01/02/03, monospace labels, a clock-face pictogram.

## Variations
- Accent field: the whole poster in hazard yellow, ink text; once, at a turn (a final night).
- Rotation: Monolith 90 degrees counter-clockwise on a tall web banner; origin column 1, first row.

## Record
Folio version: 1.0.0. Template version: 13. Date: 2026-11-02.
Pieces: the-grid/brief.md.
