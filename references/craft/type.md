# Type

The grid decides relationships; type decides whether they can be read. AI typography fails by sloppiness, not font choice: too many sizes, no weight logic, wrong punctuation, CJK set like Latin.

- **Roles are few, not one per element.** Display, body, label; add a level only for a real navigation or reading task.
- **Steps are unmistakable, not graded.** The surface sets sizes, the theme sets their relationships; skip every intermediate size the content does not need. When type leads, start at graphic scale with the title or key word spanning the frame; break fixed wording across lines before shrinking. Judge the hierarchy at thumbnail and intended viewing size, not by the legibility floor alone.
- **Size and weight are declared together, not separately.** Choose one hierarchy for the deliverable:

| Hierarchy | Relationship | Watch |
|---|---|---|
| Weight leads | Regular text, distinctly heavier headings | Heavy elements compete; leave one lead |
| Scale leads | Large light display, ordinary body, sturdy small text | Fine strokes fail in projection and small print |
| One weight | Size, position, and space carry everything | Small steps collapse |

- **Weight is judged by eye, not by number.** One family's 700 is not another's; no universal offsets. Small text needs stroke, not bold; thin display is judged at the final viewing distance.
- **One reading voice, not a collection.** A CJK/Latin pair is one voice; a second family needs a distinct task; see Faces.
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
  - Align by reading task; justify only with language-aware spacing. No closing punctuation at a line start or opening at a line end; no widows or orphans.
  - English: curly quotes, en dash for ranges, true minus, no em dash as a pause. Chinese: one quotation style, ——, ……, 《》 only for titles of works.
  - Tabular figures in tables, proportional in display; thin space before a unit, none before %.
  - Capitalization, tracking, and display effects follow the theme; sustained reading keeps familiar letterforms and enough stroke at viewing size.

## Faces

Replaceable resources, not principles. A new font is not a substitute for a stronger composition.

- **Start from a working pair, not a search.** Add a display face only when its voice changes the meaning of the work.
- **Pairs are judged together, not by spec.** Set real headings, paragraphs, numerals, and punctuation in both scripts; match apparent size, density, and baseline, not nominal size or weight. Use the locale's own resources (SC, TC, JP, KR).
- **Weights are real, not formulas.** One regular reading weight, one emphasis weight; display and small-text weights chosen optically; optical sizes matched to the set size.
- **A fallback is resolved, not accepted.** If a font is missing, substitute deliberately and reflow.
- **The exported face is checked, not assumed.** Compare rendered faces with the chosen families and weights, including embedded font names where supported; fix or report substitutions, then recheck line breaks.
- **Embedding prefers static TTF, not OTF/CFF.** Use a static TrueType build when a file must carry its faces; presentation engines often embed TrueType but not CFF-based OpenType, and variable fonts are unreliable. Embed where the format and license allow, then open the delivered file on the target machine. A PDF subset does not prove the PPTX carries the font.

| Job | Chinese | Latin | Stack |
|---|---|---|---|
| Explain, navigate, compare | Source Han Sans SC | Inter | `"Inter", "Source Han Sans SC", "Noto Sans SC", sans-serif` |
| Read an argument | Source Han Serif SC | Source Serif 4 (optical sizes) | `"Source Serif 4", "Source Han Serif SC", "Noto Serif SC", serif` |
| High-contrast cultural display, when called for | A display cut of the Song face | Bodoni Moda | `"Bodoni Moda", "Source Han Serif SC", "Noto Serif SC", serif` |

A title first changes scale, weight, line break, and position; it does not automatically need another face. Labels may keep the explanation pair inside a serif book.

### Working families and fallback

The first two pairings above are defaults, not required installs. If a needed face is missing, choose installed faces with the right scripts and weights (for example Helvetica Neue + PingFang SC, Arial + Microsoft YaHei, Georgia + Songti SC, or available Noto CJK); reflow and report the substitution. If no installed face serves the brief and installation is permitted, use the official packages below. Source Han packages are for Simplified Chinese (SC).

| Family | Official download | Package |
|---|---|---|
| Source Han Sans SC | [Adobe SC OTF package, v2.005R](https://github.com/adobe-fonts/source-han-sans/releases/download/2.005R/09_SourceHanSansSC.zip) | Static OTF weights |
| Inter | [Inter desktop package, v4.1](https://github.com/rsms/inter/releases/download/v4.1/Inter-4.1.zip) | Desktop fonts |
| Source Han Serif SC | [Adobe SC OTF package, v2.003R](https://github.com/adobe-fonts/source-han-serif/releases/download/2.003R/09_SourceHanSerifSC.zip) | Static OTF weights |
| Source Serif 4 | [Adobe desktop package, v4.005R](https://github.com/adobe-fonts/source-serif/releases/download/4.005R/source-serif-4.005_Desktop.zip) | Desktop fonts |

When installation is permitted, use Font Book or `~/Library/Fonts` on macOS, **Install** on Windows, or `~/.local/share/fonts` and a font-cache refresh on Linux. Restart the renderer and confirm the chosen families, scripts, and real weights before export. The high-contrast display family remains optional.

### Licenses

No font binaries are bundled; the license shipped with the actual file governs.

| Family | Official source | License |
|---|---|---|
| Source Han Sans | [Adobe](https://github.com/adobe-fonts/source-han-sans) | [OFL 1.1](https://github.com/adobe-fonts/source-han-sans/blob/master/LICENSE.txt) |
| Source Han Serif | [Adobe](https://github.com/adobe-fonts/source-han-serif) | [OFL 1.1](https://github.com/adobe-fonts/source-han-serif/blob/master/LICENSE.txt) |
| Inter | [Rasmus Andersson](https://github.com/rsms/inter) | [OFL 1.1](https://github.com/rsms/inter/blob/master/LICENSE.txt) |
| Source Serif 4 | [Adobe](https://github.com/adobe-fonts/source-serif) | [OFL 1.1](https://github.com/adobe-fonts/source-serif/blob/release/LICENSE.md) |
| Bodoni Moda | [Google Fonts package](https://github.com/google/fonts/tree/main/ofl/bodonimoda) | [OFL 1.1](https://github.com/google/fonts/blob/main/ofl/bodonimoda/OFL.txt) |
| Noto Sans SC, fallback | [Google Fonts package](https://github.com/google/fonts/tree/main/ofl/notosanssc) | [OFL 1.1](https://github.com/google/fonts/blob/main/ofl/notosanssc/OFL.txt) |
| Noto Serif SC, fallback | [Google Fonts package](https://github.com/google/fonts/tree/main/ofl/notoserifsc) | [OFL 1.1](https://github.com/google/fonts/blob/main/ofl/notoserifsc/OFL.txt) |

OFL allows commercial documents and full or subset embedding without making the document OFL; redistributing font files requires the license and notices; modified fonts stay OFL and respect reserved names. A newly chosen font does not inherit these terms. [OFL FAQ](https://openfontlicense.org/ofl-faq/)

At adoption, record: font and installation name, file version, source, license, embedding and redistribution terms, date, replacement. For PPT, check the [embedding flags](https://learn.microsoft.com/en-us/typography/opentype/spec/os2#fstype) and reopen the delivered file; for print, check embedded subsets and missing glyphs. See the [production charter](../production.md).
