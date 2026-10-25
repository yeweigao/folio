# Anti-patterns

Why defaults fail, and what to do instead. "Evidence" names a concrete failure of legibility, navigation, honesty, or production; test the actual result. "House" names a Swiss preference, which the brief or brand may override. A style choice alone is not a failed quality check.

## Layout

| Pattern | Why it fails | Instead | Basis |
|---|---|---|---|
| Centered hero, three equal cards, gradient button, logo wall | The most common generated page; says nothing about this subject | A flush-left claim, one supporting sentence, one action; the real product or number on the first screen | house |
| Equal boxes despite unequal importance | Equal space erases real priority | Rank by area when priority differs; equal peers may use equal spans and repeated structure | house |
| Floating rounded cards, cards in cards | The box replaces the grid; corners and shadows carry no meaning | Remove the box; separate with a solid field, a 3 px rule, or a 1 px rule; rank by area and weight | house |
| KPI tiles | Each number floats without baseline, period, or meaning | A typographic ledger: value, baseline, period, change, source, hairlines | house |
| An icon on every bullet; icon walls | Pictures stand in for hierarchy and add no information | No icons on text units; one consistent pictogram set only where readers need fast, language-free recognition | house |
| Centering by default | Symmetry is the absent decision; it weakens the reading line | Flush left, asymmetric spans; center only with a stated reason | house |
| Snake columns for ordered content | The order breaks across the Z | One axis, one direction | evidence |
| 01 / 02 / 03 on unordered content; giant watermark numbers | Implies a structure that does not exist | Number only real sequences, in reading order | house |
| Accidental gaps or filler panels added to hide them | Leftover reads as unfinished; filler reads as noise | Give space a job: group, separate, or focus. Adjust scale, position, or grouping; never fill a gap merely because it is empty | house |
| Two whole dialects on one page | Competing systems weaken the shared voice | One primary dialect; a guest contributes one move where the content earns a variation | house |

## Surface and color

| Pattern | Why it fails | Instead | Basis |
|---|---|---|---|
| Purple-blue gradients, glow, glass, drop shadows, fake 3D | Familiar effects can substitute for a subject-specific decision | Fields of paper, ink, or accent; depth through scale and field changes. If effects are requested, measure text contrast on the composite | house |
| Greys invented per component | Every box gets its own grey; the page turns into cards | Greys declared once in the palette (ink opacity or theme tokens) | house |
| Several accents, or one accent assigned to unrelated roles | Emphasis loses its meaning | Declare color roles; build hierarchy with weight, position, and scale too | house |
| Cream or warm paper on screen by habit | A palette convention stands in for a decision | Swiss defaults to white on screen; a brand or subject may call for another ground. Measure the actual text/background pairs | house |
| Fake luxury: gold gradients, glassmorphism, dark pages with glowing outlines, widely spaced serif capitals | The stereotype of expensive, not expense | Proportion, space, real photography, one accent | house |

## Type and copy

| Pattern | Why it fails | Instead | Basis |
|---|---|---|---|
| Inter or system fonts by default; extra fonts or colored text as hierarchy | Reads as unchosen; hierarchy without a system | One declared family; hierarchy by size, weight, position, space | house |
| A small colored eyebrow above every heading; tiny letterspaced capitals | Repeated chrome adds a competing hierarchy | Let headings stand alone; retain kickers and running heads when they navigate, at the surface's legible size | house |
| Filler verbs, "not just X but Y", em-dash drama, emoji | Rhetoric replaces information and reads as generated | Concrete actions, objects, numbers, dates | house |
| Decorative English on Chinese pages (STRATEGY, VOL.01) | Carries no information; signals "design" rather than meaning | Include English for real readers or necessary terminology, with a deliberate language hierarchy | house |
| A giant word with no claim behind it | Remove the word and nothing is left | Giant type carries a repeatable claim plus a fact or an action | house |
| Fake editorial: drop caps, quote walls, decorative folios, "Vol. 01" | Magazine skin standing in for an argument | Action titles, evidence, captions, and sources first; folios and sections only where they navigate | house |

## Charts and data

| Pattern | Why it fails | Instead | Basis |
|---|---|---|---|
| Pie, donut, gauge for precise comparisons | Angles and arcs make close differences harder to compare | Bars on a shared baseline; progress as a number on a ruler | evidence |
| Dual Y axes implying a relationship through arbitrary scaling | An apparent crossing or correlation can be manufactured by changing the axes | Aligned panels, or series indexed to an explicit common base; scatter plots keep their independent X and Y quantities | evidence |
| A chart on a white card with a legend and a grey plot area | The card is a box; the legend makes readers look twice | A transparent plot on the page; direct end labels | house |
| Invented numbers ("99.9% uptime", "300% growth"); unlabeled demo data | Deception, not design | Real data with a source; otherwise a visible placeholder; demo values marked `illustrative` with their arithmetic | evidence |
| Deliverable text baked into images | It cannot be edited or accessed as text | Keep authored reading text live; source screenshots and documentary lettering may remain images with accessible context | evidence |

## Images and motion

| Pattern | Why it fails | Instead | Basis |
|---|---|---|---|
| Generated photos of people, places, or products presented as real | Fabricated evidence | Real material, a labeled placeholder, or type and geometry for mood | evidence |
| Parallax, fly-ins, floating backgrounds, fade-up on every block | Repeated effects can compete with content | Motion for state, feedback, or one deliberate expressive moment; keep content available without it and honor reduced motion | house |
| Text below the surface's size or contrast floor; required motion without an accessible alternative | Content becomes difficult or impossible to perceive | Measure the real composite and viewing size; preserve meaning with motion reduced | evidence |
| Unreadable experiments: rotated body text, type over busy photographs, 2:1 contrast | The experiment is paid for by the reader | Experiment only in the display voice; body upright, legible, ≥ 4.5:1 | evidence |

## Habit

Models also converge on newer defaults: a cream background with a high-contrast serif and a terracotta accent; a near-black page with one acid-green or vermilion accent; a broadsheet of hairlines, zero radius, and dense columns. The last two overlap with the Swiss theme's own vocabulary, which is exactly why they need a reason each time. If the plan could be described without mentioning this brief's subject, it is a default, not a decision.
