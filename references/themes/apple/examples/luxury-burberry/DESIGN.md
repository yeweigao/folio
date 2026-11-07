# Highland · Apple + Burberry, Luxury

Highland's world: one coat carrying a British outerwear house through weather.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview
Apple + Burberry style — Make one trench coat carry the house's weather story, then prove its claims in cloth and construction; never use a house mark, check or photograph as borrowed decoration.
World: A fictional British outerwear house across launch, purchase and environmental stories. Every piece keeps one coat, a serif voice and weather or construction as evidence; each brings its own weather question or product decision. Translate a new subject by deciding which weather condition its coat answers, then show proof beside the claim. The price stays present but quiet.
Method: Start with the whole coat in a believable environment. Let actual weather or a visible cloth construction generate the argument; prefer measured conditions over a mood word. Then move from silhouette to the tested detail, preserving enough of the coat to identify the product. A material claim without a detail or stated measurement is removed. Use a fictional house name in serif as the identity; the real knight, check and Burberry wordmark do not transfer.
Amplitude: Full on the coat in its weather; reduced on price and product labels.
Anti-reference: A gold-and-plaid luxury template, a stock portrait and a price bigger than the coat's name.

## Images
Use cleared or generated images of the fictional coat in British rain and wind, never Burberry or Apple imagery or insignia. These example pieces use illustrated weather fields and a coat diagram, labeled Illustrative render, not a photograph; they describe weather or construction rather than document a real coat. Keep the whole coat silhouette on a cover. The rain story may run full bleed, but preserve a calm text zone and do not place live type on the coat's seam. In the shop, keep every coat in a shared crop and at the same scale. Scale source art uniformly; captions stay live, outside the crop. No check pattern is used. On a cover the coat stands half the frame tall or more.

## Layout
Grid system: Weather gallery — the coat and its environment make the lead; construction details align to that same product axis.
Derive 12 tracks from W × H, with margin max(5%W, 0.06S) and gutter margin/4. Keynote uses the same left axis for title, condition and figure; the coat or material proof owns the large opposite field. Store cards sit on the same grid, one coat per card with a shared image slot and aligned price row. Editorial opens with a full-bleed weather field and joins a centered 980 px reading column beneath it; prose stays flush-left and captions align with the tested detail. Change from white to parchment only at a weather/story turn. A new section opens at section scale with its proof, so the page does not fall to one volume. Price, source and measurements stay quiet and findable.

## Typography
Use Cormorant Garamond for serif display and Noto Serif SC for the Chinese display pair; use Inter with Noto Sans SC for body, labels and figures. Open-source Google Fonts only, no Burberry or Apple files. At S = 1000: display 72 px / 400 / 1.05; section head 52 / 400 / 1.08; lead 28 / 300 / 1.35; body 17 / 400 / 1.55; product name 21 / 600 / 1.3; price 17 / 400 / 1.4; label 14 / 400 / 1.4; caption 12 / 400 / 1.5. Figures use tabular numerals, right-aligned. Chinese and Latin share apparent size and baseline; use 300 only for large leads, never fine text. On slides the Keynote floors hold: slide title at least 0.1 S, body at least 0.037 S.

## Colors

Ground: white, with the trench's own honey as the warm panel. Use white and parchment fields, ink for text, and subdued weather neutrals in the render. Hairline marks separators; trim names the neutral detail on the drawn cloth. Saturated knight blue replaces every Apple blue role: link, action, focus and dark-ground link. It appears only on a small action, one decisive measured boundary or a selected store option. It never becomes a full field or a house pattern. Muted labels remain readable; on dark weather fields use white or soft blue-white text. The blue is the only interface accent.

## Shapes
Use sharp full-bleed weather fields and the Apple continuous corner for nonzero radii: M 0 1.52866 C 0 1.08849 0 .86841 .07491 .63149 C .16906 .37282 .37282 .16906 .63149 .07491 C .86841 0 1.08849 0 1.52866 0. Store cards use R = 18 px at S = 1000 and the shared continuous-corner.js helper; actions are pills. Use one path for fill, stroke and media clipping, no CSS radius, preset curve or decorative shadow. Nested R is max(0, outer R − gap), capped at half the short side. A garment or weather illustration may have one contact shadow only.

## Forms
- Keynote: one message and one large coat or material proof; keep a calm zone for live type and use one measurement only when it proves garment response to weather. Price is quiet.
- Store: equal product peers share crop, scale and label order; name then price then one buy action. The buy bar remains fixed, selected state uses the same blue in a 2 px continuous outline.
- Editorial: one full-bleed weather vista with one headline and at most one action, then one reading column. Keep paragraph measure at 65 characters, leads flush-left and evidence close to the stated claim. Close on the implication of the weather record, not another sales slogan.

## Variations
A weather turn may place the coat against one complete dark field. A detail turn may replace the whole object with a readable cloth section; the caption restores the coat and the function of that layer. Keep each turn to one variation, not both at once.

## Do's and Don'ts

Floors: facts match each brief exactly; declare every illustration; maintain 4.5:1 text contrast (3:1 for large type); keep reading text live and at its declared size floor for the intended viewing distance; make static output complete as a still; recompose each format instead of scaling a layout; use only original or licensed assets.

Render check: at thumbnail size, both coat silhouette and weather condition are legible; at full size, the claimed cloth or measurement detail is visibly tied to that coat.

Test: Hide the Burberry name; the restrained serif voice and saturated blue still identify the house without relying on a check or emblem. Substitute another outerwear house; this combination should no longer fit unchanged.

Caricature: knight-blue badges announce the house while the trench's weather use and cloth remain unshown.

## Tokens
All values are authored for the fictional outerwear house at S = 1000. The blue is a visual anchor only; no house mark or photograph is supplied.

```yaml
colors:
  canvas: "#ffffff"
  panel: "#f7f4ed"
  dark: "#202124"
  ink: "#202124"
  muted: "#626269"
  mutedDark: "#c4c6c9"
  action: "#1936c8"
  link: "#1936c8"
  focus: "#1936c8"
  darkLink: "#a8b8ff"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
  weather: "#343941"
  cloth: "#e5e0d7"
  trim: "#8f8c85"
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
Pieces: rain-test (Keynote), trench-series (Store), weather (Editorial), each made from this file alone. Subject is fictional; no Burberry product, photograph, mark, pattern or font file is used. Changes after the lock: none.
