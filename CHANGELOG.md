# Changelog

## 0.4.0 — 2026-10-31 · 师夷长技 (learn from the neighbours)

A borrowing release: Folio kept its grammar and took the mechanisms the
DESIGN.md ecosystem proved elsewhere. Each item names its source.

**Enforcement （借 Google + impeccable + taste-skill)**
- Inspect now runs machines before judgment: Google's `lint` (a hard gate,
  zero warnings) is step one of step 8, and the loop is bounded — failures
  in floor order, top three fixed, at most two rounds, the rest to Gaps.
- New `scripts/folio-check.py`: deterministic gates in impeccable's
  detector spirit — DESIGN.md completeness (versions recorded, focus and
  soft-field tokens present, CJK face in every type stack), component
  contrast recomputed offline, orphan tokens, and export checks (off-token
  colors and faces in .pptx/.html, banned pie/doughnut charts).
- SKILL.md carries `version: 0.4.0`; the DESIGN.md template carries a
  template version, so the Record section's version requirement can
  actually be met.

**Template repairs (from review)**
- Colors gain `soft` and `focus` tokens with their component pairs
  (text-on-soft, muted-on-soft, focus-ring): the theme's four fields each
  carry a palette now, and the web surface's focus token exists.
- Typography tokens use a real CJK/Latin stack (Inter + Source Han Sans
  SC) instead of bare Arial; craft reconciles its three roles with the
  template's four type tokens.
- The template states its example numbers are the slides starting system,
  to be recomputed per surface.
- Directions rule fixed: a dialect direction is judged on the dimensions
  its file replaces, not the ones it keeps.
- Poster table: A4 title cap-height floor corrected to 2.5–5 mm, matching
  its own distance formula.

**Evidence （借 VoltAgent + Google examples)**
- `examples/board-deck/`: a complete locked DESIGN.md (Swiss Brutal board
  deck, full-bleed chart exhibit) with generated previews; passes
  folio-check and Google lint.
- `scripts/preview.py` generates preview.html / preview-dark.html /
  tokens.css from any DESIGN.md (VoltAgent's preview convention).
- `examples/dialects/sampler.html`: the nine dialects as one contact sheet.

**Production & distribution （借 Bergside / Stitch / UI-UX-Pro-Max)**
- `scripts/extract.py` drafts a DESIGN.md from a real .pptx or .html —
  theme colors, used colors/faces/sizes counted — as Critique mode's
  evidence base (design-md-chrome's idea, aimed at PPT, which nobody else
  covers).
- `references/family.md`: master DESIGN.md + per-deliverable Overrides
  (ui-ux-pro-max's Master + Overrides, in Folio's terms); the template
  gains an Overrides section.
