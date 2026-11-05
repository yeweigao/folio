# Volt, a small electric car · Apple + Showroom, Tesla hand

A visual world for a fictional small electric car, not a real Tesla product: one photograph, one message, one price per screen, and a configurator that never leaves the screen. Dialect: Showroom, governing hand Tesla. Surfaces shown: Keynote slide, Store card, Editorial opener; Bento grid as a variation for a range unit only.

> Use alone: S = 1000 is the reference short side; multiply reference sizes by actual S / 1000. Web px values below are reference units at S = 1000, not fixed sizes for every format. Derive the grid from W × H. Recompose when scaled type would breach the delivery surface's size floor; never shrink facts to fit. Read Overview and Images before any value. Content lives in the brief, never in this file. The photograph proves the claim; the price stays visible.

## Overview

Apple as base, Showroom as dialect, Tesla as governing hand — Compose one full-viewport object photograph with price and options at the decision point; never tile a single-object hero or hide the configurator behind atmosphere.

World: Volt, a small electric car, its range, its price, its options, its configurator, across a launch deck, a configurator page and a story opener. Keep Apple's single-accent discipline and one lead per screen; let Tesla's philosophy govern the look — full-viewport photograph, normal tracking, two weights only, small square buttons, one electric blue for the primary action only, price and configurator always visible.

Method: Separate the content into a claim, its visible evidence and a decision or lookup task. Build the proof field before setting the labels; select Keynote, Store or Editorial structure by the reader's task, then recompose the reading axis and crop for the actual format.

## Images

Full-viewport cinematic photographs of the car, one per screen, silhouette intact, material readable. No card grid pretending to be a showroom, no chrome competing with the photograph. Car photographs are generated stand-ins, not a real manufacturer's photographs, and are labelled as such. Crop: cover claim sits in a calm light zone (sky or light ground), never over a dark bumper or windshield, and is shortened until it reads over light ground.

## Layout

Grid system: Gallery field — derive the proof field and one reading axis from W × H; Store subdivides that field into equal peers, Editorial joins it to a reading column, and Keynote assigns one claim to each slide.

One full-viewport screen per message, scrolling to the next screen rather than stacking sections on one page. Slide field 16:9, one thesis per slide, photograph full-bleed with live title in the calm zone. Store field: configurator with price, options and blue primary action always visible while the photograph changes. Editorial field: one centred column opening with a full-bleed photograph, then long leads with the price present but quiet. Every text shape carries internal padding of at least 11.34 reference units at S = 1000 (0.3 cm at 96 dpi); a shape whose text touches its box edge is unfinished. Title boxes are taller than their type and clear descenders: detail images, cards and body text sit below title descenders, never overlapping them. Number groups sit mid-frame: number, label and context spaced down the slide, never stranded at the top. Body, leads, captions, card names and prices are flush left, ragged right; a centred container is never centred text; only hero, vista and cover headlines may centre.

## Typography

A display face and a text face with normal letter-spacing at every size — the explicit break with Apple's negative tracking. Only two weights: a medium weight for heroes, a regular weight for interface text. Most interface text is small; heroes are restrained, never heavy.

Concrete type for this fictional world: Inter for display, Inter for body and labels; pair Chinese with Noto Serif SC for serif display and Noto Sans SC for sans roles. These are open-source substitutes, not the named brand's proprietary faces. Tokens below are authored example values, not measured brand specifications.

## Colors

Neutral grounds — dark carbon, graphite, pewter, light ash — with one electric blue for primary calls to action only, never as a field, never as decoration, never beside a second hue. No gradients, no shadows, no borders as decoration. The only chrome is a frosted nav on scroll.

Concrete field roles: canvas is carbon, panel graphite and dark the hero polarity; ink, muted and onDark are light reading colours. Hairline is reserved for a functional option divider. Action is electric blue for the primary action only, with onAction text. Keep body and secondary actions neutral. Text uses only the checked pairs in Tokens.

## Shapes

