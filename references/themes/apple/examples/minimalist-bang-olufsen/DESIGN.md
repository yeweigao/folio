# Sound · Apple + Bang & Olufsen

Sound's world: audio as material sculpture in a quiet room.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Bang & Olufsen style — Build one audio object as a sculpture in a quiet room, then show the material or sound measure that helps a listener judge it; never make a feature list stand in for listening.

World: A fictional minimal audio house and its speakers or listening objects, materials, sound and buying choices, across a launch deck, a shop page and a long read. Every piece keeps the object and its material as the lead; each brings one listening or material question.

Method: Start with what a listener can judge: the product's shape, the material they touch, or the one sound result the brief can substantiate. Build the object in its own geometry, with aluminium, wood or textile treated as material rather than decoration. Choose a quiet room only when it gives the product scale and silence; remove room details that compete. A sound claim needs a stated measure or listening evidence. The path is object, material or sound proof, then the useful choice.

Amplitude: Full on the object; reduced on material notes, names, prices and source lines.

Anti-reference: an empty white page with a thin typeface and no evidence of what the object does.

## Images

Use a declared illustrative product render or a sourced material image made for the brief; never a borrowed Bang & Olufsen product photograph. Each drawn object is captioned `Illustrative render, not a photograph`. Show the whole product at its own proportions and let its material be judged; use a detail crop only to prove a material claim, with a caption naming the whole it came from. The cover product owns at least half the field. A quiet room is atmosphere and must be identified as such. Do not draw a waveform or room scene as evidence for sound; use a checkable, labeled measure when sound is the claim.

## Layout

Grid system: Object field — derive a 12-column field from W × H with side margin m = max(0.05W, 0.06S), gutter = m ÷ 4 and column = (W − 2m − 11 gutters) ÷ 12. Centre the object within the field that belongs to it; align its name, caption and controls to one shared edge. Do not recenter body copy. Use an 8 px spacing step at S = 1000, scaled with S. Keynote keeps critical text inside the central 84% and the product large enough to read from the room; reserve a calm text zone beside it. Store uses white cards on a hairline grid, radius 18, one comparable product crop per card and each name and price directly below. Editorial opens with one quiet-room product vista, then one centred reading column no wider than 980 px; material evidence belongs beside the claim it proves.

## Typography

Use Inter for display and reading, Noto Sans SC for Chinese; one quiet grotesque voice across all roles. No face competes with the object. No files are bundled; Inter and Noto Sans SC are Google Fonts, OFL 1.1. Use 600 for the claim, 400 for names and body, and 300 only for a large quiet lead. At S = 1000, Keynote slide title at least 0.1 S / 400 / 1.05, body at least 0.037 S / 400 / 1.47, labels 0.026 S / 400 / 1.4 and source 16 / 400; Store lead 56 / 600 / 1.07; Editorial lead 24 / 300 / 1.5 and body 17 / 400 / 1.47, with a 12 px caption floor. Use tabular figures when comparing sound measures. Match Chinese and Latin apparent size and baseline; break Chinese at phrase boundaries.

## Colors

Ground: Bang & Olufsen's quiet light grey; aluminium and wood bring the warmth. Aluminium, wood, textile and the quiet room supply the colour. Use warm paper, white and material grey as page grounds; charcoal is one deliberate turn. There is no separate chromatic accent: the action uses neutral ink, and Apple blue is retired. Ink carries reading; muted is for secondary information; hairline separates functional choices only. Keep material colour in the product image, not in decorative interface chrome.

## Shapes

The product keeps its actual geometry; do not round a square product or square a curved one for the layout. Store cards use radius 18, tool controls 8, primary actions and chips are fully rounded; full-bleed fields stay square. Every nonzero radius uses Apple's continuous corner, never `border-radius`, `rect rx`, a preset or superellipse. One corner, inward from the corner point in units of R:

```text
M 0 1.52866
C 0 1.08849 0 .86841 .07491 .63149
C .16906 .37282 .37282 .16906 .63149 .07491
C .86841 0 1.08849 0 1.52866 0
```

R is at most half the shorter side; below 3.05732R, shorten the shoulder toward the native saturated form. Fill, stroke and media clip share one path; nested radii share centres, inner R = max(0, outer R − gap). Use one shadow beneath the product at rest, nowhere else.

## Forms

- **Keynote:** one listening or material claim per slide, one large object, live text in its calm zone, and one checkable sound measure only when the claim needs it.
- **Store:** one object and one price per white card, shared crop and scale for peers, a choice chip only when a buyer must choose material or size, one fixed buy action.
- **Editorial:** one product in a quiet-room vista, one headline and at most one action; then a single flush-left column with material evidence and a cited sound measure where relevant.

## Variations

A quiet-room turn is allowed when the change is from object to listening; keep only the product and one sentence. A material turn is allowed when the surface itself becomes the subject; use one close detail and name what it belongs to. Each variation occupies one unit and returns to the neutral product field.

## Do's and Don'ts

Floors: facts match each brief exactly; declare every illustration; maintain 4.5:1 text contrast (3:1 for large type); keep reading text live and at its declared size floor for the intended viewing distance; make static output complete as a still; recompose each format instead of scaling a layout; use only original or licensed assets.

Render check: at normal display size, the speaker's aluminium, wood or textile remains legible as a distinct material rather than a flat color fill.

Test: Cover Bang & Olufsen's name; aluminium, wood or textile still lead, and each sound claim remains a measure rather than a mood mark. Add one element back; if it competes with listening or clarifies nothing, it does not belong.

Caricature: plastic chrome and a decorative accent overpower the speaker, leaving its sound claim as mood instead of a measure.

## Tokens

Values are authored for this fictional audio house at S = 1000. Action equals neutral ink because this hand has no chromatic accent; no Apple blue is used. Inter and Noto Sans SC are Google Fonts, OFL 1.1; no font file is bundled.

```yaml
colors:
  canvas: "#f3f3f3"
  panel: "#ffffff"
  dark: "#282722"
  ink: "#282722"
  muted: "#636159"
  action: "#282722"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
typography:
  display: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 80, fontWeight: 400, lineHeight: 1.05 }
  slideBody: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 24, fontWeight: 400, lineHeight: 1.47 }
  slideLabel: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 18, fontWeight: 400, lineHeight: 1.4 }
  slideSource: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 16, fontWeight: 400, lineHeight: 1.5 }
  tile: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 56, fontWeight: 600, lineHeight: 1.07 }
  editorialLead: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 24, fontWeight: 300, lineHeight: 1.5 }
  body: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.47 }
  label: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  caption: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  fine: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 12, fontWeight: 400, lineHeight: 1.5 }
spacing:
  unit: 8
  textInset: 12
  cardInset: 24
  proofGap: 40
  tileInset: 80
rounded:
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
  action-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.action}" }
  action-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.action}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-07.
Pieces: quietest-setting (Keynote, 1600 × 900), three-surfaces (Store, 1440 × 1000), one-sheet (Editorial, 1200 × 1600); each uses its brief and this DESIGN.md. Product and figures are fictional; no Bang & Olufsen product, photograph, logo or font file is used. Changes after the lock: none.
