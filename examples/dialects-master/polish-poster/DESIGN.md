---
version: alpha
name: The Grid, an evening · Polish Poster School
description: "One authored metaphor: the net that catches the letters."
colors:
  primary: "#1A1A1A"
  secondary: "#5A4A38"
  tertiary: "#9C2B1E"
  neutral: "#E8DCC3"
  soft: "#DFD2B2"
  line: "#8A7A5C"
  dark: "#1A1A1A"
  focus: "#005FCC"
  teal: "#2E5E4E"
typography:
  display: { fontFamily: "Inter, Source Han Sans SC, Noto Sans SC, sans-serif", fontSize: 120px, fontWeight: 800, lineHeight: 1.05 }
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
---

## Invocation

**「波兰海报学派（Polish Poster School）」 — Make this poster as Tomaszewski's school made the film posters: a painted metaphor before any information, letters manhandled by hand, the facts demoted to a quiet block at the foot.**

This line governs the file. Where a parameter below and the named hand's evident way of working conflict on atmosphere or composition, the hand wins and the conflict is recorded in Record; the parameters bind absolutely on the facts, the contrast floors, live text, the format, and the bans.

Hands: governed by Tomaszewski — the subject, the grid itself, can be said as one painterly metaphor. No guest: a single-image poster has one metaphor, and Trepkowski's stark symbol or Cieślewicz's montage would split its voice; both stand in the roster, deliberately not taken.

