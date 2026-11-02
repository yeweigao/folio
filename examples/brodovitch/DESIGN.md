# Swiss, Brodovitch · the Bazaar cover

One photograph of the subject in motion and one Didone word, cut by the same edge, over a quiet Swiss page.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. Check the piece against Do's and Don'ts.

## Overview

Swiss, in Alexey Brodovitch's hand of the *Harper's Bazaar* covers and *Ballet* (1934–58) — crop one photograph of the subject in motion to a single gesture, then set one Didone word across the crop's edge at the scale of the figure, so the line that cuts the picture cuts the word; never a stock figure under a centred serif, never gold, never a script face.

World: any content, on any surface. A subject with no body to photograph is translated: photograph its trace (the object, the hand, the place), or let its strongest form, a number's fall or one word, become the figure. Every piece keeps the cut, the Didone word, the quiet page, ink and paper; each brings its photograph, its word and its facts.

Method:
1. The figure: the subject in motion, cropped on the contact sheet until one gesture remains.
2. The word: the subject's name or its one strongest noun; never a slogan.
3. The cut: one edge through the figure's weight and through the word, paper type above it, ink below.
4. The page: Swiss beneath the edge; quiet, so the cut stays loud.
5. In a sequence, pace it like film: a loud unit, then a quiet one.

Amplitude: full above the edge, reduced below.

Anti-reference: a centred serif over a stock model; gold, glass, script; Didone body text.

## Images

A real photograph, credited, never invented; motion blur kept; it may dissolve at one edge. Until it exists, the plate is ink marked "FPO". A number as the figure is the picture, not a headline: its digits in the grotesque, paper on ink, cap height near the plate's height, bleeding off at least two edges and cropped like a photograph; the word and the lockup are set over it. Nothing drawn, rendered or generated poses as a photograph; no chart on the plate.

## Layout

Grid system: Column — tracks under one division of the format into a plate and a page.

S = min(W, H); unit u = S ÷ 72; margin 4u; gutter u; six tracks, twelve where W > 1.4 H. The plate bleeds on three sides; its edge lies on a whole u, a third to two fifths down a portrait, near half a square, 0.5–0.6 across a landscape (a vertical edge). The word spans the margins, and the edge crosses it between 40% and 60% of its height. The page is set from the bottom margin up, so the space it does not need opens under the word and the cut breathes; groups 2u to 4u apart. On the page, the first language and figures hang on track 0, the second language on track 3; one fact, one row.

## Typography

- **The word** fills its span: Latin in Bodoni Moda 800, Chinese in Noto Serif SC 900 at span ÷ characters. One live text element, filled with a hard stop at the edge. If it falls below 0.2 S, choose a shorter word.
- **The lockup** sits 2u above the word, at a third of the word's size and never wider than half its span: the name in the other language, Latin in Bodoni Moda italic, Chinese in Noto Serif SC.
- **Titles** 46: Bodoni Moda 700, Chinese in Noto Serif SC 700.
- **Everything read:** Hanken Grotesk with Noto Sans SC 500, 30 on 42; credits 15. Nothing read below 30.
- Latin and Chinese as one voice: same size, same track. Tabular figures in data.

## Colors

- **Ink `#0B0B0C` (primary).** The plate, the word below the edge, everything read.
- **Paper `#F6F7F7` (neutral).** Cold white, never cream; the word above the edge, credits on the plate.
- **Muted `#55585C` (secondary).** Secondary facts on paper.
- Emphasis is weight or position, never colour.

## Shapes

No radius, shadow, border or card. At most two 2 ink rules organize the page; rules drawn to scale in data are measures, not organization.

## Forms

- **Cover:** the plate, the word on its edge, the lockup; the page beneath carries the facts or one other form.
- **Statement:** one sentence in Bodoni Moda italic, flush left, no plate.
- **Exhibit:** the plate alone, credited.
- **Data:** the title as the content gives it, then rows at reading size, each at most four tracks long with its value at the row's end; a 2 ink rule per row drawn to scale where the difference must be seen; the key row in 700.
- **Sequence and comparison:** frames at one crop scale in order, as in *Ballet*, one word crossing them.
- **Reference and close:** the page alone, rows on the tracks.

## Variations

- **Symmetric axis.** On a cover only, word and lockup centred; once per series.
- **Sequence strip.** Equal frames of one movement, blur kept, the word across them; once per deliverable.

## Do's and Don'ts

- **Look before delivering:** render the piece and see it at full size and as a thumbnail; space nobody placed and two things leading are faults.
- **Floors:** facts verbatim and live; credits never invented; every pair in Tokens holds its contrast.
- **Test:** remove the type and the crop loses its composition; remove the photograph and the type loses its edge.
- **Caricature:** fake luxury: gold, rose gold, glass, script, a centred serif logo over a stock model.

## Tokens

```yaml
colors:
  primary: "#0B0B0C"
  secondary: "#55585C"
  neutral: "#F6F7F7"
typography:
  word: { fontFamily: "Bodoni Moda, Noto Serif SC, serif", fontSize: 336, fontWeight: 800, lineHeight: 1 }
  lockup: { fontFamily: "Bodoni Moda, Noto Serif SC, serif", fontSize: 112, fontWeight: 400, lineHeight: 1 }
  title: { fontFamily: "Bodoni Moda, Noto Serif SC, serif", fontSize: 46, fontWeight: 700, lineHeight: 1.22 }
  body: { fontFamily: "Hanken Grotesk, Noto Sans SC, sans-serif", fontSize: 30, fontWeight: 500, lineHeight: 1.4 }
  credit: { fontFamily: "Hanken Grotesk, Noto Sans SC, sans-serif", fontSize: 15, fontWeight: 400, lineHeight: 1.4 }
spacing:
  unit: 14
  margin: 56
  rule: 2
pairs:
  ink-on-paper: { backgroundColor: "{colors.neutral}", textColor: "{colors.primary}" }
  muted-on-paper: { backgroundColor: "{colors.neutral}", textColor: "{colors.secondary}" }
  paper-on-ink: { backgroundColor: "{colors.primary}", textColor: "{colors.neutral}" }
```

Word and lockup are shown for a six-letter Latin word; Typography derives them for any other.

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-02.
Pieces: the-grid/brief.md, made from the earlier, programme-bound version of this file; the system it shows is unchanged.
