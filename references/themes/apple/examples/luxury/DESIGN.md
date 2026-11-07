# Atelier · Apple + Hermès

A leather house in Apple + Hermès: white, one orange, every line a stitch.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are px at S = 1000, S the format's short side, and scale with it; each is a floor for how far the format is read from, never a ceiling. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath; form names are the maker's, never set on the page. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Hermès style — Make every unit hold one object and draw every line as a stitch in the house orange; never a second accent, never a craft claim without its detail.

World: Atelier's objects, collections, workshop and stories, on any surface. Every piece keeps the stitched rule, the white page and the serif; each brings its object and the craft detail that proves it.

Method:
1. Choose the one object and the one detail of its making that proves it.
2. Give the object the field; give the detail a close plate.
3. Divide and underline only with the stitch.
4. Let price sit quiet beside the name, never above it.

Amplitude: Full on covers and details; reduced in the range and reference.

Anti-reference: Fake luxury: gold, glowing outlines, spaced serif capitals over a stock photograph.

## Images

Renders of fictional leather goods, modelled — key light, grain from `feTurbulence` lighting, painted edges, contact shadow — on white or the house paper, declared once. On a cover the object or its craft detail takes half the frame or more. No house mark, pattern or photograph borrowed.

## Layout

Grid system: Atelier field — one object per unit, its detail on a plate that shares its baseline.

Twelve tracks from W × H: margin max(5% W, 6% S), gutter 1.25% W, an 8 px module. The object spans seven tracks, the detail plate four; captions hang from the stitch beneath them. Formats: on a 1600 × 900 slide, critical content stays inside the central 84%, the slide title at least 90 px and body at least 33; a scrolling page reads the tokens as given at a 1440 px viewport, body never below 17 px; a shop subdivides the field into peer cards on hairlines.

## Typography

- Cormorant Garamond for display and heading; Inter for lead, body and labels; Noto Serif SC and Noto Sans SC for Chinese.
- Display 72 / 400; heading 52 / 400; lead 28 / 300; body 17 / 400; product 21 / 600; price 17 / 400; label 14; caption 12.
- Price never larger than the product name.

## Colors

Ground: Hermès white, its warm panel the house's paper; orange is the one accent.
- **canvas** white; **panel** `#f7f3eb` the house paper; **dark** `#24211d` a night unit.
- **ink** `#24211d`, **muted** `#67615a`; **onDark** white, **mutedDark** `#c4bcb2` on dark.
- **action**, **link** and **focus** `#a74b00` the house orange — the stitch, the link, the one action; **darkLink** `#ffc28a` on dark; **onAction** white.
- **leather** `#d8c8ad`, **leatherLight** `#e9e0cf`, **leatherMid** `#c1b29a`, **leatherDark** `#857359`, **wood** `#dbd4c7`, **metal** `#b6b4ad`: the render's own materials, never interface.
- **hairline** `#d2d2d7` is replaced by the stitch wherever a line is seen.

## Shapes

**The device: the stitched rule.** Every line a reader sees — divider, underline, frame edge — is a saddle stitch in the house orange: dashes 0.6 % S long and 0.25 % S thick, slanted 20°, spaced 0.4 % S. It may run horizontal or vertical, short or full width; it never curves into ornament, never doubles, never changes colour.

Cards 18; controls 12; actions full pills. Every nonzero radius, pills included, takes Apple's continuous corner, copied, never derived; `border-radius`, `rect rx` and superellipses are other curves. A page built with Folio inlines `continuous-corner.js` and marks each box `data-cc="R"`. Anything else draws one of the two paths below, in units of R, with `transform="translate(x y) scale(R)"` and `vector-effect="non-scaling-stroke"`, filling in A = W ÷ R − 3.05732 and B = H ÷ R − 3.05732. R is at most half the short side, a box or a pill, never between; inner R = max(0, outer R − gap); fill, stroke, clip and focus ring share one path.