- `references/steering.md`: seven named refinement moves in Folio's own
  grammar (impeccable's command vocabulary, kept small).
- `references/manifest.json` maps every file to its role and load moment;
  README adds the one-line `npx skills add yeweigao/folio` install.
- Practice gains a sanctioned light path: small jobs compress the eight
  steps openly and record the compression, instead of skipping silently.

**Not borrowed, on purpose:** brand scraping and renaming (VoltAgent) —
against Folio's facts floor; a palette database (ui-ux-pro-max) — color
comes from the subject; a 30–45 minute loop for every job (taste-skill) —
the bound was borrowed, not the cost; a format fork (Bergside) — Folio
stays lint-compatible with Google's spec.

## 0.4.1 — 2026-10-31 · names at the point of making

Field finding: masters were cited in the theme and recorded in DESIGN.md,
yet the work came out in the generic equivalent — a name in a reference
table or a past-tense citation instructs no one. Names now live where
generation happens.

- **Make (step 7)** gains the invocation discipline: before each unit,
  re-read the cited cells in the theme just in time; write the unit's
  brief first, opening with an invocation — master + work + imperative +
  visual predicates + one ban — renewed per unit. Generated images
  receive the master's name and work verbatim in their prompt.
- **Directions** must name a governing hand per direction: one master or
  programme leading the whole deliverable.
- **Lock / template (v3)**: the Overview carries a Governing hand line in
  instruction voice; Sequence citations carry the evocation bundle
  (master · work: imperative + parameters + ban), because post-lock
  readers no longer open the theme by default. Practice states the
  just-in-time exception to that rule.
- **Inspect** gains the recognition test: with citations covered, would
  the unit be recognised as the governing master's way of working?
  Citing a method and executing its generic equivalent is a failure.
- theme.md's Methods note rewritten: "A name is a handle, not a spell."
- The board-deck example is rewritten to demonstrate the format.

## 0.4.2 — 2026-10-31 · rhythm is decided first

Field finding: the 21 variations were listed, eligible, and almost never
used. The incentives pointed the other way: continuity could be bought
with one vague sentence, a variation attempted badly was a visible
failure while monotony failed nothing, and "turn" was never marked
anywhere, so the rule had no trigger.

- **Lock (step 6)** maps the rhythm before the Sequence's details: every
  unit gets a register (base / turn / pause) as one composition. At a
  marked turn, continuity now costs as much as a variation — its reason
  must name what the rhythm loses. A speaking deliverable of four or
  more units with no variation taken does not lock (reference and
  single-unit work excepted).
- **Template (v4)**: the Sequence gains a Register column, a rhythm-map
  line above the table, and a variation cell that demands name +
  magnitude + keep — or continuity with its rhythm cost.
- **Make (step 7)**: a turn unit's brief gains a second line invoking
  its variation with its magnitude and Keep condition; a turn made
  without its variation has failed its brief.
- **Inspect (step 8)** judges the contact sheet first: all units as
  thumbnails, rhythm before detail; monotony is named there.
- **folio-check C8** enforces the gate mechanically: 4+ units, no
  variation, reference not in the majority → fail.
- The board-deck example demonstrates the format; the theme's Variations
  note now reads: a variation named without its magnitude is a wish.

## 0.5.0 — 2026-10-31 · the signature tier, and the soul wired in

Two decisions frame this release. The thirteen philosophy lines are the
soul of the skill, not its decoration: they are now stated as its
constitution — they outrank every other file, conflicts are recorded,
and every Inspect failure must be named by the line it breaks. And no
master reference images will be added: the masters are reached through
construction, parameters, and tests, not through pictures to imitate.

**Signature tier (the audit's core finding)**
- `references/signature.md`: nine methods lifted out of the Methods
  matrix into recipe cards — graphic scale, grid alphabet, exposed grid,
  Isotype, Becher typology, route line, cut-out, programme series,
  close-up — each with Construction, Parameters, Test, Caricature.
- Lock requires a signature programme (one card, governing the whole
  work) or a recorded "Signature: none — reason"; **folio-check C9**
  enforces it. The theme's Methods section now discloses the two prices.
- Template v5 adds the Signature programme line to the Overview.

**Instruments （制作工具）**
- `scripts/generators/`: isotype.py (equal symbols, remainders cut,
  never shrunk), ledger.py (decimal-aligned, hairline opens, ink rule
  closes), programme.py (a declared cycle, no hand-tuned states) — all
  SVG, stdlib only.
- `scripts/measure.py`: field shares from rendered thumbnails — the
  theme's paper ≥ 50% / accent ≤ 10% grammar is now measurable (Pillow).

**Orphans wired**
- Inspect's judge list now includes the surface's Done means and each
  unit's form "Fails when"; Critique calls `extract.py`; Lock generates
  the preview catalog; folio-check scans exports for the Copy blacklist
  (**E4**) and warns on pictures whose captions it cannot verify (**E5**);
  the preview doubles as the CJK/Latin type proof sheet.

**Calibration & regression**
- `examples/paired/`: one dataset set twice — basic (KPI cards, gradient,
  copy tells; fails E1/E4) vs signature (graphic scale, generated ledger
  and Isotype; passes) — the recognition test's calibration pair.
- `tests/`: three fixed regression briefs; skill changes are judged by
  finished contact sheets, never by the DESIGN.md files.

## 0.5.1 — 2026-10-31 · the dialect master set

`examples/dialects-master/`: one fictional, product-free programme —
"THE GRID", a public lecture evening (three talks, a foyer poster
exhibition; all names, venue, and times illustrative) — set as a poster
in each of the nine dialects at full strength. Content is held word-for-
word still across the nine (`content.md`), so the dialect has nowhere
to hide: the set is the recognition test's reference standard.

Each dialect folder carries its render (`poster.html`), a locked
DESIGN.md (tokens, governing hand, signature line, the dialect's Test
and caricature), and the generated token preview. All nine pass
folio-check against their posters and Google's lint at 0/0 (four token
sets were darkened during the build to hold the contrast floors — the
floors moved the dialects, not the other way round).

Borrowed openly, per the set's README: one content × many systems
(awesome-design-md), named numeric settings beside every render
(taste-skill), the caricature printed next to the example (impeccable),
and a lint-clean spec per example (Google design.md).
Correction (same day): the first 0.5.1 package was announced as lint
0/0 before the lint run had actually finished; it in fact carried
warnings — orphaned dialect tokens (blue/yellow/teal defined but
referenced by no component) and unquoted descriptions containing
colons. Fixed: each extra token is now referenced by a real component
pair (paper-on-blue, ink-on-yellow, paper-on-teal — all passing the
contrast gate), and all descriptions are quoted. Re-verified:
folio-check 9/9 against the posters, Google lint 0 errors / 0 warnings
on all nine. The package was replaced in place.

## 0.5.2 — 2026-10-31 · the blind test

The dialect master set was put to the test its own Lock states: nine
fresh agents, each allowed to read ONLY its one DESIGN.md — no SKILL.md,
no craft, no dialect file, no reference render — rebuilt the posters.
Round 1 of the test (agents could read the whole skill) found the files
determined the system but not the composition, and caught a real defect:
the spacing tokens summed to 1060px on a 900px poster. The nine files
were therefore rebuilt as self-contained briefs — Source facts, the
dialect in full, the binding floors, the signature card in full where
one is used, and a Composition paragraph giving the lead's geometry in
numbers — and round 2 ran against those.

Round 2 verdict: every blind render is recognisably its dialect with
labels covered, and most compositions converge with the references
(Swiss Brutal and Ulm nearly line for line). The agents' INVENTED lists
shrank from whole compositions to furniture: kicker wording, gaps,
label phrasing. Their CONTRADICTIONS lists were the real yield — some
thirty internal inconsistencies (token vs prose sizes, a yellow glyph
below the contrast floor, a route branch drawn after the event it
precedes, facts silently truncated by a build spec, zone arithmetic
that does not close), each now fixed in the files and, where the
reference render shared the fault, in the render: Bauhaus snapped to
its module with a right triangle and a title that clears the date bar,
ma's stack recomputed so every Source fact fits, Ulm's branch moved to
the entry node and its pictograms drawn, Brodovitch's figure given the
front/behind split its signature card demands. All nine pass
folio-check against their posters and Google lint at 0/0.
