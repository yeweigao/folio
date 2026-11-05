# Relay, a deployment platform · Apple + Developer, Vercel hand

A visual world for a fictional deployment platform for small teams, not a real Vercel product: the action is deploy, preview, ship, and the proof is the interface working. Dialect: Developer, governing hand Vercel. Forms shown: Keynote slide, Store card, Editorial opener, Flyer sheet, Website page; Bento grid as a variation for a many-feature unit.

> Use alone: S = 1000 is the reference short side; multiply reference sizes by actual S / 1000. Web px values below are reference units at S = 1000, not fixed sizes for every format. Derive the grid from W × H. Recompose when scaled type would breach the delivery surface's size floor; never shrink facts to fit. Read Overview and Images before any value. Content lives in the brief, never in this file. The interface proves the claim; the headline states the action.

## Overview

Apple as base, Developer as dialect, Vercel as governing hand — Build a readable interface as the proof beneath the claim; reserve gradient for hero-scale verbs and mono for technical labels; never pass abstract placeholder bars off as a working interface.

World: Relay, a platform that takes code to a live URL, its deploy, preview and ship actions, its dashboard, its pricing, across a launch deck, a pricing page and a story opener. Keep Apple's single-accent discipline and one lead per screen; let Vercel's philosophy govern the look — light ground, gradient verbs, mono only for technical labels, interface below the headline as proof.

Method: Separate the content into a claim, its visible evidence and a decision or lookup task. Build the proof field before setting the labels; select Keynote, Store or Editorial structure by the reader's task, then recompose the reading axis and crop for the actual format.

## Images

No photograph hero. The hero image is a product interface: a deployment dashboard, a preview URL, a build log, shown at rest below the headline, with mono labels naming what it is. Screenshots are fictional interface mockups, never a real product's screenshot, and are labelled as such. Crop: interface crops must show the whole frame — a wide crop that cuts a browser frame is rejected and replaced with a letterboxed whole interface, no stretch, no cut frame.

## Layout

Grid system: Gallery field — derive the proof field and one reading axis from W × H; Store subdivides that field into equal peers, Editorial joins it to a reading column, and Keynote assigns one claim to each slide.

Light ground with dark bands only for code and dashboard sections, returning to light after each band. Hero: large centred headline above two actions, product interface below. Slide field 16:9, critical content inside the central 80%. Store field: white cards on a hairline grid, each card carrying one plan with its interface thumbnail. Editorial field: one centred column, with the interface as a full-width proof figure inside the story. Every text shape carries internal padding of at least 11.34 reference units at S = 1000 (0.3 cm at 96 dpi); a shape whose text touches its box edge is unfinished. Title boxes are taller than their type and clear descenders: detail images, cards and body text sit below title descenders, never overlapping them. Number groups sit mid-frame: number, label and context spaced down the slide, never stranded at the top. Body, leads, captions, card names and prices are flush left, ragged right; a centred container is never centred text; only hero, vista and cover headlines may centre.

## Typography

A geometric sans for display and body, sentence case, period-terminated headlines, tight tracking on display, ceiling weight 600. A monospace face only for code, technical labels and small technical details — never for headlines, taglines or body. Body regular, highly readable; display light in feel compared with Apple's 600-weight headline, but never thin enough to fail the contrast floor.

Concrete type for this fictional world: Manrope for display, Manrope for body and labels; pair Chinese with Noto Serif SC for serif display and Noto Sans SC for sans roles. These are open-source substitutes, not the named brand's proprietary faces. Tokens below are authored example values, not measured brand specifications.

## Colors

Near-white canvas, ink text, black and white as the base, one link blue for links. Colour beyond that comes only as a mesh gradient on headline verbs at hero scale, one gradient per verb, never miniaturised onto a button, card or badge, never as a wallpaper. Dark bands are polarity-flipped depth, never the governing ground.

Concrete field roles: canvas is the page, panel the card, dark a proof-field polarity, ink the main reading colour, muted the secondary reading colour; onDark and onAction are their contrasting text. Hairline is a non-text separator. Action is the single neutral action. Text uses only the foreground/ground pairs in Tokens; other product or gradient colours carry no reading text without a new checked pair.

## Shapes

Every nonzero radius uses **continuous corner**; square forms stay square. 圆角用 Apple continuous corner：直边处曲率为 0、到角中最大，肩部在约 1.53R 内完成（路径为拟合，非解析 G2），禁用普通 circular border-radius，禁用超椭圆 squircle；嵌套同心，内半径 = max(0, 外半径 − 间距)。 The contour is geometry, not an API: in units of R, one corner is A (0, 1), C (0, .96) (0, .82) (.07491, .63149), C (.16906, .37282) (.37282, .16906) (.63149, .07491), C (.86841, 0) (1.08849, 0) (1.52866, 0), B (1.52866, 0). Build that path in whatever the delivery format offers — a native continuous corner, an SVG or canvas path, a freeform shape in a slide, or Figma at 60% smoothing — and use the same path for fill, border and media clip, with R clamped to min(R, h/2, w/(2 × 1.52866)). This 1.53R construction is the project's implementation brief, not an Apple-published formula; inspect the delivered edge at size.

