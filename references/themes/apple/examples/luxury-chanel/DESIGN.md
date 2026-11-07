# Noir · Apple + Chanel

A fashion house in Apple + Chanel: white, and one black band.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are px at S = 1000, S the format's short side, and scale with it; each is a floor for how far the format is read from, never a ceiling. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath; form names are the maker's, never set on the page. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Chanel style — Set every unit in white with one black band across it, the claim knocked out inside; never a colour, never gold, never a headline louder than the garment.

World: Noir's garments, collections, fragrance and stories, on any surface. Every piece keeps the black band, the white page and the serif; each brings its garment or object and one line.

Method:
1. Choose the garment or object and give it the white field.
2. Lay the band on the third that leaves the garment whole.
3. Knock the claim out of the band, in the serif.
4. Everything else is quiet sans on white.

Amplitude: Full on covers and campaign units; reduced in the collection and reference.

Anti-reference: Fake luxury: gold, glowing outlines, spaced serif capitals over a stock photograph.

## Images

Renders and illustrations of fictional garments in black, white and grey — modelled cloth, tweed texture by `feTurbulence`, a contact shadow — declared once. On a cover the garment owns half the field or more. No house mark, interlocking letter or photograph borrowed.

## Layout

Grid system: Band field — one horizontal black band on a third line, white above and below.

Twelve tracks from W × H: margin max(5% W, 6% S), gutter 1.25% W, an 8 px module. The band sits on the upper or lower third; the garment may cross it, the band never cuts its face or hands. Formats: on a 1600 × 900 slide, critical content stays inside the central 84%, the slide title at least 90 px and body at least 33; a scrolling page reads the tokens as given at a 1440 px viewport, body never below 17 px; a shop subdivides the field into peer cards on hairlines.

## Typography

- Cormorant Garamond for display and heading; Inter for lead, body and labels; Noto Serif SC and Noto Sans SC for Chinese.
- Display 80 / 400; heading 56 / 400; lead 24 / 300; body 17 / 400; label 14; caption 12.
- Inside the band only the serif, white.

## Colors

Ground: Chanel's white and black.
- **canvas** white; **panel** `#f5f5f5` the collection; **dark** `#111111` the band and only black field.
- **ink** `#111111`, **muted** `#626262`; **onDark** white inside the band.
- **action** `#111111` black pills; **onAction** white.
- **hairline** `#d2d2d7` in reference rows.

## Shapes

**The device: the black band.** One full-width band of dark, height S / 6, on the upper or the lower third line; the claim knocked out in the serif, set within its middle 60%. One per unit; it moves between the thirds, it never thickens, tilts, fades, or holds anything but type.

Cards 18; actions full pills; the band is square. Every nonzero radius, pills included, takes Apple's continuous corner, copied, never derived; `border-radius`, `rect rx` and superellipses are other curves. A page built with Folio inlines `continuous-corner.js` and marks each box `data-cc="R"`. Anything else draws one of the two paths below, in units of R, with `transform="translate(x y) scale(R)"` and `vector-effect="non-scaling-stroke"`, filling in A = W ÷ R − 3.05732 and B = H ÷ R − 3.05732. R is at most half the short side, a box or a pill, never between; inner R = max(0, outer R − gap); fill, stroke, clip and focus ring share one path.

A box, both sides at least 3.06 R:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .23692 .07491 .457 .07491 .89717 v{B} c0 .44017 0 .66025 -.07491 .89717 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.23692 -.07491 -.457 -.07491 -.89717 v-{B} c0 -.44017 0 -.66025 .07491 -.89717 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

A pill, R = H ÷ 2:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .18851 .07491 .32851 .07491 .36851 c0 .04 0 .18 -.07491 .36851 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.18851 -.07491 -.32851 -.07491 -.36851 c0 -.04 0 -.18 .07491 -.36851 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

## Forms

- **Cover:** the garment whole on white, the band across a third with the name.
- **Statement:** the band alone, one serif line, white field around it.
- **Exhibit:** a construction detail at macro scale, the band below it.
- **Data:** one figure in the band, its label in sans on white beneath.
- **Sequence and comparison:** looks in a row at one scale, one band crossing them all.
- **Collection:** garments on panel cards, name then quiet price; the band names the collection.
- **Reference and close:** sans rows on white; the close is the band with one line.

## Variations

- **Black field:** one unit wholly dark, a white band across it; once per sequence.
- **Close crop:** the garment cropped to texture, the band unchanged.

## Do's and Don'ts

- **Look before delivering:** one band per unit, readable at thumbnail; a second black field, a colour, gold or a band cutting a face are faults.
- **Floors:** facts verbatim and live; renders declared once per piece, in the fine print; every pair in Tokens holds its contrast.
- **Test:** cover the names and pour in new content: white with one black band and the knocked-out serif still say Noir.
- **Caricature:** gold; an interlocking monogram; a colour field.

## Tokens

Authored for this fictional world at S = 1000. 

```yaml
colors:
  canvas: "#ffffff"
  panel: "#f5f5f5"
  dark: "#111111"
  ink: "#111111"
  muted: "#626262"
  onDark: "#ffffff"
  action: "#111111"
  onAction: "#ffffff"
  hairline: "#d2d2d7"
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
Pieces: one-jacket (Keynote), collection (Bento), archive (Editorial), each made from an earlier version of this file, each made from an earlier version of this file, each made from an earlier version of this file, each made from an earlier version of this file. Noir and its garments are fictional; no Chanel product, mark, photograph, pattern or font file is used. Changes after the lock: rewritten around the world's device; the pieces predate it.
