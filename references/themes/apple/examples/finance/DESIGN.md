# Ledger, a payments product for small shops · Apple + Finance, Stripe hand

A visual world for a fictional payments product for small shops, not a real Stripe product: money moves, figures line up, and a dark dashboard proves it over a white page. Dialect: Finance, governing hand Stripe. Surfaces shown: Keynote slide, Store card, Editorial opener; Bento grid as a variation for a many-plan unit.

> Use alone: S = 1000 is the reference short side; multiply reference sizes by actual S / 1000. Web px values below are reference units at S = 1000, not fixed sizes for every format. Derive the grid from W × H. Recompose when scaled type would breach the delivery surface's size floor; never shrink facts to fit. Read Overview and Images before any value. Content lives in the brief, never in this file. Figures must line up and be believed.

## Overview

Apple as base, Finance as dialect, Stripe as governing hand — Set the decisive amount with its label and context, then prove it in a readable dashboard or comparison; never turn the page ground into a gradient wallpaper.

World: Ledger, a product that takes payments for small shops, its checkout, its dashboard, its fees, its pricing, across a launch deck, a pricing page and a story opener. Keep Apple's single-accent discipline and one lead per screen; let Stripe's philosophy govern the look — white ground, gradient wash in the hero only, light display type, dark dashboard over white, tabular figures.

Method: Separate the content into a claim, its visible evidence and a decision or lookup task. Build the proof field before setting the labels; select Keynote, Store or Editorial structure by the reader's task, then recompose the reading axis and crop for the actual format.

## Images

No lifestyle photograph hero. The hero image is a dashboard mockup: a dark dashboard sitting over the white page, with readable figures inside it. Dashboard mockups are fictional interface mockups, never a real product's dashboard, and are labelled as such. Crop: dashboard heroes are landscape sources; a portrait cover crop necessarily truncates outer panels, so the cover reads as a dashboard detail, not a complete dashboard — the complete dashboard must appear on a proof slide.

## Layout

Grid system: Gallery field — derive the proof field and one reading axis from W × H; Store subdivides that field into equal peers, Editorial joins it to a reading column, and Keynote assigns one claim to each slide.

White ground with cream bands as rhythm; dark belongs inside dashboard proof, not page sections. Hero: headline and subheadline with a dashboard mockup over or under a gradient wash. Slide field 16:9, critical content inside the central 80%. Store field: white cards on a hairline grid, one plan per card, dashboard thumbnail on top, name and price below. Editorial field: one centred column, with dashboard figures as proof inside the story. Every text shape carries internal padding of at least 11.34 reference units at S = 1000 (0.3 cm at 96 dpi); a shape whose text touches its box edge is unfinished. Title boxes are taller than their type and clear descenders: detail images, cards and body text sit below title descenders, never overlapping them. Number groups sit mid-frame: number, label and context spaced down the slide, never stranded at the top. Body, leads, captions, card names and prices are flush left, ragged right; a centred container is never centred text; only hero, vista and cover headlines may centre.

## Typography

A light display face with tight tracking for headlines, regular body highly readable. Use tabular numerals where the renderer supports them; otherwise use a right-aligned figure column, so amounts and percentages line up across rows, cards and pages. Check the exported alignment; never claim tabular numerals from a renderer that cannot set them.

Concrete type for this fictional world: Inter for display, Inter for body and labels; pair Chinese with Noto Serif SC for serif display and Noto Sans SC for sans roles. These are open-source substitutes, not the named brand's proprietary faces. Tokens below are authored example values, not measured brand specifications.

## Colors

White canvas, cream bands, dark navy as heading and text colour, one indigo accent for calls to action, links and key highlights, on pill buttons. Gradient wash only as a soft multi-colour mesh behind the hero, never as a wallpaper, never on a button or card. The page itself never goes dark; dark is the mockup, not the ground.

Concrete field roles: canvas is the page, panel the card, dark a proof-field polarity, ink the main reading colour, muted the secondary reading colour; onDark and onAction are their contrasting text. Hairline is a non-text separator. Action is the single action accent. Text uses only the foreground/ground pairs in Tokens; other product or gradient colours carry no reading text without a new checked pair.

## Shapes

