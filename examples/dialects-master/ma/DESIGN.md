---
version: alpha
name: The Grid, an evening · ma 間
description: "One small grid, low on a large white field; the interval does the inviting."
colors:
  primary: "#2B2B28"
  secondary: "#6B675C"
  tertiary: "#A63A2E"
  neutral: "#FAF8F3"
  soft: "#F1EEE6"
  line: "#D8D3C6"
  dark: "#2B2B28"
  focus: "#005FCC"
typography:
  display: { fontFamily: "'Hiragino Mincho ProN', 'Songti SC', 'Noto Serif SC', serif", fontSize: 64px, fontWeight: 700, lineHeight: 1.05 }
  title: { fontFamily: "'Hiragino Mincho ProN', 'Songti SC', 'Noto Serif SC', serif", fontSize: 44px, fontWeight: 700, lineHeight: 1.15 }
  body: { fontFamily: "Inter, Source Han Sans SC, Noto Sans SC, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.45 }
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
---

## Overview
One poster (print-first, read at arm's length and across a foyer) for a fictional public evening, THE GRID — three talks and a poster exhibition on the system behind modern design. It is one of nine dialect master examples in examples/dialects-master/: the source content (content.md) is identical in all nine; only the design changes. All names, the venue, and the times are illustrative. Theme: Swiss; dialect: Kenya Hara, ma 間.
Governing hand: Make this poster as Kenya Hara made the Horizon campaign: gather the content so one large interval stays whole, let the subject lead by isolation at small scale, set the type quiet in Mincho on unbleached paper, one small vermillion mark at most; never Zen props, never an empty page with nothing worth seeing, never type below the floors.
Signature: none — emptiness is the dialect's vessel; the signature tier adds moves, and this work's move is a held interval.

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
- **Emptiness is a vessel, not spacing.** Content gathers so one large interval stays whole; it frames the content, never replaces it.
- **One thing leads by isolation, not by scale.** Small, quiet type in a large field; position, horizon, and interval set the hierarchy, and centering is allowed; the subject stays identifiable at viewing size.
- **The image evokes, not proves.** Material, light, and the ordinary seen again; never posed as evidence.
- **Mincho and paper, not a black grotesque.** A Song or Mincho serif with a quiet sans; white or unbleached stock, soft ink, one small mark at most.
**Swiss keeps:** the grid, exact placement on it, and the type floors.
**Test:** The emptiness changes how the subject is felt, and the subject rewards the attention.
**Caricature:** Zen props, stones, bamboo, brush ink; an empty page with nothing worth seeing; type too small to read.

### Floors that bind this poster
- Facts are exact: the Source above is the whole material. Add nothing, rename nothing, invent no names, prices, or credits.
- Contrast: reading text ≥ 4.5:1 against the ground it actually touches; large text (≥ 24px, or ≥ 18.7px bold) ≥ 3:1. The component pairs in the frontmatter are pre-verified pairings — set text in those pairings, or in the primary ink on the neutral or soft field.
- Reading text is live text, never baked into an image or drawn as paths; any drawn or turned lettering keeps a complete live-text equivalent on the poster.
- One unit, one lead, one primary form (Cover). Static work: no motion, no gradient, no shadow, no rounded corner unless this file explicitly says otherwise.
- Format: 900 × 1200 px (the HTML preview scale, 1px = 1px). Type sizes in the tokens are final sizes at that scale. Set the poster as one self-contained HTML file with inline CSS/SVG and no external assets.

## Colors
Unbleached paper #FAF8F3, soft ink #2B2B28, secondary #6B675C for the quietest apparatus, line #D8D3C6 for the horizon. Tertiary #A63A2E is the vermillion of the single 10px mark — the only saturated pixel-field on the poster. Focus is interface-only.

## Typography
Mincho for the title (Hiragino Mincho ProN, Songti SC, Noto Serif SC) at 64px; the facts in a quiet sans at body size, gathered at the horizon; nothing below the label token (14px).

## Layout
Poster 900 × 1200. Composition, in numbers: the kicker — the words 'MUSEUM OF DESIGN · 设计博物馆' in the label token, letter-spacing 0.22em, in the primary ink — stands at (64,56), the only thing in the upper field. A horizon rule is drawn at y=700, from x=64 to x=836, 1px in the line color; above it, one unbroken field of paper. The subject — a nine-square grid drawn at 96 × 96 (three 32px cells), stroke 1.5px in the primary ink — stands at (120,732). The title stands at (288,738): 格网 in Mincho at display 64, then a 24px gap, then THE GRID at 40px/700 on the same line. The one vermillion mark, a 10 × 10 square, stands at (292,846). The facts stand at (120,884), width 716, in body 18/1.45, as these lines verbatim, in this order: 'Three talks and a poster exhibition on the system behind modern design.' / '三场讲座，一场海报展——现代设计背后的系统' / '19:30　模块 · The Module — Josef Müller-Brockmann · the grid for print' / '20:15　系统 · The System — Otl Aicher · rules for every case' / '21:00　间 · The Interval — Kenya Hara · emptiness as a vessel' / '2026年11月14日 星期六 · Saturday 14 November 2026 · 19:30–22:00 · Hall 2, Museum of Design 设计博物馆 二号厅' / '门厅海报展自 19:00 · Foyer poster exhibition from 19:00 · Admission free, seats unreserved · 免费入场，不设座位预订 · Illustrative example 虚构节目示例'. The two long lines wrap inside the measure; the stack is nine rendered lines and ends at approximately y=1120, inside the bottom margin. There is no separate subtitle block and no footer: the subtitle is the facts' first two lines, and the illustrative line closes the facts. If a value must move, move the horizon up, never shrink the type.

## Do's and Don'ts
Dialect test: the emptiness changes how the subject is felt — the small grid reads as precious because the field withholds everything else; and the subject rewards the attention, being the evening's whole subject in nine squares. Ruled out: stones, bamboo, brush ink; type too small to read (no text below the label token, 14px, at poster scale).

## Directions
| | Direction | Looks | Why it suits | Grid · faces · color · lead · methods |
|---|---|---|---|---|
| A | Mother tongue, by the book | Quiet white poster, one red accent, hairlines | Correct, and indistinguishable from any competent institute poster | 12-col · grotesque · ink + vermilion · scale contrast |
| B | Mother tongue, pushed | The title at graphic scale over a full accent field | Louder, but the material's own character is still unused | Same grid · same faces · accent field |
| C | Kenya Hara, ma 間 | A small grid low on an unbroken white field | The material does what this dialect is for | See Overview and Sequence |

Chosen: C — this set exists to test the dialects at full strength on held-still content; A and B remain written as the control.

## Sequence
Rhythm: a single unit; the rhythm map is the set's — nine posters read as one contact sheet, each a turn from the last, the mother tongue withheld so the dialects must carry the evening alone.

| Unit | Form | Register | Lead | Methods (master · work: imperative + parameters + ban) | Variation (name + magnitude + keep) or continuity (with its rhythm cost) |
|---|---|---|---|---|---|
| 1 | Cover | turn | The small grid at the horizon, held by the interval | Hara · Horizon, 2003: compose by interval — content gathered low, one horizon, the field left whole; never fill the field to justify the format, never center by default (placement is on the grid) | The unit is itself the set's variation: one dialect at full strength; keep condition — every fact from the Source section present and exact |

## Coverage
Text: title and facts gathered at the horizon, quiet but at floor sizes. Image: the nine-square grid, drawn, the subject itself. Data: the three talks in three quiet lines with their times. Space: the interval is the composition; it is placed, not left over.

## Gaps
The programme is fictional and marked illustrative on the poster itself. No photography is used in this dialect render. Print proof: the HTML is the preview at poster scale; a press proof is unmade and would be checked before any real printing.

## Record
Folio version: 0.5.2. Template version: 5. Files read: SKILL.md, craft, Swiss theme, ma dialect, poster surface, design-md template, signature.md. Date: 2026-10-31. Family master: none. Part of the dialects-master set; content source: examples/dialects-master/content.md.

## Overrides
Empty: no family master.
