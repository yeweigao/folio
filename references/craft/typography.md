# Typography

Type is the smallest unit of design. The grid decides relationships; type decides whether they can be read. Most AI typography fails not in font choice but in sloppiness: too many sizes, no weight logic, wrong punctuation, CJK set like Latin.

## Roles

Start with three roles, each with one job. Reference work may need more levels; add one only when it distinguishes a real navigation or reading task.

| Role | Job | Size | Weight |
|---|---|---|---|
| Display | One claim, one word, one key figure | 46–300 by surface | 700–900 |
| Body | Reading, argument, explanation | 16–24 px screen · 10.5–12 pt A4 · 9.5–10.5 pt A5 | 400 |
| Label | Captions, sources, units, numbers, table heads | 12–14 px near screen · 18–22 px projected · 8.5–9.5 pt print | 500 |

Do not add a size merely for variety; reference units need no display role.

## Scale and weight

The surface and viewing distance set absolute sizes; the theme sets their relationships. The Swiss 11 / 13 / 14 / 16 / 20 / 24 / 32 / 46 / 64 / 112 / 196 / 280 ladder is a starting pattern, not the same physical scale on every surface. Declare one scale per deliverable (ratios around 1.2 for dense handbooks, 1.25 for decks and web, 1.333 for posters) and map each size to a role.

Weight follows size. Each size band carries its own weight, declared once for the whole piece; never pick a weight independently of the band. Two coherent ways to run it:

- **Heavy mode**: weight rises with size (body 400, lead 600, headings 700, display 900). Emphasis adds one step (+200) within the band, capped at 900.
- **Thin mode**: weight falls as size grows (display 200, H1 250, H2 300), while small text stays at 500–600 so it holds on the page. Emphasis comes from size and position, not bolding.

Small sizes are set a step heavier than body, because thin strokes vanish at caption size. A deliverable may switch modes for a section (a thin-mode chapter opener in a heavy-mode book) as a deliberate variation. Never synthesize weights: use real font files.

Tracking tightens as size grows (−0.02em at display, −0.04em at hero or edge-cropped sizes), stays 0 for text, and opens (+0.12em) only for kickers and running heads at legible sizes.

## Families

- One main family. A second reading family only as a declared role (a serif display voice in editorial), never "for variety". Pair by role contrast, not style contrast: two similar grotesques side by side read as a mistake.
- Inter, Roboto, and system defaults need a reason, such as brand continuity or a dialect's technical voice; do not choose them by habit.
- For Chinese-led work, start with a CJK family (`"Noto Sans SC", "PingFang SC", sans-serif`) and supply real weights. Inspect actual CJK runs for fallback and synthetic bold. Serif CJK: Noto Serif SC / Source Han Serif.

## Measure and leading

| Role | Latin | CJK | Leading |
|---|---|---|---|
| Body | 45–75 chars | 25–40 | 1.5–1.75 |
| Lead | 40–60 | 22–32 | 1.5–1.6 |
| Display | 8–20 | 4–12 | 0.95–1.12 |
| Caption | 30–50 | 18–28 | 1.4–1.5 |

Estimate prose measure before setting: Latin characters ≈ width ÷ (0.5 × size); CJK characters ≈ width ÷ size. Headings, labels, and table cells follow their content, not prose line lengths. Break titles by meaning; aim for two balanced lines unless the format or fixed wording needs more.

## Details models get wrong

- Flush left by default; justify only with language-aware spacing and line breaking. Keep closing punctuation off line starts and opening punctuation off line ends; fix widows and orphans.
- Curly quotes in English; one quotation style in Chinese (“ ” or 「 」); en dash for ranges (2025–2026); true minus (−); no em dash as a rhythmic pause in English. Chinese dash is ——, ellipsis ……
- Space between CJK and Latin comes from the font or 1/8–1/4 em, not typed spaces.
- Tabular figures in tables, proportional in display; thin space between number and unit (32 MB), none before % (32%).
- No all-caps sentences, no letterspaced all-caps labels under 12 px, no outlined, glowing, or gradient text.
