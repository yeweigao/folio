# Mono, a small radio · Apple + Minimalist, Braun hand

A visual world for a fictional small radio, not a real Braun product: a functional system, reduced until nothing unnecessary remains, with material and modularity as the only decoration. Dialect: Minimalist, governing hand Braun. Forms shown: Keynote slide, Store card, Editorial opener, Flyer sheet, Website page; Bento grid as a variation for a system unit.

> Use alone: S = 1000 is the reference short side; multiply reference sizes by actual S / 1000. Web px values below are reference units at S = 1000, not fixed sizes for every format. Derive the grid from W × H. Recompose when scaled type would breach the delivery surface's size floor; never shrink facts to fit. Read Overview and Images before any value. Content lives in the brief, never in this file. Subtraction is judged by use, not by emptiness.

## Overview

Apple as base, Minimalist as dialect, Braun as governing hand — Build the product as a functional modular system, with only the controls and labels its use needs; never add decoration to fill the interval.

World: Mono, a small radio as a system — receiver, speaker, controls — its function, its material, its price, across a launch deck, a shop page and a story opener. Keep Apple's single-accent discipline and one lead per screen; let Braun's philosophy govern the look — less, but better; functional, honest, unobtrusive, modular, thorough to the last detail, and as little design as possible.

Method: Separate the content into a claim, its visible evidence and a decision or lookup task. Build the proof field before setting the labels; select Keynote, Store or Editorial structure by the reader's task, then recompose the reading axis and crop for the actual format.

## Images

One product per unit, photographed as a functional object on a neutral field, silhouette intact, material readable — aluminium, textile, neutral plastic. No lifestyle mood, no decorative photograph. Radio photographs are generated stand-ins, not a real manufacturer's photographs, and are labelled as such. Crop: hero source is scaled uniformly (never stretched in one axis) and re-cropped if it clips the top of the product; the full silhouette must be intact on cover and proof.

## Layout

Grid system: Gallery field — derive the proof field and one reading axis from W × H; Store subdivides that field into equal peers, Editorial joins it to a reading column, and Keynote assigns one claim to each slide.

Neutral canvas with generous whitespace, one centred axis per unit, modular parts laid out so they combine without fitting. Slide field 16:9, critical content inside the central 80%. Store field: white cards on a hairline grid, one part or product per card, photograph on top, name and price below. Editorial field: one centred column, with the system diagram as a proof figure inside the story. Every text shape carries internal padding of at least 11.34 reference units at S = 1000 (0.3 cm at 96 dpi); a shape whose text touches its box edge is unfinished. Title boxes are taller than their type and clear descenders: detail images, cards and body text sit below title descenders, never overlapping them. Number groups sit mid-frame: number, label and context spaced down the slide, never stranded at the top. Body, leads, captions, card names and prices are flush left, ragged right; a centred container is never centred text; only hero, vista and cover headlines may centre.

## Typography

One quiet grotesque sans, regular weights, generous leading, no display face competing with the object. Labels and body in the same quiet voice; a display serif or condensed headline would import another school's voice.

Concrete type for this fictional world: Inter for display, Inter for body and labels; pair Chinese with Noto Serif SC for serif display and Noto Sans SC for sans roles. These are open-source substitutes, not the named brand's proprietary faces. Tokens below are authored example values, not measured brand specifications.

## Colors

Neutral grounds — white, neutral greys, material tones — with colour, where it appears at all, coming from the material itself, never from chrome. No decorative colour, no second accent, no gradient.

Concrete field roles: canvas is the page, panel the card, dark a proof-field polarity, ink the main reading colour, muted the secondary reading colour; onDark and onAction are their contrasting text. Hairline is a non-text separator. Action is the single neutral action. Text uses only the foreground/ground pairs in Tokens; other product or gradient colours carry no reading text without a new checked pair.

## Shapes

