# Lumen · Apple

A home-audio house in Apple's own language: one object, one claim, one light.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are px at S = 1000, S the format's short side, and scale with it; each is a floor for how far the format is read from, never a ceiling. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath; form names are the maker's, never set on the page. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple, the gallery — Set every unit as one lit field: the lead stands in the light, everything else waits in the ground; never a second light, never a page that reads as documentation.

World: Lumen's products, launches, shop and stories, on any surface. Every piece keeps the light field, the change of ground between units and one claim per unit; each brings its own lead — an object, a figure, a word — and its reader's task. A subject with no object to show lights its proof instead: an interface, a number, a material.

Method:
1. Name the one thing this unit is about; it is the only thing lit.
2. Place the light, falling from the upper left with the lead at its brightest, then set the claim in the calm the light leaves.
3. Turn the ground where the story turns — white, parchment, near-black — never two units in a row at one volume.
4. Let the shop and the reference go dense under the same light, never a brighter one.

Amplitude: Full on covers, turns and the close; reduced on buying, measurement and sources, where the light dims but never leaves.

Anti-reference: A SaaS landing page: a centred slogan, three icon cards, a gradient button.

## Images

Renders of Lumen's fictional objects, made for the piece and declared once. The object is modelled — key light from the upper left, falloff, a specular edge, one contact shadow `rgba(0,0,0,.22) 3px 5px 30px` — on a field that matches its ground or bleeds. On a cover it stands half the frame or more, silhouette whole, scaled from its source and never cropped to fit. Without an object, the lit thing is the proof at the same scale. No Apple or other brand product, photograph, mark, system font file or apple.com element.

## Layout

Grid system: Gallery field — one lit field per unit keeps lead, claim and light on one axis in any format.

Twelve tracks from W × H: margin max(5% W, 6% S), gutter 1.25% W, an 8 px module. The light's centre sits on a track intersection in the upper two-thirds; the lead and the headline share track edges; unused tracks stay ground. Headline, line and actions are one group, the lead stands at least five modules apart; gaps are measured between ink. Formats: on a 1600 × 900 slide, critical content stays inside the central 84%, the slide title at least 90 px and body at least 33; a scrolling page reads the tokens as given at a 1440 px viewport, body never below 17 px; a shop subdivides the field into peer cards on hairlines.

## Typography

- The system face through `-apple-system, system-ui`; Inter stands in for it alone, display tracking a further −0.01 em. Chinese in Noto Sans SC at the same role size, a space between scripts (`text-autospace`), line-end punctuation trimmed (`text-spacing-trim`), product names unbroken.
- Display 80 / 600, the largest type after the lead; heading 56 / 600; lead 24 / 300 at large sizes only; body 17 / 400; label 14; fine 12. Never 500; 700 only as emphasis; tabular figures when compared.
- A headline is one short claim; colour, when any, falls on its core word.

## Colors

Ground: Apple's white, parchment and near-black.
- **canvas** `#ffffff` the gallery; **panel** `#f5f5f7` a quiet unit; **dark** `#272729` a turn or photographic void. Consecutive grounds differ at thumbnail.
- **ink** `#1d1d1f` and **muted** `#6e6e73` read on light; **onDark** white on dark.
- Blue in its roles: **action** and **focus** `#0071e3`, **link** `#0066cc` on light, **darkLink** `#2997ff` on dark, **onAction** white on action.
- **hairline** `#d2d2d7` separates rows and outlines shop cards; on dark, white at low alpha.
- The light is the ground's own tone lifted, never a hue; colour beyond these comes from the product, one per unit.

## Shapes

**The device: the light field.** One radial falloff per unit, centred on the lead, radius 0.9–1.4 S, lifting the ground by one visible step toward white. It enters from the upper left; the lead's shadow falls away from it. It moves, grows or tightens with the lead; it never doubles, never sits behind text alone, never takes a hue, never becomes a wallpaper.

