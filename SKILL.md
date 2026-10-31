---
name: folio
description: Art-directs visual work across slides and PPT, posters, websites, canvases, and handbooks. Use for visual design, redesign, or critique, and whenever a result looks generic, templated, AI-made, or not premium enough. Defaults to Swiss style, the International Typographic Style, and related modernist movements unless the brief or an existing system says otherwise. Not for copywriting, data analysis, or engineering tasks with no visual deliverable.
license: MIT
version: 0.5.2
---

# Folio — Swiss-style design for AI agents

Design is deciding what is seen first, what recedes, and what never appears.

## Philosophy

These thirteen lines are the constitution of this skill: they outrank every other file here. Where a craft rule, a theme habit, or a surface starting value conflicts with a line, the line wins and the conflict is recorded in DESIGN.md. They are not decoration and not a summary of the rules below — the rules are their instruments. At Inspect, every failure is named by the line it breaks; a failure that names no line is an opinion, and opinions do not block delivery.

- **A unit has a lead, not a crowd.** One element is read first; everything else queues behind it.
- **The eye's path is designed, not discovered.** Reading follows declared axes; lookup gets clear entry points and a predictable order.
- **The decisive move comes from the subject, not from a style.** Every speaking unit has one leading idea you can say in a sentence; reference units stay quiet.
- **Layout serves the content, not the other way round.** Recompose first, then edit or paginate within scope; never hide content or shrink type to make it fit.
- **Measure is shared, not improvised.** Columns, spacing, baselines, and proportions belong to one system, fitted to the surface.
- **Space is placed, not left over.** Judge it by its job (group, separate, focus), not its amount; fix accidental gaps with scale or placement, never filler.
- **Hierarchy is steps, not slopes.** Few faces, few levels, wide gaps, one treatment per role.
- **Color is a role, not a decoration.** Hue carries meaning; every foreground stays distinct from the ground it actually touches.
- **A deliverable has rhythm, not monotony.** Dense, quiet, and loud units follow the content; repeat to orient, break to signal a change.
- **Information is encoded, not decorated.** Data takes a readable form; decoration never poses as evidence; meaning never depends on color alone.
- **An image is information, not filler.** Evidence, explanation, setting, or atmosphere; illustration never poses as documentary proof.
- **Style is a constraint system, not an element set.** Strip away colors and fonts, and the piece is still recognizable.
- **The frame is composed, not inherited.** Format, crop, and spread boundaries shape the composition; use the edge deliberately.

## Practice

Read these whole, once per deliverable, before making anything: [craft](references/craft.md), the active theme ([Swiss](references/themes/swiss/theme.md) by default), the one surface ([slides](references/surfaces/slides.md), [poster](references/surfaces/poster.md), [web](references/surfaces/web.md), [canvas](references/surfaces/canvas.md), or [handbook](references/surfaces/handbook.md)), the [DESIGN.md template](references/design-md.md), the [signature cards](references/signature.md) for any signature method a direction uses, and the file of every dialect a direction uses. Scale the process to the job: a single small unit with a named direction runs the same eight steps compressed — directions written but not rendered, one inspection round — and records the compression in DESIGN.md's Record; it never skips the floors or the lock. After delivery, refinement turns use the named moves in [steering](references/steering.md), each recorded in DESIGN.md before it is applied. Decisions are written into the deliverable's DESIGN.md, one line each, not held in mind; once it is locked, later sessions and helpers read SKILL.md, craft, the surface, and DESIGN.md instead of the theme and dialects — with one exception: at Make, the master cells and dialect rules a unit cites are re-read in the original, just in time (step 7). Revisit earlier decisions when later ones fail.

