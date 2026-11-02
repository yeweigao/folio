---
version: alpha
name: The Grid · Ulm, Aicher
description: The Museum of Design's evening series on the systems behind modern design, one bilingual poster per evening, each built from the same module, the same visitor figure drawn in stages, and two place codes.
colors:
  primary: "#101418"
  secondary: "#4B5057"
  neutral: "#E3E4E0"
  line: "#B3B6B2"
  hall: "#0A5AA6"
  foyer: "#D4470C"
typography:
  display: { fontFamily: "Archivo, Noto Sans SC, sans-serif", fontSize: 200, fontWeight: 800, lineHeight: 1 }
  display-han: { fontFamily: "Noto Sans SC, Archivo, sans-serif", fontSize: 144, fontWeight: 900, lineHeight: 1 }
  lead: { fontFamily: "Archivo, Noto Sans SC, sans-serif", fontSize: 44, fontWeight: 700, lineHeight: 1.045 }
  lead-han: { fontFamily: "Noto Sans SC, Archivo, sans-serif", fontSize: 36, fontWeight: 700, lineHeight: 1.28 }
  title: { fontFamily: "Archivo, Noto Sans SC, sans-serif", fontSize: 44, fontWeight: 700, lineHeight: 1.045 }
  body: { fontFamily: "Archivo, Noto Sans SC, sans-serif", fontSize: 28, fontWeight: 500, lineHeight: 1.214 }
spacing:
  margin: 40
  module: 46
  half: 23
  figure-unit: 23
  rule: 3
  hairline: 1
  marker: 20
rounded:
  square: 0
  circle: 10
components:
  ink-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.primary}" }
  muted-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.secondary}" }
  hall-on-ground-large: { backgroundColor: "{colors.neutral}", textColor: "{colors.hall}" }
  foyer-on-ground-large: { backgroundColor: "{colors.neutral}", textColor: "{colors.foyer}" }
  ground-on-hall: { backgroundColor: "{colors.hall}", textColor: "{colors.neutral}" }
---

## Overview

Ulm, Otl Aicher — the Munich 1972 pictogram and wayfinding system: write the manual first (module, one figure drawn on it, the codes), then draw every case from it; never a difference without a nameable reason.

World: the evening series "The Grid" of the Museum of Design. Any A-series size, English above Chinese at equal status, two or three talks, one secondary event in a second place. A later evening changes words, talk count and stage names; never module, ground, ink, codes, faces, figure or zone order.

Method:
1. Module first: 20 across the measure, 46 px at 1000 px. Display cap 3 modules, lead line 1, figure sheet whole modules.
2. Figure on squared paper: 45° and 90° only, one band width, one gap width, vertices on grid nodes, never traced (Shapes). A walking visitor.
3. One construction stage above each talk, in time order.
4. One code per place, colour and shape together; code every line naming or in that place, no other.
5. Facts as live type, English above Chinese, flush left on columns 0, 7, 14.

Amplitude: reduced. One figure, two codes, one sheet, read in three seconds; rules before cases, colour as code, 0°, 45°, 90° kept.

Anti-reference: cream sheet, black type, one vermilion square; Munich palette or sports pictogram on an ordinary page; UI line icons; grid as wallpaper.

## Colors

- **Ground `#E3E4E0`** (neutral). Cool concrete grey, not cream; at least 70% of the sheet (76% measured).
- **Ink `#101418`** (primary). All first-reading type, rules, figure. 14.5:1.
- **Muted `#4B5057`** (secondary). Speakers' names only. 6.4:1.
- **Line `#B3B6B2`**. Construction grid in stages 1 and 2 only.
- **Hall `#0A5AA6`** (code). Solid 20 px square left of each hall line. 5.4:1.
- **Foyer `#D4470C`** (code). Solid 20 px circle, same placement; never text or line. 3.5:1.
- A third place needs a third code added here first; never more than three. No other hue; codes under 2% of the sheet. No dark register.

## Typography

- **Archivo** (variable, width 62–125, weight 100–900; OFL). Width by job: 100 body, 86 talk titles, 92.7 display (THE GRID at cap 3 modules fills 20).
- **Han: Noto Sans SC** (500, 700, 900; OFL). Display 144 px = 3.13 modules, two characters six modules wide, three tall. Lead and body Han equal Latin size; place name 36 against 44.
- **Ramp: 200 / 144 display, 44 lead and title, 28 body.** No label size, italic, small caps, tracking. Weight: 800/900 display, 700 facts to act on, 500 the rest.
- Display in capitals. Break by meaning; family names never split; Chinese breaks at a phrase, never begins with ——, full-width punctuation; English ranges with en dash.

## Layout

Grid system: Modular — whole modules both ways; the figure occupies whole modules.

