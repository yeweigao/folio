# Sound · Apple + Bang & Olufsen

Audio as material sculpture in Apple + Bang & Olufsen: every unit divided between aluminium and oak.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are px at S = 1000, S the format's short side, and scale with it; each is a floor for how far the format is read from, never a ceiling. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath; form names are the maker's, never set on the page. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Bang & Olufsen style — Divide every unit between two materials at the golden section and let the object sit on the seam; never a feature list, never a waveform posing as sound.

World: Sound's speakers, headphones, rooms and stories, on any surface. Every piece keeps the material split, the quiet grey and the plain sans; each brings its object as sculpture and one claim about listening.

Method:
1. Choose the object and the two materials it is made of.
2. Split the unit at the golden section between them.
3. Set the object across the seam, in a quiet light.
4. Say one thing about listening; measure it if it is a claim.

Amplitude: Reduced throughout; the cover is the largest, not the loudest.

Anti-reference: Grey minimal skin: empty white, a thin sans, nothing to hold.

## Images

Renders of fictional audio objects — anodised aluminium with brushed highlights, oak grain, woven textile; a soft key light, a contact shadow — declared once. On a cover the object owns half the field or more. No waveform or room scene as evidence for sound.

## Layout

Grid system: Split field — two material fields at the golden section, the object on the seam.

Twelve tracks from W × H: margin max(5% W, 6% S), gutter 1.25% W, an 8 px module. The seam falls at 0.618 of the width or height; type sits wholly in one field, never across the seam. Formats: on a 1600 × 900 slide, critical content stays inside the central 84%, the slide title at least 90 px and body at least 33; a scrolling page reads the tokens as given at a 1440 px viewport, body never below 17 px; a shop subdivides the field into peer cards on hairlines.

## Typography

- Inter, a quiet neo-grotesque, for every role; Noto Sans SC for Chinese.
- Display 80 / 400; heading 56 / 400; lead 24 / 300; body 17 / 400; label 14; caption 12.

## Colors

Ground: Bang & Olufsen's quiet light grey; aluminium and wood bring the warmth.
- **canvas** `#f3f3f3` grey; **panel** white; **dark** `#282722` a listening room.
- **aluminium** `#d9d9d6` and **oak** `#b48a5f`: the two fields of the split.
- **ink** `#282722`, **muted** `#636159`; **onDark** white.
- **action** `#282722` quiet actions; **onAction** white.
- **hairline** `#d2d2d7` in reference rows only.

## Shapes

**The device: the material split.** Every unit is divided at the golden section — 0.618 of its width or its height — into two fields of different materials: aluminium and oak, or grey and dark. The seam is the only straight line; the object sits across it. The ratio never changes; which material takes the larger side, and whether the seam is vertical or horizontal, follow the composition.

Cards 18; controls 8; the object's own curves are modelled, never outlined. Every nonzero radius, pills included, takes Apple's continuous corner, copied, never derived; `border-radius`, `rect rx` and superellipses are other curves. A page built with Folio inlines `continuous-corner.js` and marks each box `data-cc="R"`. Anything else draws one of the two paths below, in units of R, with `transform="translate(x y) scale(R)"` and `vector-effect="non-scaling-stroke"`, filling in A = W ÷ R − 3.05732 and B = H ÷ R − 3.05732. R is at most half the short side, a box or a pill, never between; inner R = max(0, outer R − gap); fill, stroke, clip and focus ring share one path.

A box, both sides at least 3.06 R:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .23692 .07491 .457 .07491 .89717 v{B} c0 .44017 0 .66025 -.07491 .89717 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.23692 -.07491 -.457 -.07491 -.89717 v-{B} c0 -.44017 0 -.66025 .07491 -.89717 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

A pill, R = H ÷ 2:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .18851 .07491 .32851 .07491 .36851 c0 .04 0 .18 -.07491 .36851 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.18851 -.07491 -.32851 -.07491 -.36851 c0 -.04 0 -.18 .07491 -.36851 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

## Forms

- **Cover:** the object on the seam at half the field or more, one claim in the larger field.
- **Statement:** one sentence in the larger field, the other field bare material.
- **Exhibit:** a material detail at macro scale filling one field.
- **Data:** one measured figure in one field, its label beneath.
- **Sequence and comparison:** finishes side by side, each split the same way.
- **Collection:** products on white cards, each card split at the same ratio.
- **Reference and close:** rows in the aluminium field; the close is the object on the seam.

## Variations

- **Room turn:** one unit on dark, the split between room and object; once per sequence.
- **Rotation:** one unit turns the seam horizontal.

## Do's and Don'ts

- **Look before delivering:** the seam must read at 0.618 at thumbnail; a third field, type across the seam, a waveform or a feature list are faults.
- **Floors:** facts verbatim and live; renders declared once per piece, in the fine print; every pair in Tokens holds its contrast.
- **Test:** cover the names and pour in new content: two materials at the golden section with the object on the seam still say Sound.
- **Caricature:** plastic chrome; a waveform as proof; a spec grid.

## Tokens

Authored for this fictional world at S = 1000. 

```yaml
colors:
  canvas: "#f3f3f3"
  panel: "#ffffff"
  dark: "#282722"
  ink: "#282722"
  muted: "#636159"
  action: "#282722"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
  aluminium: "#d9d9d6"
  oak: "#b48a5f"
  aluminium: "#d9d9d6"
  oak: "#b48a5f"
typography:
  display: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 80, fontWeight: 400, lineHeight: 1.05 }
  heading: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 56, fontWeight: 400, lineHeight: 1.07 }
  lead: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 24, fontWeight: 300, lineHeight: 1.5 }
  body: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.47 }
  label: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  caption: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 12, fontWeight: 400, lineHeight: 1.5 }
spacing:
  unit: 8
  textInset: 12
  cardInset: 24
  proofGap: 40
  tileInset: 80
rounded:
  control: 8
  card: 18
corners:
  contour: "continuous corner"
  smoothing: 0.6
  shoulderExtent: 1.52866
  innerRadius: "max(0, outerRadius - gap)"
pairs:
  ink-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}" }
  ink-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.ink}" }
  muted-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.muted}" }
  muted-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.muted}" }
  onDark-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.onDark}" }
  onAction-on-action: { backgroundColor: "{colors.action}", textColor: "{colors.onAction}" }
  action-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.action}" }
  action-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.action}" }
  ink-on-aluminium: { backgroundColor: "{colors.aluminium}", textColor: "{colors.ink}" }
  ink-on-aluminium: { backgroundColor: "{colors.aluminium}", textColor: "{colors.ink}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-07.
Pieces: quietest-setting (Keynote, 1600 × 900), three-surfaces (Store, 1440 × 1000), one-sheet (Editorial, 1200 × 1600); each uses its brief and this DESIGN, each made from an earlier version of this file, each made from an earlier version of this file. Sound and every product, figure and price are fictional; no Bang & Olufsen product, photograph, logo or font file is used. Changes after the lock: rewritten around the world's device; the pieces predate it.
