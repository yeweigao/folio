---
version: alpha
name: The Grid · Swiss Punk, Weingart
description: A museum's evening series on the systems behind modern design, printed as slipped films on one 6 x 9 module grid.
colors:
  primary: "#0B0B0C"
  secondary: "#4F555C"
  tertiary: "#1560D6"
  neutral: "#ECEEEF"
  screen: "#C3CCDA"
typography:
  display-latin: { fontFamily: "Archivo, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 250, fontWeight: 900, lineHeight: 0.82 }
  display-light: { fontFamily: "Archivo, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 236, fontWeight: 300, lineHeight: 0.82 }
  display-han: { fontFamily: "Noto Sans SC, Noto Sans CJK SC, Archivo, sans-serif", fontSize: 140, fontWeight: 900, lineHeight: 1 }
  level-2: { fontFamily: "Archivo, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 44, fontWeight: 800, lineHeight: 1.05 }
  level-2-light: { fontFamily: "Archivo, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 44, fontWeight: 300, lineHeight: 1 }
  level-3: { fontFamily: "Archivo, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 32, fontWeight: 700, lineHeight: 1.14 }
  level-3-medium: { fontFamily: "Archivo, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 30, fontWeight: 600, lineHeight: 1.12 }
  level-3-muted: { fontFamily: "Archivo, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 28, fontWeight: 500, lineHeight: 1.14 }
  level-3-han: { fontFamily: "Noto Sans SC, Noto Sans CJK SC, Archivo, sans-serif", fontSize: 26, fontWeight: 500, lineHeight: 1.2 }
spacing:
  margin: 40
  gutter: 16
  module-x: 140
  module-y: 134
  pitch-x: 156
  pitch-y: 150
  dot-pitch: 14
  slip-x: 14
  slip-y: 10
  step: 62
rounded:
  none: 0
components:
  ink-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.primary}" }
  muted-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.secondary}" }
  accent-on-ground-large: { backgroundColor: "{colors.neutral}", textColor: "{colors.tertiary}" }
  ink-on-screen: { backgroundColor: "{colors.screen}", textColor: "{colors.primary}" }
---

## Overview
Swiss Punk, Wolfgang Weingart — the Kunsthalle Basel posters: build each film separately, slip the films against the grid by declared amounts, overprint, render to see the slip; never displacement that covers a fact.
World: The Grid, a museum's recurring evening on the systems behind modern design; one A-series poster per evening, read at 2–5 m.
Method:
1. Compute the grid from the format.
2. Film 0, black: + at gutter crossings of rows 1–4; the stepped thread.
3. Film 1, screen: one glyph of the title as a true dot screen from one raster, solid one side, thinning to a 45% tone floor.
4. Film 2, accent: copy of the display forms by pseudo-content, one container slipped whole.
5. Film 3, black: live type; display baseline stepped down per letter, condensed light word over extended black word; reading text flat.
Amplitude: Full. Only rotation is the upright vertical Han title. Reading text never slipped, stepped, overprinted or over the screen.
Anti-reference: grey Swiss minimum with one red square; distressed punk (glitch, scatter, one rotated word, drop shadow as slip).

## Colors
- primary #0B0B0C: live type, thread, + marks, target.
- secondary #4F555C: second-language lines only, on the ground. Names are ink.
- tertiary #1560D6: grid-pencil blue; slipped copies of display forms and half the target, multiplied. Never reading text or ground; under 10% of area.
- neutral #ECEEEF: cool newsprint ground, about 70% of area, never below 50%.
- screen #C3CCDA: dot-film tint; display type crosses it, reading text never.
Overprint by multiply: on black it stays black; the slip shows as a blue fringe.

## Typography
Archivo variable (OFL), wdth 62 at weight 300 to wdth 125 at weight 900 in one title; Noto Sans SC for Han, same weight; fallback Noto Sans CJK SC.
Ramp: display Latin 250 px black extended, light word 236 px condensed, Han 140 px black; level 2 44 px (weight 800 facts, 300 clock times); level 3 26–32 px (speakers 30 px weight 600). Nothing below 26 px. Sizes belong to the 1000 px master read at A1; recompose, never shrink.
Display Latin steps down 62 px per letter; the light word is not stepped. Han title upright, vertical, one column. Tabular figures; no caps tracking; letters touch, not fuse.

## Layout
Grid system: Modular, 6 columns by 9 rows. Margin = 4% of short side; gutter = 0.4 margin; column = (short - 2 margin - 5 gutter) / 6; rows = round((long - 2 margin + gutter) / (column + gutter)). At 1000 x 1414: margin 40, gutter 16, modules 140 x 134, pitches 156 and 150.
Row 0: when. Rows 1–4: title and screen; Han title in the last column from row 0. Rows 5–7: stepped thread. Lower triangle: place and notices; declaration line at the bottom margin.
Thread: 5 px black line stepping right 6 / N columns (N = 3: two) and down one row per talk, risers in the gutter; each talk hangs flush left under its rule: time, title, speaker. Steps stay equal; print times if intervals differ.
Dot screen: pitch column / 10 = 14 px, axis-aligned, anchored to the margin; radius follows tone, capped at 0.72 pitch. Rows 1–4, right of the light word, under display type only; glyph about 4 columns.
Slip: whole accent film 14 px right, 10 px down, one vector. Bottom-right target prints both films.

## Shapes
Zero radius, no boxes, shadows or gradients. 5 px thread, 1.5 px + marks of 14 px, 3 px target; dots are circles on a lattice. The slip is a second flat ink overlapping its black form on both axes.

## Components
- Title: light word over black word, slipped accent copy, black word stepping. Never centered.
- Han title: upright, vertical, top right, slipped accent copy. Never the only carrier of a fact.
- When: date level 2 weight 800, clock time beneath weight 300, doors level 3. No dots or slashes.
- Screen: dot film of a title glyph. Never under reading text, never flat, never a changing pitch.
- Thread and talk: never a table, never 01 02 03.
- Tagline: level 3 bold, other language beneath in muted; never over the screen.
- Place and notices: level 3, flush left in the lower triangle, second language muted.
- Registration target: one, at the bottom margin.
- Declaration line: the piece's status, level 3 bold, ink, flush left on the bottom margin; never small print.

## Do's and Don'ts
- Do slip each film whole; never a single word.
- Do let + marks, thread and target prove the grid.
- Do keep every fact horizontal, flat, clear of the screen.
- Don't use drop shadow or glow for the second ink.
- Don't use a stock image for the screen.
- Refused defaults: cream and vermilion, hairline split footer, 01/02/03, tracked caps kickers, giant numeral, grid-of-squares pictogram.

## Variations
- Accent field: whole piece on the accent; screen turns to ground tone. One per run.
- Rotation: one display element at 90 degrees from a grid intersection; never with the vertical Han title.
- Thin-mode turn: hairline light word at giant size.
- Pause: screen alone, title at declaration size; one per set.

## Record
Folio version: 1.0.0. Template version: 13. Date: 2026-11-02.
Pieces: the-grid/brief.md.
