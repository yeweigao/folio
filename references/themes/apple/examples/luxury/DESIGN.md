# Atelier, a leather house · Apple + Luxury, Hermès hand

A visual world for a fictional leather house, not a real Hermès product: craft photographed at detail scale, a single bag as the product that carries the house, one orange as the only accent. Dialect: Luxury, governing hand Hermès. Forms shown: Keynote slide, Store card, Editorial opener, Flyer sheet, Website page; Bento grid as a variation for a range unit.

> Use alone: S = 1000 is the reference short side; multiply reference sizes by actual S / 1000. Web px values below are reference units at S = 1000, not fixed sizes for every format. Derive the grid from W × H. Recompose when scaled type would breach the delivery surface's size floor; never shrink facts to fit. Read Overview and Images before any value. Content lives in the brief, never in this file. Craft is loud; price is quiet. No house mark, pattern or photograph is borrowed.

## Overview

Apple as base, Luxury as dialect, Hermès as governing hand — Compose one object, then show the material and craft that justify it; never borrow a house mark, monogram or photograph.

World: Atelier, a house that makes one leather bag, its leather, its stitching, its craft, its price, across a launch deck, a shop page and a story opener. Keep Apple's single-accent discipline and one lead per screen; let Hermès's philosophy govern the look — clean neutral palette, craft photography, refined typography, subtle animation, one orange as the signature colour and the only accent, Apple blue retired for this work.

Method: Separate the content into a claim, its visible evidence and a decision or lookup task. Build the proof field before setting the labels; select Keynote, Store or Editorial structure by the reader's task, then recompose the reading axis and crop for the actual format.

## Images

Craft photography at detail scale: leather texture, stitching, a bag crisp against softened surroundings, a bag shown empty to judge its form. No borrowed house photograph, pattern or mark; all photographs are generated stand-ins for a fictional house, and are labelled as such. Crop: detail crops are tight to the craft detail; a detail image that overlaps title descenders is moved down until descenders clear it.

## Layout

Grid system: Gallery field — derive the proof field and one reading axis from W × H; Store subdivides that field into equal peers, Editorial joins it to a reading column, and Keynote assigns one claim to each slide.

Clean neutral canvas with generous whitespace, product-led sections. Hero: one bag photograph with one headline and at most one action. Slide field 16:9, critical content inside the central 80%. Store field: white cards on a hairline grid, one product per card, photograph on top, name and price below in body size — price present but quiet, never larger than the product name. Editorial field: one centred column, with craft photographs as proof inside the story. Every text shape carries internal padding of at least 11.34 reference units at S = 1000 (0.3 cm at 96 dpi); a shape whose text touches its box edge is unfinished. Title boxes are taller than their type and clear descenders: detail images, cards and body text sit below title descenders, never overlapping them. Number groups sit mid-frame: number, label and context spaced down the slide, never stranded at the top. Body, leads, captions, card names and prices are flush left, ragged right; a centred container is never centred text; only hero, vista and cover headlines may centre.

## Typography

A refined serif for display, a quiet grotesque sans for labels and body. Serif speaks for the house; sans labels and reads. No sans-only display, no heavy display face competing with the product.

Concrete type for this fictional world: Cormorant Garamond for display, Inter for body and labels; pair Chinese with Noto Serif SC for serif display and Noto Sans SC for sans roles. These are open-source substitutes, not the named brand's proprietary faces. Tokens below are authored example values, not measured brand specifications.

## Colors

Clean neutral palette — white, cream, neutral greys — with one orange as the signature colour and the only accent in the work, for pills, links and highlights only, never as a field, a wash or a background. Apple blue does not appear beside the orange in this work.

Concrete field roles: canvas is the page, panel the card, dark a proof-field polarity, ink the main reading colour, muted the secondary reading colour; onDark and onAction are their contrasting text. Hairline is a non-text separator. Action is the single action accent. Text uses only the foreground/ground pairs in Tokens; other product or gradient colours carry no reading text without a new checked pair.

## Shapes

Every nonzero radius uses **continuous corner**; square forms stay square. 圆角用 Apple continuous corner：直边处曲率为 0、到角中最大，肩部在约 1.53R 内完成（路径为拟合，非解析 G2），禁用普通 circular border-radius，禁用超椭圆 squircle；嵌套同心，内半径 = max(0, 外半径 − 间距)。 The contour is geometry, not an API: in units of R, one corner is A (0, 1), C (0, .96) (0, .82) (.07491, .63149), C (.16906, .37282) (.37282, .16906) (.63149, .07491), C (.86841, 0) (1.08849, 0) (1.52866, 0), B (1.52866, 0). Build that path in whatever the delivery format offers — a native continuous corner, an SVG or canvas path, a freeform shape in a slide, or Figma at 60% smoothing — and use the same path for fill, border and media clip, with R clamped to min(R, h/2, w/(2 × 1.52866)). This 1.53R construction is the project's implementation brief, not an Apple-published formula; inspect the delivered edge at size.

