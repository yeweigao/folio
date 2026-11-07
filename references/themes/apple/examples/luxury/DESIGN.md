# Atelier · Apple + Hermès, Luxury

Atelier's world: a leather house whose craft is the proof.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview
Apple + Hermès style — Make one leather object carry the page, then show the material and craft that prove its claim; never borrow another house's mark, pattern or photograph.
World: A fictional leather house across launch, shopping and workshop stories. Every piece keeps one product as the lead, a restrained serif voice and craft as evidence; each brings a different material decision or buying question. Translate a new subject by choosing the single construction detail that makes its claim checkable; the object stays visible when the crop moves close.
Method: Begin with the whole silhouette and the use the reader is considering. Find the material operation that changes durability, feel or construction, then draw or photograph that detail at a scale it can be judged. Keep a close crop only if its caption restores the whole object and the detail explains the claim. The order of reading is object, craft, quiet price or next action. Use a disclosed diagram when a real craft photograph is unavailable; do not present its texture as documentary proof.
Amplitude: Full on the object and one craft detail; reduced on prices, labels and supporting notes.
Anti-reference: Gold accents, glowing outlines and spaced serif capitals over a stock photograph.

## Images
Use only cleared photographs or generated explanatory artwork for this fictional house. The current example pieces are illustrative SVG renders, captioned Illustrative render, not a photograph; they depict construction and material, not a real bag or real workshop. A cover shows a complete object at gallery scale or one unmistakable detail; the crop preserves seam direction and the relation of stitch to edge. An editorial vista may meet the trim; a construction or product drawing sits inset when its labels need room. Keep text live and outside busy material. Scale source art uniformly and credit real source material beside the figure. On a cover the object or its craft detail takes half the frame or more.

## Layout
Grid system: Gallery field — the product or material proof occupies the largest field; labels share an axis.
Derive a 12-column construction from W × H with outer margin max(5%W, 0.06S) and gutter margin/4. The object takes the largest span; title and caption repeat one edge. In Bento, true product variants share equal spans, one image scale and one price baseline; a lead variant gets a larger field only when the brief sets a real priority. Editorial uses one centered column capped at 980 px, flush-left body and an inset caption measure. Keep a close detail beside the sentence it proves. Prices sit below the product name and remain quieter than it. Empty tracks stay calm; do not fill them with ornament.

## Typography
Use Cormorant Garamond for Latin display with Noto Serif SC as the Chinese display pair; use Inter with Noto Sans SC for body, labels and prices. These open-source Google Fonts approximate an editorial house voice; no Hermès or Apple files. At S = 1000: display 72 px / 400 / 1.05; section head 52 / 400 / 1.08; lead 28 / 300 / 1.35; body 17 / 400 / 1.55; product name 21 / 600 / 1.3; price 17 / 400 / 1.4; label 14 / 400 / 1.4; caption 12 / 400 / 1.5. Use tabular numerals for dimensions and prices; right-align them in reference rows. Serif leads the house; sans reads its apparatus. Chinese and Latin stay matched in size and baseline. On slides the Keynote floors hold: slide title at least 0.1 S, body at least 0.037 S.

## Colors

Ground: Hermès white, its warm panel the house's paper; orange is the one accent. Use white, warm ivory and ink as fields; leather, wood and metal tones come from the object or its disclosed render. leatherLight and leatherMid describe the illustrated hide, leatherDark carries its edge and shadow, and wood marks the workshop surface. Hairline separates rows. Hermès orange is the only interface accent, replacing Apple blue in links, actions, focus and dark-ground links. It marks one action or one meaningful material callout; never use orange as a full field, gradient or second system. Muted text remains legible on white and ivory; dark image fields get a complete white foreground palette. No gold.

## Shapes
Use square, full-bleed fields and the Apple continuous corner for nonzero radii: M 0 1.52866 C 0 1.08849 0 .86841 .07491 .63149 C .16906 .37282 .37282 .16906 .63149 .07491 C .86841 0 1.08849 0 1.52866 0. Build natively or through the shared continuous-corner.js asset with one path for fill, stroke and clip; no CSS radius, rect rx or preset curve. R ≤ half the short side; nested R = max(0, outer R − gap). Store cards use R = 18 px at S = 1000, actions are pills, and article fields are sharp. No shadow on cards; the object may cast one grounded shadow only.

