# Sound, minimal audio · Apple + Minimalist, Bang & Olufsen hand

A visual world for a fictional minimal audio house, not a real Bang & Olufsen product: craftsmanship and material carry the design, the product as sculpture in a quiet room, sound as the only performance claim. Dialect: Minimalist, governing hand Bang & Olufsen. Forms shown: Keynote slide, Store card, Editorial opener, Flyer sheet, Website page; Bento grid as a variation for a system unit.

> Use alone: S = 1000 is the reference short side; multiply reference sizes by actual S / 1000. Web px values below are reference units at S = 1000, not fixed sizes for every format. Derive the grid from W × H. Recompose when scaled type would breach the delivery surface's size floor; never shrink facts to fit. Read Overview and Images before any value. Content lives in the brief, never in this file. Subtraction is judged by use, not by emptiness.

## Overview

Apple as base, Minimalist as dialect, Bang & Olufsen as governing hand — Compose the object as sculpture, then show aluminium, wood or textile where it explains listening and use; never let chrome compete with the object.

World: Sound, a house that makes minimal audio products — a speaker, a headphone — its material, its sound, its price, across a launch deck, a shop page and a story opener. Keep Apple's single-accent discipline and one lead per screen; let Bang & Olufsen's philosophy govern the look — minimal audio where craftsmanship and material carry the design: aluminium, wood and textile as the palette, the product as sculpture in a quiet room, sound as the only performance claim.

Method: Separate the content into a claim, its visible evidence and a decision or lookup task. Build the proof field before setting the labels; select Keynote, Store or Editorial structure by the reader's task, then recompose the reading axis and crop for the actual format.

## Images

One audio product per unit, photographed as sculpture in a quiet room, silhouette intact, material readable — aluminium, wood, textile. No lifestyle mood, no decorative photograph. Product photographs are generated stand-ins, not a real manufacturer's photographs, and are labelled as such. Crop: sculpture photographs keep the product whole in its quiet room; a title that overflows into body text, or a detail title sitting underneath its image, is rejected and the title box is made taller and the image moved down.

## Layout

Grid system: Gallery field — derive the proof field and one reading axis from W × H; Store subdivides that field into equal peers, Editorial joins it to a reading column, and Keynote assigns one claim to each slide.

Neutral canvas with generous whitespace, one centred axis per unit, the product as sculpture in the centre of its field. Slide field 16:9, critical content inside the central 80%. Store field: white cards on a hairline grid, one product per card, photograph on top, name and price below. Editorial field: one centred column, with sculpture photographs as proof inside the story. Every text shape carries internal padding of at least 11.34 reference units at S = 1000 (0.3 cm at 96 dpi); a shape whose text touches its box edge is unfinished. Title boxes are taller than their type and clear descenders: detail images, cards and body text sit below title descenders, never overlapping them. Number groups sit mid-frame: number, label and context spaced down the slide, never stranded at the top. Body, leads, captions, card names and prices are flush left, ragged right; a centred container is never centred text; only hero, vista and cover headlines may centre.

## Typography

One quiet grotesque sans, regular weights, generous leading, no display face competing with the object. Labels and body in the same quiet voice; a display serif or condensed headline would import another school's voice.

Concrete type for this fictional world: Inter for display, Inter for body and labels; pair Chinese with Noto Serif SC for serif display and Noto Sans SC for sans roles. These are open-source substitutes, not the named brand's proprietary faces. Tokens below are authored example values, not measured brand specifications.

## Colors

Neutral grounds — white, neutral greys, material tones in aluminium, wood and textile — with colour, where it appears at all, coming from the material itself, never from chrome. No decorative colour, no second accent, no gradient.

Concrete field roles: canvas is the page, panel the card, dark a proof-field polarity, ink the main reading colour, muted the secondary reading colour; onDark and onAction are their contrasting text. Hairline is a non-text separator. Action is the single neutral action. Text uses only the foreground/ground pairs in Tokens; other product or gradient colours carry no reading text without a new checked pair.

## Shapes

