# Swiss Punk, Weingart · the slipped films

Separate films on one module grid (type, screen, accent), slipped and overprinted by declared amounts, every fact left flat and readable.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Swiss Punk, Wolfgang Weingart — the Kunsthalle Basel posters (1970s–): build each film separately, slip the films against the grid by declared amounts, overprint them, and render to see the slip; never a displacement that covers a fact.

World: any content, on any surface. Content of trust is tempered, not refused: the slip goes first, then rotation; the step and the overprint stay longest. Every piece keeps the grid, the films, the faces, ink and accent and the slip vector; each brings its words, the glyph its screen is made from, and its facts.

Method:
1. Compute the grid from the format.
2. Film 0, black: + marks at the gutter crossings, and the thread, a stepped line carrying the content's order, one step per item.
3. Film 1, screen: one glyph or word of the content as a dot screen from one raster, solid on one side, thinning to a 45% tone.
4. Film 2, accent: a copy of the display forms, slipped whole by one vector.
5. Film 3, black: live type; the display baseline steps down letter by letter at the derived step, a condensed light word over an extended black word; reading text flat.
6. Render, look at the slip, and change the declared values, never one element by hand.

Amplitude: full; tempered in the order above, the amplitude stated.

Anti-reference: grey Swiss minimum with one red square; a centred title over a stock image.

## Images

Computed: the dot screen from a glyph of the content, or from a real photograph of the subject screened at the same pitch. Never stock, a glitch filter or a distress texture.

## Layout

Grid system: Modular — six by nine in portrait, nine by six in landscape, six by six in a square.

S = min(W, H); margin 0.04 S; gutter 0.4 × margin; column c = (S − 2 × margin − 5 × gutter) ÷ 6; rows along the long side as many whole (c + gutter) as fit. The title and screen take the top four rows, the thread the next three, the facts the lower field, the declaration the bottom margin; landscape runs the same order left to right. The thread steps right by (columns ÷ items) and down one row per item, risers in the gutter. Screen pitch c ÷ 10, dot radius at most 0.72 pitch. The slip vector is derived from the step (Typography), never a constant: the accent film slips one full step, or half a step where a full step would land the copy on the next glyph; the amount used is declared with the piece. Facts are set from the bottom margin up; the space they leave belongs to the screen.

## Typography

- **Archivo** (OFL, variable width 62–125, weight 100–900): width and weight change inside one title, so registers collide within one voice.
- Display: the black word extended at 250, the light word condensed at 236, stepping by the derived step — one grid row divided by (the letters in the longest stepped word − 1), so the word's fall spans exactly one row; a word too wide narrows on the width axis first, then steps down in size.
- **Noto Sans SC** at the Latin's weight; the Chinese title upright in one vertical column, at 140.
- Facts 44 (800, figures 300); reading 26–32; nothing read below 26. Tabular figures; no tracked capitals.

## Colors

- **Ink `#0B0B0C` (primary).** Live type, thread, marks.
- **Muted `#4F555C` (secondary).** The second language.
- **Accent `#1560D6` (tertiary).** The slipped copies, multiplied; never reading text; under 10% of the area.
- **Ground `#ECEEEF` (neutral).** Cool newsprint, about 70% of the area.
- **Screen `#C3CCDA`.** The dot film; never under reading text.
- Overprint by multiply: over black it stays black; the slip shows as a blue fringe. Emphasis is weight, never colour.

## Shapes

Zero radius; no boxes, shadows or gradients. Thread 5; + marks 1.5 thick, 14 long; one registration target. The slip is a second flat ink overlapping its black form on both axes.

## Forms

- **Cover:** the light word over the stepped black word, the slipped copy, the screen, the thread, the facts flat.
- **Statement:** one line at display size, stepped by word.
- **Exhibit:** the screen across the field, from a glyph or a screened photograph.
- **Data:** the thread as the axis, one step per value, each figure flat and tabular; one value's glyph may become the screen.
- **Sequence and comparison:** the thread, one step per item, each item flush left under its riser; one form in two films offset by the difference, to scale and declared.
- **Reference and close:** flat type in the lower field; the declaration on the bottom margin.

## Variations

- **Accent field.** The whole unit on the accent, the screen in ground tone; once per series.
- **Rotation.** One display element at 90° from a grid intersection; never with the vertical Chinese title.

## Do's and Don'ts

- **Look before delivering:** render it, see it full size and as a thumbnail. A fact slipped, stepped or over the screen; a slip or step without its declared value: faults.
- **Floors:** facts verbatim and live; every pair in Tokens holds its contrast; no shadow or glow as a second ink.
- **Test:** the typographic relations themselves express the subject; remove one tilted word, and the system survives.
- **Caricature:** glitch filters, random distress, illegible stacks; one rotated word on an otherwise Swiss page; a drop shadow as a slip.

## Tokens

```yaml
colors:
  primary: "#0B0B0C"
  secondary: "#4F555C"
  tertiary: "#1560D6"
  neutral: "#ECEEEF"
  screen: "#C3CCDA"
typography:
  display: { fontFamily: "Archivo, Noto Sans SC, sans-serif", fontSize: 250, fontWeight: 900, lineHeight: 0.82 }
  display-light: { fontFamily: "Archivo, Noto Sans SC, sans-serif", fontSize: 236, fontWeight: 300, lineHeight: 0.82 }
  display-han: { fontFamily: "Noto Sans SC, Archivo, sans-serif", fontSize: 140, fontWeight: 900, lineHeight: 1 }
  fact: { fontFamily: "Archivo, Noto Sans SC, sans-serif", fontSize: 44, fontWeight: 800, lineHeight: 1.05 }
  body: { fontFamily: "Archivo, Noto Sans SC, sans-serif", fontSize: 30, fontWeight: 600, lineHeight: 1.12 }
spacing:
  margin: 40
  gutter: 16
  dot-pitch: 14
  thread: 5
pairs:
  ink-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.primary}" }
  muted-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.secondary}" }
  accent-on-ground-large: { backgroundColor: "{colors.neutral}", textColor: "{colors.tertiary}" }
  ink-on-screen: { backgroundColor: "{colors.screen}", textColor: "{colors.primary}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-03.
Pieces: the-grid/brief.md, made from the earlier, programme-bound version of this file; the system it shows is unchanged.