Any A-series format (W, H = 1.414 W); values at W = 1000, scaled by W / 1000.
- Margin m = 4% of W (40). Module u = (W − 2m) / 20 (46). Lines = floor((H − 2m) / u) (29); remainder to the bottom margin. Counts start at 0 from the margin.
- Axes: columns 0, 7, 14, six modules (276 px) plus a one-module gutter. Display and hairlines span 20.
- Gaps: half module (23) within a group, one between peers, 1.5–2 between sections; no other size.
- Zones, top to bottom:
  1. Lockup. English title, cap 3 modules, baseline on a module line, column 0 to 20. Half a module under, the Chinese title at column 0. From column 7: date at lead; time at column 7, doors (500) at column 14; place at lead, Han line in lead-han under it, hall marker. Cap top aligned to the Chinese title top.
  2. Descriptor. One module under the facts, column 0, 14 modules wide: English, Chinese under it, body.
  3. Strip. One 12 × 18 unit sheet (p = 23; 6 × 9 modules) per talk at columns 0, 7, 14, on the next half-module line, one module under the descriptor. Two talks: start at column 0. Closes on a 3 px ink rule the figures stand on.
  4. Programme. 10 px under the rule, a column under each sheet: time (body 700), title (title), name (body 500, muted). Hall marker in the gutter left of each column, level with the time; first in the margin.
  5. Secondary event. Hairline half a module under; line type 11 px below it; second hairline half a module under. Body 700, foyer marker in the margin; up to 70 Latin characters, longer takes two lines at the same size.
  6. Entry. Under the second hairline (type 11 px below), column 0: English, Chinese under it (body 700); half-module gap; disclosure line, body 700, last.
- Overrun: close gaps by half modules, strip to descriptor then hairline to hairline. Type and figure never shrink.
- New format: recompute m, u, lines; re-check display cap (metres × 5 mm). Assumed A1, read 2–5 m: display cap 82 mm, lead cap 18 mm, body em 16.6 mm.

## Shapes

- Radius 0 except the foyer circle. No shadow, glow, gradient, plate, card.
- Ink rules: 3 px closes strip; 1 px hairline separates sections.
- **Figure.** Sheet 12 × 18 units, p = 23 px. Bands 2 p (torso 4 p), diagonals 45° cut by a 3 p chord, gaps 1 p, head a circle of diameter 4 p. Interval layout, in p:
  - head: centre (6, 2), radius 2.
  - torso: (4,5) (8,5) (8,10) (4,10).
  - front arm: (9,5) (9,8) (12,11) (12,8).
  - back arm: (3,5) (3,8) (0,11) (0,8).
  - back leg: (3,11) (5,11) (5,18) (3,18).
  - thigh: (6,11) (9,11) (12,14) (9,14).
  - shank: (10,15) (12,15) (12,18) (10,18).
  Joined layout (each part grown 1 p along its axis to touch its neighbour): torso (4,4) (8,4) (8,10) (4,10); front arm (8,4) (8,7) (12,11) (12,8); back arm (4,4) (4,7) (0,11) (0,8); back leg (3,10) (5,10) (5,18) (3,18); thigh (5,10) (8,10) (12,14) (9,14); shank (10,14) (12,14) (12,18) (10,18); head unchanged.
- **Stages**, only these:
  1. Cell: 1 px line-colour grid at every unit; interval layout as 2 px ink outlines, no fill; 6 px ink square on each vertex, 8 px on the head centre.
  2. Bands: same grid, joined layout solid ink.
  3. Interval: no grid, interval layout solid ink.
  Two talks use stages 1 and 3.
- Markers: hall 20 px square, foyer 20 px circle. Left edge 33 px left of the block's column (10 px from the edge in the margin); centre level with the first line's capital middle.

## Components

- **English title:** display, ink, capitals, one line, full measure. No tracking, outline, colour.
- **Chinese title:** display-han, ink, column 0 under the English.
- **Facts block:** lead, ink, column 7. No icon, label, map pin.
- **Descriptor:** body 500, ink, two English lines at most. No slogan.
- **Figure sheet:** one stage, standing on the 3 px rule. No fourth stage, other pose, or fill but ink.
- **Programme column:** time, title, name, hall marker. No numbering, box, ranking.
- **Place marker:** never on a line outside its place, never as text colour, never the only cue.
- **Secondary-event line:** body 700, ink, between hairlines, foyer marker. No box, button, arrow.
- **Entry lines and disclosure:** body 700, flush left; the disclosure states the programme is illustrative, never smaller or muted.

## Do's and Don'ts

1. **Do write the rule before the case.** A difference this file cannot explain is removed.
2. **Do keep colour a code.** Blue and orange mark places only.
3. **Do draw the figure from the Shapes vertices.** Redrawn or off-angle is another world.
4. **Don't let two languages share a line.**
5. **Don't shrink type to fit.** Close gaps or recompose.

Refused: cream ground with one vermilion accent, small tracked capitals above numbered rows, dots-and-line timelines, sports pictograms in the Munich palette, UI line icons, three kinds of arrow.

## Variations

- **Sign field.** One stage may sit as a Munich-style sign: interval figure in ground colour on a hall-blue field of 6 × 9 modules replacing its sheet. Once per sheet, only for a hall talk, at most 10% of the sheet. Not yet rendered.

## Record

Folio version: 1.0.0. Template version: 13. Date: 2026-11-02.
Pieces: the-grid/brief.md.
Changes after the lock: Han display size 150 px to 144 px, to clear the hall marker.
