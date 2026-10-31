---
version: alpha
name: The Grid, an evening · De Stijl
description: "One evening's programme held inside a balance of black bars and primary planes."
colors:
  primary: "#111111"
  secondary: "#4A463F"
  tertiary: "#D22730"
  neutral: "#FFFFFF"
  soft: "#E8E6E0"
  line: "#111111"
  dark: "#111111"
  focus: "#005FCC"
  blue: "#2255A4"
  yellow: "#F2C500"
typography:
  display: { fontFamily: "Inter, Source Han Sans SC, Noto Sans SC, sans-serif", fontSize: 150px, fontWeight: 700, lineHeight: 1.05 }
  title: { fontFamily: "Inter, Source Han Sans SC, Noto Sans SC, sans-serif", fontSize: 44px, fontWeight: 700, lineHeight: 1.15 }
  body: { fontFamily: "Inter, Source Han Sans SC, Noto Sans SC, sans-serif", fontSize: 19px, fontWeight: 400, lineHeight: 1.5 }
  label: { fontFamily: "Inter, Source Han Sans SC, Noto Sans SC, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.3 }
spacing:
  margin: 56px
  gutter: 16px
  column: 51px
  columns: 12
  module: 8px
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

**「荷兰风格派（De Stijl）」 — Make this poster as van Doesburg and Mondrian made the compositions: divide the field with black bars, let unequal planes in the three primaries balance, set every word flush-left inside its plane.**

This line governs the file. Where a parameter below and the named hand's evident way of working conflict on atmosphere or composition, the hand wins and the conflict is recorded in Record; the parameters bind absolutely on the facts, the contrast floors, live text, the format, and the bans.

Hands: governed by Mondrian, the compositions (1921–30) — the evening is itself a system of weights, so the relation leads. Guesting: Bart van der Leck's print hand — the colour planes carry whole fact-blocks flat (the FREE plane, the date plane), his way of making content itself a plane. Not taken: van Doesburg's diagonal — this dialect's keeps forbid it, and the school's internal heresy stays outside this deliverable.

## Overview
One poster (print-first, read at arm's length and across a foyer) for a fictional public evening, THE GRID — three talks and a poster exhibition on the system behind modern design. It is one of nine dialect master examples in examples/dialects-master/: the source content (content.md) is identical in all nine; only the design changes. All names, the venue, and the times are illustrative. Theme: Swiss; dialect: De Stijl.
Governing hand: Make this poster as van Doesburg and Mondrian made the compositions: divide the field with black bars on the tracks, let the largest plane lead against unequal counterweights, set every word flush-left inside its plane; never symmetry, never equal cells, never a diagonal.
Signature: none — the balance of planes is the whole work here; a signature method laid over it would compete with the lead, which is a relation, not an object.

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
- **The grid is the picture, not the scaffold.** Black bars on the tracks divide the field; text and images live inside its planes.
- **The lead is a balance, not an object.** The largest plane leads against unequal counterweights; never symmetry, never equal cells.
- **Primaries are planes, not an accent.** Red, yellow, and blue build the structure beside white, grey, and black.
- **Right angles, not rotation,** unless the brief names van Doesburg's Elementarism, which turns the whole field 45°.
**Swiss keeps:** asymmetry, the tracks the bars fall on, and flush-left type inside the planes.
**Test:** Resize or recolor one plane, and the balance of the whole shifts.
**Caricature:** A card grid filled red, yellow, and blue; a black lattice laid over an ordinary page; Mondrian as a border.

### Floors that bind this poster
- Facts are exact: the Source above is the whole material. Add nothing, rename nothing, invent no names, prices, or credits.
- Contrast: reading text ≥ 4.5:1 against the ground it actually touches; large text (≥ 24px, or ≥ 18.7px bold) ≥ 3:1. The component pairs in the frontmatter are pre-verified pairings — set text in those pairings, or in the primary ink on the neutral or soft field.
- Reading text is live text, never baked into an image or drawn as paths; any drawn or turned lettering keeps a complete live-text equivalent on the poster.
- One unit, one lead, one primary form (Cover). Static work: no motion, no gradient, no shadow, no rounded corner unless this file explicitly says otherwise.
- Format: 900 × 1200 px (the HTML preview scale, 1px = 1px). Type sizes in the tokens are final sizes at that scale. Set the poster as one self-contained HTML file with inline CSS/SVG and no external assets.

## Colors
Primary planes carry the structure: red #D22730 is the largest plane, blue #2255A4 and yellow #F2C500 are counterweights, black #111111 is the bars and the ink, white the paper planes, soft #E8E6E0 one grey plane. Tertiary names the red in the token set; paper-on-accent pairs paper text on it. Focus #005FCC is interface-only.

## Typography
One grotesque, Inter with Source Han Sans SC; display at 150px for the plane titles, facts at body and label. Flush left inside every plane; no centered text anywhere.

## Layout
Poster 900 × 1200. Black bars 18px on the twelve-column tracks divide the field into unequal planes; type lives inside planes, flush left, one role per plane.

Composition, in numbers: bars are 18px — one vertical at x=560 running the full height, horizontals at y=300 and y=880 running the full width. Red plane x578–900 × y0–300 carries 格网 in paper at display size, inset 22px from the left, bottom-left, so its box closes inside the trim. Title plane x0–560 × y0–300: the kicker — the words 'A PUBLIC EVENING · 公共讲座之夜' in the label token — at (48,36), and THE GRID on two lines at a declared local 120px with line-height 0.95 (the display token governs 格网 and plane titles; at 150px two lines cannot fit a 300px plane, so this plane's Latin title takes 120 and the arithmetic closes: 36 + 18 + 12 + 228 = 294). Programme plane x0–560 × y318–880: the heading 'PROGRAMME · 节目' in the label token at (48,354), then three rows with 26px between them — time at 30px/700, the talk and speaker on one line at 21px/400, the note at 16px in secondary — and the subtitle at 19px, width 470, at (48,764), closing the plane. The side plane x578–900 × y318–880 is the soft grey plane of the Colors section; it carries the foyer text at 20px, inset 36, from y=354. Yellow plane x0–560 × y898–1200 carries FREE / 免费入场 at 34px/700, inset 48/36, and beneath them at body size 'seats unreserved · 不设座位预订' — the admission fact complete. Blue plane x578–900 × y898–1200 carries the date and venue in paper at 26px/700, line-height 1.45, inset 36, on five lines: 'SAT 14 NOV 2026' / '19:30–22:00' / 'HALL 2' / 'MUSEUM OF DESIGN' / '设计博物馆 二号厅'; the illustrative line stands at its foot in paper at a declared local 12px. Plane text insets are 36–48px; nothing is centered; no plane is divided further.

## Do's and Don'ts
Dialect test: resize or recolor one plane and the balance of the whole shifts — the red plane is the largest, the yellow the smallest, and the programme plane answers both. Ruled out: equal card grids, a black lattice over an ordinary layout, Mondrian as a border.

## Directions
| | Direction | Looks | Why it suits | Grid · faces · color · lead · methods |
|---|---|---|---|---|
| A | Mother tongue, by the book | Quiet white poster, one red accent, hairlines | Correct, and indistinguishable from any competent institute poster | 12-col · grotesque · ink + vermilion · scale contrast |
| B | Mother tongue, pushed | The title at graphic scale over a full accent field | Louder, but the material's own character is still unused | Same grid · same faces · accent field |
| C | De Stijl | Black bars, unequal primary planes, facts inside the white plane | The material does what this dialect is for | See Overview and Sequence |

Chosen: C — this set exists to test the dialects at full strength on held-still content; A and B remain written as the control.

## Sequence
Rhythm: a single unit; the rhythm map is the set's — nine posters read as one contact sheet, each a turn from the last, the mother tongue withheld so the dialects must carry the evening alone.

| Unit | Form | Register | Lead | Methods (master · work: imperative + parameters + ban) | Variation (name + magnitude + keep) or continuity (with its rhythm cost) |
|---|---|---|---|---|---|
| 1 | Cover | turn | The balance itself: the large red plane against the programme's white plane | Mondrian · Composition with Red, Blue and Yellow: build the field from bars on the tracks, planes unequal, primaries as structure not accent; never equal cells, never a centered title block | The unit is itself the set's variation: one dialect at full strength; keep condition — every fact from the Source section present and exact |

## Coverage
Text: all facts inside planes, flush left. Image: none — the planes are the picture. Data: the programme as three rows inside the largest white plane. Space: the bars are the space; no margins beyond the trim.

## Gaps
The programme is fictional and marked illustrative on the poster itself. No photography is used in this dialect render. Print proof: the HTML is the preview at poster scale; a press proof is unmade and would be checked before any real printing.

## Record
Folio version: 0.5.4. Template version: 7. Files read: SKILL.md, craft, Swiss theme, de-stijl dialect, poster surface, design-md template, signature.md. Date: 2026-10-31. Family master: none. Part of the dialects-master set; content source: examples/dialects-master/content.md.

## Overrides
Empty: no family master.