## Forms
- Keynote: one claim and one product or craft proof, live title clear of the image; one detail may fill the frame at a real turn. Keep price quiet and secondary.
- Bento: genuine product variants share one crop, scale, label axis and quiet price; vary tile span only for real importance. One tile carries one claim and is proved in a following unit or by a checkable figure.
- Editorial: one full-bleed material or workshop vista with one headline and at most one action, then a single reading column. Leads are 24 px / 300 / 1.5 and body 17 px / 400 / 1.47 at web size; figures and source sit by the detail they explain. Price remains smaller than the product name.

## Variations
At one craft turn, replace the whole object with one close detail and a caption naming the whole it came from. Keep its crop legible and the object or construction relationship recoverable. One orange action may mark a second turn; never add another accent field.

## Do's and Don'ts

Floors: facts match each brief exactly; declare every illustration; maintain 4.5:1 text contrast (3:1 for large type); keep reading text live and at its declared size floor for the intended viewing distance; make static output complete as a still; recompose each format instead of scaling a layout; use only original or licensed assets.

Render check: the seam, grain, hardware or join named by the claim is sharp enough to inspect, and its caption identifies the whole object it came from.

Test: Cover orange; the page still reads as one crafted object with evidence. Change the house; this construction would need a different hand.

Caricature: softened white surroundings, one vivid orange accent and a playful drawn moment frame a pristine leather object whose construction cannot be inspected.

## Tokens
All values are authored for this fictional world at S = 1000. Orange is Hermès' one accent; leather and metal tones belong to the illustrative object.

```yaml
colors:
  canvas: "#ffffff"
  panel: "#f7f3eb"
  dark: "#24211d"
  ink: "#24211d"
  muted: "#67615a"
  mutedDark: "#c4bcb2"
  action: "#a74b00"
  link: "#a74b00"
  focus: "#a74b00"
  darkLink: "#ffc28a"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
  leather: "#d8c8ad"
  leatherLight: "#e9e0cf"
  leatherMid: "#c1b29a"
  leatherDark: "#857359"
  wood: "#dbd4c7"
  metal: "#b6b4ad"
typography:
  display: { fontFamily: "Cormorant Garamond, Noto Serif SC, serif", fontSize: 72, fontWeight: 400, lineHeight: 1.05 }
  heading: { fontFamily: "Cormorant Garamond, Noto Serif SC, serif", fontSize: 52, fontWeight: 400, lineHeight: 1.08 }
  lead: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 28, fontWeight: 300, lineHeight: 1.35 }
  body: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.55 }
  product: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 21, fontWeight: 600, lineHeight: 1.3 }
  price: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.4 }
  label: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  caption: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 12, fontWeight: 400, lineHeight: 1.5 }
spacing:
  unit: 8
  pair: 16
  group: 24
  section: 64
  objectInset: 80
  cardInset: 24
rounded:
  card: 18
  control: 12
  action: "pill"
corners:
  contour: "continuous corner"
  shoulderExtent: 1.52866
  innerRadius: "max(0, outerRadius - gap)"
pairs:
  ink-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}" }
  ink-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.ink}" }
  muted-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.muted}" }
  muted-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.muted}" }
  mutedDark-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.mutedDark}" }
  onDark-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.onDark}" }
  onAction-on-action: { backgroundColor: "{colors.action}", textColor: "{colors.onAction}" }
  action-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.action}" }
  link-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.link}" }
  darkLink-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.darkLink}" }
```

## Record
Folio version: 1.1.0. Template version: 14. Date: 2026-11-07.
Pieces: the-making (Keynote), the-range (Bento), the-workshop (Editorial), each made from this file alone. Subject is fictional; no Hermès product, photograph, mark, pattern or font file is used. Changes after the lock: none.