Every nonzero radius uses **continuous corner**; square forms stay square. 圆角用 Apple continuous corner：直边处曲率为 0、到角中最大，肩部在约 1.53R 内完成（路径为拟合，非解析 G2），禁用普通 circular border-radius，禁用超椭圆 squircle；嵌套同心，内半径 = max(0, 外半径 − 间距)。 The contour is geometry, not an API: in units of R, one corner is A (0, 1), C (0, .96) (0, .82) (.07491, .63149), C (.16906, .37282) (.37282, .16906) (.63149, .07491), C (.86841, 0) (1.08849, 0) (1.52866, 0), B (1.52866, 0). Build that path in whatever the delivery format offers — a native continuous corner, an SVG or canvas path, a freeform shape in a slide, or Figma at 60% smoothing — and use the same path for fill, border and media clip, with R clamped to min(R, h/2, w/(2 × 1.52866)). This 1.53R construction is the project's implementation brief, not an Apple-published formula; inspect the delivered edge at size.

Forms following the product's own geometry, never a decorative radius. Cards carry hairlines and quiet separation, never heavy shadow. No chrome detail competing with listening.

## Forms

- Keynote: one thesis per slide, one sculpture product per slide, live text over a calm zone.
- Store: one product per card, photograph on top, name and price below, one buy action per card.
- Editorial: opener with the listening story, then long leads with sculpture photographs as proof inside the column.
- Flyer: one A4 sheet, real internal padding so no text touches a frame edge, one claim, one dominant image, figure or price at display size in the footer rule.
- Website: full-width hero image, hero plus three sections plus footer, hierarchy carried by size and weight, centred container with flush-left body, leads, captions and prices.
- Bento grid: a system unit — many Sound products on one page, tiles sized by importance, one claim per tile, each tile one product, specs as small number posters.

## Variations

One break per unit. A quiet-room turn: one unit as a single product in an empty quiet room, with one headline and at most one action, the quiet itself as the argument. A material turn: one unit in the product's own material tone, with a complete foreground palette on that tone.

## Do's and Don'ts

Do: material minimal audio, product as sculpture, quiet room, sound as the only performance claim, one quiet sans, material as colour. Don't: a plastic chrome detail, a feature list pretending to be sound, a loud visual competing with listening, a decorative colour, a display face competing with the object.

## Three rules from the supplementary test

- Accent replacement: no chromatic hand accent governs this world, so no accent replaces Apple blue and no decorative colour is introduced — an action uses a neutral treatment, and Apple blue does not appear as a decorative accent.
- Vista: the Editorial opener uses a photographic vista — a full-bleed photograph of the product as sculpture in a quiet room with one headline and at most one action.
- Bento as index: the Bento variation is an index, not proof — each tile's claim must be provable in a following unit, or the tile itself must carry its checkable number, label or figure; a tile's sound claim is its check, not its proof of listening.

## Master edition — what changed

Master edition: proof titles no longer overflow into body text and detail titles no longer sit underneath their images — title boxes made taller, detail image and caption moved down. Limitation remaining: none structural; sound figures in this deck are fictional test figures, not measured data. Store on the web is left text with right image, price row plus total; Editorial on the web is vista opener plus flush-left long-read column; Bento on the web is main image first, four-tile index after, numbers at equal size. Fonts in the master deck are named, never embedded; spacing is buffered against LibreOffice substitution shifting line breaks.

## Tokens

Authored values for this fictional world at S = 1000. Radius values control size; contour is continuous corner. Product-image colours and hero gradients are source imagery, not additional action colours.

```yaml
colors:
  canvas: "#f4f3ef"
  panel: "#ffffff"
  dark: "#282722"
  ink: "#282722"
  muted: "#636159"
  action: "#282722"
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

Master edition iterated from the master PPT deck, the master Flyer and Website units, and the master world for this example — not from the earlier test cards. Written from references/themes/apple/theme.md and dialects/minimalist.md, Bang & Olufsen hand only. Subject is fictional; no Bang & Olufsen product, photograph, logo or font file is used. Values here are this world's tokens, not the dialect's rules — the dialect file specifies philosophy only.

Integration update: token values and portable font choices were authored from this world's existing colour and type roles; no new render or transfer test was made for this schema and continuous corner update.
