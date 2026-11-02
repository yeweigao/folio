---
version: alpha
name: The Grid · De Stijl, Mondrian
description: The Museum of Design's evening series on the systems behind modern design, one bilingual poster per evening, each drawn as black bars and planes of primary colour with the bars set at the evening's own clock times.
colors:
  primary: "#111111"
  neutral: "#F2F1EC"
  red: "#D02A1E"
  yellow: "#F5C400"
  blue: "#1F3F9A"
  grey: "#D6D5CF"
typography:
  display: { fontFamily: "Anybody, Noto Sans SC, sans-serif", fontSize: 200, fontWeight: 900, lineHeight: 0.86 }
  display-han: { fontFamily: "Noto Sans SC, Anybody, sans-serif", fontSize: 150, fontWeight: 900, lineHeight: 1.15 }
  numeral: { fontFamily: "Anybody, Noto Sans SC, sans-serif", fontSize: 62, fontWeight: 900, lineHeight: 0.92 }
  text: { fontFamily: "Anybody, Noto Sans SC, sans-serif", fontSize: 40, fontWeight: 800, lineHeight: 1.1 }
  body: { fontFamily: "Anybody, Noto Sans SC, sans-serif", fontSize: 28, fontWeight: 600, lineHeight: 1.3 }
  body-han: { fontFamily: "Noto Sans SC, Anybody, sans-serif", fontSize: 28, fontWeight: 700, lineHeight: 1.3 }
spacing:
  bar: 16
  baseline: 8
  pad-x: 22
  pad-y: 20
  gap: 8
  scale: 3.1
rounded:
  square: 0
components:
  ground-on-red: { backgroundColor: "{colors.red}", textColor: "{colors.neutral}" }
  ground-on-blue: { backgroundColor: "{colors.blue}", textColor: "{colors.neutral}" }
  ink-on-yellow: { backgroundColor: "{colors.yellow}", textColor: "{colors.primary}" }
  ink-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.primary}" }
  ink-on-grey: { backgroundColor: "{colors.grey}", textColor: "{colors.primary}" }
---

## Overview

De Stijl, Piet Mondrian — the Compositions (1921–30): set the black bars on the tracks, then move one bar or resize one plane at a time and re-render until no change improves the balance; never a centred title block, a diagonal, or two equal cells.

World: "The Grid", the Museum of Design's evening series; any A-series size, English and Chinese equal. Words, times and talk count change; ground, bar, primaries, grey, faces, roles and construction do not.

Method:
1. Clock times first: doors, talk starts, close. They fix the five horizontal bars; every plane between two is drawn to its duration.
2. Free bars by eye, one move per re-render: spine, title-row bar, date split, clock vertical.
3. Colour by job, never taste: largest plane red, counterweights unequal, no square.
4. Live type flush left: what, when, where, who, how to come. Never on a bar.
5. Resize or recolour one plane; if balance holds, it was decoration; remove it.

Amplitude: full for structure, reduced for emptiness; every plane carries a fact; white plus grey at least 45 %.

Anti-reference: cream sheet with one red square; a black lattice over an ordinary page; a red, yellow, blue card grid; Mondrian as a border.

## Colors

- **Ink `#111111`** (primary). Bars, and type on yellow, white, grey. 3.6:1 on red, 2.0:1 on blue: never there.
- **Ground `#F2F1EC`** (neutral). White plane; type on red (4.6:1) and blue (8.3:1).
- **Red `#D02A1E`.** Lead and disclosure: largest plane, Latin title. At most 15 %.
- **Blue `#1F3F9A`.** The reader's side: Han title, invitation. At most 15 %.
- **Yellow `#F5C400`.** Time only: date, range, clock. A plane, never a mark.
- **Grey `#D6D5CF`.** Receding reading planes: descriptor, parallel event.
- Measured: red 12.9 %, blue 14.9 %, yellow 12.0 %, bars 13.4 %, white 24.3 %, grey 22.5 %. Primaries together at most 40 %.
- No other hue, gradient, tint, transparency or dark register.

## Typography

