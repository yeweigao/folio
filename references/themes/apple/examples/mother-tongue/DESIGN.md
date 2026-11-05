# Lumen, a small home speaker · Apple, mother tongue

A visual world for a fictional home speaker, not an Apple product: one product, shown as a sculpture on a solid field, in a gallery sequence. Dialect: none — the mother tongue alone. Forms shown: Keynote slide, Store card, Editorial opener, Flyer sheet, Website page; Bento grid as a variation for a many-feature unit.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts. One product per tile, one claim per unit.

## Overview

Apple, mother tongue — a photography-first gallery in which the product is shown as a sculpture on a solid field, and the interface retreats until it is invisible — Build a gallery from the product silhouette and one claim per field; let field changes mark the reading sequence; never add chrome that competes with the product.

World: Lumen, a small home speaker, its sound, its material, its price, across a launch gallery, a buy page and a story opener. Keep the tile rhythm, the single blue by role, and the product shadow on the render alone; let each piece bring its own claim and reading task.

Method: Separate the content into a claim, its visible evidence and a decision or lookup task. Build the proof field before setting the labels; select Keynote, Store or Editorial structure by the reader's task, then recompose the reading axis and crop for the actual format.

Amplitude: full on covers, heroes and vistas; reduced on Store, reference and specification units.

Anti-reference: a SaaS landing page: centred hero, three icon cards, a gradient button.

## Images

One dominant subject per unit, photographed as a sculpture on a solid field, silhouette intact, never cropped to fit. The speaker render carries the single system shadow and nothing else does. A full-page picture with baked text is not an Apple slide, it is a poster. Test images are generated stand-ins, not Apple photographs, and are labelled as such in captions. Crop: hero product cropped to its slot, silhouette intact; cover claim sits in a calm light zone, never over a dark bumper or busy ground.

## Layout

Grid system: Gallery field — derive the proof field and one reading axis from W × H; Store subdivides that field into equal peers, Editorial joins it to a reading column, and Keynote assigns one claim to each slide.

Gallery field: one product per tile, centred stack, full-bleed field; tiles stack with no gap, and the change of ground is the divider — white, near-black, parchment in sequence. Slide field 16:9, critical content inside the central 80%, nothing critical in the outer 8%. Store field: white cards on a hairline grid. Editorial field: one centred column, about 980 px on the web. Text sits at least 11.34 inside its shape; a title clears its descenders before anything below it; a number group sits mid-frame, number, label and context spaced down. Containers may centre; body, leads, captions, card names and prices stay flush left, ragged right; only hero, vista and cover headlines centre.

## Typography

The system face, Display cut for titles and Text cut for body, through `-apple-system, system-ui`; elsewhere Inter, display tracking tightened a further 0.01 em. Hero 56 px at 600, leading 1.07, tracking −0.28 px; tile headline 40 px at 600; body 17 px at 400, leading 1.47; caption 14 px; fine print 12 px. Weight 500 never appears; headlines are 600, body is 400.

Tokens carry the portable Inter / Noto Sans SC version; the system face is never distributed.

## Colors

Grounds: white, parchment, near-black product tiles, pure black for video and photograph void. Ink on light grounds, white on dark. Muted secondary and tertiary greys for secondary and footnote text. Blue by role only: link, filled CTA and focus ring, dark-ground link — never one variable for all three. No second hue; colour beyond blue comes from the product itself.

Roles: canvas the page, panel the card, dark the proof-field polarity, ink and muted the reading colours, onDark and onAction their contrasts, hairline a non-text separator; action is the single action accent. Reading text uses only the pairs in Tokens.

## Shapes

Every nonzero radius takes Apple's continuous corner; square forms stay square. One corner, inward from the corner point in units of R: `M 0 1.52866 C 0 1.08849 0 .86841 .07491 .63149 C .16906 .37282 .37282 .16906 .63149 .07491 C .86841 0 1.08849 0 1.52866 0`. R is at most half the shorter side; a side shorter than 3.05732R shortens its shoulder to half the side, toward the native saturated form (first cubic 0 1, 0 .96, 0 .82). Build it natively (`.continuous`), as this path in SVG, canvas, clip or a slide freeform, or in Figma at 60% smoothing; never `border-radius`, `rect rx`, a preset or a superellipse. Fill, stroke and media clip share one path; nested corners share centres, inner R = max(0, outer R − gap).

Radius ladder: full-bleed fields 0, small elements 5 px, tool buttons 8 px, medium elements 11 px, store cards 18 px, primary actions and choice chips pill. Homepage promo tiles are sharp and full-bleed, separated by gutter; product-page gallery cards are large rounded rectangles. No shadows on cards, buttons or text.

## Forms

- Keynote: one thesis per slide, live text over a calm zone, one dominant image per slide.
- Store: white utility card, square product crop on top, name and price below in body size, one buy action per card.
- Editorial: vista opener with one headline and at most one action, then long leads in a centred column. The opener is a photographic vista — a full-bleed product photograph with one headline and at most one action.
- Flyer: one A4 sheet, real internal padding so no text touches a frame edge, one claim, one dominant image, figure or price at display size in the footer rule.
- Website: full-width hero image, hero plus three sections plus footer, hierarchy carried by size and weight, centred container with flush-left body, leads, captions and prices.
- Bento grid: many features on one page, tiles sized by importance, one claim per tile, specs as small number posters, never table rows. Tiles index; they do not prove: each claim is proved in a following unit or carries its own figure.

## Variations

One break per unit. A dark turn: one whole unit on a near-black field, with a complete foreground palette on that ground. An oversized numeral: one number at display size, label beneath, the number is the claim, not decoration.

## Do's and Don'ts

Do: one product per tile, one claim per unit, live text, blue only by role, a reduced-motion version as the same static sequence. Don't: text baked into images, bullet walls, a second accent colour, a gradient wallpaper, a shadow on a card, weight 500, a single blue variable for link, CTA and focus.

## Tokens

Authored for this fictional world at S = 1000; radius sets size, the contour is continuous corner. Product-image colours and hero gradients are source imagery, not additional action colours.

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
  shoulderExtent: 1.52866
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
Pieces: quiet-hour (Keynote), graphite (Store), aluminium (Editorial), each made from this file alone. Subject is fictional; no Apple product, photograph, logo or font file is used. Tokens are authored for this world, not measured from the brand.
