# Mono, a small radio · Apple + Minimalist, Braun hand

A visual world for a fictional small radio, not a real Braun product: a functional system, reduced until nothing unnecessary remains, with material and modularity as the only decoration. Dialect: Minimalist, governing hand Braun. Forms shown: Keynote slide, Store card, Editorial opener, Flyer sheet, Website page; Bento grid as a variation for a system unit.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts. Subtraction is judged by use, not by emptiness.

## Overview

Apple as base, Minimalist as dialect, Braun as governing hand — Build the product as a functional modular system, with only the controls and labels its use needs; never add decoration to fill the interval.

World: Mono, a small radio as a system — receiver, speaker, controls — its function, its material, its price, across a launch deck, a shop page and a story opener. Keep Apple's single-accent discipline and one lead per screen; let Braun's philosophy govern the look — less, but better; functional, honest, unobtrusive, modular, thorough to the last detail, and as little design as possible.

Method: Separate the content into a claim, its visible evidence and a decision or lookup task. Build the proof field before setting the labels; select Keynote, Store or Editorial structure by the reader's task, then recompose the reading axis and crop for the actual format.

Amplitude: full on covers, heroes and vistas; reduced on Store, reference and specification units.

Anti-reference: grey minimal skin: empty white, a thin sans, nothing to hold.

## Images

One product per unit, photographed as a functional object on a neutral field, silhouette intact, material readable — aluminium, textile, neutral plastic. No lifestyle mood, no decorative photograph. Radio photographs are generated stand-ins, not a real manufacturer's photographs, and are labelled as such. Crop: hero source is scaled uniformly (never stretched in one axis) and re-cropped if it clips the top of the product; the full silhouette must be intact on cover and proof.

## Layout

Grid system: Gallery field — derive the proof field and one reading axis from W × H; Store subdivides that field into equal peers, Editorial joins it to a reading column, and Keynote assigns one claim to each slide.

Neutral canvas with generous whitespace, one centred axis per unit, modular parts laid out so they combine without fitting. Slide field 16:9, critical content inside the central 80%. Store field: white cards on a hairline grid, one part or product per card, photograph on top, name and price below. Editorial field: one centred column, with the system diagram as a proof figure inside the story. Text sits at least 11.34 inside its shape; a title clears its descenders before anything below it; a number group sits mid-frame, number, label and context spaced down. Containers may centre; body, leads, captions, card names and prices stay flush left, ragged right; only hero, vista and cover headlines centre.

## Typography

One quiet grotesque sans, regular weights, generous leading, no display face competing with the object. Labels and body in the same quiet voice; a display serif or condensed headline would import another school's voice.

Concrete type for this fictional world: Inter for display, Inter for body and labels; pair Chinese with Noto Serif SC for serif display and Noto Sans SC for sans roles. Open-source substitutes, not the brand's own faces.

## Colors

Neutral grounds — white, neutral greys, material tones — with colour, where it appears at all, coming from the material itself, never from chrome. No decorative colour, no second accent, no gradient.

Roles: canvas the page, panel the card, dark the proof-field polarity, ink and muted the reading colours, onDark and onAction their contrasts, hairline a non-text separator; action is the single neutral action. Reading text uses only the pairs in Tokens. Accent: none; actions stay neutral, and no blue decorates.

## Shapes

Every nonzero radius takes Apple's continuous corner; square forms stay square. One corner, inward from the corner point in units of R: `M 0 1.52866 C 0 1.08849 0 .86841 .07491 .63149 C .16906 .37282 .37282 .16906 .63149 .07491 C .86841 0 1.08849 0 1.52866 0`. R is at most half the shorter side; a side shorter than 3.05732R shortens its shoulder to half the side, toward the native saturated form (first cubic 0 1, 0 .96, 0 .82). Build it natively (`.continuous`), as this path in SVG, canvas, clip or a slide freeform, or in Figma at 60% smoothing; never `border-radius`, `rect rx`, a preset or a superellipse. Fill, stroke and media clip share one path; nested corners share centres, inner R = max(0, outer R − gap).

Squared or modestly rounded forms following the product's own geometry, never a decorative radius. Cards carry hairlines and quiet separation, never heavy shadow. Controls do exactly one thing each, and are labelled as such.

## Forms

- Keynote: one thesis per slide, one functional object per slide, live text over a calm zone.
- Store: one part or product per card, photograph on top, name and price below, one buy action per card.
- Editorial: opener with the system's story, then long leads with the system diagram as proof inside the column. The opener is a photographic vista — a full-bleed photograph of the functional object with one headline and at most one action; the system diagram appears as a proof figure inside the column, not as the vista.
- Flyer: one A4 sheet, real internal padding so no text touches a frame edge, one claim, one dominant image, figure or price at display size in the footer rule.
- Website: full-width hero image, hero plus three sections plus footer, hierarchy carried by size and weight, centred container with flush-left body, leads, captions and prices.
- Bento grid: a system unit — many Mono parts on one page, tiles sized by importance, one claim per tile, each tile one part that combines with the others, specs as small number posters. Tiles index; they do not prove: each claim is proved in a following unit or carries its own figure; a system tile's claim is its part combining with the others.

## Variations

One break per unit. A system turn: one unit showing the whole system assembled and disassembled, with every part a whole multiple of one module. A material turn: one unit in the product's own material tone, with a complete foreground palette on that tone.

## Do's and Don'ts

Do: functional, honest, unobtrusive, modular, thorough to the last detail, as little design as possible, one quiet sans, material as colour. Don't: a decorative detail, a feature that does not change use, a loud logo, a decorative colour, a display face competing with the object, an empty page that is hard to use.

## Tokens

Authored for this fictional world at S = 1000; radius sets size, the contour is continuous corner. Product-image colours and hero gradients are source imagery, not additional action colours.

```yaml
colors:
  canvas: "#f7f7f5"
  panel: "#ffffff"
  dark: "#242424"
  ink: "#242424"
  muted: "#626262"
  action: "#242424"
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
Pieces: one-knob (Keynote), three-models (Bento), inside (Editorial), each made from this file alone. Subject is fictional; no Braun product, photograph, logo or font file is used. Tokens are authored for this world, not measured from the brand.
