# Highland · Apple + Burberry

A British outerwear house in Apple + Burberry: one coat, a low horizon, the weather above it.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are px at S = 1000, S the format's short side, and scale with it; each is a floor for how far the format is read from, never a ceiling. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath; form names are the maker's, never set on the page. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Burberry style — Set every unit on one low horizon with the weather above it and the coat standing on it; never the check as wallpaper, never a range with no single coat.

World: Highland's coats, collections, campaigns and stories, on any surface. Every piece keeps the horizon, the weather tone above it and the serif; each brings its coat or detail and its day's weather.

Method:
1. Choose the one coat or detail and the weather it stands in.
2. Draw the horizon low; give the sky the weather's tone.
3. Stand the coat on the horizon; the claim sits in the sky.
4. Price stays below the line, quiet.

Amplitude: Full on covers and campaign units; reduced in the shop and reference.

Anti-reference: Fake heritage: a check pattern everywhere, a crest, gold.

## Images

Renders of fictional coats with modelled cloth — key light, gabardine twill, a contact shadow on the ground — and illustrated weather fields, declared once. On a cover the coat stands half the frame tall or more, on the horizon.

## Layout

Grid system: Horizon field — every unit split by one low line, sky above, ground below.

Twelve tracks from W × H: margin max(5% W, 6% S), gutter 1.25% W, an 8 px module. The horizon sits at 64% of the height; type above it reads on the sky, the shop's rows below it on ground. Formats: on a 1600 × 900 slide, critical content stays inside the central 84%, the slide title at least 90 px and body at least 33; a scrolling page reads the tokens as given at a 1440 px viewport, body never below 17 px; a shop subdivides the field into peer cards on hairlines.

## Typography

- Cormorant Garamond for display and heading; Inter for lead, body and labels; Noto Serif SC and Noto Sans SC for Chinese.
- Display 72 / 400; heading 52 / 400; lead 28 / 300; body 17 / 400; product 21 / 600; price 17 / 400; label 14; caption 12.

## Colors

Ground: white, with the trench's own honey as the warm panel.
- **canvas** white; **panel** `#f7f4ed` honey; **dark** `#202124` a night unit.
- **weather** `#343941` storm sky, **cloth** `#e5e0d7` the gabardine, **trim** `#8f8c85` the horizon line and seams.
- **ink** `#202124`, **muted** `#626269`; **onDark** white, **mutedDark** `#c4c6c9` on dark.
- **action**, **link** and **focus** `#1936c8` the knight blue, replacing Apple blue; **darkLink** `#a8b8ff`; **onAction** white.
- **hairline** `#d2d2d7` in rows below the horizon.

## Shapes

**The device: the horizon.** One full-width line in trim, 1 px at S = 1000, at 64% of the unit's height. Above it the sky in one weather tone — white, honey, storm — below it the ground; the coat or object stands on it and its shadow falls on the ground. The line never tilts, never doubles, never leaves the unit.

Cards 18; actions full pills. Every nonzero radius, pills included, takes Apple's continuous corner, copied, never derived; `border-radius`, `rect rx` and superellipses are other curves. A page built with Folio inlines `continuous-corner.js` and marks each box `data-cc="R"`. Anything else draws one of the two paths below, in units of R, with `transform="translate(x y) scale(R)"` and `vector-effect="non-scaling-stroke"`, filling in A = W ÷ R − 3.05732 and B = H ÷ R − 3.05732. R is at most half the short side, a box or a pill, never between; inner R = max(0, outer R − gap); fill, stroke, clip and focus ring share one path.

A box, both sides at least 3.06 R:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .23692 .07491 .457 .07491 .89717 v{B} c0 .44017 0 .66025 -.07491 .89717 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.23692 -.07491 -.457 -.07491 -.89717 v-{B} c0 -.44017 0 -.66025 .07491 -.89717 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

A pill, R = H ÷ 2:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .18851 .07491 .32851 .07491 .36851 c0 .04 0 .18 -.07491 .36851 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.18851 -.07491 -.32851 -.07491 -.36851 c0 -.04 0 -.18 .07491 -.36851 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

## Forms

- **Cover:** the coat on the horizon, the serif claim in the sky.
- **Statement:** one serif sentence in a storm sky over the line.
- **Exhibit:** a cloth or seam detail with its own horizon crossing it.
- **Data:** one figure in the sky, its label below the line.
- **Sequence and comparison:** the same coat in different weathers, one horizon height.
- **Collection:** coats as cards, each on its own small horizon, name then quiet price.
- **Reference and close:** rows below the line; the close is one coat in one weather.

## Variations

- **Storm turn:** one unit in the storm tone with white type; once per sequence.
- **High horizon:** one unit raises the line to 80% for a ground-led detail.

## Do's and Don'ts

- **Look before delivering:** the horizon must read at thumbnail at one height; the check as a field, a coat off the line, or type below the line in a campaign unit are faults.
- **Floors:** facts verbatim and live; renders declared once per piece, in the fine print; every pair in Tokens holds its contrast.
- **Test:** cover the names and pour in new content: a low horizon, weather above it and one object on it still say Highland.
- **Caricature:** the check as wallpaper; a crest; gold.

## Tokens

Authored for this fictional world at S = 1000. 

```yaml
colors:
  canvas: "#ffffff"
  panel: "#f7f4ed"
  dark: "#202124"
  ink: "#202124"
  muted: "#626269"
  mutedDark: "#c4c6c9"
  action: "#1936c8"
  link: "#1936c8"
  focus: "#1936c8"
  darkLink: "#a8b8ff"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
  weather: "#343941"
  cloth: "#e5e0d7"
  trim: "#8f8c85"
typography:
  display: { fontFamily: "Cormorant Garamond, Noto Serif SC, serif", fontSize: 72, fontWeight: 400, lineHeight: 1.05 }
  heading: { fontFamily: "Cormorant Garamond, Noto Serif SC, serif", fontSize: 52, fontWeight: 400, lineHeight: 1.08 }
  lead: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 28, fontWeight: 300, lineHeight: 1.35 }
  body: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.55 }
  product: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 21, fontWeight: 600, lineHeight: 1.3 }
  price: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.4 }
  label: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  caption: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 12, fontWeight: 400, lineHeight: 1.5 }
spacing:
  unit: 8
  pair: 16
  group: 24
  section: 64
  objectInset: 80
  cardInset: 24
rounded:
  card: 18
  action: "pill"
corners:
  contour: "continuous corner"
  shoulderExtent: 1.52866
  innerRadius: "max(0, outerRadius - gap)"
pairs:
  ink-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}" }
  ink-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.ink}" }
  muted-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.muted}" }
  muted-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.muted}" }
  mutedDark-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.mutedDark}" }
  onDark-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.onDark}" }
  onAction-on-action: { backgroundColor: "{colors.action}", textColor: "{colors.onAction}" }
  action-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.action}" }
  link-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.link}" }
  darkLink-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.darkLink}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-07.
Pieces: rain-test (Keynote), trench-series (Store), weather (Editorial), each made from an earlier version of this file, each made from an earlier version of this file. Highland and its coats are fictional; no Burberry product, mark, pattern, photograph or font file is used. Changes after the lock: rewritten around the world's device; the pieces predate it.