## Overview
One poster (print-first, read at arm's length and across a foyer) for a fictional public evening, THE GRID — three talks and a poster exhibition on the system behind modern design. It is one of nine dialect master examples in examples/dialects-master/: the source content (content.md) is identical in all nine; only the design changes. All names, the venue, and the times are illustrative. Theme: Swiss; dialect: Polish Poster School.
Governing hand: Make this poster as Lenica made the Wozzeck poster: give the picture to one metaphor in one hand's line — here cut paper, a net of black bars falling over loose letters — and give the facts to the grid in live type; never a brush font, never distress as decoration, never a metaphor unrelated to the subject.
Signature: none — the authored metaphor is the dialect's own decisive move; the signature tier serves methods, and this work's method is the picture itself.

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
- **The image interprets, not reports.** One visual metaphor states a view of the subject; it never poses as evidence.
- **The hand shows, not hides.** Brush, crayon, cut paper, or montage, in one named artist's line, not a blend of all.
- **Lettering belongs to the picture, not beside it.** Drawn titles join the image; every fact also stands as live type.
- **The idea holds the composition, not the grid.** Image and title arrange around the metaphor.
**Swiss keeps:** the facts: date, place, and credits flush left on the grid, in live type.
**Test:** The picture says something about this subject that a photograph of it could not.
**Caricature:** A brush font, distressed paper, and a surreal object unrelated to the subject.

### Floors that bind this poster
- Facts are exact: the Source above is the whole material. Add nothing, rename nothing, invent no names, prices, or credits.
- Contrast: reading text ≥ 4.5:1 against the ground it actually touches; large text (≥ 24px, or ≥ 18.7px bold) ≥ 3:1. The component pairs in the frontmatter are pre-verified pairings — set text in those pairings, or in the primary ink on the neutral or soft field.
- Reading text is live text, never baked into an image or drawn as paths; any drawn or turned lettering keeps a complete live-text equivalent on the poster.
- One unit, one lead, one primary form (Cover). Static work: no motion, no gradient, no shadow, no rounded corner unless this file explicitly says otherwise.
- Format: 900 × 1200 px (the HTML preview scale, 1px = 1px). Type sizes in the tokens are final sizes at that scale. Set the poster as one self-contained HTML file with inline CSS/SVG and no external assets.

## Colors
The picture's palette: ochre paper #E8DCC3 as neutral, ink #1A1A1A, the red #9C2B1E of the falling letters, a deep teal #2E5E4E as the net's counterweight, soft #DFD2B2 as the shaded plane. Tertiary names the red; paper-on-accent pairs the neutral on it at display weight only.

## Typography
Live type in Inter with Source Han Sans SC; the title lettering is live text turned letter by letter inside the picture (a complete live title also stands in the facts block, per the floors).

## Layout
Poster 900 × 1200 on ochre paper. The upper two-thirds are the picture: cut-paper letters tumbling into a net of black bars, the title lettering drawn as part of the picture (each letter a live-text span, turned by hand-like amounts). Facts stand flush left on the grid below, in live type.

Composition, in numbers: the picture occupies y0–760 on the ochre ground. The picture is summoned, not coordinated (v0.5.3, from the name test): the title lettering is manhandled by hand — T H E G R I D as live spans at display/800 across the top of the field, each letter nudged and turned (within ±6°), G and the I in the red, the rest in ink; their exact places are the hand's. Five loose letters fall through the middle field (a in red, k in ink, m in teal, z in ink, q in teal) at 50–58px and weight 700, turned as they fall. The net is drawn by hand beneath them: a field of black bars, roughly 760 × 300 in the picture's lower half, its lines allowed to sag under the caught glyphs — never ruled straight, never mechanical; a net that could be drawn with a ruler has failed and is redrawn. Caught glyphs stand upright in the cells at 44px/800 — first row: 19, 30 (red), 格， 网 (teal), 间； second row: 序 (teal), 列， 统 (red), 系， 块 (red). The facts block begins at y806, left 56, width 788: the live title at the title token, subtitle at 19px, programme rows at 19px with times bold, then the when/where/admission lines, then the illustrative line in secondary.

## Do's and Don'ts
Dialect test: the picture says what a photograph could not — that the grid is a net: it catches falling letters and holds them in order. Ruled out: a surreal object unrelated to the subject, a brush font, distressed paper texture.

## Directions
| | Direction | Looks | Why it suits | Grid · faces · color · lead · methods |
|---|---|---|---|---|
| A | Mother tongue, by the book | Quiet white poster, one red accent, hairlines | Correct, and indistinguishable from any competent institute poster | 12-col · grotesque · ink + vermilion · scale contrast |
| B | Mother tongue, pushed | The title at graphic scale over a full accent field | Louder, but the material's own character is still unused | Same grid · same faces · accent field |
| C | Polish Poster School | Cut-paper letters caught in a net of bars | The material does what this dialect is for | See Overview and Sequence |

Chosen: C — this set exists to test the dialects at full strength on held-still content; A and B remain written as the control.

## Sequence
Rhythm: a single unit; the rhythm map is the set's — nine posters read as one contact sheet, each a turn from the last, the mother tongue withheld so the dialects must carry the evening alone.

| Unit | Form | Register | Lead | Methods (master · work: imperative + parameters + ban) | Variation (name + magnitude + keep) or continuity (with its rhythm cost) |
|---|---|---|---|---|---|
| 1 | Cover | turn | The metaphor: loose letters caught in the net of the grid | Lenica · Wozzeck, 1964: state the subject as one cut-paper metaphor, letters drawn into the picture, facts kept as live type on the grid; never let the metaphor pose as evidence, never blend two hands | The unit is itself the set's variation: one dialect at full strength; keep condition — every fact from the Source section present and exact |

## Coverage
Text: title inside the picture as turned live letters; all facts as live type below. Image: the authored metaphor, cut-paper construction. Data: programme rows flush left under the picture. Space: the ochre field is the picture's ground.

## Gaps
The programme is fictional and marked illustrative on the poster itself. No photography is used in this dialect render. Print proof: the HTML is the preview at poster scale; a press proof is unmade and would be checked before any real printing.

## Record
Folio version: 0.5.4. Template version: 7. Files read: SKILL.md, craft, Swiss theme, polish-poster dialect, poster surface, design-md template, signature.md. Date: 2026-10-31. Family master: none. Part of the dialects-master set; content source: examples/dialects-master/content.md.

## Overrides
Empty: no family master.
