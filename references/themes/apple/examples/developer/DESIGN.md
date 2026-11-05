# Relay, a deployment platform · Apple + Developer, Vercel hand

A visual world for a fictional deployment platform for small teams, not a real Vercel product: the action is deploy, preview, ship, and the proof is the interface working. Dialect: Developer, governing hand Vercel. Forms shown: Keynote slide, Store card, Editorial opener, Flyer sheet, Website page; Bento grid as a variation for a many-feature unit.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts. The interface proves the claim; the headline states the action.

## Overview

Apple as base, Developer as dialect, Vercel as governing hand — Build a readable interface as the proof beneath the claim; reserve gradient for hero-scale verbs and mono for technical labels; never pass abstract placeholder bars off as a working interface.

World: Relay, a platform that takes code to a live URL, its deploy, preview and ship actions, its dashboard, its pricing, across a launch deck, a pricing page and a story opener. Keep Apple's single-accent discipline and one lead per screen; let Vercel's philosophy govern the look — light ground, gradient verbs, mono only for technical labels, interface below the headline as proof.

Method: Separate the content into a claim, its visible evidence and a decision or lookup task. Build the proof field before setting the labels; select Keynote, Store or Editorial structure by the reader's task, then recompose the reading axis and crop for the actual format.

Amplitude: full on covers, heroes and vistas; reduced on Store, reference and specification units.

Anti-reference: the generic SaaS landing: a dark gradient hero, three icon cards, a glowing screenshot.

## Images

No photograph hero. The hero image is a product interface: a deployment dashboard, a preview URL, a build log, shown at rest below the headline, with mono labels naming what it is. Screenshots are fictional interface mockups, never a real product's screenshot, and are labelled as such. Crop: interface crops must show the whole frame — a wide crop that cuts a browser frame is rejected and replaced with a letterboxed whole interface, no stretch, no cut frame.

## Layout

Grid system: Gallery field — derive the proof field and one reading axis from W × H; Store subdivides that field into equal peers, Editorial joins it to a reading column, and Keynote assigns one claim to each slide.

Light ground with dark bands only for code and dashboard sections, returning to light after each band. Hero: large centred headline above two actions, product interface below. Slide field 16:9, critical content inside the central 80%. Store field: white cards on a hairline grid, each card carrying one plan with its interface thumbnail. Editorial field: one centred column, with the interface as a full-width proof figure inside the story. Text sits at least 11.34 inside its shape; a title clears its descenders before anything below it; a number group sits mid-frame, number, label and context spaced down. Containers may centre; body, leads, captions, card names and prices stay flush left, ragged right; only hero, vista and cover headlines centre.

## Typography

A geometric sans for display and body, sentence case, period-terminated headlines, tight tracking on display, ceiling weight 600. A monospace face only for code, technical labels and small technical details — never for headlines, taglines or body. Body regular, highly readable; display light in feel compared with Apple's 600-weight headline, but never thin enough to fail the contrast floor.

Concrete type for this fictional world: Manrope for display, Manrope for body and labels; pair Chinese with Noto Serif SC for serif display and Noto Sans SC for sans roles. Open-source substitutes, not the brand's own faces.

## Colors

Near-white canvas, ink text, black and white as the base, one link blue for links. Colour beyond that comes only as a mesh gradient on headline verbs at hero scale, one gradient per verb, never miniaturised onto a button, card or badge, never as a wallpaper. Dark bands are polarity-flipped depth, never the governing ground.

Roles: canvas the page, panel the card, dark the proof-field polarity, ink and muted the reading colours, onDark and onAction their contrasts, hairline a non-text separator; action is the single neutral action. Reading text uses only the pairs in Tokens. Accent: the chromatic event is the gradient verb; no flat accent joins it.

## Shapes

Every nonzero radius takes Apple's continuous corner; square forms stay square. One corner, inward from the corner point in units of R: `M 0 1.52866 C 0 1.08849 0 .86841 .07491 .63149 C .16906 .37282 .37282 .16906 .63149 .07491 C .86841 0 1.08849 0 1.52866 0`. R is at most half the shorter side; a side shorter than 3.05732R shortens its shoulder to half the side, toward the native saturated form (first cubic 0 1, 0 .96, 0 .82). Build it natively (`.continuous`), as this path in SVG, canvas, clip or a slide freeform, or in Figma at 60% smoothing; never `border-radius`, `rect rx`, a preset or a superellipse. Fill, stroke and media clip share one path; nested corners share centres, inner R = max(0, outer R − gap).

Marketing calls to action are full pill, solid dark primary with an outlined secondary; tool and nav controls are small and square-ish. Cards carry inset hairlines and subtle stacked shadows, never heavy shadow. No coloured section blocks as rhythm.

## Forms

- Keynote: one thesis per slide — one verb per slide where the action is the claim — live text over a calm zone, interface below the headline.
- Store: one plan per card, interface thumbnail on top, name and price below, one buy action per card.
- Editorial: opener with the deployment story, then long leads with interface figures as proof inside the column. The opener is a proof-field vista — a product interface at full-bleed with one headline and at most one action, where the interface itself is the atmosphere.
- Flyer: one A4 sheet, real internal padding so no text touches a frame edge, one claim, one dominant image, figure or price at display size in the footer rule.
- Website: full-width hero image, hero plus three sections plus footer, hierarchy carried by size and weight, centred container with flush-left body, leads, captions and prices.
- Bento grid: many Relay features on one page, tiles sized by importance, one claim per tile, the deploy-preview-ship actions as the wide tiles, specs as small number posters. Tiles index; they do not prove: each claim is proved in a following unit or carries its own figure.

## Variations

One break per unit. A dark band turn: one code or dashboard section on a dark band inside a light page, with a complete foreground palette on that band. A gradient-word turn: one headline verb in gradient, never the whole headline, never a rainbow headline.

## Do's and Don'ts

Do: text-first hero, interface below as proof, mono only for technical labels, gradient verbs at hero scale only, one governing hand per work. Don't: a dark page, a photograph hero, a gradient on a button or card, mono body copy, an all-caps bold headline, a second flat accent.

## Tokens

Authored for this fictional world at S = 1000; radius sets size, the contour is continuous corner. Product-image colours and hero gradients are source imagery, not additional action colours.

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
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-05.
Pieces: eight-seconds (Keynote), team-plans (Bento), preview-link (Editorial), each made from this file alone. Subject is fictional; no Vercel product, screenshot, logo or font file is used. Tokens are authored for this world, not measured from the brand.