A box, both sides at least 3.06 R:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .23692 .07491 .457 .07491 .89717 v{B} c0 .44017 0 .66025 -.07491 .89717 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.23692 -.07491 -.457 -.07491 -.89717 v-{B} c0 -.44017 0 -.66025 .07491 -.89717 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

A pill, R = H ÷ 2:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .18851 .07491 .32851 .07491 .36851 c0 .04 0 .18 -.07491 .36851 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.18851 -.07491 -.32851 -.07491 -.36851 c0 -.04 0 -.18 .07491 -.36851 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

## Forms

- **Cover:** the object at half the frame or more, the serif name, a stitch beneath it.
- **Statement:** one serif line at display size over a stitch.
- **Exhibit:** the craft detail at macro scale, caption hung from a stitch.
- **Data:** one figure in the serif, its label beneath a stitch.
- **Sequence and comparison:** the making in steps, divided by stitches; sizes at one scale.
- **Collection:** objects on the house paper, one per card, name then quiet price.
- **Reference and close:** rows divided by stitches; the close is one object and one line.

## Variations

- **Night turn:** one unit on dark, the stitch in darkLink; once per sequence.
- **Hand turn:** one unit shows the hand at work at macro scale, the stitch being made.

## Do's and Don'ts

- **Look before delivering:** every visible line must be a stitch at thumbnail; a straight rule, a second accent, a price louder than the name are faults.
- **Floors:** facts verbatim and live; renders declared once per piece, in the fine print; every pair in Tokens holds its contrast.
- **Test:** cover the names and pour in new content: white, one orange and every line stitched still say Atelier.
- **Caricature:** gold, a monogram wallpaper, spaced capitals over a stock photograph.

## Tokens

Authored for this fictional world at S = 1000. 

```yaml
colors:
  canvas: "#ffffff"
  panel: "#f7f3eb"
  dark: "#24211d"
  ink: "#24211d"
  muted: "#67615a"
  mutedDark: "#c4bcb2"
  action: "#a74b00"
  link: "#a74b00"
  focus: "#a74b00"
  darkLink: "#ffc28a"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
  leather: "#d8c8ad"
  leatherLight: "#e9e0cf"
  leatherMid: "#c1b29a"
  leatherDark: "#857359"
  wood: "#dbd4c7"
  metal: "#b6b4ad"
typography:
  display: { fontFamily: "Cormorant Garamond, Noto Serif SC, serif", fontSize: 72, fontWeight: 400, lineHeight: 1.05 }
  heading: { fontFamily: "Cormorant Garamond, Noto Serif SC, serif", fontSize: 52, fontWeight: 400, lineHeight: 1.08 }
  lead: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 28, fontWeight: 300, lineHeight: 1.35 }
  body: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.55 }
  product: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 21, fontWeight: 600, lineHeight: 1.3 }
  price: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.4 }
  label: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  caption: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 12, fontWeight: 400, lineHeight: 1.5 }
spacing:
  unit: 8
  pair: 16
  group: 24
  section: 64
  objectInset: 80
  cardInset: 24
rounded:
  card: 18
  control: 12
  action: "pill"
corners:
  contour: "continuous corner"
  shoulderExtent: 1.52866
  innerRadius: "max(0, outerRadius - gap)"
pairs:
  ink-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}" }
  ink-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.ink}" }
  muted-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.muted}" }
  muted-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.muted}" }
  mutedDark-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.mutedDark}" }
  onDark-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.onDark}" }
  onAction-on-action: { backgroundColor: "{colors.action}", textColor: "{colors.onAction}" }
  action-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.action}" }
  link-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.link}" }
  darkLink-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.darkLink}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-07.
Pieces: the-making (Keynote), the-range (Bento), the-workshop (Editorial), each made from an earlier version of this file, each made from an earlier version of this file. Atelier and its goods are fictional; no Hermès product, mark, pattern, photograph or font file is used. Changes after the lock: rewritten around the world's device; the pieces predate it.
