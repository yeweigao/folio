---
version: alpha
name: The Grid, an evening · Ulm
description: "The evening as a small system: codes, pictograms, and rules a stranger can extend."
colors:
  primary: "#111111"
  secondary: "#4A463F"
  tertiary: "#D22730"
  neutral: "#FFFFFF"
  soft: "#EFF0EC"
  line: "#B9BDC2"
  dark: "#111111"
  focus: "#005FCC"
  blue: "#2255A4"
typography:
  display: { fontFamily: "Inter, Source Han Sans SC, Noto Sans SC, sans-serif", fontSize: 104px, fontWeight: 700, lineHeight: 1.05 }
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
---

## Invocation

**「乌尔姆设计学院（HfG Ulm）」 — Make this poster as Aicher and Bill made the Ulm system: decide the rules before the page, color only as labelled code, pictograms a stranger can extend.**

This line governs the file's atmosphere and judgment. The parameters bind absolutely on the facts, the contrast floors, live text, the format, and the bans — and on this file's own invention, the route line, which the name cannot know and which therefore stands below as discipline, not as summoning.

Hands: governed by Aicher — the evening is a system a stranger must use, so the code-and-route hand leads. Guesting: Max Bill's concrete hand — the pictograms are built as concrete signs, systematic variations on one law, inside Aicher's system.

