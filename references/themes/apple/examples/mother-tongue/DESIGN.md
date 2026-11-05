# Lumen, a small home speaker · Apple, mother tongue

A visual world for a fictional home speaker, not an Apple product: one product, shown as a sculpture on a solid field, in a gallery sequence. Dialect: none — the mother tongue alone. Forms shown: Keynote slide, Store card, Editorial opener, Flyer sheet, Website page; Bento grid as a variation for a many-feature unit.

> Use alone: S = 1000 is the reference short side; multiply reference sizes by actual S / 1000. Web px values below are reference units at S = 1000, not fixed sizes for every format. Derive the grid from W × H. Recompose when scaled type would breach the delivery surface's size floor; never shrink facts to fit. Read Overview and Images before any value. Content lives in the brief, never in this file. One product per tile, one claim per unit.

## Overview

Apple, mother tongue — a photography-first gallery in which the product is shown as a sculpture on a solid field, and the interface retreats until it is invisible — Build a gallery from the product silhouette and one claim per field; let field changes mark the reading sequence; never add chrome that competes with the product.

World: Lumen, a small home speaker, its sound, its material, its price, across a launch gallery, a buy page and a story opener. Keep the tile rhythm, the single blue by role, and the product shadow on the render alone; let each piece bring its own claim and reading task.

Method: Separate the content into a claim, its visible evidence and a decision or lookup task. Build the proof field before setting the labels; select Keynote, Store or Editorial structure by the reader's task, then recompose the reading axis and crop for the actual format.

## Images

One dominant subject per unit, photographed as a sculpture on a solid field, silhouette intact, never cropped to fit. The speaker render carries the single system shadow and nothing else does. A full-page picture with baked text is not an Apple slide, it is a poster. Test images are generated stand-ins, not Apple photographs, and are labelled as such in captions. Crop: hero product cropped to its slot, silhouette intact; cover claim sits in a calm light zone, never over a dark bumper or busy ground.

## Layout

Grid system: Gallery field — derive the proof field and one reading axis from W × H; Store subdivides that field into equal peers, Editorial joins it to a reading column, and Keynote assigns one claim to each slide.

Gallery field: one product per tile, centred stack, full-bleed field; tiles stack with no gap, and the change of ground is the divider — white, near-black, parchment in sequence. Slide field 16:9, critical content inside the central 80%, nothing critical in the outer 8%. Store field: white cards on a hairline grid. Editorial field: one centred column, about 980 px on the web. Every text shape carries internal padding of at least 11.34 reference units at S = 1000 (0.3 cm at 96 dpi); a shape whose text touches its box edge is unfinished. Title boxes are taller than their type and clear descenders: detail images, cards and body text sit below title descenders, never overlapping them. Number groups sit mid-frame: number, label and context spaced down the slide, never stranded at the top. Body, leads, captions, card names and prices are flush left, ragged right; a centred container is never centred text; only hero, vista and cover headlines may centre.

## Typography

SF Pro Display for titles, SF Pro Text for body; off Apple devices Inter is the substitute, tracking tightened a further 0.01 em at display sizes. Hero 56 px at 600, leading 1.07, tracking −0.28 px; tile headline 40 px at 600; body 17 px at 400, leading 1.47; caption 14 px; fine print 12 px. Weight 500 never appears; headlines are 600, body is 400.

Tokens specify the portable Inter / Noto Sans SC version. Use the system SF stack only where the platform provides it; do not distribute SF font files. These are authored example values based on the theme's reference ramp, not Apple specifications.

## Colors

Grounds: white, parchment, near-black product tiles, pure black for video and photograph void. Ink on light grounds, white on dark. Muted secondary and tertiary greys for secondary and footnote text. Blue by role only: link, filled CTA and focus ring, dark-ground link — never one variable for all three. No second hue; colour beyond blue comes from the product itself.

Concrete field roles: canvas is the page, panel the card, dark a proof-field polarity, ink the main reading colour, muted the secondary reading colour; onDark and onAction are their contrasting text. Hairline is a non-text separator. Action is the single action accent. Text uses only the foreground/ground pairs in Tokens; other product or gradient colours carry no reading text without a new checked pair.

## Shapes

