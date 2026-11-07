# Noir · Apple + Luxury, Chanel hand

Noir's world: a fashion house in black and white, the garment leading.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Chanel + Luxury — Compose each garment as a study in black and white: let its silhouette lead, then make its cut judgeable; never borrow a house mark, pattern, or photograph.

World: Noir is a fictional fashion house for garments, construction, archive, and collection across a presented slide, a shop range, and a long read. Every piece keeps one clear claim and a product or its proof at gallery scale; each brings the garment, question, and reader task that make that claim specific.

Method: Begin with the garment's silhouette and the decision it makes visible. Choose one garment or one construction feature as the lead; draw or render it as a declared stand-in, then use a seam, panel, or dated entry only when it can be inspected. Keep the reading path claim → object → evidence → action or lookup. Remove an element only when neither use nor judgment changes without it. Quiet labels and reference matter stay flush left and ordered for lookup.

Amplitude: full for a silhouette, statement, or vista; reduced for labels, prices, and archive entries.

Anti-reference: a seasonal product catalogue with interchangeable photographs, equal cards, and a price-led hierarchy.

## Images

Use a newly drawn or generated illustrative stand-in, never a real house asset. Put the garment or its proof at gallery scale; for a cover the subject owns at least half the field. A whole garment meets the frame as a calm, solid form on white or black; construction evidence sits in a separate inset or plate with live labels. Scale uniformly, preserve shoulder, hem, and any seam being discussed, and recompose the frame rather than crop away the garment. Keep text live in a calm region. Declare illustrative renders once per piece; no mark, pattern, or text is baked into it.

## Layout

Grid system: Gallery field — the garment is the image mass; text and construction evidence share a small set of axes.

Derive a 12-column field from W × H: margins are max(5% W, 6% S), gutters are S/50, and the module is S/125. For projected Keynote, keep critical ink inside 8% of each edge. For a Bento range, give the lead garment the widest span; supporting pieces use equal spans only when they are genuine peers, with a white gutter between square tiles. For Editorial, use one centered column no wider than min(980 px, 82% W), with flush-left reading. Let the black field turn mark a real change in argument; unused tracks remain quiet. Keep the same alignment for garment names, prices, dimensions, captions, and table values. The figure column aligns on decimal or unit, never by color.

## Typography

Use Cormorant Garamond 400 for display and section leads; Inter 400 for body, labels, and prices. Pair Cormorant with Noto Serif SC 400 for Chinese display and Inter with Noto Sans SC 400 for Chinese reading. At S = 1000, set display 80/400/1.02, heading 56/400/1.08, lead 24/300/1.5, body 17/400/1.5, label 14/400/1.4, and caption 12/400/1.45. The title leads by scale; labels are separated by weight and placement. Prices stay at body size or smaller than the garment name. Use tabular figures for years, dimensions, and prices. Keep a mixed Chinese/Latin space, break Chinese at phrase boundaries, and enlarge title boxes before moving body copy. Web reading text remains 16–20 px with a measure of 25–35 CJK characters. On slides the Keynote floors hold: slide title at least 0.1 S, body at least 0.037 S.

## Colors

Ground: Chanel's white and black. Use white `canvas` and near-white `panel` as the light grounds, black `dark` for the single field turn, and black `ink` for reading. `muted` is for secondary labels only; `hairline` separates actual table entries. `action` is black, including links and buy actions: this hand has no chromatic accent. Keep every ground's foreground in the declared pairs. No gradient or colored field.

## Shapes

Keep image fields square-edged; Bento promo tiles use a white gutter rather than a container. If a control or store card needs a radius, use Apple's continuous corner, not a preset: normalized path `M 0 1.52866 C 0 1.08849 0 .86841 .07491 .63149 C .16906 .37282 .37282 .16906 .63149 .07491 C .86841 0 1.08849 0 1.52866 0`. Use the shared helper at 60% smoothing; R is at most half the shorter side and nested corners share centres with inner R = max(0, outer R − gap). A pill action is fully rounded; do not add shadows. Keep garments as solid, recognizable masses; a seam diagram uses one line weight and only the joins needed to explain construction.

## Forms

- Keynote: one judgment, one garment at gallery scale, then one inspectable construction detail; live text stays in a calm zone and the slide cuts to the next claim.
- Bento: one lead collection tile plus smaller true peers, one garment and one quiet price per tile; use a number tile only when its label and context make it independently checkable. It indexes the range; it does not replace the detail proof.
- Editorial: one black vista with one headline and at most one action, followed by a centered, flush-left column; leads carry the argument and the archive uses aligned rows for lookup. End with the source and one quiet close.

## Variations

At a real turn, allow one full black unit with a complete white foreground palette, or one near-empty garment unit whose silhouette carries the whole claim. Keep either to one unit and return to the base field afterward.

## Do's and Don'ts

Floors: facts match each brief exactly; declare every illustration; maintain 4.5:1 text contrast (3:1 for large type); keep reading text live and at its declared size floor for the intended viewing distance; make static output complete as a still; recompose each format instead of scaling a layout; use only original or licensed assets.

Render check: at thumbnail size the garment remains a distinct silhouette; at full size its cut or seam can be inspected.

Test: Hide Noir's name; the garment's balanced couturier proportions, precise shoulder and clean line still read as Chanel's hand without a logo or patterned cue. Substitute another house; this cut should need a different hand.

Caricature: a black-and-white house costume with spaced serif capitals over a garment whose cut cannot be judged.

## Tokens

Values below are derived for this fictional house at S = 1000; the black action is neutral, not an extra accent.

```yaml
colors:
  canvas: "#ffffff"
  panel: "#f5f5f5"
  dark: "#111111"
  ink: "#111111"
  muted: "#626262"
  onDark: "#ffffff"
  action: "#111111"
  onAction: "#ffffff"
  hairline: "#d2d2d7"
typography:
  display: { fontFamily: "Cormorant Garamond, Noto Serif SC, serif", fontSize: 80, fontWeight: 400, lineHeight: 1.02 }
  heading: { fontFamily: "Cormorant Garamond, Noto Serif SC, serif", fontSize: 56, fontWeight: 400, lineHeight: 1.08 }
  lead: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 24, fontWeight: 300, lineHeight: 1.5 }
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
  card: 18
  action: 999
pairs:
  ink-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}" }
  ink-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.ink}" }
  muted-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.muted}" }
  muted-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.muted}" }
  onDark-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.onDark}" }
  onAction-on-action: { backgroundColor: "{colors.action}", textColor: "{colors.onAction}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-07.
Pieces: one-jacket (Keynote), collection (Bento), archive (Editorial), built from this file alone. The house and garments are fictional; no Chanel product, mark, photograph, pattern, or font file is used. Changes after the lock: none.
