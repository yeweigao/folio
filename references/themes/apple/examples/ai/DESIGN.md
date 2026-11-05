# Fern, a writing assistant · Apple + AI, Claude hand

A visual world for a fictional writing assistant, not a real Claude product: intelligence has no photograph, so warm paper stands in for it, and a product surface checks every claim. Dialect: AI, governing hand Claude. Forms shown: Keynote slide, Store card, Editorial opener, Flyer sheet, Website page; Bento grid as a variation for a many-feature unit.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts. The material is a stand-in, not the proof; the product surface is the proof.

## Overview

Apple as base, AI as dialect, Claude as governing hand — Set the writing or editing claim on warm paper and prove it with readable document or conversation content; never let an atmospheric material stand in for product evidence.

World: Fern, an assistant that helps write and edit, its chat and document surfaces, its pricing, its story, across a launch deck, a pricing page and a story opener. Keep Apple's single-accent discipline and one lead per screen; let Claude's philosophy govern the look — warm cream canvas, serif display, warm coral calls to action, dark navy product surfaces, humanist sans for body.

Method: Separate the content into a claim, its visible evidence and a decision or lookup task. Build the proof field before setting the labels; select Keynote, Store or Editorial structure by the reader's task, then recompose the reading axis and crop for the actual format.

Amplitude: full on covers, heroes and vistas; reduced on Store, reference and specification units.

Anti-reference: the generic AI page: a cool gradient, a glowing orb, a robot.

## Images

No robot illustration, no glowing orb, no generic blue gradient. The visual proof is a product surface: a chat surface, a document surface, a code or model card, shown at rest with readable content inside it. Product surfaces are fictional interface mockups, never a real product's interface, and are labelled as such. Crop: product-surface crops show the screen interior only; a crop that lets keyboard keys or chrome peek at an edge is rejected and re-cropped to the interior.

## Layout

Grid system: Gallery field — derive the proof field and one reading axis from W × H; Store subdivides that field into equal peers, Editorial joins it to a reading column, and Keynote assigns one claim to each slide.

Warm cream canvas with cream feature cards and dark navy product surfaces as contrast. Hero: headline with a product surface below it as proof. Slide field 16:9, critical content inside the central 80%. Store field: cream cards on a hairline grid, one plan per card, product surface thumbnail on top, name and price below. Editorial field: one centred column, with product surfaces as proof figures inside the story. Text sits at least 11.34 inside its shape; a title clears its descenders before anything below it; a number group sits mid-frame, number, label and context spaced down. Containers may centre; body, leads, captions, card names and prices stay flush left, ragged right; only hero, vista and cover headlines centre.

## Typography

A slab-serif display face for headlines, a humanist sans for body. Serif speaks; sans labels and reads. No sans-only display, no generic blue-gradient headline, no mono body copy.

Concrete type for this fictional world: Roboto Slab for display, Source Sans 3 for body and labels; pair Chinese with Noto Serif SC for serif display and Noto Sans SC for sans roles. Open-source substitutes, not the brand's own faces.

## Colors

Tinted cream canvas, ink text, warm coral for calls to action, dark navy for product surfaces, cream feature cards. The brand voltage is the cream and coral pairing, deliberately warm and humanist where most AI brands use cool blue and slate. No cool blue page, no gradient wash as the page itself.

Roles: canvas the page, panel the card, dark the proof-field polarity, ink and muted the reading colours, onDark and onAction their contrasts, hairline a non-text separator; action is the single action accent. Reading text uses only the pairs in Tokens. Accent: coral replaces every Apple blue role: link, CTA, focus ring, dark-ground link.

## Shapes

Every nonzero radius takes Apple's continuous corner; square forms stay square. One corner, inward from the corner point in units of R: `M 0 1.52866 C 0 1.08849 0 .86841 .07491 .63149 C .16906 .37282 .37282 .16906 .63149 .07491 C .86841 0 1.08849 0 1.52866 0`. R is at most half the shorter side; a side shorter than 3.05732R shortens its shoulder to half the side, toward the native saturated form (first cubic 0 1, 0 .96, 0 .82). Build it natively (`.continuous`), as this path in SVG, canvas, clip or a slide freeform, or in Figma at 60% smoothing; never `border-radius`, `rect rx`, a preset or a superellipse. Fill, stroke and media clip share one path; nested corners share centres, inner R = max(0, outer R − gap).

Softly rounded cards, cream feature cards, dark navy product cards, no heavy shadow, no decorative border. Calls to action in warm coral, secondary actions as quiet outlines. No pill on every control; shape follows the card system, not a template.

## Forms

- Keynote: one thesis per slide, serif headline, product surface below as proof, live text over a calm zone.
- Store: one plan per card, product surface thumbnail on top, name and price below, one buy action per card.
- Editorial: opener with the assistant's story in serif leads, then long leads with product surfaces as proof inside the column. The opener is a proof-field vista — a product surface at full-bleed with one headline and at most one action, where the surface itself is the atmosphere.
- Flyer: one A4 sheet, real internal padding so no text touches a frame edge, one claim, one dominant image, figure or price at display size in the footer rule.
- Website: full-width hero image, hero plus three sections plus footer, hierarchy carried by size and weight, centred container with flush-left body, leads, captions and prices.
- Bento grid: many Fern features on one page, tiles sized by importance, one claim per tile, cream feature cards as tiles, specs as small number posters. Tiles index; they do not prove: each claim is proved in a following unit or carries its own figure.

## Variations

One break per unit. A dark-surface turn: one product surface on a dark navy card inside a cream page, with a complete foreground palette on that card. A serif-lead turn: one long serif lead opening a story section, with body returning to sans below it.

## Do's and Don'ts

Do: warm cream canvas, serif display, coral calls to action, product surface as proof, one governing hand per work. Don't: a cool blue page, a sans-only display, a robot illustration, a glowing orb, a gradient wash as the page, a claim without a product surface to check it on, a second accent colour.

## Tokens

Authored for this fictional world at S = 1000; radius sets size, the contour is continuous corner. Product-image colours and hero gradients are source imagery, not additional action colours.

```yaml
colors:
  canvas: "#f8f3e8"
  panel: "#fffaf2"
  dark: "#182b40"
  ink: "#272520"
  muted: "#635e56"
  action: "#ad4937"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
typography:
  display: { fontFamily: "Roboto Slab, Noto Serif SC, serif", fontSize: 56, fontWeight: 400, lineHeight: 1.07 }
  heading: { fontFamily: "Roboto Slab, Noto Serif SC, serif", fontSize: 40, fontWeight: 400, lineHeight: 1.1 }
  lead: { fontFamily: "Source Sans 3, Noto Sans SC, sans-serif", fontSize: 28, fontWeight: 400, lineHeight: 1.3 }
  body: { fontFamily: "Source Sans 3, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.47 }
  label: { fontFamily: "Source Sans 3, Noto Sans SC, sans-serif", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  fine: { fontFamily: "Source Sans 3, Noto Sans SC, sans-serif", fontSize: 12, fontWeight: 400, lineHeight: 1.5 }
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
Pieces: deleted-sentence (Keynote), word-allowance (Store), draft-and-final (Editorial), each made from this file alone. Subject is fictional; no Claude product, interface, logo or font file is used. Tokens are authored for this world, not measured from the brand.
