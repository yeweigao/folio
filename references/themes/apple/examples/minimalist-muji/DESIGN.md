# Plain · Apple + MUJI

Everyday goods in Apple + MUJI: unbleached paper, and a board strip carrying every label.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are px at S = 1000, S the format's short side, and scale with it; each is a floor for how far the format is read from, never a ceiling. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath; form names are the maker's, never set on the page. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + MUJI style — Make every unit plain paper with a strip of board down its left edge carrying the label; never a loud mark, never decoration, never a colour that is not a material.

World: Plain's goods, packaging, shop and stories, on any surface. Every piece keeps the board strip, the paper ground and the plain sans; each brings its object or drawing and the measurements that describe it.

Method:
1. Find what the buyer needs to know; write it as measurements.
2. Set the label in the board strip.
3. Show the object or its drawing plainly on paper.
4. Remove the rest.

Amplitude: Reduced throughout; the cover is the quietest unit at its largest.

Anti-reference: Japanese decoration; a loud mark; a product that demands attention.

## Images

Plain renders and technical drawings of fictional goods — natural materials, soft light, one contact shadow; cut edges solid, folds dashed — declared once. On a cover the object or its measured drawing takes half the frame or more.

## Layout

Grid system: Strip field — a left strip of board and a paper field, both square.

Twelve tracks from W × H: margin max(5% W, 6% S), gutter S / 50, module S / 125. The strip takes one track at the left edge, full height; the field begins one gutter after it. Formats: on a 1600 × 900 slide, critical content stays inside the central 84%, the slide title at least 90 px and body at least 33; a scrolling page reads the tokens as given at a 1440 px viewport, body never below 17 px; a shop subdivides the field into peer cards on hairlines.

## Typography

- Inter at 400 for every role; Noto Sans SC for Chinese; tabular figures.
- Display 80 / 400; heading 52 / 400; lead 24 / 400; body 17 / 400; label 14; caption 12.
- Hierarchy by size and position, never weight.

## Colors

Ground: MUJI's unbleached paper, the brand's signature.
- **canvas** `#f8f6f1` paper; **panel** white plates; **dark** `#302d27` a rare turn.
- **ink** `#302d27`, **muted** `#666056`; **onDark** white.
- **action** `#302d27` square actions; **onAction** white.
- **board** `#c5a976` the strip; **cotton** `#d7cdbc`, **porcelain** `#ebe7df`, **beech** `#bd9667`: materials in renders.
- **mark** `#8f1d26`: one small unlettered mark, at most, on the strip's top.
- **hairline** `#d5d2ca` only where rows need it.

## Shapes

**The device: the board strip.** A strip of board colour, one track wide, full height at the left edge, with a subtle fibre texture; the unit's label — name, then its measurements — set in ink at its top, reading left to right. One per unit; it never moves to another edge, never holds an image, never carries a slogan.

Everything square: radius zero is part of the restraint.

## Forms

- **Cover:** the object on paper at half the frame or more, its name and size in the strip.
- **Statement:** one plain sentence on paper, the strip holding its source.
- **Exhibit:** a measured drawing at 1:1 or a stated scale on a white plate.
- **Data:** one measurement at display size; others in the strip.
- **Sequence and comparison:** goods at one scale on one baseline, each with its strip label.
- **Collection:** square white plates, name and price beneath in one size.
- **Reference and close:** specification rows; the close is the object and its strip.

## Variations

- **Section:** one unit shows the material in section at a stated scale.
- **Plate field:** one unit is a white plate edge to edge, the strip unchanged.

## Do's and Don'ts

- **Look before delivering:** the strip must read at thumbnail on the left of every unit; a rounded corner, a colour that is not a material, or a slogan are faults.
- **Floors:** facts verbatim and live; renders declared once per piece, in the fine print; every pair in Tokens holds its contrast.
- **Test:** cover the names and pour in new content: paper, a board strip at the left and plain measurements still say Plain.
- **Caricature:** Japanese ornament; a loud logo; a decorative colour.

## Tokens

Authored for this fictional world at S = 1000. 

```yaml
colors:
  canvas: "#f8f6f1"
  panel: "#ffffff"
  dark: "#302d27"
  ink: "#302d27"
  muted: "#666056"
  onDark: "#ffffff"
  action: "#302d27"
  onAction: "#ffffff"
  hairline: "#d5d2ca"
  mark: "#8f1d26"
  cotton: "#d7cdbc"
  porcelain: "#ebe7df"
  beech: "#bd9667"
  board: "#c5a976"
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
  field: 0
  card: 0
  action: 0
pairs:
  ink-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}" }
  ink-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.ink}" }
  muted-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.muted}" }
  muted-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.muted}" }
  onDark-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.onDark}" }
  onAction-on-action: { backgroundColor: "{colors.action}", textColor: "{colors.onAction}" }
  mark-on-canvas-large: { backgroundColor: "{colors.canvas}", textColor: "{colors.mark}" }
  mark-on-panel-large: { backgroundColor: "{colors.panel}", textColor: "{colors.mark}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-07.
Pieces: one-sheet (Keynote), three-things (Bento), cut-open (Editorial), each made from an earlier version of this file, each made from an earlier version of this file, each made from an earlier version of this file, each made from an earlier version of this file. Plain and all goods, packaging, measurements, prices and materials are fictional; no MUJI product, logo, photograph or font file is used. Changes after the lock: rewritten around the world's device; the pieces predate it.
