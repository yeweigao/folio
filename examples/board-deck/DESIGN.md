---
version: alpha
name: Quarterly board report · Swiss Brutal
description: The quarter's numbers, shown as a working document whose structure is the design.
colors:
  primary: "#111111"
  secondary: "#625F59"
  tertiary: "#C83024"
  neutral: "#FFFFFF"
  soft: "#F4F2ED"
  line: "#C5C2BC"
  dark: "#141414"
  focus: "#005FCC"
typography:
  display: { fontFamily: "Inter, Source Han Sans SC, Noto Sans SC, sans-serif", fontSize: 120px, fontWeight: 700, lineHeight: 1 }
  title: { fontFamily: "Inter, Source Han Sans SC, Noto Sans SC, sans-serif", fontSize: 52px, fontWeight: 700, lineHeight: 1.12 }
  body: { fontFamily: "Inter, Source Han Sans SC, Noto Sans SC, sans-serif", fontSize: 20px, fontWeight: 400, lineHeight: 1.45 }
  label: { fontFamily: "Inter, Source Han Sans SC, Noto Sans SC, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.3 }
spacing:
  margin: 70px
  gutter: 24px
  column: 73px
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
A quarterly board report deck (slides, read alone at desk distance). Subject: the quarter's operating numbers and what they oblige next. Reader: board members, ten minutes, alone with the file. Theme: Swiss; dialect: Swiss Brutal — the material is a technical system whose structure is the content. All figures in this example are illustrative.
Governing hand: Make every unit as Müller-Brockmann made the Grid Systems plates: construct it on the twelve columns, let one element take graphic scale while the apparatus stays small and flush-left on one axis; never center a reading element, never round a corner, never let a figure float without its baseline, period, and change.
Signature programme: Exposed grid (Crouwel, signature card) — the twelve columns and master lines are drawn on every unit at 1px in the line color, only where a track carries content; squint test: text first, rules second.

## Colors
Primary ink #111111 carries all reading on paper and soft. Secondary #625F59 is muted apparatus only, never body text. Tertiary #C83024 is the hazard: it marks a real alert or the one figure that changed the plan, and carries paper text as a field in paper-on-accent. Neutral is the paper; soft #F4F2ED is the second working field for ledger bands (text-on-soft, muted-on-soft). Line #C5C2BC separates groups already legible; never text. Dark #141414 is the closing field (paper-on-dark). Focus #005FCC appears only as the focus-ring in interactive exports.

## Typography
One grotesque voice, Inter with Source Han Sans SC. Weight leads: display and title at 700, body at 400. Figures are tabular everywhere; the Kennzahl uses display at full frame width.

## Layout
Slides starting system kept: 1280 × 720, margins 70, twelve columns of 73 with 24 gutters, module 8. The grid is drawn, not implied: a mid-grey hairline opens each ledger and a heavier ink rule closes it. Zero radius, no shadows.

## Do's and Don'ts
Dialect test: every visible line is a real boundary and every band holds working content. Ruled out: KPI tiles, floating cards, gradients, a chart on a card with a legend.

## Directions
| | Direction | Looks | Why it suits | Grid · faces · color · lead · methods |
|---|---|---|---|---|
| A | Mother tongue, by the book | Quiet white pages, one red accent, hairlines | Safe, but reads as a standard report | 12-col · Inter/Source Han · ink + vermilion · scale contrast |
| B | Mother tongue, pushed | A full accent field at the key figure | The turn is felt, the rest stays polite | Same grid · same faces · accent field variation |
| C | Swiss Brutal | Visible grid rules, dense ledger rows, huge numerals | The subject is a system of numbers; structure is the content | Exposed grid · same faces · ink, hazard red only on alert · Ledger, Kennzahl |

Dialects set aside: Ulm (close, but this deck persuades, it does not instruct); ma (the material is dense, emptiness would hide it). Chosen: C, by the author, from the render of unit 3 (the dense chart page) in all three directions.

## Sequence
Rhythm, mapped before the details: cover establishes the grammar (base), the key figure turns it (turn), the evidence turns it again by scale (turn), the ledger holds (base), the close turns to dark (turn).

| Unit | Form | Register | Lead | Methods (master · work: imperative + parameters + ban) | Variation (name + magnitude + keep) or continuity (with its rhythm cost) |
|---|---|---|---|---|
| 1 | Cover | base | The quarter and its one verdict, set as a title | Müller-Brockmann · Der Film: set the verdict word at graphic scale across 10 of 12 columns at 700, the quarter and date at label size on the left axis; never a slogan in place of the title, never centered | Continuity — cost named: the cover must establish the grammar the later turns break; a break here would leave nothing to break from |
| 2 | Statement | turn | The Kennzahl: the one figure that changed the plan | Müller-Brockmann · Zurich Tonhalle posters: put the figure alone at display size on the full tertiary field, paper text, its baseline and period in label size beneath it; never a KPI tile, never a second figure on this unit | Accent field turn (tertiary field, paper-on-accent) |
| 3 | Argument | turn | The revenue chart, full-bleed to the slide edges | Tufte · data-ink: run the plot edge to edge with no frame, no legend, labels inside the plot at 16px or above, one axis only; never a chart on a card, never a dual axis | Variation: bleed — the exhibit is the evidence, framing it in white margins would demote it |
| 4 | Comparison | base | The cost ledger: value, baseline, period, change | Neurath & Arntz's ledger discipline via IBCS: tabular figures aligned on the decimal, one hairline opens the table and one ink rule closes it, rows at one module; never right-align figures on their last digit by eye, never color-code the change without a +/− sign | Continuity — cost named: a flat stretch in the middle, accepted because the ledger's sameness is what makes unit 5's dark field land |
| 5 | Close | turn | The one decision the board is asked to take | Müller-Brockmann · Grid Systems plates: the decision in one line at title size on the dark field (paper-on-dark), flush left, nothing else on the unit; never a 'thank you', never a new conclusion | Field turn to dark |

## Coverage
Text: hanging indent for apparatus, judgment titles. Image: none — this material has no honest photograph; type and data carry it. Data: Ledger, shared baseline, Kennzahl. Space and frame: exposed grid throughout, one bleed at unit 3, one accent field at unit 2, dark close at unit 5.

## Gaps
All figures are illustrative demo values, marked as such on their units. No photography is used; none was needed. Print proof not applicable (screen deck).

## Record
Folio version: 0.5.0. Template version: 5. Files read: SKILL.md, craft, Swiss theme, brutalist dialect, slides surface, design-md template. Date: 2026-10-31. Family master: none. Changes after the lock: 0.4.1 — Sequence citations rewritten as evocation bundles and a Governing hand line added, to demonstrate the invocation format. 0.4.2 — Sequence gains the Register column and a rhythm map; continuity rows name their rhythm cost. 0.5.0 — Signature programme line added (Exposed grid, to its card).

## Overrides
Empty: no family master.
