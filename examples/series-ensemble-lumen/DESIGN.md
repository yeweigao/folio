# Ensemble Lumen concert posters · Swiss, Müller-Brockmann (musica viva) with Gerstner's programme

A series of one-sheet concert posters in which each evening's lead image is a field computed from the cyclic structure of one work on the programme, set on a modular grid, in black, paper and one cobalt.

## Overview

Swiss, Müller-Brockmann (Tonhalle *musica viva*): compute the grid from the format, build the lead image from the music's own structure in the grid's modules, set type flush left in four sizes; never draw a clock, metronome, note or stave-as-ornament.
World: one ensemble, one sheet per evening, read in passing at three metres; evening facts live in its brief.
Method: (1) Take the work whose score is a rule; state it in the brief as (row, track) → filled or empty. (2) Compute one rect per cell in code. (3) Each row is two half-cell staves: upper the fixed reference, lower the moving voice; both sounding join into a full cell. (4) Colour one traced element cobalt through every row. (5) One-line caption under the field. (6) Title, two-track fact block, price and address on one baseline.
Amplitude: full. Field the largest black mass, title second.
Anti-reference: clock face, metronome, concentric rings, cream-and-vermilion cultural poster.

## Images

Computed. The lead field is generated in code from the cyclic structure of one work on the programme (Method); no drawn instrument, note or clock.

## Layout

Grid system: modular, 12 tracks by 12 rows.
Values at S = 1000 (S, the format's short side), scaled by S ÷ 1000; the module is recomputed from the work's pulses as below, never scaled.
Margin 60, gutter 8, module 74, cell 66, stave 33. Field square, flush to top trim (3 mm bleed). A work with n pulses uses n tracks and rows, n ≤ 16, module = (measure + gutter) / n. Text zone at least 34% of height. Hanging block: seven tracks who, when, where; five programme; one first baseline; price and address on one baseline, bottom margin 60. Flush left, nothing centred.

## Typography

Host Grotesk (OFL); fallback system sans. Display 161 px / 800, tracking -0.04em, the evening title on one line, a cap: a longer title takes the largest whole px that fits, tracking unchanged, size in its brief. Title 36 / 700 for who, when, where. Body 21 / 400 programme, composers 700. Label 16 / 500 caption. Price and address body 700. A2, 1 px = 0.42 mm. Hand-broken lines; work numbers no-break; quotes and diacritics as supplied.

## Colors

Primary #111111 ink: field, title, facts. Neutral #F3F3F1 off-white stock. Tertiary #3A4BFF cobalt: the traced element only, never text or ground. Accent at most 5%, paper at least 55% on the standard sheet; the premiere sheet keeps its own shares (Variations). No greys, tints.

## Shapes

Rectangles, radius 0; no outline, shadow, gradient, texture, rule. One gutter between cells and rows. The traced element is a full stave cell.

## Forms

Field: one SVG, one rect per sounding cell, script-generated. Ban: a cell the rule does not produce.
Caption: label size, one line, counts only in words. Ban: marketing.
Title: display size, one line. Ban: tracking changed to fit.
Fact block: title size, one fact per line: who, date, time, place. Ban: icons, labels.
Programme: body size, composer bold, blank line between works. Ban: numbering, bullets.
Footer: body bold. Ban: button, decorative QR.

## Variations

Accent field: sheet cobalt, ink and paper in front; premieres only; field still computed. On this sheet the standard caps do not apply: cobalt is the ground, uncapped; the field's cells and every word are paper, the traced element ink, and both pairs hold their contrast.
Type-only evening: no computable work; title three times at display size, offset one module each, copies cropped by the trim. One break per sheet.

## Do's and Don'ts

- Do compute the field from a rule any reader can check against the score.
- Do keep one lead: field, title, then the rest.
- Do trace exactly one element in cobalt.
- Don't draw the subject's pictogram.
- Don't add a second colour, tint, frame or centred block.

## Tokens

```yaml
colors:
  primary: "#111111"
  neutral: "#F3F3F1"
  tertiary: "#3A4BFF"
typography:
  display: { fontFamily: "Host Grotesk, sans-serif", fontSize: 161, fontWeight: 800, lineHeight: 0.9 }
  title: { fontFamily: "Host Grotesk, sans-serif", fontSize: 36, fontWeight: 700, lineHeight: 1.16 }
  body: { fontFamily: "Host Grotesk, sans-serif", fontSize: 21, fontWeight: 400, lineHeight: 1.26 }
  label: { fontFamily: "Host Grotesk, sans-serif", fontSize: 16, fontWeight: 500, lineHeight: 1.3 }
spacing:
  margin: 60
  gutter: 8
  cell: 66
  module: 74
  stave: 33
rounded:
  none: 0
pairs:
  ink-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.primary}" }
  accent-on-ground-large: { backgroundColor: "{colors.neutral}", textColor: "{colors.tertiary}" }
  accent-on-ink-large: { backgroundColor: "{colors.primary}", textColor: "{colors.tertiary}" }
```

## Record

Folio version: 1.0.0. Template version: 14. Date: 2026-11-02.
Pieces: three-clocks/brief.md and bells-and-silence/brief.md.
Changes after the lock: Typography, display 161 px became a cap; a 17-character title sets at 125 px.
Template 13 → 14 on 2026-11-02: sections reordered method first, Images condensed from the existing text, tokens moved to the end; nothing else changed.