1. **Brief.** Facts, wording, format, and brand bind, and so does a supplied DESIGN.md; refinement keeps the existing system, redesign may replace it.
2. **Reader.** Who reads, where, from how far, for how long, in which languages, to do what. Infer routine choices and state assumptions; ask once, and only what changes the work: what binds every direction (brand, format, how the work reaches its reader) before step 4, the rest with step 5.
3. **Material.** The claim and its proof: the words, data, and images available or still needed. Ask for references, images, and real numbers in the same round; name every gap, including evidence that could be shown and is missing.
4. **Directions.** The work's central idea in a sentence, then three directions drafted in DESIGN.md before anything is rendered: the mother tongue by the book; the mother tongue pushed, through other method cells, bolder scale, a color field, or one guest move; and the dialect from the table below closest to what the material does and who reads it. Each names its grid, faces, color roles, leading move, method cells, and its governing hand — the one master or programme whose way of working leads the whole deliverable, not a per-unit garnish; any two share at most one of layout (the zones; the grid may be shared), type, color, and leading move. A dialect direction is judged on the dimensions its file replaces, not the ones it declares it keeps: it must differ from the mother tongue on every replaced dimension and in its leading move. The theme comes from the brief or an existing system, else Swiss; the surface never chooses a dialect. A named style, designer, or dialect binds its lineage, from its library entry or supplied references, and the material is re-formed within scope to suit it. That, an existing system, a supplied DESIGN.md, or a refinement makes one direction unless options are asked for; naming only the theme keeps three.
5. **Choose.** Render the hardest unit, the densest or most constrained and rarely the cover, once per direction, at one size, with real content. Show the renders in one image, adjacent and large enough to read, wide units stacked, each with one line on how it looks and one on why it suits; recommend one, the plainest only when the others fail the unit's job, then stop until the user chooses or combines. With one direction, or when the user cannot be asked, has said to decide, or the work is a batch, render the recommendation only, keep the others written, and go on.
6. **Lock.** Complete DESIGN.md, its sizes tried on the longest title and the densest text: the system once; for every unit its form, its lead, and for each reader task a named method, never a default; the Sequence's rhythm is mapped before its details: every unit is marked with a register (base, turn, or pause) as one composition, the turns placed where the content turns — an opener, a key figure, a change of register — never spread evenly for variety's sake. At every marked turn a variation is taken, or continuity is chosen with a reason that names what the rhythm loses by it, as specific as the variation's own parameters; 'continuity serves' without the cost is not a reason. A deliverable of four or more speaking units with no variation taken does not lock (reference units and single-unit work excepted): monotony is a lock failure, not a style; each method column used or its absence explained; every named cell, variation, and dialect rule with one line on how. The Overview names the governing hand in instruction voice ("Make every unit as …"), because after the lock the theme is not re-read by default and a name recorded as a past-tense citation does not instruct anyone. A method citation that will be relied on carries its evocation bundle with it into the file: the master's name, the work that carries the move, the move as an imperative, its parameters, and one ban — a name alone is a label, not an instruction. Lock also names the deliverable's signature programme in the Overview — one signature method from references/signature.md, built to its card, governing the whole work — or records 'Signature: none' with the reason (a reference deliverable, a supplied system that forbids it); a speaking deliverable with neither does not lock, and folio-check enforces it. It is locked when a new session could make any unit from it and the source without inventing a value, and `scripts/folio-check.py DESIGN.md` passes. At the lock, generate the token catalog with `scripts/preview.py DESIGN.md` and keep preview.html beside the file, so the system can be seen without rendering a unit. Record in it the Folio version (SKILL.md frontmatter) and the template version (references/design-md.md frontmatter comment).
7. **Make.** Every unit from DESIGN.md, starting from the chosen render with its largest problem fixed. A value the file lacks is added to it first; when a unit fails, fix the file, then the unit. Before making each unit, re-read in the theme the original cells and dialect rules that unit cites, and the signature card when the unit carries the signature programme, — just in time, never from the memory of an earlier reading — and write the unit's brief before its content: its first line invokes the hand, as name + work + imperative + two or three visual predicates + one ban ("Make this unit as Müller-Brockmann made the musica viva posters: the title word at graphic scale across ten columns at 700; everything else drops to label size on the left axis; never centered, never a second accent"). The invocation is renewed per unit: a summons spent on the previous unit does not carry over. For a unit the rhythm map marks as a turn, the brief's second line is the variation, invoked the same way: its name, its magnitude (an angle, an area, a count, a size), and its Keep condition from the theme's table; a turn unit made without its variation has failed its brief, however correct the rest of it is. Where a unit's image is generated, the master's name and the named work go verbatim into the image prompt — that hand-off is where a name acts most strongly — and the generated image still answers to craft's imagery rules.
8. **Inspect.** Machines first, judgment second. Run `npx @google/design.md lint DESIGN.md` (token references and component contrast pairs; zero warnings to proceed) and `scripts/folio-check.py DESIGN.md <export>` (completeness, off-token colors and faces in the export, banned chart forms). First judge the sequence as a contact sheet — every unit as a thumbnail on one sheet: the rhythm the map promised must be visible there, turns landing where they were marked, no run of base units long enough to flatten the middle; monotony found here is named a failure before any single unit is praised. Then judge the final export, every unit at viewing size, against the philosophy, craft, the floors, DESIGN.md, the theme's anti-patterns, each dialect's test, the active surface's 'Done means' list, and — unit by unit — the 'Fails when' column of that unit's declared form. Every failure is named by the philosophy line it breaks (step 8's naming rule in the Philosophy section). Add the recognition test for the hand: with the citations covered, would this unit be recognised as the governing master's way of working — or is the name present in the file and absent from the picture? A unit that fails it has cited a method and executed its generic equivalent, which counts as a failure like any other; a habit the theme names passes only with the brief's reason in DESIGN.md. The loop is bounded: name the failures in floor order, fix the top three, re-render, at most two rounds; what still fails goes to Gaps and is reported, not silently passed.

Critique runs 1–3 to understand the supplied work, drafts its system as a DESIGN.md from evidence — `scripts/extract.py <file>` first for a .pptx or .html, so colors, faces, and sizes come from the artifact and not from an impression — then runs 8; it makes nothing new and separates observed defects from proposed directions.

Delivery attaches DESIGN.md and names the direction, each variation and what it breaks, substantive copy edits, and what remains unverified. Work read alone on other machines goes as PDF with fonts embedded; an editable source goes beside it, its fonts named.

## Forms

Choose the form first: what the unit must make the reader do. A unit is one slide, poster, screen or section, canvas frame, page, or spread.

| Form | Job | Reader tasks | Holds | Fails when |
|---|---|---|---|---|
| Cover | Identify the work | Find the lead; feel the edge | Title, maker, date; one image or typographic idea | A slogan replaces the title |
| Statement | Make one sentence memorable | Find the lead | One claim, almost nothing else | Evidence or explanation creeps in |
| Exhibit | Make one object seen | Find the lead; feel the edge | An identifiable subject, labeled directly; scale or isolation makes it the lead | The subject is lost or shares the stage |
| Argument | Make a judgment accepted | Find the lead; compare | A judgment title, relevant evidence, the implication in one place | Evidence without a judgment; evidence off the claim's axis |
| Sequence | Lead through steps, time, or cause | Follow the order | One action per step, then the conclusion | Snake columns; shuffled or flattened order |
| Comparison | Make a difference visible | Compare | Shared scales, direct labels | Misaligned scales; color as the only difference |
| Exercise | Make the reader do it | Follow the order; see the groups | The task and room to answer; answers on another unit | Answers on the same unit |
| Collection | Let peers be scanned | See the groups; compare | Shared alignment; unequal spans only for real priority | Invented rankings; equals treated unequally |
| Opener | Open a chapter | Feel the change | One sentence on what comes next | Body text, previews, a repeated contents list |
| Reference | Let the reader look things up | Know where they are; see the groups | A guessable order and scannable heads; density welcome | Decoration, a decisive move, a hidden order |
| Close | Leave the one claim or next action | Find the lead | The claim the units proved, or the action | A new conclusion |

- **One primary form per unit.** One subordinate form at most; two primary forms are two units. A form may span units, each with its own lead.
- **The test is structural.** Strip the decoration; the reader can still do the unit's job.

## Floors

Floors hold under every theme and dialect; every other value in Folio is a starting point the chosen system may change.

- **Facts are exact.** Names, dates, numbers, places, quotations, and required text never change; other edits stay within scope and are disclosed. If fixed facts collide with a fixed length, ask which can change.
- **Nothing invented poses as real.** Demo values say illustrative; calculated values name their basis; missing real names, places, hours, lineups, or product options are marked unprovided; generated people, places, and products are never evidence.
- **Text separates from its actual ground.** Normal text ≥ 4.5:1; verified large text (≥ 24 CSS px regular or ≥ 18⅔ px bold, or equivalent CJK size, after scaling) ≥ 3:1; essential non-text cues ≥ 3:1 against adjacent colors; the surface's size floors hold. These thresholds alone do not establish accessibility conformance.
- **Reading text is live.** Never baked into an image; an image-filled or cropped title keeps a complete live-text equivalent.
- **Static work stays static.** Motion belongs to interactive work.
- **Print frames are separate.** Trim, bleed, safe area, and binding are not one margin; a new format is recomposed, not scaled; 1 in = 96 CSS px = 72 pt = 25.4 mm, and an HTML preview scales the whole print layout together; trim and type sizes are confirmed in the export.
- **The export is inspected, not the draft.** Every unit plus its sequence, spreads, or viewports: fonts as rendered and embedded, crops, overflow, navigation, contrast after overlays; a fix earns a recheck; unverified is reported, not passed.
- **A shared system changes by version.** One deliverable keeps its adjustments local and records the template version and role mappings in DESIGN.md; a family upgrade gets a new version, a change note, a dense and a sparse output rechecked, and the previous baseline kept.
- **Licenses travel with assets.** Folio's MIT license covers neither fonts nor photographs; see [fonts](references/fonts.md).

## Theme and dialect

The theme owns the visual grammar; a dialect replaces only the rules it names, across the whole piece, while forms keep their reader tasks; a variation breaks the grammar on one unit, and one dialect's signature move may visit a unit as a guest; floors never move. An existing system outside the library uses its own references with the shared craft. The default theme is [Swiss](references/themes/swiss/theme.md), the International Typographic Style.

The mother tongue alone suits material that argues, reports, testifies, surveys, counts, or lists; it is the by-the-book direction, and the closest row below is still tested beside it.

| Dialect | The material | Departs from Swiss |
|---|---|---|
| [De Stijl](references/themes/swiss/dialects/de-stijl.md) | Relates: parts whose proportions and balance are the subject | Black bars and primary planes in equilibrium |
| [Bauhaus](references/themes/swiss/dialects/bauhaus.md) | Celebrates or explains: events, culture, education, where geometry can carry the subject | Primaries and primitives on one module, overlapping into figures |
| [Brodovitch](references/themes/swiss/dialects/brodovitch.md) | Seduces: fashion, beauty, portraits, exhibitions, where the image is the subject | Didot type colliding with a daring crop; spreads paced like film |
| [Polish Poster School](references/themes/swiss/dialects/polish-poster.md) | Interprets: a cultural subject that wants a point of view | One authored, hand-made metaphor |
| [Ulm](references/themes/swiss/dialects/ulm.md) | Coordinates: instructions, wayfinding, a system of related messages | Rules for every case; color and pictograms as codes |
| [Swiss Punk](references/themes/swiss/dialects/swiss-punk.md) | Provokes: culture and music that should feel rebellious, still readable | The grid tested by rotation, layering, and stepped type |
| [Memphis](references/themes/swiss/dialects/memphis.md) | Delights: products, events, youth culture that want character | Clashing colors and pattern as material |
| [Kenya Hara, ma 間](references/themes/swiss/dialects/ma.md) | Invites: one object, craft, or ceremony, few words | Emptiness as the vessel; small, quiet type |
| [Swiss Brutal](references/themes/swiss/dialects/brutalist.md) | Specifies: a technical system whose structure is the content | Visible grid rules, zero radius, dense ledger rows |
