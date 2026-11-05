# Sound, minimal audio · Apple + Minimalist, Bang & Olufsen hand

A visual world for a fictional minimal audio house, not a real Bang & Olufsen product: craftsmanship and material carry the design, the product as sculpture in a quiet room, sound as the only performance claim. Dialect: Minimalist, governing hand Bang & Olufsen. Forms shown: Keynote slide, Store card, Editorial opener, Flyer sheet, Website page; Bento grid as a variation for a system unit.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts. Subtraction is judged by use, not by emptiness.

## Overview

Apple as base, Minimalist as dialect, Bang & Olufsen as governing hand — Compose the object as sculpture, then show aluminium, wood or textile where it explains listening and use; never let chrome compete with the object.

World: Sound, a house that makes minimal audio products — a speaker, a headphone — its material, its sound, its price, across a launch deck, a shop page and a story opener. Keep Apple's single-accent discipline and one lead per screen; let Bang & Olufsen's philosophy govern the look — minimal audio where craftsmanship and material carry the design: aluminium, wood and textile as the palette, the product as sculpture in a quiet room, sound as the only performance claim.

Method: Separate the content into a claim, its visible evidence and a decision or lookup task. Build the proof field before setting the labels; select Keynote, Store or Editorial structure by the reader's task, then recompose the reading axis and crop for the actual format.

Amplitude: full on covers, heroes and vistas; reduced on Store, reference and specification units.

Anti-reference: grey minimal skin: empty white, a thin sans, nothing to hold.

## Images

One audio product per unit, photographed as sculpture in a quiet room, silhouette intact, material readable — aluminium, wood, textile. No lifestyle mood, no decorative photograph. Product photographs are generated stand-ins, not a real manufacturer's photographs, and are labelled as such. Crop: sculpture photographs keep the product whole in its quiet room; a title that overflows into body text, or a detail title sitting underneath its image, is rejected and the title box is made taller and the image moved down.

## Layout

Grid system: Gallery field — derive the proof field and one reading axis from W × H; Store subdivides that field into equal peers, Editorial joins it to a reading column, and Keynote assigns one claim to each slide.

Neutral canvas with generous whitespace, one centred axis per unit, the product as sculpture in the centre of its field. Slide field 16:9, critical content inside the central 80%. Store field: white cards on a hairline grid, one product per card, photograph on top, name and price below. Editorial field: one centred column, with sculpture photographs as proof inside the story. Text sits at least 11.34 inside its shape; a title clears its descenders before anything below it; a number group sits mid-frame, number, label and context spaced down. Containers may centre; body, leads, captions, card names and prices stay flush left, ragged right; only hero, vista and cover headlines centre.

## Typography

One quiet grotesque sans, regular weights, generous leading, no display face competing with the object. Labels and body in the same quiet voice; a display serif or condensed headline would import another school's voice.

Concrete type for this fictional world: Inter for display, Inter for body and labels; pair Chinese with Noto Serif SC for serif display and Noto Sans SC for sans roles. Open-source substitutes, not the brand's own faces.

## Colors

Neutral grounds — white, neutral greys, material tones in aluminium, wood and textile — with colour, where it appears at all, coming from the material itself, never from chrome. No decorative colour, no second accent, no gradient.

Roles: canvas the page, panel the card, dark the proof-field polarity, ink and muted the reading colours, onDark and onAction their contrasts, hairline a non-text separator; action is the single neutral action. Reading text uses only the pairs in Tokens. Accent: none; actions stay neutral, and no blue decorates.

## Shapes

Every nonzero radius takes Apple's continuous corner; square forms stay square. One corner, inward from the corner point in units of R: `M 0 1.52866 C 0 1.08849 0 .86841 .07491 .63149 C .16906 .37282 .37282 .16906 .63149 .07491 C .86841 0 1.08849 0 1.52866 0`. R is at most half the shorter side; a side shorter than 3.05732R shortens its shoulder to half the side, toward the native saturated form (first cubic 0 1, 0 .96, 0 .82). Build it natively (`.continuous`), as this path in SVG, canvas, clip or a slide freeform, or in Figma at 60% smoothing; never `border-radius`, `rect rx`, a preset or a superellipse. Fill, stroke and media clip share one path; nested corners share centres, inner R = max(0, outer R − gap).

Forms following the product's own geometry, never a decorative radius. Cards carry hairlines and quiet separation, never heavy shadow. No chrome detail competing with listening.

## Forms

- Keynote: one thesis per slide, one sculpture product per slide, live text over a calm zone.
- Store: one product per card, photograph on top, name and price below, one buy action per card.
- Editorial: opener with the listening story, then long leads with sculpture photographs as proof inside the column. The opener is a photographic vista — a full-bleed photograph of the product as sculpture in a quiet room with one headline and at most one action.
- Flyer: one A4 sheet, real internal padding so no text touches a frame edge, one claim, one dominant image, figure or price at display size in the footer rule.
- Website: full-width hero image, hero plus three sections plus footer, hierarchy carried by size and weight, centred container with flush-left body, leads, captions and prices.
- Bento grid: a system unit — many Sound products on one page, tiles sized by importance, one claim per tile, each tile one product, specs as small number posters. Tiles index; they do not prove: each claim is proved in a following unit or carries its own figure; a tile's sound claim is its check, not its proof of listening.

## Variations

One break per unit. A quiet-room turn: one unit as a single product in an empty quiet room, with one headline and at most one action, the quiet itself as the argument. A material turn: one unit in the product's own material tone, with a complete foreground palette on that tone.

## Do's and Don'ts

Do: material minimal audio, product as sculpture, quiet room, sound as the only performance claim, one quiet sans, material as colour. Don't: a plastic chrome detail, a feature list pretending to be sound, a loud visual competing with listening, a decorative colour, a display face competing with the object.

## Tokens

Authored for this fictional world at S = 1000; radius sets size, the contour is continuous corner. Product-image colours and hero gradients are source imagery, not additional action colours.

```yaml
colors:
  canvas: "#f4f3ef"
  panel: "#ffffff"
  dark: "#282722"
  ink: "#282722"
  muted: "#636159"
  action: "#282722"
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
Pieces: quietest-setting (Keynote), three-surfaces (Store), one-sheet (Editorial), each made from this file alone. Subject is fictional; no Bang & Olufsen product, photograph, logo or font file is used. Tokens are authored for this world, not measured from the brand.
