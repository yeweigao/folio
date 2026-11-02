# ma 間, Kenya Hara · the white as vessel

The stock and one whole interval as the medium; a few lines of Song and quiet sans where the white is most felt; measures as equal intervals of white.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. Check the piece against Do's and Don'ts.

## Overview

Swiss, ma 間 — Kenya Hara's *White* (2008), the paper works and MUJI Horizon (2003): make the stock and the interval the medium, set a few lines where the white is most felt, and let equal intervals of white do the measuring; never draw a horizon, a stone, a paper grain or any object in code.

World: any content, on any surface. Dense content is translated, not refused: it gathers into one block so a single interval stays whole, and its measures become equal steps of white. Every piece keeps the stock, the ink, the whole interval, the axes and the faces; each brings its words, its measure and, when one exists, a real photograph.

Method:
1. Stock first: cool uncoated white, one graphite ink, one muted tone.
2. Keep one large interval whole: a field of at least four modules that nothing enters.
3. Ladder, not list: a measure becomes position, one module of white per step; equal steps are equal white.
4. Hang everything from three axes; set the type last.
5. With a real photograph of the subject, the photograph becomes the interval; without one, the interval and the type are the image.

Amplitude: reduced: few, wide size steps; movement only down the ladder.

Anti-reference: the template timetable (bold title, coloured band, equal cards); the Zen costume (stones, bamboo, brush ink, a rendered bowl on beige).

## Images

Photographed, or none. One real photograph of the object, material, light or place, edge to edge, no frame or scrim, its source and place in a small caption. Without one, nothing is drawn or generated in its place, and no placeholder is printed.

## Layout

Grid system: Modular — the field cut both ways into whole modules.

S = min(W, H); module M = S ÷ 14; columns and rows are the whole modules that fit; the margin is one module. Axes: L at module 1 (title, colophon), T at module 5 (figures and times), C from module 7 to the margin (everything else); nothing else aligns. The interval is the block between L and T, from the title to the colophon. A ladder entry's row is set by its value: first row + (value − first value) ÷ step. The colophon sits in the last quarter. Space is the interval or the ladder's measure; none is left over.

## Typography

- **Source Serif 4** (OFL) 300 with **Noto Serif SC** 300 (200 at display): display 88, titles 56.
- **Hanken Grotesk** (OFL) 400 with **Noto Sans SC** 400: body 30, labels and captions 22.
- Nothing read below 30 except labels and captions; quiet is not small. Flush left, ragged right; no tracking; tabular figures for every measure.

## Colors

- **Ground `#F3F4F2` (neutral).** The stock, at least 90% of the area.
- **Ink `#20242A` (primary).** Display, titles, every fact.
- **Muted `#5C626B` (secondary).** Figures, times, captions; never a fact alone.
- No accent; emphasis is position in the white, never colour.

## Shapes

None: no rules, boxes, dots, radius, shadow or grain. The grid is read in the white.

## Forms

- **Cover:** the title at L, the description at C, the interval whole, the colophon.
- **Statement:** one sentence at title size on C, where the white is most felt; everything else removed.
- **Exhibit:** one photograph edge to edge, the name small on its horizon line, the caption.
- **Data:** the ladder: each value's position set by its measure, its figure muted at T, its label at C on the same baseline.
- **Sequence and comparison:** the ladder in time, equal time as equal white; two ladders on one scale, sharing T.
- **Reference and close:** the colophon on L and C; one line of next action alone in the white.

## Variations

- **Horizon.** A real photograph fills the interval or the whole field; the title stays live, small on its horizon line.
- **Pause.** Title and colophon only; once per set, every fact appearing on another unit.

## Do's and Don'ts

- **Look before delivering:** render it, see it full size and as a thumbnail. A broken interval, a position placed by eye, type too small to read from where it will be seen: faults.
- **Floors:** facts verbatim and live; nothing drawn stands in for the real; every pair in Tokens holds its contrast.
- **Test:** the emptiness changes how the subject is felt, and the subject rewards the attention.
- **Caricature:** Zen props, stones, bamboo, brush ink; a computer-rendered bowl on beige; an empty page with nothing worth seeing.

## Tokens

```yaml
colors:
  primary: "#20242A"
  secondary: "#5C626B"
  neutral: "#F3F4F2"
typography:
  display: { fontFamily: "Source Serif 4, Noto Serif SC, serif", fontSize: 88, fontWeight: 300, lineHeight: 1 }
  title: { fontFamily: "Source Serif 4, Noto Serif SC, serif", fontSize: 56, fontWeight: 300, lineHeight: 1.1 }
  body: { fontFamily: "Hanken Grotesk, Noto Sans SC, sans-serif", fontSize: 30, fontWeight: 400, lineHeight: 1.4 }
  label: { fontFamily: "Hanken Grotesk, Noto Sans SC, sans-serif", fontSize: 22, fontWeight: 400, lineHeight: 1.45 }
spacing:
  module: 71.4
  margin: 71.4
pairs:
  ink-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.primary}" }
  muted-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.secondary}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-02.
Pieces: the-grid/brief.md, made from the earlier, programme-bound version of this file; the system it shows is unchanged.
