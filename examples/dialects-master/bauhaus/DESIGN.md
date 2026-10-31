---
version: alpha
name: The Grid, an evening · Bauhaus
description: "The evening constructed from point, line, and plane on one square module."
colors:
  primary: "#111111"
  secondary: "#4A463F"
  tertiary: "#D22730"
  neutral: "#FFFFFF"
  soft: "#F4F1E8"
  line: "#111111"
  dark: "#111111"
  focus: "#005FCC"
  blue: "#2255A4"
  yellow: "#F2C500"
typography:
  display: { fontFamily: "Poppins, Inter, Source Han Sans SC, sans-serif", fontSize: 120px, fontWeight: 700, lineHeight: 1.05 }
  title: { fontFamily: "Poppins, Inter, Source Han Sans SC, sans-serif", fontSize: 44px, fontWeight: 700, lineHeight: 1.15 }
  body: { fontFamily: "Inter, Source Han Sans SC, Noto Sans SC, sans-serif", fontSize: 19px, fontWeight: 400, lineHeight: 1.5 }
  label: { fontFamily: "Inter, Source Han Sans SC, Noto Sans SC, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.3 }
spacing:
  margin: 56px
  gutter: 16px
  column: 51px
  columns: 12
  module: 60px
rounded:
  none: 0px
components:
  text-on-paper: { backgroundColor: "{colors.neutral}", textColor: "{colors.primary}" }
  muted-on-paper: { backgroundColor: "{colors.neutral}", textColor: "{colors.secondary}" }
  paper-on-accent: { backgroundColor: "{colors.tertiary}", textColor: "{colors.neutral}" }
  paper-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.neutral}" }
  hairline: { backgroundColor: "{colors.line}", height: 1px }
  text-on-soft: { backgroundColor: "{colors.soft}", textColor: "{colors.primary}" }
  muted-on-soft: { backgroundColor: "{colors.soft}", textColor: "{colors.secondary}" }
  focus-ring: { backgroundColor: "{colors.focus}", height: 2px }
  paper-on-blue: { backgroundColor: "{colors.blue}", textColor: "{colors.neutral}" }
  ink-on-yellow: { backgroundColor: "{colors.yellow}", textColor: "{colors.primary}" }
---

## Invocation

**「包豪斯（Bauhaus）」 — Make this poster as Kandinsky, Moholy-Nagy and Bayer made the Dessau work: circle, square and triangle in the primaries constructing the field, the type set as one shape among shapes.**

This line governs the file. Where a parameter below and the named hand's evident way of working conflict on atmosphere or composition, the hand wins and the conflict is recorded in Record; the parameters bind absolutely on the facts, the contrast floors, live text, the format, and the bans.

