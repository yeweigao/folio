# Polish Poster School, Tomaszewski · the hand-made metaphor

One hand-made, ironic picture in gouache on a muted ground, with every fact beneath it as quiet live type on the tracks.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Polish Poster School, Henryk Tomaszewski — the film posters (1947–) and *Henry Moore* (1959): fuse two things the content joins into one ironic image, paint it in gouache on a muted ground, and set every fact under it as live type flush left on the grid; never a ruled mechanical image, never a brush font standing in for a hand.

World: any content, on any surface. Figures and abstractions are interpreted, not illustrated: what the content says becomes the picture, and the figures stand beneath it as type. Every piece keeps the ground, ink, accent, faces, the picture over the facts, and one hand; each brings its picture and its facts.

Method:
1. The sentence: "*the subject* becomes *the device*": two things the content joins, one form. It fails if a rival subject fits it, or if the picture would merely show the subject.
2. Paint it: gouache on the ground colour, flat and opaque, brush edges visible; ink draws, the accent goes to one figure. The accent is spent last, on the figure the subject itself gives; a metaphor invented to hold the accent is derivation running backwards, and a fault.
3. Material: scan real hand work; else generate the picture naming master and medium, declared as illustration; with neither, a labelled slot of the exact crop. Never code, CSS shapes, a brush font or stock.
4. Set the facts as live type on the tracks beneath.

Amplitude: reduced: the picture shares the format with the facts; full when it takes the whole unit.

Anti-reference: a cream sheet with one red square; a stock photograph; a code-drawn "hand"; the literal pictogram.

## Images

Hand-made, one picture per unit, one artist's hand: Tomaszewski's by default. Drawn lettering may join the picture only when the same words stand as live type. A visiting hand is named and used alone: Lenica's swelling line, Trepkowski's silhouette, Cieślewicz's photomontage. A generated picture is declared; nothing poses as documentary proof.

## Layout

Grid system: Hierarchical — zones sized by content weight on shared tracks.

S = min(W, H); margin 0.052 S; gutter 0.016 S; six tracks, twelve where W > 1.4 H; baseline 0.008 S, every height whole baselines. The picture bleeds on three sides and ends on a 3 ink rule: at least the top 45% of a portrait, half a square, the left 55% of a landscape. Beneath it, in order: the title (first language on four tracks, second on two, one baseline), a short description, the facts under a 3 rule, peers under 1 hairlines in equal spans. The facts are set from the bottom margin up; space they do not need goes to the picture.

## Typography

- **Bricolage Grotesque** (OFL, variable): display 800 at width 75, at 200; titles 700 at width 86, at 32; body 500 at 24.
- **Noto Sans SC** 500–900: beside Latin, display at 0.72 of it, sharing cap height and baseline; alone, at 144.
- Latin titles in typed capitals, never tracked or compressed. Size first, then weight; tabular figures. Nothing read below 24.

## Colors

- **Ground `#CFD4C6` (neutral).** Cold grey-green board, the picture's ground, at least half the area.
- **Ink `#16235C` (primary).** All type, every rule, the drawing.
- **Muted `#454E63` (secondary).** Secondary headings and notes.
- **Accent `#F2B61C` (tertiary).** The picture's one figure and one band, under 10%; never type, only ink on it. The role is fixed; the hue is the world's gold unless the subject carries a colour it cannot deny — blood is red — in which case the hue follows the subject, the role is unchanged, and the deviation is declared on the piece.
- Emphasis is weight, never colour.

## Shapes

Radius 0; no shadow, card or plate. Ink rules: 3 closes the picture or opens the facts, 1 separates peers. Code draws rules, band and type, never the picture.

## Forms

- **Cover:** the picture, the title, the essential facts.
- **Statement:** the picture with one sentence beneath at title size.
- **Exhibit:** the picture across the whole unit, its credit under the rule.
- **Data:** the picture says what the figures mean; beneath, rows on the tracks, tabular, the value at the row's end. No chart inside the picture.
- **Sequence and comparison:** one picture per step at one crop and one hand; one picture holding both sides of a comparison, the facts in two blocks beneath.
- **Reference and close:** facts only, under rules; the next action on the accent band.

## Variations

- **Full picture** (Trepkowski, *Nie!*). The picture takes the whole unit, near-wordless; the facts move to the band. Once per series.
- **Figure across the rule.** The accent figure crosses the closing rule by up to six baselines, never touching type.

## Do's and Don'ts

- **Look before delivering:** render it, see it full size and as a thumbnail. Two hands, a fact painted rather than set, a drawn title without its live twin, the accent on a second figure: faults.
- **Floors:** facts verbatim and live; a generated picture declared; every pair in Tokens holds its contrast.
- **Test:** the picture says something about this subject that a photograph of it could not, and says it once.
- **Caricature:** a brush font, distressed paper, and a surreal object unrelated to the subject.

## Tokens

```yaml
colors:
  primary: "#16235C"
  secondary: "#454E63"
  tertiary: "#F2B61C"
  neutral: "#CFD4C6"
typography:
  display: { fontFamily: "Bricolage Grotesque, Noto Sans SC, sans-serif", fontSize: 200, fontWeight: 800, lineHeight: 0.92 }
  display-han: { fontFamily: "Noto Sans SC, Bricolage Grotesque, sans-serif", fontSize: 144, fontWeight: 900, lineHeight: 0.92 }
  title: { fontFamily: "Bricolage Grotesque, Noto Sans SC, sans-serif", fontSize: 32, fontWeight: 700, lineHeight: 1.15 }
  body: { fontFamily: "Bricolage Grotesque, Noto Sans SC, sans-serif", fontSize: 24, fontWeight: 500, lineHeight: 1.4 }
spacing:
  margin: 52
  gutter: 16
  baseline: 8
  rule: 3
  hairline: 1
pairs:
  ink-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.primary}" }
  muted-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.secondary}" }
  ink-on-accent: { backgroundColor: "{colors.tertiary}", textColor: "{colors.primary}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-03.
Pieces: the-grid/brief.md, made from the earlier, programme-bound version of this file; the system it shows is unchanged.
