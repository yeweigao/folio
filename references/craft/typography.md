# Typography

The grid decides relationships; type decides whether they can be read. AI typography fails by sloppiness, not font choice: too many sizes, no weight logic, wrong punctuation, CJK set like Latin.

- **Roles are few, not one per element.** Display, body, label; add a level only for a real navigation or reading task.
- **Steps are unmistakable, not graded.** The surface sets absolute sizes, the theme sets their relationships; skip every intermediate size the content does not need.
- **Size and weight are declared together, not separately.** Choose one hierarchy for the deliverable:

| Hierarchy | Relationship | Watch |
|---|---|---|
| Weight leads | Regular text, distinctly heavier headings | Heavy elements compete; leave one lead |
| Scale leads | Large light display, ordinary body, sturdy small text | Fine strokes fail in projection and small print |
| One weight | Size, position, and space carry everything | Small steps collapse |

- **Weight is judged by eye, not by number.** One family's 700 is not another's; no universal offsets. Small text needs stroke, not bold; thin display is judged at the final viewing distance.
- **One reading voice, not a collection.** A CJK/Latin pair is one voice; a second family needs a distinct task. See [fonts](fonts.md).
- **Measure follows the reader, not the box.**

| Role | Latin chars | CJK chars | Leading |
|---|---|---|---|
| Body | 45–75 | 25–40 | 1.5–1.75 |
| Lead | 40–60 | 22–32 | 1.5–1.6 |
| Display | 8–20 | 4–12 | 0.95–1.12 |
| Caption | 30–50 | 18–28 | 1.4–1.5 |

  Latin ≈ width ÷ (0.5 × size); CJK ≈ width ÷ size.
- **Lines break by meaning, not by width.** Titles in balanced lines; headings, labels, and cells follow their content.
- **Spacing is designed, not typed.** Body keeps the font's spacing; display tracking follows the actual letterforms; CJK and Latin are separate decisions; the gap between them comes from the font or 1/8–1/4 em.
- **Punctuation is exact, not approximate.**
  - Flush left; justify only with language-aware spacing. No closing punctuation at a line start or opening at a line end; no widows or orphans.
  - English: curly quotes, en dash for ranges, true minus, no em dash as a pause. Chinese: one quotation style, ——, ……, 《》 only for titles of works.
  - Tabular figures in tables, proportional in display; thin space before a unit, none before %.
  - No all-caps sentences, no tracked caps below 12 px, no outlined, glowing, or gradient text.
