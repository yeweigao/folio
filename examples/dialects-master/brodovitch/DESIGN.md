---
version: alpha
name: The Grid, an evening · Brodovitch
description: "A Didot word cut by a figure in motion; the evening as a magazine cover."
colors:
  primary: "#111111"
  secondary: "#59544C"
  tertiary: "#7A1F1F"
  neutral: "#FFFFFF"
  soft: "#F2EFE9"
  line: "#C5C2BC"
  dark: "#111111"
  focus: "#005FCC"
typography:
  display: { fontFamily: "Didot, 'Bodoni MT', 'Playfair Display', 'Songti SC', serif", fontSize: 320px, fontWeight: 700, lineHeight: 1.05 }
  title: { fontFamily: "Didot, 'Bodoni MT', 'Playfair Display', 'Songti SC', serif", fontSize: 44px, fontWeight: 700, lineHeight: 1.15 }
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
---

## Invocation

**亚历山大·布罗多维奇（Alexey Brodovitch），《Harper's Bazaar》时期 — Make this poster as Brodovitch made the Bazaar covers: one Didot word and one figure in motion colliding at theatrical scale, the crop daring, the apparatus whispered in tracked capitals on a centered axis.**

This line governs the file. Where a parameter below and the named hand's evident way of working conflict on atmosphere or composition, the hand wins and the conflict is recorded in Record; the parameters bind absolutely on the facts, the contrast floors, live text, the format, and the bans.