- **Latin: Anybody** (Google Fonts, OFL; variable). Display 900 width 100; numeral 900 width 100 (clock) or 64 (range); text 800 width 84 (date 78); body 600 width 84.
- **Han: Noto Sans SC** (700, 900), same stack and steps.
- **Ramp: 200 / 150 display (Latin / Han), 62 numeral, 40 text, 28 body.** No italic or tracking. Latin title in capitals.
- **Han title** at 0.75 of Latin, one character per line (one or two characters) or two (three or four); pitch 172 px at 200; first glyph top on the Latin cap line.
- Latin breaks by meaning, `text-wrap: balance`. Chinese breaks by hand in no-wrap spans, never inside a word or before ——; full-width punctuation, en dash ranges, tabular clock figures.
- Never compress the display; a wide line drops it in 8 px steps, Han at 0.75.
- Both faces must load.

## Layout

Grid system: Hierarchical — zones sized by content weight, drawn as Mondrian bars, the timetable on a time scale.

At W = 1000, H = 1.414 W; scale by W / 1000; snap to 8 px.
- **Bars.** Ink ground; planes separated by 16 px gaps; no frame; planes bleed left, right, bottom.
- **Spine** at 624, full height.
- **Zone 1**, 432 from top: red Latin title (main column), blue Han (second); disclosure at the red foot.
- **Zone 2**, to the 19:00 bar (264 high): yellow date and range, white place, split at 352; grey descriptor in the second column.
- **Zone 3, timetable.** Bar for t centred at y = y_end − (end − t) × 3.1; doors bar centre 720, closing 1278 (558 px, 180 min). Planes run half a bar inside their bars.
  - White doors plane, full main column.
  - Talk row: yellow clock plane top-left, vertical at 256, white title and name; height is duration × 3.1.
  - Grey parallel-event plane in the second column from the doors bar; off the foot if no end is given.
- **Zone 4**, 128 under the closing bar: blue invitation, main column.
- **Fit.** Talk plane needs 120 px, one-line plane 72; if shorter, merge with its neighbour and record it. Other lengths: scale = 558 ÷ minutes, rounded down to a tenth.
- Padding 20 under a bar, 22 from a vertical; lines 8 apart; bottom gives way first.
- New formats are recomposed, not scaled; cap height 5 mm per metre of distance.

## Shapes

- Radius 0; no shadow, outline, card, texture, gradient, picture or ornament.
- Bars: ink, 16, horizontal or vertical, right angles, ending on a bar or the edge.
- Time is height only, one scale per sheet.

## Components

- **Title:** red, ground type. Latin display, two lines flush left; disclosure in text at the foot.
- **Han:** blue, ground type. display-han, flush left; no caption.
- **Date:** yellow, ink. Date in text, range in numeral at width 64; no label or icon.
- **Place:** white, ink. Text, Chinese in body-han beneath; no pin or map.
- **Descriptor:** grey, ink. One body block per script, three lines at most.
- **Doors:** white, ink. One text line.
- **Clock:** yellow, ink, numeral width 100, tabular; no end time or duration.
- **Talk:** white, ink. Title in text, speaker in body; no numbering, bullets, uncaptioned photograph.
- **Parallel event:** grey, ink. Text line at the top; no invented end.
- **Invitation:** blue, ground type. Body line plus body-han; no button or arrow.

## Do's and Don'ts

1. **Do take the bars from the subject.** Clock bars are the times.
2. **Do keep facts live and flush left,** once each, in both scripts.
3. **Don't let colour decorate.** Red leads, blue answers, yellow is time.
4. **Don't make equal cells or symmetry.**
5. **Don't put a second hand in.** One hand per sheet.

## Variations

- **Boogie bar.** One non-clock bar breaks into at most six primary and grey segments, each at least 40 px, after *Broadway Boogie Woogie*, for a closing night.
- **Counter-composition.** Only if the brief names van Doesburg: field at 45°, clock scale dropped.

## Record

Folio version: 1.0.0. Template version: 13. Date: 2026-11-02.
Pieces: the-grid/brief.md.
