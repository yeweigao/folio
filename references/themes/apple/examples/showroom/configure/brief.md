# Brief — Configure

One configurator page for a small electric car, where choosing the parts builds
the running price. The car, every option and every price are fictional and must
say so.

## Facts

Every string below must appear in the deliverable exactly as written.

- `Volt`
- `Configure`
- `Every choice shows its price.`
- `每一项选择，都标着价格`
- `Illustrative render, not a photograph`
- `Battery`
- `电池`
- `Standard 402 km`
- `Included`
- `Long range 560 km`
- `+¥12,000`
- `Wheels`
- `轮毂`
- `16-inch Aero`
- `18-inch Turbine`
- `+¥4,800`
- `Finish`
- `车色`
- `Ash`
- `Pewter`
- `+¥2,200`
- `Carbon`
- `+¥3,600`
- `¥92,400`
- `Base ¥80,400 + ¥12,000 Long range`
- `Reserve`
- `Illustrative example`

## Deliverable

One self-contained HTML file, one `.unit` of 1440 × 1000 px. Google Fonts are
allowed; the continuous-corner helper is a local sibling asset. The world's
Tokens govern colour and face: carbon, graphite, pewter and ash with one
electric blue for the primary action only, all corners square, Inter with a
Chinese serif/sans pair. No Apple product, photograph, logo or font file is
used.

## Reader and outcome

A buyer on a laptop, 50–70 cm from the screen, building a car. In one glance:
the object, what it costs now, and that the price moves as they choose. Next:
they change an option and reserve without hunting for the action.

## The idea

On this surface, *the sequence of choices* becomes *the price itself*: a small
car is wanted differently by every buyer, so its cost cannot be one quoted
number — the configurator lets each decision add its own amount, and the buyer
reads the consequence of a choice at the moment of making it rather than
discovering a total at the end.

## Sequence

1. Cover / exhibit — lead: `Every choice shows its price.`, register: base
   (a whole carbon field, one object at full scale).
2. Collection / configurator — three option groups on a shared field,
   register: configurator turn (the object stays; choices, price and action
   stay visible); a hairline divides one group from the next.
3. Close — the running total and one square blue action in a sticky bar,
   register: pause; the price never leaves the screen.

## Assumptions and gaps

- The selected chip is shown by an inverted fill, not the dialect's focus-blue
  border: the Tesla hand spends its single electric-blue accent on the primary
  action only, so state is carried by value, never by a second accent.
- The car is one illustrative stand-in, declared in the caption; it is the same
  world object drawn for the launch slide, not a photograph and not evidence.
- The three groups are functional controls, not three equal-claim cards; one
  claim governs the screen.
- The base price, the deltas and the total are fictional; `Illustrative
  example` states this on the page.
- Fonts load from Google Fonts; offline fallbacks change the setting. Every
  text and chip carries internal padding so no line touches a frame edge.
