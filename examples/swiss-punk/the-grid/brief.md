# Brief — The Grid

A poster for a public evening at the Museum of Design: three talks and a
poster exhibition about the system behind modern design. It hangs in the
museum's windows and around the city, read from two to five metres. The
programme is fictional and must say so.

## Facts

Every string below must appear in the deliverable exactly as written.

- `THE GRID`
- `格网`
- `Three talks and a poster exhibition on the system behind modern design.`
- `三场讲座，一场海报展——现代设计背后的系统`
- `Saturday 14 November 2026`
- `19:30–22:00`
- `Doors 19:00`
- `Hall 2, Museum of Design`
- `设计博物馆 二号厅`
- `19:30`
- `The Module`
- `Josef Müller-Brockmann`
- `20:15`
- `The System`
- `Otl Aicher`
- `21:00`
- `The Interval`
- `Kenya Hara`
- `Foyer, from 19:00: poster exhibition, nine dialects, one mother tongue`
- `Free entry, seats unreserved`
- `免费入场，不设座位预订`
- `Illustrative example`

## Deliverable

One self-contained HTML file. The poster is one element with class
`unit`, exactly 1000 × 1414 px (A-series proportion). Web fonts from
Google Fonts are allowed; no other external assets.

## Reader and outcome

Passers-by and museum visitors reading in English and Chinese from 2 to 5 m while walking. In three seconds: the series (THE GRID), the day (Saturday 14 November 2026), the place (Museum of Design). Close up: three talks, the foyer exhibition, free entry. Outcome: they come on the night, unbooked, knowing the programme is fictional. Read at about A1 (594 x 841 mm); one master pixel is 0.594 mm.

## The idea

On this surface, *the grid* becomes *a stack of films slipped off the grid they are printed on*: 格 is an enlarged dot screen under the Latin title, whose letters step down a fixed step each, overprinted by a blue film slipped 14 right and 10 down; the three talks hang from one thread stepping two columns right and one row down per 45-minute interval.

## Assumptions and gaps

- No talk end times, organiser name or talk descriptions are given, so none is printed.
- `Illustrative example` declares the programme fictional: level 3 bold, ink, bottom margin.
- `格网` is live text once (large, vertical); the blue copies are CSS pseudo-content. The dot screen is an aria-hidden image of 格 only.
- Fonts load from Google Fonts (Archivo, Noto Sans SC); the fallback has different widths and was not tested offline.
- Screen master: no bleed, trim or PDF/X.
