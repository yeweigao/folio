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

**A theme, not a template.** The Swiss mother tongue (Müller-Brockmann, Ruder, Hofmann, *Neue Grafik*) holds every piece together. A dialect is a named movement: its people, place, and period, and the three or four Swiss rules it overturns across the whole piece. Nine are in the library, from De Stijl to Swiss Brutal. The masters' moves inside Swiss, Crouwel's grid-built letters, Gerstner's programmes, Isotype rows, Vignelli's Unigrid, live in its methods. One of 21 variations breaks a rule where the content turns.

**Forms and methods.** Each unit takes one of eleven forms by what the reader must do. The theme's methods cross eight reader tasks with text, image, data, and space, each cell a master's move, built from Gestalt, Bertin's visual variables, and Gerstner's morphological box.

**Craft that holds up.** Typography, fonts, grid, imagery, copy, and motion, plus color with 21 named classics from International Klein Blue to Cloud Dancer, and data in the McKinsey exhibit tradition with IBCS notation.

**Floors.** Facts stay exact. Text holds 4.5:1 on its actual composite. The final export is inspected, not the draft.

## Dialects

| Dialect | The material | Departs from Swiss |
|---|---|---|
| *the mother tongue alone* | Argues, reports, testifies, surveys, counts, or lists | — |
| [De Stijl](references/themes/swiss/dialects/de-stijl.md) | Relates: parts whose proportions and balance are the subject | Black bars and primary planes in equilibrium |
| [Bauhaus](references/themes/swiss/dialects/bauhaus.md) | Explains structure: how parts, geometry, or proportion work | One primitive at changing scale, one primary, bars |
| [Brodovitch](references/themes/swiss/dialects/brodovitch.md) | Seduces: fashion, beauty, portraits, exhibitions, where the image is the subject | Didot type colliding with a daring crop; spreads paced like film |
| [Polish Poster School](references/themes/swiss/dialects/polish-poster.md) | Interprets: a cultural subject that wants a point of view | One authored, hand-made metaphor |
| [Ulm](references/themes/swiss/dialects/ulm.md) | Coordinates: instructions, wayfinding, a system of related messages | Rules for every case; color and pictograms as codes |
| [Swiss Punk](references/themes/swiss/dialects/swiss-punk.md) | Provokes: culture and music that should feel rebellious, still readable | The grid tested by rotation, layering, and stepped type |
| [Memphis](references/themes/swiss/dialects/memphis.md) | Delights: products, events, youth culture that want character | Clashing colors and pattern as material |
| [Kenya Hara, ma 間](references/themes/swiss/dialects/ma.md) | Invites: one object, craft, or ceremony, few words | Emptiness as the vessel; small, quiet type |
| [Swiss Brutal](references/themes/swiss/dialects/brutalist.md) | Specifies: a technical system whose structure is the content | Visible grid rules, zero radius, dense ledger rows |

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
  forms.md            what each unit makes the reader do
  themes/swiss/       mother tongue · master methods · 21 variations · 9 dialects · anti-patterns
  craft/              type · color · grid · imagery · data · copy · motion
```

Every file serves one decision in the eight-step Practice of `SKILL.md`: brief, reader, material, move, system, sequence, make, inspect. A change goes to the file of the decision it changes; a new file only for a new decision; no file depends on a later step.

## 中文

Folio 是给 AI agent 用的设计 skill：PPT、海报、网页、画布、手册，做出瑞士风，不再一眼 AI 味。

13 条设计哲学，一套瑞士母语，瑞士大师方法，21 种变奏，9 种方言。方言是有名有姓的设计运动，管整件作品的美学：风格派、包豪斯、Brodovitch 时尚杂志、波兰海报学派、乌尔姆、瑞士朋克、孟菲斯、原研哉（ma 間）、粗野主义。大师方法是大师们在瑞士语法里琢磨出的单页招式：Crouwel 的格子造字、Gerstner 的程序规则、Isotype 符号计数、Vignelli 的 Unigrid、字穿图，任何方言都能调用。以后加新主题，带上自己的母语、方法、变奏和方言即可；形式、载体、工艺各主题共用。

没有点名时按内容在做什么选方言，格式从不决定方言；点名了风格或人物，就照它的谱系走。安装方式同上。

## License

MIT. No fonts are bundled; each keeps its own license.
