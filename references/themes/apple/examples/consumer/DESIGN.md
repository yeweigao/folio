# Pebble, a wellness ring · Apple + Consumer, Oura hand

A visual world for a fictional wellness ring, not a real Oura product: a daily rhythm, photographed in a life, with warm paper and a single decisive action colour. Dialect: Consumer, governing hand Oura. Forms shown: Keynote slide, Store card, Editorial opener, Flyer sheet, Website page; Bento grid as a variation for a many-feature unit.

> Use alone: S = 1000 is the reference short side; multiply reference sizes by actual S / 1000. Web px values below are reference units at S = 1000, not fixed sizes for every format. Derive the grid from W × H. Recompose when scaled type would breach the delivery surface's size floor; never shrink facts to fit. Read Overview and Images before any value. Content lives in the brief, never in this file. Photography of the life leads; chrome stays retail-quiet.

## Overview

Apple as base, Consumer as dialect, Oura as governing hand — Compose the product in a life that shows its use, then attach checkable facts in quiet sans; never let a mood photograph replace the claim's evidence.

World: Pebble, a ring worn daily, its sleep and activity rhythms, its app, its price, across a launch deck, a shop page and a story opener. Keep Apple's single-accent discipline and one lead per screen; let Oura's philosophy govern the look — warm paper, high-contrast editorial serif with a quiet grotesque sans, cream-and-earth palette, photography-led layouts, one decisive action colour against otherwise calm surfaces.

Method: Separate the content into a claim, its visible evidence and a decision or lookup task. Build the proof field before setting the labels; select Keynote, Store or Editorial structure by the reader's task, then recompose the reading axis and crop for the actual format.

## Images

Photographs of the ring in a life — morning, sleep, movement — at high resolution, with the ring crisp and the life around it calm. No spec sheet pretending to be a life, no chrome shouting louder than the photograph. Ring photographs are generated stand-ins, not a real manufacturer's photographs, and are labelled as such. Crop: cover text sits in a calm zone of the photograph (pale curtain, top-left), with transparent fill, never over solid blocks of the photograph that cover descenders.

## Layout

Grid system: Gallery field — derive the proof field and one reading axis from W × H; Store subdivides that field into equal peers, Editorial joins it to a reading column, and Keynote assigns one claim to each slide.

Warm paper canvas with cream and earth sections, generous whitespace, photography-led sections. Hero: photograph with one headline and at most one action. Slide field 16:9, critical content inside the central 80%. Store field: softly rounded cards on a hairline grid, one product or plan per card, photograph on top, name and price below. Editorial field: one centred column, with photographs as proof inside the story. Every text shape carries internal padding of at least 11.34 reference units at S = 1000 (0.3 cm at 96 dpi); a shape whose text touches its box edge is unfinished. Title boxes are taller than their type and clear descenders: detail images, cards and body text sit below title descenders, never overlapping them. Number groups sit mid-frame: number, label and context spaced down the slide, never stranded at the top. Body, leads, captions, card names and prices are flush left, ragged right; a centred container is never centred text; only hero, vista and cover headlines may centre.

## Typography

A high-contrast editorial serif for display, a quiet grotesque sans for labels and body. Serif carries the life; sans carries the facts. No sans-only display, no heavy display face competing with the photograph.

Concrete type for this fictional world: Fraunces for display, Inter for body and labels; pair Chinese with Noto Serif SC for serif display and Noto Sans SC for sans roles. These are open-source substitutes, not the named brand's proprietary faces. Tokens below are authored example values, not measured brand specifications.

## Colors

Cream-and-earth palette drawn from mustard, clay and olive, with a single decisive action blue against otherwise calm surfaces. Colour comes from the life and the product, never from chrome. No second action colour, no chromatic chrome element.

Concrete field roles: canvas is the page, panel the card, dark a proof-field polarity, ink the main reading colour, muted the secondary reading colour; onDark and onAction are their contrasting text. Hairline is a non-text separator. Action is the single action accent. Text uses only the foreground/ground pairs in Tokens; other product or gradient colours carry no reading text without a new checked pair.

## Shapes

