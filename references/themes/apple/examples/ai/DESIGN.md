# Fern · Apple + Claude

A writing assistant in Apple + Claude: warm paper, a serif voice, one hand-drawn stroke under the word that matters.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are px at S = 1000, S the format's short side, and scale with it; each is a floor for how far the format is read from, never a ceiling. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath; form names are the maker's, never set on the page. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Claude style — Make every unit read like a page someone cared about: warm paper, a serif claim, one hand-drawn stroke under its core word, the writing itself as proof; never a cool gradient, never a robot.

World: Fern's assistant, plans, launches and essays, on any surface. Every piece keeps the warm paper, the serif voice and the hand stroke; each brings its own claim and a readable piece of writing — a draft, a reply, a margin note — as its proof.

Method:
1. Find the claim's core word: the one the reader must not miss.
2. Set the claim in the serif and draw the stroke under that word.
3. Prove it with writing, readable: a draft beside its edit, a reply, a note.
4. Let the dark product surface carry anything technical; the paper carries the rest.

Amplitude: Full on covers and turns; reduced in pricing and reference, where the stroke may be absent.

Anti-reference: The generic AI page: a cool gradient, a glowing orb, a robot.

## Images

No photograph. The proof is writing set live on paper or on the dark product surface, readable at viewing size, its crop the text interior only; declared once as illustrative. On a cover the proof takes half the frame or more. No Anthropic or other brand mark.

## Layout

Grid system: Page field — a reading column and a proof column share the baseline, like a manuscript and its margin.

Twelve tracks from W × H: margin max(5% W, 6% S), gutter 1.25% W, an 8 px module. The claim spans seven tracks, the proof five; on narrow formats the proof follows the claim. Paper never tints a second time behind text. Formats: on a 1600 × 900 slide, critical content stays inside the central 84%, the slide title at least 90 px and body at least 33; a scrolling page reads the tokens as given at a 1440 px viewport, body never below 17 px; a shop subdivides the field into peer cards on hairlines.

## Typography

- Newsreader for display, heading and lead; Source Sans 3 for body and labels; Noto Serif SC and Noto Sans SC for Chinese in the same roles.
- Display 80 / 400; heading 56 / 400; lead 28 / 400; body 17 / 400; label 14; fine 12.
- Sentence case; the serif never bolds; emphasis is the stroke, not weight.

## Colors

Ground: Claude's tinted cream, the brand's signature.
- **canvas** `#f8f3e8` the paper; **panel** `#fffaf2` a lifted sheet, visibly lighter at thumbnail; **dark** `#302e2b` the product surface.
- **ink** `#272520`, **muted** `#635e56`; **onDark** white.
- **action**, **link** and **focus** `#ad4937` terracotta, the stroke's colour and the one action; **darkLink** `#ef9a87` on dark; **onAction** white.
- **hairline** `#d2d2d7` between reference rows only.

## Shapes

**The device: the hand stroke.** One terracotta stroke, drawn as a single tapered path, under the headline's core word: length 1.05× the word, thickness 0.06 em rising to 0.1 em at its centre, a slight upward lift at the right end. One per unit, under one word, never under a whole line, never a straight rule, never in body text or on a button.

Product surfaces and cards 18; actions full pills; tools 8. Every nonzero radius, pills included, takes Apple's continuous corner, copied, never derived; `border-radius`, `rect rx` and superellipses are other curves. A page built with Folio inlines `continuous-corner.js` and marks each box `data-cc="R"`. Anything else draws one of the two paths below, in units of R, with `transform="translate(x y) scale(R)"` and `vector-effect="non-scaling-stroke"`, filling in A = W ÷ R − 3.05732 and B = H ÷ R − 3.05732. R is at most half the short side, a box or a pill, never between; inner R = max(0, outer R − gap); fill, stroke, clip and focus ring share one path.

