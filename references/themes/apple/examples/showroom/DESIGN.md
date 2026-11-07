# Volt · Apple + Tesla

A small electric car range in Apple + Tesla: the frame full of the object, the title at the top, the pair at the foot.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are px at S = 1000, S the format's short side, and scale with it; each is a floor for how far the format is read from, never a ceiling. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath; form names are the maker's, never set on the page. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Tesla style — Fill every frame with the object, set the title at its top and the pair at its foot; never a card grid, never chrome over the object, never a price kept for the end.

World: Volt's range, configurator, launches and journeys, on any surface. Every piece keeps the full frame, the title at the top and the pair at the foot; each brings its own object view and its two facts or actions.

Method:
1. Choose the one view of the object this unit needs and give it the whole frame.
2. Find the calm band at the top of that view; the title and one line sit there, centred.
3. Set the pair at the foot: two actions, or on a slide two facts.
4. Keep the price in the pair wherever the unit sells.

Amplitude: Full on every frame; the reference and configurator go denser, never smaller in their object.

Anti-reference: A dealer page: the object in a card grid under a discount banner.

## Images

Renders of Volt's fictional vehicles, modelled — key light, paint falloff, glass reflection, a contact shadow — at the largest scale the frame allows, silhouette whole on a cover; declared once. A night showroom ground; the object brings the light. No Tesla vehicle, photograph or mark.

## Layout

Grid system: Full frame — the object owns the field; type keeps to two bands, top and foot.

Twelve tracks from W × H: margin max(5% W, 6% S), an 8 px module. The title band is the top 22% of the frame, the pair band the bottom 14%; the object owns everything between and may run under both. Type never enters the object's middle. Formats: on a 1600 × 900 slide, critical content stays inside the central 84%, the slide title at least 90 px and body at least 33; a scrolling page reads the tokens as given at a 1440 px viewport, body never below 17 px; a shop subdivides the field into peer cards on hairlines.

## Typography

- Montserrat, the nearest open face to Tesla's geometric sans, for every role; Chinese in Noto Sans SC.
- Display 64 / 600 at normal tracking; heading 44 / 600; lead 28 / 400; body 17 / 400; label 14; caption 12; figure 144 / 600 for a single number.
- Two weights only; tracking stays normal, an explicit break with Apple.

## Colors

Ground: carbon, the night showroom this world chose; the object brings the light.
- **canvas** and **dark** `#171a20` carbon; **panel** `#30343b` graphite for the configurator.
- **ink** `#f5f5f7`, **muted** and **mutedDark** `#d2d4d8`, **onDark** `#f5f5f7`; **link** `#f5f5f7`.
- **action** and **focus** `#1559b7`, the primary of the pair only; **onAction** white.
- **pewter** `#5a6068` secondary vehicle tones; **vehicleBody** `#4a505a`, **vehicleGlass** `#262b32`, **vehicleHighlight** `#a9afb8` the render's own paint and glass.
- **hairline** `#6c737c` divides configurator rows.

## Shapes

**The device: the pair at the foot.** Two equal rectangular buttons, side by side and centred in the bottom band, 56 px tall at S = 1000, each at most 2.5 modules wide of text padding; the primary in action blue, the second outlined in ink. Above the object the title and one line sit centred in the top band. On a slide the pair holds two facts set in the same rectangles; in the configurator it holds the running price and the order. The pair never moves to a side, never becomes a pill, never multiplies.

Radius zero for every control and field; the vehicle alone is curved.

## Forms

- **Cover:** the full frame, title and line at the top, the pair at the foot.
- **Statement:** one message on a frame of the object in motion.
- **Exhibit:** one view — side, rear, interior — filling the frame, the pair naming what it shows.
- **Data:** one figure at 144 / 600 in the title band, its unit beside it; the pair carries the condition.
- **Sequence and comparison:** frames in order, one view each; models compared at one scale and one angle, a pair under each.
- **Collection:** the configurator: the object large, options as rows on graphite, the price and order in the pair.
- **Reference and close:** dense rows on graphite; the close is one frame and one pair.

## Variations

- **Interior turn:** one frame from inside the car, the pair over the dashboard, once per sequence.
- **Day frame:** one full-bleed daylight photograph-like frame, the bands unchanged.

## Do's and Don'ts

- **Look before delivering:** the object must fill the frame at thumbnail; a pill, type across the object's middle, a hidden price on a selling unit or three messages in one frame are faults.
- **Floors:** facts verbatim and live; renders declared once per piece, in the fine print; every pair in Tokens holds its contrast.
- **Test:** cover the names and pour in new content: full frames, a title band and a centred pair at the foot still say Volt.
- **Caricature:** a card grid posing as a showroom; chrome over the object; a gradient wash.

## Tokens

Authored for this fictional world at S = 1000. 

```yaml
colors:
  canvas: "#171a20"
  panel: "#30343b"
  dark: "#171a20"
  ink: "#f5f5f7"
  muted: "#d2d4d8"
  mutedDark: "#d2d4d8"
  pewter: "#5a6068"
  vehicleBody: "#4a505a"
  vehicleGlass: "#262b32"
  vehicleHighlight: "#a9afb8"
  action: "#1559b7"
  focus: "#1559b7"
  link: "#f5f5f7"
  onAction: "#ffffff"
  onDark: "#f5f5f7"
  hairline: "#6c737c"
typography:
  display: { fontFamily: "Montserrat, Noto Sans SC, sans-serif", fontSize: 64, fontWeight: 600, lineHeight: 1.08 }
  heading: { fontFamily: "Montserrat, Noto Sans SC, sans-serif", fontSize: 44, fontWeight: 600, lineHeight: 1.1 }
  lead: { fontFamily: "Montserrat, Noto Sans SC, sans-serif", fontSize: 28, fontWeight: 400, lineHeight: 1.45 }
  body: { fontFamily: "Montserrat, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.5 }
  label: { fontFamily: "Montserrat, Noto Sans SC, sans-serif", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  caption: { fontFamily: "Montserrat, Noto Sans SC, sans-serif", fontSize: 12, fontWeight: 400, lineHeight: 1.5 }
  figure: { fontFamily: "Montserrat, Noto Sans SC, sans-serif", fontSize: 144, fontWeight: 600, lineHeight: 1.0 }
spacing:
  unit: 8
  pair: 16
  group: 24
  section: 64
  imageText: 24
  controlRow: 56
rounded:
  all: 0
corners:
  contour: "continuous corner"
  shoulderExtent: 1.52866
  innerRadius: "max(0, outerRadius - gap)"
pairs:
  ink-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}" }
  muted-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.muted}" }
  ink-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.ink}" }
  muted-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.muted}" }
  mutedDark-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.mutedDark}" }
  onDark-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.onDark}" }
  onAction-on-action: { backgroundColor: "{colors.action}", textColor: "{colors.onAction}" }
  link-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.link}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-07.
Pieces: per-charge (Keynote), configure (Store), one-road (Editorial), each made from an earlier version of this file, each made from an earlier version of this file. Volt and every vehicle, figure and price are fictional; no Tesla product, photograph, logo or font file is used. Changes after the lock: rewritten around the world's device; the pieces predate it.
