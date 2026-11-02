# Bauhaus, Joost Schmidt · the constructed figure

A figure of the content built from circle, square and bar on one module, in red, blue, yellow and black, with every line of type hung from the same construction.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. Check the piece against Do's and Don'ts.

## Overview

Bauhaus, Joost Schmidt — the 1923 Bauhaus exhibition poster: draw the content's figure with compass and square from circle, square and bar on one module, in red, blue, yellow and black, then set every line of type into the same construction; never shapes that build nothing.

World: any content, on any surface. Its leading parts (three at most) become shapes, its order or measure becomes the black thread they hang from, their weights set sizes on the doubling scale. Every piece keeps the module, the primaries, the thread, the faces and the construction; each brings its parts, its order and its figure.

Method:
1. Find the parts, their order, and the axis that orders them (time, a process, a rank, a quantity).
2. Lay the axis as one black thread; hang each part from it by a drop at its position.
3. Draw each part with compass, square and rule: square, circle, bar, in that order, sized by weight on the doubling scale.
4. Where two primaries cross, the overlap is ink.
5. Hang the type from the same drops.

A fourth term (time, sound, a sequence) takes the line, never a fourth hue. Kandinsky visits once: form and colour go to parts by place in the order, never by meaning.

Amplitude: full: three primaries and black, flat, type at graphic scale.

Anti-reference: the triad recited as pattern; pastel or teal primaries; shapes off the module; the subject's literal pictogram.

## Images

Computed: the figure drawn from the module. Moholy-Nagy may visit once: one real photograph in black and white, cut to a rectangle or circle on the module, in tension with a bar. Never an illustration.

## Layout

Grid system: Modular — one square module; every edge on its lines.

S = min(W, H); margin S ÷ 20; twelve columns without gutters, sixteen where W > 1.4 H; module = column width; rows = whole modules that fit. The thread lies on a row line about a third down (at mid-height in landscape); the shapes hang from the row three below it; the masthead sits above, the ledger below, one row per fact. Sizes double (1, 2, 4, 8 modules); every edge, centre and drop lands on a module line. Rows nobody needs gather into one band of ink at the foot, never between the parts of the figure.

## Typography

- **League Spartan** (OFL; 500, 700), whose round letters echo the circle; **Noto Sans SC** (500, 700) for Chinese.
- Display at a cap height of two modules, broken by meaning into lines that fit, never tracked or stretched; the Chinese display at the same ink height.
- Title 36 / 700, name 36 / 500, body and label 26; Chinese body 24. Nothing read smaller.
- Two weights, lining figures; no italic, outline or letterspacing. Latin may run lowercase, after Bayer.

## Colors

- **Ink `#111111` (primary).** Thread, drops, overlaps, rules, the foot band, everything read.
- **Muted `#4A4A46` (secondary).** Secondary text.
- **Ground `#F4F4F0` (neutral).** Paper white, over half the area.
- **Red `#D7281E`, blue `#1D3E9E`, yellow `#F3B900`.** First, second and last part, in that order; never type. Yellow always carries an ink keyline and never touches red.
- **Line `#8A8A83`.** The grid, where it is shown.
- Primaries mark place in the order, never value or emphasis.

## Shapes

Flat, hard-edged, zero radius. Square; circle (at least four modules across); bar (one module thick, four long); a fourth part restarts at the square, one doubling larger. Each shape's left edge sits on its part's column line. Thread 6 ink at 0° or 90°, each drop ending on a corner or the circle's leftmost point. Keyline 3 ink. Ledger rules 2 ink to open, 1 between rows.

## Forms

- **Cover:** masthead, the figure, the ledger.
- **Statement:** one sentence at title size hung from the thread, one shape as its counterweight.
- **Exhibit:** one shape at eight modules, or one photograph cut on the module, its label on a drop.
- **Data:** values as shapes of one kind along the thread; the doubling scale shows magnitude, the ledger the exact figure.
- **Sequence and comparison:** the thread in order, one drop per step; two figures on one thread at one scale.
- **Reference and close:** the ledger; the next action on the foot band.

## Variations

- **Vertical Chinese.** The Chinese display in a column two modules wide; once per series.
- **Typophoto** (Moholy-Nagy). One photograph in diagonal tension with one bar; once per deliverable.

## Do's and Don'ts

- **Look before delivering:** render it, see it full size and as a thumbnail. A shape off the module, type on a primary, a figure that would fit another subject: faults.
- **Floors:** facts verbatim and live; every pair in Tokens holds its contrast.
- **Test:** remove the type, and the shapes still build this content's figure, not any content's.
- **Caricature:** the Kandinsky triad on any subject; shapes scattered off the grid; pastel "Bauhaus"; gradients, shadows, rounded cards.

## Tokens

```yaml
colors:
  primary: "#111111"
  secondary: "#4A4A46"
  neutral: "#F4F4F0"
  red: "#D7281E"
  blue: "#1D3E9E"
  yellow: "#F3B900"
  line: "#8A8A83"
typography:
  display: { fontFamily: "League Spartan, Noto Sans SC, sans-serif", fontSize: 224, fontWeight: 700, lineHeight: 0.9 }
  display-zh: { fontFamily: "Noto Sans SC, League Spartan, sans-serif", fontSize: 158, fontWeight: 700, lineHeight: 0.9 }
  title: { fontFamily: "League Spartan, Noto Sans SC, sans-serif", fontSize: 36, fontWeight: 700, lineHeight: 1.1 }
  name: { fontFamily: "League Spartan, Noto Sans SC, sans-serif", fontSize: 36, fontWeight: 500, lineHeight: 1.1 }
  body: { fontFamily: "League Spartan, Noto Sans SC, sans-serif", fontSize: 26, fontWeight: 500, lineHeight: 1.3 }
  body-zh: { fontFamily: "Noto Sans SC, League Spartan, sans-serif", fontSize: 24, fontWeight: 500, lineHeight: 1.4 }
spacing:
  module: 75
  margin: 50
  thread: 6
  keyline: 3
pairs:
  ink-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.primary}" }
  muted-on-ground: { backgroundColor: "{colors.neutral}", textColor: "{colors.secondary}" }
  ground-on-ink: { backgroundColor: "{colors.primary}", textColor: "{colors.neutral}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-02.
Pieces: the-grid/brief.md, made from the earlier, programme-bound version of this file; the system it shows is unchanged.
