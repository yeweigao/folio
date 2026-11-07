# Plain · Apple + Minimalist, MUJI hand

Plain's world: everyday products whose packaging is their specification.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + MUJI + Minimalist — Set everyday goods so their use and material can be judged directly; remove whatever serves neither, and let plainness carry the identity; never add a loud mark or decorative Japanese motif.

World: Plain is a fictional no-brand range for household, stationery, and daily-use objects across a presented slide, a shop comparison, and an explanatory long read. Every piece keeps a quiet sans, plain construction, and useful material evidence; each brings the object, task, and dimensions that it needs.

Method: Begin with what the object does. Choose the view that makes its material and join visible; draw the object's net or cutaway only when it explains how the object is made or used. Remove a label, shape, or color if the buyer can still use and understand the piece without it. A new subject is selected by its use and material, not by an ethnic motif. The reading path is object → material → dimension → action or lookup.

Amplitude: the object or its measured proof may own the field; retail labels and reference entries remain small, plain, and ordered.

Anti-reference: an empty white page that withholds the one label, measurement, or action a buyer needs.

## Images

Use newly drawn objects and material sections or declared generated illustrative renders; use no real product photo, logo, or borrowed packaging. When there is no photograph, the object or its proof still fills a gallery-scale field; do not make a small diagram sit alone in a large blank. Keep a silhouette whole on a cover and keep scale bars exact on drawings. Swatches meet the grid as inset material samples, never as page wallpaper. Scale source geometry uniformly and change the frame if the object no longer fits. The small red mark, when needed, is a simple unlettered material/packaging marker, never a logo. Declare renders once per piece; keep explanatory type live. On a cover the object or its measured drawing takes half the frame or more.

## Layout

Grid system: Plain field — square material samples and product views share measured edges; no container is added for decoration.

Derive a 12-column grid from W × H: margin max(5% W, 6% S), gutter S/50, module S/125. Keynote protects the outer 8% safe area and uses one stable left axis. In a Bento range, the lead material comparison spans the widest tracks; real peers occupy matching square spans with the same order of use, material, size, and price. Keep the 1 px hairline only where a buyer needs to separate a sample, card, or table row. Editorial uses a centered column no wider than min(980 px, 82% W), with flush-left text and its cutaway on the same evidence axis. Let material tone provide the image's color; don't repeat its swatch in decorative UI.

## Typography

Use Inter 400 for every Latin role and Noto Sans SC 400 for Chinese; the page has one unembellished grotesque voice. At S = 1000 use display 80/400/1.05, heading 52/400/1.1, lead 24/400/1.45, body 17/400/1.5, label 14/400/1.4, caption 12/400/1.45. Hierarchy is established by scale and position, never by a second face or a bold utility label. Use tabular numerals for measurements and prices; share the baseline and unit position among peers. Keep body text at 16–20 px on the web, 45–75 Latin or 25–35 CJK characters per line, and break Chinese at phrase boundaries. The red mark is never typographic. On slides the Keynote floors hold: slide title at least 0.1 S, body at least 0.037 S.

## Colors

Ground: MUJI's unbleached paper, the brand's signature. Use `canvas` warm paper, `panel` white, `ink` for reading and product outlines, `muted` for labels, and `hairline` only for real divisions. `cotton`, `porcelain`, `beech`, and `board` approximate the depicted materials and may change with the subject. `mark` is a single small dark red mark only; it never becomes a CTA, line, badge, or field. `action` stays ink; no Apple blue or gradient. Keep text pairs at the declared contrast floor.

## Shapes

Keep all page fields, tiles, samples, and actions square: radius zero is part of the no-brand restraint. Use a single 1 px hairline to separate actual reading groups, with no shadows, badge, or ornamental stroke. Draw product outlines with one consistent stroke and show only the joins that explain use. If an unusually small viewport requires a nonzero control radius, use Apple's continuous-corner contour from the shared helper; never substitute a circular preset, and keep the surrounding surface square.

## Forms

- Keynote: one plain object or packaging net at gallery scale, one claim, live labels, and a second field only for its measured material proof.
- Bento: a material-led lead tile, then genuine product peers at square edges; each peer uses the same field order for use, material, size, price, and one plain action. A numeric tile must label its count and scope.
- Editorial: open on the object or a material vista with one headline and at most one action; continue with a centered reading column and a measured cutaway or material plate, then a quiet price/source line.

## Variations

At a real content turn, allow one full unit that shows plain packaging or one product material at a closer scale. The whole surface stays square and quiet; material tone changes only with the subject.

## Do's and Don'ts

Floors: facts match each brief exactly; declare every illustration; maintain 4.5:1 text contrast (3:1 for large type); keep reading text live and at its declared size floor for the intended viewing distance; make static output complete as a still; recompose each format instead of scaling a layout; use only original or licensed assets.

Render check: the object’s material join or cutaway is legible at its displayed scale, and each live annotation can be matched to the part it names.

Test: Hide the brand name and the red mark; can the object still be understood from its use, material and dimensions?

Caricature: a plain surface with Japanese-looking decoration but no usable construction, measurement or instruction.

## Tokens

Values below are derived for this fictional no-brand range at S = 1000; material tones are illustrative and the mark never colors an action.

```yaml
colors:
  canvas: "#f8f6f1"
  panel: "#ffffff"
  dark: "#302d27"
  ink: "#302d27"
  muted: "#666056"
  onDark: "#ffffff"
  action: "#302d27"
  onAction: "#ffffff"
  hairline: "#d5d2ca"
  mark: "#8f1d26"
  cotton: "#d7cdbc"
  porcelain: "#ebe7df"
  beech: "#bd9667"
  board: "#c5a976"
typography:
  display: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 80, fontWeight: 400, lineHeight: 1.05 }
  heading: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 52, fontWeight: 400, lineHeight: 1.1 }
  lead: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 24, fontWeight: 400, lineHeight: 1.45 }
  body: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.5 }
  label: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  caption: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 12, fontWeight: 400, lineHeight: 1.45 }
spacing:
  module: 8
  gutter: 20
  group: 32
  section: 64
  cardInset: 24
rounded:
  field: 0
  card: 0
  action: 0
pairs:
  ink-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}" }
  ink-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.ink}" }
  muted-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.muted}" }
  muted-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.muted}" }
  onDark-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.onDark}" }
  onAction-on-action: { backgroundColor: "{colors.action}", textColor: "{colors.onAction}" }
  mark-on-canvas-large: { backgroundColor: "{colors.canvas}", textColor: "{colors.mark}" }
  mark-on-panel-large: { backgroundColor: "{colors.panel}", textColor: "{colors.mark}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-07.
Pieces: one-sheet (Keynote), three-things (Bento), cut-open (Editorial), built from this file alone. Plain and all goods, packaging, measurements, prices, and materials are fictional; no MUJI product, logo, photograph, or font file is used. Changes after the lock: none.
