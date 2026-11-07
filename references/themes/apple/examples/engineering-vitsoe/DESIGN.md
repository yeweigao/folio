# Shelf · Apple + Vitsoe

Shelf's world: one module and every system it builds.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Vitsoe style — Build the whole system from one physical module and show it assembled and disassembled; never change a part's measure to fit the page.

World: A fictional modular shelving system, its components, combinations and dimensions, across a launch deck, a configuration comparison and an explanatory long read. Every piece keeps one shared module and the proof of how its parts combine; each brings a different system question.

Method: Read the dimensions in the brief and name the smallest repeated construction measure M. Express every part edge and every system span as an integer multiple of M. Compose the assembled view first, then lay out those same parts disassembled on the same grid. Choose the view that answers the question; reject any relationship that requires a non-integer part or a second scale. Keep reading on one axis: claim, whole system, parts, dimensions.

Amplitude: Full on the assembled and disassembled system; reduced on dimensions, options, prices and sources.

Anti-reference: a generic shelving photograph above a list of unrelated dimensions.

## Images

Use a measured vector construction, not a borrowed Vitsoe product, photograph or system drawing. Every drawn system is an illustrative stand-in and is captioned `Illustrative render, not a photograph`. Preserve the same scale across assembled and disassembled views; crop empty margin, never a shelf edge or upright. If the complete system cannot fit in a cover field, show a complete module-sized portion and put the whole assembly on the proof unit. Dimensions, component names and captions stay live; each one identifies the part it measures.

## Layout

Grid system: Module grid — for each drawing, let p = min(available width ÷ system width in M, available height ÷ system height in M); draw one M as p pixels and every component edge at an integer multiple of p. Derive a 12-column reading field from W × H with side margin m = max(0.05W, 0.06S), gutter = m ÷ 4, column = (W − 2m − 11 gutters) ÷ 12; the module grid governs the object, the columns govern text. Share baselines for dimensions and direct labels; keep visible label ink at least half a label line-height clear of measured edges and leader lines, and unrelated callouts one label line-height apart. Measure glyph ink, not text boxes. No box is added just to fill a track. Use an 8 px spacing step at S = 1000, scaled with S.

Keynote keeps critical text inside the central 84%; the system or a complete module portion occupies at least half the slide. Bento assigns the widest tile to the assembled system, with component and number tiles following the reader's comparison. Number tiles share one numeral size and one label position. Editorial opens on the diagram at full bleed, then uses one centred column no wider than 980 px; the column explains the module and names the dimensions at the place they can be checked.

## Typography

Use Inter for display and reading, Noto Sans SC for Chinese; no typeface competes with the system. No binaries are bundled; Inter and Noto Sans SC are Google Fonts, OFL 1.1. Use 600 for the main claim, 400 for body and direct labels. At S = 1000, Keynote slide title at least 0.1 S / 600 / 1.05, body at least 0.037 S / 400 / 1.47, labels 0.026 S / 400 / 1.4 and source 16 / 400; Bento lead 56 / 600 / 1.07; Editorial lead 24 / 300 / 1.5 and body 17 / 400 / 1.47, with a 12 px caption floor. Set all dimensions with tabular numerals or a right-aligned figure column. Match Chinese and Latin apparent size and baseline; phrase-break Chinese and retain punctuation.

## Colors

Ground: Vitsoe's white; colour comes from the shelf's materials. White is the system field; light grey carries quiet separations, charcoal carries a dark turn when contrast is useful. The system itself uses ink, grey and its declared material colours. No chromatic accent is assigned to Vitsoe; actions use neutral ink, never Apple blue. Muted marks secondary dimensions, hairline only the measured divider. Keep labels readable in grayscale.

## Shapes

Shelf parts keep their actual squared construction edges; no radius is applied to a component, module or measured drawing. Bento cards use radius 18, tools 8, and full-bleed fields stay square. Any nonzero radius uses the continuous corner, never `border-radius`, `rect rx`, a preset or superellipse. One corner, inward from the corner point in units of R:

```text
M 0 1.52866
C 0 1.08849 0 .86841 .07491 .63149
C .16906 .37282 .37282 .16906 .63149 .07491
C .86841 0 1.08849 0 1.52866 0
```

R is at most half the shorter side; below 3.05732R, shorten the shoulder toward the native saturated form. Fill, stroke and media clip share one path; nested radii share centres, inner R = max(0, outer R − gap). No shadow on components or cards.

## Forms

- **Keynote:** state one system claim, show the assembly at the largest scale available, and keep one set of dimensions on the same module grid.
- **Bento:** compare one assembly, component or configuration per tile; tile size follows the question, figures share size, each component is shown as part of the whole.
- **Editorial:** let a full-bleed assembled/disassembled diagram open the argument; continue in one column with the module, dimensions and part relationships.

## Variations

A module turn is allowed at the point where component dimensions become the subject: show the construction grid itself and keep every edge on M. An assembly turn is allowed where a comparison resolves into the whole: include both assembled and disassembled views at the same scale. Either turn occupies one unit.

## Do's and Don'ts

Floors: facts match each brief exactly; declare every illustration; maintain 4.5:1 text contrast (3:1 for large type); keep reading text live and at its declared size floor for the intended viewing distance; make static output complete as a still; recompose each format instead of scaling a layout; use only original or licensed assets.

Render check: measure a named part in the assembled and disassembled drawings; it occupies the same integer multiple of M at the same drawn scale.

Test: Hide the dimension labels; can a maker count the repeated module from the part edges? Hide the assembly; can the parts still be recomposed into the same system?

Caricature: a dimension off the module, a part that fits only one configuration, or a system shown only assembled.

## Tokens

Values are authored for this fictional system at S = 1000. Action is neutral ink because the Vitsoe line assigns no chromatic accent; no Apple blue is used. Inter and Noto Sans SC are Google Fonts, OFL 1.1; no font file is bundled.

```yaml
colors:
  canvas: "#ffffff"
  panel: "#ffffff"
  dark: "#2b302d"
  ink: "#2b302d"
  muted: "#626a64"
  action: "#2b302d"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
typography:
  display: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 80, fontWeight: 600, lineHeight: 1.05 }
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
  tool: 8
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
Pieces: one-module (Keynote, 1600 × 900), configurations (Bento, 1440 × 1000), disassembled (Editorial, 1200 × 1600); each uses its brief and this DESIGN.md. System, dimensions and figures are fictional; no Vitsoe product, image, logo or font file is used. Changes after the lock: none.