Softly rounded cards, no heavy shadow, no decorative border, no gradient. Calls to action in orange, secondary actions as quiet outlines. No second accent colour.

## Forms

- Keynote: one thesis per slide, craft photograph-led, serif headline, live text over a calm zone.
- Store: one product per card, photograph on top, name and price below in body size, one buy action per card, price quiet.
- Editorial: opener with the house's story in serif leads, then long leads with craft photographs as proof inside the column.
- Flyer: one A4 sheet, real internal padding so no text touches a frame edge, one claim, one dominant image, figure or price at display size in the footer rule.
- Website: full-width hero image, hero plus three sections plus footer, hierarchy carried by size and weight, centred container with flush-left body, leads, captions and prices.
- Bento grid: range units only — many Atelier products on one page, one product and one quiet price per tile, each tile with its own craft photograph.

## Variations

One break per unit. A craft-detail turn: one full-bleed detail photograph as a unit, with one headline and at most one action, the detail itself as the argument. An orange turn: one pill or link in orange as the single accent moment on an otherwise neutral page.

## Do's and Don'ts

Do: clean neutral palette, craft photography at detail scale, serif display, one orange as the only accent, price quiet, one governing hand per work. Don't: a borrowed mark, pattern or photograph; a second accent beside the orange; orange as a field or wash; a price larger than the product name; a spec sheet pretending to be a house; a sans-only display.

## Three rules from the supplementary test

- Accent replacement: the Hermès hand's orange replaces every Apple blue role for this work — link, filled CTA, focus ring and dark-ground link — and Apple blues retire for this work; orange beside Apple blue would be two accents.
- Vista: the Editorial opener uses a photographic vista — a full-bleed craft photograph with one headline and at most one action.
- Bento as index: the Bento variation is an index, not proof — each tile's claim must be provable in a following unit, or the tile itself must carry its checkable number, label or figure; a range tile's quiet price is its check, not its proof of craft.

## Master edition — what changed

Master edition: slide-3 detail image moved down to clear title descenders, caption moved with it. Limitation remaining: the detail image is reused at a different crop/scale across slides — reuse must be declared in the caption record, not hidden; a reused image at a new crop is a second use, not a second proof. Store on the web is left text with right image, price row plus total; Editorial on the web is vista opener plus flush-left long-read column; Bento on the web is main image first, four-tile index after, numbers at equal size. Fonts in the master deck are named, never embedded; spacing is buffered against LibreOffice substitution shifting line breaks.

## Tokens

Authored values for this fictional world at S = 1000. Radius values control size; contour is continuous corner. Product-image colours and hero gradients are source imagery, not additional action colours.

```yaml
colors:
  canvas: "#ffffff"
  panel: "#f7f3eb"
  dark: "#24211d"
  ink: "#24211d"
  muted: "#67615a"
  action: "#a74b00"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
typography:
  display: { fontFamily: "Cormorant Garamond, Noto Serif SC, serif", fontSize: 56, fontWeight: 400, lineHeight: 1.07 }
  heading: { fontFamily: "Cormorant Garamond, Noto Serif SC, serif", fontSize: 40, fontWeight: 400, lineHeight: 1.1 }
  lead: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 28, fontWeight: 400, lineHeight: 1.3 }
  body: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.47 }
  label: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  fine: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 12, fontWeight: 400, lineHeight: 1.5 }
spacing:
  unit: 8
  textInset: 11.34
  cardInset: 24
  proofGap: 40
  tileInset: 80
rounded:
  small: 5
  control: 8
  card: 18
corners:
  contour: "continuous corner"
  smoothing: 0.6
  shoulderExtent: 1.53
  innerRadius: "max(0, outerRadius - gap)"
pairs:
  ink-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}" }
  ink-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.ink}" }
  muted-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.muted}" }
  muted-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.muted}" }
  onDark-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.onDark}" }
  onAction-on-action: { backgroundColor: "{colors.action}", textColor: "{colors.onAction}" }
  action-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.action}" }
  action-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.action}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-05.

Master edition iterated from the master PPT deck, the master Flyer and Website units, and the master world for this example — not from the earlier test cards. Written from references/themes/apple/theme.md and dialects/luxury.md, Hermès hand only. Subject is fictional; no Hermès product, photograph, mark, pattern or font file is used. Values here are this world's tokens, not the dialect's rules — the dialect file specifies philosophy only.

Integration update: token values and portable font choices were authored from this world's existing colour and type roles; no new render or transfer test was made for this schema and continuous corner update.
