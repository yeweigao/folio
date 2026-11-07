# Ledger · Apple + Stripe

Payments for small shops in Apple + Stripe: white, indigo, figures that close, grounds cut on one slant.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are px at S = 1000, S the format's short side, and scale with it; each is a floor for how far the format is read from, never a ceiling. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath; form names are the maker's, never set on the page. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Stripe style — Make every figure close on white and cut every change of ground on the same slant; never a dark page, never a gradient beyond the first edge.

World: Ledger's payments, pricing, statements, launches and stories, on any surface. Every piece keeps the slanted edge, the white reading field and figures that sum; each brings the amount its reader decides with and the statement that proves it.

Method:
1. Find the amount this reader decides with: a fee, a payout, a total.
2. Build the statement or dashboard that proves it, every line summing to the figure shown.
3. Set the claim light and large above it; the amount is the largest figure.
4. Cut the next ground on the slant; the wave lives only in the first.

Amplitude: Full at the opening claim and the payout; reduced in rates, footnotes and reference.

Anti-reference: A dark fintech wallpaper with floating cards, glowing charts and a gradient behind every section.

## Images

Fictional statements, dashboards and cards drawn live, readable and whole, declared once with the figures as fictional. On a cover the proof takes half the frame or more; a crop of a dashboard is a detail and the whole one belongs on a proof unit. No third-party mark, no real dashboard.

## Layout

Grid system: Ledger field — figures right-aligned on shared decimal edges, so every unit compares and reconciles.

Twelve tracks from W × H: margin max(5% W, 0.06 S), gutter a quarter of the margin, an 8 px module. Labels flush left, amounts on one decimal edge; density rises only inside statements and comparisons. Formats: on a 1600 × 900 slide, critical content stays inside the central 84%, the slide title at least 90 px and body at least 33; a scrolling page reads the tokens as given at a 1440 px viewport, body never below 17 px; a shop subdivides the field into peer cards on hairlines.

## Typography

- Hanken Grotesk, the nearest open face to Stripe's light grotesk, for every role; Chinese in Noto Sans SC on matched baselines.
- Display 80 / 300, tight; heading 48 / 300; lead 28 / 400; body 17 / 400; value 17 / 400 tabular; label 14; caption 12. Decisive totals 600.
- 300 only at display size; figures tabular or on a right-aligned column.

## Colors

Ground: Stripe's white with cool grey-blue bands.
- **canvas** white; **panel** `#f6f9fc` a cool band; **dark** `#172b4d` the statement surface.
- **ink** `#172b4d`, **muted** `#5c6574`; **onDark** white and **mutedDark** `#b9c2d2` on dark.
- **action**, **link** and **focus** `#5140c9` indigo, replacing every Apple blue; **darkLink** `#b5adff` on dark; **onAction** white.
- **waveBlue** `#dfe9ff`, **waveViolet** `#f0e5ff`, **waveMint** `#e2f6ef`: the wave, behind the opening claim only.
- **hairline** `#d2d2d7` under rows.

## Shapes

**The device: the slanted edge.** Every change of ground is cut on one straight slant of 6°, rising to the right, its height across the full width 0.105 W. The direction never changes within a piece; text never sits on the slanted strip; the first slant carries the wave behind the opening claim, every later slant is a plain change of ground. In a fixed frame the slant may enter as one corner cut.

Cards and statements 18; actions full pills; nothing else rounded. Every nonzero radius, pills included, takes Apple's continuous corner, copied, never derived; `border-radius`, `rect rx` and superellipses are other curves. A page built with Folio inlines `continuous-corner.js` and marks each box `data-cc="R"`. Anything else draws one of the two paths below, in units of R, with `transform="translate(x y) scale(R)"` and `vector-effect="non-scaling-stroke"`, filling in A = W ÷ R − 3.05732 and B = H ÷ R − 3.05732. R is at most half the short side, a box or a pill, never between; inner R = max(0, outer R − gap); fill, stroke, clip and focus ring share one path.

A box, both sides at least 3.06 R:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .23692 .07491 .457 .07491 .89717 v{B} c0 .44017 0 .66025 -.07491 .89717 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.23692 -.07491 -.457 -.07491 -.89717 v-{B} c0 -.44017 0 -.66025 .07491 -.89717 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

A pill, R = H ÷ 2:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .18851 .07491 .32851 .07491 .36851 c0 .04 0 .18 -.07491 .36851 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.18851 -.07491 -.32851 -.07491 -.36851 c0 -.04 0 -.18 .07491 -.36851 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

## Forms

- **Cover:** the claim light and large on the wave's slant; the statement at half the frame or more.
- **Statement:** one sentence at display size on white.
- **Exhibit:** a statement or dashboard whole, lines summing.
- **Data:** the decisive amount at display size with unit and period; peers on one decimal edge, the decision in indigo.
- **Sequence and comparison:** a payment's steps as statement lines in order; tiers as columns on one scale from zero.
- **Collection:** plans or products as cards on hairlines, the amount leading each.
- **Reference and close:** dense rows and footnotes on a cool band; the close is one proved claim and one action.

## Variations

- **Statement turn:** one unit's proof on the dark statement surface, once per sequence.
- **Return of the wave:** a later section that opens a new argument may take the wave on its slant; never two in sight.

## Do's and Don'ts

- **Look before delivering:** the slant must be one angle throughout; figures off the decimal edge, a gradient beyond the first slant, a dark page or a total that does not close are faults.
- **Floors:** facts verbatim and live; renders declared once per piece, in the fine print; every pair in Tokens holds its contrast.
- **Test:** cover the names and pour in new content: white fields cut on one slant, indigo actions and figures that close still say Ledger.
- **Caricature:** a neon dashboard that cannot be audited; a gradient on every section.

## Tokens

Authored for this fictional world at S = 1000. 

```yaml
colors:
  canvas: "#ffffff"
  panel: "#f6f9fc"
  dark: "#172b4d"
  ink: "#172b4d"
  muted: "#5c6574"
  mutedDark: "#b9c2d2"
  action: "#5140c9"
  link: "#5140c9"
  focus: "#5140c9"
  darkLink: "#b5adff"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
  waveBlue: "#dfe9ff"
  waveViolet: "#f0e5ff"
  waveMint: "#e2f6ef"
typography:
  display: { fontFamily: "Hanken Grotesk, Noto Sans SC, sans-serif", fontSize: 80, fontWeight: 300, lineHeight: 1.05 }
  heading: { fontFamily: "Hanken Grotesk, Noto Sans SC, sans-serif", fontSize: 48, fontWeight: 300, lineHeight: 1.1 }
  lead: { fontFamily: "Hanken Grotesk, Noto Sans SC, sans-serif", fontSize: 28, fontWeight: 400, lineHeight: 1.42 }
  body: { fontFamily: "Hanken Grotesk, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.55 }
  value: { fontFamily: "Hanken Grotesk, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.4 }
  label: { fontFamily: "Hanken Grotesk, Noto Sans SC, sans-serif", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  caption: { fontFamily: "Hanken Grotesk, Noto Sans SC, sans-serif", fontSize: 12, fontWeight: 400, lineHeight: 1.5 }
spacing:
  unit: 8
  pair: 16
  group: 24
  section: 64
  cardInset: 24
  tileInset: 32
rounded:
  card: 18
  button: "pill"
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
Pieces: quarter-close (Keynote), fee-tiers (Bento), journey (Editorial), each made from an earlier version of this file, each made from an earlier version of this file. Ledger, its merchants and every figure are fictional; no Stripe product, dashboard, logo or font file is used. Changes after the lock: rewritten around the world's device; the pieces predate it.
