# DESIGN.md

One file per deliverable, beside the work, holds every decision, so each unit, later session, or helper makes the same piece without rereading the theme. It follows the open [DESIGN.md](https://github.com/google-labs-code/design.md) format, tokens in YAML front matter and reasons in prose under its sections in order, and adds Folio's sections after them.

- **Drafted at Directions, locked at Lock.** Step 4 writes Overview, Directions, and Gaps; step 6 completes the rest for the chosen direction.
- **It names the subject.** A file that would fit another deliverable is a default.
- **Cite by name, then say how.** Each method cell, variation, and dialect rule appears under its name in the theme, with one line on how this work makes it.
- **The file changes before the work.** A missing value is added first; a failed unit changes the file, then the unit; changes after the lock go in Record.
- **A supplied DESIGN.md binds** like a brand: keep its values and fill its gaps in place.
- **Tokens use px, em, or rem;** print gives CSS px, with pt or mm in the prose. Primary is ink, secondary muted, tertiary accent, neutral paper; other roles keep Folio's names. Each component pairs a foreground with the ground it touches, so `npx @google/design.md lint DESIGN.md` checks its contrast.
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
  line: "#C5C2BC"
  dark: "#141414"
typography:
  display: { fontFamily: Arial, fontSize: 120px, fontWeight: 700, lineHeight: 1 }
  title: { fontFamily: Arial, fontSize: 48px, fontWeight: 700, lineHeight: 1.15 }
  body: { fontFamily: Arial, fontSize: 20px, fontWeight: 400, lineHeight: 1.45 }
  label: { fontFamily: Arial, fontSize: 14px, fontWeight: 700, lineHeight: 1.3 }
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
---

## Overview
Subject, reader and setting, surface; the central idea; theme and dialect.

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
| Unit | Form | Lead | Methods (name: how) | Variation or continuity |
|---|---|---|---|---|

## Coverage
Text · Image · Data · Space and frame: the cells used, or why a column stays empty.

## Gaps
Missing assets and evidence; unverified facts; what is illustrative.

## Record
Folio version, files read, date; template version and role mappings; changes after the lock.
```
