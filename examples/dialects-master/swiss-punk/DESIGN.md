---
version: alpha
name: The Grid, an evening · Swiss Punk
description: "The grid tested by its own subject: stepped, rotated, overprinted — and still readable."
colors:
  primary: "#111111"
  secondary: "#4A463F"
  tertiary: "#D10015"
  neutral: "#F5F2EA"
  soft: "#E9E4D6"
  line: "#111111"
  dark: "#111111"
  focus: "#005FCC"
  blue: "#2255A4"
typography:
  display: { fontFamily: "Inter, Source Han Sans SC, Noto Sans SC, sans-serif", fontSize: 168px, fontWeight: 800, lineHeight: 1.05 }
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

**沃尔夫冈·魏因加特（Wolfgang Weingart）的「瑞士朋克排印（Swiss Punk / New Wave）」 — Make this poster as Weingart made the Kunsthalle posters: break the baseline, step the text, slip the register, layer the process marks until the grid is tested everywhere at once.**

This line governs the file. Where a parameter below and the named hand's evident way of working conflict on atmosphere or composition, the hand wins and the conflict is recorded in Record; the parameters bind absolutely on the facts, the contrast floors, live text, the format, and the bans.

Hands: governed by Weingart — the subject is a system tested by its own rebellion. Guesting: April Greiman's floating layers — the rotated outline setting drifts off-register above the construction, her depth without shadows.