Every nonzero radius uses **continuous corner**; square forms stay square. 圆角用 Apple continuous corner：直边处曲率为 0、到角中最大，肩部在约 1.53R 内完成（路径为拟合，非解析 G2），禁用普通 circular border-radius，禁用超椭圆 squircle；嵌套同心，内半径 = max(0, 外半径 − 间距)。 The contour is geometry, not an API: in units of R, one corner is A (0, 1), C (0, .96) (0, .82) (.07491, .63149), C (.16906, .37282) (.37282, .16906) (.63149, .07491), C (.86841, 0) (1.08849, 0) (1.52866, 0), B (1.52866, 0). Build that path in whatever the delivery format offers — a native continuous corner, an SVG or canvas path, a freeform shape in a slide, or Figma at 60% smoothing — and use the same path for fill, border and media clip, with R clamped to min(R, h/2, w/(2 × 1.52866)). This 1.53R construction is the project's implementation brief, not an Apple-published formula; inspect the delivered edge at size.

Radius ladder: full-bleed fields 0, small elements 5 px, tool buttons 8 px, medium elements 11 px, store cards 18 px, primary actions and choice chips pill. Homepage promo tiles are sharp and full-bleed, separated by gutter; product-page gallery cards are large rounded rectangles. No shadows on cards, buttons or text.

## Forms

- Keynote: one thesis per slide, live text over a calm zone, one dominant image per slide.
- Store: white utility card, square product crop on top, name and price below in body size, one buy action per card.
- Editorial: vista opener with one headline and at most one action, then long leads in a centred column.
- Flyer: one A4 sheet, real internal padding so no text touches a frame edge, one claim, one dominant image, figure or price at display size in the footer rule.
- Website: full-width hero image, hero plus three sections plus footer, hierarchy carried by size and weight, centred container with flush-left body, leads, captions and prices.
- Bento grid: many features on one page, tiles sized by importance, one claim per tile, specs as small number posters, never table rows.

## Variations

One break per unit. A dark turn: one whole unit on a near-black field, with a complete foreground palette on that ground. An oversized numeral: one number at display size, label beneath, the number is the claim, not decoration.

## Do's and Don'ts

Do: one product per tile, one claim per unit, live text, blue only by role, a reduced-motion version as the same static sequence. Don't: text baked into images, bullet walls, a second accent colour, a gradient wallpaper, a shadow on a card, weight 500, a single blue variable for link, CTA and focus.

## Three rules from the supplementary test

- Accent replacement: no brand hand governs this world, so no replacement applies — Apple blues keep their separate roles for link, filled CTA, focus ring and dark-ground link.
- Vista: the Editorial opener uses a photographic vista — a full-bleed product photograph with one headline and at most one action.
- Bento as index: the Bento variation is an index, not proof — each tile's claim must be provable in a following unit, or the tile itself must carry its checkable number, label or figure.

## Master edition — what changed

Master edition: number group moved mid-frame (number, label, context spaced down the slide) so the number slide no longer strands at the top. Limitation remaining: none structural; cover uses a right-half hero, so cover variety across the set is not demonstrated by this deck alone. Store on the web is left text with right image, price row plus total; Editorial on the web is vista opener plus flush-left long-read column; Bento on the web is main image first, four-tile index after, numbers at equal size. Fonts in the master deck are named, never embedded; spacing is buffered against LibreOffice substitution shifting line breaks.

## Tokens

Authored values for this fictional world at S = 1000. Radius values control size; contour is continuous corner. Product-image colours and hero gradients are source imagery, not additional action colours.

```yaml
colors:
  canvas: "#ffffff"
  panel: "#f5f5f7"
  dark: "#272729"
  ink: "#1d1d1f"
  muted: "#6e6e73"
  action: "#0071e3"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
  link: "#0066cc"
  darkLink: "#2997ff"
typography:
  display: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 56, fontWeight: 600, lineHeight: 1.07 }
  heading: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 40, fontWeight: 600, lineHeight: 1.1 }
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
  link-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.link}" }
  darkLink-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.darkLink}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-05.

Master edition iterated from the master PPT deck, the master Flyer and Website units, and the master world for this example — not from the earlier test cards. Written from references/themes/apple/theme.md alone, mother tongue only. Subject is fictional; no Apple product, photograph, logo or font file is used.

Integration update: token values and portable font choices were authored from this world's existing colour and type roles; no new render or transfer test was made for this schema and continuous corner update.