## Overview
One poster (print-first, read at arm's length and across a foyer) for a fictional public evening, THE GRID — three talks and a poster exhibition on the system behind modern design. It is one of nine dialect master examples in examples/dialects-master/: the source content (content.md) is identical in all nine; only the design changes. All names, the venue, and the times are illustrative. Theme: Swiss; dialect: Ulm.
Governing hand: Make this poster as Aicher made the Munich 1972 system: decide the rules before the page — one grotesque, color as code with a legend and a direct label, pictograms built solid on a modular grid, the primary language above and the second below; never three kinds of arrow, never a difference without a nameable reason.
Signature programme: Route line (signature card) — the evening's order is one continuous line through three stops at 0° and 90°, stops as equal nodes, labels on the line's axis; a visitor traces it without lifting a finger.

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
- **The system is the design, not the page.** Rules for every case come first; each unit is one application another designer could extend.
- **Function justifies every difference, not taste.** Same function, same treatment; each difference in size, color, or position has a nameable reason.
- **Color and pictograms are codes, not accents.** A few mapped colors, decoded by direct labels or a legend, never the only cue; one pictogram set of solid figures built on a modular grid at 0°, 45°, and 90°.
- **Instruction, not expression.** Short, unambiguous lines; the primary language above, the second below, never in one line.
**Swiss keeps:** the grid, one grotesque after Univers, asymmetry, and the rule, now used as a code.
**Test:** A stranger knows what to do next, and a designer could apply the rules to a new case.
**Caricature:** Sports pictograms and the Munich palette pasted onto an ordinary page; UI line icons; three kinds of arrow.

### Floors that bind this poster
- Facts are exact: the Source above is the whole material. Add nothing, rename nothing, invent no names, prices, or credits.
- Contrast: reading text ≥ 4.5:1 against the ground it actually touches; large text (≥ 24px, or ≥ 18.7px bold) ≥ 3:1. The component pairs in the frontmatter are pre-verified pairings — set text in those pairings, or in the primary ink on the neutral or soft field.
- Reading text is live text, never baked into an image or drawn as paths; any drawn or turned lettering keeps a complete live-text equivalent on the poster.
- One unit, one lead, one primary form (Cover). Static work: no motion, no gradient, no shadow, no rounded corner unless this file explicitly says otherwise.
- Format: 900 × 1200 px (the HTML preview scale, 1px = 1px). Type sizes in the tokens are final sizes at that scale. Set the poster as one self-contained HTML file with inline CSS/SVG and no external assets.

### The signature card, in full (Route line)
**Construction.** A sequence is drawn as one continuous line through
ordered stops on the grid; stops are nodes on the line, labelled in
reading order; branches are drawn only where the sequence truly forks.
The line is straight segments at 0°, 45°, or 90°.
**Parameters.** One line weight for the route (2px screen / 1pt print),
stops as equal nodes; labels never leave the line's axis; the whole
route fits one unit or continues across units at the same height.
**Test.** A reader can trace the route with a finger without lifting it
and recite the order back; remove the labels and the order is still
legible from the line alone.
**Caricature.** A wavy decorative path with icons pinned to it; arrows
between boxes doing the line's job; a timeline with stops floating off
the axis.

## Colors
Ink on white; code colors mapped once: blue #2255A4 codes the talks, red #D22730 (tertiary) codes the exhibition branch, each decoded by a direct label and the header legend — never color alone. Soft #EFF0EC is the header field; line #B9BDC2 rules the system table.

## Typography
One grotesque after Univers: Inter with Source Han Sans SC. Primary language above, second below, never in one line; display is reserved for the title; the stop times take a declared 27px/700.

## Layout
Poster 900 × 1200. A rule header states the system (code colors, pictogram set); the route line runs down the left axis through the three talks as stops; the foyer exhibition is a coded branch with its label; bilingual lines never share a line.

Composition, in numbers: the system header occupies the soft field to y≈152, closed by a 2px ink rule; its text states the code (blue chip 14px = Talk 讲座， red chip = Exhibition 展览， every code also labelled) and shows the pictogram set. The title block stands at top 196, its content inset at the 56px margin: the kicker — the words 'A PUBLIC EVENING · 公共讲座之夜' in the label token, tracked 0.14em — then THE GRID at display 104, 格网 at 40px/700, subtitle EN at 18px then CN at 16px in secondary — never on one line. The route line is 4px ink on the axis x=150, running y470–950 (the signature card's screen parameter is 2px; at poster scale this system takes 4px, recorded here as this deliverable's value). An entry node — ink disc, same construction — stands on the axis at (150,470), and the exhibition branch forks there, running right to a red node at x=490: the foyer is open from 19:00, before the first talk, and the line then descends through the three stops; stops are nodes of 32px — a code-color disc with a 5px paper ring and a 2px ink outline — at y520 (19:30), y700 (20:15), y880 (21:00); times and stop text are centered on each node's y; times at 27px/700 in tabular figures, right-aligned to end 10px left of the axis; stop text from x=206, three lines: the name at 25px/700 ('1 · The Module'), the speaker-and-note line at 17px ('Josef Müller-Brockmann · the grid for print'), and the Chinese line at 15.5px in secondary ('模块 · 约瑟夫·米勒-布罗克曼：印刷的格网'; stop 2: '2 · The System' / 'Otl Aicher · rules for every case' / '系统 · 奥托·艾舍：为每种情形立法'; stop 3: '3 · The Interval' / 'Kenya Hara · emptiness as a vessel' / '间 · 原研哉：以空为器'). The branch label stands right of the red node at x=530: 'Foyer · Poster exhibition' at 21px/700 over 'From 19:00 · nine dialects, one mother tongue · 门厅海报展' at 15.5px. The remaining facts (when, where, admission, the illustrative line) stand in a footer apparatus at the foot of the poster in the label token, secondary for the illustrative line. The system header's soft field runs y0–150 exactly, closed by its 2px ink rule at y150–152, its content inset at the 56px margin. Pictograms, one set, solid, built on a 8px module at 0/45/90°: Module = four squares in a 2 × 2 block; System = three filled circles joined by bars; Interval = an open square frame; Exhibition = a frame with a filled inner square — each drawn at 40px beside its stop's name, in ink, the code color reserved to nodes and chips.

## Do's and Don'ts
Dialect test: a stranger knows what to do next — enter, foyer, hall, in that order, from the line alone; and the rules stated in the header would let another designer add a fourth talk. Ruled out: Munich pictograms pasted on, UI line icons, decoration.

## Directions
| | Direction | Looks | Why it suits | Grid · faces · color · lead · methods |
|---|---|---|---|---|
| A | Mother tongue, by the book | Quiet white poster, one red accent, hairlines | Correct, and indistinguishable from any competent institute poster | 12-col · grotesque · ink + vermilion · scale contrast |
| B | Mother tongue, pushed | The title at graphic scale over a full accent field | Louder, but the material's own character is still unused | Same grid · same faces · accent field |
| C | Ulm | A route line of stops, coded colors, pictograms | The material does what this dialect is for | See Overview and Sequence |

Chosen: C — this set exists to test the dialects at full strength on held-still content; A and B remain written as the control.

## Sequence
Rhythm: a single unit; the rhythm map is the set's — nine posters read as one contact sheet, each a turn from the last, the mother tongue withheld so the dialects must carry the evening alone.

| Unit | Form | Register | Lead | Methods (master · work: imperative + parameters + ban) | Variation (name + magnitude + keep) or continuity (with its rhythm cost) |
|---|---|---|---|---|---|
| 1 | Cover | turn | The route line: the evening as one traceable order | Aicher · Munich 1972 pictogram system: build every sign solid on the module grid at 0/45/90°, code color mapped once and decoded by label; never outline icons, never color as the only cue | The unit is itself the set's variation: one dialect at full strength; keep condition — every fact from the Source section present and exact |

## Coverage
Text: short unambiguous lines, EN above CN. Image: pictograms only, as code. Data: the programme as stops on the route line with times at the nodes. Space: the grid decides; nothing is placed by eye.

## Gaps
The programme is fictional and marked illustrative on the poster itself. No photography is used in this dialect render. Print proof: the HTML is the preview at poster scale; a press proof is unmade and would be checked before any real printing.

## Record
Folio version: 0.5.4. Template version: 7. Files read: SKILL.md, craft, Swiss theme, ulm dialect, poster surface, design-md template, signature.md. Date: 2026-10-31. Family master: none. Part of the dialects-master set; content source: examples/dialects-master/content.md.

## Overrides
Empty: no family master.
