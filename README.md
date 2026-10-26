![Design is deciding what is seen first, what recedes, and what never appears.](assets/hero.png)

# Folio

**Swiss-style design for AI agents.** A skill that art-directs slides, posters, websites, canvases, and handbooks, so the result reads as designed rather than generated.

[Install](#install) · [How it works](#how-it-works) · [Dialects](#dialects) · [中文](#中文)

## What changes

Agents reach for the same moves. Folio names each one and gives the alternative.

| The default | With Folio |
|---|---|
| Centered hero, three equal cards, gradient button | A flush-left claim, one supporting line, one action |
| Floating rounded cards, shadows, glass | Grouping by space, rules, or one solid field |
| KPI tiles | A ledger: value, baseline, period, change |
| An icon per bullet, emoji | Hierarchy by type; one pictogram set where it speeds recognition |
| Pie, donut, gauge, dual axis | Sorted bars, labeled lines, aligned panels |
| Purple-blue gradients | Paper, ink, and one accent taken from the subject |
| Elevate, seamless, 赋能, 一站式 | The concrete action, object, and number |

## How it works

**Thirteen lines of philosophy.** `SKILL.md` changes the output on its own:

1. A unit has a lead, not a crowd.
2. The eye's path is designed, not discovered.
3. The decisive move comes from the subject, not from a style.
4. Layout serves the content, not the other way round.
5. Measure is shared, not improvised.
6. Space is placed, not left over.
7. Hierarchy is steps, not slopes.
8. Color is a role, not a decoration.
9. A deliverable has rhythm, not monotony.
10. Information is encoded, not decorated.
11. An image is information, not filler.
12. Style is a constraint system, not an element set.
13. The frame is composed, not inherited.

**A theme, not a template.** The Swiss mother tongue (Müller-Brockmann, Ruder, Hofmann, *Neue Grafik*) holds every piece together. One of thirteen dialects changes only what the subject needs. One of 21 variations breaks a rule where the content turns.

**Forms and methods.** Each unit takes one of eleven forms by what the reader must do. A methods matrix crosses eight reader tasks with text, image, data, and space, built from Gestalt, Bertin's visual variables, and Gerstner's morphological box.

**Craft that holds up.** Typography, fonts, grid, imagery, copy, and motion, plus color with 21 named classics from International Klein Blue to Cloud Dancer, and data in the McKinsey exhibit tradition with IBCS notation.

**Floors.** Facts stay exact. Text holds 4.5:1 on its actual composite. The final export is inspected, not the draft.

## Dialects

| Dialect | The material | Signature move |
|---|---|---|
| editorial | Argues to a decision: a judgment and its evidence | Action title, one exhibit, a full-width decision band |
| aicher | Instructs: steps, rules, schedules for strangers or mixed-language readers | One grotesque, mapped function colors, one pictogram set |
| documentary | Testifies: real photographs and sourced facts | One real photograph leads; captions say who, where, when, source |
| brodovitch | Seduces: the image is the subject, as in fashion, beauty, exhibitions | Bodoni-scale type colliding with a cropped image |
| constructivist | Mobilizes: one claim and one fact that call to act | One diagonal, condensed giant type, red and black |
| bauhaus | Explains structure: how parts, geometry, or proportion work | One primitive shape repeated at changing scale; one primary |
| brutalist | Specifies: a technical system whose structure is the content | Grid and containers drawn in plain view; system type |
| unigrid | Surveys: many parallel parts of unequal weight, no single argument | Unequal modules, one dominant |
| swiss-punk | Provokes: culture and music that should feel rebellious, still readable | One rotation, overprint, or crop; body text on the grid |
| gerstner | Varies: a series or identity whose units one rule can generate | One declared rule generates every unit |
| isotype | Counts: quantities for readers who do not read charts | Quantities as rows of repeated, equal pictograms |
| ma 間 | Invites: one object, craft, or ceremony, few words; East Asian identity | One thing in measured emptiness; small, quiet type |
| gridnik | Constructs: a technical or architectural identity whose name can be built | Display letters built from the page grid |

The image above is set in ma 間, after Kenya Hara: one sentence, one red mark, and the emptiness kept whole.

## Install

**Claude Code**, for every project:

```bash
git clone https://github.com/yeweigao/folio ~/.claude/skills/folio
```

For one repository, clone into `.claude/skills/folio` instead.

**Claude apps.** Zip the `folio` folder, then open Customize → Skills → + → Create skill → Upload a skill. Code execution must be on.

**Other agents** that read `SKILL.md`: place the folder wherever the agent loads skills.

## Use

Ask for the work. The skill triggers on visual design, redesign, or critique, and whenever a result looks generic or AI-made.

> Turn this report into a board deck.

> Redesign this landing page.

> 这张海报太 AI 味了，重做一版，用 ma 間。

## Structure

```
SKILL.md              philosophy, the eight decisions, theme and dialects, defaults
references/
  production.md       floors: scope, viewing, frame, inspection
  surfaces/           slides · poster · web · canvas · handbook
  themes/swiss/       mother tongue · 13 dialects · 21 variations
  methods.md          forms and the methods matrix
  craft/              typography · fonts · color · grid · imagery · data · copy · motion
  anti-patterns.md    why defaults fail, and on what basis
  examples/           three studied cases
```

Every file serves one decision in the eight-step Practice of `SKILL.md`: brief, reader, material, move, system, sequence, make, inspect. A change goes to the file of the decision it changes; a new file only for a new decision; no file depends on a later step.

## 中文

Folio 是给 AI agent 用的设计 skill：PPT、海报、网页、画布、手册，做出瑞士风，不再一眼 AI 味。

13 条设计哲学，一套瑞士母语，13 种方言，21 种变奏。默认瑞士国际主义，按内容在做什么换方言：论证到决策用 editorial，请人静观用 ma 間，给不读图表的人数数量用 isotype；格式从不决定方言。每一页先定形式，再用方法撑起来，只在内容转折处变奏，节奏跟着内容走。安装方式同上。

## License

MIT. Example previews in `references/examples` are Apache 2.0. No fonts are bundled; each keeps its own license.