Full-bleed fields are square; shop cards 18, tools 8, actions and chips full pills. Every nonzero radius, pills included, takes Apple's continuous corner, copied, never derived; `border-radius`, `rect rx` and superellipses are other curves. A page built with Folio inlines `continuous-corner.js` and marks each box `data-cc="R"`. Anything else draws one of the two paths below, in units of R, with `transform="translate(x y) scale(R)"` and `vector-effect="non-scaling-stroke"`, filling in A = W ÷ R − 3.05732 and B = H ÷ R − 3.05732. R is at most half the short side, a box or a pill, never between; inner R = max(0, outer R − gap); fill, stroke, clip and focus ring share one path.

A box, both sides at least 3.06 R:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .23692 .07491 .457 .07491 .89717 v{B} c0 .44017 0 .66025 -.07491 .89717 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.23692 -.07491 -.457 -.07491 -.89717 v-{B} c0 -.44017 0 -.66025 .07491 -.89717 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

A pill, R = H ÷ 2:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .18851 .07491 .32851 .07491 .36851 c0 .04 0 .18 -.07491 .36851 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.18851 -.07491 -.32851 -.07491 -.36851 c0 -.04 0 -.18 .07491 -.36851 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

## Forms

- **Cover:** the lead lit at half the frame or more; headline in the calm above or beside it; two actions at most.
- **Statement:** one sentence at display size on a quiet ground, the light on its core word.
- **Exhibit:** the object or proof alone in the light; a caption beneath says what it proves.
- **Data:** one figure at display size is the lit thing, its label beneath; compared figures share a baseline, the decisive one in action blue.
- **Sequence and comparison:** peers share one crop, one scale and one light angle; the light steps across them in reading order.
- **Collection:** white cards on parchment, one crop, name and price flush left, choices as pills, the buy action fixed beside the running price; only the chosen card is lit.
- **Reference and close:** dense rows on parchment; the close is near-black, one claim, one action.

## Variations

- **Dark turn:** one unit on near-black where the story turns, the light at its strongest; once per sequence.
- **Vista:** a full-bleed photograph replaces the object, its own light standing in for the field; one headline, one action.

## Do's and Don'ts

- **Look before delivering:** the light must read at thumbnail; a second light, a lead outside it, type below the ramp, or two adjacent units at one volume are faults.
- **Floors:** facts verbatim and live; renders declared once per piece, in the fine print; every pair in Tokens holds its contrast.
- **Test:** cover the name and pour in new content: the lit field, the turning grounds and one claim per unit still say Lumen; with colour removed, each unit still has one lead.
- **Caricature:** frosted glass everywhere, a gradient wallpaper, blue on everything, a pill for every sentence.

## Tokens

Authored for this fictional world at S = 1000. 

```yaml
colors:
  canvas: "#ffffff"
  panel: "#f5f5f7"
  dark: "#272729"
  ink: "#1d1d1f"
  muted: "#6e6e73"
  action: "#0071e3"
  focus: "#0071e3"
  link: "#0066cc"
  darkLink: "#2997ff"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
typography:
  display: { fontFamily: "-apple-system, system-ui, Inter, Noto Sans SC, sans-serif", fontSize: 80, fontWeight: 600, lineHeight: 1.05 }
  heading: { fontFamily: "-apple-system, system-ui, Inter, Noto Sans SC, sans-serif", fontSize: 56, fontWeight: 600, lineHeight: 1.08 }
  lead: { fontFamily: "-apple-system, system-ui, Inter, Noto Sans SC, sans-serif", fontSize: 24, fontWeight: 300, lineHeight: 1.5 }
  body: { fontFamily: "-apple-system, system-ui, Inter, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.47 }
  label: { fontFamily: "-apple-system, system-ui, Inter, Noto Sans SC, sans-serif", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  fine: { fontFamily: "-apple-system, system-ui, Inter, Noto Sans SC, sans-serif", fontSize: 12, fontWeight: 400, lineHeight: 1.45 }
spacing:
  unit: 8
  grid: 12
  margin: "max(5% W, 6% S)"
  gutter: "1.25% W"
  cardInset: 24
rounded:
  control: 8
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
  link-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.link}" }
  darkLink-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.darkLink}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-07.
Pieces: quiet-hour (Keynote), graphite (Store), aluminium (Editorial), each made from an earlier version of this file, each made from an earlier version of this file. Lumen and its objects are fictional; no Apple product, photograph, logo, font file or site asset is used. Changes after the lock: rewritten around the world's device; the pieces predate it.
