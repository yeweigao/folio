# Craft

Shared technique for every theme and surface: the theme sets relationships and finish, the surface sets sizes.

## Grid

Without a grid, layouts fall back to equal thirds and centered stacks.

- **Solve the grid from the format.** Content = n × column + (n − 1) × gutter; zero-based column k starts at margin + k × (column + gutter). The surface gives starting dimensions.
- **Tracks are construction lines, not columns to fill.** Equal spans for real peers, unequal spans for real priority; never invent priority to avoid symmetry. Subdivide only for an alignment the content needs; an unused track is not a vacancy.
- **Axes are shared.** Image edges, title starts, captions, and sources repeat the alignments their relationships need.
- **Spacing has declared steps:** within a group, between groups, between sections; the theme sets the ratios; baselines follow leading.
- **Alignment is optical.** Round and pointed forms overshoot; quotes and points hang; large titles compensate for side bearing.

| Reading need | Composition | Invariant |
|---|---|---|
| Compare peers | Equal spans, criteria in shared rows | Row alignment, units, scales |
| Read with evidence | Unequal spans for reading and support | Text and evidence share an anchor |
| Annotate | Narrow note track beside the reading column | Each note beside its passage |
| Argue | Claim, evidence, implication | One reading axis, claim before evidence |
| Survey | Contact sheet | Comparable crops, aligned caption baselines |
| Carry a brand | A unit derived from the actual mark | Its proportions and clear space |

## Type

AI typography fails by sloppiness, not font choice: too many sizes, no weight logic, wrong punctuation, CJK set like Latin.

- **Three roles: display, body, label.** Add a level only for a real navigation task; skip every intermediate size the content does not need; judge the hierarchy at thumbnail and at viewing size.
- **When type leads, start at graphic scale,** the title or key word spanning the frame.
- **Choose one hierarchy for the deliverable,** declaring size and weight together:

| Hierarchy | Relationship | Watch |
|---|---|---|
| Weight leads | Regular text, distinctly heavier headings | Heavy elements compete; leave one lead |
| Scale leads | Large light display, ordinary body, sturdy small text | Fine strokes fail in projection and small print |
| One weight | Size, position, and space carry everything | Small steps collapse |

- **Weight is judged by eye.** One family's 700 is not another's; one reading and one emphasis weight; small text needs stroke, not bold; thin display is judged at the final distance.
- **Measure follows the reader** (Latin ≈ width ÷ (0.5 × size); CJK ≈ width ÷ size):

| Role | Latin chars | CJK chars | Leading |
|---|---|---|---|
| Body | 45–75 | 25–40 | 1.5–1.75 |
| Lead | 40–60 | 22–32 | 1.5–1.6 |
| Display | 8–20 | 4–12 | 0.95–1.12 |
| Caption | 30–50 | 18–28 | 1.4–1.5 |

- **Lines break by meaning.** Titles in balanced lines; headings, labels, and cells follow their content; no widows or orphans. CJK breaks between any two characters, so set breaks by hand at phrase boundaries.
- **Spacing is designed.** Body keeps the font's spacing; display tracking follows the letterforms; the CJK–Latin gap is 1/8–1/4 em, from the font or the renderer; where the renderer adds none, as in PPTX, one typed space of that width; never both.
- **Punctuation is exact.** Align by reading task; justify only with language-aware spacing; no closing punctuation at a line start or opening at a line end. English: curly quotes, en dash for ranges, true minus, no em dash as a pause. Chinese: one quotation style, ——, ……, 《》 only for titles of works. Tabular figures in tables, proportional in display; a thin space before a unit, none before %.

### Faces

A new font is not a substitute for a stronger composition. Start from a working pair; add a display face only when its voice changes the meaning. A CJK/Latin pair is one voice: set real headings, paragraphs, numerals, and punctuation in both scripts, match apparent size, density, and baseline, and use the locale's own resources (SC, TC, JP, KR).

| Job | Chinese | Latin | Stack |
|---|---|---|---|
| Explain, navigate, compare | Source Han Sans SC | Inter | `"Inter", "Source Han Sans SC", "Noto Sans SC", sans-serif` |
| Read an argument | Source Han Serif SC | Source Serif 4 (optical sizes) | `"Source Serif 4", "Source Han Serif SC", "Noto Serif SC", serif` |
| High-contrast cultural display, when called for | A display cut of the Song face | Bodoni Moda | `"Bodoni Moda", "Source Han Serif SC", "Noto Serif SC", serif` |

- **Titles inherit the reading family** and change scale, weight, line break, and position first; labels may keep the explanation pair inside a serif book.
- **A fallback is resolved, not accepted.** These pairs are defaults, not required installs: choose installed faces with the right scripts and weights (Helvetica Neue + PingFang SC, Arial + Microsoft YaHei, Georgia + Songti SC, or Noto CJK), reflow, and report the substitution. Installing or embedding fonts: [fonts](fonts.md).

## Color

