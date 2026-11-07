# Pebble · Apple + Oura

A wellness ring in Apple + Oura: warm paper, an editorial serif, one thin arc around the lead.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are px at S = 1000, S the format's short side, and scale with it; each is a floor for how far the format is read from, never a ceiling. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath; form names are the maker's, never set on the page. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Oura style — Make every unit a calm page with one thin arc around its lead: the ring in the life it measures, the serif in charge, colour from earth; never a spec sheet posing as a life.

World: Pebble's ring, app, shop and stories, on any surface. Every piece keeps the arc, the warm paper and the serif; each brings its own lead — the ring, a figure, a person's moment — and its reader's day.

Method:
1. Choose the lead: the ring, the person wearing it, or the one figure that matters today.
2. Draw the arc around it, opening toward where the eye goes next.
3. Set the serif claim in the arc's open side.
4. Keep the shop quiet beneath: neutral chrome, one action colour.

Amplitude: Full on covers and turns; reduced in the shop and reference.

Anti-reference: A template shop: stock lifestyle photographs, star ratings, promo badges.

## Images

Renders of the fictional ring with modelled metal — key light, specular band, contact shadow — and illustrated life scenes in a calm palette, declared once. On a cover the life takes the frame and the ring is the largest object in it.

## Layout

Grid system: Arc field — the lead and its arc on one centre, the claim in the open side.

Twelve tracks from W × H: margin max(5% W, 6% S), gutter 1.25% W, an 8 px module. The arc's centre sits on a track intersection; its open side faces the claim; dense rows sit on panel, never in the arc. Formats: on a 1600 × 900 slide, critical content stays inside the central 84%, the slide title at least 90 px and body at least 33; a scrolling page reads the tokens as given at a 1440 px viewport, body never below 17 px; a shop subdivides the field into peer cards on hairlines.

## Typography

- Fraunces for display, heading and lead; Inter for body and labels; Noto Serif SC and Noto Sans SC for Chinese.
- Display 80 / 400; heading 56 / 400; lead 28 / 400; body 17 / 400; label 14; fine 12.
- The serif speaks, the sans measures.

## Colors

Ground: Oura's warm paper, the brand's signature.
- **canvas** `#f9f5ed` paper; **panel** `#eee7db` the shop and reference, a step darker; **dark** `#243329` a night unit.
- **ink** `#263028`, **muted** `#5a625b`; **onDark** white.
- **action**, **link** and **focus** `#81523a` clay, the single action colour and the arc's accent; **darkLink** `#d6a58c` on dark; **onAction** white.
- **hairline** `#d2d2d7` in rows only.

## Shapes

**The device: the arc.** One circular arc, stroke 1.5 at S = 1000 in ink, radius 0.42 S around the lead, open by 90° to 150° toward the claim; its two ends square. One per unit; its opening angle varies with the composition, its stroke never thickens, never fills, never becomes a full ring or a progress chart.

Cards 18; actions full pills. Every nonzero radius, pills included, takes Apple's continuous corner, copied, never derived; `border-radius`, `rect rx` and superellipses are other curves. A page built with Folio inlines `continuous-corner.js` and marks each box `data-cc="R"`. Anything else draws one of the two paths below, in units of R, with `transform="translate(x y) scale(R)"` and `vector-effect="non-scaling-stroke"`, filling in A = W ÷ R − 3.05732 and B = H ÷ R − 3.05732. R is at most half the short side, a box or a pill, never between; inner R = max(0, outer R − gap); fill, stroke, clip and focus ring share one path.

A box, both sides at least 3.06 R:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .23692 .07491 .457 .07491 .89717 v{B} c0 .44017 0 .66025 -.07491 .89717 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.23692 -.07491 -.457 -.07491 -.89717 v-{B} c0 -.44017 0 -.66025 .07491 -.89717 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

A pill, R = H ÷ 2:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .18851 .07491 .32851 .07491 .36851 c0 .04 0 .18 -.07491 .36851 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.18851 -.07491 -.32851 -.07491 -.36851 c0 -.04 0 -.18 .07491 -.36851 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

## Forms

- **Cover:** the ring or the person in the arc, the serif claim in its opening.
- **Statement:** one serif sentence with the arc opening onto it.
- **Exhibit:** the ring alone, modelled, in the arc.
- **Data:** one figure at display size in the arc, its label in sans beneath.
- **Sequence and comparison:** a day as moments in one row, each with a small arc; sizes compared at one scale.
- **Collection:** finishes and sizes as quiet cards on panel, the arc on the chosen one.
- **Reference and close:** sans rows on panel; the close is one serif line in an arc.

## Variations

- **Night turn:** one unit on dark, the arc in darkLink; once per sequence.
- **Close-up:** the arc tightens to the ring's own curve at macro scale.

## Do's and Don'ts

- **Look before delivering:** the arc must read at thumbnail and never close; a progress ring, chrome louder than the image, or a cool tech page are faults.
- **Floors:** facts verbatim and live; renders declared once per piece, in the fine print; every pair in Tokens holds its contrast.
- **Test:** cover the names and pour in new content: warm paper, the serif and one open arc still say Pebble.
- **Caricature:** a dashboard of rings and charts; stock wellness photographs.

## Tokens

Authored for this fictional world at S = 1000. 

```yaml
colors:
  canvas: "#f9f5ed"
  panel: "#eee7db"
  dark: "#243329"
  ink: "#263028"
  muted: "#5a625b"
  action: "#81523a"
  link: "#81523a"
  focus: "#81523a"
  darkLink: "#d6a58c"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
typography:
  display: { fontFamily: "Fraunces, Noto Serif SC, serif", fontSize: 80, fontWeight: 400, lineHeight: 1.05 }
  heading: { fontFamily: "Fraunces, Noto Serif SC, serif", fontSize: 56, fontWeight: 400, lineHeight: 1.1 }
  lead: { fontFamily: "Fraunces, Noto Serif SC, serif", fontSize: 28, fontWeight: 400, lineHeight: 1.45 }
  body: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.5 }
  label: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  fine: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 12, fontWeight: 400, lineHeight: 1.5 }
spacing:
  unit: 8
  grid: 12
  margin: "max(5% W, 6% S)"
  gutter: "1.25% W"
  cardInset: 24
rounded:
  card: 18
corners:
  contour: "continuous corner"
  shoulderExtent: 1.52866
  innerRadius: "max(0, outerRadius - gap)"
pairs:
  ink-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}" }
  muted-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.muted}" }
  ink-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.ink}" }
  muted-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.muted}" }
  onDark-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.onDark}" }
  onAction-on-action: { backgroundColor: "{colors.action}", textColor: "{colors.onAction}" }
  action-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.action}" }
  action-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.action}" }
  darkLink-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.darkLink}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-07.
Pieces: sleep-report (Keynote), ring-sizing (Bento), one-night (Editorial), each made from an earlier version of this file, each made from an earlier version of this file. Pebble and every person, figure and price are fictional; no Oura product, photograph, logo or font file is used. Changes after the lock: rewritten around the world's device; the pieces predate it.
