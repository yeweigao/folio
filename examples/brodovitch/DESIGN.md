# Brodovitch · the house editorial

Photographs in black and white, one saturated colour that is the subject's own, a serif that speaks and a grotesque that labels, the figure cut against the word.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. Check the piece against Do's and Don'ts.

## Overview

Brodovitch and the fashion houses after him — the *Harper's Bazaar* covers (1934–58) and today's campaign books: make one photograph series in black and white, find the one colour that is the subject's own, and give each unit one collision of figure and word; never a borrowed house's marks, never template chrome.

World: any content, on any surface: decks, campaign books, covers, pages. Photographs show people, objects or places, whatever the subject is; a number becomes a giant serif numeral cropped in a panel. Every piece keeps the black-and-white photography, the one colour, the two voices and the grid; each brings its photographs, its colour and its words.

Method:
1. The colour: the subject's own (its material, its place, its mark), one saturated hue; never another house's.
2. The series: photographs in black and white, each cropped to one gesture, one crop scale across the series.
3. The collision, one per loud unit: the figure in front of the word; the crop's edge through the word; a giant numeral cropped in a panel; a letter as the photograph's window.
4. The page: between loud units, white and quiet, Swiss on the tracks.
5. The pace: a loud unit, then a quiet one, like film.

Amplitude: full on loud units, reduced on quiet ones.

Anti-reference: fake luxury; a borrowed house's logo, monogram or colour; rounded cards, pill buttons, checkmarks, arrows, KPI tiles.

## Images

Real photographs, black and white, credited; motion blur kept; until one exists, a grey panel marked "FPO". A duotone is the photograph multiplied with the one colour, declared. A cut-out figure is cut from a real photograph, never drawn or generated. No generated person poses as a real one; no chart on a photograph.

## Layout

Grid system: Column — whole tracks; panels are whole tracks and whole u.

S = min(W, H); unit u = S ÷ 72; margin 4u; gutter u; twelve tracks where W > 1.4 H, six otherwise. A unit is a colour field, an ink field or paper, never a mix of grounds without an edge between. Panels sit on tracks with zero radius. On a cover, the plate's edge lies on a whole u where the photograph's gesture falls, and the word spans the margins. A page is set from the bottom margin up; the space it does not need opens where the collision is.

## Typography

- **Instrument Serif** (OFL), a sharp serif of moderate contrast, speaks: headlines in sentence case at 46 to 64; the one word or numeral derived to fill its span or its panel's height: a Latin word fills the span, a Chinese word sets at span ÷ characters, a numeral at the panel's height. Chinese in Noto Serif SC. **Bodoni Moda** (OFL), the Didone, only for the Bazaar cut's word.
- **Hanken Grotesk** (OFL) labels: small capitals at 18, a bold lead word and regular rest in one label; reading text 500 at 30. Chinese in Noto Sans SC.
- Two voices, nothing between. Nothing read below 30, except labels at 18 that are never sentences.
- Proportional serif numerals; tabular figures in rows of data.

## Colors

- **Ink `#1C1C1C` (primary).** Ink fields, type on paper.
- **Paper `#FFFFFF` (neutral).** Pages and type on ink and colour.
- **Grey `#5E5E5E` (secondary).** Secondary lines on paper.
- **The subject's colour (tertiary), shown as `#1F2BB8`.** A field, a duotone, a knockout, one panel; never text on paper. The value stands in until the subject's own is found; it is no house's colour.
- Emphasis is the colour field or scale, never a second hue.

## Shapes

Zero radius; no shadow, outline, pill or card. Hairlines 1 where a page needs an edge. No arrows, checkmarks or icons.

## Forms

- **Cover,** one of two. The Bazaar cut: a plate bleeding on three sides, its edge where the gesture falls, the word across the edge between 40% and 60% of its height, paper on the plate and ink on the page. Or the figure in front: a full-bleed photograph, the word across it at full width, the figure cut out in front of the word. Labels in small capitals at two corners.
- **Statement:** one sentence in the serif, sentence case, flush left, on the colour field or on paper.
- **Exhibit:** one photograph in a panel of whole tracks, credited; or the letter as its window.
- **Section:** the section's numeral in the serif at twice headline size, its title in small capitals beside it on the same cap line, a few lines beneath; one column of whole tracks holds a photograph in duotone.
- **Gallery:** a wall of photographs on whole tracks and rows, gutters of u, crops varied in scale but each to one gesture; one panel among them in the colour or in ink carries a label and one line. A word may run across the wall's top at full width.
- **Data:** each number a giant serif numeral cropped in its own panel, a label in small capitals and one line beneath; or a row of numerals at twice headline size, each under its label, over a gallery that runs off the edge.
- **Sequence and comparison:** a photograph series at one crop scale in a row of panels; the same crop for things compared.
- **Reference and close:** grotesque rows on the tracks; the close, one word on the colour field.

## Variations

- **Stepped mask.** The colour field cut in whole-track steps across one photograph; once per deliverable.
- **Pattern letter.** A giant letter filled with a pattern drawn from the subject's own mark; never a borrowed monogram.

## Do's and Don'ts

- **Look before delivering:** render it, see it full size and as a thumbnail. Rounded cards, pills, arrows, checkmarks, KPI tiles, grey text too small to read, two loud units in a row, a borrowed mark: faults.
- **Floors:** facts verbatim and live; credits never invented; no generated person posing as real; every pair in Tokens holds its contrast.
- **Test:** remove the colour, and the series still reads as one house; remove the photographs, and the type loses its reason.
- **Caricature:** fake luxury, gold, glass, script; a borrowed house's logo, monogram or colour; template chrome.

## Tokens

```yaml
colors:
  primary: "#1C1C1C"
  secondary: "#5E5E5E"
  tertiary: "#1F2BB8"
  neutral: "#FFFFFF"
typography:
  word: { fontFamily: "Instrument Serif, Noto Serif SC, serif", fontSize: 336, fontWeight: 400, lineHeight: 0.9 }
  cut: { fontFamily: "Bodoni Moda, Noto Serif SC, serif", fontSize: 336, fontWeight: 500, lineHeight: 0.9 }
  headline: { fontFamily: "Instrument Serif, Noto Serif SC, serif", fontSize: 56, fontWeight: 400, lineHeight: 1.12 }
  body: { fontFamily: "Hanken Grotesk, Noto Sans SC, sans-serif", fontSize: 30, fontWeight: 500, lineHeight: 1.4 }
  label: { fontFamily: "Hanken Grotesk, Noto Sans SC, sans-serif", fontSize: 18, fontWeight: 700, lineHeight: 1.2 }
spacing:
  unit: 14
  margin: 56
  gutter: 14
pairs:
  ink-on-paper: { backgroundColor: "{colors.neutral}", textColor: "{colors.primary}" }
  grey-on-paper: { backgroundColor: "{colors.neutral}", textColor: "{colors.secondary}" }
  paper-on-ink: { backgroundColor: "{colors.primary}", textColor: "{colors.neutral}" }
  paper-on-colour: { backgroundColor: "{colors.tertiary}", textColor: "{colors.neutral}" }
```

The word is shown for a six-letter Latin word; Typography derives it for any other.

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-03.
Pieces: the-grid/, ballet/, nighttrain/, portfolio/, made from an earlier version of this file (the Bazaar cut alone); they show its cover, not the house editorial.
