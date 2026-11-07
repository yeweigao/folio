# Voyager · Apple + Luxury, Louis Vuitton hand

Voyager's world: a leather house read from the whole object to the grain.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Louis Vuitton + Luxury — Build a digital flagship from the whole leather object to the stitching that proves its making; never turn a close detail into wallpaper or borrow a house monogram.

World: Voyager is a fictional leather house for bags, construction, collections, and material stories across a presented slide, a shop range, and a long read. Every piece keeps one lead, a quiet neutral action, and material evidence; each brings the object and question that require a different crop or scale.

Method: Start with the whole object and name the claim it can carry. Descend to material, seam, and edge only when each step adds a checkable fact; a scale bar and direct label make every change of view honest. Keep the reader's path whole object → detail → decision. The work may use one quiet view or several scales, but it never substitutes atmosphere for craft. A new subject transfers by choosing the detail that can be judged at full size.

Amplitude: immersive on the whole object and craft vistas; restrained on names, dimensions, prices, and source notes.

Anti-reference: a catalogue grid that gives every product the same crop, weight, and amount of space.

## Images

The example collection uses declared hand-drawn or generated stand-ins, not house photography, logos, marks, or patterns. Put the whole object on a calm neutral ground at gallery scale; let a material detail meet the frame as a separate plate. Preserve silhouette, seam pitch, hide edge, and the scale-bar relationship in every crop. Scale each plate uniformly from its stated source ratio; change the frame when a detail will not fit. Keep titles live and outside the detail. Declare illustrative renders once per piece; material color describes the fictional hide and is not documentary proof. A cover or vista gives the object half the frame or more; detail plates go closer, never smaller.

## Layout

Grid system: Gallery field — one object mass is followed by a measured detail field, with labels anchored to their evidence.

Derive 12 columns from W × H: margins are max(5% W, 6% S), gutters S/50, and the module S/125. Keynote keeps critical text inside the outer 8% safe area; the object or seam takes the field opposite the reading axis. The Bento range gives the lead silhouette the largest span and true peers equal spans on one baseline; product cards use one crop and shared name, dimension, volume, weight, and price rows. Editorial uses a centered column no wider than min(980 px, 82% W), then aligns a three-detail plate set on one shared caption edge. Use dark only when material or an argument changes polarity. At text scale keep ink gaps at least one body line; no tile receives filler to balance a composition.

## Typography

Use Cormorant Garamond 400 for display and serif leads, Inter 400 for body and labels. Pair Cormorant with Noto Serif SC 400 and Inter with Noto Sans SC 400. At S = 1000 use display 80/400/1.02, heading 56/400/1.08, lead 24/300/1.5, body 17/400/1.5, label 14/400/1.4, caption 12/400/1.45. Scale derives from S; the whole-object lead is set at least 1.4× the body, while prices never exceed the product name. Scale bars, dimensions, and prices use tabular numerals and shared unit alignment. Keep the Chinese/Latin gap consistent, break CJK at phrase boundaries, and allow title height to grow before moving body copy. Web reading text stays 16–20 px and 25–35 CJK characters wide. On slides the Keynote floors hold: slide title at least 0.1 S, body at least 0.037 S.

## Colors

Ground: Louis Vuitton's white; brown stays in the leather. Keep `canvas` white and `panel` stone, a cool neutral that leaves the brown to the leather; use `dark` and `ink` as leather-brown reading polarity, `muted` for labels, and `hairline` for real divisions only. `hideLight`, `hideMid`, and `hideDark` are limited to illustrative leather surfaces; `thread` belongs to the stitch diagram. The image is the only chromatic event; `action` is neutral ink, and links stay underlined ink. No gradient may wash a page or tile. Text uses only declared contrast pairs.

## Shapes

The silhouette is a single bag profile with a body, two handles or one strap as the brief requires, a seam line, and no emblem or monogram. Stitch detail repeats one pitch, one thread thickness, and one direction; scale bars state their unit. Use Apple's continuous-corner curve for inset plates and cards: `M 0 1.52866 C 0 1.08849 0 .86841 .07491 .63149 C .16906 .37282 .37282 .16906 .63149 .07491 C .86841 0 1.08849 0 1.52866 0`. Its shoulder is 1.52866R, R ≤ half the short side, and nested inner R = max(0, outer R − gap); use the shared helper for any nonzero radius. Cards and media clips share that path. No shadows, decorative gradients, or pattern fields.

## Forms

- Keynote: one craft claim, a gallery-scale detail that can be counted or measured, and a quiet source column; live title stays clear of the crop.
- Bento: one leading range tile with the objects on a shared scale, followed by unequal or equal spans according to importance; each product tile holds one name and one quiet price, while detail claims go to proof plates.
- Editorial: open with one full-bleed object vista and one headline/action at most; continue in a flush-left reading column with progressively closer, scale-labeled material plates, then one quiet price and source.

## Variations

At a content turn, allow a single whole unit of enlarged stitch or edge detail, with one title and one caption. A second allowed break is an interactive collection view that reveals a real craft relation; the sample pieces remain static and use crop changes to show that relation.

## Do's and Don'ts

Floors: facts match each brief exactly; declare every illustration; maintain 4.5:1 text contrast (3:1 for large type); keep reading text live and at its declared size floor for the intended viewing distance; make static output complete as a still; recompose each format instead of scaling a layout; use only original or licensed assets.

Render check: the stitch pitch can be judged against its scale bar while the whole-object silhouette or material edge remains identifiable.

Test: Hide Voyager's name and brown leather; do the neutral ground, gallery-scale product and quiet decision still read as a digital leather flagship? Substitute another house; the crop and material treatment should need a different hand.

Caricature: leather grain repeated as wallpaper until the object and stitch scale disappear.

## Tokens

Derived for this fictional leather house at S = 1000. Leather tones below are illustration-only material roles.

```yaml
colors:
  canvas: "#ffffff"
  panel: "#f3f2f0"
  dark: "#30271d"
  ink: "#30271d"
  muted: "#686056"
  onDark: "#ffffff"
  action: "#30271d"
  onAction: "#ffffff"
  hairline: "#d2d2d7"
  hideLight: "#d4c2a6"
  hideMid: "#9e805d"
  hideDark: "#49372a"
  thread: "#e4d3b5"
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
  plate: 18
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
Pieces: eight-stitches (Keynote), three-sizes (Bento), from-the-whole (Editorial), built from this file alone. Voyager and every object, material, figure, and price are fictional; no Louis Vuitton product, mark, photograph, monogram, or font file is used. Changes after the lock: none.
