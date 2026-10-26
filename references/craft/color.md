# Color

Color is a role, not decoration. AI palettes fail two ways: timid and evenly spread (five pastel accents), or loud and generic (purple-to-blue gradients, teal and orange). A dominant field with one sharp accent beats both.

- **Roles, not swatches.** Paper, ink, accent; muted text and a hairline only when needed. Greys are declared once as tokens, never invented per component. A hairline separates; it never sets text.
- **One accent, not a palette.** Another hue enters only as a declared second ink, a print stock, a mapped function color (at most three, with a legend, never the only code), or an overprint.
- **The accent comes from the brand or the subject's story, not from habit or a topic cliché.** A brand color keeps its hue and moves only in lightness. Without one, choose a color the world knows by name: a historic pigment, a maker's signature, a Pantone color of the year, sourced and measured. The table below is a calibrated sample, not the limit.
- **The accent is an exception, not a second paper.** Paper ≥ 50% of the area; accent ≤ 10%, ≤ 20% on a statement unit; a full accent field is a variation.
- **Contrast is measured on the composite, not assumed from opacity.** Text ≥ 4.5:1 on its actual ground; a dark field resets every foreground role and lightens the accent until it passes.
- **Paper is material, not mood.** White on screen and the stock itself in print; a warm screen ground is a brand decision.
- **Hierarchy survives greyscale.** If it disappears, color is doing the work of size, weight, and position.

## Named colors

| Family | Name | Value | As a field, text in | As text on white | Character and caution |
|---|---|---|---|---|---|
| Blue | International Klein Blue | `#002FA7` | white 10.7:1 | yes | Yves Klein's ultramarine (1958–60); absolute, artistic |
| Blue | Prussian blue | `#003153` | white 13.4:1 | yes | The first modern synthetic pigment, the blueprint; engineering, archives |
| Blue | Majorelle blue | `#6050DC` | white 5.7:1 | yes | Jacques Majorelle's garden in Marrakech; warm, vivid |
| Blue | Classic Blue (Pantone 19-4052, 2020) | `#0F4C81` | white 8.9:1 | yes | Steady, institutional |
| Green | British racing green | `#004225` | white 11.6:1 | yes | Britain's motor-racing color; heritage, engineering |
| Teal | Tiffany Blue (Pantone 1837) | `#0ABAB5` | ink 7.8:1 | no (2.4:1) | Celebration; a registered trademark, so never for jewelry or gifts |
| Teal | Marrs green | `#4BACA5` | ink 7.0:1 | no (2.7:1) | G. F Smith's 2017 "world's favourite colour", from the River Tay; the Chinese web often circulates a deeper teal under this name |
| Orange | Hermès orange | ≈ `#F37021` | ink 6.4:1 | no (2.9:1) | Craft, warmth; no official value exists, so this is an approximation; never to evoke luxury packaging |
| Orange | International orange | `#FF4F00` | ink 5.7:1 | display only (3.3:1) | NASA suits, the Bell X-1; aerospace, infrastructure |
| Red | Rosso corsa | `#E4002B` | white 4.8:1 | just | Ferrari's racing red; speed, competition |
| Red | Cartier red | `#D50032` | white 5.4:1 | yes | The jewelry box; ceremony, gift |
| Red | Folio vermilion | `#C83024` | white 5.4:1 | yes | Swiss poster red; this theme's habit |
| Red | Louboutin red | Pantone 18-1663 TP | proof the swatch | — | No reliable screen value; a trademark for shoe soles |
| Magenta | Viva Magenta (Pantone 18-1750, 2023) | `#BB2649` | white 6.0:1 | yes | Bold, carmine-based |
| Pink | Shocking pink | `#FC0FC0` | ink 5.4:1 | display only (3.5:1) | Schiaparelli, 1937; surreal, fashion |
| Violet | Very Peri (Pantone 17-3938, 2022) | `#6667AB` | white 5.1:1 | yes | Digital, playful |
| Warm | Peach Fuzz (Pantone 13-1023, 2024) | `#FFBE98` | ink 11.8:1 | no | Soft, caring; a field rather than a mark |
| Warm | Mocha Mousse (Pantone 17-1230, 2025) | `#A47864` | ink 4.9:1 | display only (3.9:1) | Earth, comfort |
| Yellow | Illuminating (Pantone 13-0647, 2021) | `#F5DF4D` | ink 14.0:1 | never | Optimism; a marker, not a text color |
| Yellow | Folio signal yellow | `#F5C84B` | ink 11.9:1 | never | This theme's second ink |
| Paper | Cloud Dancer (Pantone 11-4201, 2026) | `#F0EEE9` | ink 16.3:1 | — | A soft white ground, not an accent |

Values are common screen approximations; print needs the physical swatch. A signature color borrowed into another category lends character; used in its owner's category, it reads as imitation. A Pantone color of the year dates the work.

## Calibration

| Role | Value | Note |
|---|---|---|
| Paper · ink | `#FFFFFF` · `#111111` | Dark turn: `#141414` with white |
| Muted | `#625F59` (≈ ink 62%) | Secondary labels, sources |
| Secondary | ink 78% | Strong secondary text |
| Hairline | `#C5C2BC` (≈ ink 12–16%) | Rules only |
| Disabled · hover | ink 38% · 8% | Interface states |

Framework defaults read as unchosen and several fail contrast: Tailwind blue `#3B82F6`, indigo `#6366F1`, violet `#8B5CF6`, emerald `#10B981`, Bootstrap blue `#007BFF`.

## Screen and print

- Screen: sRGB tokens (paper, ink, accent, muted, line, focus); no gradients except a functional scrim.
- Print: the printer's profile, stock, and ink limit govern. 100K for small text and hairlines; rich black and total-ink recipes only where the printer allows; spot colors when specified; proof out-of-gamut accents, since stock shifts every ink.
