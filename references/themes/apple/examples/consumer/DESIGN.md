# Pebble, a wellness ring · Apple + Consumer, Oura hand

A visual world for a fictional wellness ring, not a real Oura product: a daily rhythm, photographed in a life, with warm paper and a single decisive action colour. Dialect: Consumer, governing hand Oura. Forms shown: Keynote slide, Store card, Editorial opener, Flyer sheet, Website page; Bento grid as a variation for a many-feature unit.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts. Photography of the life leads; chrome stays retail-quiet.

## Overview

Apple as base, Consumer as dialect, Oura as governing hand — Compose the product in a life that shows its use, then attach checkable facts in quiet sans; never let a mood photograph replace the claim's evidence.

World: Pebble, a ring worn daily, its sleep and activity rhythms, its app, its price, across a launch deck, a shop page and a story opener. Keep Apple's single-accent discipline and one lead per screen; let Oura's philosophy govern the look — warm paper, high-contrast editorial serif with a quiet grotesque sans, cream-and-earth palette, photography-led layouts, one decisive action colour against otherwise calm surfaces.

Method: Separate the content into a claim, its visible evidence and a decision or lookup task. Build the proof field before setting the labels; select Keynote, Store or Editorial structure by the reader's task, then recompose the reading axis and crop for the actual format.

Amplitude: full on covers, heroes and vistas; reduced on Store, reference and specification units.

Anti-reference: a template shop: stock lifestyle photographs, star ratings, promo badges.

## Images

Photographs of the ring in a life — morning, sleep, movement — at high resolution, with the ring crisp and the life around it calm. No spec sheet pretending to be a life, no chrome shouting louder than the photograph. Ring photographs are generated stand-ins, not a real manufacturer's photographs, and are labelled as such. Crop: cover text sits in a calm zone of the photograph (pale curtain, top-left), with transparent fill, never over solid blocks of the photograph that cover descenders.

## Layout

Grid system: Gallery field — derive the proof field and one reading axis from W × H; Store subdivides that field into equal peers, Editorial joins it to a reading column, and Keynote assigns one claim to each slide.

Warm paper canvas with cream and earth sections, generous whitespace, photography-led sections. Hero: photograph with one headline and at most one action. Slide field 16:9, critical content inside the central 80%. Store field: softly rounded cards on a hairline grid, one product or plan per card, photograph on top, name and price below. Editorial field: one centred column, with photographs as proof inside the story. Text sits at least 11.34 inside its shape; a title clears its descenders before anything below it; a number group sits mid-frame, number, label and context spaced down. Containers may centre; body, leads, captions, card names and prices stay flush left, ragged right; only hero, vista and cover headlines centre.

## Typography

A high-contrast editorial serif for display, a quiet grotesque sans for labels and body. Serif carries the life; sans carries the facts. No sans-only display, no heavy display face competing with the photograph.

Concrete type for this fictional world: Fraunces for display, Inter for body and labels; pair Chinese with Noto Serif SC for serif display and Noto Sans SC for sans roles. Open-source substitutes, not the brand's own faces.

## Colors

Cream-and-earth palette drawn from mustard, clay and olive, with a single decisive action blue against otherwise calm surfaces. Colour comes from the life and the product, never from chrome. No second action colour, no chromatic chrome element.

Roles: canvas the page, panel the card, dark the proof-field polarity, ink and muted the reading colours, onDark and onAction their contrasts, hairline a non-text separator; action is the single action accent. Reading text uses only the pairs in Tokens. Accent: the one action blue is the only blue, in every Apple blue role.

## Shapes

Every nonzero radius takes Apple's continuous corner; square forms stay square. One corner, inward from the corner point in units of R: `M 0 1.52866 C 0 1.08849 0 .86841 .07491 .63149 C .16906 .37282 .37282 .16906 .63149 .07491 C .86841 0 1.08849 0 1.52866 0`. R is at most half the shorter side; a side shorter than 3.05732R shortens its shoulder to half the side, toward the native saturated form (first cubic 0 1, 0 .96, 0 .82). Build it natively (`.continuous`), as this path in SVG, canvas, clip or a slide freeform, or in Figma at 60% smoothing; never `border-radius`, `rect rx`, a preset or a superellipse. Fill, stroke and media clip share one path; nested corners share centres, inner R = max(0, outer R − gap).

Softly rounded cards, no hard corners except the body grid, no heavy shadow, no decorative border. Calls to action in the single action colour, secondary actions as quiet outlines.

## Forms

- Keynote: one thesis per slide, photograph-led, serif headline, live text over a calm zone.
- Store: one product or plan per card, photograph on top, name and price below, one buy action per card.
- Editorial: opener with the daily rhythm story in serif leads, then long leads with photographs as proof inside the column. The opener is a photographic vista — a full-bleed photograph of the life with one headline and at most one action.
- Flyer: one A4 sheet, real internal padding so no text touches a frame edge, one claim, one dominant image, figure or price at display size in the footer rule.
- Website: full-width hero image, hero plus three sections plus footer, hierarchy carried by size and weight, centred container with flush-left body, leads, captions and prices.
- Bento grid: many Pebble features on one page, tiles sized by importance, one claim per tile, warm paper tiles, specs as small number posters. Tiles index; they do not prove: each claim is proved in a following unit or carries its own figure.

## Variations

One break per unit. An earth turn: one section on a clay or olive field inside a cream page, with a complete foreground palette on that field. A serif-lead turn: one long serif lead opening a story section, with body returning to sans below it.

## Do's and Don'ts

Do: warm paper, editorial serif with quiet sans, photography of the life, one decisive action colour, retail chrome quiet. Don't: a cool blue page, a sans-only display, a spec sheet pretending to be a life, chrome shouting louder than the photograph, a second action colour, a chromatic chrome element.

## Tokens

Authored for this fictional world at S = 1000; radius sets size, the contour is continuous corner. Product-image colours and hero gradients are source imagery, not additional action colours.

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
Pieces: sleep-report (Keynote), ring-sizing (Bento), one-night (Editorial), each made from this file alone. Subject is fictional; no Oura product, photograph, logo or font file is used. Tokens are authored for this world, not measured from the brand.
