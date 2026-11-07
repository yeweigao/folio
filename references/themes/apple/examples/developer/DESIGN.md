# Relay · Apple + Vercel

A deployment platform in Apple + Vercel: black and white, one gradient verb, the tool at work.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are px at S = 1000, S the format's short side, and scale with it; each is a floor for how far the format is read from, never a ceiling. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath; form names are the maker's, never set on the page. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Vercel style — Make every unit say one action and show it done: the verb carries the gradient, the working interface proves it; never a gradient anywhere else, never a photograph.

World: Relay's tools, launches, pricing, docs and stories, on any surface. Every piece keeps the gradient verb, the black-and-white field and a readable interface as proof; each brings its own action and the screen that shows it done. A subject without an interface proves with its output: a log, a URL, a number.

Method:
1. Find the verb the software performs for this reader and write the claim around it.
2. Build the proof first: an interface at gallery scale, readable, whole.
3. Set the claim above the proof; the verb alone takes the gradient.
4. Keep the technical voice — mono, states, commands — inside the proof.

Amplitude: Full on covers and launches; reduced in docs, pricing and reference, where the verb may stay ink.

Anti-reference: The generic SaaS landing: a dark gradient hero, three icon cards, a glowing screenshot.

## Images

Fictional interfaces drawn live — terminal, deploy log, preview, dashboard — readable at viewing size, the whole frame letterboxed, never cut; declared once. On a cover the proof spans eight tracks and half the frame or more. No photograph hero, no placeholder bars, no real product screenshot or mark.

## Layout

Grid system: Proof field — the claim above, the proof beneath on the same tracks, so every unit reads as action then evidence.

Twelve tracks from W × H: margin max(5% W, 6% S), gutter 1.25% W, an 8 px module. The claim group sits at least five modules above the proof; the proof's left edge is the claim's left edge; dark proof bands run full width. Formats: on a 1600 × 900 slide, critical content stays inside the central 84%, the slide title at least 90 px and body at least 33; a scrolling page reads the tokens as given at a 1440 px viewport, body never below 17 px; a shop subdivides the field into peer cards on hairlines.

## Typography

- Geist, Vercel's own open face, for every role; Geist Mono for the technical voice only; Chinese in Noto Sans SC.
- Display 80 / 600 at −0.03 em; heading 56 / 600; lead 28 / 400; body 17 / 400; label 14; fine 12; technical 14 mono. Sentence case, a full stop.
- Never 500; never mono in headline or body.

## Colors

Ground: Vercel's near-white and black.
- **canvas** `#fafafa` the page; **panel** `#ffffff` cards; **dark** `#171717` proof bands and code.
- **ink** `#171717`, **muted** `#626262`; **onDark** white on dark.
- **action**, **link** and **focus** `#171717`: black pills and black links; **focusDark** white on dark; **onAction** white.
- **heroStart** `#004a9f` to **heroEnd** `#2f8fd8`: the verb's gradient, at display or heading size only.
- **hairline** `#d2d2d7` between rows and around cards.

## Shapes

**The device: the gradient verb.** One word per unit — the claim's verb — filled heroStart to heroEnd, left to right, at display or heading size. Never two words, never a noun, never body, button, panel or background; on a dark band the verb keeps its gradient and the rest turns white. A unit without a headline carries no verb rather than moving it elsewhere.

Proof panels and cards 18; primary actions black full pills; tools 8. Every nonzero radius, pills included, takes Apple's continuous corner, copied, never derived; `border-radius`, `rect rx` and superellipses are other curves. A page built with Folio inlines `continuous-corner.js` and marks each box `data-cc="R"`. Anything else draws one of the two paths below, in units of R, with `transform="translate(x y) scale(R)"` and `vector-effect="non-scaling-stroke"`, filling in A = W ÷ R − 3.05732 and B = H ÷ R − 3.05732. R is at most half the short side, a box or a pill, never between; inner R = max(0, outer R − gap); fill, stroke, clip and focus ring share one path.

A box, both sides at least 3.06 R:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .23692 .07491 .457 .07491 .89717 v{B} c0 .44017 0 .66025 -.07491 .89717 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.23692 -.07491 -.457 -.07491 -.89717 v-{B} c0 -.44017 0 -.66025 .07491 -.89717 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

A pill, R = H ÷ 2:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .18851 .07491 .32851 .07491 .36851 c0 .04 0 .18 -.07491 .36851 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.18851 -.07491 -.32851 -.07491 -.36851 c0 -.04 0 -.18 .07491 -.36851 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

## Forms

- **Cover:** the verb headline over the proof at half the frame or more; two actions, black pill and text link.
- **Statement:** one verb sentence at display size, nothing else.
- **Exhibit:** one interface, whole, its states readable.
- **Data:** one number — a time, a count — at display size in ink, label beneath; never the gradient.
- **Sequence and comparison:** steps as successive states of one interface on one axis; plans as cards on hairlines, the recommended one in black.
- **Collection:** a feature index as tiles, each with one interface crop and one claim.
- **Reference and close:** dense docs rows; the close returns to the verb and one action.

## Variations

- **Dark band:** one unit's proof on a full-width dark band, once per sequence.
- **Terminal turn:** a full-width terminal is the unit, the verb in its first line.

## Do's and Don'ts

- **Look before delivering:** the verb must read as a gradient at thumbnail and stay legible; a second gradient, mono in body, a cut frame or placeholder bars are faults.
- **Floors:** facts verbatim and live; renders declared once per piece, in the fine print; every pair in Tokens holds its contrast.
- **Test:** cover the names and pour in new content: the black-and-white field with one gradient verb over a working interface still says Relay; another deployment product does not fit without a new verb.
- **Caricature:** a gradient mesh wallpaper, a glowing grid, gradient buttons, a dark page.

## Tokens

Authored for this fictional world at S = 1000. 

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
Pieces: eight-seconds (Keynote), team-plans (Bento), preview-link (Editorial), each made from an earlier version of this file, each made from an earlier version of this file. Relay and its interfaces are fictional; no Vercel product screenshot, logo or font file is used. Changes after the lock: rewritten around the world's device; the pieces predate it.
