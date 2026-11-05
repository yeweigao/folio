![Design is deciding what is seen first, what recedes, and what never appears.](assets/hero.png)

# Folio

**Master-level design for AI agents.** A skill that art-directs slides, posters, websites, canvases and handbooks in the hand of a named school, so they read as designed, not generated, and writes each world's aesthetic skeleton as a DESIGN.md.

[Install](#install) · [How it works](#how-it-works) · [Themes](#themes) · [中文](#中文)

![Nine dialects on one programme](references/themes/swiss/examples/dialects.png)

## What changes

| Left to itself, a model reaches for | With Folio |
|---|---|
| A cream ground, black, one vermilion | Ground and accent from the hand and the subject |
| The subject's most literal pictogram | A structure found in the subject and built in code |
| A named style as costume | The master's way of working: first move, tools, material, procedure |
| Kickers, 01/02/03, mono labels, a navy closing slide | Hierarchy by type and scale; chrome only with a job |
| A rendered object standing in for material | Real material, or an honest placeholder |
| Grading its own work | Critics who did not make it, and a judge |

## How it works

- **The author's eye.** Thirteen lines of philosophy outrank everything else.
- **Names carry methods.** A master is summoned by name and practised by his way of working.
- **Three layers, one voice.** The philosophy is the eye no school bends; the theme is the grammar; a dialect overturns only the rules it names. Each DESIGN.md merges them into one world.
- **Routes, not steps.** SKILL.md says which file each moment opens, the theme before the first mark; the agent plans its own route.
- **A skeleton per world.** A DESIGN.md written for the agent that makes the next piece: method before look, values last, no content; another piece of the world can be made from it alone.
- **Floors by machine.** Facts verbatim, contrast, live text, the export against its tokens.
- **Tested against no skill.** Fixed briefs, a light maker, a blind judge. In 1.0, Folio placed first on all five briefs against 0.9.0 and no skill.

## Themes

A theme is a school with its masters, grammar and dialects; SKILL.md holds only what is true under every theme. **[Swiss](references/themes/swiss/theme.md)**, the International Typographic Style, suits material that argues, reports, counts or lists. **[Apple](references/themes/apple/theme.md)** draws on its public marketing and launch language for product, feature and launch work; it is not official interface guidance. An explicit direction or selected reference takes precedence.

Apple combines an optional industry dialect with a Keynote, Store or Editorial surface when applicable; Bento is a feature-grid method. Its theme routes these choices and their precedence. The existing Swiss dialects are:

| Dialect | The material | Departs from Swiss |
|---|---|---|
| [De Stijl](references/themes/swiss/dialects/de-stijl.md) | Relates: compositions, paragraphs, comparisons and sequences | Drawn fields organize reading; strict Mondrian and contemporary reference applications have explicit boundaries |
| [Bauhaus](references/themes/swiss/dialects/bauhaus.md) | Celebrates or explains, where point, line and plane can build the subject | Elements as forces built into a figure; primaries mixing only where parts meet |
| [Brodovitch](references/themes/swiss/dialects/brodovitch.md) | Seduces, where people or images are the subject | Black-and-white photographs under the subject's own colour; figure cut against the word |
| [Polish Poster School](references/themes/swiss/dialects/polish-poster.md) | Interprets a cultural subject | One authored metaphor, two things in one hand-made form |
| [Ulm](references/themes/swiss/dialects/ulm.md) | Coordinates a system of messages | Rules before cases; colour and pictograms as codes |
| [Swiss Punk](references/themes/swiss/dialects/swiss-punk.md) | Provokes, still readable | The grid tested by rotation, layering, stepped type |
| [Memphis](references/themes/swiss/dialects/memphis.md) | Delights | Clashing colour, a constructed vocabulary and fields made from tiles, partitions, letters or projected parts |
| [Kenya Hara, ma 間](references/themes/swiss/dialects/ma.md) | Invites: one object, craft or ceremony | The charged interval, in space and in time |
| [Swiss Brutal](references/themes/swiss/dialects/brutalist.md) | Specifies: structure is the content | Structure shown, material as found |

## Install

Any agent that reads Agent Skills:

```
npx skills add yeweigao/folio
```

Claude Code, for every project:

```bash
git clone https://github.com/yeweigao/folio ~/.claude/skills/folio
```

Claude apps: zip the folder, then go to Customize → Skills → + → Upload a skill. Code execution must be on.

`render.py` needs Playwright; `contact.py` and `measure.py` need Pillow. Every other script uses only the Python standard library.

## Use

> Turn this report into a board deck.

> Make the poster series for our concert season.

> 这张海报太 AI 味了，重做一版，用 ma 間。

## Structure

```
SKILL.md          goal · philosophy · routes · themes (v1.1.0)
references/       design-md · review · tools · craft · signature · steering
  surfaces/       slides · poster · web · canvas · handbook
  themes/swiss/   theme · 9 dialects · examples
  themes/apple/   theme · industry dialects · surfaces · Bento · example skeletons
scripts/          render · contact · factcheck · folio-check · imagecheck · preview · extract · measure · release-check · generators
tests/            fixed briefs for judging changes
CONTRIBUTING.md   laws, contracts and releases for changing the skill
```

[De Stijl report examples](references/themes/swiss/examples/de-stijl/README.md): 69 reference reconstructions, five standalone worlds and 15 new-content reading, table and timeline pages.

[Memphis examples](references/themes/swiss/examples/memphis/README.md): 28 reconstructions, ten extracted worlds and independent same-world transfer tests.

## 中文

Folio 是给 AI agent 用的设计 skill,覆盖 PPT、海报、网页、画布和手册,以具名流派和大师的做法做出大师水准(主题包括瑞士国际主义与 Apple 产品营销语言),并把每个世界的审美骨架写成一份 DESIGN.md。

- **作者的眼光**:13 条设计哲学凌驾一切。
- **名字带方法**:大师以名字召唤,以他的做法实践。
- **三层合一**:哲学是眼睛,任何流派都改不了;主题是语法;方言只推翻它点名的规则。每份 DESIGN.md 把三层合成一个世界。
- **给路由,不给步骤**:什么情况打开哪个文件,动手前必读主题;路线由 agent 自己定。
- **骨架不含内容**:同一个世界的下一件作品,只凭骨架就能做出来。
- **底线由机器检查**:事实、对比度、活字。

### 世界观

用洪荒来讲最好懂。

- **大道**:SKILL.md 的 13 条设计哲学。在一切之上,任何流派都改不了;每一次评判,都要说出它依据的是哪一条。
- **天条**:review.md 的底线,包括事实、对比度、活字、授权。不论在哪一方天地,都不能破。
- **天道**:主题。第一方天地由瑞士国际主义主理,如同鸿钧合道,定下网格、字体、色彩的秩序。它只管关系,不管样子,所以容得下众多道统。Apple 主题也是同一哲学之下的另一套视觉语法。
- **圣人道统**:方言。每个流派在天道之中立自己的道统,只改它点名的那几条,其余照天道运行;主题列出的保留规则就是它不改的部分。
- **门人与客卿**:hand。一门之中由一位主事,其余只出一招。召唤名字,召来的是功法(做法),不是法相(样子)。
- **小世界**:每份 DESIGN.md。把大道、天道、道统合成一部天道,只写规矩,不写众生,脱离洪荒也能自行运转。
- **众生**:每件作品和它的 brief。众生各有其事,但都守所在世界的天道。一件作品要例外,就在 brief 里写明缘由;所有作品都要的例外,先改天道。要换一个流派,就是另开一方世界。
- **着相**:caricature。只修其形,不修其法,是披着大师外衣的空壳。

## License

MIT for the skill and code. Example font assets retain their own licenses and accompanying notices; supplied reference works are not covered by this code license.
