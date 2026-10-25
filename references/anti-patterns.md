# Anti-patterns

Why each default in SKILL.md's Avoid list fails, and what to do instead. "Evidence" means the harm is measurable (legibility, accessibility, honesty, production); "house" means it is the Swiss theme's preference, which another theme may decide differently. The distinction matters when a user asks for one: house rules yield readily, evidence does not.

## Layout

| Pattern | Why it fails | Instead | Basis |
|---|---|---|---|
| Centered hero, three equal cards, gradient button, logo wall | The most common generated page; says nothing about this subject | A flush-left claim, one supporting sentence, one action; the real product or number on the first screen | house |
| Three or nine equal boxes | Equal space erases priority; scanning becomes reading every box | Decide parallel or sequence; parallel gets unequal spans (12 / 6 / 4 / 3), four to seven blocks | house |
| Floating rounded cards, cards in cards | The box replaces the grid; corners and shadows carry no meaning | Remove the box; separate with a solid field, a 3 px rule, or a 1 px rule; rank by area and weight | house |
| KPI tiles | Each number floats without baseline, period, or meaning | A typographic ledger: value, baseline, period, change, source, hairlines | house |
| An icon on every bullet; icon walls | Pictures stand in for hierarchy and add no information | No icons on text units; one consistent pictogram set only where readers need fast, language-free recognition | house |
| Centering by default | Symmetry is the absent decision; it weakens the reading line | Flush left, asymmetric spans; center only with a stated reason | house |
| Snake columns for ordered content | The order breaks across the Z | One axis, one direction | evidence |
| 01 / 02 / 03 on unordered content; giant watermark numbers | Implies a structure that does not exist | Number only real sequences, in reading order | house |
| Leftover space (content bunched at the top, the bottom half empty) or filler panels added to hide it | Leftover reads as unfinished; filler reads as noise; neither is structure | Placed space has an axis and a focus and ends on a grid line. Fix leftover space by changing one grid variable (anchor size, scale contrast, start line, anchoring to the foot) or by splitting or merging units; never add a panel | evidence |
| Two dialects on one page | Style soup: no voice survives | One dialect per piece; fusion belongs in defining a dialect, not in a project | house |

## Surface and color

| Pattern | Why it fails | Instead | Basis |
|---|---|---|---|
| Purple-blue gradients, glow, glass, drop shadows, fake 3D | The visual signature of generated UI; gradient text makes contrast unstable | Fields of paper, ink, or accent; depth through scale and field changes; a neutral scrim only for legibility on photographs | evidence |
| Greys invented per component | Every box gets its own grey; the page turns into cards | Greys declared once in the palette (ink opacity or theme tokens) | house |
| Several accents, or one accent used for titles, buttons, and lines at once | Nothing reads as the exception; greyscale shows no hierarchy | One accent with one meaning; hierarchy from ink, weight, position | evidence |
| Cream or warm paper on screen | Projectors wash it out; it is now a generated-design default itself | Pure white on screen; warm stock only in print, as the paper | evidence |
| Fake luxury: gold gradients, glassmorphism, dark pages with glowing outlines, widely spaced serif capitals | The stereotype of expensive, not expense | Proportion, space, real photography, one accent | house |

## Type and copy

| Pattern | Why it fails | Instead | Basis |
|---|---|---|---|
| Inter or system fonts by default; extra fonts or colored text as hierarchy | Reads as unchosen; hierarchy without a system | One declared family; hierarchy by size, weight, position, space | house |
| A small colored eyebrow above every heading; tiny letterspaced capitals | The single most common generated-page tell; small size plus wide tracking reduces legibility | Let the heading stand alone; kickers and running heads only as furniture, at legible sizes (≥ 12 px on screen, ≥ 8 pt in print) | evidence |
| Filler verbs, "not just X but Y", em-dash drama, emoji | Rhetoric replaces information and reads as generated | Concrete actions, objects, numbers, dates | house |
| Decorative English on Chinese pages (STRATEGY, VOL.01) | Carries no information; signals "design" rather than meaning | English only for real bilingual readers, at equal standing | house |
| A giant word with no claim behind it | Remove the word and nothing is left | Giant type carries a repeatable claim plus a fact or an action | house |
| Fake editorial: drop caps, quote walls, decorative folios, "Vol. 01" | Magazine skin standing in for an argument | Action titles, evidence, captions, and sources first; folios and sections only where they navigate | house |

## Charts and data

| Pattern | Why it fails | Instead | Basis |
|---|---|---|---|
| Pie, donut, gauge | Angles compare far worse than lengths | Bars on a shared baseline; progress as a number on a ruler | evidence |
| Dual axes | Readers treat the crossing as a conclusion | Two charts on one baseline, or both indexed to 100 | evidence |
| A chart on a white card with a legend and a grey plot area | The card is a box; the legend makes readers look twice | A transparent plot on the page; direct end labels | house |
| Invented numbers ("99.9% uptime", "300% growth"); unlabeled demo data | Deception, not design | Real data with a source; otherwise a visible placeholder; demo values marked `illustrative` with their arithmetic | evidence |
| Text baked into images | Uneditable and inaccessible | Geometry in the image, text as live text on top | evidence |

## Images and motion

| Pattern | Why it fails | Instead | Basis |
|---|---|---|---|
| Generated photos of people, places, or products presented as real | Fabricated evidence | Real material, a labeled placeholder, or type and geometry for mood | evidence |
| Parallax, fly-ins, floating backgrounds, fade-up on every block | Motion takes attention from content and breaks reduced-motion settings | Motion only for state change, ≤ 300 ms, `transform` and `opacity`; one orchestrated moment at most | evidence |
| Unreadable experiments: rotated body text, type over busy photographs, 2:1 contrast | The experiment is paid for by the reader | Experiment only in the display voice; body upright, legible, ≥ 4.5:1 | evidence |

## Habit

Models also converge on newer defaults: a cream background with a high-contrast serif and a terracotta accent; a near-black page with one acid-green or vermilion accent; a broadsheet of hairlines, zero radius, and dense columns. The last two overlap with the Swiss theme's own vocabulary, which is exactly why they need a reason each time. If the plan could be described without mentioning this brief's subject, it is a default, not a decision.
