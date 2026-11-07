# Aero · Apple + Dyson

Airflow machines in Apple + Dyson: one section line cuts through every unit.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are px at S = 1000, S the format's short side, and scale with it; each is a floor for how far the format is read from, never a ceiling. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath; form names are the maker's, never set on the page. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Dyson style — Cut every unit with one section line and show what lies on it; never a mood without a mechanism, never a performance claim with nothing to check it by.

World: Aero's machines, filters, launches and stories, on any surface. Every piece keeps the section line, the white field and the geometric sans; each brings its machine and the mechanism the line passes through.

Method:
1. Find the mechanism the claim depends on.
2. Draw the section line through it.
3. Show what lies on the line: the cut, the airflow, the part.
4. Give every performance claim a figure on a shared baseline.

Amplitude: Full on covers and sections; reduced in ranges and reference.

Anti-reference: A spec sheet under a lifestyle photograph, beside a rendered explosion.

## Images

Renders of fictional machines and their sections — satin metal, polycarbonate, a key light, a contact shadow; airflow as flat lines at one weight — declared once. On a cover the mechanism takes half the unit or more; a system too wide shows its named part, the whole on the proof unit.

## Layout

Grid system: Section field — the section line organizes the unit; content aligns along or perpendicular to it.

Twelve tracks from W × H: margin max(5% W, 6% S), gutter 1.25% W, an 8 px module. The line crosses the full unit at 15°–30°; labels sit perpendicular to it at its markers; diagrams are cropped tight to the mechanism. Formats: on a 1600 × 900 slide, critical content stays inside the central 84%, the slide title at least 90 px and body at least 33; a scrolling page reads the tokens as given at a 1440 px viewport, body never below 17 px; a shop subdivides the field into peer cards on hairlines.

## Typography

- Jost, the nearest open face to Dyson's Futura lineage, for every role; Noto Sans SC for Chinese.
- Display 80 / 600; heading 56 / 600; lead 24 / 300; body 17 / 400; label 14; caption 12.

## Colors

Ground: Dyson's white and neutral grey; colour is the machine's own.
- **canvas** `#f5f5f5`; **panel** white; **dark** `#25272a` a section turn.
- **ink** `#25272a`, **muted** `#62666b`; **onDark** white.
- **action** `#6525a0`: the section line, its markers and the one action; **onAction** white.
- **hairline** `#d2d2d7` in rows.

## Shapes

**The device: the section line.** One straight cutting-plane line in action colour, long dash and dot, 1.5 at S = 1000, crossing the whole unit at 15°–30°, with a marker at each end — a short perpendicular arrow and the letter A — pointing the view. The lead sits on the line. One per unit; the angle may change with the content, the pattern, colour and markers never.

Small parts 5, controls 8, cards 18; diagrams square. Every nonzero radius, pills included, takes Apple's continuous corner, copied, never derived; `border-radius`, `rect rx` and superellipses are other curves. A page built with Folio inlines `continuous-corner.js` and marks each box `data-cc="R"`. Anything else draws one of the two paths below, in units of R, with `transform="translate(x y) scale(R)"` and `vector-effect="non-scaling-stroke"`, filling in A = W ÷ R − 3.05732 and B = H ÷ R − 3.05732. R is at most half the short side, a box or a pill, never between; inner R = max(0, outer R − gap); fill, stroke, clip and focus ring share one path.

A box, both sides at least 3.06 R:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .23692 .07491 .457 .07491 .89717 v{B} c0 .44017 0 .66025 -.07491 .89717 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.23692 -.07491 -.457 -.07491 -.89717 v-{B} c0 -.44017 0 -.66025 .07491 -.89717 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

A pill, R = H ÷ 2:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .18851 .07491 .32851 .07491 .36851 c0 .04 0 .18 -.07491 .36851 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.18851 -.07491 -.32851 -.07491 -.36851 c0 -.04 0 -.18 .07491 -.36851 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

## Forms

- **Cover:** the machine cut by the line, the claim along it.
- **Statement:** one sentence set along the line.
- **Exhibit:** the section itself: what the line cuts, labelled at the markers.
- **Data:** one performance figure on the line, its baseline shared with its peers.
- **Sequence and comparison:** air paths in steps along the line; filters compared at one scale.
- **Collection:** machines on white cards, each with its own short section line.
- **Reference and close:** rows on grey; the close is the machine and the line.

## Variations

- **Section turn:** one unit on dark with the line in white; once per sequence.
- **Macro cut:** one unit fills the frame with the cut face of one part.

## Do's and Don'ts

- **Look before delivering:** the line must read at thumbnail; two lines, a claim without a figure or a rendered explosion that cannot be read are faults.
- **Floors:** facts verbatim and live; renders declared once per piece, in the fine print; every pair in Tokens holds its contrast.
- **Test:** cover the names and pour in new content: white fields cut by one marked section line still say Aero.
- **Caricature:** a lifestyle mood; a 3D explosion; every node type in one diagram.

## Tokens

Authored for this fictional world at S = 1000. 

```yaml
colors:
  canvas: "#f5f5f5"
  panel: "#ffffff"
  dark: "#25272a"
  ink: "#25272a"
  muted: "#62666b"
  action: "#6525a0"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
typography:
  display: { fontFamily: "Jost, Noto Sans SC, sans-serif", fontSize: 80, fontWeight: 600, lineHeight: 1.05 }
  heading: { fontFamily: "Jost, Noto Sans SC, sans-serif", fontSize: 56, fontWeight: 600, lineHeight: 1.07 }
  lead: { fontFamily: "Jost, Noto Sans SC, sans-serif", fontSize: 24, fontWeight: 300, lineHeight: 1.5 }
  body: { fontFamily: "Jost, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.47 }
  label: { fontFamily: "Jost, Noto Sans SC, sans-serif", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  caption: { fontFamily: "Jost, Noto Sans SC, sans-serif", fontSize: 12, fontWeight: 400, lineHeight: 1.5 }
spacing:
  unit: 8
  textInset: 12
  cardInset: 24
  proofGap: 40
  tileInset: 80
rounded:
  small: 5
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
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-07.
Pieces: airflow-section (Keynote, 1600 × 900), filter-range (Bento, 1440 × 1000), air-path (Editorial, 1200 × 1600); each uses its brief and this DESIGN, each made from an earlier version of this file, each made from an earlier version of this file. Aero and every machine, figure and price are fictional; no Dyson product, photograph, logo or font file is used. Changes after the lock: rewritten around the world's device; the pieces predate it.
