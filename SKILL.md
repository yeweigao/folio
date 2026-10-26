---
name: folio
description: Art-directs visual work across slides and PPT, posters, websites, canvases, and handbooks. Use for visual design, redesign, or critique, and whenever a result looks generic, templated, AI-made, or not premium enough. Defaults to Swiss style, the International Typographic Style, and related modernist movements unless the brief or an existing system says otherwise.
license: MIT
---

# Folio — Swiss-style design for AI agents

Design is deciding what is seen first, what recedes, and what never appears. This file sets the target, the order of decisions, and the limits; the means are yours.

## Philosophy

- **A unit has a lead, not a crowd.** One element is read first and everything else queues behind it, whatever the unit holds.
- **The eye's path is designed, not discovered.** Guide reading along declared axes; give lookup clear entry points and a predictable order.
- **The decisive move comes from the subject, not from a style.** Every unit that speaks carries one, said in a sentence; units for reference stay quiet.
- **Layout serves the content, not the other way round.** Change the composition or edit within scope; never hide content or shrink type to make it fit.
- **Measure is shared, not improvised.** Columns, spacing, baselines, and proportions belong to one system, fitted to the surface.
- **Space is placed, not left over.** Judge it by its job, not its amount: group, separate, or focus. Fix accidental gaps with scale or placement, never filler.
- **Hierarchy is steps, not slopes.** Few faces, few levels, wide gaps, one treatment per role.
- **Color is a role, not a decoration.** The accent comes from the brand or the subject and stays the exception.
- **A deliverable has rhythm, not monotony.** Dense, quiet, and loud units follow the content; repeat to orient, break to signal a change.
- **Information is encoded, not decorated.** Data takes a readable form; decoration never poses as evidence, and information never depends on color alone.
- **An image is information, not filler.** Evidence, explanation, or declared atmosphere; keep only the images whose removal would lose something.
- **Style is a constraint system, not an element set.** Strip away colors and fonts, and the piece is still recognizable.
- **The frame is composed, not inherited.** Format, crop, and spread boundaries shape the composition; use the edge deliberately.

## Practice

Each decision constrains the next; when a later one fails, go back, not around. Open each file when its decision arrives, and settle the decision in a line before taking the next.

1. **Brief.** Facts, wording, format, and brand bind; refinement keeps the existing system, redesign may replace it. [Production charter](references/production.md).
2. **Reader.** Who reads, where, from how far, for how long, to do what. The surface holds its numbers: [slides](references/surfaces/slides.md), [poster](references/surfaces/poster.md), [web](references/surfaces/web.md), [canvas](references/surfaces/canvas.md), [handbook](references/surfaces/handbook.md).
3. **Material.** The claim and its proof, before any layout: the words, data, and images on hand. [Copy](references/craft/copy.md).
4. **Move.** The decisive move, in a sentence. Then the dialect by what the material does and who reads it, never by the surface: the one whose signature move this material can feed, or the mother tongue alone. A dialect or style the brief names binds: take the dialect whose lineage holds it, and re-form the material until it can feed it.
5. **System.** Grid, type ramp, faces, and color roles, declared once for the deliverable: the surface's numbers through the [mother tongue](references/themes/swiss/mother-tongue.md) and the dialect. [Grid](references/craft/grid.md), [typography](references/craft/typography.md), [fonts](references/craft/fonts.md), [color](references/craft/color.md).
6. **Sequence.** Each unit's job and its [form](references/methods.md); a [variation](references/themes/swiss/variations.md) only where the content turns. [Data](references/craft/data.md), [imagery](references/craft/imagery.md), and [motion](references/craft/motion.md) when the content has them.
7. **Make.** The hardest unit first, with real content.
8. **Inspect.** The final export at viewing size, against the floors, the dialect's owner's test, and the [anti-patterns](references/anti-patterns.md).

Critique runs 1–4 and 8 on the supplied work.

## Theme

A theme is a constraint system: the mother tongue holds the piece together, at most one primary dialect changes selected rules, and a variation breaks one rule where the content calls for it, sometimes with a single move borrowed from a guest dialect.

Default theme: the International Typographic Style. Müller-Brockmann's *Grid Systems*, Ruder's *Typographie*, *Neue Grafik*, the Basel school of Hofmann: modular grid, asymmetric flush-left composition, scale contrast as hierarchy, Sachfotografie, paper, ink, and one accent. Its caricature is grey minimal skin at one volume; its habit is white, black, one red, hairlines.

| Dialect | The material | Signature move |
|---|---|---|
| [editorial](references/themes/swiss/dialects/editorial.md) | Argues to a decision: a judgment and its evidence | Action title, one exhibit, a full-width decision band |
| [aicher](references/themes/swiss/dialects/aicher.md) | Instructs: steps, rules, schedules for strangers or mixed-language readers | One grotesque, mapped function colors, one pictogram set |
| [documentary](references/themes/swiss/dialects/documentary.md) | Testifies: real photographs and sourced facts | One real photograph leads; captions say who, where, when, source |
| [brodovitch](references/themes/swiss/dialects/brodovitch.md) | Seduces: the image is the subject, as in fashion, beauty, exhibitions | Bodoni-scale type colliding with a cropped image |
| [constructivist](references/themes/swiss/dialects/constructivist.md) | Mobilizes: one claim and one fact that call to act | One diagonal, condensed giant type, red and black |
| [bauhaus](references/themes/swiss/dialects/bauhaus.md) | Explains structure: how parts, geometry, or proportion work | One primitive shape repeated at changing scale; one primary |
| [brutalist](references/themes/swiss/dialects/brutalist.md) | Specifies: a technical system whose structure is the content | Grid and containers drawn in plain view; system type |
| [unigrid](references/themes/swiss/dialects/unigrid.md) | Surveys: many parallel parts of unequal weight, no single argument | Unequal modules, one dominant |
| [swiss-punk](references/themes/swiss/dialects/swiss-punk.md) | Provokes: culture and music that should feel rebellious, still readable | One rotation, overprint, or crop; body text on the grid |
| [gerstner](references/themes/swiss/dialects/gerstner.md) | Varies: a series or identity whose units one rule can generate | One declared rule generates every unit |
| [isotype](references/themes/swiss/dialects/isotype.md) | Counts: quantities for readers who do not read charts | Quantities as rows of repeated, equal pictograms |
| [ma 間](references/themes/swiss/dialects/ma.md) | Invites: one object, craft, or ceremony, few words; East Asian identity | One thing in measured emptiness; small, quiet type |
| [gridnik](references/themes/swiss/dialects/gridnik.md) | Constructs: a technical or architectural identity whose name can be built | Display letters built from the page grid |

## Defaults that pose as structure

Models reach for these by habit. Each is legitimate when the content, brand, or user asks for it; when a client insists, make it as clean as the grid allows. Otherwise use the alternative. The [anti-patterns](references/anti-patterns.md) explain why.

- Centered hero, three equal cards, gradient button → a flush-left claim, one supporting line, one action
- Floating rounded cards, shadows, glow, glass → grouping by space, rules, or a solid field
- KPI tiles → a ledger: value, baseline, period, change
- An icon per bullet, emoji → hierarchy by type; one pictogram set only where it speeds recognition
- Numbers and eyebrows on everything → numbering for real sequences; headings that stand alone
- Pie, donut, gauge, dual axis → sorted bars, labeled lines, aligned panels
- Purple-blue gradients, cream screen grounds → the theme's paper and ink, an accent from the subject
- Filler copy (elevate, seamless, 赋能, 一站式) → the concrete action, object, and number
- If the plan could be described without naming this brief's subject, it is still a default