Every nonzero radius uses **continuous corner**; square forms stay square. 圆角用 Apple continuous corner：直边处曲率为 0、到角中最大，肩部在约 1.53R 内完成（路径为拟合，非解析 G2），禁用普通 circular border-radius，禁用超椭圆 squircle；嵌套同心，内半径 = max(0, 外半径 − 间距)。 The contour is geometry, not an API: in units of R, one corner is A (0, 1), C (0, .96) (0, .82) (.07491, .63149), C (.16906, .37282) (.37282, .16906) (.63149, .07491), C (.86841, 0) (1.08849, 0) (1.52866, 0), B (1.52866, 0). Build that path in whatever the delivery format offers — a native continuous corner, an SVG or canvas path, a freeform shape in a slide, or Figma at 60% smoothing — and use the same path for fill, border and media clip, with R clamped to min(R, h/2, w/(2 × 1.52866)). This 1.53R construction is the project's implementation brief, not an Apple-published formula; inspect the delivered edge at size.

Softly rounded cards, no hard corners except the body grid, no heavy shadow, no decorative border. Calls to action in the single action colour, secondary actions as quiet outlines.

## Forms

- Keynote: one thesis per slide, photograph-led, serif headline, live text over a calm zone.
- Store: one product or plan per card, photograph on top, name and price below, one buy action per card.
- Editorial: opener with the daily rhythm story in serif leads, then long leads with photographs as proof inside the column.
- Flyer: one A4 sheet, real internal padding so no text touches a frame edge, one claim, one dominant image, figure or price at display size in the footer rule.
- Website: full-width hero image, hero plus three sections plus footer, hierarchy carried by size and weight, centred container with flush-left body, leads, captions and prices.
- Bento grid: many Pebble features on one page, tiles sized by importance, one claim per tile, warm paper tiles, specs as small number posters.

## Variations

One break per unit. An earth turn: one section on a clay or olive field inside a cream page, with a complete foreground palette on that field. A serif-lead turn: one long serif lead opening a story section, with body returning to sans below it.

## Do's and Don'ts

Do: warm paper, editorial serif with quiet sans, photography of the life, one decisive action colour, retail chrome quiet. Don't: a cool blue page, a sans-only display, a spec sheet pretending to be a life, chrome shouting louder than the photograph, a second action colour, a chromatic chrome element.

## Three rules from the supplementary test

- Accent replacement: the Oura hand's single decisive action blue is the only blue in this work — it replaces every Apple blue role, and no separate link blue, CTA blue or dark-ground blue remains beside it.
- Vista: the Editorial opener uses a photographic vista — a full-bleed photograph of the life with one headline and at most one action.
- Bento as index: the Bento variation is an index, not proof — each tile's claim must be provable in a following unit, or the tile itself must carry its checkable number, label or figure.

## Master edition — what changed

Master edition: cover text moved to the calm pale-curtain zone at top-left with taller title geometry, fixing cover text sitting on solid cream blocks over the photograph. Limitation remaining: serif display is Georgia in the master deck (substitute, never embedded); line breaks may shift, so spacing is buffered. Store on the web is left text with right image, price row plus total; Editorial on the web is vista opener plus flush-left long-read column; Bento on the web is main image first, four-tile index after, numbers at equal size. Fonts in the master deck are named, never embedded; spacing is buffered against LibreOffice substitution shifting line breaks.

## Tokens

Authored values for this fictional world at S = 1000. Radius values control size; contour is continuous corner. Product-image colours and hero gradients are source imagery, not additional action colours.

```yaml
colors:
  canvas: "#f9f5ed"
  panel: "#eee7db"
  dark: "#243329"
  ink: "#263028"
  muted: "#5a625b"
  action: "#215a8a"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
typography:
  display: { fontFamily: "Fraunces, Noto Serif SC, serif", fontSize: 56, fontWeight: 400, lineHeight: 1.07 }
  heading: { fontFamily: "Fraunces, Noto Serif SC, serif", fontSize: 40, fontWeight: 400, lineHeight: 1.1 }
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

Master edition iterated from the master PPT deck, the master Flyer and Website units, and the master world for this example — not from the earlier test cards. Written from references/themes/apple/theme.md and dialects/consumer.md, Oura hand only. Subject is fictional; no Oura product, photograph, logo or font file is used. Values here are this world's tokens, not the dialect's rules — the dialect file specifies philosophy only.

Integration update: token values and portable font choices were authored from this world's existing colour and type roles; no new render or transfer test was made for this schema and continuous corner update.
