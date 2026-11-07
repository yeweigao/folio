# Fern · Apple + Claude

Fern's world: an AI writing assistant on warm paper, its proof a readable draft.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview

Apple + Claude style — make intelligence tangible by setting a readable conversation or document on warm paper, with the material carrying mood and the product surface checking the claim; never let a gradient, robot or glowing orb stand in for proof.

World: A fictional writing assistant across launch, plan choice and editorial explanation. Intelligence has no photograph, so every piece keeps the warm editorial ground, the living text surface and one claim; each brings the writing task or decision that makes the assistant legible.

Method: Start from the reader’s writing task and name the change the assistant makes. Build that change into a legible document, conversation or count, then place the proof surface against warm paper. The subject determines which surface matters; choose the one that lets a reader verify the claim at a glance. Keep the atmosphere quiet and the reading path claim → surface → consequence. When no interface can check a statement, remove the statement.

Amplitude: Full at the opening claim and one proof turn; reduced for plan comparison and notes.

Anti-reference: A generic AI landing page built from a cool blue gradient, an orb and uncheckable capability claims.

## Images

Use no literal robot or synthetic mood photograph. Render the material as a flat warm field; make the proof a self-contained fictional interface with readable text, not placeholder bars. Declare every mock screen as illustrative and credit any external image if one is later introduced. For Keynote, the document sits inside the trim at gallery scale with a calm title field beside it. In Store, the interface is a repeated inset crop with the screen interior only; keep the same crop across plans. In Editorial, the opening proof surface may meet the trim, but its readable content remains unobscured; the story and figure sit in an inset column. Never stretch a screen or crop its frame. On a cover the product surface leads at half the frame or more, larger than any headline.

## Layout

Grid system: Gallery field — paper gives the interface room to read, while changes between paper and charcoal separate product proof from explanation.

Derive 12 tracks from W × H with side margin max(5% W, 6% S), a 1.25% W gutter and equal remaining tracks. Put the claim and proof on a shared track edge. Use an 8 px module at S = 1000, spacing groups by 1, 2, 3 or 5 modules. At every text-to-image boundary, leave at least two modules between visible glyph bounds and the image; measure ink, not text boxes. The proof surface owns the largest uninterrupted field; the title never overlays readable interface text. In Keynote, assign one thesis to the 16:9 slide and keep critical content inside the central 84%. In Store, keep choices, price and the buy action on one fixed axis; use white cards on parchment only for plans, not for the hero proof. In Editorial, begin with one proof-field vista, then continue in a flush-left column no wider than 82% W or 65 characters; make the footer dense only for source or plan reference.

## Typography

Use Newsreader for display and lead, Source Sans 3 for reading, labels and controls; pair with Noto Serif SC and Noto Sans SC respectively. These are licensed public font substitutes, not Claude or Apple files. At S = 1000 use launch display 80 / 400 / 1.05, section heading 56 / 400 / 1.1, lead 28 / 400 / 1.45, body 17 / 400 / 1.55, label 14 / 400 / 1.4 and fine 12 / 400 / 1.5. Let the serif set the editorial voice; 600 appears only on a product name, selected plan or action. Keep CJK and Latin at matched apparent size and baseline, with a quarter-em script gap; break Chinese at phrase boundaries. Keep code and counters tabular when present; there is no mono body. On slides the Keynote floors hold: slide title at least 0.1 S, body at least 0.037 S.

## Colors

Ground: Claude's tinted cream, the brand's signature. Warm cream #f8f3e8 is the page canvas, soft cream #fffaf2 is the Store card, charcoal #302e2b is the product-surface field and ink #272520 is reading text. Muted #635e56 supports notes; hairline #d2d2d7 separates controls and outlines Store cards, never decorating. Coral-clay #ad4937 marks links, buy actions and focus on light grounds; pale coral #ef9a87 is the dark-ground link. White text belongs on coral or charcoal; ink and muted belong on the two cream grounds. No cool blue or page-wide gradient.

## Shapes

Use full-bleed square fields. Store cards use the Apple continuous contour at R = 18 at S = 1000; controls use R = 8 and selection chips are pills. The contour is M 0 1.52866 C 0 1.08849 0 .86841 .07491 .63149 C .16906 .37282 .37282 .16906 .63149 .07491 C .86841 0 1.08849 0 1.52866 0, drawn by the shared continuous-corner.js helper. Keep inner curves concentric: inner R = max(0, outer R − gap). Use no shadow, badge or decorative border. Product screens remain square within their rounded frame.

## Forms

- Keynote: a short serif thesis with one readable conversation or document surface at gallery scale; keep the claim and interface on separate calm fields, never bake text into an image.
- Store: use white cards on parchment with a 1 px hairline and continuous R = 18; put one allowance and price in each card, repeat the proof surface at the same crop, and keep selection and the buy action visible and stationary.
- Editorial: one full-width proof vista with one headline and at most one action, then a flush-left long read with a large serif lead, readable surface, checkable figure and source.

## Variations

At a genuine change from drafting to editing, allow one charcoal proof field inside the cream page; it must carry a complete readable foreground palette. A long serif lead may open one story section; body copy returns to Source Sans 3 below it. Each variation is used once where the writing changes, not as decoration.

## Do's and Don'ts

Floors: facts match each brief exactly; declare every illustration; maintain 4.5:1 text contrast (3:1 for large type); keep reading text live and at its declared size floor for the intended viewing distance; make static output complete as a still; recompose each format instead of scaling a layout; use only original or licensed assets.

Render check: at the intended viewing size, the draft exposes the exact passage or count that makes the assistant's claim checkable.

Test: Hide Fern's name; warm cream, serif display and coral action still read as Claude's hand, with a readable dark drafting surface beneath. Swap in another assistant; that material and action relationship should no longer fit unchanged.

Caricature: a warm-paper editorial whose dark mock interface cannot show the words that changed.

## Tokens

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
Pieces: deleted-sentence (Keynote), word-allowance (Store), draft-and-final (Editorial). Fictional assistant and interface; no Claude product, screenshot, logo or font file is used. Changes after the lock: aligned to the current Apple theme.
