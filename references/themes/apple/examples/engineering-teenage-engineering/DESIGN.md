# Kit · Apple + Teenage Engineering

Small instruments in Apple + Teenage Engineering: every label set like a panel legend.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are px at S = 1000, S the format's short side, and scale with it; each is a floor for how far the format is read from, never a ceiling. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath; form names are the maker's, never set on the page. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Teenage Engineering style — Set every label as a panel legend in a ruled grid and let the kit show how it works; never a hidden mechanism, never colour as decoration.

World: Kit's instruments, parts, launches and stories, on any surface. Every piece keeps the panel legend, the light grey field and the one signal colour; each brings its kit, assembled or apart, and the controls a reader must find.

Method:
1. Find the controls or parts this unit names.
2. Lay the legend grid and set their names in it.
3. Draw the kit so each legend points to a part.
4. Give the one signal colour to the one thing that is live.

Amplitude: Full on the kit; the legend stays small at every scale.

Anti-reference: A lifestyle hero above a dense specification sheet.

## Images

Renders of fictional instruments — anodised aluminium, printed legends, exposed screws, a key light, a contact shadow — assembled or exploded on a grid, declared once. On a cover the kit takes half the frame or more.

## Layout

Grid system: Legend field — a ruled four-column legend band and the kit drawn to it.

Twelve tracks from W × H: margin max(5% W, 6% S), gutter 1.25% W, an 8 px module. The legend band runs along the top or the bottom edge, four equal ruled cells; parts align under their cells. Formats: on a 1600 × 900 slide, critical content stays inside the central 84%, the slide title at least 90 px and body at least 33; a scrolling page reads the tokens as given at a 1440 px viewport, body never below 17 px; a shop subdivides the field into peer cards on hairlines.

## Typography

- Inter for display and reading, the panel's neo-grotesque; Noto Sans Mono for codes and values; Noto Sans SC for Chinese.
- Display 80 / 600; heading 56 / 600; lead 24 / 300; body 17 / 400; label 14 tracked +8% uppercase for Latin; technical 14 mono; caption 12.

## Colors

Ground: Teenage Engineering's light aluminium grey; the signal colour is the only warmth.
- **canvas** `#efefef`; **panel** white; **dark** `#272823` a powered-on unit.
- **ink** `#272823`, **muted** `#62635c`; **onDark** white.
- **action** `#9a4100`: the signal — one live control, one action; **onAction** white.
- **hairline** `#d2d2d7`: the legend's rules.

## Shapes

**The device: the panel legend.** A band of four equal cells ruled in hairline, along the top or bottom edge; each cell holds one label in tracked uppercase at label size and, where it names a control, a circled numeral that also appears on the part. Every name on the unit lives in the legend. The band's edge and cell count never change; its labels follow the content.

Small parts 5, controls 8, cards 11; legend cells square. Every nonzero radius, pills included, takes Apple's continuous corner, copied, never derived; `border-radius`, `rect rx` and superellipses are other curves. A page built with Folio inlines `continuous-corner.js` and marks each box `data-cc="R"`. Anything else draws one of the two paths below, in units of R, with `transform="translate(x y) scale(R)"` and `vector-effect="non-scaling-stroke"`, filling in A = W ÷ R − 3.05732 and B = H ÷ R − 3.05732. R is at most half the short side, a box or a pill, never between; inner R = max(0, outer R − gap); fill, stroke, clip and focus ring share one path.

A box, both sides at least 3.06 R:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .23692 .07491 .457 .07491 .89717 v{B} c0 .44017 0 .66025 -.07491 .89717 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.23692 -.07491 -.457 -.07491 -.89717 v-{B} c0 -.44017 0 -.66025 .07491 -.89717 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

A pill, R = H ÷ 2:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .18851 .07491 .32851 .07491 .36851 c0 .04 0 .18 -.07491 .36851 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.18851 -.07491 -.32851 -.07491 -.36851 c0 -.04 0 -.18 .07491 -.36851 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

## Forms

- **Cover:** the kit assembled at half the frame or more, the legend naming four controls.
- **Statement:** one sentence above an empty legend that names its four words' sources.
- **Exhibit:** the kit exploded on the grid, parts under their cells.
- **Data:** one value in mono at display size in a legend cell.
- **Sequence and comparison:** states of one control in the four cells, in order.
- **Collection:** parts on white cards, each with its circled numeral.
- **Reference and close:** the legend expanded to rows; the close is the kit and one live control.

## Variations

- **Powered turn:** one unit on dark, the signal lit; once per sequence.
- **Top plate:** one unit shows only the printed top plate at 1:1.

## Do's and Don'ts

- **Look before delivering:** the legend band must read at thumbnail; labels outside it, a second warm colour, or a hidden mechanism are faults.
- **Floors:** facts verbatim and live; renders declared once per piece, in the fine print; every pair in Tokens holds its contrast.
- **Test:** cover the names and pour in new content: light grey, a four-cell legend and one signal colour still say Kit.
- **Caricature:** toy colours everywhere; tracked caps as decoration; a hidden mechanism.

## Tokens

Authored for this fictional world at S = 1000. 

```yaml
colors:
  canvas: "#efefef"
  panel: "#ffffff"
  dark: "#272823"
  ink: "#272823"
  muted: "#62635c"
  action: "#9a4100"
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
  technical: { fontFamily: "Noto Sans Mono, Noto Sans SC, monospace", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
spacing:
  unit: 8
  textInset: 12
  cardInset: 24
  proofGap: 40
  tileInset: 80
rounded:
  small: 5
  control: 8
  card: 11
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
Pieces: taken-apart (Keynote, 1600 × 900), kit-contents (Bento, 1440 × 1000), signal-states (Editorial, 1200 × 1600); each uses its brief and this DESIGN, each made from an earlier version of this file, each made from an earlier version of this file. Kit and every instrument, part, figure and price are fictional; no Teenage Engineering product, photograph, logo or font file is used. Changes after the lock: rewritten around the world's device; the pieces predate it.
