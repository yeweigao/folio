# Brief — Three things, three materials

One Bento page for the shop side of a fictional everyday-goods house: three
kitchen things at one shelf of the same range, each with its use, its material,
its size and its price, and three material samples above them. The house, the
figures and the prices are fictional and must say so.

## Facts

Every string below must appear in the deliverable exactly as written.

- `Plain`
- `Everyday range · 2026`
- `Three things, three materials.`
- `三件东西，三种材料`
- `Nothing here is a colour.`
- `Cotton off the roll, porcelain out of the kiln, beech off the plane.`
- `Cotton`
- `Porcelain`
- `Beech`
- `0`
- `marks printed on the outside`
- `One care label is sewn inside the seam, in one colour.`
- `Cotton cloth`
- `Wipes a table`
- `100% cotton, 12 oz`
- `300 × 300 mm`
- `Porcelain cup`
- `Holds 200 ml`
- `porcelain, unglazed foot`
- `Ø 78 × 90 mm`
- `Beech spoon`
- `Stirs a pot`
- `solid beech, oiled`
- `300 mm`
- `¥45`
- `¥38`
- `¥32`
- `Add`
- `Prices include tax`
- `Illustrative example`
- `Illustrative render, not a photograph`

## Deliverable

One self-contained HTML file, one `.unit` of 1440 × 1000 px, built as a Bento
grid that carries the range's comparison and purchase task. Google Fonts are
allowed; the continuous-corner helper is a local sibling asset but no shape uses
it, because this world's ladder is zero: every tile, sample and button is square
and the separation is a 1 px hairline. No accent colour: cotton, porcelain and
beech are the only chromatic events. No logo, no borrowed photograph.

## Reader and outcome

A buyer on a laptop, fifty to seventy centimetres from the screen, buying three
small things at once. In one glance: that they come from one range with nothing
printed on them, and what each is made of. Next: they compare the material line
of the three cards and add the ones they need.

## The idea

On this surface, *three small purchases* become *three material arguments*: a
brand would put its name where these three put their fibre, clay and grain, so
the page spends its largest tile on the materials themselves and lets the
products sit below as a plain comparison — the claim that nothing is decorative
is made by showing nothing decorative.

## Sequence

1. Lead tile — the three material samples, `Nothing here is a colour.`,
   register: base (a white card with three bands).
2. Number tile — `0` marks printed on the outside, register: dark turn.
3. Collection — three product cards with the same four lines in the same order:
   what it does, what it is, how big, what it costs, register: densest.
4. Close — the tax line and the two disclaimers, register: pause.

## Assumptions and gaps

- Each product is drawn at a size that lets it be read, not at a shared scale;
  the sizes are stated in millimetres on each card instead, so no drawing claims
  a comparison it does not make.
- The three material bands are drawn stand-ins for cotton, glaze and beech, at
  no stated scale; they show the material, never a measurement.
- `0` counts printed marks on the outside only: one care label is named in the
  same tile, so the number cannot be read as a claim about the whole object.
- Prices and sizes are fictional and consistent within this range; `Prices
  include tax` sits in the footer, in fine print, never beside a name.
- No card carries a shadow, a badge or a second accent; the hairline is the only
  edge.
- Fonts load from Google Fonts; offline fallbacks change the setting.
