# Aero · Apple + Dyson

Aero's world: an airflow fan proved by its section and its figures.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Dyson style — Build each claim from a readable mechanism section and its measured figure; never substitute lifestyle mood or an unreadable exploded render for proof.

World: A fictional airflow product and the claims its mechanism can support, across a launch deck, a feature comparison and a long read. Every piece keeps the mechanism legible and the claim checkable; each brings one question, one proof and its own reading path.

Method: Start from the part that makes the claim true: airflow, motor or filtration. Choose a section, flat diagram or in-use view whose visible parts explain that cause. Keep diagram line weight and node types consistent; add a figure only when it measures the claim. Reject a view when its arrows or labels cannot be followed without an extra legend. Quiet copy names parts and units; the reader moves from claim to mechanism to figure.

Amplitude: Full on the mechanism and decisive figure; reduced on part labels, prices and sources.

Anti-reference: a product photograph with a list of unconnected specifications.

## Images

Use inline vector diagrams and declared illustrative product renders, never a borrowed Dyson image or an invented documentary photograph. The mechanism is the proof; a product view appears only where its working parts remain visible. Declare drawn objects once per piece: `Illustrative render, not a photograph`. Keep the full mechanism at native proportions and crop only unused source margin. On a cover the mechanism or proof occupies at least half the unit; if the system is too wide, show a named part and place the complete diagram on its proof unit. Keep labels live and captions beside their evidence.

## Layout

Grid system: Gallery field — derive a 12-column field from W × H. Set side margin m = max(0.05W, 0.06S), gutter = m ÷ 4, and column = (W − 2m − 11 gutters) ÷ 12. Share the title, mechanism, labels and source edge that their evidence requires. Equal figures share a baseline; unmatched parts do not get equal boxes. Leave unused tracks open. Use an 8 px base spacing step at S = 1000, scaled with S.

For Keynote, keep critical content inside the central 84%; the cover gives the mechanism a field at least half the slide and a 25–35% calm area for live text. For Bento, use a 12-column grid with one wide lead tile and supporting tiles sized by importance; a specification tile uses one large number, one muted label and one check line. Tiles index claims; proof follows or is carried in the tile. For Editorial, use a full-bleed proof vista followed by one centred reading column no wider than 980 px; the body stays flush left and the footer alone may go dense. Set source, unit and caption beside each figure.

## Typography

Voice: Dyson's Futura-lineage geometric, set in Jost, the nearest open face of that lineage. Use Jost for display, labels and reading; Noto Sans SC for Chinese; Noto Sans Mono only for short part codes when needed. No font file is bundled; Google Fonts sources are OFL 1.1 and fall back to Jost and Noto system families. Use 600 for a claim and 400 for body and labels; 300 is reserved for a large quiet lead. At S = 1000, Keynote slide title at least 0.1 S / 600 / 1.05, body at least 0.037 S / 400 / 1.47, labels 0.026 S / 400 / 1.4 and source 16 / 400; Bento lead 56 / 600 / 1.07; Editorial lead 24 / 300 / 1.5 and body 17 / 400 / 1.47, with a 12 px caption floor. Tabular numerals or a right-aligned figure column keep measurements aligned. CJK and Latin share size and baseline; break Chinese by phrase and keep punctuation inside the measure.

## Colors

Ground: Dyson's white and neutral grey; colour is the machine's own. White and soft neutral are the reading grounds; charcoal is a proof-field polarity, not the page default. Ink carries reading text; muted marks secondary labels and sources; hairline separates actual diagram groups. One Dyson purple marks the action and one decisive airflow path only. White is the foreground on charcoal or the action; purple never becomes a page wash. Keep diagram meaning legible in grayscale and label each flow directly.

## Shapes

Diagram parts use square joins and one line weight. UI controls follow the radius ladder: small 5, tool control 8, card 18, primary actions and chips fully rounded; full-bleed fields stay square. Every nonzero radius uses the continuous corner, not `border-radius`, `rect rx`, a preset or superellipse. One corner, inward from the corner point in units of R:

