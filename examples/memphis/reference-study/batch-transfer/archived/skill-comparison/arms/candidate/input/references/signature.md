# Signature — the methods that carry a master's hand

Most cells of the theme's Methods matrix are baseline craft: done well, they make work correct, not recognisable. These are the other kind, the methods in which a master's name is legible.

- **One at most, only when the material calls for it.** It governs the whole piece, never a flourish per unit.
- **Built to its card.** Construction and parameters go into the skeleton; review runs the card's Test.
- **Computed where computable.** Isotype and programme series have generators in `scripts/generators/`; a drawn imitation of an algorithmic move is a fake.

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

## Halftone screen — the process image (letterpress and screen-print craft; Weingart's enlarged screens)

**Construction.** A subject — a photograph, a drawn form, or a display
word at graphic scale — is rendered as a true dot screen: one raster
of the subject feeds the screen, each dot's area is set by the tone at
its cell (tone × the subject's coverage of that cell, so edges halve
their dots), and the subject reads because the dots carry its tones.
A dissolve runs the tone from solid at one extreme — the subject
printed whole — across a declared boundary into the screen, fading
with distance until the subject ghosts out.
**Parameters.** One pitch per work, declared in DESIGN.md (8–20px at
poster scale; an *enlarged* screen is the point — the dots must be
seen as dots). Dot radius follows area, capped where neighbours merge
into solid. The lattice is axis-aligned or at a declared angle; the
boundary and the falloff distance are declared numbers, not eyeballed.
A printer's control strip (the same screen as a 0–1 ramp) may be
printed in the apparatus as the work's evidence.
**Test.** Squint: the subject reads from the dots alone. Lay a flat
dot field beside it: if the two are interchangeable, the screen is
carrying no tone and the method has not been used.
**Caricature.** Polka-dot texture behind type; dots as confetti; a
screen whose pitch changes mid-subject; a dissolve boundary that
misregisters the solid and screened halves (one raster feeds both, or
the seam shows).

## The Thread — the editorial line (Swiss brochure work)

**Construction.** One continuous drawn line is the unit's lead and does
its main compositional work. The line is one *figure*, not necessarily one stroke: branches and dropped connectors that join it and share its weight (the Cut's drops, the String's connectors) are the same line. Per unit the line takes ONE of four jobs:
*Link* — it crosses a spread or a gutter and joins the two halves into
one composition, kinking where it meets the fold or a fact; *Cut* —
lines drop or run from an edge and divide the field into staggered
columns, each element hanging on its line at its own height; *Point* —
one diagonal travels across the unit to the single element it marks,
and may knot or circle it — the knot, a circle the line draws or ends
on, is the one curve the figure permits, and it must be the marked
element or hold it; *String* — the line flows through a sequence
(a chronology, a process) and drops a connector to every entry, so the
order is read off the line. Where the sequence is self-ordering (dates,
numbered steps), ordering alone does not pass: the strand must also
carry what the numerals do not — a rise for growth, a stagger for
weight, uneven steps for uneven intervals — or it is a divider under
data. Everything in the unit either hangs on the
line, is cut by it, or is pointed at by it; anything else is kept clear
of it.
**Parameters.** One weight for the whole work (hairline to 2px at
brochure scale) and one colour — the work's ink by default; an accent thread is a whole-work declaration, never mixed — declared in DESIGN.md; the line is drawn, never a
border, a box edge, or a table rule; segments are straight, on the
grid's angles (0/45/90) — in the Swiss keeping a flowing strand is
built from straight segments and steps, never a freehand wave; the
line may kink only where it meets something (the fold, a node, the
element it marks). The thread works because it is the ONLY line
doing this — the page's other rules are furniture and read as such.
**Test.** Remove the line and the unit falls apart: halves separate,
columns lose their hang, the marked element is unmarked, the sequence
scatters. If the unit still composes, the line was a divider — cut it,
or promote it until the test passes.
**Caricature.** A wavy decorative path drifting behind content; two
competing threads in one unit; a line that touches nothing it claims
to organize; underlining as emphasis.

## Route line — Vignelli, Charysyn & Noorda (New York Subway Map)

**Construction.** A sequence is drawn as one continuous line through
ordered stops on the grid; stops are nodes on the line, labelled in
reading order; branches are drawn only where the sequence truly forks.
The line is straight segments at 0°, 45°, or 90°.
**Parameters.** One line weight for the route (2px screen / 1pt print at document scale; re-derive it for another surface and settle it by the squint test),
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
