# Kit, a small instrument · Apple + Engineering, Teenage Engineering hand

A visual world for a fictional small instrument, not a real Teenage Engineering product: minimal products with their engineering exposed, visible screws and joints, a product that reads as a kit or a tool. Dialect: Engineering, governing hand Teenage Engineering. Forms shown: Keynote slide, Store card, Editorial opener, Flyer sheet, Website page; Bento grid as a variation for a system unit.

> Use alone: S = 1000 is the reference short side; multiply reference sizes by actual S / 1000. Web px values below are reference units at S = 1000, not fixed sizes for every format. Derive the grid from W × H. Recompose when scaled type would breach the delivery surface's size floor; never shrink facts to fit. Read Overview and Images before any value. Content lives in the brief, never in this file. Every performance claim carries a figure or a section.

## Overview

Apple as base, Engineering as dialect, Teenage Engineering as governing hand — Build the exposed kit so controls, joints and signal colours explain how it works; never use a signal as decoration.

World: Kit, a small instrument that can be understood by looking at it, its exposed mechanism, its controls, its price, across a launch deck, a shop page and a story opener. Keep Apple's single-accent discipline and one lead per screen; let Teenage Engineering's philosophy govern the look — minimal products with their engineering exposed: visible screws and joints, a product that reads as a kit or a tool, playful engineering that still shows how it works, a small set of strong colours used as product signals rather than decoration.

Method: Separate the content into a claim, its visible evidence and a decision or lookup task. Build the proof field before setting the labels; select Keynote, Store or Editorial structure by the reader's task, then recompose the reading axis and crop for the actual format.

## Images

No lifestyle mood alone. The hero image is the exposed kit: the instrument with its screws, joints and controls visible, or shown disassembled as a kit, with labels naming every part shown. Kit images are fictional mockups, never a real manufacturer's images, and are labelled as such. Crop: cover hero must fill its slot — a small hero lost in its own whitespace is rejected and replaced with a tight product crop filling the right half.

## Layout

Grid system: Gallery field — derive the proof field and one reading axis from W × H; Store subdivides that field into equal peers, Editorial joins it to a reading column, and Keynote assigns one claim to each slide.

Neutral canvas with generous whitespace, one centred axis per unit. Hero: headline with the exposed kit below it as proof. Slide field 16:9, critical content inside the central 80%. Store field: white cards on a hairline grid, one product per card, kit thumbnail on top, name and price below. Editorial field: one centred column, with kit images and figures as proof inside the story. Every text shape carries internal padding of at least 11.34 reference units at S = 1000 (0.3 cm at 96 dpi); a shape whose text touches its box edge is unfinished. Title boxes are taller than their type and clear descenders: detail images, cards and body text sit below title descenders, never overlapping them. Number groups sit mid-frame: number, label and context spaced down the slide, never stranded at the top. Body, leads, captions, card names and prices are flush left, ragged right; a centred container is never centred text; only hero, vista and cover headlines may centre.

## Typography

One quiet grotesque sans, regular weights for body, medium weight for display, no display face competing with the mechanism. Use tabular numerals where the renderer supports them; otherwise use a right-aligned figure column, so performance figures line up across rows, cards and pages.

Concrete type for this fictional world: Inter for display, Inter for body and labels; pair Chinese with Noto Serif SC for serif display and Noto Sans SC for sans roles. These are open-source substitutes, not the named brand's proprietary faces. Tokens below are authored example values, not measured brand specifications.

## Colors

Neutral grounds with one signal colour for action and product signals only, never as a field, a wash or a background. The signal colour is a product signal — a control, a joint, an action — not decoration. No second accent, no gradient.

Concrete field roles: canvas is the page, panel the card, dark a proof-field polarity, ink the main reading colour, muted the secondary reading colour; onDark and onAction are their contrasting text. Hairline is a non-text separator. Action is the single action accent. Text uses only the foreground/ground pairs in Tokens; other product or gradient colours carry no reading text without a new checked pair.

## Shapes

