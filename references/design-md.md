# DESIGN.md — the skeleton, and the brief

<!-- folio-template-version: 14 -->

A world has one DESIGN.md: its aesthetic system, no content. Each piece has a brief. The skeleton is written for the agent that makes the next piece, so it reads in the order a maker works: the hand's method and material, then construction, type and color, exact values last. Token names follow Google's [DESIGN.md](https://github.com/google-labs-code/design.md) where they overlap.

## The skeleton

- **A world, not a piece.** A brand, a series, or a kind of content: the scope its content shares. What every piece keeps and what each piece brings are both stated; no fact of any piece appears, not even as an example.
- **It stands alone.** With this file and their content, a maker without Folio can make the piece: the method, how a new subject yields its idea, how the method translates to content it was not made for, and the forms any content needs. A master's method has no unsuitable content.
- **Relative to the format, never one size.** Every size derives from S, the format's short side, and every construction from W × H, so the same file builds a poster, a slide, a phone cover or a page. A size set by a span is derived, never also fixed: one rule per size.
- **Three tests per line.** Would a maker get it wrong without it? Is it the rule, not one result of it (a ratio, not 336)? Does it say what no other line says? A line that fails one goes; a skeleton of rules, not instances, has nothing to contradict.
- **No rule against itself.** Every rule holds for Latin and Chinese, for one language or two, for every form; a translation in World is never banned in Forms. Where two rules meet, the file says which wins.
- **Method before look.** The invocation opens it: school, hand, the work that carries the method, the method as an imperative, one ban. Then the method as process: the first move, the tools and materials, the procedure, and how each piece finds its own idea in its subject. Values read first teach a look.
- **Images decided once.** Where they come from (photographed, hand-made, computed, or none), crop, treatment, credit.
- **Layout as construction, not coordinates.** The grid system named, with the rule that derives it from any format.
- **Forms, one line each.** How each form this world uses is set, and its ban.
- **Tokens derived, not inherited.** From the hand and the world, at the end as data. A role only if used, every role used. Every text-on-ground pair is listed under `pairs`, so contrast can be checked.
- **Written as commands.** After the lock, helpers read this file instead of the theme.
- **The file changes before the work.**
- **English headings**, so scripts can find them; the prose may follow the person's language.

````markdown
# <World> · <school, hand>

<What this system makes, for which content, in one sentence.>

> Use alone: read Overview and Images before any value; build the grid from your format by Layout; Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. Check the piece against Do's and Don'ts.

## Overview
<School>, <hand> — <the work>: <the method as an imperative>; never <the ban>.
World: <the content and surfaces it serves; how the method translates to content it was not made for; what every piece keeps, what each piece brings>.
Method: <the first move, the tools and materials, the procedure; how each piece finds its idea in its subject>.
Amplitude: <full, or reduced: what is turned down, and why>.
Anti-reference: <the default this world refuses>.

## Images
<Source: photographed, hand-made, computed, or none. Crop, treatment, credit; what stands in, declared, until the real one exists.>

## Layout
Grid system: <one system from the theme's roster> — <why>.
<The construction from W × H: unit, margins, tracks; how portrait, landscape and square differ; where the space the content does not need goes.>

## Typography
<Faces and lineage; the ramp as steps at S = 1000; the smallest reading size; CJK and Latin as one voice; figures.>

## Colors
<Each role: what it marks, the grounds it touches, where it never appears.>

## Shapes
<Edges, rules, radius, depth; the drawing grammar of anything made in code.>

## Forms
<The forms any content brings (cover, statement, exhibit, argument and data, sequence, comparison, collection, reference, close), each as this hand sets it, or refused; its ban.>

## Variations
<The breaks this world allows at a turn, each with magnitude and keep condition.>

## Do's and Don'ts
<Look before delivering: what the render must not show. The floors. The school's test; its caricature.>

## Tokens

```yaml
colors:
  primary: "<ink>"
  neutral: "<ground>"
  <role>: "<value>"
typography:
  <role>: { fontFamily: "<face, CJK pair, generic>", fontSize: <px>, fontWeight: <n>, lineHeight: <n> }
spacing:
  <step>: <px>
pairs:
  <fg>-on-<ground>: { backgroundColor: "{colors.<ground>}", textColor: "{colors.<fg>}" }
```

## Record
Folio version: <x.y.z>. Template version: 14. Date: <date>.
Pieces: <briefs>. Changes after the lock: <list>.
````

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
- **Assumptions and gaps.** Ask once, only what changes the work; what stays unknown or unverified is reported with the delivery.

A piece that must differ from the skeleton records why in its brief. A difference that holds for every piece changes the skeleton.

## The test

- **Same world.** A fresh session gets the skeleton and a brief for other content in this world. What it makes reads as one set with the first piece, and only the piece's idea was new, found by the skeleton's method.
- **Rival world.** The same skeleton with a brief from another world (another subject, the same hand) should not fit. If it fits unchanged, it is the hand's costume, not this world's system.
