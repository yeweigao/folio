# Mono · Apple + Minimalist, Braun hand

Mono's world: a small radio as a functional system, nothing unnecessary.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Braun + Minimalist — Reduce each product to the control and parts that change its use, then show their relation as a working system; never decorate the interval or make a feature list stand in for the object.

World: Mono is a fictional small-appliance line for objects, controls, repairs, and range choices across a presented slide, a shop comparison, and an explanatory long read. Every piece keeps functional honesty, modular relations, and only the material or signal the use calls for; each brings one claim and its needed evidence.

Method: Start by naming the task the object enables. Lay out its real operation in sequence, then draw the object at a view where controls, parts, and dimensions can be checked. Remove any element that does not change operation or lookup. Choose a side-by-side field for a true comparison, a cutaway when the mechanism explains the claim, and a quiet single-object field when use needs no comparison. Preserve a readable route from claim to control to evidence.

Amplitude: full for the object or the control that carries the claim; reduced for support copy, prices, and reference dimensions.

Anti-reference: a device listing with equal feature tiles, floating spec cards, and ornament used to fill empty space.

## Images

Use newly drawn product elevations, measured diagrams, or declared generated renders; never a real brand product or borrowed image. The hero is a legible product object at gallery scale, not a decorative line drawing. Keep a control's working range, its pointer, and the geometry that makes it operable in frame. For a cutaway, preserve each part's join and label it with live text. Scale drawings uniformly and state when they are not to scale. Place captions outside the drawing. The single colored control marker is a functional signal, not a logo. On a cover the product stands half the frame or more, straight on.

## Layout

Grid system: Functional field — object geometry sets the major spans; a shared baseline makes models and dimensions comparable.

Derive a 12-column field from W × H: margins are max(5% W, 6% S), gutters S/50, and the module S/125. A projected Keynote keeps critical matter inside the outer 8% safe area. Put a front elevation on one side of its spec rows; cutaway labels terminate at their parts, not at arbitrary columns. In a Bento comparison, give the shared-scale silhouettes one baseline and align dimensions, weights, prices, and actions in the same row order. In Editorial, center a column no wider than min(980 px, 82% W) and keep the cutaway with its labels as one proof plate. Equal models share crop, view, scale, and data order. Unused tracks stay empty; they are not filled with decorative controls.

## Typography

Use Inter 400 for display, body, and labels, with Noto Sans SC 400 as its Chinese match. Keep one grotesque voice; 600 is reserved for the decisive figure or selected control. At S = 1000 use display 80/400/1.05, heading 52/400/1.1, lead 24/400/1.45, body 17/400/1.5, label 14/400/1.4, caption 12/400/1.45. Size leads; weight distinguishes a selected figure from its context. Specs and prices use tabular numerals, labels align to a common baseline, and product names stay larger than prices. Break Chinese at phrase boundaries and keep mixed-script spacing consistent. Web reading text stays 16–20 px at 45–75 Latin or 25–35 CJK characters per line. On slides the Keynote floors hold: slide title at least 0.1 S, body at least 0.037 S.

## Colors

Ground: Braun's white and light grey. Use `canvas` and `panel` as neutral surfaces, `ink` for product and reading, `muted` for secondary labels, and `hairline` only for actual divisions. The single `control` color marks the useful pointer or operating state on the object; it is never a color wash or decorative CTA. `action` stays ink, so shop actions do not compete with the control. `dark` is a rare polarity for a decisive figure tile. No gradient or ornamental accent. All text stays in declared contrast pairs.

## Shapes

Construct an object from function: casing first, openings and joints at their working edges, controls at the reach point, labels beside the feature they identify. Do not add a badge, bezel, or control with no operation. Product panels stay square or follow their own manufactured geometry. Where a card or button has a nonzero radius, use Apple's continuous corner: `M 0 1.52866 C 0 1.08849 0 .86841 .07491 .63149 C .16906 .37282 .37282 .16906 .63149 .07491 C .86841 0 1.08849 0 1.52866 0`. The curve uses shoulder extent 1.52866R, R ≤ half the shorter side; nested corners share centres, inner R = max(0, outer R − gap). Use the shared helper at 60% smoothing; never substitute circular `border-radius` for a continuous radius. No shadowed cards.

## Forms

- Keynote: one useful reduction, the object at gallery scale, then only the figures needed to check it; one color appears on the functional control.
- Bento: compare true models on one baseline and scale; a spec poster may state an invariant, and product cards repeat name, size, weight, price, and action in shared order.
- Editorial: open with a large object or mechanism proof, then a flush-left column; the cutaway and its live labels stay together, followed by the implication and a quiet close.

## Variations

At a real change in the argument, allow one complete cutaway plate with labels or one dark number tile. Both keep the mechanism legible and the same single control signal; no variation adds another decorative device.

## Do's and Don'ts

Floors: facts match each brief exactly; declare every illustration; maintain 4.5:1 text contrast (3:1 for large type); keep reading text live and at its declared size floor for the intended viewing distance; make static output complete as a still; recompose each format instead of scaling a layout; use only original or licensed assets.

Render check: at a glance, a control's marked state corresponds to its physical range and operating part; no signal floats free of a function.

Test: Cover the Braun name; the object still reads as functional and material. Add one element back; if use or lookup is no clearer, it does not belong.

Caricature: a retro Braun costume with no working relation between control and part.

## Tokens

Values describe this fictional product line at S = 1000. The warm orange is the one functional control signal; actions remain ink.

```yaml
colors:
  canvas: "#f4f4f4"
  panel: "#ffffff"
  dark: "#242424"
  ink: "#242424"
  muted: "#626262"
  onDark: "#ffffff"
  action: "#242424"
  onAction: "#ffffff"
  control: "#a94725"
  hairline: "#d2d2d7"
typography:
  display: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 80, fontWeight: 400, lineHeight: 1.05 }
  heading: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 52, fontWeight: 400, lineHeight: 1.1 }
  lead: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 24, fontWeight: 400, lineHeight: 1.45 }
  body: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.5 }
  label: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  caption: { fontFamily: "Inter, Noto Sans SC, sans-serif", fontSize: 12, fontWeight: 400, lineHeight: 1.45 }
spacing:
  module: 8
  gutter: 20
  group: 32
  section: 64
  cardInset: 24
rounded:
  card: 18
  control: 0
pairs:
  ink-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.ink}" }
  ink-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.ink}" }
  muted-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.muted}" }
  muted-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.muted}" }
  onDark-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.onDark}" }
  onAction-on-action: { backgroundColor: "{colors.action}", textColor: "{colors.onAction}" }
  control-on-canvas-large: { backgroundColor: "{colors.canvas}", textColor: "{colors.control}" }
  control-on-panel-large: { backgroundColor: "{colors.panel}", textColor: "{colors.control}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-07.
Pieces: one-knob (Keynote), three-models (Bento), inside (Editorial), built from this file alone. Mono and every model, measurement, price, and part are fictional; no Braun product, photograph, logo, or font file is used. Changes after the lock: none.
