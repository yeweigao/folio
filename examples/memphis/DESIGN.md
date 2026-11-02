# Memphis, Sottsass · the clad primitive

Flat primitives cut from drawn laminates, clad in clashing hues, each standing on a solid slab that carries its words, assembled whole on a square module field.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. Check the piece against Do's and Don'ts.

## Overview

Memphis, Ettore Sottsass — the Bacterio laminate (1978) and the Carlton bookcase (1981): draw the pattern first as a tileable laminate, cut flat primitives from it, and assemble them on the module field until the format is the furniture; never a pattern that carries information, never a pattern behind reading text.

World: any content, on any surface. Serious content is translated, not refused: the clash marks its parts honestly, and its facts stay on solid ground. Every piece keeps the module, laminates, hues by role, faces and the tower; each brings its parts, their order, and the primitive each takes.

Method:
1. Draw the laminates as tileable patterns, each repeat derived from the primitive's side.
2. Cut one primitive per leading part; the part's subject picks it: square for what is built, triangle for what moves, disc for what turns or is whole.
3. Clad it in its laminate and its part's hue, and stand it on a solid slab of that hue carrying the words.
4. Tile the field whole: towers in the content's order, left to right, one module lower each; every other cell a solid fact block or a deliberate white.

Amplitude: full: hues clash, laminates run coarse, type is heavy; only the white and the text on solid ground stay quiet.

Anti-reference: the grey Swiss poster with one red square; Memphis as wallpaper; CSS objects with shadows.

## Images

Computed: laminates cut into primitives. Branzi may visit once: one real photograph cut to a primitive's outline, no pattern on it. Never an illustration.

## Layout

Grid system: Modular — every fact, form and block takes whole modules.

S = min(W, H); margin 0.04 S; gutter 0.4 × margin; six tracks, nine where W > 1.4 H; module = track width, square; rows = whole modules that fit, the rest a base band of at least 0.06 S. A tower is two modules plus a gutter square: primitive above, slab below. Two parts take three tracks each, three parts two; more parts start a second staircase. The title stands in the first rows at the left, one word per row; facts fill free cells in reading order. A cell with nothing to carry is white on purpose; none is left white by accident.

## Typography

- **League Spartan** (OFL; 600–900) for titles, figures and facts; **DM Serif Display Italic** (OFL) for voices only, the names of people and quoted words; **Noto Sans SC** (700, 900) for Chinese, never smaller than the Latin it translates.
- Display at a cap height of one module, one word per row; a word wider than the field drops to two thirds of a module, never compressed.
- Headline 64, numeral 84, title 44, voice 30, label 26; nothing read below 26.

## Colors

- **Ink `#111111` (primary).** Type on white, the title, ink blocks.
- **White `#FFFFFF` (neutral).** Ground, at least 40% of the area; type on cobalt and ink.
- **Cobalt `#2438E0`, rose `#FF4FA3`, lemon `#FFD21F`.** First, second, third part, then the cycle restarts; a hue stays with its part everywhere.
- **Mint `#00C389`.** One named category, held across the deliverable.
- White on cobalt and ink; ink on every other hue. Hues mark parts, never value or emphasis.

## Shapes

Radius zero; flat; no outline or shadow; one 6 ink rule over the base band. Primitives cut from a tower-side square: square; right triangle; disc with a quarter-side square gap turned 45°. Laminates: grid lines for the square, 45° stripes for the triangle, half-drop dots for the disc, each repeat a fraction of the side; cut off by the edge, never fitted, never behind text.

## Forms

- **Cover:** the title rows, the towers, the main facts in the free cells.
- **Statement:** one sentence at headline size on white, one tower as its counterweight.
- **Exhibit:** one tower at double size, its slab carrying the name.
- **Data:** each value on its part's slab, the figure at numeral size, the label beneath; the primitive says which part, never how much.
- **Sequence and comparison:** the staircase in order; two towers at one height on one row.
- **Reference and close:** label size on white cells; the next action on the base band.

## Variations

- **Night field.** The whole unit on ink, type white, towers unchanged.
- **Gap turned.** A second primitive turned 45° off axis.

## Do's and Don'ts

- **Look before delivering:** render it, see it full size and as a thumbnail. Text on pattern, a hue recoloured for balance, white nobody placed: faults.
- **Floors:** facts verbatim and live; every pair in Tokens holds its contrast; pattern never says anything.
- **Test:** remove the laminates and the staircase; if a neat table of coloured boxes remains, the clash was decoration.
- **Caricature:** squiggle confetti, black outlines everywhere, an 80s pastel palette, Memphis as wallpaper behind a Swiss page.

## Tokens

```yaml
colors:
  primary: "#111111"
  neutral: "#FFFFFF"
  cobalt: "#2438E0"
  rose: "#FF4FA3"
  lemon: "#FFD21F"
  mint: "#00C389"
typography:
  display: { fontFamily: "League Spartan, Noto Sans SC, sans-serif", fontSize: 212, fontWeight: 900, lineHeight: 0.74 }
  headline: { fontFamily: "League Spartan, Noto Sans SC, sans-serif", fontSize: 64, fontWeight: 800, lineHeight: 1.09 }
  numeral: { fontFamily: "League Spartan, Noto Sans SC, sans-serif", fontSize: 84, fontWeight: 900, lineHeight: 0.9 }
  title: { fontFamily: "League Spartan, Noto Sans SC, sans-serif", fontSize: 44, fontWeight: 800, lineHeight: 1.02 }
  voice: { fontFamily: "DM Serif Display, Noto Sans SC, serif", fontSize: 30, fontWeight: 400, lineHeight: 1.05 }
  label: { fontFamily: "League Spartan, Noto Sans SC, sans-serif", fontSize: 26, fontWeight: 800, lineHeight: 1.12 }
spacing:
  margin: 40
  gutter: 16
  module: 140
  rule: 6
pairs:
  ink-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.primary}" }
  ground-on-ink: { backgroundColor: "{colors.primary}", textColor: "{colors.neutral}" }
  ground-on-cobalt: { backgroundColor: "{colors.cobalt}", textColor: "{colors.neutral}" }
  ink-on-rose: { backgroundColor: "{colors.rose}", textColor: "{colors.primary}" }
  ink-on-lemon: { backgroundColor: "{colors.lemon}", textColor: "{colors.primary}" }
  ink-on-mint: { backgroundColor: "{colors.mint}", textColor: "{colors.primary}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-02.
Pieces: the-grid/brief.md, made from the earlier, programme-bound version of this file; the system it shows is unchanged.
