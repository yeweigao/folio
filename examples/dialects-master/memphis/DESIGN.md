---
version: alpha
name: The Grid, an evening · Memphis
description: "The party on the grid: clashing hues and a patterned band, facts still flush left."
colors:
  primary: "#111111"
  secondary: "#4A463F"
  tertiary: "#D12A66"
  neutral: "#FFFFFF"
  soft: "#FFF3D6"
  line: "#111111"
  dark: "#111111"
  focus: "#005FCC"
  teal: "#0E7C7B"
  yellow: "#F2C500"
  blue: "#2255A4"
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
  paper-on-teal: { backgroundColor: "{colors.teal}", textColor: "{colors.neutral}" }
  ink-on-yellow: { backgroundColor: "{colors.yellow}", textColor: "{colors.primary}" }
  paper-on-blue: { backgroundColor: "{colors.blue}", textColor: "{colors.neutral}" }
---

## Invocation

**「孟菲斯设计（Memphis Group）」、索特萨斯（Ettore Sottsass） — Make this poster as Sottsass and the Memphis group made the 1981 collection: pattern as clothing, glyphs and primitives colliding at jaunty angles, hierarchy by exuberance rather than by system.**

This line governs the file. Where a parameter below and the named hand's evident way of working conflict on atmosphere or composition, the hand wins and the conflict is recorded in Record; the parameters bind absolutely on the facts, the contrast floors, live text, the format, and the bans.

