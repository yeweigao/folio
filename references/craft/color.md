# Color

Color is meaning, not decoration. Every palette here has three roles: paper (the ground), ink (type, rules, dark fields), and an accent (the exception). The theme sets their values; the Swiss theme uses white, near-black, and one hue. AI palettes fail by being timid and evenly spread (five pastel accents) or loud and generic (purple-to-blue gradients, teal and orange). A dominant field with one sharp accent outperforms both.

## Roles and budget

| Voice | Role | Area |
|---|---|---|
| Paper | where reading happens | ≥ 50% |
| Ink | type, rules, and full-bleed fields | structure |
| Accent | punctuation: the key figure, the current item, the risk, the turn | ≤ 10%; ≤ 20% on a statement unit |

Past that budget the accent stops being an exception and becomes a second paper. A full-bleed accent page is a deliberate turn, usually once per piece. Check the area: an 8 × 600 px line on a 1280 × 720 slide is 0.5%; a 200 × 100 block is 2.2%.

## Mid-tones come from ink

| Name | Value | Use |
|---|---|---|
| Muted | ink at 62% | secondary labels, sources |
| Secondary | ink at 78% | strong secondary text |
| Rule | ink at 12–16% | hairlines, table rules |
| Disabled · Hover | ink at 38% · 8% | interface states |

On white these resolve to about 5.3:1 (muted), 9.6:1 (secondary), and 1.3–1.4:1 (rules only). A theme may instead declare its greys as tokens (the Swiss theme uses warm greys tuned to its soft paper); either way greys are part of the palette, never invented per component, or the page starts to look like cards. On dark fields use white at 100 / 78 / 62% (about 18.9 / 11.4 / 7.8:1 on `#111`).

## Choosing the accent

Take the project's color when it has one. Otherwise derive it from the subject's own world (a school's crest, a material, a place) and test it on the real surface; never pick by topic cliché or reader age (blue for tech, rainbow for children). Light hues (yellows, limes, pale oranges) take ink and never white; saturated reds, blues, and greens usually take white at 5–7:1. Measure the actual hue. Ink on an accent field needs 7:1.

One project, one accent. Another hue appears only as a declared second ink (the Swiss theme calls it the signal), as paper (a declared print stock), as a mapped function color (at most three, each in a legend, never the only code), or in a declared overprint.

## Paper is material

Screens default to pure white. Warm, stone, and cream stocks belong to print, where they are the paper itself. Projectors and cheap screens wash warm whites out, and cream on screen is now an AI default.

## Screen and print

- Screen: sRGB; colors as tokens (paper, ink, accent, muted, line, focus). Dark mode inverts the fields (paper ↔ ink) and keeps the accent. No gradients except a functional photo scrim.
- Print: CMYK, total ink ≤ 300%; small text and hairlines in 100K; large blacks rich black 60/40/40/100; brand accents as spot colors; RGB neons do not print. Paper color shifts every ink: only a proof counts.

## Test

Convert to greyscale. If the hierarchy disappears, color was doing the work that size, weight, and position should do.
