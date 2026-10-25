# Color

Color is meaning, not decoration. Every palette here has three roles: paper (the ground), ink (type, rules, dark fields), and an accent (the exception). The theme sets their values; the Swiss theme uses white, near-black, and one hue. AI palettes fail by being timid and evenly spread (five pastel accents) or loud and generic (purple-to-blue gradients, teal and orange). A dominant field with one sharp accent outperforms both.

## Roles and budget

| Voice | Role | Area |
|---|---|---|
| Paper | where reading happens | ≥ 50% |
| Ink | type, rules, and full-bleed fields | structure |
| Accent | punctuation: the key figure, the current item, the risk, the turn | ≤ 10%; ≤ 20% on a statement unit |

Past that budget the accent stops being an exception and becomes a second paper. A full-bleed accent page is a deliberate turn when the content changes register. Check the area: an 8 × 600 px line on a 1280 × 720 slide is 0.5%; a 200 × 100 block is 2.2%.

## Mid-tones come from ink

| Name | Value | Use |
|---|---|---|
| Muted | ink at 62% | secondary labels, sources |
| Secondary | ink at 78% | strong secondary text |
| Rule | ink at 12–16% | hairlines, table rules |
| Disabled · Hover | ink at 38% · 8% | interface states |

These opacities are starting values, not contrast guarantees: the ink, background, and compositing determine the result. Measure text on the actual composite at ≥ 4.5:1. On dark fields, white at 100 / 78 / 62% is another starting set. Declare the resulting greys as palette tokens, never invent them per component.

## Choosing the accent

Take the project's color when it has one. Otherwise derive it from the subject's own world (a school's crest, a material, a place), never a topic cliché or reader age (blue for tech, rainbow for children). Light hues usually need ink; saturation alone cannot tell you whether white text will pass. Choose the foreground by measuring the actual pair at ≥ 4.5:1.

One project, one accent. Another hue appears only as a declared second ink (the Swiss theme calls it the signal), as paper (a declared print stock), as a mapped function color (at most three, each in a legend, never the only code), or in a declared overprint.

## Paper is material

Swiss defaults to white on screen and the stock's own color in print. Warm screen backgrounds are a brief or brand choice, not a shortcut to an editorial mood; measure their foreground contrast like any other ground.

## Screen and print

- Screen: sRGB; colors as tokens (paper, ink, accent, muted, line, focus). Dark mode resets every foreground role against its new field; adjust the accent's lightness as needed. No gradients except a functional photo scrim.
- Print: the printer's profile, stock, and ink limit govern conversion. Use 100K for small black text and hairlines; 300% total ink and rich black 60/40/40/100 are starting recipes only where the printer permits. Use spot colors when specified; proof out-of-gamut accents. Paper color shifts every ink: only a proof counts.

## Test

Convert to greyscale. If the hierarchy disappears, color was doing the work that size, weight, and position should do.