## Overview
One poster (print-first, read at arm's length and across a foyer) for a fictional public evening, THE GRID — three talks and a poster exhibition on the system behind modern design. It is one of nine dialect master examples in examples/dialects-master/: the source content (content.md) is identical in all nine; only the design changes. All names, the venue, and the times are illustrative. Theme: Swiss; dialect: Bauhaus.
Governing hand: Make this poster as Joost Schmidt made the 1923 exhibition poster: construct the subject from circle, square, and triangle on the module, let the primaries overlap and overprint, set the type as one shape among shapes; never a photograph, never a shape off the grid, never a fourth hue.
Signature: none — the construction from elements is the dialect's own programme; a signature card method would import a second system.

## Standalone brief — this file is the whole brief

This DESIGN.md is self-contained: an agent holding only this file — no other document, no design system, no conversation — has everything needed to make the poster to a master-level standard. Do not look anything up; where this file gives a number, use it; where it gives a rule, obey it; the Composition paragraph in Layout is the build spec for the lead. Composition coordinates are absolute poster coordinates: they outrank the spacing tokens, which govern only what the Composition does not place.

### Source — every fact, verbatim
- Title: THE GRID · 格网
- Subtitle: Three talks and a poster exhibition on the system behind modern design. · 三场讲座，一场海报展——现代设计背后的系统
- When: Saturday 14 November 2026, 19:30–22:00 (doors 19:00)
- Where: Hall 2, Museum of Design · 设计博物馆 二号厅
- 19:30 — The Module · Josef Müller-Brockmann: the grid for print
- 20:15 — The System · Otl Aicher: rules for every case
- 21:00 — The Interval · Kenya Hara: emptiness as a vessel
- Foyer, from 19:00 — Poster exhibition: nine dialects, one mother tongue
- Admission: free, seats unreserved · 免费入场，不设座位预订
- The line "Illustrative example" stands on the poster (the programme is fictional; the masters named are the talks' subjects).

### The dialect, in full
- **Primaries together, not one accent.** Red, yellow, and blue with black, on white or off-white paper; no other hue.
- **The image is constructed from elements, not photographed or drawn.** Point, line, and plane, after Kandinsky's *Point and Line to Plane*: circle, square, triangle, bar, and their halves and quarters assemble the subject, a face, a chair, a letter, a number.
- **Shapes overlap, not only abut.** Where two primaries cross, one overprints or cuts the other.
- **Type is a shape among shapes, not a caption.** A geometric sans or constructed capitals, set vertical, diagonal, or across the field; Latin may go lowercase.
**Swiss keeps:** the module, every shape snapped to one square grid at doubling sizes; reading text, the type ramp, and the facts.
**Test:** Remove the type, and the shapes still compose the subject on the grid.
**Caricature:** Shapes scattered off the grid with no relation; pastel or teal "Bauhaus"; gradients, shadows, rounded UI cards; geometry pasted beside an ordinary layout.

### Floors that bind this poster
- Facts are exact: the Source above is the whole material. Add nothing, rename nothing, invent no names, prices, or credits.
- Contrast: reading text ≥ 4.5:1 against the ground it actually touches; large text (≥ 24px, or ≥ 18.7px bold) ≥ 3:1. The component pairs in the frontmatter are pre-verified pairings — set text in those pairings, or in the primary ink on the neutral or soft field.
- Reading text is live text, never baked into an image or drawn as paths; any drawn or turned lettering keeps a complete live-text equivalent on the poster.
- One unit, one lead, one primary form (Cover). Static work: no motion, no gradient, no shadow, no rounded corner unless this file explicitly says otherwise.
- Format: 900 × 1200 px (the HTML preview scale, 1px = 1px). Type sizes in the tokens are final sizes at that scale. Set the poster as one self-contained HTML file with inline CSS/SVG and no external assets.

## Colors
The three primaries together: red #D22730, yellow #F2C500, blue #2255A4, with black ink on white and soft off-white; no other hue. Tertiary names the red; blue and yellow are first-class tokens here because the dialect builds with all three.

## Typography
A geometric sans (Poppins) with Inter and Source Han Sans SC; the title is set as a shape — diagonal on the module, lowercase Latin allowed; facts in the grotesque at body size.

## Layout
Poster 900 × 1200 on a 60px square module; every shape is a module multiple, overlapping shapes overprint with multiply; the programme is set in the lower field on the same module.

Composition, in numbers (the module governs the constructed shapes; type and bars take the coordinates given here): yellow circle Ø360 (6 modules) centered at (360,300); red square 300 × 300 (5 modules) at (360,180); blue right triangle with vertices (540,480), (840,480), (540,180) — every vertex on the module; the three overprint with multiply where they cross; an ink bar 780 × 24 at (60,480) closes the figure along the triangle's base line. The title 'the grid' (lowercase, display 120) starts at (60,800) on the baseline, rotated −26.565° — the 1:2 module diagonal — about its left end: it rises through the empty paper field below the figure and ends near (595,533), crossing paper only, never a shape and never the bar. 格网 stands upright at (700,584) at 64px/700 on paper. The exhibition note — the foyer fact from the Source, verbatim — stands at (600,720), 250 wide, 17px. A full-width ink bar at y=840, 72 tall, carries two lines in paper at 26px/700, line-height 1.2, from x=48: the date line over the venue line. The facts zone follows: the subtitle, English at (56,936) then Chinese at (56,964), both in the body token; the three programme rows at a 44px pitch from y=1020 — time at 26px/700 in a 110px column, talk at 20px, note at 16px in secondary on the same line; and a closing line at y=1156 in the label token in secondary: the foyer, admission, and illustrative facts from the Source, in that order.

## Do's and Don'ts
Dialect test: remove the type and the shapes still compose the subject — a circle, square, and triangle locked on the module read as the grid's own elements in balance. Ruled out: shapes scattered off the grid, pastel Bauhaus, geometry pasted beside an ordinary layout.

## Directions
| | Direction | Looks | Why it suits | Grid · faces · color · lead · methods |
|---|---|---|---|---|
| A | Mother tongue, by the book | Quiet white poster, one red accent, hairlines | Correct, and indistinguishable from any competent institute poster | 12-col · grotesque · ink + vermilion · scale contrast |
| B | Mother tongue, pushed | The title at graphic scale over a full accent field | Louder, but the material's own character is still unused | Same grid · same faces · accent field |
| C | Bauhaus | Circle, square, triangle overprinting on the module | The material does what this dialect is for | See Overview and Sequence |

Chosen: C — this set exists to test the dialects at full strength on held-still content; A and B remain written as the control.

## Sequence
Rhythm: a single unit; the rhythm map is the set's — nine posters read as one contact sheet, each a turn from the last, the mother tongue withheld so the dialects must carry the evening alone.

| Unit | Form | Register | Lead | Methods (master · work: imperative + parameters + ban) | Variation (name + magnitude + keep) or continuity (with its rhythm cost) |
|---|---|---|---|---|---|
| 1 | Cover | turn | The constructed figure: yellow circle, red square, blue triangle overprinting on the module | Kandinsky · Point and Line to Plane: assemble the figure from primitives snapped to module multiples (the circle is 6 modules across, the square 5), overprint where they cross; never draw freehand, never round a corner the module did not round | The unit is itself the set's variation: one dialect at full strength; keep condition — every fact from the Source section present and exact |

## Coverage
Text: the title set as a shape, diagonal on the module; facts in the lower field, flush left. Image: constructed, not photographed. Data: programme rows on module lines. Space: the module is the space.

## Gaps
The programme is fictional and marked illustrative on the poster itself. No photography is used in this dialect render. Print proof: the HTML is the preview at poster scale; a press proof is unmade and would be checked before any real printing.

## Record
Folio version: 0.5.3. Template version: 6. Files read: SKILL.md, craft, Swiss theme, bauhaus dialect, poster surface, design-md template, signature.md. Date: 2026-10-31. Family master: none. Part of the dialects-master set; content source: examples/dialects-master/content.md.

## Overrides
Empty: no family master.