Marketing calls to action are full pill, solid dark primary with an outlined secondary; tool and nav controls are small and square-ish. Cards carry inset hairlines and subtle stacked shadows, never heavy shadow. No coloured section blocks as rhythm.

## Forms

- Keynote: one thesis per slide — one verb per slide where the action is the claim — live text over a calm zone, interface below the headline.
- Store: one plan per card, interface thumbnail on top, name and price below, one buy action per card.
- Editorial: opener with the deployment story, then long leads with interface figures as proof inside the column.
- Flyer: one A4 sheet, real internal padding so no text touches a frame edge, one claim, one dominant image, figure or price at display size in the footer rule.
- Website: full-width hero image, hero plus three sections plus footer, hierarchy carried by size and weight, centred container with flush-left body, leads, captions and prices.
- Bento grid: many Relay features on one page, tiles sized by importance, one claim per tile, the deploy-preview-ship actions as the wide tiles, specs as small number posters.

## Variations

One break per unit. A dark band turn: one code or dashboard section on a dark band inside a light page, with a complete foreground palette on that band. A gradient-word turn: one headline verb in gradient, never the whole headline, never a rainbow headline.

## Do's and Don'ts

Do: text-first hero, interface below as proof, mono only for technical labels, gradient verbs at hero scale only, one governing hand per work. Don't: a dark page, a photograph hero, a gradient on a button or card, mono body copy, an all-caps bold headline, a second flat accent.

## Three rules from the supplementary test

- Accent replacement: the Vercel hand's chromatic event is the gradient verb at hero scale, not a second accent beside blue — gradient never sits beside a flat accent, and blue roles for links and CTAs do not gain a competing colour.
- Vista: the Editorial opener uses a proof-field vista — a product interface at full-bleed with one headline and at most one action, where the interface itself is the atmosphere.
- Bento as index: the Bento variation is an index, not proof — each tile's claim must be provable in a following unit, or the tile itself must carry its checkable number, label or figure.

## Master edition — what changed

Master edition: detail image replaced with a letterboxed whole interface, and the number group moved mid-frame. The DESIGN intent was NOT followed on two points in the master deck and is restored here: hero-scale gradient verbs (gradient on the verb only, never wallpaper) and mono for technical labels only (never body) are required again. Limitation remaining: proof interfaces in the master deck are abstract placeholder bars, not readable dashboards — an abstract placeholder-bar interface is NOT proof; proof must be readable. The master deck also carries overflow warnings on its 84 pt number shape, verified only in LibreOffice rendering, not in PowerPoint. Store on the web is left text with right image, price row plus total; Editorial on the web is vista opener plus flush-left long-read column; Bento on the web is main image first, four-tile index after, numbers at equal size. Fonts in the master deck are named, never embedded; spacing is buffered against LibreOffice substitution shifting line breaks.

## Tokens

Authored values for this fictional world at S = 1000. Radius values control size; contour is continuous corner. Product-image colours and hero gradients are source imagery, not additional action colours.

```yaml
colors:
  canvas: "#fafafa"
  panel: "#ffffff"
  dark: "#171717"
  ink: "#171717"
  muted: "#626262"
  action: "#171717"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
  link: "#005cc5"
typography:
  display: { fontFamily: "Manrope, Noto Sans SC, sans-serif", fontSize: 56, fontWeight: 600, lineHeight: 1.07 }
  heading: { fontFamily: "Manrope, Noto Sans SC, sans-serif", fontSize: 40, fontWeight: 600, lineHeight: 1.1 }
  lead: { fontFamily: "Manrope, Noto Sans SC, sans-serif", fontSize: 28, fontWeight: 400, lineHeight: 1.3 }
  body: { fontFamily: "Manrope, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.47 }
  label: { fontFamily: "Manrope, Noto Sans SC, sans-serif", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  fine: { fontFamily: "Manrope, Noto Sans SC, sans-serif", fontSize: 12, fontWeight: 400, lineHeight: 1.5 }
  technical: { fontFamily: "Noto Sans Mono, Noto Sans SC, monospace", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
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
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-05.

Master edition iterated from the master PPT deck, the master Flyer and Website units, and the master world for this example — not from the earlier test cards. Written from references/themes/apple/theme.md and dialects/developer.md, Vercel hand only. Subject is fictional; no Vercel product, screenshot, logo or font file is used. Values here are this world's tokens, not the dialect's rules — the dialect file specifies philosophy only.

Integration update: token values and portable font choices were authored from this world's existing colour and type roles; no new render or transfer test was made for this schema and continuous corner update.