## Overview
One poster (print-first, read at arm's length and across a foyer) for a fictional public evening, THE GRID — three talks and a poster exhibition on the system behind modern design. It is one of nine dialect master examples in examples/dialects-master/: the source content (content.md) is identical in all nine; only the design changes. All names, the venue, and the times are illustrative. Theme: Swiss; dialect: Brodovitch.
Governing hand: Make this poster as Brodovitch made the Harper's Bazaar covers: let one Didot word and one figure in motion collide on a centered axis, the crop daring and the apparatus in small tracked capitals; never gold, never a script face, never a photograph that merely sits beside the type.
Signature programme: Cut-out (signature card) — the figure is cut from its ground and passes in front of the display word and behind its last letter, crossing both; edge clean at final size; reading text never sits on the figure.

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
- **Type and image collide, not sit side by side.** A Didot or Bodoni display word covers, cuts, or yields to the photograph; a text block may echo the figure's line.
- **The photograph is desire, not fact.** The body in motion, a daring crop that keeps one gesture; credits name model, garment, and photographer, and never invent one.
- **The issue is paced like film, not stacked as pages.** Scale, crop, and white change from spread to spread; a quiet spread prepares a loud one.
- **Black and white is the palette, not a restraint.** Deep black and paper white; one cool accent or one duotone at most.
- **A centered axis is allowed.** Covers and openers may hang on one axis; place, date, and name in small tracked capitals.
**Swiss keeps:** the column grid, white as structure, and reading text and credits in a quiet grotesque.
**Test:** Remove the type, and the photograph loses its composition; remove the photograph, and the type loses its reason.
**Caricature:** Fake luxury: gold gradients, rose gold, glass, script fonts, a centered serif logo over a stock model; Bodoni as body text.

### Floors that bind this poster
- Facts are exact: the Source above is the whole material. Add nothing, rename nothing, invent no names, prices, or credits.
- Contrast: reading text ≥ 4.5:1 against the ground it actually touches; large text (≥ 24px, or ≥ 18.7px bold) ≥ 3:1. The component pairs in the frontmatter are pre-verified pairings — set text in those pairings, or in the primary ink on the neutral or soft field.
- Reading text is live text, never baked into an image or drawn as paths; any drawn or turned lettering keeps a complete live-text equivalent on the poster.
- One unit, one lead, one primary form (Cover). Static work: no motion, no gradient, no shadow, no rounded corner unless this file explicitly says otherwise.
- Format: 900 × 1200 px (the HTML preview scale, 1px = 1px). Type sizes in the tokens are final sizes at that scale. Set the poster as one self-contained HTML file with inline CSS/SVG and no external assets.

### The signature card, in full (Cut-out)
**Construction.** A photograph's subject is cut from its ground and set
in front of or behind display type, so type and figure compose one
shape; the cut edge is clean at final size, and reading text never sits
on the figure. One cut-out per unit; the figure is the subject, not a
decoration.
**Parameters.** The figure crosses at least one type element or the
frame edge — a cut-out that touches nothing is a sticker; edge quality
checked at 100% (no halo, no fringe); text keeps its floors against
paper, not against the figure.
**Test.** Remove the type: the photograph loses its composition. Remove
the figure: the type loses its reason. Both must hurt.
**Caricature.** A product shot with a drop shadow floating over a
headline; clip-art silhouettes; a cut-out used because the photo was
boring.

## Colors
Black and white is the palette: deep ink #111111 on paper white, soft #F2EFE9 for the quiet field, secondary warm grey for apparatus. Tertiary #7A1F1F is the one cool-dark accent, used once, on the date line only. Focus is interface-only.

## Typography
Display in Didot/Bodoni with Songti SC for the Chinese title word; reading text and credits in Inter with Source Han Sans SC, small tracked capitals for place and date.

## Layout
Poster 900 × 1200. Centered axis allowed for the cover: masthead capitals at top, the Didot word at graphic scale across the middle, the figure (an SVG silhouette, atmosphere not evidence) crossing it, programme and credits in a quiet grotesque at the foot.

Composition, in numbers: masthead at top 52 — place in label capitals tracked 0.34em, centered; the date line below it in the tertiary, tracked 0.30em, carrying exactly 'SATURDAY 14 NOVEMBER 2026 · 19:30–22:00'. The lead is summoned, not coordinated (v0.5.3, from the name test): the word Grid in Didot at theatrical scale — the display token, 320px, or larger where the hand dares, cropped by the sheet's edge rather than seated politely inside the frame at reading size; it stands below the date line with clear air under the masthead. The figure is one ink silhouette in motion crossing the word, its bounding field roughly x250–880, y90–760 — a head above a single curved body falling diagonally — passing in front of the word's first letters and behind its last letter (the Cut-out signature); the split point and the body's curve are the hand's, decided at the sheet, not in this file. Predicates: one collision only, and everything else whispers. Ban: a word that fits is a word too small. 格网 is centered beneath the word in Songti at the title token, letter-spacing 0.5em. A hairline 56 × 1 in the line color, centered, stands 44px below 格网. The date line takes the label token. Below the hairline, the programme block stands centered in the body token (19px) at a declared local line-height of 2.0, in this order: the talks on one line with their times bold; the subtitle (EN · CN, as in the Source); the foyer and admission line. Credits close at bottom 34, at a declared local 12.5px in secondary, naming the figure an illustrative silhouette. The poster face is neutral white; the soft token is the surround outside the trim in preview.

## Do's and Don'ts
Dialect test: remove the word and the figure loses its composition; remove the figure and the word loses its reason — the crop is chosen so the gesture crosses the word's stem. Ruled out: fake luxury, gold gradients, a centered serif logo over a stock model, Bodoni as body text.

## Directions
| | Direction | Looks | Why it suits | Grid · faces · color · lead · methods |
|---|---|---|---|---|
| A | Mother tongue, by the book | Quiet white poster, one red accent, hairlines | Correct, and indistinguishable from any competent institute poster | 12-col · grotesque · ink + vermilion · scale contrast |
| B | Mother tongue, pushed | The title at graphic scale over a full accent field | Louder, but the material's own character is still unused | Same grid · same faces · accent field |
| C | Brodovitch | A Didot word cut by a figure in motion | The material does what this dialect is for | See Overview and Sequence |

Chosen: C — this set exists to test the dialects at full strength on held-still content; A and B remain written as the control.

## Sequence
Rhythm: a single unit; the rhythm map is the set's — nine posters read as one contact sheet, each a turn from the last, the mother tongue withheld so the dialects must carry the evening alone.

| Unit | Form | Register | Lead | Methods (master · work: imperative + parameters + ban) | Variation (name + magnitude + keep) or continuity (with its rhythm cost) |
|---|---|---|---|---|---|
| 1 | Cover | turn | The word GRID in Didot, cut by the figure's diagonal gesture | Brodovitch · Harper's Bazaar covers: set the display word at graphic scale and crop the figure so one gesture crosses it, apparatus in tracked capitals; never place the image beside the type as an illustration, never invent a credit | The unit is itself the set's variation: one dialect at full strength; keep condition — every fact from the Source section present and exact |

## Coverage
Text: title as the collision; the programme in grotesque at the foot, credits naming the figure as an illustrative silhouette. Image: one cut-out figure, atmosphere. Data: times as a single line of apparatus. Space: white as structure around the collision.

## Gaps
The programme is fictional and marked illustrative on the poster itself. No photography is used in this dialect render. Print proof: the HTML is the preview at poster scale; a press proof is unmade and would be checked before any real printing.

## Record
Folio version: 0.5.3. Template version: 6. Files read: SKILL.md, craft, Swiss theme, brodovitch dialect, poster surface, design-md template, signature.md. Date: 2026-10-31. Family master: none. Part of the dialects-master set; content source: examples/dialects-master/content.md.

## Overrides
Empty: no family master.