Every nonzero radius uses **continuous corner**; square forms stay square. 圆角用 Apple continuous corner：直边处曲率为 0、到角中最大，肩部在约 1.53R 内完成（路径为拟合，非解析 G2），禁用普通 circular border-radius，禁用超椭圆 squircle；嵌套同心，内半径 = max(0, 外半径 − 间距)。 The contour is geometry, not an API: in units of R, one corner is A (0, 1), C (0, .96) (0, .82) (.07491, .63149), C (.16906, .37282) (.37282, .16906) (.63149, .07491), C (.86841, 0) (1.08849, 0) (1.52866, 0), B (1.52866, 0). Build that path in whatever the delivery format offers — a native continuous corner, an SVG or canvas path, a freeform shape in a slide, or Figma at 60% smoothing — and use the same path for fill, border and media clip, with R clamped to min(R, h/2, w/(2 × 1.52866)). This 1.53R construction is the project's implementation brief, not an Apple-published formula; inspect the delivered edge at size.

Cards carry hairlines and quiet separation, never heavy shadow. Diagrams use one line weight, squared ends, no decorative stroke. Calls to action are modest rectangles or pills following the card system, never a pill on every control.

## Forms

- Keynote: one thesis per slide; a kit slide is one unit, with the exposed kit as proof, one decisive figure in accent and the rest muted.
- Store: one product per card, kit thumbnail on top, name and price below, one buy action per card; a configurator variation lets the visitor build the kit without hiding its mechanism.
- Editorial: opener with the kit story, then long leads with kit images and figures as proof inside the column.
- Flyer: one A4 sheet, real internal padding so no text touches a frame edge, one claim, one dominant image, figure or price at display size in the footer rule.
- Website: full-width hero image, hero plus three sections plus footer, hierarchy carried by size and weight, centred container with flush-left body, leads, captions and prices.
- Bento grid: a system unit — many Kit parts and figures on one page, tiles sized by importance, one claim per tile, figures as small number posters with tabular numerals.

## Variations

One break per unit. A kit turn: one full unit as the instrument disassembled, with labels naming every part shown. A signal turn: one unit where a single signal colour marks every control that does one thing, and nothing else is coloured.

## Do's and Don'ts

Do: exposed mechanism, visible screws and joints, kit that can be taken apart, play that shows how the thing works, one signal colour, one governing hand per work. Don't: a hidden mechanism, a playful detail that hides how the thing works, a colour used as decoration rather than signal, a second accent colour, a diagram with every node type at once.

## Three rules from the supplementary test

- Accent replacement: the Teenage Engineering hand's single signal colour replaces every Apple blue role for this work — link, filled CTA, focus ring and dark-ground link — and Apple blues retire for this work; a second accent beside the signal colour would be two accents.
- Vista: the Editorial opener uses a proof-field vista — an exposed kit at full-bleed with one headline and at most one action, where the kit itself is the atmosphere.
- Bento as index: the Bento variation is an index, not proof — each tile's claim must be provable in a following unit, or the tile itself must carry its checkable number, label or figure.

## Master edition — what changed

Master edition: cover hero replaced with a tight product crop on a matching background, filling the right half instead of floating in it. Limitation remaining: the detail image is reused at a different crop/scale across slides — reuse must be declared, not hidden. Tabular setting is unavailable and is not claimed. Store on the web is left text with right image, price row plus total; Editorial on the web is vista opener plus flush-left long-read column; Bento on the web is main image first, four-tile index after, numbers at equal size. Fonts in the master deck are named, never embedded; spacing is buffered against LibreOffice substitution shifting line breaks.

## Tokens

Authored values for this fictional world at S = 1000. Radius values control size; contour is continuous corner. Product-image colours and hero gradients are source imagery, not additional action colours.

```yaml
colors:
  canvas: "#f4f4ef"
  panel: "#ffffff"
  dark: "#272823"
  ink: "#272823"
  muted: "#62635c"
  action: "#9a4100"
  onAction: "#ffffff"
  onDark: "#ffffff"
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

Master edition iterated from the master PPT deck, the master Flyer and Website units, and the master world for this example — not from the earlier test cards. Written from references/themes/apple/theme.md and dialects/engineering.md, Teenage Engineering hand only. Subject is fictional; no Teenage Engineering product, image, logo or font file is used. Values here are this world's tokens, not the dialect's rules — the dialect file specifies philosophy only.

Integration update: token values and portable font choices were authored from this world's existing colour and type roles; no new render or transfer test was made for this schema and continuous corner update.
