# DESIGN.md

<!-- folio-template-version: 7 -->

One file per deliverable, beside the work, holds every decision, so each unit, later session, or helper makes the same piece without rereading the theme. It follows the open [DESIGN.md](https://github.com/google-labs-code/design.md) format, tokens in YAML front matter and reasons in prose under its sections in order, and adds Folio's sections after them.

- **Drafted at Directions, locked at Lock.** Step 4 writes Overview, Directions, and Gaps; step 6 completes the rest for the chosen direction.
- **It names the subject.** A file that would fit another deliverable is a default.
- **Cite by name, then say how.** Each method cell, variation, and dialect rule appears under its name in the theme, with one line on how this work makes it.
- **The first content line is an Invocation.** The locked file opens, before Overview, with the tested term or master's name, the named work, and the imperative — and that line governs everything below it. Parameters are the discipline: facts, floors, bans, arithmetic; they also carry the work's own inventions (its signature programme above all), which no name can know. A lead of gesture or atmosphere is specified by invocation + visual predicates + one ban, not by coordinates; coordinates are for construction-led leads. The division is empirical (blind tests, v0.5.2–0.5.3): a name buried mid-file loses to checkable numbers at Make, and a bare name without the file drifts facts and breaks floors.
- **Names are written as commands, not records.** The Overview carries a Governing hand line in instruction voice; a Sequence citation a unit will rely on carries its evocation bundle (master, work, imperative, parameters, one ban). After the lock, helpers read this file instead of the theme, so whatever the bundle leaves out is lost.
- **The file changes before the work.** A missing value is added first; a failed unit changes the file, then the unit; changes after the lock go in Record.
- **A supplied DESIGN.md binds** like a brand: keep its values and fill its gaps in place.
- **Run the checks.** `scripts/folio-check.py DESIGN.md` verifies completeness (versions recorded, focus and soft-field tokens present, type faces carry a CJK fallback, every token used, Sequence filled); Google's lint verifies references and contrast.
- **Family work** follows [family](family.md): a master DESIGN.md holds the shared system; a deliverable records its master in Record and lists only its differences under Overrides.
- **The example numbers are the slides starting system.** Recompute spacing and type from the active surface before use; a template value that survives unchanged into a poster or handbook is a default, not a decision.
- **Tokens use px, em, or rem;** print gives CSS px, with pt or mm in the prose. Every size and gap a unit uses has a token; none goes unused. Primary is ink, secondary muted, tertiary accent, neutral paper; other roles keep Folio's names. Each component pairs a foreground with the ground it touches, so `npx @google/design.md lint DESIGN.md` checks its contrast.
- **Headings stay in English** for tools; prose may use the user's language.

```markdown
---
version: alpha
name: <work> · <direction>
description: <the central idea in one sentence>
colors:
  primary: "#111111"
  secondary: "#625F59"
  tertiary: "#C83024"
  neutral: "#FFFFFF"
  soft: "#F4F2ED"
  focus: "#005FCC"
  line: "#C5C2BC"
  dark: "#141414"
typography:
  display: { fontFamily: "Inter, Source Han Sans SC, Noto Sans SC, sans-serif", fontSize: 120px, fontWeight: 700, lineHeight: 1 }
  title: { fontFamily: "Inter, Source Han Sans SC, Noto Sans SC, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.15 }
  body: { fontFamily: "Inter, Source Han Sans SC, Noto Sans SC, sans-serif", fontSize: 20px, fontWeight: 400, lineHeight: 1.45 }
  label: { fontFamily: "Inter, Source Han Sans SC, Noto Sans SC, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.3 }
spacing:
  margin: 70px
  gutter: 24px
  column: 73px
  columns: 12
  module: 8px
rounded:
  none: 0px
components:
  text-on-paper: { backgroundColor: "{colors.neutral}", textColor: "{colors.primary}" }
  muted-on-paper: { backgroundColor: "{colors.neutral}", textColor: "{colors.secondary}" }
  paper-on-accent: { backgroundColor: "{colors.tertiary}", textColor: "{colors.neutral}" }
  paper-on-dark: { backgroundColor: "{colors.dark}", textColor: "{colors.neutral}" }
  hairline: { backgroundColor: "{colors.line}", height: 1px }
  text-on-soft: { backgroundColor: "{colors.soft}", textColor: "{colors.primary}" }
  muted-on-soft: { backgroundColor: "{colors.soft}", textColor: "{colors.secondary}" }
  focus-ring: { backgroundColor: "{colors.focus}", height: 2px }
---

## Invocation
<The tested term or master's name + the named work, as an imperative — this file's first content line. The school is fixed by the dialect; the hand is not: choose the governing hand from the active dialect's Hands roster, for this material, and say why it suits, here or in Overview; a period of the same master is a different hand. Other hands guest as moves (evocation bundles in Sequence), never as co-hands — one governing hand per deliverable. It governs everything below: where a parameter and the named hand's evident way of working conflict on atmosphere or composition, the hand wins and the conflict is recorded in Record; the parameters bind absolutely on facts, contrast floors, live text, format, and the bans.>

## Overview
Subject and where its content lives (the file holds decisions, not content); reader, setting, and one reading mode; surface; the central idea; theme and dialect.
Governing hand: Make every unit as <master / programme> made <work>: <the move in one imperative line>; never <the ban>.
Signature programme: <one signature method from signature.md, its card's parameters for this work> — or: Signature: none — <the reason>.

## Colors
Each role: what it marks, the grounds it touches, where it never appears.

## Typography
Faces and their lineage; the ramp; Chinese and Latin pairing; figures.

## Layout
Grid, module, master lines; what changed from the surface's starting system.

## Do's and Don'ts
The dialect's rules and test; habits ruled out, or the brief's reason for one.

## Directions
| | Direction | Looks | Why it suits | Grid · faces · color · lead · methods |
|---|---|---|---|---|
| A | Mother tongue, by the book | | | |
| B | Mother tongue, pushed | | | |
| C | <closest dialect> | | | |

Dialects set aside, each with its reason. Chosen: which, by whom, from which render.

## Sequence
Rhythm first, as one composition: mark every unit's register (base / turn / pause) before filling the columns; the turns sit where the content turns. A speaking deliverable of four or more units with no variation does not lock.

| Unit | Form | Register | Lead | Methods (master · work: imperative + parameters + ban) | Variation (name + magnitude + keep) or continuity (with its rhythm cost) |
|---|---|---|---|---|

## Coverage
Text · Image · Data · Space and frame: the cells used, or why a column stays empty.

## Gaps
Missing assets and evidence; unverified facts; what is illustrative.

## Record
Folio version, files read, date; template version and role mappings; the family master, if any; changes after the lock.

## Overrides
Against the family master: each token or rule this deliverable changes, and why. Empty when there is no master.
```
