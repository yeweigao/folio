# Ledger, a payments product for small shops · Apple + Finance, Stripe hand

A visual world for a fictional payments product for small shops, not a real Stripe product: money moves, figures line up, and a dark dashboard proves it over a white page. Dialect: Finance, governing hand Stripe. Surfaces shown: Keynote slide, Store card, Editorial opener; Bento grid as a variation for a many-plan unit.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts. Figures must line up and be believed.

## Overview

Apple as base, Finance as dialect, Stripe as governing hand — Set the decisive amount with its label and context, then prove it in a readable dashboard or comparison; never turn the page ground into a gradient wallpaper.

World: Ledger, a product that takes payments for small shops, its checkout, its dashboard, its fees, its pricing, across a launch deck, a pricing page and a story opener. Keep Apple's single-accent discipline and one lead per screen; let Stripe's philosophy govern the look — white ground, gradient wash in the hero only, light display type, dark dashboard over white, tabular figures.

Method: Separate the content into a claim, its visible evidence and a decision or lookup task. Build the proof field before setting the labels; select Keynote, Store or Editorial structure by the reader's task, then recompose the reading axis and crop for the actual format.

Amplitude: full on covers, heroes and vistas; reduced on Store, reference and specification units.

Anti-reference: the generic fintech landing: a dark gradient hero, floating cards, a glowing chart.

## Images

No lifestyle photograph hero. The hero image is a dashboard mockup: a dark dashboard sitting over the white page, with readable figures inside it. Dashboard mockups are fictional interface mockups, never a real product's dashboard, and are labelled as such. Crop: dashboard heroes are landscape sources; a portrait cover crop necessarily truncates outer panels, so the cover reads as a dashboard detail, not a complete dashboard — the complete dashboard must appear on a proof slide.

## Layout

Grid system: Gallery field — derive the proof field and one reading axis from W × H; Store subdivides that field into equal peers, Editorial joins it to a reading column, and Keynote assigns one claim to each slide.

White ground with cream bands as rhythm; dark belongs inside dashboard proof, not page sections. Hero: headline and subheadline with a dashboard mockup over or under a gradient wash. Slide field 16:9, critical content inside the central 80%. Store field: white cards on a hairline grid, one plan per card, dashboard thumbnail on top, name and price below. Editorial field: one centred column, with dashboard figures as proof inside the story. Text sits at least 11.34 inside its shape; a title clears its descenders before anything below it; a number group sits mid-frame, number, label and context spaced down. Containers may centre; body, leads, captions, card names and prices stay flush left, ragged right; only hero, vista and cover headlines centre.

## Typography

A light display face with tight tracking for headlines, regular body highly readable. Use tabular numerals where the renderer supports them; otherwise use a right-aligned figure column, so amounts and percentages line up across rows, cards and pages. Check the exported alignment; never claim tabular numerals from a renderer that cannot set them.

Concrete type for this fictional world: Inter for display, Inter for body and labels; pair Chinese with Noto Serif SC for serif display and Noto Sans SC for sans roles. Open-source substitutes, not the brand's own faces.

## Colors

White canvas, cream bands, dark navy as heading and text colour, one indigo accent for calls to action, links and key highlights, on pill buttons. Gradient wash only as a soft multi-colour mesh behind the hero, never as a wallpaper, never on a button or card. The page itself never goes dark; dark is the mockup, not the ground.

Roles: canvas the page, panel the card, dark the proof-field polarity, ink and muted the reading colours, onDark and onAction their contrasts, hairline a non-text separator; action is the single action accent. Reading text uses only the pairs in Tokens. Accent: indigo replaces every Apple blue role.

## Shapes

Every nonzero radius takes Apple's continuous corner; square forms stay square. One corner, inward from the corner point in units of R: `M 0 1.52866 C 0 1.08849 0 .86841 .07491 .63149 C .16906 .37282 .37282 .16906 .63149 .07491 C .86841 0 1.08849 0 1.52866 0`. R is at most half the shorter side; a side shorter than 3.05732R shortens its shoulder to half the side, toward the native saturated form (first cubic 0 1, 0 .96, 0 .82). Build it natively (`.continuous`), as this path in SVG, canvas, clip or a slide freeform, or in Figma at 60% smoothing; never `border-radius`, `rect rx`, a preset or a superellipse. Fill, stroke and media clip share one path; nested corners share centres, inner R = max(0, outer R − gap).

Pill primary buttons, dark or indigo filled, with a lighter ghost secondary. Cards carry hairlines and quiet separation, never heavy shadow. No second flat accent, no square primary button.

## Forms

- Keynote: one thesis per slide; a figure-set slide is one unit, with figures on a shared baseline, one decisive figure in accent and the rest muted — the per-slide exception to the one-number rule.
- Store: one plan per card, dashboard thumbnail on top, name and price below, one buy action per card.
- Editorial: opener with the shop's story, then long leads with dashboard figures as proof inside the column. The opener is a proof-field vista — a dashboard mockup at full-bleed with one headline and at most one action, where the dashboard itself is the atmosphere.
- Flyer: one A4 sheet, real internal padding so no text touches a frame edge, one claim, one dominant image, figure or price at display size in the footer rule.
- Website: full-width hero image, hero plus three sections plus footer, hierarchy carried by size and weight, centred container with flush-left body, leads, captions and prices.
- Bento grid: many Ledger plans and features on one page, tiles sized by importance, one claim per tile, figures as small number posters with tabular numerals. Tiles index; they do not prove: each claim is proved in a following unit or carries its own figure.

## Variations

One break per unit. A cream-band turn: one band in cream between white sections to pace a long page, each band carrying one idea. A dashboard turn: one dark dashboard mockup over white as a full unit, with a readable figure inside it.

## Do's and Don'ts

Do: white ground, gradient wash in the hero only, light display type, tabular figures, dark dashboard as proof, one indigo accent. Don't: a dark page, a gradient on every section, a heavy display headline, a photograph hero, a square primary button, a second flat accent, figures that will not align.

## Tokens

Authored for this fictional world at S = 1000; radius sets size, the contour is continuous corner. Product-image colours and hero gradients are source imagery, not additional action colours.

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
  shoulderExtent: 1.52866
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
Pieces: quarter-close (Keynote), fee-tiers (Bento), journey (Editorial), each made from this file alone. Subject is fictional; no Stripe product, dashboard, logo or font file is used. Tokens are authored for this world, not measured from the brand.