Every nonzero radius uses **continuous corner**; square forms stay square. 圆角用 Apple continuous corner：直边处曲率为 0、到角中最大，肩部在约 1.53R 内完成（路径为拟合，非解析 G2），禁用普通 circular border-radius，禁用超椭圆 squircle；嵌套同心，内半径 = max(0, 外半径 − 间距)。 The contour is geometry, not an API: in units of R, one corner is A (0, 1), C (0, .96) (0, .82) (.07491, .63149), C (.16906, .37282) (.37282, .16906) (.63149, .07491), C (.86841, 0) (1.08849, 0) (1.52866, 0), B (1.52866, 0). Build that path in whatever the delivery format offers — a native continuous corner, an SVG or canvas path, a freeform shape in a slide, or Figma at 60% smoothing — and use the same path for fill, border and media clip, with R clamped to min(R, h/2, w/(2 × 1.52866)). This 1.53R construction is the project's implementation brief, not an Apple-published formula; inspect the delivered edge at size.

Squared or modestly rounded forms following the product's own geometry, never a decorative radius. Cards carry hairlines and quiet separation, never heavy shadow. Controls do exactly one thing each, and are labelled as such.

## Forms

- Keynote: one thesis per slide, one functional object per slide, live text over a calm zone.
- Store: one part or product per card, photograph on top, name and price below, one buy action per card.
- Editorial: opener with the system's story, then long leads with the system diagram as proof inside the column.
- Flyer: one A4 sheet, real internal padding so no text touches a frame edge, one claim, one dominant image, figure or price at display size in the footer rule.
- Website: full-width hero image, hero plus three sections plus footer, hierarchy carried by size and weight, centred container with flush-left body, leads, captions and prices.
- Bento grid: a system unit — many Mono parts on one page, tiles sized by importance, one claim per tile, each tile one part that combines with the others, specs as small number posters.

## Variations

One break per unit. A system turn: one unit showing the whole system assembled and disassembled, with every part a whole multiple of one module. A material turn: one unit in the product's own material tone, with a complete foreground palette on that tone.

## Do's and Don'ts

Do: functional, honest, unobtrusive, modular, thorough to the last detail, as little design as possible, one quiet sans, material as colour. Don't: a decorative detail, a feature that does not change use, a loud logo, a decorative colour, a display face competing with the object, an empty page that is hard to use.

## Three rules from the supplementary test

- Accent replacement: no chromatic hand accent governs this world, so no accent replaces Apple blue and no decorative colour is introduced — an action uses a neutral treatment, and Apple blue does not appear as a decorative accent.
- Vista: the Editorial opener uses a photographic vista — a full-bleed photograph of the functional object with one headline and at most one action; the system diagram appears as a proof figure inside the column, not as the vista.
- Bento as index: the Bento variation is an index, not proof — each tile's claim must be provable in a following unit, or the tile itself must carry its checkable number, label or figure; a system tile's claim is its part combining with the others.

## Master edition — what changed

Master edition: hero source scaled uniformly to 95% and both cover and proof slots re-cropped (first render clipped the top of the radio), and the close action bar tightened to remove empty space below the action text. Limitation remaining: one shape in this deck has no bodyPr insets — it is a hairline rule shape carrying no text, not a text shape, so it is not a padding failure; every text shape does carry insets. Store on the web is left text with right image, price row plus total; Editorial on the web is vista opener plus flush-left long-read column; Bento on the web is main image first, four-tile index after, numbers at equal size. Fonts in the master deck are named, never embedded; spacing is buffered against LibreOffice substitution shifting line breaks.

## Tokens

Authored values for this fictional world at S = 1000. Radius values control size; contour is continuous corner. Product-image colours and hero gradients are source imagery, not additional action colours.

```yaml
colors:
  canvas: "#f7f7f5"
  panel: "#ffffff"
  dark: "#242424"
  ink: "#242424"
  muted: "#626262"
  action: "#242424"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
typography:
  display: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 56, fontWeight: 400, lineHeight: 1.07 }
  heading: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 40, fontWeight: 400, lineHeight: 1.1 }
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
  card: 11
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

Master edition iterated from the master PPT deck, the master Flyer and Website units, and the master world for this example — not from the earlier test cards. Written from references/themes/apple/theme.md and dialects/minimalist.md, Braun hand only. Subject is fictional; no Braun product, photograph, logo or font file is used. Values here are this world's tokens, not the dialect's rules — the dialect file specifies philosophy only.

Integration update: token values and portable font choices were authored from this world's existing colour and type roles; no new render or transfer test was made for this schema and continuous corner update.
