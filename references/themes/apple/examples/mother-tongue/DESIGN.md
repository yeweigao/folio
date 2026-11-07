# Lumen · Apple

Lumen's world: a small home speaker as a sculpture on a solid field.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple, mother tongue — make the product or its proof the gallery-scale subject on one solid field, then let a change of ground carry each turn; never reduce the hero until the page reads as documentation.

World: Fictional object-led products and their launch, purchase and material stories. A photographed object leads when its form can be judged; where there is no photograph, a readable interface or a measured figure takes its place at the same scale. Every piece keeps one claim, live text and the object’s identity; each brings the task and proof particular to its reader.

Method: Begin with the product silhouette and the change it makes in use. Choose one view that proves that change, then compose the field around its edge; crop only after the object is large enough to lead. Keep the object, its claim and one supporting action on a shared reading axis. Quiet material is an intentional ground, not an empty slot. Follow the sequence from claim to proof to decision.

Amplitude: Full for the cover and one later turn; quieter for buying, measurement and source lines.

Anti-reference: A SaaS landing page with a centred slogan, three icon cards and a gradient button.

## Images

Use a photographed or rendered fictional object made for the piece; credit and label a render as illustrative. No Apple or real brand product, photograph, logo, system font file or apple.com interface element may enter. The hero meets the trim as a full-bleed field or sits as a large inset object; on a cover it occupies at least half the frame including its surrounding field. Preserve the full silhouette unless a detail is the declared proof. Scale uniformly; crop to the object’s contour, never stretch it. In Store, repeat one shared product crop across genuine peers. In Editorial, the opening vista may bleed, while proof figures and material views sit within the reading column. Keep all type live, in the calm area the image leaves.

## Layout

Grid system: Gallery field — it keeps the object, claim and proof in one composed field while the reading axis survives changes of format.

Derive a 12-track grid from W × H: side margin is max(5% W, 6% S), gutter is 1.25% W, and track width is the remaining measure divided by 12. Align title, object bounds, caption and action to shared track edges. Use an 8 px module at S = 1000; group internal gaps in 1, 2, 3 or 5 modules. At every text-to-image boundary, leave at least two modules between visible glyph bounds and the image; measure ink, not text boxes. The image field takes the largest contiguous span and unused tracks remain air. Keynote uses the 16:9 field with critical content inside the central 84%. Store uses the same tracks for a product gallery, choice controls and a fixed purchase row; cards live only here. Editorial uses a centred measure no wider than 82% W or 65 characters, with a full-bleed vista followed by a flush-left reading column. Recompose when W:H changes; never shrink a layout to fit.

## Typography

Use the platform system face through -apple-system and system-ui, followed by Inter, Noto Sans SC and sans-serif; ship no Apple face. At S = 1000 set launch display at 80 / 600 / 1.05, section display at 56 / 600 / 1.08, editorial lead at 24 / 300 / 1.5, body at 17 / 400 / 1.47, label at 14 / 400 / 1.4 and source at 12 / 400 / 1.45. The product leads the cover, the claim is the largest type after it, and each level differs by visible scale or weight. Keep display tracking at −0.01 em on web only; native tracking follows the face. Use Noto Sans SC at the same role size for Chinese, with 1/8–1/4 em between scripts; break Chinese by phrase, keep product names unbroken and pull line-end punctuation back optically. Use tabular numerals for comparisons. On slides the Keynote floors hold: slide title at least 0.1 S, body at least 0.037 S.

## Colors

Ground: Apple's white, parchment and near-black. White is the gallery ground; parchment #f5f5f7 separates a quiet field; near-black is reserved for a product or photographic void. Ink #1d1d1f carries reading text, muted #6e6e73 carries secondary text, and hairline #d2d2d7 separates functional rows and outlines Store cards, never decorating. Apple blue has separate roles: link #0066cc on light grounds, action and focus #0071e3, and link #2997ff on dark grounds. A product may bring its own color; no second interface accent appears. White on action and dark, ink or muted on their declared light grounds only.

## Shapes

Use square full-bleed fields. Every nonzero corner uses the continuous contour, built from the shared continuous-corner.js helper or its path: M 0 1.52866 C 0 1.08849 0 .86841 .07491 .63149 C .16906 .37282 .37282 .16906 .63149 .07491 C .86841 0 1.08849 0 1.52866 0. Set R no larger than half the short side; shorten the shoulder when a side is under 3.05732R. Store cards use R = 18 at S = 1000; actions and choice chips are pills, small tools use R = 8. Inner curves share centres with inner R = max(0, outer R − gap). No card shadow; one soft shadow may ground a rendered product, rgba(0,0,0,.22) at 3 px 5 px 30 px.

## Forms

- Keynote: one thesis and one large product view per slide; keep live type in a calm zone and the exhibit inside the central field. Never shrink a web tile onto a slide.
- Store: white cards on parchment with a 1 px hairline and continuous R = 18; one object crop per card at a shared scale, name and price flush left below, choices as pills, and one buy action fixed beside the running price. Never sell with a gallery tile.
- Editorial: one full-bleed vista with one headline and at most one action, then a generous one-column argument with proof and source beside the claim. Keep the body flush left and end with a dense reference only when the content needs lookup.

## Variations

At a real content turn, permit one complete near-black unit with its own white foreground palette; use it once per sequence. A single figure may take gallery scale when the figure itself is the claim, with its label directly beneath. Keep the object, one claim and the established reading axis.

## Do's and Don'ts

Floors: facts match each brief exactly; declare every illustration; maintain 4.5:1 text contrast (3:1 for large type); keep reading text live and at its declared size floor for the intended viewing distance; make static output complete as a still; recompose each format instead of scaling a layout; use only original or licensed assets.

Render check: hide the object; does the proof still make its claim checkable at the same scale? Hide the proof; does the object still show what the claim is about?

Test: follow the object’s silhouette, claim and proof across each field change; the turn should clarify the same product rather than start a second story.

Apple test: cover the Lumen name—the composition still reads as Apple’s product language, without another dialect; remove colour—each field holds one lead and one claim; thumbnail the set—the volume changes where the story turns.

Caricature: a centered launch slogan, floating glass controls and a tiny white product render on pale grey; the object cannot be identified or judged.

## Tokens

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
Pieces: quiet-hour (Keynote), graphite (Store), aluminium (Editorial). Fictional subject; no Apple product, photograph, logo, font file or site asset is used. Changes after the lock: aligned to the current Apple theme.
