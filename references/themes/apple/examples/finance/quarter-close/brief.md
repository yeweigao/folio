# Brief — What the quarter did not keep

One closing slide for a payment product, read by a shop owner at the end of a
quarter. The shop, the statement and every figure are invented.

## Facts

Every string below must appear in the deliverable exactly as written.

- `Ledger`
- `Quarter close, Q3 2026`
- `¥16,660 of the quarter never reached the shop.`
- `这个季度有 ¥16,660 没有到店`
- `Gross takings less refunds and fees is what was paid out. The statement holds the whole of that arithmetic, line by line, in one column.`
- `CNY, 1 July – 30 September 2026`
- `1,250 charges at ¥392`
- `The ¥16,660 is the two deductions added: ¥9,180 in refunds and ¥7,480 in fees. Fees are 1.45% of gross plus ¥0.30 a charge.`
- `A refunded sale returns the customer's money, not the fee that was taken when it was charged.`
- `Settlement statement`
- `Q3 2026`
- `Gross takings`
- `¥490,000`
- `Refunds`
- `−¥9,180`
- `Ledger fees`
- `−¥7,480`
- `Paid to the shop`
- `¥473,340`
- `1,250 charges, 1.45% + ¥0.30`
- `Paid 2 October 2026`
- `Source: Ledger settlement statement, illustrative shop, 1 July – 30 September 2026. Figures cover 1,250 charges.`
- `Illustrative example`
- `Illustrative render, not a photograph`

## Deliverable

One self-contained HTML file, one `.unit` of 1600 × 900 px. Google Fonts are
allowed; the continuous-corner helper is a local sibling asset. The statement
panel is the only rounded shape. No Apple product, photograph, logo or font file
is used.

## Reader and outcome

A shop owner at a laptop, 50–70 cm from the screen, at the end of the quarter.
In one glance: how much of the quarter did not arrive, and that the statement
can be audited line by line. Next: they read the three rows and the total, then
the two lines that explain where the money went.

## The idea

On this surface, *a settlement* becomes *a subtraction that has to close*: the
claim is not the size of the quarter but the distance between what was charged
and what was paid, so the slide sets the deductions as a column that ends in a
total and states the difference above it.

## Sequence

1. Statement — lead: the amount that did not arrive, in the one accent on the
   slide, register: base (white field, one figure, one sentence).
2. Argument — the dark statement with three deductions and the total, amounts
   right-aligned on one edge, register: dark turn (a complete foreground palette
   on the panel).
3. Close — the two lines that explain the difference, then source, register:
   pause.

## Assumptions and gaps

- The arithmetic closes exactly: 490,000 − 9,180 − 7,480 = 473,340, and
  1.45% of 490,000 plus 1,250 × ¥0.30 is 7,480.
- Figures are set with tabular numerals and a shared right edge; the fallback
  would be the right-aligned column, which is also what the render uses.
- No chart appears: three amounts and a total are read faster as a column than
  as bars, and the slide keeps one accent for the missing money.
- The statement is an illustrative interface, declared in the caption; it is
  readable evidence, never a screenshot.
- Fonts load from Google Fonts; offline fallbacks change the setting.