## Overview
One poster (print-first, read at arm's length and across a foyer) for a fictional public evening, THE GRID — three talks and a poster exhibition on the system behind modern design. It is one of nine dialect master examples in examples/dialects-master/: the source content (content.md) is identical in all nine; only the design changes. All names, the venue, and the times are illustrative. Theme: Swiss; dialect: Memphis.
Governing hand: Make this poster as Sottsass and Du Pasquier made the Carlton and the Bacterio laminate: clash saturated hues as relations, clad one surface in pattern as material, let primitives sit at odd proportions — and keep the grid under every line of reading text; never squiggle confetti, never pattern behind text, never pastel nostalgia.
Signature: none — the clash is the dialect's whole register; no single signature method governs a party.

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
- **Color clashes on purpose, not one accent.** Several saturated hues with black and white, chosen as relations.
- **Pattern is material, not ornament.** A laminate-like pattern clads a surface; never behind reading text, never posing as data.
- **Form plays, not only serves.** Primitives at odd proportions and off axis; delight is part of the function.
- **Contrary voices coexist, not resolve.** Type joins the clash in color, weight, and register.
**Swiss keeps:** the grid under reading text, the facts flush left, and every contrast floor.
**Test:** The clash changes how the subject is felt; remove it and the character goes.
**Caricature:** Squiggle confetti on everything, black outlines everywhere, an 80s pastel palette, Memphis as wallpaper behind a Swiss page.

### Floors that bind this poster
- Facts are exact: the Source above is the whole material. Add nothing, rename nothing, invent no names, prices, or credits.
- Contrast: reading text ≥ 4.5:1 against the ground it actually touches; large text (≥ 24px, or ≥ 18.7px bold) ≥ 3:1. The component pairs in the frontmatter are pre-verified pairings — set text in those pairings, or in the primary ink on the neutral or soft field.
- Reading text is live text, never baked into an image or drawn as paths; any drawn or turned lettering keeps a complete live-text equivalent on the poster.
- One unit, one lead, one primary form (Cover). Static work: no motion, no gradient, no shadow, no rounded corner unless this file explicitly says otherwise.
- Format: 900 × 1200 px (the HTML preview scale, 1px = 1px). Type sizes in the tokens are final sizes at that scale. Set the poster as one self-contained HTML file with inline CSS/SVG and no external assets.

## Colors
The clash as relations: pink #D12A66 (tertiary), teal #0E7C7B, yellow #F2C500, blue #2255A4, with black and white; no hue touches reading text — facts are ink on white, and the hues carry the title, the band, and the primitives. Soft #FFF3D6 is the title field.

## Typography
Inter with Source Han Sans SC at display weight for the title; its glyphs cycle pink, teal, blue, ink — in that order, repeating — and yellow is never a glyph color on paper or soft (1.5:1, below the large-text floor): yellow appears only as a ground behind ink glyphs (ink-on-yellow), in the pattern, and as row markers. The Chinese title 格网 takes the title token as paper on a dark chip at the title field's lower right, overlapping the band's top edge. Facts in ink at body size, flush left on the grid.

## Layout
Poster 900 × 1200. Zones in order: title field (soft, y0–430) carrying the kicker at (56,44) and the title THE GRID — its line, tilt, and place inside the field are the hand's (v0.5.3: in this dialect the lead is summoned, not coordinated); the patterned band, outer box y430–640 (190 of pattern between two 10px ink rules, full bleed); the programme zone on white opening at y=640, its first row at y=690; the details block (subtitle EN then CN, when, where, admission — body size, gaps of one module, in Source order); the apparatus at the foot (the illustrative line at a declared local 12px in secondary, bottom-left, 24px from the foot). The Chinese-title chip stands at the title field's lower right: right offset 56, top y=396, padding 8px vertical / 22px horizontal. The title's glyphs cycle pink, teal, blue, ink; a Bacterio-like squiggle band — SVG pattern, tile 90 × 60: one teal squiggle stroke 6px, one pink disc r6, one yellow bar 16 × 8 per tile — clads the middle surface and carries no text; a black triangle (about 200 × 170) and a pink ellipse (about 120 × 150) are dropped onto the band's edges at the hand's angles — jaunty, crossing, never aligned to the grid. Ban: no shape and no pattern ever crosses a line of text; exuberance stops at the facts' edge (the name test's recorded defect). The programme stands black on white, flush left, on the grid, its rows marked by 20px squares in pink, teal, blue, and yellow in row order (the foyer line is the fourth row, marked yellow).

## Do's and Don'ts
Dialect test: remove the clash and the character goes — the same facts read as a committee notice. The pattern is a clad surface with edges, never wallpaper behind the Swiss page. Ruled out: confetti on everything, black outlines everywhere, an 80s pastel palette.

## Directions
| | Direction | Looks | Why it suits | Grid · faces · color · lead · methods |
|---|---|---|---|---|
| A | Mother tongue, by the book | Quiet white poster, one red accent, hairlines | Correct, and indistinguishable from any competent institute poster | 12-col · grotesque · ink + vermilion · scale contrast |
| B | Mother tongue, pushed | The title at graphic scale over a full accent field | Louder, but the material's own character is still unused | Same grid · same faces · accent field |
| C | Memphis | Clashing title letters over a patterned band | The material does what this dialect is for | See Overview and Sequence |

Chosen: C — this set exists to test the dialects at full strength on held-still content; A and B remain written as the control.

## Sequence
Rhythm: a single unit; the rhythm map is the set's — nine posters read as one contact sheet, each a turn from the last, the mother tongue withheld so the dialects must carry the evening alone.

| Unit | Form | Register | Lead | Methods (master · work: imperative + parameters + ban) | Variation (name + magnitude + keep) or continuity (with its rhythm cost) |
|---|---|---|---|---|---|
| 1 | Cover | turn | The title in clashing hues over the patterned band | Du Pasquier · Bacterio patterns: generate the squiggle as a repeating material with declared tile size, clad one bounded surface only; never set text on the pattern, never let the pattern pose as data | The unit is itself the set's variation: one dialect at full strength; keep condition — every fact from the Source section present and exact |

## Coverage
Text: title joins the clash; facts black on white, floors kept. Image: pattern as material, one clad band. Data: programme rows on the grid in ink. Space: play happens at the surfaces; the grid under text does not move.

## Gaps
The programme is fictional and marked illustrative on the poster itself. No photography is used in this dialect render. Print proof: the HTML is the preview at poster scale; a press proof is unmade and would be checked before any real printing.

## Record
Folio version: 0.5.3. Template version: 6. Files read: SKILL.md, craft, Swiss theme, memphis dialect, poster surface, design-md template, signature.md. Date: 2026-10-31. Family master: none. Part of the dialects-master set; content source: examples/dialects-master/content.md.

## Overrides
Empty: no family master.
