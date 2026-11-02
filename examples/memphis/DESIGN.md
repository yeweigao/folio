---
version: alpha
name: The Grid · Memphis, Sottsass
description: The evening series of a design museum on the systems behind modern design, set as flat primitives cut from printed laminates and assembled on the sheet's own module field.
colors:
  primary: "#111111"
  neutral: "#FFFFFF"
  cobalt: "#2438E0"
  rose: "#FF4FA3"
  lemon: "#FFD21F"
  mint: "#00C389"
typography:
  display: { fontFamily: "League Spartan, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 212, fontWeight: 900, lineHeight: 156px }
  display-cjk: { fontFamily: "Noto Sans SC, Noto Sans CJK SC, League Spartan, sans-serif", fontSize: 136, fontWeight: 900, lineHeight: 1 }
  headline: { fontFamily: "League Spartan, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 64, fontWeight: 800, lineHeight: 70px }
  numeral: { fontFamily: "League Spartan, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 84, fontWeight: 900, lineHeight: 0.9 }
  title: { fontFamily: "League Spartan, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 44, fontWeight: 800, lineHeight: 1.02 }
  voice: { fontFamily: "DM Serif Display, Noto Sans SC, serif", fontSize: 30, fontWeight: 400, lineHeight: 1.05 }
  label: { fontFamily: "League Spartan, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 26, fontWeight: 800, lineHeight: 1.12 }
  label-cjk: { fontFamily: "Noto Sans SC, Noto Sans CJK SC, League Spartan, sans-serif", fontSize: 26, fontWeight: 700, lineHeight: 1.2 }
spacing:
  margin: 40
  gutter: 16
  module: 140
  tower: 296
  band: 86
  rule: 6
rounded:
  none: 0
components:
  ink-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.primary}" }
  ground-on-ink: { backgroundColor: "{colors.primary}", textColor: "{colors.neutral}" }
  ground-on-cobalt: { backgroundColor: "{colors.cobalt}", textColor: "{colors.neutral}" }
  ink-on-rose: { backgroundColor: "{colors.rose}", textColor: "{colors.primary}" }
  ink-on-lemon: { backgroundColor: "{colors.lemon}", textColor: "{colors.primary}" }
  ink-on-mint: { backgroundColor: "{colors.mint}", textColor: "{colors.primary}" }
---

## Overview
Memphis, Ettore Sottsass: the Bacterio laminate (1978) and the Carlton bookcase (1981). Draw the pattern first as a tileable laminate, cut flat primitives from it, and assemble them on the module field until the sheet is the furniture; never a pattern that carries information, and never a pattern behind reading text.
World: THE GRID, evening series of a design museum on the systems behind modern design. One poster per evening (A-series, read at 2 to 5 m); the same skeleton carries a ticket or foyer screen by recomposing the module field, never scaling it. Content: series title, date and place, ordered talks, one exhibition, free-entry line, disclosure line when fictional.
Method: (1) Draw three laminates as SVG pattern tiles with a declared repeat from the primitive's side; judge flat at full scale. (2) Cut each primitive from a square of one tower side (2 modules + gutter). (3) Clad it with the laminate in its talk's hue; stand it on a solid slab of that hue carrying the words. (4) Tile the field whole: towers in a staircase, one module lower each; every other cell a solid fact block (black place, mint exhibition) or deliberate white.
Amplitude: full. Hues clash, laminates run coarse, type is heavy; only the white between pieces and the text on solid fields stay quiet.
Anti-reference: the grey Swiss poster with one red square; Memphis as wallpaper (squiggle confetti, outlines, 80s pastels behind Helvetica).

## Colors
Black ink (primary): every reading line on white, the title, and fields (second script's title block, place block). White (neutral): ground between pieces and text on cobalt and ink; 46% of the 1000 × 1414 sheet, below the Swiss 50% rule by dialect; never under 40%.
Four hues, none decoration. Order markers: cobalt first talk, rose second, lemon third, then restart. A hue stays with its talk everywhere; never recoloured for balance. Mint names one category: the exhibition. Laminate rules and dots: white on cobalt, ink on rose, lemon, mint. Text: white on cobalt, ink on every other hue (contrast above 6:1). No tints, gradients or greys.

## Typography
League Spartan (600, 800, 900) for titles, times, labels, facts. DM Serif Display Italic (400): speakers' names only. Noto Sans SC (700, 900) for Chinese at the Latin's weight; Noto Sans CJK SC fallback. Google Fonts, OFL.
Ramp: display 212 px (title, one word per row, cap height one module, 140 ÷ 0.66); display-cjk 136; headline 64 (date, two lines make one module); numeral 84 (talk time); title 44 (talk name); voice 30 italic (speaker); label 26 (other facts, Chinese beside at the same size). Chinese never smaller than the Latin it translates. En dash for ranges; full-width Chinese punctuation, —— for the dash; Chinese broken by hand at phrase boundaries with non-breaking spans. Floors at 1000 px: lead facts 46 px, supporting 26, description 22, disclosure 30.

## Layout
Grid system: Modular. Every fact, form and block takes whole modules.
From format W × H: margin m = 4% of W (40); six tracks, gutter g = 0.4 m (16); module c = (W − 2m − 5g) ÷ 6 (140), square; rows n = whole (c + g) fitting in H − 2m − 60; base band = H − 2m − n(c + g), at least 60 (86; n = 8). Tower = 2c + g square (296): primitive over a same-size solid slab, a gutter between. Towers stand left to right in evening order, one module lower each. Three talks: two tracks wide; two talks: three tracks wide, slab still two rows tall; four or more not drawn.
Title in rows 1 and 2 at left, one word per row, baseline on the row's bottom edge, stem on the margin, round letters hang 3 to 4 px out. Chinese title: ink block, first module row at right, description beneath. Date: first free row right of the first tower, pitch fills one module. Times: next free cell right. Place: ink 2 × 2 under the first tower. Exhibition: mint 2 × 1 under the second. Base band: 6 px ink rule, entry line left, disclosure right. Unnamed cells stay white. No content in margin; no bleed.

## Shapes
Radius zero; no shadow, outline, gradient or stroke on a form; one rule (the 6 px ink rule). Flat.
Primitives, each a tower-side square cut to shape: square; right triangle (right angle bottom left, 45 degree hypotenuse); disc with a square gap (a quarter side, turned 45 degrees, off axis to the lower right of centre). The brief picks the primitive from the talk's subject; hue follows order. Add a new primitive here before use.
Laminates, SVG pattern tiles clipped by the shape:
Grid, for the square: repeat side ÷ 4 (74); 6 px white or ink rules on top and left edges, offset half a rule; 12 px ink node at each cell centre; 3 px frame of the hue round the shape.
Diagonal, for the triangle: repeat side ÷ 8 (37) along a leg; 11 px ink stripes at 45 degrees parallel to the hypotenuse, with corner stripes for a seamless tile.
Dot, for the disc: repeat side ÷ 8 (37) by twice that high, half-drop; ink dots of radius 8.
Cut off by the edge, never fitted. Never behind text, never encoding a quantity, never off its tower's hue.

## Components
Series title: display, ink on white, one word per row, tracking -0.01 em; never centred or on pattern.
Chinese title block: display-cjk white on ink, one row by two tracks, centred (the one centred form); never on a hue.
Series description: label and label-cjk 22 to 23 px on white, English then Chinese, at most two sentences.
Date: headline on white, flush left, two lines, unabbreviated.
Times: numeral-sized range over a smaller label, white, under the date; doors line a label.
Primitive: one laminate-clad shape per talk, aria-hidden, no text.
Talk slab: solid hue, two tracks by two rows; start time (numeral) top left, title over speaker (voice) bottom left; white on cobalt, ink on rose and lemon; no pattern.
Place block: ink 2 × 2; English place in label weight, Chinese beneath at 40 px display-cjk weight, white; no map or pictogram.
Exhibition cell: mint, two tracks by one row, one sentence as label, ink; never a talk.
Base band: 6 px ink rule; entry line label 29 px, Chinese beneath, left; disclosure voice 34 px, right, never smaller or faded, on every fictional piece.

## Do's and Don'ts
Do tile the field whole; white only as gutter or deliberate quiet cell.
Do carry the evening in order: left to right, high to low.
Do keep all text on solid ground; forms carry no words.
Do make the clash a relation: one hue per talk, black place, mint exhibition.
Don't let pattern say anything, scale it down to texture, or fit it to its edge.
Test: remove laminates and staircase; if a neat table of coloured boxes remains as the poster, the clash was decoration.
Caricature: squiggle confetti, black outlines, 80s pastels, wallpaper behind a Swiss page.
Refused defaults: cream ground with one rust accent (pure white, so hues stay untinted); Inter, Plex, Newsreader, Jost (heavy geometric plus Didone); template chrome (no kicker, no 01 02 03, no middle-dot strings, no monospace); numerals as hero (title leads); CSS objects with shadows.

## Variations
Night field: whole unit on ink, type white, towers and slabs unchanged, gutters ink.
Gap turned: a second primitive turned 45 degrees off axis; field, hue and slab untouched.
A variation never touches reading text; a unit takes one.

## Record
Folio version: 1.0.0. Template version: 13. Date: 2026-11-02.
Pieces: the-grid/brief.md.
