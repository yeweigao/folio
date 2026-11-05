# Volt, a small electric car · Apple + Showroom, Tesla hand

A visual world for a fictional small electric car, not a real Tesla product: one photograph, one message, one price per screen, and a configurator that never leaves the screen. Dialect: Showroom, governing hand Tesla. Surfaces shown: Keynote slide, Store card, Editorial opener; Bento grid as a variation for a range unit only.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts. The photograph proves the claim; the price stays visible.

## Overview

Apple as base, Showroom as dialect, Tesla as governing hand — Compose one full-viewport object photograph with price and options at the decision point; never tile a single-object hero or hide the configurator behind atmosphere.

World: Volt, a small electric car, its range, its price, its options, its configurator, across a launch deck, a configurator page and a story opener. Keep Apple's single-accent discipline and one lead per screen; let Tesla's philosophy govern the look — full-viewport photograph, normal tracking, two weights only, small square buttons, one electric blue for the primary action only, price and configurator always visible.

Method: Separate the content into a claim, its visible evidence and a decision or lookup task. Build the proof field before setting the labels; select Keynote, Store or Editorial structure by the reader's task, then recompose the reading axis and crop for the actual format.

Amplitude: full on covers, heroes and vistas; reduced on Store, reference and specification units.

Anti-reference: a dealer page: the object in a card grid under a discount banner.

## Images

Full-viewport cinematic photographs of the car, one per screen, silhouette intact, material readable. No card grid pretending to be a showroom, no chrome competing with the photograph. Car photographs are generated stand-ins, not a real manufacturer's photographs, and are labelled as such. Crop: cover claim sits in a calm light zone (sky or light ground), never over a dark bumper or windshield, and is shortened until it reads over light ground.

## Layout

Grid system: Gallery field — derive the proof field and one reading axis from W × H; Store subdivides that field into equal peers, Editorial joins it to a reading column, and Keynote assigns one claim to each slide.

One full-viewport screen per message, scrolling to the next screen rather than stacking sections on one page. Slide field 16:9, one thesis per slide, photograph full-bleed with live title in the calm zone. Store field: configurator with price, options and blue primary action always visible while the photograph changes. Editorial field: one centred column opening with a full-bleed photograph, then long leads with the price present but quiet. Text sits at least 11.34 inside its shape; a title clears its descenders before anything below it; a number group sits mid-frame, number, label and context spaced down. Containers may centre; body, leads, captions, card names and prices stay flush left, ragged right; only hero, vista and cover headlines centre.

## Typography

A display face and a text face with normal letter-spacing at every size — the explicit break with Apple's negative tracking. Only two weights: a medium weight for heroes, a regular weight for interface text. Most interface text is small; heroes are restrained, never heavy.

Concrete type for this fictional world: Inter for display, Inter for body and labels; pair Chinese with Noto Serif SC for serif display and Noto Sans SC for sans roles. Open-source substitutes, not the brand's own faces.

## Colors

Neutral grounds — dark carbon, graphite, pewter, light ash — with one electric blue for primary calls to action only, never as a field, never as decoration, never beside a second hue. No gradients, no shadows, no borders as decoration. The only chrome is a frosted nav on scroll.

Concrete field roles: canvas is carbon, panel graphite and dark the hero polarity; ink, muted and onDark are light reading colours. Hairline is reserved for a functional option divider. Action is electric blue for the primary action only, with onAction text. Keep body and secondary actions neutral. Reading text uses only the pairs in Tokens. Accent: electric blue replaces every Apple blue role.

## Shapes

Every nonzero radius takes Apple's continuous corner; square forms stay square. One corner, inward from the corner point in units of R: `M 0 1.52866 C 0 1.08849 0 .86841 .07491 .63149 C .16906 .37282 .37282 .16906 .63149 .07491 C .86841 0 1.08849 0 1.52866 0`. R is at most half the shorter side; a side shorter than 3.05732R shortens its shoulder to half the side, toward the native saturated form (first cubic 0 1, 0 .96, 0 .82). Build it natively (`.continuous`), as this path in SVG, canvas, clip or a slide freeform, or in Figma at 60% smoothing; never `border-radius`, `rect rx`, a preset or a superellipse. Fill, stroke and media clip share one path; nested corners share centres, inner R = max(0, outer R − gap).

Buttons are small squares, never pill. Primary in electric blue, secondary as frosted or ghost treatments. No shadowed cards, no gradient wash, no bordered panels as decoration.

## Forms

- Keynote: one thesis per slide, one full-bleed photograph per slide, live title in the calm zone.
- Store: configurator — price, options and blue primary action always visible, photograph changing behind them.
- Editorial: full-bleed photograph opener, then long leads; price present but quiet, never the headline. The opener is a photographic vista — a full-bleed car photograph with one headline and at most one action.
- Flyer: one A4 sheet, real internal padding so no text touches a frame edge, one claim, one dominant image, figure or price at display size in the footer rule.
- Website: full-width hero image, hero plus three sections plus footer, hierarchy carried by size and weight, centred container with flush-left body, leads, captions and prices.
- Bento grid: range units only — many Volt variants on one page, one object and one price per tile, each tile with its own photograph. Bento never visits a single-object hero unit. Tiles index; they do not prove: each claim is proved in a following unit or carries its own figure; a range tile's price is its check, not its proof of range.

## Variations

One break per unit. A configurator turn: the photograph changes while price, options and action stay fixed. A subtraction turn: remove everything that does not change the photograph, the message or the price.

## Do's and Don'ts

Do: one photograph and one message per screen, normal tracking, price and configurator always visible, one electric blue for action only, frosted nav only. Don't: a pill button, tight tracking, a heavy headline, a gradient wash, a shadowed card, a price hidden until checkout, three messages stacked on one screen, a second accent colour.

## Tokens

Authored for this fictional world at S = 1000; radius sets size, the contour is continuous corner. Product-image colours and hero gradients are source imagery, not additional action colours.

```yaml
colors:
  canvas: "#171a20"
  panel: "#30343b"
  dark: "#171a20"
  ink: "#f5f5f7"
  muted: "#d2d4d8"
  action: "#1559b7"
  onAction: "#ffffff"
  onDark: "#f5f5f7"
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
  small: 0
  control: 0
  card: 0
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
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-05.
Pieces: per-charge (Keynote), configure (Store), one-road (Editorial), each made from this file alone. Subject is fictional; no Tesla product, photograph, logo or font file is used. Tokens are authored for this world, not measured from the brand.