A box, both sides at least 3.06 R:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .23692 .07491 .457 .07491 .89717 v{B} c0 .44017 0 .66025 -.07491 .89717 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.23692 -.07491 -.457 -.07491 -.89717 v-{B} c0 -.44017 0 -.66025 .07491 -.89717 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

A pill, R = H ÷ 2:

```
M1.52866 0 h{A} c.44017 0 .66025 0 .89717 .07491 c.25867 .09415 .46243 .29791 .55658 .55658 c.07491 .18851 .07491 .32851 .07491 .36851 c0 .04 0 .18 -.07491 .36851 c-.09415 .25867 -.29791 .46243 -.55658 .55658 c-.23692 .07491 -.457 .07491 -.89717 .07491 h-{A} c-.44017 0 -.66025 0 -.89717 -.07491 c-.25867 -.09415 -.46243 -.29791 -.55658 -.55658 c-.07491 -.18851 -.07491 -.32851 -.07491 -.36851 c0 -.04 0 -.18 .07491 -.36851 c.09415 -.25867 .29791 -.46243 .55658 -.55658 c.23692 -.07491 .457 -.07491 .89717 -.07491z
```

## Forms

- **Cover:** the serif claim with its stroke; the writing proof at half the frame or more.
- **Statement:** one serif sentence at display size, the stroke under its core word.
- **Exhibit:** a draft and its revision side by side, the change readable.
- **Data:** one figure in the serif at display size, its label in sans beneath.
- **Sequence and comparison:** versions of one text in order; plans on one baseline.
- **Collection:** prompts or uses as sheets on paper, each one sentence and one sample.
- **Reference and close:** dense sans rows on a lifted sheet; the close is one serif line and one action.

## Variations

- **Dark surface turn:** one unit on the product surface, the stroke in darkLink; once per sequence.
- **Margin turn:** one unit where notes run in a narrow margin beside the text they annotate.

## Do's and Don'ts

- **Look before delivering:** the stroke must read as drawn at thumbnail; a straight underline, two strokes, a cool page, or writing too small to read are faults.
- **Floors:** facts verbatim and live; renders declared once per piece, in the fine print; every pair in Tokens holds its contrast.
- **Test:** cover the names and pour in new content: warm paper, the serif claim and one hand stroke still say Fern.
- **Caricature:** a glowing orb as the page; a blue-violet gradient; a robot.

## Tokens

Authored for this fictional world at S = 1000. 

```yaml
colors:
  canvas: "#f8f3e8"
  panel: "#fffaf2"
  dark: "#302e2b"
  ink: "#272520"
  muted: "#635e56"
  action: "#ad4937"
  link: "#ad4937"
  focus: "#ad4937"
  darkLink: "#ef9a87"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
typography:
  display: { fontFamily: "Newsreader, Noto Serif SC, serif", fontSize: 80, fontWeight: 400, lineHeight: 1.05 }
  heading: { fontFamily: "Newsreader, Noto Serif SC, serif", fontSize: 56, fontWeight: 400, lineHeight: 1.1 }
  lead: { fontFamily: "Newsreader, Noto Serif SC, serif", fontSize: 28, fontWeight: 400, lineHeight: 1.45 }
  body: { fontFamily: "Source Sans 3, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.55 }
  label: { fontFamily: "Source Sans 3, Noto Sans SC, sans-serif", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  fine: { fontFamily: "Source Sans 3, Noto Sans SC, sans-serif", fontSize: 12, fontWeight: 400, lineHeight: 1.5 }
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
  action-on-canvas: { backgroundColor: "{colors.canvas}", textColor: "{colors.action}" }
  action-on-panel: { backgroundColor: "{colors.panel}", textColor: "{colors.action}" }
  darkLink-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.darkLink}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-07.
Pieces: deleted-sentence (Keynote), word-allowance (Store), draft-and-final (Editorial), each made from an earlier version of this file, each made from an earlier version of this file. Fern and every text shown are fictional; no Anthropic product, mark or font file is used. Changes after the lock: rewritten around the world's device; the pieces predate it.
