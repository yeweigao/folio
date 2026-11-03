# Swiss Brutal · the document of record

A working document whose row grid is the content's own measure: visible hairlines, one monolith at architectural scale, dense rows, one hazard colour for a real alert.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Swiss Brutal, the Construction hand, after the Modulor cast into the concrete of Le Corbusier's Unité d'Habitation and the grids computed in Müller-Brockmann's *Grid Systems*: compute the rows from the content's own measure, draw only the rules the content uses, and let one word or figure at architectural scale stand on them; never a rule that bounds nothing, never a surface effect.

World: any content, on any surface. Lyrical content is translated, not refused: its sections, sequence or counts become the rows, and its one essential word becomes the monolith. Every piece keeps the ground, ink, rules, faces, the row computation and the monolith; each brings its data, its measure and its word.

Method:
1. Find the measure (time, count, sequence, sections); its units are the rows.
2. Cut whole rows and twelve equal columns.
3. A hairline and an axis tick per row, a longer tick per major unit.
4. Each item a black cell on its row; a secondary track a grey field beside the main one.
5. The monolith: the one word or figure the reader must not miss, on whole rows, flush left. Everything else stays document.
6. A dark footer begins on the closing line. Computed, never nudged.

Amplitude: full on the monolith, quiet elsewhere; the grid quieter than the text.

Anti-reference: the polished product page: rounded cards, soft shadows, a gradient hero, airy bands that carry nothing.

## Images

None by default: rules and cells are the image. A real photograph enters as found and as record: as taken, never filtered, rectangular, whole columns and rows, its source as the caption row beneath.

## Layout

Grid system: Modular — the rows are the content's measure.

N rows = the measure's units plus the header, monolith, description and footer rows; row height = (H − 2 × margin) ÷ N in whole pixels, the margin (at least 0.032 S) taking the halved remainder. Twelve columns without gutters, text inset 0.012 S: the axis on columns 1–2, cells on 3, items on 4–9, a secondary track on 10–12. Heavy rules open and close the field; verticals at columns 3 and 10; a hairline per row. Ticks stand on the axis at every row line, one unit long, longer at major units; a lone decorative tick is a fault. Landscape and web keep the axis left and the rows down. Nothing is centred; no row is empty unless the measure says so.

## Typography

- **Inter** (OFL), with its Display cut for the monolith and titles: a tight grotesque that holds at architectural scale and at 32.
- **Noto Sans SC** Bold or Black, its em box at 0.9 of the Latin; both scripts at one size and weight.
- The monolith is derived by one formula on every piece: its em spans its whole rows exactly — font size = rows × row height — so the digits take the band's height the same way everywhere; at most the twelve columns wide (276 holds six letters at S = 1000).
- Titles 56, figures 40, body and labels 32; nothing read below 32. Tabular figures; a text line sits inside one row.

## Colors

- **Ground `#E3E4E1` (neutral).** Concrete grey-white, at least half the area.
- **Ink `#0B0B0B` (primary).** Text, monolith, cells, footer.
- **Muted `#454745` (secondary).** Keys and secondary lines.
- **Field `#C9CBC7`.** The secondary track only.
- **Line `#7A7C79`.** Grid and ticks; never text.
- **Hazard `#FFD200` (tertiary).** A real alert only, ink on it.
- Emphasis is weight or the monolith, never colour.

## Shapes

Zero radius, shadow, gradient or outline. Hairlines 1; table rules 6 ink; the top edge one 8 ink rule. A cell is one column by one row.

## Forms

- **Cover:** the monolith flush left; header rows for what, when, where.
- **Statement:** the monolith alone on whole rows, one line beneath.
- **Exhibit:** one photograph as record on whole rows and columns, its caption row beneath.
- **Data:** rows of label, value, unit and source on the columns; the one number that matters may be the monolith.
- **Sequence and comparison:** the measure as rows, each item's cell on its starting row; two tracks side by side on one row scale.
- **Reference and close:** the header ledger and the key, once; the footer in ink, ground text, a hazard cell for a real notice.

## Variations

- **Accent field.** The whole unit in hazard yellow, ink text; once, at a real turn.
- **Rotation.** The monolith at 90° counter-clockwise on a tall format, from column 1, first row.

## Do's and Don'ts

- **Look before delivering:** render it, see it full size and as a thumbnail; squint, and the text reads before the rules. Two monoliths, a rule heavier than the text it bounds, a figure without its unit or source: faults.
- **Floors:** facts verbatim and live; every pair in Tokens holds its contrast.
- **Test:** every visible line is a real boundary and every band holds working content.
- **Caricature:** terminal cosplay, green on black, scanlines; stickers with thick outlines and hard shadows; a lattice as wallpaper; ugliness on purpose; broken layouts called raw.

## Tokens

```yaml
colors:
  primary: "#0B0B0B"
  secondary: "#454745"
  tertiary: "#FFD200"
  neutral: "#E3E4E1"
  field: "#C9CBC7"
  line: "#7A7C79"
typography:
  monolith: { fontFamily: "Inter Display, Inter, Noto Sans SC, sans-serif", fontSize: 276, fontWeight: 900, lineHeight: 0.76 }
  title: { fontFamily: "Inter Display, Inter, Noto Sans SC, sans-serif", fontSize: 56, fontWeight: 800, lineHeight: 1 }
  figure: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 40, fontWeight: 800, lineHeight: 1 }
  body: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 32, fontWeight: 700, lineHeight: 1.5 }
spacing:
  margin: 32
  inset: 12
  rule: 6
  edge: 8
  hairline: 1
pairs:
  ink-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.primary}" }
  muted-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.secondary}" }
  ink-on-field: { backgroundColor: "{colors.field}", textColor: "{colors.primary}" }
  ground-on-ink: { backgroundColor: "{colors.primary}", textColor: "{colors.neutral}" }
  ink-on-hazard: { backgroundColor: "{colors.tertiary}", textColor: "{colors.primary}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-03.
Pieces: the-grid/brief.md, made from the earlier, programme-bound version of this file; the system it shows is unchanged.