- **Roles, not swatches.** Define ground, text, muted, emphasis, and line once; choose foreground lightness per ground and try dark ink on bright fields. A hairline separates; it never sets text.
- **Color comes from the brand or the subject, not a topic cliché.** Keep specified brand colors; choose a readable foreground before changing a brand field.
- **Measure the composite, not the opacity.** Thin strokes and long reading need more margin than the floor.
- **Hierarchy survives greyscale.** Greyscale tests hierarchy, not contrast.
- **Print:** the printer's profile, stock, and ink limit govern; 100K for small text and hairlines; rich black only where the printer allows; spot colors when specified; proof out-of-gamut accents.

Starting calibration, measured per pair before use: paper `#FFFFFF`, ink `#111111`, muted `#625F59` (≈ ink 62%), secondary ink 78%, hairline `#C5C2BC` (≈ ink 12–16%), dark turn `#141414` with white; interface disabled ink 38%, hover 8%.

Named starting points are screen approximations: print needs the physical swatch, and unrounded values are tested against the floors. A signature color in its owner's category reads as imitation; a Pantone color of the year dates the work.

| Name | Value | As a field, text in | As text on white | Character and caution |
|---|---|---|---|---|
| International Klein Blue | `#002FA7` | white 10.7:1 | yes | Yves Klein's ultramarine; absolute, artistic |
| Prussian blue | `#003153` | white 13.4:1 | yes | The blueprint; engineering, archives |
| Majorelle blue | `#6050DC` | white 5.7:1 | yes | Majorelle's garden; warm, vivid |
| Classic Blue (Pantone 19-4052, 2020) | `#0F4C81` | white 8.9:1 | yes | Steady, institutional |
| British racing green | `#004225` | white 11.6:1 | yes | Heritage, engineering |
| Tiffany Blue (Pantone 1837) | `#0ABAB5` | ink 7.8:1 | no (2.4:1) | Celebration; a trademark, never for jewelry or gifts |
| Marrs green | `#4BACA5` | ink 7.0:1 | no (2.7:1) | G. F Smith's 2017 favourite; the Chinese web often circulates a deeper teal under this name |
| Hermès orange | ≈ `#F37021` | ink 6.4:1 | no (2.9:1) | Approximation, no official value; never to evoke luxury packaging |
| International orange | `#FF4F00` | ink 5.7:1 | large only (3.3:1) | Aerospace, infrastructure |
| Rosso corsa | `#E4002B` | white 4.8:1 | just | Speed, competition |
| Cartier red | `#D50032` | white 5.4:1 | yes | Ceremony, gift |
| Folio vermilion | `#C83024` | white 5.4:1 | yes | Poster red; carries white text |
| Viva Magenta (Pantone 18-1750, 2023) | `#BB2649` | white 6.0:1 | yes | Bold, carmine-based |
| Shocking pink | `#FC0FC0` | ink 5.4:1 | large only (3.5:1) | Schiaparelli; surreal, fashion |
| Very Peri (Pantone 17-3938, 2022) | `#6667AB` | white 5.1:1 | yes | Digital, playful |
| Peach Fuzz (Pantone 13-1023, 2024) | `#FFBE98` | ink 11.8:1 | no | A field rather than a mark |
| Mocha Mousse (Pantone 17-1230, 2025) | `#A47864` | ink 4.9:1 | large only (3.9:1) | Earth, comfort |
| Illuminating (Pantone 13-0647, 2021) | `#F5DF4D` | ink 14.0:1 | never | A marker, not a text color |
| Folio signal yellow | `#F5C84B` | ink 11.9:1 | never | Fields and markers |
| Cloud Dancer (Pantone 11-4201, 2026) | `#F0EEE9` | ink 16.3:1 | — | A soft white ground, not an accent |

## Copy

AI copy is as recognizable as AI layout.

- **Words come before layout.** An argument needs claim, evidence, implication, action; a claim without evidence becomes a question or goes. Covers identify; reference units label and order.
- **Wording is a service; verbatim means verbatim.** Where editing is allowed, a vague title becomes a claim and a paragraph a line; edit for the message, never only to rescue a layout.
- **An argument title states a judgment, not a topic.** Aim for 12–24 Chinese or 40–70 Latin characters in two lines; fixed wording governs; read in order, the titles form the summary. Covers, tables, reference, and navigation keep descriptive titles.
- **Concrete, not inflated.** Replace each tell with the action, object, quantity, or date; if nothing concrete remains, the sentence had no information.
  - Words: elevate, seamless, unleash, empower, revolutionize, cutting-edge, game-changing, unlock; 赋能, 一站式, 打造, 引领, 闭环, 抓手, 颠覆.
  - Shapes: "not just X, it's Y"; three adjectives in a row; "Imagine a world where"; rhetorical questions; "In today's fast-paced world"; "We believe".
  - Marks: dramatic em dashes, exclamation marks, suspense ellipses, emoji. Buttons: "Learn more", "Get started", "Submit".
