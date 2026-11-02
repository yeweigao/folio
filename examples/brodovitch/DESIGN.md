---
version: alpha
name: The Grid · Swiss, Brodovitch (the Bazaar covers)
description: The Museum of Design's evening series on the systems behind modern design, set as a fashion cover that has been cut by a ruler.
colors:
  primary: "#0B0B0C"
  secondary: "#55585C"
  tertiary: "#86C9EE"
  neutral: "#F6F7F7"
  ash: "#A3A6AA"
typography:
  display: { fontFamily: "Bodoni Moda, Didot, Bodoni 72, serif", fontSize: 336, fontWeight: 800, lineHeight: 1 }
  lockup: { fontFamily: "Bodoni Moda, Noto Serif SC, Noto Serif CJK SC, Didot, serif", fontSize: 160, fontWeight: 400, lineHeight: 1 }
  lockup-cjk: { fontFamily: "Noto Serif SC, Noto Serif CJK SC, Bodoni Moda, serif", fontSize: 160, fontWeight: 900, lineHeight: 1 }
  title: { fontFamily: "Bodoni Moda, Didot, Bodoni 72, serif", fontSize: 46, fontWeight: 700, lineHeight: 1.22 }
  body: { fontFamily: "Hanken Grotesk, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 30, fontWeight: 500, lineHeight: 1.4 }
  label: { fontFamily: "Hanken Grotesk, Noto Sans SC, Noto Sans CJK SC, sans-serif", fontSize: 15, fontWeight: 400, lineHeight: 1.4 }
spacing:
  unit: 14
  margin: 56
  gutter: 12
  column: 138
  plate-edge: 504
rounded:
  none: 0
components:
  primary-on-neutral: { backgroundColor: "{colors.neutral}", textColor: "{colors.primary}" }
  secondary-on-neutral: { backgroundColor: "{colors.neutral}", textColor: "{colors.secondary}" }
  neutral-on-primary: { backgroundColor: "{colors.primary}", textColor: "{colors.neutral}" }
  ash-on-primary: { backgroundColor: "{colors.primary}", textColor: "{colors.ash}" }
  tertiary-on-primary: { backgroundColor: "{colors.primary}", textColor: "{colors.tertiary}" }
---

## Overview
Swiss, in Alexey Brodovitch's hand of the *Harper's Bazaar* covers (1934–58): work from one commissioned photograph, crop it to a single gesture, then set one Didone word across the edge of that crop at the scale of the figure, so that the ruler that cuts the picture also cuts the word; never a stock figure under a centred serif, never gold, never a script face.
World: The Grid, the Museum of Design's evening series on the systems behind modern design; one poster per evening, read at two to five metres, English and Simplified Chinese at equal status. Evening specifics live in its brief.
Method: (1) One photograph of a body in motion, cut to one gesture, near-black plate, shadows where the type falls; until then a labeled FPO plate. (2) Plate edge on a module line, a third down. (3) Display word in Bodoni Moda, full content width, crossing the edge past its middle: paper on the plate, ink on the paper, one live element split by a hard stop. (4) Small word and Chinese title on one baseline above. (5) Below the edge: column grid, grotesque, two hairlines.
Amplitude: Full on the plate (one word at 336 px, one picture); reduced below.
Anti-reference: Centred serif logo over a stock model, gold, tracked capitals; the museum-evening default of cream, vermilion, small tasteful sans, giant numeral.

## Colors
- **Ink `#0B0B0C` (primary).** The plate, the display word's lower half, reading text, the two rules.
- **Paper `#F6F7F7` (neutral).** Cold coated white, never cream; type colour on the plate.
- **Muted `#55585C` (secondary).** Speakers' names, on paper only. Never on ink, never a rule.
- **Ash `#A3A6AA`.** The photograph credit, 15 px, on the plate only.
- **Non-photo blue `#86C9EE` (tertiary).** The editor's pale pencil: four corner crop marks, twelve column ticks at the trim, the bold word in the credit line; under 1% of the sheet, on the plate only (below 3:1 on paper).

## Typography
- **Bodoni Moda** (Google Fonts, optical sizes 6–96; fallbacks Didot, Bodoni 72). Display word: 800 at 336 px, tracking −0.012 em, size set by the word to fill 888 px, never tracked to fit. Small word: italic 400 at 160 px, left optical margin −4 px. Titles 700 at 46 px; date 600 at 46 px. Never body.
- **Noto Serif SC 900**, 160 px, on the small word's baseline, flush right; Song strokes answer the Didone.
- **Hanken Grotesk** with **Noto Sans SC**: reading 30 px, 500, leading 42 px; credit 15 px, 400.
- **Ramp:** 336, 160, 46, 30, 15; steps at least 1.5×, no size between.
- **Chinese and Latin.** One hierarchy, same track, same size. Wrap `white-space: nowrap` phrases; no break inside a fact. The dash pair —— stays whole and ends a line. No added space between scripts. Proportional Bodoni figures in titles and date; en dashes in ranges.

## Layout
Grid system: Column — six tracks, under a division of the height into a plate and a page.
Width W, height H: u = H ÷ 101 (14 px at 1414); margin m = 4u; gutter g = W ÷ 83 (12 px at 1000); column c = (W − 2m − 5g) ÷ 6 (138 px); track k starts at m + k(c + g). Verticals are multiples of u.
1. **Plate:** bleeds on three sides, ends on a module line at 0.356 H (36u; 504 px). Holds photograph, lockup, marks; nothing else.
2. **Display word:** spans W − 2m. Cap top on 26u; plate edge crosses 56% down the caps. Small word flush left and Chinese title flush right on one baseline above.
3. **Page:** axis A is track 0 (English, times); axis B track 1 (talk titles); axis D track 3 (Chinese, doors, speakers). English left, Chinese right, same row for the same fact.
4. **Reading order:** word, what, when and where, running order, foyer and entry. Groups 1.5u–3u apart; two 2 px rules open the dated block and the running order; nothing else ruled.
5. **Marks:** corner marks inside the plate 2u from the trim, 2u long; ticks at the trim start and end each track.

## Shapes
No radius, shadow, border or card. Rules: 2 px ink, content width. Marks: 2 px accent, drawn in code. Nothing imitates a photograph. The only gradient is the hard stop: two flat ink fields.

## Components
- **Plate.** Ink bleed field, photograph detail in the lower and right shadows. Ban: stock picture, drawn figure, gradient, scrim.
- **Credit line.** Ash, 15 px, 56 px from the left; FPO in the accent until delivery, then model, garment, photographer. Ban: invented name.
- **Display word.** One live text element, hard-stop split at the plate edge. Ban: two copies, outline, shadow, script, centred axis.
- **Lockup.** Small italic word left, Chinese title right, one baseline. Ban: third line, size between.
- **Statement row.** English at A, Chinese at D, 30 px, three lines at most. Ban: kicker.
- **Dated block.** Date in Bodoni 600 at 46 px, then time and doors, then place; English at A, Chinese or second fact at D. Ban: icons.
- **Running order.** Rows of 63 px: time at A, title at B in Bodoni 700, speaker at D in muted, one baseline. Ban: numbering, card, portrait.
- **Foyer and entry.** Reading size, English at A across 564 px, entry in both languages last. Ban: button, badge.
- **Disclosure.** For an illustrative programme: 30 px paper on the plate, top left, read first. Ban: footnote.

## Do's and Don'ts
- **Cut the picture and the word with the same line;** both halves legible.
- **Keep the page quiet:** one grotesque size, one Didone size, white. Every fact 30 px or more.
- **Test:** remove the type and the crop loses its composition; remove the photograph and the type loses its edge.
- **Refuse:** centred Didone logo, gold, glass, script, Bodoni body text, the cream-vermilion-numeral default.

## Variations
- **Symmetric axis.** Opening poster or cover only: display word and lockup centred at x = W ÷ 2; once per series.
- **Pause.** Reminder or reprint card: plate 0.3 H, display word alone on its edge, one line of reading; one per run, never beside a loud poster.

## Record
Folio version: 1.0.0. Template version: 13. Date: 2026-11-02.
Pieces: the-grid/brief.md.
