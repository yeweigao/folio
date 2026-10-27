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
- **The decisive move comes from the subject, not from a style.** Every unit that speaks has one leading idea, said in a sentence; it may combine methods, while reference units stay quiet.
- **Layout serves the content, not the other way round.** Change the composition or edit within scope; never hide content or shrink type to make it fit.
- **Measure is shared, not improvised.** Columns, spacing, baselines, and proportions belong to one system, fitted to the surface.
- **Space is placed, not left over.** Judge it by its job, not its amount: group, separate, or focus. Fix accidental gaps with scale or placement, never filler.
- **Hierarchy is steps, not slopes.** Few faces, few levels, wide gaps, one treatment per role.
- **Color is a role, not a decoration.** Hue carries meaning; every foreground stays distinct from the ground it actually touches.
- **A deliverable has rhythm, not monotony.** Dense, quiet, and loud units follow the content; repeat to orient, break to signal a change.
- **Information is encoded, not decorated.** Data takes a readable form; decoration never poses as evidence, and information never depends on color alone.
- **An image is information, not filler.** Evidence, explanation, or declared atmosphere; keep only the images whose removal would lose something.
- **Style is a constraint system, not an element set.** Strip away colors and fonts, and the piece is still recognizable.
- **The frame is composed, not inherited.** Format, crop, and spread boundaries shape the composition; use the edge deliberately.

## Practice

Each decision informs the next; revisit earlier decisions when later ones fail. Read the files needed to make each decision, and state the choice in a line.

1. **Brief.** Facts, wording, format, and brand bind; refinement keeps the existing system, redesign may replace it. [Production charter](references/production.md).
2. **Reader.** Who reads, where, from how far, for how long, to do what. The surface holds its numbers: [slides](references/surfaces/slides.md), [poster](references/surfaces/poster.md), [web](references/surfaces/web.md), [canvas](references/surfaces/canvas.md), [handbook](references/surfaces/handbook.md).
3. **Material.** The claim and its proof: words, data, and images available or needed. Read [copy](references/craft/copy.md), [data](references/craft/data.md), [imagery](references/craft/imagery.md), and [motion](references/craft/motion.md) when the task needs them, including assets not yet supplied.
4. **Move.** The work's central idea, in a sentence. Choose the theme from the brief or existing system, defaulting to Swiss; within it choose a dialect by the material and reader, never by surface. A named style or designer binds its lineage: use its library entry or supplied references. A named dialect governs the whole piece; re-form material within scope.
5. **System.** Read the active theme's mother tongue and methods whole, plus its chosen dialect. Declare grid, type ramp, faces, and color roles once for the deliverable. [Grid](references/craft/grid.md), [type](references/craft/type.md), [color](references/craft/color.md).
6. **Sequence.** For each unit, choose its job and [form](references/forms.md), then methods from the active theme to carry them; combine, reuse, or change methods as the content requires within the shared system. Read that theme's variations when the content calls for a turn.
7. **Make.** The hardest unit first, with real content.
8. **Inspect.** Read the active theme's anti-patterns; inspect the final export at viewing size against the production floors, relevant craft, and theme's test. A dialect sets its own test; with the mother tongue alone, use philosophy 12: strip away colors and fonts, and the piece is still recognizable.

Critique uses 1–6 to understand the supplied work and its existing system, then 8 to judge it.

## Theme

A theme owns the visual grammar; a dialect inherits it and replaces only the style rules it names across the whole piece. Forms retain their reader tasks; craft and surface starting values yield to the chosen system, while truth, scope, and legibility floors hold. Methods realize a reader task within that grammar; a variation breaks it locally. A new theme replaces the grammar; a dialect changes a few rules. Read the active package at `references/themes/<theme>/`: `mother-tongue.md`, `methods.md`, `variations.md`, `anti-patterns.md`, and the chosen file in `dialects/`. For an existing system outside the library, use its supplied references with shared craft and production.

Default theme: [Swiss — the International Typographic Style](references/themes/swiss/mother-tongue.md). Müller-Brockmann's *Grid Systems*, Ruder's *Typographie*, *Neue Grafik*, the Basel school of Hofmann: modular grid, asymmetric flush-left composition, scale contrast, Sachfotografie, paper, ink, and one accent. Its [methods](references/themes/swiss/methods.md), [variations](references/themes/swiss/variations.md), [anti-patterns](references/themes/swiss/anti-patterns.md), and dialects below belong to this package. Its caricature is grey minimal skin at one volume; white, black, one red, and hairlines are its habit.

| Dialect | The material | Departs from Swiss |
|---|---|---|
| *the mother tongue alone* | Argues, reports, testifies, surveys, counts, or lists | — |
| [De Stijl](references/themes/swiss/dialects/de-stijl.md) | Relates: parts whose proportions and balance are the subject | Black bars and primary planes in equilibrium |
| [Bauhaus](references/themes/swiss/dialects/bauhaus.md) | Celebrates or explains: events, culture, education, where geometry can carry the subject | Primaries and primitives on one module, overlapping into figures |
| [Brodovitch](references/themes/swiss/dialects/brodovitch.md) | Seduces: fashion, beauty, portraits, exhibitions, where the image is the subject | Didot type colliding with a daring crop; spreads paced like film |
| [Polish Poster School](references/themes/swiss/dialects/polish-poster.md) | Interprets: a cultural subject that wants a point of view | One authored, hand-made metaphor |
| [Ulm](references/themes/swiss/dialects/ulm.md) | Coordinates: instructions, wayfinding, a system of related messages | Rules for every case; color and pictograms as codes |
| [Swiss Punk](references/themes/swiss/dialects/swiss-punk.md) | Provokes: culture and music that should feel rebellious, still readable | The grid tested by rotation, layering, and stepped type |
| [Memphis](references/themes/swiss/dialects/memphis.md) | Delights: products, events, youth culture that want character | Clashing colors and pattern as material |
| [Kenya Hara, ma 間](references/themes/swiss/dialects/ma.md) | Invites: one object, craft, or ceremony, few words | Emptiness as the vessel; small, quiet type |
| [Swiss Brutal](references/themes/swiss/dialects/brutalist.md) | Specifies: a technical system whose structure is the content | Visible grid rules, zero radius, dense ledger rows |
