# Signature — the methods that carry a master's hand

The Methods matrix in the theme lists every cell at one price. That is a
lie of the table format: most cells are baseline craft — any competent
studio does them, and doing them well makes a work correct, not
recognisable. The methods below are the other kind: a master's name is
legible in them. They are tiered above the matrix.

- **One signature programme per deliverable** (SKILL.md, Lock): a single
  signature method, built to its card, governing the whole work — not a
  different flourish per unit. Its card is re-read at Make with the unit
  brief, and Inspect runs the card's Test.
- **A signature method without its parameters is not locked.** The card
  gives the construction and the numbers; DESIGN.md's citation carries
  both, as with tokens.
- **Generators exist for the computable cards** (Isotype, Ledger is
  baseline, Programme): use `scripts/generators/` where a card names one.
  A drawn imitation of an algorithmic move is a fake.

## Graphic scale — Müller-Brockmann (*Der Film*, *musica viva*)

**Construction.** One word or figure is set so large it becomes the
composition's architecture; everything else is apparatus at label or
body size, flush to one axis. The large element is chosen from the
content (the verdict word, the decisive figure), never a decorative word.
**Parameters.** Display-to-body size ratio ≥ 6:1; the large element spans
≥ 8 of 12 columns or the full measure; at most one graphic-scale element
per unit; apparatus stays within the type ramp's two smallest roles.
**Test.** Squint at the unit: one thing is read first, at three times the
distance anything else survives. Cover the large element — the unit has
no composition left, only text.
**Caricature.** A big number beside a normal layout; a giant watermark
word behind body text; size used on a word that carries no claim.

## Grid alphabet — Crouwel (*New Alphabet*)

**Construction.** Display letterforms are built, not typed: strokes are
segments of the unit's own module grid, drawn as vector shapes at a
declared cell size; counters and curves are resolved by the grid's
logic, consistently across every letter used. The readable title also
stands in live text (floors).
**Parameters.** One cell module for all constructed letters (e.g. 8px
grid, letters 5×7 cells); only display words are constructed — never
body text; the construction grid is the layout grid or an exact multiple.
**Test.** Overlay the module grid: every stroke of every letter falls on
it, and the same letter is the same drawing everywhere it appears.
**Caricature.** A pixel font downloaded and used as texture; letters
"inspired by" a grid but drawn freehand; constructed type for a whole
paragraph.

## Exposed grid — Crouwel

**Construction.** The grid's rules are drawn on the page at hairline
weight in the line color, quieter than any text; columns, master lines,
and the baseline rhythm the content actually used stay visible as the
work's structure. Only tracks that carry something are drawn.
**Parameters.** Rules at 1px / 0.5pt, line color, never ink; text keeps
its full contrast against paper, rules never compete (squint test
below); a heavier ink rule only opens or closes a table.
**Test.** Squint: the text reads first, the rules second. Remove a rule —
a real boundary disappears with it.
**Caricature.** A full lattice wallpaper behind an ordinary layout;
rules at text weight; a grid drawn that the layout does not use.

## Isotype — Neurath & Arntz

**Construction.** A quantity is shown as a row of equal symbols, one
symbol per declared unit (1 symbol = 10,000 people), rows aligned to a
shared start; a remainder smaller than one unit is shown as a partial
symbol, cut — never shrunk. A key states the unit once. Generator:
`scripts/generators/isotype.py` produces the rows as SVG from values.
**Parameters.** One symbol size for the whole deliverable; unit chosen
so the largest row is 5–20 symbols; partial symbols are clipped by exact
fraction; symbols are solid silhouettes from one drawn set.
**Test.** Count the symbols and recover the numbers exactly, including
the partial. Any symbol a different size from its row fails.
**Caricature.** Emoji or icon fonts as symbols; pictograms of different
sizes to show different amounts; a legend that repeats what the rows
already say, in numbers, beside every row.

## Becher typology

**Construction.** A set of comparable subjects (products, buildings,
faces, interfaces) is photographed or rendered at the same angle, same
scale, same crop, same ground, and set in a grid on shared edges, so the
differences between them become the content. Captions are one line,
identical in form.
**Parameters.** One camera logic for the whole set: same viewpoint,
subject fills the same fraction of its frame (±10%), one ground color,
one caption position; set size 4–16; no member gets a larger cell unless
priority is real and declared.
**Test.** Shuffle test: any cell could swap with any other and the grid
still reads as one system; the eye compares subjects, never framings.
**Caricature.** A moodboard of mixed crops and angles called a typology;
stock photos of different styles in a tidy grid.

## Route line — Vignelli, Charysyn & Noorda (New York Subway Map)

**Construction.** A sequence is drawn as one continuous line through
ordered stops on the grid; stops are nodes on the line, labelled in
reading order; branches are drawn only where the sequence truly forks.
The line is straight segments at 0°, 45°, or 90°.
**Parameters.** One line weight for the route (2px screen / 1pt print),
stops as equal nodes; labels never leave the line's axis; the whole
route fits one unit or continues across units at the same height.
**Test.** A reader can trace the route with a finger without lifting it
and recite the order back; remove the labels and the order is still
legible from the line alone.
**Caricature.** A wavy decorative path with icons pinned to it; arrows
between boxes doing the line's job; a timeline with stops floating off
the axis.

## Cut-out — Brodovitch (*Harper's Bazaar*)

**Construction.** A photograph's subject is cut from its ground and set
in front of or behind display type, so type and figure compose one
shape; the cut edge is clean at final size, and reading text never sits
on the figure. One cut-out per unit; the figure is the subject, not a
decoration.
**Parameters.** The figure crosses at least one type element or the
frame edge — a cut-out that touches nothing is a sticker; edge quality
checked at 100% (no halo, no fringe); text keeps its floors against
paper, not against the figure.
**Test.** Remove the type: the photograph loses its composition. Remove
the figure: the type loses its reason. Both must hurt.
**Caricature.** A product shot with a drop shadow floating over a
headline; clip-art silhouettes; a cut-out used because the photo was
boring.

## Programme series — Gerstner & Lohse

**Construction.** A series of units is generated from a declared
programme: a small set of variables (position, size, rotation, field)
and a cycle or permutation rule produce every unit, so the family is one
idea at many states. The programme is written in DESIGN.md in one line
anyone could re-run. Generator: `scripts/generators/programme.py`
produces programme fields as SVG from a declared cycle.
**Parameters.** 2–4 variables, one rule, no hand-tuned exceptions; the
series length is set by the cycle completing or the content ending;
each state differs from its neighbours by exactly the rule's step.
**Test.** State the programme from the finished series without seeing
DESIGN.md; then predict the next unit. If you cannot, there is no
programme, only repetition.
**Caricature.** The same template with different text called a system;
randomised "generative" decoration whose rule nobody can state.

## Close-up — Herbert Matter (*Pontresina Engadin*)

**Construction.** One subject is cropped so close that a part of it
carries the whole: the crop chooses the decisive detail (the gesture,
the mechanism, the material), and the caption restores the whole the
crop removed. The image is the lead; type stays quiet.
**Parameters.** The subject fills the frame edge to edge; the cropped
detail stays identifiable from the caption alone; one close-up per
unit; resolution computed for the placed size (craft, Imagery).
**Test.** Show the crop alone: a viewer can say what it is part of and
why that part matters. If they can only say it looks nice, the crop is
decoration.
**Caricature.** A zoomed texture with no subject; a close crop that
hides what the reader needed to see; several competing close-ups.
