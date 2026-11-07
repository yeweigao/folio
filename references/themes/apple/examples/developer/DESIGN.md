# Relay · Apple + Vercel

Relay's world: a deployment platform proved by its interface at work.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Vercel style — make the deploy tool prove itself with a readable working interface beneath one short action headline, in black and white with one gradient word at hero scale; never lead with a photograph or spread the gradient across the page.

World: A fictional deployment tool and the work people do through it: deploy, inspect, share and choose a team plan. Every piece keeps a readable working interface and one action claim; each brings the workflow or decision it needs to explain.

Method: Begin with the action the reader needs to trust. Build a complete interface state that lets the reader verify that action, then compose the headline and proof as one hierarchy. Use terminal output for process, a live preview for the result and plan comparison for a buying decision. Technical language belongs inside the proof surface only. If a cropped or abstract UI cannot be read, use the whole interface at a larger scale.

Amplitude: Full for an action and a measurable result; reduced for plan comparison and technical notes.

Anti-reference: A generic SaaS page with a dark gradient mesh, glowing grid and floating screenshot cards.

## Images

The hero is a complete fictional interface or terminal; there is no photograph hero. Show real-looking, readable content inside the screen frame, label it as an illustrative render and keep the whole frame visible. Do not use abstract placeholder bars. Use a restrained dark surface for code and dashboard proof, with live captions outside it. On Keynote, the interface sits inset at gallery scale; on Bento, each plan or workflow state uses a shared crop; on Editorial, the preview is a full-width proof figure inside the story, never an arbitrary cut through the browser frame. Scale the source uniformly. No Vercel screenshot, logo or font file is used. On a cover or lead tile the interface takes half the frame or more; the headline sits above it, never beside a thumbnail.

## Layout

Grid system: Gallery field — give the software proof enough uninterrupted area to read, and place the action headline on the same axis.

Derive 12 tracks from W × H: margin max(5% W, 6% S), gutter 1.25% W and equal remaining tracks. Use an 8 px module at S = 1000; align headline, whole interface frame, caption and action to track edges. At every text-to-image boundary, leave at least two modules between visible glyph bounds and the image; measure ink, not text boxes. The headline owns the first reading step and the interface the largest proof field. Keynote uses one thesis in the 16:9 field; keep critical content inside the central 84% and let the interface carry the remainder of the slide. Bento uses unequal tile spans sized by importance; plans that are real peers share crop, baseline and price row, while a specification is a number poster. Editorial opens with one interface vista, then a flush-left column no wider than 82% W or 65 characters; source, code notes and plan details may densify at the close. Recompose on every aspect-ratio change.

## Typography

Voice: Vercel's geometric sans, set in Geist, its own open face. Use Geist for display, body and labels, with Noto Sans SC for Chinese; these are open-source substitutes, not Vercel or Apple font files. Use Geist Mono only inside the proof interface for paths, statuses and timings. At S = 1000 set launch display at 80 / 600 / 1.05, section heading at 56 / 600 / 1.1, lead at 28 / 400 / 1.4, body at 17 / 400 / 1.5, label at 14 / 400 / 1.4 and source at 12 / 400 / 1.5. Display is geometric and sentence case; 600 is the ceiling. Tighten tracking only on the single gradient word; keep the rest of the heading at −0.01 em at large web sizes. Match CJK to Latin by apparent size and baseline, break Chinese at phrase boundaries, and use tabular numerals for durations and prices. On slides the Keynote floors hold: slide title at least 0.1 S, body at least 0.037 S.

## Colors

Ground: Vercel's near-white and black, the brand's signature. Near-white #fafafa and white #ffffff are the only page grounds. Ink #171717 carries body and actions; muted #626262 is secondary text; hairline #d2d2d7 marks functional interface boundaries and divides data rows, never decoration. Dark #171717 appears only inside terminal and dashboard proof, with white text. The one brand event is a two-stop hero-word gradient from #004a9f to #2f8fd8; it appears on one action word at hero scale and nowhere else. Buttons remain solid ink or text links; gradient is never a control, card, badge or wallpaper. Focus is ink on light and white on dark.

## Shapes

Full-bleed fields stay square. Interface and Store cards use Apple’s continuous contour, path M 0 1.52866 C 0 1.08849 0 .86841 .07491 .63149 C .16906 .37282 .37282 .16906 .63149 .07491 C .86841 0 1.08849 0 1.52866 0; the shared continuous-corner.js helper draws it. At S = 1000 use R = 18 for cards, R = 8 for small controls and pill primary actions; inner R = max(0, outer R − gap). Buttons use ink fill or a quiet outline, no blur or colored glow. A hairline belongs to a real interface boundary, never to decoration.

## Forms

- Keynote: state one action in the title and prove it with a full, readable interface state; a measured number may lead if it is the decision’s proof.
- Bento: size features and plans by importance, one claim per tile; use equal cards only for true plan peers, and set specifications as number posters rather than a table.
- Editorial: open with one live preview or terminal field, one headline and at most one action; then explain the workflow in a flush-left column with the relevant proof figure beside the claim.

## Variations

Use one complete dark interface field at a workflow turn, with white foreground and its own readable hierarchy; it does not change the page ground. One single gradient word may lead the cover, one per piece, never repeated in body copy or a button. These are the only departures from black-and-white continuity.

## Do's and Don'ts

Floors: facts match each brief exactly; declare every illustration; maintain 4.5:1 text contrast (3:1 for large type); keep reading text live and at its declared size floor for the intended viewing distance; make static output complete as a still; recompose each format instead of scaling a layout; use only original or licensed assets.

Render check: from the visible interface, a reader can follow one named operation to the status or result that proves it.

Test: Hide Vercel's name; black and white, one gradient word, and a terminal paired with its live preview still read as this hand. Swap in another developer brand; that gradient word and proof pairing should no longer fit unchanged.

Caricature: one hero-scale gradient word repeated across buttons, labels and every section.

## Tokens

```yaml
colors:
  canvas: "#fafafa"
  panel: "#ffffff"
  dark: "#171717"
  ink: "#171717"
  muted: "#626262"
  action: "#171717"
  link: "#171717"
  focus: "#171717"
  focusDark: "#ffffff"
  heroStart: "#004a9f"
  heroEnd: "#2f8fd8"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
typography:
  display: { fontFamily: "Geist, Noto Sans SC, sans-serif", fontSize: 80, fontWeight: 600, lineHeight: 1.05 }
  heading: { fontFamily: "Geist, Noto Sans SC, sans-serif", fontSize: 56, fontWeight: 600, lineHeight: 1.1 }
  lead: { fontFamily: "Geist, Noto Sans SC, sans-serif", fontSize: 28, fontWeight: 400, lineHeight: 1.4 }
  body: { fontFamily: "Geist, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.5 }
  label: { fontFamily: "Geist, Noto Sans SC, sans-serif", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  fine: { fontFamily: "Geist, Noto Sans SC, sans-serif", fontSize: 12, fontWeight: 400, lineHeight: 1.5 }
  technical: { fontFamily: "Geist Mono, Noto Sans SC, monospace", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
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
  heroStart-on-canvas-large: { backgroundColor: "{colors.canvas}", textColor: "{colors.heroStart}" }
  heroEnd-on-canvas-large: { backgroundColor: "{colors.canvas}", textColor: "{colors.heroEnd}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-07.
Pieces: eight-seconds (Keynote), team-plans (Bento), preview-link (Editorial). Fictional platform and interfaces; no Vercel product screenshot, logo or font file is used. Changes after the lock: aligned to the current Apple theme.