- **One idea per sentence.** Active voice; review sentences past 35 Chinese characters or 25 English words.
- **Voice comes from sentence length, verbs, and density, not adjectives.**
- **Languages follow their readers, not decorative rank.** Equal-status languages share a hierarchy; a subordinate translation fits its role and the size floor; no decorative English on Chinese pages.

## Data

A chart answers a question or shows a finding; a table serves lookup. For an argument, start from the consulting exhibit (Zelazny's *Say It With Charts*, Minto's pyramid, Tufte's data-ink, IBCS): action title, unit line, chart, source and notes. Exploration and lookup titles name the question or measure.

| Question | Use | Not |
|---|---|---|
| Which is bigger | Bars (long labels), columns (short) | Pie, donut, 3D |
| How it changed | Line; area when magnitude from zero matters | Unmarked scale changes, invented smoothing |
| How it is distributed | Histogram, box, strip plot | A lone average |
| Whether two things relate | Scatter | Correlation sold as cause |
| What it is made of | Stacked or 100% bar | Pie, treemap without hierarchy |
| How a total moved | Waterfall, signed variance bars | Two pies |
| Share and size at once | Marimekko | Bubble clouds |
| How far from a baseline | Diverging bar | Gauge |
| How uncertain | Intervals, error bars | Bare points |
| Many small groups | Small multiples | Twelve lines in one plot |

- **Geometry is honest.** Bars from zero; cut axes marked; shared comparisons on shared scales; aligned panels rather than dual axes, and any separate axes name their units and scales. Grid lines aid reading without competing.
- **Emphasis follows the reading task, not what is newest or largest.** Context recedes without hiding required comparisons; meanings stay consistent; a non-color cue always.
- **Label directly;** a legend only where it reads more clearly. Annotate what the question needs; order by value or the reader's lookup logic.
- **Notation is declared once.** With IBCS: actual solid, earlier periods lighter, plan outlined, forecast hatched. Sequential data steps lightness; diverging data splits at a midpoint; never red–green alone.
- **Precision serves the decision.** Percent is not percentage points; rates name their denominator; missing is not zero.
- **Tables:** numbers aligned on the decimal, units in the header, totals distinguished; reference tables keep stable widths, order, and repeated headers.
- **A dashboard is a ranked scan, not a gallery of cards** (Few, *Information Dashboard Design*). Rank the questions, then spend position, size, and accent in that order; a row of big-number cards is a default, not a hierarchy. A value someone acts on is a number, a direction is a chart, a value without a comparison is noise; a measure and its comparison form one module, as wide as its content. Accent marks real exceptions, not every module; status has explicit labels and a redundant code. A narrative leads with one question; a monitor holds a layout that never moves; both show source and as-of time. Exemplars: Hilfiker's SBB clock, the FOPH Covid-19 dashboard, the *Financial Times* and *NZZ* data desks.

## Imagery

| Job | Contributes | Must carry |
|---|---|---|
| Evidence | A place, product, person, interface, result | Caption (who, what, where, when, source) and a traceable origin |
| Explanation | A diagram, map, pictogram, process, mechanism, or a story that is the content | One drawing style for the piece, labels as live text |
| Atmosphere | Setting, material, light, feeling | Honesty that it is atmosphere, never proof |

| Source | Serves | Constraint |
|---|---|---|
| The user's own photographs and screenshots | Evidence, atmosphere | Crop and correct; never alter what it proves |
| Generated by AI | Declared atmosphere or illustration | Distinct from documentary evidence; live lettering; one prompt grammar in the theme's image register; credited as generated |
| Found: the subject's own site, museums, archives, Wikimedia, Openverse | Evidence, atmosphere | License checked and credited; search the subject's world, not "premium" |
| Drawn in code | Explanation, authored illustration | The theme's drawing grammar and color roles; labels as live text |
| Type and color alone | When imagery is optional | Better than an image doing the wrong job |

- **One strong image, not four weak ones.** Missing required imagery gets a labeled placeholder, reported if unresolved at delivery.
- **The crop serves the subject:**

| Relationship | For | Check |
|---|---|---|
| Contained | An object or document seen whole | Nothing lost to the frame |
| Edge to edge | A gesture, place, or material that composes the page | The crop strengthens the subject |
| Beside reading | Explanation with a visual counterpart | Text keeps its measure |
| Across a spread | A scene whose breadth matters | One coordinate system; subject clear of the seam |
| Type across image | A short statement whose form is the idea | One legible gesture |

- **Faces, hands, and marks are never cut by accident.** The theme sets media, crop families, edges, and finish.
- **Separate the foreground, preserve the image.** Placement, text tone, or local backing, scrim, or halo, altering only the area reading requires; check every text region on the final composite, across crops and states.
- **Captions carry facts, not mood.** Source on its own line; unknown says unknown.
- **Resolution is computed:** pixels = mm ÷ 25.4 × dpi; print 300 dpi at placed size, large formats ≥ 150, web at 2×.
- **People never become fabricated evidence.** Fictional figures are declared; real customers and documentary subjects are traceable; consent from vulnerable subjects; hardship is never mood; no identifiable children without authorization.
