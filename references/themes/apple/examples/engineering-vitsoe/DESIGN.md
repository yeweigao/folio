# Shelf, a modular shelving system · Apple + Engineering, Vitsoe hand

A visual world for a fictional modular shelving system, not a real Vitsoe product: one module, every part a whole multiple of it, the system shown assembled and disassembled. Dialect: Engineering, governing hand Vitsoe. Forms shown: Keynote slide, Store card, Editorial opener, Flyer sheet, Website page; Bento grid as a variation for a system unit.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts. Every performance claim carries a figure or a section.

## Overview

Apple as base, Engineering as dialect, Vitsoe as governing hand — Build assembled and disassembled views from one module, then attach dimensions to matching parts; never vary the module to fit a composition.

World: Shelf, a shelving system whose proof is that parts combine without fitting, its module, its parts, its configurations, its price, across a launch deck, a shop page and a story opener. Keep Apple's single-accent discipline and one lead per screen; let Vitsoe's philosophy govern the look — a shelving system where the proof is that parts combine without fitting: one module, every part a whole multiple of it, the system shown assembled and disassembled.

Method: Separate the content into a claim, its visible evidence and a decision or lookup task. Build the proof from the module before setting the labels; select Keynote, Store or Editorial structure by the reader's task, then recompose the reading axis and crop for the actual format.

Amplitude: full on covers, heroes and vistas; reduced on Store, reference and specification units.

Anti-reference: a spec sheet under a lifestyle photograph, beside a rendered explosion.

## Images

No lifestyle mood alone. The hero image is the system: the shelving assembled, or disassembled into its parts laid out on the module grid, with labels naming every part shown. System images are fictional mockups, never a real manufacturer's images, and are labelled as such. Crop: cover slot scope — a right-half cover slot is too narrow for a three-bay system, so the cover shows two complete bays and the full three-bay system must appear on the proof slide; a crop that cuts through uprights or shelves is rejected.

## Layout

Grid system: Module grid — derive all part dimensions from the one construction module, then align the reading and proof fields to it.

Neutral canvas with generous whitespace, one centred axis per unit, the module grid visible as the construction grid, never as wallpaper. Hero: headline with the system below it as proof. Slide field 16:9, critical content inside the central 80%. Store field: white cards on a hairline grid, one part or configuration per card, system thumbnail on top, name and price below. Editorial field: one centred column, with system images and figures as proof inside the story. Text sits at least 11.34 inside its shape; a title clears its descenders before anything below it; a number group sits mid-frame, number, label and context spaced down. Containers may centre; body, leads, captions, card names and prices stay flush left, ragged right; only hero, vista and cover headlines centre.

## Typography

One quiet grotesque sans, regular weights for body, medium weight for display, no display face competing with the system. Use tabular numerals where the renderer supports them; otherwise use a right-aligned figure column, so module dimensions line up across rows, cards and pages.

Concrete type for this fictional world: Inter for display, Inter for body and labels; pair Chinese with Noto Serif SC for serif display and Noto Sans SC for sans roles. Open-source substitutes, not the brand's own faces.

## Colors

Neutral grounds with one accent for calls to action and key highlights only, never as a field, a wash or a background. Colour beyond the accent comes from the diagram's own line and the product's material, never from chrome. No second accent, no gradient.

Roles: canvas the page, panel the card, dark the proof-field polarity, ink and muted the reading colours, onDark and onAction their contrasts, hairline a non-text separator; action is the single action accent. Reading text uses only the pairs in Tokens. Accent: the single accent replaces every Apple blue role.

## Shapes

Every nonzero radius takes Apple's continuous corner; square forms stay square. One corner, inward from the corner point in units of R: `M 0 1.52866 C 0 1.08849 0 .86841 .07491 .63149 C .16906 .37282 .37282 .16906 .63149 .07491 C .86841 0 1.08849 0 1.52866 0`. R is at most half the shorter side; a side shorter than 3.05732R shortens its shoulder to half the side, toward the native saturated form (first cubic 0 1, 0 .96, 0 .82). Build it natively (`.continuous`), as this path in SVG, canvas, clip or a slide freeform, or in Figma at 60% smoothing; never `border-radius`, `rect rx`, a preset or a superellipse. Fill, stroke and media clip share one path; nested corners share centres, inner R = max(0, outer R − gap).

Cards carry hairlines and quiet separation, never heavy shadow. Diagrams use one line weight, squared ends, no decorative stroke. Calls to action are modest rectangles or pills following the card system, never a pill on every control.

## Forms

- Keynote: one thesis per slide; a system slide is one unit, with the system assembled or disassembled as proof, one decisive figure in accent and the rest muted.
- Store: one part or configuration per card, system thumbnail on top, name and price below, one buy action per card; a configurator variation lets the visitor combine parts without fitting.
- Editorial: opener with the system story, then long leads with system images and figures as proof inside the column. The opener is a diagram vista — a system assembled and disassembled at full-bleed with one headline and at most one action, where the system itself is the atmosphere; the diagram must be readable as a diagram, not a rendered explosion.
- Flyer: one A4 sheet, real internal padding so no text touches a frame edge, one claim, one dominant image, figure or price at display size in the footer rule.
- Website: full-width hero image, hero plus three sections plus footer, hierarchy carried by size and weight, centred container with flush-left body, leads, captions and prices.
- Bento grid: a system unit — many Shelf parts on one page, tiles sized by importance, one claim per tile, each tile one part that combines with the others, figures as small number posters with tabular numerals. Tiles index; they do not prove: each claim is proved in a following unit or carries its own figure; a system tile's claim is its part combining with the others.

## Variations

One break per unit. A system turn: one full unit showing the whole system assembled and disassembled, with every part a whole multiple of one module. A module turn: one unit as the module grid itself, with every dimension on that grid and no dimension off it.

## Do's and Don'ts

Do: one module, every part a whole multiple of it, system shown assembled and disassembled, one governing hand per work. Don't: a dimension off the module, a part that fits only one configuration, a system shown only assembled, a second accent colour, a diagram with every node type at once.

## Tokens

Authored for this fictional world at S = 1000; radius sets size, the contour is continuous corner. Product-image colours and hero gradients are source imagery, not additional action colours.

```yaml
colors:
  canvas: "#f8f7f3"
  panel: "#ffffff"
  dark: "#2b302d"
  ink: "#2b302d"
  muted: "#626a64"
  action: "#345c5c"
  onAction: "#ffffff"
  onDark: "#ffffff"
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
Pieces: one-module (Keynote), configurations (Bento), disassembled (Editorial), each made from this file alone. Subject is fictional; no Vitsoe product, image, logo or font file is used. Tokens are authored for this world, not measured from the brand.
