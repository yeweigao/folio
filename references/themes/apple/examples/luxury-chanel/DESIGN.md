# Noir, a timeless fashion house · Apple + Luxury, Chanel hand

A visual world for a fictional timeless fashion house, not a real Chanel product: black and white as the foundation, ample whitespace, a product that leads without shouting. Dialect: Luxury, governing hand Chanel. Forms shown: Keynote slide, Store card, Editorial opener, Flyer sheet, Website page; Bento grid as a variation for a range unit.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts. Craft is loud; price is quiet. No house mark, pattern or photograph is borrowed.

## Overview

Apple as base, Luxury as dialect, Chanel as governing hand — Compose a single silhouette on a neutral field, then show its construction in a detail; never borrow an interlocking mark or add a chromatic accent.

World: Noir, a house that makes timeless fashion and beauty, its black and white foundation, its clean lines, its restraint, its price, across a launch deck, a shop page and a story opener. Keep Apple's single-accent discipline and one lead per screen; let Chanel's philosophy govern the look — black and white, clean lines, ample whitespace, classic typography, a minimalist aesthetic that lets the product lead, an interlocking mark understood as the house's own and never borrowed.

Method: Separate the content into a claim, its visible evidence and a decision or lookup task. Build the proof field before setting the labels; select Keynote, Store or Editorial structure by the reader's task, then recompose the reading axis and crop for the actual format.

Amplitude: full on covers, heroes and vistas; reduced on Store, reference and specification units.

Anti-reference: fake luxury: gold, glowing outlines, spaced serif capitals over a stock photograph.

## Images

Timeless photographs of the product — a garment, a bottle, a bag — at high resolution, with the product crisp against a calm, neutral field. No borrowed house photograph or mark; all photographs are generated stand-ins for a fictional house, and are labelled as such. Crop: timeless photographs keep the product whole; a display title that wraps must get a taller box, never a body line pushed underneath it.

## Layout

Grid system: Gallery field — derive the proof field and one reading axis from W × H; Store subdivides that field into equal peers, Editorial joins it to a reading column, and Keynote assigns one claim to each slide.

Black-and-white canvas with generous whitespace, product-led sections. Hero: one product photograph with one headline and at most one action. Slide field 16:9, critical content inside the central 80%. Store field: white cards on a hairline grid, one product per card, photograph on top, name and price below in body size — price present but quiet, never larger than the product name. Editorial field: one centred column, with timeless photographs as proof inside the story. Text sits at least 11.34 inside its shape; a title clears its descenders before anything below it; a number group sits mid-frame, number, label and context spaced down. Containers may centre; body, leads, captions, card names and prices stay flush left, ragged right; only hero, vista and cover headlines centre.

## Typography

A classic serif for display, a quiet grotesque sans for labels and body. Serif speaks for the house's timelessness; sans labels and reads. No sans-only display, no heavy display face competing with the product.

Concrete type for this fictional world: Cormorant Garamond for display, Inter for body and labels; pair Chinese with Noto Serif SC for serif display and Noto Sans SC for sans roles. Open-source substitutes, not the brand's own faces.

## Colors

Black and white as the foundation, neutral greys between them, no chromatic colour at all. Black carries action; white carries the page. No second accent, no gradient, no colour field pretending to be a house colour.

Roles: canvas the page, panel the card, dark the proof-field polarity, ink and muted the reading colours, onDark and onAction their contrasts, hairline a non-text separator; action is the single neutral action. Reading text uses only the pairs in Tokens. Accent: black carries every action role; no blue appears.

## Shapes

Every nonzero radius takes Apple's continuous corner; square forms stay square. One corner, inward from the corner point in units of R: `M 0 1.52866 C 0 1.08849 0 .86841 .07491 .63149 C .16906 .37282 .37282 .16906 .63149 .07491 C .86841 0 1.08849 0 1.52866 0`. R is at most half the shorter side; a side shorter than 3.05732R shortens its shoulder to half the side, toward the native saturated form (first cubic 0 1, 0 .96, 0 .82). Build it natively (`.continuous`), as this path in SVG, canvas, clip or a slide freeform, or in Figma at 60% smoothing; never `border-radius`, `rect rx`, a preset or a superellipse. Fill, stroke and media clip share one path; nested corners share centres, inner R = max(0, outer R − gap).

Softly rounded cards, no heavy shadow, no decorative border, no gradient. Calls to action in black, secondary actions as quiet outlines. No chromatic accent colour.

## Forms

- Keynote: one thesis per slide, timeless photograph-led, serif headline, live text over a calm zone.
- Store: one product per card, photograph on top, name and price below in body size, one buy action per card, price quiet.
- Editorial: opener with the house's story in serif leads, then long leads with timeless photographs as proof inside the column. The opener is a photographic vista — a full-bleed timeless photograph with one headline and at most one action.
- Flyer: one A4 sheet, real internal padding so no text touches a frame edge, one claim, one dominant image, figure or price at display size in the footer rule.
- Website: full-width hero image, hero plus three sections plus footer, hierarchy carried by size and weight, centred container with flush-left body, leads, captions and prices.
- Bento grid: range units only — many Noir products on one page, one product and one quiet price per tile, each tile with its own timeless photograph. Tiles index; they do not prove: each claim is proved in a following unit or carries its own figure; a range tile's quiet price is its check, not its proof of timelessness.

## Variations

One break per unit. A black turn: one unit on a black field inside a white page, with a complete foreground palette on that field. A whitespace turn: one unit with a single product and a single headline, and nothing else, as the proof of restraint.

## Do's and Don'ts

Do: black and white, clean lines, ample whitespace, classic serif display, price quiet, one governing hand per work. Don't: a borrowed mark or photograph; a chromatic colour field; a price larger than the product name; a spec sheet pretending to be a house; a sans-only display; a headline shouting louder than the product.

## Tokens

Authored for this fictional world at S = 1000; radius sets size, the contour is continuous corner. Product-image colours and hero gradients are source imagery, not additional action colours.

```yaml
colors:
  canvas: "#ffffff"
  panel: "#f5f5f5"
  dark: "#111111"
  ink: "#111111"
  muted: "#626262"
  action: "#111111"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
typography:
  display: { fontFamily: "Cormorant Garamond, Noto Serif SC, serif", fontSize: 56, fontWeight: 400, lineHeight: 1.07 }
  heading: { fontFamily: "Cormorant Garamond, Noto Serif SC, serif", fontSize: 40, fontWeight: 400, lineHeight: 1.1 }
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
Pieces: one-jacket (Keynote), collection (Bento), archive (Editorial), each made from this file alone. Subject is fictional; no Chanel product, photograph, mark or font file is used. Tokens are authored for this world, not measured from the brand.
