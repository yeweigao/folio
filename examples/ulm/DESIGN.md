# Ulm, Aicher · the system manual

The rules written before any case: one module, figures drawn on it at 0°, 45° and 90°, colour only as a labelled code, every fact an instruction in one neo-grotesque.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. Check the piece against Do's and Don'ts.

## Overview

Ulm, Otl Aicher — the Munich 1972 pictogram and wayfinding system: write the manual first (module, figure grid, code table, zone order), then draw every case from it; never a difference without a nameable reason.

World: any content, on any surface. Expressive content is translated into instruction: what it is, where, when, what to do next. Every piece keeps the module, ground, ink, codes, faces, figure grammar and zone order; each brings its facts, its categories and the figures it needs, drawn on the same grid.

Method:
1. Write the manual: module, figure grid, code table, zone order.
2. Model the content before any surface, after Maldonado: who uses it, for what task, at what decision; the zones follow the model.
3. Draw figures on squared paper: one band width, one gap width, 45° and 90° only, vertices on grid nodes.
4. Code each category once, colour and shape together, with a legend or a direct label.
5. Set facts as live type, the first language above the second, flush left on the axes.

Amplitude: reduced: one figure per unit, at most three codes.

Anti-reference: the Munich palette or sports pictograms pasted onto an ordinary page; UI line icons; a grid as wallpaper.

## Images

Computed: figures on the module grid, at most in three construction stages (grid and outline, solid bands, solid figure). Photographs only as record: black and white, rectangular, whole modules, captioned.

## Layout

Grid system: Modular — whole modules both ways.

S = min(W, H); margin 0.04 S; module u = (W − 2 × margin) ÷ 20, ÷ 32 where W > 1.4 H; lines = whole modules that fit. Axes every seven modules: six-module columns, one-module gutters. Gaps: half a module within a group, one between peers, one and a half to two between sections, no other size. Zones in the manual's order: lockup, description, figures standing on a 3 ink rule, a column beneath each figure, instruction last. Leftover lines go to the bottom margin; type and figures never shrink to fit.

## Typography

- **Archivo** (OFL, variable width 62–125): one neo-grotesque family for every job, by width and weight. Body at width 100, titles at 86.
- Display at a cap height of three modules, its width axis set between 75 and 125 so the longest line fills the measure; the setting used is stated with the piece — a display left at width 100 by default is unexamined, and a fault.
- **Noto Sans SC** 500–900: beside Latin, display at 0.72 of it; titles and body at the Latin size.
- Sizes: display 200, Chinese display 144, title 44, body 28; nothing read smaller. Weight is meaning: 800 display, 700 facts to act on, 500 the rest. No italic or tracking.

## Colors

- **Ground `#E3E4E0` (neutral).** Concrete grey, at least 70% of the area.
- **Ink `#101418` (primary).** Type, rules, figures.
- **Muted `#4B5057` (secondary).** Secondary names and notes.
- **Line `#B3B6B2`.** Figure construction grids only; declared wherever figures are drawn. Every figure is built on it at one construction unit per piece — the module or its half — and the grid stage stands beneath the finished figure in the construction record; a figure with no grid under it is unfinished.
- **Code one `#0A5AA6`** with a square; **code two `#D4470C`** with a circle. A third category needs a third code written here first. Codes under 2% of the area, never the only cue, never text colour.

## Shapes

Radius 0 except circles. A figure sheet is 12 × 18 units of half a module: bands two units, gaps one, diagonals at 45° cut square, a head a circle of four. Reference figure, a person walking, in units: head centre (6, 2), radius 2; torso (4,5) (8,5) (8,10) (4,10); arms (9,5) (9,8) (12,11) (12,8) and (3,5) (3,8) (0,11) (0,8); legs (3,11) (5,11) (5,18) (3,18), (6,11) (9,11) (12,14) (9,14) and (10,15) (12,15) (12,18) (10,18). Every new figure is calibrated against it. One kind of arrow.

## Forms

- **Cover:** lockup, one figure, the facts to act on.
- **Statement:** one instruction at title size, one line per language.
- **Exhibit:** one figure on six by nine modules.
- **Data:** a table on the axes, categories by code, values tabular; solid ink bars one module high, to scale, where a comparison must be seen.
- **Sequence and comparison:** steps along one axis, one figure or line per step; two columns with the same figures at one scale.
- **Reference and close:** the legend (marker, name, both languages); the instruction line last.

## Variations

- **Variation series** (Max Bill). One figure or form carried through a law written in the manual, one step per unit; for series.
- **Sign field.** One figure in ground colour on a code-one field of six by nine modules; once per unit.

## Do's and Don'ts

- **Look before delivering:** render it, see it full size and as a thumbnail. A difference the manual cannot explain, a figure off the grid, two languages on one line: faults.
- **Floors:** facts verbatim and live; every pair in Tokens holds its contrast.
- **Test:** a stranger knows what to do next, and a designer could apply the rules to a new case.
- **Caricature:** sports pictograms and the Munich palette on an ordinary page; UI line icons; three kinds of arrow.

## Tokens

```yaml
colors:
  primary: "#101418"
  secondary: "#4B5057"
  neutral: "#E3E4E0"
  line: "#B3B6B2"
  code-one: "#0A5AA6"
  code-two: "#D4470C"
typography:
  display: { fontFamily: "Archivo, Noto Sans SC, sans-serif", fontSize: 200, fontWeight: 800, lineHeight: 1 }
  display-han: { fontFamily: "Noto Sans SC, Archivo, sans-serif", fontSize: 144, fontWeight: 900, lineHeight: 1 }
  title: { fontFamily: "Archivo, Noto Sans SC, sans-serif", fontSize: 44, fontWeight: 700, lineHeight: 1.045 }
  body: { fontFamily: "Archivo, Noto Sans SC, sans-serif", fontSize: 28, fontWeight: 500, lineHeight: 1.214 }
spacing:
  margin: 40
  module: 46
  rule: 3
  hairline: 1
pairs:
  ink-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.primary}" }
  muted-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.secondary}" }
  code-one-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.code-one}" }
  code-two-on-ground-large: { backgroundColor: "{colors.neutral}", textColor: "{colors.code-two}" }
  ground-on-code-one: { backgroundColor: "{colors.code-one}", textColor: "{colors.neutral}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-02.
Pieces: the-grid/brief.md, made from the earlier, programme-bound version of this file; the system it shows is unchanged.
