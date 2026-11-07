# Volt · Apple + Tesla, Showroom

Volt's world: a small electric car in a night showroom, its price always in view.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview
Apple + Tesla style — Compose one full-viewport object scene with the price at the decision point; never put the vehicle in a card grid or hide its configurator behind atmosphere.
World: A fictional small electric-car range, across launch, configuration and route stories. Every piece keeps the complete vehicle silhouette, one message and a visible price when selling; each brings a different buyer decision or journey. Translate a new subject by locating the object, its material and the proof the buyer can judge. A selling page keeps its live price and options together as the image changes.
Method: Begin with the object's silhouette and the selling question. Choose a camera angle that makes the material and shape legible, then place the short claim in the calmest part of the image. The reader moves from object to message to price and options; where the page sells, price and configuration remain in one stationary decision band. A route story can give the landscape the lead only when the route is the proof and the vehicle remains identifiable. Prefer a shaded illustrative render when no cleared photograph exists; a flat line drawing cannot stand in for the object.
Amplitude: Full on the car and its surrounding field; reduced on controls, price detail and secondary specifications.
Anti-reference: A dealer catalogue of floating car cards under a discount banner.

## Images
Use a generated or supplied image of the fictional object; never use Tesla or Apple product imagery, a real owner's photo, badge, wordmark or vehicle interface. In these examples the vehicle is a layered vector illustration, disclosed with Illustrative render, not a photograph; vehicleBody is the painted shell, vehicleGlass the glazing, and vehicleHighlight the reflected edge. The drawing is a stand-in, not evidence of a real car or performance. Give it at least half of a cover's useful field. Keep the whole silhouette on launch and configure surfaces; on the road story the landscape may meet the trim, but its road and distant car must remain legible. Scale source proportions uniformly. The live headline sits on an unplated calm zone; if contrast fails, move the text or adjust the image field, never add chrome. No content is baked into the image.

## Layout
Grid system: Full viewport field — the object sets the screen's balance; the decision apparatus stays anchored.
Derive a 12-track field from W × H with margin max(5% of W, 0.06S) and gutter margin/4. In landscape, give the vehicle at least 7 tracks and the text or decision group no more than 5; the calm area follows the actual silhouette, not a fixed side rule. In Store, place the rendered object across the first 8 tracks and keep options plus running price in the remaining tracks and bottom action band. The buy band stays at the trim. In editorial, the full-bleed landscape opens the page; the reading column below is centered, capped at 980 px and 65 Latin characters, flush-left. Portrait formats stack image first, choice and price next. Use the same baseline for price, option deltas and action; do not stagger them for rhythm.

## Typography

Voice: Tesla's geometric sans, set in Montserrat, the nearest open face of that lineage. Use Montserrat for Latin and Noto Sans SC for Chinese interface and body; Noto Serif SC may carry a Chinese editorial title only when the bilingual story requires a distinct display voice. Load open-source faces from Google Fonts, no Apple or Tesla file. Use only two weights: 400 for body and labels, 600 for titles and primary action. At S = 1000: display 64 px / 600 / 1.08; heading 44 / 600 / 1.1; lead 28 / 400 / 1.45; body 17 / 400 / 1.5; label 14 / 400 / 1.4; caption 12 / 400 / 1.5; primary figure 144 / 600 / 1.0. Tracking stays normal at all sizes. Use tabular figures for prices, ranges and deltas. The object and amount outrank the slogan. On slides the Keynote floors hold: slide title at least 0.1 S, body at least 0.037 S.

## Colors

Ground: carbon, the night showroom this world chose; the photograph brings the light. Carbon canvas and near-black photo void are fields, graphite is the neutral surface, ash is readable text, pewter labels the vehicle rendering and secondary information. Tesla blue marks the primary action and keyboard focus only; links stay neutral, and blue never fills a field or changes the object rendering. No gradient, decorative border, card shadow or second accent. Hairline appears only between functional option groups.

## Shapes
Tesla's example world uses square corners and no decorative borders or shadows. Every radius is zero. If a future control requires a nonzero corner, use only Apple's continuous corner M 0 1.52866 C 0 1.08849 0 .86841 .07491 .63149 C .16906 .37282 .37282 .16906 .63149 .07491 C .86841 0 1.08849 0 1.52866 0, built with the shared continuous-corner.js helper; fill, stroke and clip share one path. No CSS radius, rect rx, preset curve or shadow. The Tesla render stays flat and carries no cast shadow.

## Forms
- Keynote: one thesis, one full-bleed vehicle render and one live title in a calm zone. Keep the from-price and the range figure visible together; one primary square action may use blue.
- Store: a single-car configurator, not a card collection. Keep the object large, options grouped by decision, selection states neutral, and running price plus reserve action fixed in the decision band. The image may change while the price does not leave.
- Editorial: one road or landscape vista opens the argument, then a single reading column explains route, range and source. The price is quiet and blue is reserved for one primary link only where the page is navigable.

## Variations
One route vista may take the full-bleed landscape for an environmental story. One configuration turn may change the image while holding choice groups, running price and action on the same baseline. No other departure uses a gradient, shadow, or decorative border.

## Do's and Don'ts

Floors: facts match each brief exactly; declare every illustration; maintain 4.5:1 text contrast (3:1 for large type); keep reading text live and at its declared size floor for the intended viewing distance; make static output complete as a still; recompose each format instead of scaling a layout; use only original or licensed assets.

Render check: at first view, the complete vehicle silhouette, live price and next option can be found without relying on a caption or badge.

Test: Remove blue and price; the silhouette and message still read as Tesla showroom. Swap the hand; its calm image-plus-configurator relationship should no longer fit.

Caricature: a cinematic night render whose reflections hide the vehicle's silhouette and whose buyer choices arrive only after checkout.

## Tokens
All values are authored for this fictional world at S = 1000. Vehicle drawing colors represent illustrative paint and glass; the only interface accent is Tesla blue.

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
Pieces: per-charge (Keynote), configure (Store), one-road (Editorial), each made from this file alone. Subject is fictional; no Tesla product, photograph, logo or font file is used. Changes after the lock: none.
