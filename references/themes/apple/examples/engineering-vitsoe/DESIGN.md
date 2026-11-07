# Shelf · Apple + Vitsoe

A modular shelving system in Apple + Vitsoe: a slot rail sets the module of every unit.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are px at S = 1000, S the format's short side, and scale with it; each is a floor for how far the format is read from, never a ceiling. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath; form names are the maker's, never set on the page. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Vitsoe style — Build every unit on a rail of slots at the shelf's own pitch and snap everything to it; never a dimension off the module, never a system shown only assembled.

World: Shelf's system, configurations, parts and stories, on any surface. Every piece keeps the slot rail, the white field and the plain sans; each brings its configuration, assembled and apart.

Method:
1. Find the module: the slot pitch.
2. Draw the rail at the left edge.
3. Snap every element's top edge to a slot.
4. Show the system assembled, then apart, on the same rail.

Amplitude: Reduced throughout; scale comes from the system, not the type.

Anti-reference: A furniture catalogue: lifestyle rooms and price stickers.

## Images

Renders of fictional shelving — powder-coated aluminium, oak shelves, a soft key light, contact shadows — drawn to the module, declared once. On a cover the system or a complete module occupies half the frame or more.

## Layout

Grid system: Rail field — one vertical slot rail sets the page module.

The pitch is S / 40; margins and gutters are whole pitches; the rail occupies the left margin full height. Every block's top edge sits on a slot; heights are whole pitches. Formats: on a 1600 × 900 slide, critical content stays inside the central 84%, the slide title at least 90 px and body at least 33; a scrolling page reads the tokens as given at a 1440 px viewport, body never below 17 px; a shop subdivides the field into peer cards on hairlines.

## Typography

- Inter, a plain neo-grotesque, for every role; Noto Sans SC for Chinese.
- Display 80 / 600; heading 56 / 600; lead 24 / 300; body 17 / 400; label 14; caption 12.
- Line heights round to the pitch.

## Colors

Ground: Vitsoe's white; colour comes from the shelf's materials.
- **canvas** white; **panel** `#f5f5f5` a light grey for configurations; **dark** `#2b302d` a turn.
- **ink** `#2b302d`, **muted** `#626a64`; **onDark** white.
- **action** `#2b302d` square actions; **onAction** white.
- **hairline** `#d2d2d7`: the rail's slots and rows.

## Shapes

**The device: the slot rail.** A vertical rail in the left margin, full height: slots 0.25 pitch wide and 0.6 pitch tall in hairline, one per pitch. Every element's top edge aligns to a slot; the rail is drawn on every unit, unbroken. It never moves to the right, never changes pitch, never holds a label.

Tools 8, cards 18; shelves and uprights square. Every nonzero radius, pills included, takes Apple's continuous corner, copied, never derived; `border-radius`, `rect rx` and superellipses are other curves. A page built with Folio inlines `continuous-corner.js` and marks each box `data-cc="R"`. Anything else draws one of the two paths below, in units of R, with `transform="translate(x y) scale(R)"` and `vector-effect="non-scaling-stroke"`, filling in A = W ÷ R − 3.05732 and B = H ÷ R − 3.05732. R is at most half the short side, a box or a pill, never between; inner R = max(0, outer R − gap); fill, stroke, clip and focus ring share one path.

A box, both sides at least 3.06 R:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .23692 .07491 .457 .07491 .89717 v{B} c0 .44017 0 .66025 -.07491 .89717 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.23692 -.07491 -.457 -.07491 -.89717 v-{B} c0 -.44017 0 -.66025 .07491 -.89717 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

A pill, R = H ÷ 2:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .18851 .07491 .32851 .07491 .36851 c0 .04 0 .18 -.07491 .36851 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.18851 -.07491 -.32851 -.07491 -.36851 c0 -.04 0 -.18 .07491 -.36851 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

## Forms

- **Cover:** a configuration at half the frame or more, every shelf on a slot.
- **Statement:** one sentence whose lines sit on slots.
- **Exhibit:** the system disassembled into its parts along the rail.
- **Data:** one dimension as a whole number of pitches, at display size.
- **Sequence and comparison:** configurations growing from one module, on one rail.
- **Collection:** parts on grey cards, sized in pitches.
- **Reference and close:** rows on the rail; the close is the system assembled.

## Variations

- **Exploded turn:** one unit shows every part apart on the rail; once per sequence.
- **Wall field:** one unit is a configuration at full width, the rail running through it.

## Do's and Don'ts

- **Look before delivering:** the rail must read at thumbnail, every top edge on a slot; a dimension off the pitch, a broken rail or a lifestyle room are faults.
- **Floors:** facts verbatim and live; renders declared once per piece, in the fine print; every pair in Tokens holds its contrast.
- **Test:** cover the names and pour in new content: white fields on a slot rail with everything snapped to it still say Shelf.
- **Caricature:** a lifestyle room; a configurator with arbitrary sizes.

## Tokens

Authored for this fictional world at S = 1000. 

```yaml
colors:
  canvas: "#ffffff"
  panel: "#f5f5f5"
  dark: "#2b302d"
  ink: "#2b302d"
  muted: "#626a64"
  action: "#2b302d"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
typography:
  display: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 80, fontWeight: 600, lineHeight: 1.05 }
  heading: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 56, fontWeight: 600, lineHeight: 1.07 }
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
  tool: 8
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
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-07.
Pieces: one-module (Keynote, 1600 × 900), configurations (Bento, 1440 × 1000), disassembled (Editorial, 1200 × 1600); each uses its brief and this DESIGN, each made from an earlier version of this file, each made from an earlier version of this file. Shelf and every part, dimension and price are fictional; no Vitsoe product, photograph, logo or font file is used. Changes after the lock: rewritten around the world's device; the pieces predate it.
