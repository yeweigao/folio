# DESIGN.md — the skeleton, and the brief

<!-- folio-template-version: 14 -->

A world has one DESIGN.md: its aesthetic system, no content. Each piece has a brief. The skeleton is written for the agent that makes the next piece, so it reads in the order a maker works: the hand's method and material, then construction, type and color, exact values last. Token names follow Google's [DESIGN.md](https://github.com/google-labs-code/design.md) where they overlap.

## From supplied work

Inspect the finished images before deriving the system. When reconstruction is requested, make and compare that reconstruction first; for extraction alone, inspect the supplied work directly. A selected reference establishes the direction. Describe the construction actually present, including a hybrid, and identify an author only when the source establishes one.

Group worlds by shared construction and identity, not by a shared palette or movement label. Separate what must survive in every piece from what a new piece may change. Infer the module, pattern frequency, type hierarchy and colour roles from the material; the template's fields are questions to answer, not values or paragraphs to copy.

A motif name is not its construction. Put its distinguishing silhouette, internal parts, relative dimensions and permitted transformations in Shapes, or declare the exact supplied asset that carries them. Put colour functions in Colors and face/weight assignments by role in Typography. State the conditions for a change of field or format; a narrow strip does not establish the rule for every portrait. Keep unsupported extensions identifiable as inferences.

Read the draft as a maker who cannot see the images: which missing decision could change the identity? Resolve those decisions in the file while leaving placement free where it does not define the world. Record reconstruction evidence and independent transfer evidence separately. Use The test below before calling a reference-derived system transferable.

## The skeleton

- **A world, not a piece.** A brand, a series, or a kind of content: the scope its content shares. What every piece keeps and what each piece brings are both stated; no fact of any piece appears, not even as an example.
- **It stands alone.** With this file and their content, a maker without Folio can make the piece: the method, how a new subject yields its idea, how the method translates to content it was not made for, and the forms any content needs. A master's method has no unsuitable content.
- **Three layers, one voice.** The Philosophy, the theme and the dialect are written merged, never side by side. A rule the dialect overturns is written only in the dialect's form; what it does not name is written from the theme as this world's values, since the file stands alone; what the chosen theme says its dialect keeps stays. Where a theme combines an industry dialect, a surface and a method, resolve their precedence there and write the resulting rules as one voice. The Philosophy is never quoted and never bent: each line is answered by a rule in this world's terms.
- **Relative to the format, never one size.** Every size derives from S, the format's short side, and every construction from W × H, so the same file builds a poster, a slide, a phone cover or a page. A size set by a span is derived, never also fixed: one rule per size.
- **Three tests per line.** Would a maker get it wrong without it? Is it the rule, not one result of it (a ratio, not 336)? Does it say what no other line says? A line that fails one goes; a skeleton of rules, not instances, has nothing to contradict.
- **No rule against itself.** Every rule holds for Latin and Chinese, for one language or two, for every form; a translation in World is never banned in Forms. Where two rules meet, the file says which wins.
- **Method before look.** The invocation opens it: school, hand, the work that carries the method, the method as an imperative, one ban. Then the method as process: the first move, the tools and materials, how the subject yields different compositional relationships, and the visible evidence for choosing among them. State this hand's criterion in the world's terms; a material-dependent decision and a usable reading path must survive the choice. Values read first teach a look.
- **Images decided once.** Source, treatment and credit; how each image role meets the frame (full bleed, trim-connected panel or inset), what must survive the crop, and how proportions are preserved.
- **Layout as construction, not coordinates.** The grid system named, with the rule that derives it from any format.
- **Forms, one line each.** How each form this world uses is set, and its ban. For a text-heavy world, specify paragraph measure and continuation, how genuine peers share columns, and how table/data rules differ from graphic framing; test these with new text rather than infer them from a cover.
- **Tokens derived, not inherited.** From the hand and the world, at the end as data. A role only if used, every role used. Every text-on-ground pair is listed under `pairs`, so contrast can be checked.
- **Written as commands.** After the lock, helpers read this file instead of the theme.
- **The file changes before work made from it.** A new or changed file is read by the skeleton reader ([review](review.md#skeleton-reader)) before its first new piece. Reference reconstruction precedes extraction as described above.
- **English headings**, so scripts can find them; the prose may follow the person's language.

````markdown
# <World> · <school, hand>

## Overview
<School>, <hand> — <the work>: <the method as an imperative>; never <the ban>.
World: <the content and surfaces it serves; how the method translates to content it was not made for; what every piece keeps, what each piece brings>.
Method: <the first move, tools and material; the subject feature that generates different relationships; the visible criterion for retaining one and rejecting another, while preserving reading; how quiet or non-image material is handled>.
Amplitude: <full, or reduced: what is turned down, and why>.
Anti-reference: <the default a maker reaches for with no school, which this world refuses; the school's own costume goes to Caricature>.

## Images
<Source: photographed, hand-made, computed, or none; treatment and credit. For each image role, state whether it meets the trim or sits within it, and how that changes with format. Name what the crop must preserve; scale uniformly from the source ratio when fitting its frame. What stands in, declared, until the real one exists.>

## Layout
Use alone: tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size derived from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. A piece that must break a rule says why; a break every piece needs changes this file first. Check the piece against Do's and Don'ts.

Grid system: <one system from the theme's roster> — <why>.
<The construction from W × H: module, margins, tracks, pattern frequency and adjoining fields. Name the stable relationships and the free positions; state the conditions for each format or field change and where unused space goes. Resolve gaps between actual type/image ink relative to type or module; text-box clearance alone is not the measure. For recurring groups, name the shared alignment, spacing or motif, and how size or density changes with importance or content length. Genuine peers retain shared measures; add no element solely to produce a beat.>

## Typography
<Assign a face and real weight to each role, with licensed sources or supplied files and the glyph coverage needed for new content. Give the size/weight ramp at S = 1000 or a span-derived rule, the smallest reading size, CJK/Latin relationship and figures. Name what visibly separates the levels; where scale leads, state the role-to-role size ratios. Where display leads, state its scale and weight in the field. Recompose long titles within the hierarchy.>

## Colors
<Each role: what it marks, the grounds it touches, where it never appears.>

## Shapes
<Edges, rules, radius and depth. For identity-bearing motifs or constructed letters, define intrinsic counts, relative proportions, inner parts/negative shapes, joins and allowed transformations so another maker can construct them without the reference; or name the supplied asset. Repeated-instance counts and order stay variable unless they establish the identity. Pattern pitch follows the module rather than being re-scaled to each container. Keep page coordinates and piece content out.>

## Forms
<The forms any content brings (cover, statement, exhibit, argument and data, sequence, comparison, collection, reference, close), each as this hand sets it, or refused; its ban.>

## Variations
<The breaks this world allows at a turn, each with magnitude and keep condition. These depart from the grammar; ordinary within-unit cadence belongs in Layout.>

## Do's and Don'ts
<Look before delivering: what the render must not show that the test does not already catch. The floors. The school's test, as proof; its caricature, the school's look without its method. Each said once, and once only across the file.>

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
- **The idea.** "On this surface, *the subject* becomes *the device*." It fails if a rival subject fits the sentence, or a second maker would reach it unaided. The idea names the subject's cause, never its form: no primitive, hue, position or device is decided in the brief — those are found at make time by the skeleton's method and recorded in the piece's notes. A brief that pre-writes form has already made the piece, badly, and hidden the making from review.
- **Sequence.** Per unit: form, lead, register (base, turn, pause). Turns sit where the content turns and name their variation.
- **Assumptions and gaps.** Ask once, only what changes the work; what stays unknown or unverified is reported with the delivery.

A piece that must differ from the skeleton records why in its brief. A difference that holds for every piece changes the skeleton.

## The test

- **Same world.** Freeze the skeleton and a new-content brief. A fresh maker gets only these and declared production assets, without the references, previous artwork or its drawing code. Inspect the new render beside the existing set: identity, composition and content transfer are separate from craft/fact compliance. Declare which assets were supplied; a handed-over motif component is not proof that its written construction is sufficient. Keep failures before revising the file and test a revision with a fresh maker. One successful piece establishes one transfer, not general reliability.
- **Rival world.** Change the identity or governing relationships, not merely the title or subject within the same series. If the file still fits without changing its construction, it may describe the hand's generic look rather than this world. New topics within a world's declared scope are expected to fit.
