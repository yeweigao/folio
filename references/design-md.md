# DESIGN.md — the skeleton, and the brief

<!-- folio-template-version: 13 -->

A world has one DESIGN.md: its aesthetic system, no content. Each piece has a brief. The skeleton follows Google's open [DESIGN.md](https://github.com/google-labs-code/design.md) format, with tokens in YAML front matter and prose under its sections in canonical order. Folio adds Variations and Record.

## The skeleton

- **A world, not a piece.** A brand, a series, a programme: the scope its content shares. A fact of one piece belongs in that piece's brief.
- **The invocation opens it.** School, hand, the work that carries the method, the method as an imperative, one ban.
- **Method as process, not looks.** The first move, the tools and materials, the procedure.
- **Tokens derived, not inherited.** From the hand and the world. A role only if used, every role used. Primary is ink, secondary muted, tertiary accent, neutral ground. Every text-on-ground pair is a component, so contrast can be checked.
- **Layout as construction, not coordinates.** The grid system named, with the rule that derives it from any format.
- **Components are the forms.** One line each for the forms this world uses: how it is set, and its ban.
- **Written as commands.** After the lock, helpers read this file instead of the theme.
- **The file changes before the work.**
- **English headings**, so tools can parse them; the prose may follow the person's language.

```markdown
---
version: alpha
name: <world> · <school, hand>
description: <the world in one sentence>
colors:
  primary: "<ink>"
  neutral: "<ground>"
  <role>: "<value>"
typography:
  <role>: { fontFamily: "<face, CJK pair, generic>", fontSize: <px>, fontWeight: <n>, lineHeight: <n> }
spacing:
  <step>: <px>
rounded:
  <name>: <px>
components:
  <fg>-on-<ground>: { backgroundColor: "{colors.<ground>}", textColor: "{colors.<fg>}" }
---

## Overview
<School>, <hand> — <the work>: <the method as an imperative>; never <the ban>.
World: <what this skeleton is for>.
Method: <the first move, the tools and materials, the procedure>.
Amplitude: <full, or reduced: what is turned down, and why>.
Anti-reference: <the default this world refuses>.

## Colors
<Each role: what it marks, the grounds it touches, where it never appears.>

## Typography
<Faces and lineage; the ramp as steps; CJK and Latin as one voice; figures.>

## Layout
Grid system: <one system from the theme's roster> — <why>.
<The construction rule from any format.>

## Shapes
<Edges, rules, radius, depth; the drawing grammar of any image made in code.>

## Components
<One line per form: how it is set; its ban.>

## Do's and Don'ts
<Up to five named rules; the dialect's test; its caricature.>

## Variations
<The breaks this world allows at a turn, each with magnitude and keep condition.>

## Record
Folio version: <x.y.z>. Template version: 13. Date: <date>.
Pieces: <briefs>. Changes after the lock: <list>.
```

## The forms

A unit is one slide, poster, screen, frame, page or spread. Its form is what it must make the reader do: one primary, at most one subordinate. Strip the decoration, and the reader can still do the job.

| Form | Job | Holds | Fails when |
|---|---|---|---|
| Cover | Identify the work | Title, maker, date; one image or typographic idea | A slogan replaces the title |
| Statement | Make one sentence memorable | One claim, almost nothing else | Evidence creeps in |
| Exhibit | Make one object seen | An identifiable subject, labeled; scale or isolation makes it lead | The subject shares the stage |
| Argument | Make a judgment accepted | A judgment title, its evidence, the implication | Evidence without a judgment |
| Sequence | Lead through steps, time or cause | One action per step, then the conclusion | Shuffled or flattened order |
| Comparison | Make a difference visible | Shared scales, direct labels | Color as the only difference |
| Exercise | Make the reader do it | The task and room to answer | Answers on the same unit |
| Collection | Let peers be scanned | Shared alignment | Invented rankings |
| Opener | Open a chapter | One sentence on what comes next | Body text, previews |
| Reference | Let the reader look things up | A guessable order, scannable heads, density | A decisive move, a hidden order |
| Close | Leave one claim or next action | The claim the units proved | A new conclusion |

## The brief

One `brief.md` per piece, beside the skeleton:

- **Facts.** A `## Facts` section, every fixed string in backticks, verbatim.
- **Reader and outcome.** Who reads, where, from how far; what should happen next.
- **The idea.** "On this surface, *the subject* becomes *the device*." It fails if a rival subject fits the sentence, or a second maker would reach it unaided.
- **Sequence.** Per unit: form, lead, register (base, turn, pause). Turns sit where the content turns and name their variation.
- **Assumptions and gaps.**

A piece that must differ from the skeleton records why in its brief. A difference that holds for every piece changes the skeleton.

## The test

A fresh session gets the skeleton and a brief for other content in the same world. If what it makes reads as one set with the first piece, and nothing had to be invented, the skeleton holds.