Every nonzero radius uses **continuous corner**; square forms stay square. 圆角用 Apple continuous corner：直边处曲率为 0、到角中最大，肩部在约 1.53R 内完成（路径为拟合，非解析 G2），禁用普通 circular border-radius，禁用超椭圆 squircle；嵌套同心，内半径 = max(0, 外半径 − 间距)。 The contour is geometry, not an API: in units of R, one corner is A (0, 1), C (0, .96) (0, .82) (.07491, .63149), C (.16906, .37282) (.37282, .16906) (.63149, .07491), C (.86841, 0) (1.08849, 0) (1.52866, 0), B (1.52866, 0). Build that path in whatever the delivery format offers — a native continuous corner, an SVG or canvas path, a freeform shape in a slide, or Figma at 60% smoothing — and use the same path for fill, border and media clip, with R clamped to min(R, h/2, w/(2 × 1.52866)). This 1.53R construction is the project's implementation brief, not an Apple-published formula; inspect the delivered edge at size.

Pill primary buttons, dark or indigo filled, with a lighter ghost secondary. Cards carry hairlines and quiet separation, never heavy shadow. No second flat accent, no square primary button.

## Forms

- Keynote: one thesis per slide; a figure-set slide is one unit, with figures on a shared baseline, one decisive figure in accent and the rest muted — the per-slide exception to the one-number rule.
- Store: one plan per card, dashboard thumbnail on top, name and price below, one buy action per card.
- Editorial: opener with the shop's story, then long leads with dashboard figures as proof inside the column.
- Flyer: one A4 sheet, real internal padding so no text touches a frame edge, one claim, one dominant image, figure or price at display size in the footer rule.
- Website: full-width hero image, hero plus three sections plus footer, hierarchy carried by size and weight, centred container with flush-left body, leads, captions and prices.
- Bento grid: many Ledger plans and features on one page, tiles sized by importance, one claim per tile, figures as small number posters with tabular numerals.

## Variations

One break per unit. A cream-band turn: one band in cream between white sections to pace a long page, each band carrying one idea. A dashboard turn: one dark dashboard mockup over white as a full unit, with a readable figure inside it.

## Do's and Don'ts

Do: white ground, gradient wash in the hero only, light display type, tabular figures, dark dashboard as proof, one indigo accent. Don't: a dark page, a gradient on every section, a heavy display headline, a photograph hero, a square primary button, a second flat accent, figures that will not align.

## Three rules from the supplementary test

- Accent replacement: the Stripe hand's indigo replaces every Apple blue role for this work — link, filled CTA, focus ring and dark-ground link — and Apple blues retire for this work; indigo beside Apple blue would be two accents.
- Vista: the Editorial opener uses a proof-field vista — a dashboard mockup at full-bleed with one headline and at most one action, where the dashboard itself is the atmosphere.
- Bento as index: the Bento variation is an index, not proof — each tile's claim must be provable in a following unit, or the tile itself must carry its checkable number, label or figure.

## Master edition — what changed

Master edition: dark dashboard card moved down to clear title descenders, with its rows below the title. Figures align in a right-aligned figure column so decimals line up. Limitation remaining: tabular setting is unavailable in OfficeCLI, so tabular numerals must not be claimed from the file; the right-aligned column is the fallback, not the setting itself. Cover title is left-aligned (permitted) because a centred title would collide with the right-half hero. Store on the web is left text with right image, price row plus total; Editorial on the web is vista opener plus flush-left long-read column; Bento on the web is main image first, four-tile index after, numbers at equal size. Fonts in the master deck are named, never embedded; spacing is buffered against LibreOffice substitution shifting line breaks.

## Tokens

Authored values for this fictional world at S = 1000. Radius values control size; contour is continuous corner. Product-image colours and hero gradients are source imagery, not additional action colours.

```yaml
colors:
  canvas: "#ffffff"
  panel: "#f8f5ef"
  dark: "#172b4d"
  ink: "#172b4d"
  muted: "#5c6574"
  action: "#5140c9"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
typography:
  display: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 56, fontWeight: 300, lineHeight: 1.07 }
  heading: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 40, fontWeight: 300, lineHeight: 1.1 }
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

Master edition iterated from the master PPT deck, the master Flyer and Website units, and the master world for this example — not from the earlier test cards. Written from references/themes/apple/theme.md and dialects/finance.md, Stripe hand only. Subject is fictional; no Stripe product, dashboard, logo or font file is used. Values here are this world's tokens, not the dialect's rules — the dialect file specifies philosophy only.

Integration update: token values and portable font choices were authored from this world's existing colour and type roles; no new render or transfer test was made for this schema and continuous corner update.
