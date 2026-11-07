# Ledger · Apple + Stripe

Ledger's world: payments for small shops, every amount checkable.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

## Overview
Apple + Stripe style — Make the settlement claim legible on white, then prove it in a readable dark statement; never let a gradient replace the figures or turn the page itself dark.
World: A fictional payments service for small merchants, across launch, fee comparison and money stories. Every piece keeps one governing amount, a white reading field, and a checkable interface or ledger; each brings the decision or sequence its reader needs. Translate new subjects by asking which amount the reader must decide with; keep the statement's calculation visible.
Method: Start from the payment amount, separate fees, refunds and payout, then set the amount with its unit and period. Use a dashboard or statement as the proof surface, not as decoration. Keep every value on a shared decimal edge; retain only calculations that close from their stated inputs. The reading path is claim, statement, arithmetic, action. Quiet copy explains a value but never competes with it.
Amplitude: Full at the claim and payout; reduced in rate labels, sources and footnotes. A number earns display scale only when it is the amount the reader decides with.
Anti-reference: A dark fintech wallpaper with floating cards, glowing charts and a gradient behind every section.

## Images
Drawn Ledger interfaces and tables are explanatory stand-ins, never screenshots of a real service; declare them once per piece, with the figures, as illustrative and fictional. For a launch unit, show the decisive statement at readable scale beside the claim. In a fee comparison, draw one shared scale with direct value labels. In editorial, the flow or statement may meet the top trim as a proof vista; keep the reading column below it inset. Crop to the usable screen interior, preserve rows and labels, and scale the interface uniformly. Use no third-party payment mark or uncredited financial imagery. On a cover the statement or dashboard takes half the frame or more; the governing amount is the largest type.

## Layout
Grid system: Ledger field — amount columns and evidence share a baseline, so figures compare and reconcile.
Derive 12 tracks from W × H; outer margin is max(5% of W, 0.06S), gutter is one quarter of that margin, and each column is the remaining content width divided by 12 after gutters. Keep brand, claim and evidence on repeated vertical axes. In a statement, labels stay left and amounts align to the decimal at right; leave at least half a body line-height of visible ink between a row label and amount, and one body line-height between independent calculation groups and adjacent rules. Measure glyph bounds, not text boxes. In a Bento comparison, the most consequential spread gets the lead field; genuine rate peers share equal tracks and one zero baseline. In a long read, center one column capped at 980 px and 65 Latin characters; body and data share its left edge. Density increases only inside the comparison and statement; air remains around the lead and between sections. On portrait formats, the claim precedes the complete statement; unused width stays paper, not filler.

## Typography

Voice: Stripe's light grotesk, set in Hanken Grotesk, the nearest open face of that lineage. Use Hanken Grotesk with Noto Sans SC as the CJK pair, loaded from Google Fonts; use no Stripe or Apple font files. Display and large figures use 300, body and reading figures 400, labels and decisive totals 600. At S = 1000: display 56 px / 300 / 1.08; section head 38 / 300 / 1.12; lead 28 / 400 / 1.42; body 17 / 400 / 1.55; table value 17 / 400; label 14 / 400; caption 12 / 400. A decisive amount may grow from its span, with tabular numerals, never a decorative KPI. Keep 300 for display scale, not small text. Align decimal points or right edges in every repeated amount column; keep Chinese and Latin on matched baselines. Recompose long titles within the hierarchy. On slides the Keynote floors hold: slide title at least 0.1 S, body at least 0.037 S.

## Colors

Ground: Stripe's white with cool grey-blue bands. Use white canvas and a cool grey-blue panel. Navy ink and the dark navy proof surface carry the interface; muted slate is secondary text. Stripe indigo replaces Apple blue for links, actions, focus and dark-ground links. A restrained blue-to-violet-to-mint wave may sit behind the opening claim only; waveBlue, waveViolet and waveMint form that background field with dark text over it, never a chart fill, button or wallpaper. Hairline separates real rows. Never set a full dark page, second accent, glowing chart or gradient tile.