```text
M 0 1.52866
C 0 1.08849 0 .86841 .07491 .63149
C .16906 .37282 .37282 .16906 .63149 .07491
C .86841 0 1.08849 0 1.52866 0
```

R is at most half the shorter side. If a side is shorter than 3.05732R, shorten the shoulder toward the native saturated form. Use one path for fill, stroke and media clip; nested radii share centres, inner R = max(0, outer R − gap). No decorative shadow; a single shadow may sit beneath the product render only.

## Forms

- **Keynote:** one mechanism claim per slide; a readable section or diagram takes gallery scale, the figure that checks it shares a baseline, all labels remain live.
- **Bento:** one claim per tile, sized by importance; same-size specification numbers, direct labels, no tile that needs a legend or second claim.
- **Editorial:** one mechanism vista, one headline and at most one action; then long leads, a readable diagram and the cited figure in a single column.

## Variations

A section turn is allowed where the argument changes from the product to how it works; make one complete cutaway the lead and keep its labels. A figure turn is allowed where a claim becomes measurable; align the figures and give the decisive one the accent. Each appears once at that content turn.

## Do's and Don'ts

Floors: facts match each brief exactly; declare every illustration; maintain 4.5:1 text contrast (3:1 for large type); keep reading text live and at its declared size floor for the intended viewing distance; make static output complete as a still; recompose each format instead of scaling a layout; use only original or licensed assets.

Render check: follow the labelled flow from inlet through the mechanism to outlet, then match each figure to its measuring station without a legend.

Test: Cover the figures; the section still reveals what moves and where air goes. Cover the section; no performance claim remains unassigned to a mechanism.

Caricature: a fan cutaway crowded with callouts until no single path can be followed from inlet to outlet.

## Tokens

Values are authored for this fictional world at S = 1000. `action` is Dyson purple for one action and one decisive mechanism signal; it replaces Apple blue for this hand. Jost and Noto Sans SC are Google Fonts, OFL 1.1; no font file is bundled.

```yaml
colors:
  canvas: "#f5f5f5"
  panel: "#ffffff"
  dark: "#25272a"
  ink: "#25272a"
  muted: "#62666b"
  action: "#6525a0"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
typography:
  display: { fontFamily: "Jost, Noto Sans SC, sans-serif", fontSize: 80, fontWeight: 600, lineHeight: 1.05 }
  slideBody: { fontFamily: "Jost, Noto Sans SC, sans-serif", fontSize: 24, fontWeight: 400, lineHeight: 1.47 }
  slideLabel: { fontFamily: "Jost, Noto Sans SC, sans-serif", fontSize: 18, fontWeight: 400, lineHeight: 1.4 }
  slideSource: { fontFamily: "Jost, Noto Sans SC, sans-serif", fontSize: 16, fontWeight: 400, lineHeight: 1.5 }
  tile: { fontFamily: "Jost, Noto Sans SC, sans-serif", fontSize: 56, fontWeight: 600, lineHeight: 1.07 }
  editorialLead: { fontFamily: "Jost, Noto Sans SC, sans-serif", fontSize: 24, fontWeight: 300, lineHeight: 1.5 }
  body: { fontFamily: "Jost, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.47 }
  label: { fontFamily: "Jost, Noto Sans SC, sans-serif", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  caption: { fontFamily: "Jost, Noto Sans SC, sans-serif", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  fine: { fontFamily: "Jost, Noto Sans SC, sans-serif", fontSize: 12, fontWeight: 400, lineHeight: 1.5 }
spacing:
  unit: 8
  textInset: 12
  cardInset: 24
  proofGap: 40
  tileInset: 80
rounded:
  small: 5
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
Pieces: airflow-section (Keynote, 1600 × 900), filter-range (Bento, 1440 × 1000), air-path (Editorial, 1200 × 1600); each uses its brief and this DESIGN.md. The product and figures are fictional; no Dyson product, photograph, logo or font file is used. Changes after the lock: none.