## Overview
One poster (print-first, read at arm's length and across a foyer) for a fictional public evening, THE GRID — three talks and a poster exhibition on the system behind modern design. It is one of nine dialect master examples in examples/dialects-master/: the source content (content.md) is identical in all nine; only the design changes. All names, the venue, and the times are illustrative. Theme: Swiss; dialect: Swiss Punk.
Governing hand: Make this poster as Weingart made the Basel typographic posters: keep the grotesque and the grid, then test them — step the baselines, rotate the display line, slip one ink off register by a fraction of a stroke; body text, labels, and data stay horizontal on the grid; never glitch filters, never an illegible stack, never one tilted word as a garnish.
Signature: none — displacement is this dialect's grammar, applied through the whole piece; a single signature method would localise what must be systemic.

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
- **The grid is tested, not obeyed.** Rotation, stepped baselines, and displacement run through the piece as its grammar.
- **Type speaks, not only sizes.** Spacing, weight, and direction change within a display line; several registers collide.
- **Layers overprint off register, not apart.** Two or three inks of one word or shape, slipped by a fraction of a stroke, still read as one form with a vibrating edge, like a misregistered offset proof; screens and montage stack on the same axis; never under reading text.
- **The process is the image, not a texture.** Film montage, enlarged halftone, early bitmap type.
**Swiss keeps:** the grotesque, the grid as the reference being tested, and body text, labels, and data horizontal on it.
**Test:** The typographic relations themselves express the subject; remove one tilted word and the dialect survives.
**Caricature:** Glitch filters, random distress, illegible stacks; a word repeated and spread down the page like an echo; one rotated word on an otherwise Swiss page.

### Floors that bind this poster
- Facts are exact: the Source above is the whole material. Add nothing, rename nothing, invent no names, prices, or credits.
- Contrast: reading text ≥ 4.5:1 against the ground it actually touches; large text (≥ 24px, or ≥ 18.7px bold) ≥ 3:1. The component pairs in the frontmatter are pre-verified pairings — set text in those pairings, or in the primary ink on the neutral or soft field.
- Reading text is live text, never baked into an image or drawn as paths; any drawn or turned lettering keeps a complete live-text equivalent on the poster.
- One unit, one lead, one primary form (Cover). Static work: no motion, no gradient, no shadow, no rounded corner unless this file explicitly says otherwise.
- Format: 900 × 1200 px (the HTML preview scale, 1px = 1px). Type sizes in the tokens are final sizes at that scale. Set the poster as one self-contained HTML file with inline CSS/SVG and no external assets.

## Colors
Ink on off-white #F5F2EA; the red #D10015 is the slipped second ink, blue #2255A4 appears once in a stepped line. Tertiary names the red; Line is ink: in this dialect the tested grid's rules are drawn in ink at hairline weight in the apparatus zone only.

## Typography
One grotesque, Inter with Source Han Sans SC, in colliding registers: display at 168px, the stepped lines at 27px with shifting weights, facts at body size, horizontal, always.

## Layout
Poster 900 × 1200. Zones in order: kicker — the words 'A PUBLIC EVENING · 公共讲座之夜 · BASEL RULES, TESTED' in the label token, tracked 0.14em — at top 44; the title construction from y=120, 430 tall; the stepped subtitle at y=600; the programme from y=900 behind a 3px ink rule; apparatus at the foot. The title construction is summoned, not coordinated (v0.5.3, from the name test): the title stands at display 168/800 in ink with its own red copy slipped off-register behind it (about 4px — the hand judges the slip), its baseline broken, letters dropped and lifted as Weingart breaks them; a rotated outline setting (格网 GRID, about 96px, ink stroke, transparent fill) crosses the construction. Displacement, stepping, and layering are the grammar. Ban: no displacement ever covers a fact — collisions stop at the facts' edge, the name test's recorded defect. The subtitle is set as three stepped lines at 27px — 'Three talks and a poster exhibition' (indent 0, weight 400), 'on the system behind modern design' (indent 48, weight 600, the words 'modern design' in blue, the stepped setting's one blue), '三场讲座，一场海报展' (indent 96, weight 800). Below the programme rows, the remaining facts stand as two meta lines at 17px (date and venue; foyer and admission), and the illustrative line closes the poster at a declared local 12px in secondary, bottom-left. A halftone dot field fills one band inside the stepped zone: dots of 2.2px radius on a 15px pitch, ink on paper, 120 tall. The programme block stays horizontal and flush left on the grid — the reference the testing is measured against.

## Do's and Don'ts
Dialect test: the typographic relations express the subject — a grid arguing with itself; remove the rotated title and the dialect survives in the stepped lines and the slipped overprint. Ruled out: random distress, echoed words spread down the page, illegibility.

## Directions
| | Direction | Looks | Why it suits | Grid · faces · color · lead · methods |
|---|---|---|---|---|
| A | Mother tongue, by the book | Quiet white poster, one red accent, hairlines | Correct, and indistinguishable from any competent institute poster | 12-col · grotesque · ink + vermilion · scale contrast |
| B | Mother tongue, pushed | The title at graphic scale over a full accent field | Louder, but the material's own character is still unused | Same grid · same faces · accent field |
| C | Swiss Punk | The title obeyed, stepped, then rotated, inks slipped | The material does what this dialect is for | See Overview and Sequence |

Chosen: C — this set exists to test the dialects at full strength on held-still content; A and B remain written as the control.

## Sequence
Rhythm: a single unit; the rhythm map is the set's — nine posters read as one contact sheet, each a turn from the last, the mother tongue withheld so the dialects must carry the evening alone.

| Unit | Form | Register | Lead | Methods (master · work: imperative + parameters + ban) | Variation (name + magnitude + keep) or continuity (with its rhythm cost) |
|---|---|---|---|---|---|
| 1 | Cover | turn | The title, three times: obeyed, stepped, rotated — the grid tested | Weingart · Basel posters, 1970s: run rotation, stepping, and off-register overprint through the display type as grammar, apparatus horizontal; never distress the reading text, never rotate the facts | The unit is itself the set's variation: one dialect at full strength; keep condition — every fact from the Source section present and exact |

## Coverage
Text: display type tested, facts untouched and horizontal. Image: a halftone field as process, not texture. Data: programme rows on the grid. Space: layers share one axis; displacement is measured in degrees and pixels, recorded here.

## Gaps
The programme is fictional and marked illustrative on the poster itself. No photography is used in this dialect render. Print proof: the HTML is the preview at poster scale; a press proof is unmade and would be checked before any real printing.

## Record
Folio version: 0.5.4. Template version: 7. Files read: SKILL.md, craft, Swiss theme, swiss-punk dialect, poster surface, design-md template, signature.md. Date: 2026-10-31. Family master: none. Part of the dialects-master set; content source: examples/dialects-master/content.md.

## Overrides
Empty: no family master.
