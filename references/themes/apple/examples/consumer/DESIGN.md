# Pebble · Apple + Oura

Pebble's world: a wellness ring shown in the life it measures.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Oura style — make the object legible in the life that gives it meaning, with warm paper, earth color and a quiet shop beneath; never let a specification sheet pose as a life.

World: Fictional personal products whose use is part of the evidence: a wearable, its recorded rhythms, its fit and its buying choices. Every piece keeps the life context, one claim and a checkable product surface; each brings a distinct moment of use or decision.

Method: Start with the use that makes the product matter, then choose the moment, place or record that can show it. Lay a life scene and its object together before the labels; attach facts to a readable interface or measurement rather than letting atmosphere carry them. Keep the shop apparatus neutral and repeatable. Read from the human moment to the object, then to its evidence and action. These examples’ briefs require declared illustrations rather than photographs; keep those drawings illustrative and do not treat them as documentary proof.

Amplitude: Full for a life-led opening; restrained for measurements, fit lookup and purchase controls.

Anti-reference: A template shop filled with stock lifestyle images, stars and promotion badges.

## Images

The Oura dialect calls for photography of an object or place in use. Here, use only the illustrative render or computed chart allowed by each brief; caption it exactly as illustrative and never imply it records a real person or product. A later photo-led piece should use commissioned or licensed photography of the ring worn in the lived moment, not a product on a plinth. For a cover, preserve the object and a quiet text zone in the photograph; never put a text plate over the life. In Bento, draw measurements in a separate exhibit field and hold every peer to the same crop and scale. In Editorial, a proof band or scene may meet the trim; its readable labels stay inset with a caption. Preserve source proportions and disclose source, treatment and credit. On a cover the photograph of the life takes the frame and the ring is the largest object in it.

## Layout

Grid system: Life field — it pairs the object with the event or place that gives its use meaning, then makes measures directly comparable.

Derive a 12-track grid from W × H: margin max(5% W, 6% S), gutter 1.25% W and equal tracks from the remaining width. Use an 8 px module at S = 1000; set repeated facts to shared baselines. At every text-to-image boundary, leave at least two modules between visible glyph bounds and the image; measure ink, not text boxes. The image or proof owns the widest continuous field. In Keynote, use one claim and one recorded measure on the 16:9 canvas, keeping all critical material inside the central 84%. In Store, keep search and choices neutral, show one shared object crop per card and keep price beside the product name. In Bento, size tiles by importance: the lead use or comparison gets the broad span, one-figure specification tiles share one number scale and equal peers share a crop. In Editorial, use a full-bleed opening view followed by a flush-left column no wider than 82% W or 65 characters; dense data belongs in a labeled reference table, not in graphic framing. Recompose for each ratio; do not force a life scene into a data grid.

## Typography

Use Fraunces for high-contrast editorial display and Inter for body, figures and labels; pair with Noto Serif SC and Noto Sans SC. These open-source Google fonts are stand-ins, not Oura files. At S = 1000 set display at 80 / 400 / 1.05, section heading at 56 / 400 / 1.1, reading lead at 28 / 400 / 1.45, body at 17 / 400 / 1.5, label at 14 / 400 / 1.4 and source at 12 / 400 / 1.5. The serif carries the human moment; the sans carries measurements and decisions. Use tabular numerals for timelines, bars and tables; align figures on a shared baseline. Match the apparent size and baseline of Chinese and Latin; set Chinese at 400 with generous leading and break by phrase. The smallest reading text is 17 at S = 1000. On slides the Keynote floors hold: slide title at least 0.1 S, body at least 0.037 S.

## Colors

Ground: Oura's warm paper, the brand's signature. Warm paper #f9f5ed is the ground; oat #eee7db and dark olive #243329 carry changes of context; ink #263028 and muted #5a625b carry text. Mustard, clay and olive may appear in the life or material, never as decorative chrome. The dialect names one decisive action color but not its exact sRGB value; this skeleton infers clay #81523a for action, link and focus, with pale clay #d6a58c on dark ground. This is an illustrative choice, not an Oura color specification. White belongs on action and dark olive; ink and muted belong on paper and oat. Hairline #d2d2d7 separates measures and outlines functional Bento tiles, never decorating. Price/sale and success colors appear only as pricing signals.

## Shapes

Every nonzero radius uses Apple’s continuous corner: M 0 1.52866 C 0 1.08849 0 .86841 .07491 .63149 C .16906 .37282 .37282 .16906 .63149 .07491 C .86841 0 1.08849 0 1.52866 0. Use the shared continuous-corner.js helper, R no larger than half the short side, and inner R = max(0, outer R − gap). Store cards use R = 18 at S = 1000; chips are pills. Bento feature cards use this contour on a generous page radius, with a white gutter between home-promotional tiles. Data bars remain square and begin at zero. No shadow on cards and no decorative border.

## Forms

- Keynote: one human-use claim and its checkable record; the recorded measure can lead only when it is the claim, with its label directly below.
- Store: keep white cards on parchment with a 1 px hairline and continuous R = 18; show one shared product crop, name and price, choices as pills, and a buy action that stays put. No badge competes with the life.
- Bento: use when several facts must be scanned together; size tiles by importance, give each one claim, and set specification numbers on a shared scale. The grid indexes; each claim carries a figure or is proved in a following unit.
- Editorial: one life or proof vista with a single headline and at most one action, followed by a flush-left explanation with its evidence, source and a quiet close.

## Variations

At a real life change, one earth-colored section may interrupt the paper field; use one earth ground and a complete foreground palette. For a reference turn, shift to a denser shared-scale table while keeping the display and reading column unchanged. Each variation serves the change in content, not a repeating color beat.

## Do's and Don'ts

Floors: facts match each brief exactly; declare every illustration; maintain 4.5:1 text contrast (3:1 for large type); keep reading text live and at its declared size floor for the intended viewing distance; make static output complete as a still; recompose each format instead of scaling a layout; use only original or licensed assets.

Render check: at thumbnail size, the frame still identifies who is using the object and what is happening, rather than only its product category.

Test: Cover the brand name; the life, rhythm or stay should still read from image and type. Swap the brand; the page must change in its governing image and typography.

Caricature: a ring on a cream product plinth surrounded by health metrics, with no wearer or moment of use.

## Tokens

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
Pieces: sleep-report (Keynote), ring-sizing (Bento), one-night (Editorial). Fictional product and person; no Oura product, photograph, logo or font file is used. Clay action value is an inference from the dialect’s earth palette. Changes after the lock: aligned to the current Apple theme.
