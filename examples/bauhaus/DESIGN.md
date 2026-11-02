---
version: alpha
name: The Grid · Bauhaus, Joost Schmidt
description: The evening series at the Museum of Design on the systems behind modern design, whose poster is its own programme drawn as a figure of circle, square and bar on a clock-set module.
colors:
  primary: "#111111"
  secondary: "#4A4A46"
  neutral: "#F4F4F0"
  red: "#D7281E"
  blue: "#1D3E9E"
  yellow: "#F3B900"
  line: "#8A8A83"
typography:
  display: { fontFamily: "League Spartan, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 224, fontWeight: 700, lineHeight: 0.9 }
  display-zh: { fontFamily: "Noto Sans SC, Noto Sans CJK SC, League Spartan, sans-serif", fontSize: 158, fontWeight: 700, lineHeight: 0.9 }
  title: { fontFamily: "League Spartan, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 36, fontWeight: 700, lineHeight: 1.1 }
  title-zh: { fontFamily: "Noto Sans SC, Noto Sans CJK SC, League Spartan, sans-serif", fontSize: 32, fontWeight: 700, lineHeight: 1.1 }
  name: { fontFamily: "League Spartan, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 36, fontWeight: 500, lineHeight: 1.1 }
  body: { fontFamily: "League Spartan, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 26, fontWeight: 500, lineHeight: 1.3 }
  body-zh: { fontFamily: "Noto Sans SC, Noto Sans CJK SC, League Spartan, sans-serif", fontSize: 24, fontWeight: 500, lineHeight: 1.4 }
  label: { fontFamily: "League Spartan, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 26, fontWeight: 700, lineHeight: 1.3 }
spacing:
  module: 75
  margin: 50
  thread: 6
  keyline: 3
  grid: 2
  rule: 2
  hairline: 1
rounded:
  none: 0
components:
  ink-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.primary}" }
  muted-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.secondary}" }
  ground-on-ink: { backgroundColor: "{colors.primary}", textColor: "{colors.neutral}" }
---

## Overview

Bauhaus, Joost Schmidt — the 1923 Bauhaus exhibition poster: draw the evening's figure with compass and square from circle, square and bar on one module, in red, blue, yellow and black, then set every line of type into the same construction; never shapes that build nothing.

World: the poster series of The Grid, the Museum of Design's evening series on the systems behind modern design, in English and Chinese. Any evening is made from this file; its brief holds what is particular.

Method:
1. The evening's clock is the field: doors to close, twelve columns, a fixed number of minutes each.
2. Lay the black thread along the clock; hang each talk from it at its start.
3. Square the drop line to the shape's edge, strike the circle with the compass, cut the bar to the module.
4. Cut each crossing in ink.
5. Then hang the type from the same drops.

Time is the fourth term, so it takes the line, never a fourth hue. Kandinsky visits once: form and colour go to talks by place in the evening, not title.

Amplitude: full. Three primaries, one black, flat planes, graphic-scale type; only the exposed grid is turned down.

Anti-reference: a Bauhaus costume (triad recited as pattern, pastel or teal primaries, shapes off the module, gradient, shadow, rounded card); cream ground with one vermilion accent; Newsreader, Plex, Archivo, Jost, Inter; template chrome (tracked kickers, 01/02/03, monospace labels, middle dots); the literal grid of squares.

## Colors

Red, blue, yellow, black on a white card. No other hue; nothing tinted, shaded or translucent.

- **Primary, ink (#111111).** Thread, drops, overlaps, rules, foot band, reading text.
- **Secondary, muted (#4A4A46).** Speakers and exhibition line; 8.07:1 on ground.
- **Neutral, ground (#F4F4F0).** Cool paper white; over half the poster; type on the foot band.
- **Red (#D7281E).** First talk's square. 4.52:1. Never type.
- **Blue (#1D3E9E).** Second talk's circle. 8.52:1. Never type.
- **Yellow (#F3B900).** Last talk's bar. 1.62:1, so a 3 px ink keyline always. Never type; never touches red.
- **Line (#8A8A83).** Exposed grid only, 3.07:1.

Red, blue, yellow are first, second, last talk, in that order. Crossings are ink.

## Typography

- **League Spartan** (OFL; 500, 700). Futura-lineage; round G echoes the circle. Fallback: system sans.
- **Noto Sans SC** (OFL; 500, 700). Chinese voice. Fallback: Noto Sans CJK SC.
- **Roles.** Display: THE GRID in capitals, word spacing −0.08 em, ink spanning twelve columns (224 px on 1000), cap height two modules; Chinese masthead at the same ink height (158 px). Title 36/700: time, date, hall. Name 36/500: talk title. Body 26/500: descriptor, speakers. Label 26/700: doors, entry, disclaimer. Chinese at 0.9 (32, 24). No other sizes.
- Two weights. Lining figures, one time per line. No italic, letterspacing, outline type.
- Chinese: hand breaks at phrases; full-width punctuation, dash ——.

## Layout

Grid system: Modular. From width W and height H:
1. Margin W/20 (50 px).
2. Twelve columns, no gutters; module = column width (75 px).
3. Rows floor((H − 2 margins) / module): 17 on 1000 × 1414. Remainder falls to the foot: one module of black bleeding off the bottom.
4. Clock: 15 minutes a column for 19:00–22:00 (20 for four hours). A start off a column line sits on the nearest half module; the brief says so.
5. Thread on row line 5, full width. Shapes hang from row line 8. Exposed grid: columns 0–12, rows 8–12. Ledger from row line 13, one row per fact.
6. Masthead on row line 2; Chinese masthead under it; descriptor on column line 5 beside it.

Shape sizes double (1, 2, 4, 8 modules); every edge, centre and drop lands on a module line. Reading: masthead, figure, down each drop to time and name, ledger.

## Shapes

Flat fills, hard edges, zero radius, no shadow, gradient or transparency. Circle diameter four modules or more. Drawn in SVG from the module.

- **Forms**, in order: square, circle, bar (one module thick, four long). A fourth talk restarts at the square, one doubling larger.
- **Placement.** Left edge on the start's column line, row line 8; the bar's top edge on the circle's centre line. Width is the doubling size, never a talk's length.
- **Overlap.** Draw lower, upper, then lower again in ink clipped to the upper. Always overlap, never abut.
- **Thread.** 6 px ink, 0 or 90 degrees, a drop to each start ending on a corner or the circle's leftmost point. Doors drop one module. Nothing else at 6 px.
- **Keyline.** 3 px ink, yellow only, inset.
- **Exposed grid.** 2 px line colour on every module line of the field; never under text.
- **Rules.** 2 px ink opens the ledger; 1 px ink between rows.

## Components

- **Masthead.** THE GRID, then the Chinese name at the same ink height. Ban: tracking changed to fit.
- **Descriptor.** English above Chinese, body and body-zh, on column line 5, at most seven columns. Ban: English larger than Chinese.
- **Thread.** Ban: curve, diagonal, arrowhead, second thread.
- **Talk block.** 14 px right of its drop: time (title), talk (name), speaker (body, muted). Stops short of the next drop; surnames whole. Ban: text on a shape.
- **Doors mark.** Doors time in label at the thread's start.
- **Ledger.** One module-high row per fact: Latin left in title (label if secondary), Chinese pair right on the baseline; exhibition line in body, muted, unpaired. Ban: boxes, icons.
- **Foot band.** One module of ink, full bleed, disclaimer in label, ground colour, if fictional. Ban: logos.

## Do's and Don'ts

1. **Hang everything from the clock.** Starts sit on column lines, never moved for composition.
2. **Time is line, not hue.**
3. **No type on a primary shape.**
4. **Yellow is always keyed.**
5. **Test.** Remove the type: shapes, thread and grid still build this evening's figure, not any evening's.

## Variations

- **Vertical Chinese.** Masthead top to bottom in a column two modules wide, once per run, four characters at most.
- **Pause.** One evening per run shows grid, thread and descriptor only.
- **Bleed.** The last bar may run off the right edge by at most 150 px; keyline on the three visible sides.

## Record

Folio version: 1.0.0. Template version: 13. Date: 2026-11-02.
Pieces: the-grid/brief.md.
