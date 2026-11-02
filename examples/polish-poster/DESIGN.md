---
version: alpha
name: The Grid · Polish Poster School, Tomaszewski
description: The Museum of Design's evening series on the systems behind modern design, one bilingual poster per evening, each with its own hand-made ironic picture over the same quiet block of live type.
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
  label: { fontFamily: "Bricolage Grotesque, Noto Sans SC, sans-serif", fontSize: 18, fontWeight: 600, lineHeight: 1.35 }
spacing:
  margin: 52
  gutter: 16
  column: 136
  baseline: 8
  group: 8
  peer: 16
  section: 32
  rule: 3
  hairline: 1
  band: 76
rounded:
  square: 0
components:
  ink-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.primary}" }
  muted-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.secondary}" }
  ink-on-accent: { backgroundColor: "{colors.tertiary}", textColor: "{colors.primary}" }
---

## Overview

Polish Poster School, Henryk Tomaszewski — the *Cyrk* and film posters (1947–): make one hand-made, ironic picture in gouache on a muted ground, and set every fact under it as live type flush left on the grid; never a ruled mechanical image, never a brush font standing in for a hand.

World: the evening series "The Grid" of the Museum of Design. Any A-series size, English and Chinese at equal status, any number of talks. A later evening changes picture, words and talk columns; ground, ink, accent, faces and construction stay.

Method:
1. One ironic image, as "the subject becomes the device"; reject the literal pictogram.
2. Gouache on the series ground: flat opaque shapes, visible brush edges, no gradients, shadows or lettering. Ink for ruling, accent for one figure. Scan real work, else generate naming master and medium, declared as illustration.
3. With neither, a labelled slot of the exact crop, reported. Never code, CSS shapes or stock.
4. Facts as live type on six tracks: what, when, where, who, how to come.

Amplitude: reduced. Live display title; picture shares the sheet with a full programme, since the street must get when and where in three seconds.

Anti-reference: cream sheet, black type, one red square; stock photograph; a code-drawn "hand".

## Colors

- **Ground `#CFD4C6`** (neutral). Cold grey-green board, at least half the sheet.
- **Ink `#16235C`** (primary). All first-reading type, every rule, ruling in the picture. 9.7:1 on ground, 8.0:1 on accent.
- **Muted `#454E63`** (secondary). Time headings and slot note only; 5.5:1 on ground; never on accent, never a line.
- **Accent `#F2B61C`** (tertiary). The picture's one figure and the foot band, under ten per cent. Never type or rule on ground; only ink on it.
- No other hue, no dark register.

## Typography

- **Display: Bricolage Grotesque** (OFL, variable). Title weight 800, width 75; title step width 86, weight 700; body width 100, weight 500; labels 600.
- **Han: Noto Sans SC** (OFL; 500, 700, 900), same stack. At display Han is 0.72 of Latin, lifted 0.1 em to share capital height and baseline; at the title step one size.
- **Ramp: 200 / 144 display, 32 title, 24 body, 18 label.** Size, then weight; no italic, no tracked capitals.
- Latin title in typed capitals, no tracking, never compressed.
- Break by meaning, `text-wrap: balance`. Chinese breaks at phrase boundaries, never on a closing mark, never starting ——; full-width punctuation. Curly quotes, en dashes. Tabular figures in times.

## Layout

Grid system: Hierarchical — zones sized by content weight on six shared tracks. Values at W = 1000, height 1.414 W, scaled by W / 1000.
- Margin 52, gutter 16, six columns of 136; column k starts at margin + k × (column + gutter). Pairs (288) hold peers, triples (440) two-script blocks. Baseline 8; all heights whole baselines.
- Zone 1, picture: 632 (45 %), full bleed top, left, right, ending on a 3 px ink rule.
- Zone 2, title: 32 below, height 184. Latin on columns 1–4, Han on 5–6, one baseline.
- Zone 3, descriptor: 16 under, one block per script, three columns each.
- Zone 4, facts: under a 3 px rule, date/time/doors left, place right, three columns each; under a 1 px hairline the programme in equal spans (two, three or six columns), each time, title, name.
- Zone 5, foot: under a 1 px hairline, exhibition line across six columns, disclosure on its own line, flush left; band 76 (5.4 %), full bleed.
- Content 16 under a rule, next rule 16 under content; zones 32 apart, blocks 8.
- A new format is recomposed, not scaled.

## Shapes

- Radius 0; no shadow, glow, card or plate.
- Ink rules: 3 px opens a table or closes the picture, 1 px separates peers; never grey.
- Fields: ground, picture, accent band.
- Code draws rules, band and type, never the picture.

## Components

- **Picture:** gouache after Tomaszewski, bleeding on three edges, no lettering; label under the rule, flush right, says "illustration". Ban: painted lettering, mixed hands, photograph.
- **Picture slot:** ground fill, exact crop, 24 px "Picture to supply: not yet made", 18 px note. Ban: hatching, drawn imitation.
- **Title:** display, ink, Latin and Han on one capital height. Ban: tracking, outline, colour, shadow.
- **Descriptor:** body, balanced, two lines at most. Ban: third language, slogan.
- **Date and place:** title step, ink; doors and foyer in body. Ban: pin, icon, label such as "When".
- **Programme:** time (title step, muted), talk (title step, ink), name (body, ink). Ban: numbering, bullets, boxes.
- **Foot line:** body, ink; disclosure beneath it, weight 800. Ban: split footer, middle dots.
- **Type band:** entry line in both scripts, title step weight 800, ink on accent, 76 high, centred. Ban: second band, button, arrow.

## Do's and Don'ts

1. **Do start from the sentence;** it fails if a rival subject fits.
2. **Do keep facts live and flush left,** once, in both scripts.
3. **Don't draw the hand in code.** A missing picture is a reported slot.
4. **Don't turn the accent into text.**
5. **Don't let a second hand in.** A visiting move is single and named in the brief.

Refused defaults: cream ground with one vermilion accent, a pictogram of the subject, small tracked capitals over numbered rows.

## Variations

- **Type band.** The sheet's one accent field; never more than one.
- **Figure across the rule.** The accent figure may cross the 3 px rule by at most 48 px, never touching live type; the crossing belongs to the supplied picture.

## Record

Folio version: 1.0.0. Template version: 13. Date: 2026-11-02.
Pieces: the-grid/brief.md.