Every nonzero radius uses **continuous corner**; square forms stay square. 圆角用 Apple continuous corner：直边处曲率为 0、到角中最大，肩部在约 1.53R 内完成（路径为拟合，非解析 G2），禁用普通 circular border-radius，禁用超椭圆 squircle；嵌套同心，内半径 = max(0, 外半径 − 间距)。 The contour is geometry, not an API: in units of R, one corner is A (0, 1), C (0, .96) (0, .82) (.07491, .63149), C (.16906, .37282) (.37282, .16906) (.63149, .07491), C (.86841, 0) (1.08849, 0) (1.52866, 0), B (1.52866, 0). Build that path in whatever the delivery format offers — a native continuous corner, an SVG or canvas path, a freeform shape in a slide, or Figma at 60% smoothing — and use the same path for fill, border and media clip, with R clamped to min(R, h/2, w/(2 × 1.52866)). This 1.53R construction is the project's implementation brief, not an Apple-published formula; inspect the delivered edge at size.

Buttons are small squares, never pill. Primary in electric blue, secondary as frosted or ghost treatments. No shadowed cards, no gradient wash, no bordered panels as decoration.

## Forms

- Keynote: one thesis per slide, one full-bleed photograph per slide, live title in the calm zone.
- Store: configurator — price, options and blue primary action always visible, photograph changing behind them.
- Editorial: full-bleed photograph opener, then long leads; price present but quiet, never the headline.
- Flyer: one A4 sheet, real internal padding so no text touches a frame edge, one claim, one dominant image, figure or price at display size in the footer rule.
- Website: full-width hero image, hero plus three sections plus footer, hierarchy carried by size and weight, centred container with flush-left body, leads, captions and prices.
- Bento grid: range units only — many Volt variants on one page, one object and one price per tile, each tile with its own photograph. Bento never visits a single-object hero unit.

## Variations

One break per unit. A configurator turn: the photograph changes while price, options and action stay fixed. A subtraction turn: remove everything that does not change the photograph, the message or the price.

## Do's and Don'ts

Do: one photograph and one message per screen, normal tracking, price and configurator always visible, one electric blue for action only, frosted nav only. Don't: a pill button, tight tracking, a heavy headline, a gradient wash, a shadowed card, a price hidden until checkout, three messages stacked on one screen, a second accent colour.

## Three rules from the supplementary test

- Accent replacement: the Tesla hand's electric blue replaces every Apple blue role for this work — link, filled CTA, focus ring and dark-ground link — and Apple blues retire for this work; electric blue beside Apple blue would be two accents.
- Vista: the Editorial opener uses a photographic vista — a full-bleed car photograph with one headline and at most one action.
- Bento as index: the Bento variation is an index, not proof — each tile's claim must be provable in a following unit, or the tile itself must carry its checkable number, label or figure; a range tile's price is its check, not its proof of range.

## Master edition — what changed

Master edition: cover claim moved into the sky zone and shortened; price stays visible at every step, as the configurator requires. Limitation remaining: none structural; this deck is one of the few full-bleed covers in the set, which exposes how often the set repeats right-half covers. Store on the web is left text with right image, price row plus total; Editorial on the web is vista opener plus flush-left long-read column; Bento on the web is main image first, four-tile index after, numbers at equal size. Fonts in the master deck are named, never embedded; spacing is buffered against LibreOffice substitution shifting line breaks.

## Tokens

Authored values for this fictional world at S = 1000. Radius values control size; contour is continuous corner. Product-image colours and hero gradients are source imagery, not additional action colours.

```yaml
colors:
  canvas: "#171a20"
  panel: "#30343b"
  dark: "#171a20"
  ink: "#f5f5f7"
  muted: "#d2d4d8"
  action: "#1559b7"
  onAction: "#ffffff"
  onDark: "#f5f5f7"
  hairline: "#d2d2d7"
typography:
  display: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 56, fontWeight: 500, lineHeight: 1.07 }
  heading: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 40, fontWeight: 500, lineHeight: 1.1 }
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
  small: 0
  control: 0
  card: 0
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
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-05.

Master edition iterated from the master PPT deck, the master Flyer and Website units, and the master world for this example — not from the earlier test cards. Written from references/themes/apple/theme.md and dialects/showroom.md, Tesla hand only. Subject is fictional; no Tesla product, photograph, logo or font file is used. Values here are this world's tokens, not the dialect's rules — the dialect file specifies philosophy only.

Integration update: token values and portable font choices were authored from this world's existing colour and type roles; no new render or transfer test was made for this schema and continuous corner update.
