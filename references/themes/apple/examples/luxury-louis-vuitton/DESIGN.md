# Voyager · Apple + Louis Vuitton

A leather house in Apple + Louis Vuitton: white, a serif, and every unit cut 4 : 2 : 1.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are px at S = 1000, S the format's short side, and scale with it; each is a floor for how far the format is read from, never a ceiling. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath; form names are the maker's, never set on the page. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Louis Vuitton style — Cut every unit into three fields, 4 : 2 : 1, the lead whole in the largest, on white; never the monogram as wallpaper, never a catalogue grid posing as a flagship.

World: Voyager's objects, collections, flagship and stories, on any surface. Every piece keeps the 4 : 2 : 1 field, the white page and the serif; each brings its lead, its claim and its facts, the three the field holds.

Method:
1. Find the lead, the claim and the facts.
2. Give the lead the 4, whole: the object, or the headline at display size.
3. The claim takes the 2; the name and facts take the 1.
4. Part the fields by white space alone.

Amplitude: Full in the 4; reduced in the 2, the 1 and reference.

Anti-reference: Fake luxury: gold, glowing outlines, spaced serif capitals over a stock photograph.

## Images

Renders of fictional leather goods, modelled — key light, grain from `feTurbulence` lighting, painted edges, saddle stitches, contact shadow — on white or stone, declared once. An object owns the 4; where the 2 and the 1 show it too, each goes a doubling closer — a seam, then the grain — never smaller in its subject.

## Layout

Grid system: Field of 4 : 2 : 1 — three fields along the unit's long side, largest first.

Twelve tracks from W × H: margin max(5% W, 6% S), gutter 1.25% W, an 8 px module. Inside the margins the long side divides 4 : 2 : 1, the gaps one gutter: on 1080 × 1440 about 733, 367 and 183 px top to bottom; on 1600 × 900 about 807, 404 and 202 px left to right. Captions hang on one baseline. Formats: on a 1600 × 900 slide, critical content stays inside the central 84%, the slide title at least 90 px and body at least 33; a scrolling page reads the tokens as given at a 1440 px viewport, body never below 17 px; a shop subdivides the field into peer cards on hairlines.

## Typography

- Cormorant Garamond for display and heading; Inter for lead, body and labels; Noto Serif SC and Noto Sans SC for Chinese.
- Display 80 / 400; heading 56 / 400; lead 24 / 300; body 17 / 400; label 14; caption 12.

## Colors

Ground: Louis Vuitton's white; brown is the leather's, never the page's.
- **canvas** white; **panel** `#f3f2f0` stone, under collection cards; **dark** `#30271d` a night unit.
- **ink** `#30271d`, **muted** `#686056`; **onDark** white.
- **action** `#30271d` black-brown pills; **onAction** white.
- **hideLight** `#d4c2a6`, **hideMid** `#9e805d`, **hideDark** `#49372a`, **thread** `#e4d3b5`: a leather render's own colours, never interface.
- **hairline** `#d2d2d7` in reference rows.

## Shapes

**The device: the 4 : 2 : 1 field.** Every unit divides its long side, inside the margins, into three fields of 4 : 2 : 1, largest first — top to bottom on a tall frame, left to right on a wide one. The 4 holds the lead whole; the 2 the claim; the 1 the name and facts. The fields part by white space alone. Never a fourth field, a reversed order, or a rule or label between them.

Cards 18; actions full pills; the fields are square. Every nonzero radius, pills included, takes Apple's continuous corner, copied, never derived; `border-radius`, `rect rx` and superellipses are other curves. A page built with Folio inlines `continuous-corner.js` and marks each box `data-cc="R"`. Anything else draws one of the two paths below, in units of R, with `transform="translate(x y) scale(R)"` and `vector-effect="non-scaling-stroke"`, filling in A = W ÷ R − 3.05732 and B = H ÷ R − 3.05732. R is at most half the short side, a box or a pill, never between; inner R = max(0, outer R − gap); fill, stroke, clip and focus ring share one path.

A box, both sides at least 3.06 R:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .23692 .07491 .457 .07491 .89717 v{B} c0 .44017 0 .66025 -.07491 .89717 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.23692 -.07491 -.457 -.07491 -.89717 v-{B} c0 -.44017 0 -.66025 .07491 -.89717 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

A pill, R = H ÷ 2:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .18851 .07491 .32851 .07491 .36851 c0 .04 0 .18 -.07491 .36851 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.18851 -.07491 -.32851 -.07491 -.36851 c0 -.04 0 -.18 .07491 -.36851 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

## Forms

- **Cover:** the object or the headline in the 4, the claim in the 2, the name in the 1.
- **Statement:** one serif line filling the 4; the 2 and the 1 nearly empty.
- **Exhibit:** the object whole in the 4, a seam a doubling closer in the 2, the grain in the 1.
- **Data:** the figure at display size in the 4, what it measures in the 2, its source in the 1.
- **Sequence and comparison:** peers share the 4 at one scale; the difference in the 2.
- **Collection:** objects on stone cards across the 4, the chosen one named in the 2, prices in the 1.
- **Reference and close:** rows on white in the 4; the close is one serif line in the 4.

## Variations

- **Grain field:** one unit where a material fills the 4; once per sequence.
- **Night turn:** one unit on dark, the field unchanged.

## Do's and Don'ts

- **Look before delivering:** the three fields read 4 : 2 : 1 at thumbnail; equal fields, a fourth, a rule between them, or the monogram are faults.
- **Floors:** facts verbatim and live; renders declared once per piece, in the fine print; every pair in Tokens holds its contrast.
- **Test:** cover the names and pour in new content: white pages cut 4 : 2 : 1 under a serif still say Voyager.
- **Caricature:** the monogram as wallpaper; a catalogue grid; gold.

## Tokens

Authored for this fictional world at S = 1000. 

```yaml
colors:
  canvas: "#ffffff"
  panel: "#f3f2f0"
  dark: "#30271d"
  ink: "#30271d"
  muted: "#686056"
  onDark: "#ffffff"
  action: "#30271d"
  onAction: "#ffffff"
  hairline: "#d2d2d7"
  hideLight: "#d4c2a6"
  hideMid: "#9e805d"
  hideDark: "#49372a"
  thread: "#e4d3b5"
typography:
  display: { fontFamily: "Cormorant Garamond, Noto Serif SC, serif", fontSize: 80, fontWeight: 400, lineHeight: 1.02 }
  heading: { fontFamily: "Cormorant Garamond, Noto Serif SC, serif", fontSize: 56, fontWeight: 400, lineHeight: 1.08 }
  lead: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 24, fontWeight: 300, lineHeight: 1.5 }
  body: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.5 }
  label: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  caption: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 12, fontWeight: 400, lineHeight: 1.45 }
spacing:
  module: 8
  gutter: 20
  group: 32
  section: 64
  cardInset: 24
rounded:
  plate: 18
  card: 18
  action: 999
pairs:
  ink-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}" }
  ink-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.ink}" }
  muted-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.muted}" }
  muted-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.muted}" }
  onDark-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.onDark}" }
  onAction-on-action: { backgroundColor: "{colors.action}", textColor: "{colors.onAction}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-07.
Pieces: eight-stitches (Keynote), three-sizes (Bento), from-the-whole (Editorial), each made from an earlier version of this file, each made from an earlier version of this file, each made from an earlier version of this file, each made from an earlier version of this file. Voyager and every object, material, figure and price are fictional; no Louis Vuitton product, mark, photograph, monogram or font file is used. Changes after the lock: rewritten around the world's device; the pieces predate it.
