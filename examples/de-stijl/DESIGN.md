# De Stijl, Mondrian · the balanced composition

Black bars on the tracks and unequal planes of red, yellow, blue, white and grey, each plane carrying one fact, tuned one bar at a time until the balance holds.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. Check the piece against Do's and Don'ts.

## Overview

De Stijl, Piet Mondrian — the Compositions (1921–30): set black bars on the tracks, give each plane one fact and one colour by its job, then move one bar or resize one plane at a time and re-render until no change improves the balance; never a centred title block, a diagonal, or two equal cells.

World: any content, on any surface. Its measure (durations, shares, counts, ranks) sizes the planes; without a measure, its order of importance does. Every piece keeps the bars, the palette, the faces and the colour roles; each brings its facts and its measure.

Method:
1. Find the measure and give it one scale per unit.
2. Place the bars the measure fixes, then free bars by eye.
3. Colour by job: red leads, blue answers, yellow measures, white and grey are read.
4. Set type flush left inside the planes, never on a bar.
5. Tune: one bar or one plane per render, until no move improves the balance. A plane whose change alters nothing is decoration; remove it.

Amplitude: full in structure; every plane carries a fact or a weight the balance needs.

Anti-reference: a cream sheet with one red square; a black lattice over an ordinary page; Mondrian as a border.

## Images

None by default: bars and planes are the image. When the content is an object the reader must recognize, one real photograph may fill one plane edge to edge, as van der Leck flattened a product into a plane; never an illustration inside a plane.

## Layout

Grid system: Hierarchical — zones sized by the weight of their content, drawn as bars.

S = min(W, H); bar b = S ÷ 62; everything snaps to b ÷ 2. Six tracks, twelve where W > 1.4 H; bars fall on track lines. One spine, a full-length bar at about 0.62 of the width (0.38 or 0.62 in landscape), never the centre. On a spread the physical fold is a cut, not a spine: planes stop at it or cross it whole, and nothing mirrors around it. Planes bleed off at least two edges; no frame. A measured plane is its value times the scale; a plane too small for its text merges with its neighbour, and the merge is stated. Space is never left over: an empty plane is white or grey by its weight and passes the tuning like any other.

## Typography

- **Anybody** (OFL, variable width): display 900, width 100, at 200; numerals 900 at 62 (width 64 for ranges); text 800, width 84, at 40; body 600, width 84, at 28.
- **Noto Sans SC** 700 and 900: display at 150, text and body at the Latin size.
- A title too wide for its plane steps down by 8, never compressed. Latin titles in capitals; no italic, no tracking; tabular figures. Nothing read below 28.

## Colors

- **Ink `#111111` (primary).** Bars, and type on white, yellow and grey.
- **Ground `#F2F1EC` (neutral).** The white plane, and type on red and blue.
- **Red `#D02A1E`.** The lead: the largest coloured plane. At most 15%.
- **Blue `#1F3F9A`.** The answer: the second language, the invitation. At most 15%.
- **Yellow `#F5C400`.** Quantities only. A plane, never a mark.
- **Grey `#D6D5CF`.** Receding reading.
- Ink never on red or blue. Primaries together at most 40%. Emphasis is the plane's size or place, never a new hue.

## Shapes

Radius 0. Bars in ink, b thick, horizontal or vertical, each ending on a bar or an edge. Nothing else is drawn.

## Forms

- **Cover:** the title on the red lead plane; the second language on blue; the date or key figure on yellow; what it is on white.
- **Statement:** one sentence on the largest white plane, the bars around it unequal.
- **Exhibit:** one photograph as a plane, its caption on the grey plane beside it.
- **Data:** the title on the red plane; each value a yellow plane sized on one scale, label and value flush left inside; the rest grey.
- **Sequence and comparison:** planes in order, height as duration or weight; two series either side of the spine on one scale.
- **Reference and close:** white planes of body text; the next action on blue.

## Variations

- **Boogie bar** (*Broadway Boogie Woogie*, 1942–43). One bar that measures nothing breaks into segments of the primaries and grey, each at least 2.5b; once per deliverable, at a close.
- **Counter-composition** (van Doesburg). The whole field turned 45°, the scale dropped; only for content that is itself a rupture.

## Do's and Don'ts

- **Look before delivering:** render it, see it full size and as a thumbnail. Two equal cells, a plane that holds nothing, a plane whose change alters nothing: faults.
- **Floors:** facts verbatim and live; every pair in Tokens holds its contrast.
- **Test:** resize or recolour one plane, and the balance of the whole shifts.
- **Caricature:** a card grid filled red, yellow and blue; a black lattice laid over an ordinary page; Mondrian as a border.

## Tokens

```yaml
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
spacing:
  bar: 16
  snap: 8
  pad: 20
pairs:
  ground-on-red: { backgroundColor: "{colors.red}", textColor: "{colors.neutral}" }
  ground-on-blue: { backgroundColor: "{colors.blue}", textColor: "{colors.neutral}" }
  ink-on-yellow: { backgroundColor: "{colors.yellow}", textColor: "{colors.primary}" }
  ink-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.primary}" }
  ink-on-grey: { backgroundColor: "{colors.grey}", textColor: "{colors.primary}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-02.
Pieces: the-grid/brief.md, made from the earlier, programme-bound version of this file; the system it shows is unchanged.
