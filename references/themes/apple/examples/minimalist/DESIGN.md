# Mono · Apple + Braun

A small radio house in Apple + Braun: white and grey, and one coloured control.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are px at S = 1000, S the format's short side, and scale with it; each is a floor for how far the format is read from, never a ceiling. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath; form names are the maker's, never set on the page. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Braun style — Make every unit white and grey with one coloured control marking its lead; never a second colour, never a feature that does not change use.

World: Mono's radios and systems, launches, shop and stories, on any surface. Every piece keeps the one coloured control, the grey-white field and the plain sans; each brings its object straight on and the one thing it lets you do.

Method:
1. Find the one control that changes use on this unit: a knob, an action, a figure.
2. Draw the object straight on, as a system of parts.
3. Mark the lead with the coloured control and nothing else.
4. Remove what does not change use; stop there.

Amplitude: Full on covers and exhibits; reduced in the shop and reference.

Anti-reference: Grey minimal skin: empty white, a thin sans, nothing to hold.

## Images

Renders of fictional objects drawn straight on — matte plastic, aluminium, a soft key light, a contact shadow — at half the frame or more on a cover, declared once. Parts align to the grid; nothing nostalgic.

## Layout

Grid system: System field — the object's own module is the page module.

Twelve tracks from W × H: margin max(5% W, 6% S), gutter 1.25% W, an 8 px module equal to the object's smallest part. Labels sit on the object's axes; nothing floats off the grid. Formats: on a 1600 × 900 slide, critical content stays inside the central 84%, the slide title at least 90 px and body at least 33; a scrolling page reads the tokens as given at a 1440 px viewport, body never below 17 px; a shop subdivides the field into peer cards on hairlines.

## Typography

- Inter, the neo-grotesque of the Rams lineage, for every role, regular weight; Noto Sans SC for Chinese.
- Display 80 / 400; heading 52 / 400; lead 24 / 400; body 17 / 400; label 14; caption 12.
- One weight; hierarchy by size and position alone.

## Colors

Ground: Braun's white and light grey.
- **canvas** `#f4f4f4` grey; **panel** white; **dark** `#242424` a turn.
- **ink** `#242424`, **muted** `#626262`; **onDark** white.
- **action** `#242424` square actions in ink; **onAction** white.
- **control** `#a94725`: the one coloured control, large sizes only.
- **hairline** `#d2d2d7` in reference rows.

## Shapes

**The device: the one coloured control.** A single circle in control colour, diameter S / 40, marks the unit's lead: the knob on the object, the start of the headline, the key figure, the action. One per unit; it may sit on any of these, it never doubles, never becomes text colour for a sentence, never grows into a field.

Actions and cards are square except product cards, 18; the circle is the only curve besides the object. Every nonzero radius, pills included, takes Apple's continuous corner, copied, never derived; `border-radius`, `rect rx` and superellipses are other curves. A page built with Folio inlines `continuous-corner.js` and marks each box `data-cc="R"`. Anything else draws one of the two paths below, in units of R, with `transform="translate(x y) scale(R)"` and `vector-effect="non-scaling-stroke"`, filling in A = W ÷ R − 3.05732 and B = H ÷ R − 3.05732. R is at most half the short side, a box or a pill, never between; inner R = max(0, outer R − gap); fill, stroke, clip and focus ring share one path.

A box, both sides at least 3.06 R:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .23692 .07491 .457 .07491 .89717 v{B} c0 .44017 0 .66025 -.07491 .89717 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.23692 -.07491 -.457 -.07491 -.89717 v-{B} c0 -.44017 0 -.66025 .07491 -.89717 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

A pill, R = H ÷ 2:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .18851 .07491 .32851 .07491 .36851 c0 .04 0 .18 -.07491 .36851 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.18851 -.07491 -.32851 -.07491 -.36851 c0 -.04 0 -.18 .07491 -.36851 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

## Forms

- **Cover:** the object straight on at half the frame or more, the control on its knob.
- **Statement:** one sentence, the control before its first word.
- **Exhibit:** the object's parts exploded on the grid, the control on the part that matters.
- **Data:** one figure with the control beside it, its label beneath.
- **Sequence and comparison:** models in a row at one scale, the control on the difference.
- **Collection:** models on white cards, name and price flush left.
- **Reference and close:** rows on grey; the close is the object and the control.

## Variations

- **Dark turn:** one unit on dark, the control unchanged; once per sequence.
- **Top view:** one unit seen from above, the module visible.

## Do's and Don'ts

- **Look before delivering:** exactly one coloured circle per unit, readable at thumbnail; a second colour, retro styling, or parts off the grid are faults.
- **Floors:** facts verbatim and live; renders declared once per piece, in the fine print; every pair in Tokens holds its contrast.
- **Test:** cover the names and pour in new content: grey and white with one coloured control still say Mono.
- **Caricature:** retro nostalgia; a decorative colour; empty white with nothing to hold.

## Tokens

Authored for this fictional world at S = 1000. 

```yaml
colors:
  canvas: "#f4f4f4"
  panel: "#ffffff"
  dark: "#242424"
  ink: "#242424"
  muted: "#626262"
  onDark: "#ffffff"
  action: "#242424"
  onAction: "#ffffff"
  control: "#a94725"
  hairline: "#d2d2d7"
typography:
  display: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 80, fontWeight: 400, lineHeight: 1.05 }
  heading: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 52, fontWeight: 400, lineHeight: 1.1 }
  lead: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 24, fontWeight: 400, lineHeight: 1.45 }
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
  control: 0
pairs:
  ink-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}" }
  ink-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.ink}" }
  muted-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.muted}" }
  muted-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.muted}" }
  onDark-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.onDark}" }
  onAction-on-action: { backgroundColor: "{colors.action}", textColor: "{colors.onAction}" }
  control-on-canvas-large: { backgroundColor: "{colors.canvas}", textColor: "{colors.control}" }
  control-on-panel-large: { backgroundColor: "{colors.panel}", textColor: "{colors.control}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-07.
Pieces: one-knob (Keynote), three-models (Bento), inside (Editorial), each made from an earlier version of this file, each made from an earlier version of this file, each made from an earlier version of this file, each made from an earlier version of this file. Mono and every model, measurement, price and part are fictional; no Braun product, photograph, logo or font file is used. Changes after the lock: rewritten around the world's device; the pieces predate it.
