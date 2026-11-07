# Kit · Apple + Teenage Engineering

Kit's world: a small instrument shown as an exposed, understandable kit.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Teenage Engineering style — Build the exposed kit so its controls, joints and signal colour show how it works; never use the signal as decoration or play to conceal the mechanism.

World: A fictional small instrument and the parts, controls and performance claims that make it usable, across a launch deck, a parts comparison and a long read. Every piece keeps an exposed, understandable mechanism; each brings one function or relationship to prove.

Method: Begin with the action the instrument performs. Draw the housing, joints and controls from that action outward, then decide whether an assembled view or a disassembled view answers the reader's question. Label only the parts needed to understand the mechanism. Use a figure or section for every performance claim; one-lineweight diagrams stay flat and use few node types. The reading path is action, the part that makes it possible, then its check.

Amplitude: Full on the kit and its working parts; reduced on panel labels, comparison measures, price and source.

Anti-reference: a lifestyle hero above a dense specification sheet.

## Images

Use inline vector drawings as declared illustrative stand-ins; no borrowed Teenage Engineering product, image or mark. Show the instrument assembled with its joints visible, or disassembled with every shown part named. Do not draw screw heads, traces or labels that do not explain construction. Caption each object `Illustrative render, not a photograph`. The cover gives the kit at least half the frame; crop to the mechanism, not to empty space. A part that becomes too small to inspect belongs in the proof unit at a larger scale. Keep proportions uniform and all text live.

## Layout

Grid system: Panel field — derive a 12-column field from W × H with side margin m = max(0.05W, 0.06S), gutter = m ÷ 4 and column = (W − 2m − 11 gutters) ÷ 12. Align device sections, labels and claims to these tracks; align schematic parts to a shared component module derived from the instrument, not to the screen. Use an 8 px spacing step at S = 1000, scaled with S. Keynote keeps critical matter inside the central 84% and reserves a calm 25–35% of the image field for live text. Bento gives the primary mechanism the widest span; smaller parts and figures follow its order, not equal-card repetition. Editorial opens with one legible kit vista, then reads down one flush-left column no wider than 980 px. Where the unit holds only a diagram, its edge is cropped close to the working parts.

## Typography

Use Inter for display and reading, Noto Sans SC for Chinese, and Noto Sans Mono only for short panel legends and part codes. No font files are bundled; Google Fonts are OFL 1.1. Labels may be tracked uppercase when they name a physical control, never as decorative kickers. At S = 1000, Keynote slide title at least 0.1 S / 600 / 1.05, body at least 0.037 S / 400 / 1.47, labels 0.026 S / 400 / 1.4 and source 16 / 400; Bento lead 56 / 600 / 1.07; Editorial lead 24 / 300 / 1.5 and body 17 / 400 / 1.47, with a 12 px caption floor. Figures use tabular numerals or a right-aligned column. Chinese and Latin share apparent size and baseline; phrase-break Chinese and keep punctuation with its phrase.

## Colors

Ground: Teenage Engineering's light aluminium grey; the signal colour is the only warmth. Light grey and white are the working ground. Dark charcoal belongs to the mechanism when it improves part separation. One signal orange marks the action and actual signal controls only; all other parts stay material grey, ink or white. Ink and muted carry reading; hairline separates functional rows. Orange is never a section field or a second decorative cue. White is the foreground on charcoal and orange.

## Shapes

The instrument is built from visible planes, fasteners and joints; technical drawings use squared ends, a single stroke weight and consistent nodes. UI forms use small 5, control 8 and card 11 radii; primary actions may be pill-shaped. Full-bleed fields stay square. Every nonzero radius uses Apple's continuous corner, not `border-radius`, `rect rx`, a preset or superellipse. One corner, inward from the corner point in units of R:

```text
M 0 1.52866
C 0 1.08849 0 .86841 .07491 .63149
C .16906 .37282 .37282 .16906 .63149 .07491
C .86841 0 1.08849 0 1.52866 0
```

R is at most half the shorter side; below 3.05732R, shorten the shoulder toward the native saturated form. Fill, stroke and media clip share one path; nested corners share centres, inner R = max(0, outer R − gap). No shadow on cards or labels.

## Forms

- **Keynote:** one kit claim per slide, with the assembled or open mechanism at gallery scale; one decisive signal or figure carries the emphasis.
- **Bento:** one function or part per tile, sized by importance; specification figures share one size and direct label; a tile that needs a legend is a proof slide.
- **Editorial:** one mechanism vista, one headline and at most one action; then a single column with a readable cutaway and checkable figures.

## Variations

A kit turn shows one instrument disassembled where the content shifts from use to construction; label each part shown. A signal turn uses orange on the control that performs the named function and nowhere else in that unit. Keep either variation to one unit per piece.

## Do's and Don'ts

Floors: facts match each brief exactly; declare every illustration; maintain 4.5:1 text contrast (3:1 for large type); keep reading text live and at its declared size floor for the intended viewing distance; make static output complete as a still; recompose each format instead of scaling a layout; use only original or licensed assets.

Render check: trace one control through its joint and part to the operation it performs; the connection must remain clear at normal viewing size.

Test: Cover the assembled kit drawing; do the mechanism and part drawings still reveal how components join and function? Cover their labels; can the geometry still distinguish the parts that matter?

Caricature: a playful detail that conceals operation, or a diagram with every node type at once.

## Tokens

Values are authored for this fictional instrument at S = 1000. Signal orange `#9a4100` replaces Apple blue for the action and control signal; it does not become a field. Inter, Noto Sans SC and Noto Sans Mono are Google Fonts, OFL 1.1; no font file is bundled.

```yaml
colors:
  canvas: "#efefef"
  panel: "#ffffff"
  dark: "#272823"
  ink: "#272823"
  muted: "#62635c"
  action: "#9a4100"
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
  technical: { fontFamily: "Noto Sans Mono, Noto Sans SC, monospace", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  caption: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  fine: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 12, fontWeight: 400, lineHeight: 1.5 }
spacing:
  unit: 8
  textInset: 12
  cardInset: 24
  proofGap: 40
  tileInset: 80
rounded:
  small: 5
  control: 8
  card: 11
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
Pieces: taken-apart (Keynote, 1600 × 900), kit-contents (Bento, 1440 × 1000), signal-states (Editorial, 1200 × 1600); each uses its brief and this DESIGN.md. Subject and figures are fictional; no Teenage Engineering product, image, logo or font file is used. Changes after the lock: none.