## Shapes
Use square, full-bleed fields and the Apple continuous corner for any nonzero radius: M 0 1.52866 C 0 1.08849 0 .86841 .07491 .63149 C .16906 .37282 .37282 .16906 .63149 .07491 C .86841 0 1.08849 0 1.52866 0. Build it natively or use the shared continuous-corner.js asset with one path for fill, stroke and media clip; no CSS radius, rect rx, preset curve or shadow. R is at most half the short side, and nested R is max(0, outer R − gap). Store cards use R = 18 px at S = 1000; primary actions are pills. Bento tiles use the same contour, separated by white gutters. Statement panels are the only dark rounded surfaces.

## Forms
- Keynote: one judgment and one amount; the payout statement is large and readable beside it, with live text and one action. The statement's rows align to one decimal edge.
- Bento: unequal tiles by importance; the lead amount takes the widest field, rate peers share one scale and direct labels, the statement arithmetic remains a distinct proof unit. Never turn the mosaic into a disguised table or a wall of equal cards.
- Editorial: one proof vista, then a centered reading column; one lead opens the argument, body is 17 px / 400 / 1.47 at web size, and the source follows the numbers. Keep figure, period and unit adjacent. End with the proved claim, not a new pitch.

## Variations
At a real change in the money story, allow one statement turn: a complete dark navy proof surface against white, with its own foreground palette. The Stripe wave may return behind a later section opener only if that section starts a new argument; otherwise it appears once.

## Do's and Don'ts

Floors: facts match each brief exactly; declare every illustration; maintain 4.5:1 text contrast (3:1 for large type); keep reading text live and at its declared size floor for the intended viewing distance; make static output complete as a still; recompose each format instead of scaling a layout; use only original or licensed assets.

Render check: recompute the displayed settlement from visible amounts, units and period; it reconciles exactly at reading size.

Test: Cover indigo; the figures still line up and the page still reads as Stripe finance. Replace the Stripe signature; the same page should no longer fit.

Caricature: a white Stripe-style balance sheet dressed by a flowing hero wave, with no figure a reader can reconcile.

## Tokens
All values are authored for this fictional world at S = 1000. The wave is limited to a hero background. The house's indigo replaces every Apple blue role.

```yaml
colors:
  canvas: "#ffffff"
  panel: "#f6f9fc"
  dark: "#172b4d"
  ink: "#172b4d"
  muted: "#5c6574"
  mutedDark: "#b9c2d2"
  action: "#5140c9"
  link: "#5140c9"
  focus: "#5140c9"
  darkLink: "#b5adff"
  onAction: "#ffffff"
  onDark: "#ffffff"
  hairline: "#d2d2d7"
  waveBlue: "#dfe9ff"
  waveViolet: "#f0e5ff"
  waveMint: "#e2f6ef"
typography:
  display: { fontFamily: "Hanken Grotesk, Noto Sans SC, sans-serif", fontSize: 56, fontWeight: 300, lineHeight: 1.08 }
  heading: { fontFamily: "Hanken Grotesk, Noto Sans SC, sans-serif", fontSize: 38, fontWeight: 300, lineHeight: 1.12 }
  lead: { fontFamily: "Hanken Grotesk, Noto Sans SC, sans-serif", fontSize: 28, fontWeight: 400, lineHeight: 1.42 }
  body: { fontFamily: "Hanken Grotesk, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.55 }
  value: { fontFamily: "Hanken Grotesk, Noto Sans SC, sans-serif", fontSize: 17, fontWeight: 400, lineHeight: 1.4 }
  label: { fontFamily: "Hanken Grotesk, Noto Sans SC, sans-serif", fontSize: 14, fontWeight: 400, lineHeight: 1.4 }
  caption: { fontFamily: "Hanken Grotesk, Noto Sans SC, sans-serif", fontSize: 12, fontWeight: 400, lineHeight: 1.5 }
spacing:
  unit: 8
  pair: 16
  group: 24
  section: 64
  cardInset: 24
  tileInset: 32
rounded:
  card: 18
  button: "pill"
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
Pieces: quarter-close (Keynote), fee-tiers (Bento), journey (Editorial), each made from this file alone. Subject is fictional; no Stripe product, dashboard, logo or font file is used. Changes after the lock: none.
