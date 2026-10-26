# Fonts

Replaceable resources, not principles. A new font is not a substitute for a stronger composition.

- **Start from a working pair, not a search.** Add a display face only when its voice changes the meaning of the work.
- **Pairs are judged together, not by spec.** Set real headings, paragraphs, numerals, and punctuation in both scripts; match apparent size, density, and baseline, not nominal size or weight. Use the locale's own resources (SC, TC, JP, KR).
- **Weights are real, not formulas.** One regular reading weight, one emphasis weight; display and small-text weights chosen optically; optical sizes matched to the set size.
- **A fallback is resolved, not accepted.** If a font is missing, substitute deliberately and reflow.

| Job | Chinese | Latin | Stack |
|---|---|---|---|
| Explain, navigate, compare | Source Han Sans SC | Inter | `"Inter", "Source Han Sans SC", "Noto Sans SC", sans-serif` |
| Read an argument | Source Han Serif SC | Source Serif 4 (optical sizes) | `"Source Serif 4", "Source Han Serif SC", "Noto Serif SC", serif` |
| High-contrast cultural display, when called for | A display cut of the Song face | Bodoni Moda | `"Bodoni Moda", "Source Han Serif SC", "Noto Serif SC", serif` |

A title first changes scale, weight, line break, and position; it does not automatically need another face. Labels may keep the explanation pair inside a serif book.

## Download the working families

The first two pairings above are the skill's four default font families. If a render machine is missing one, download and install its complete official package before composing or exporting. The Source Han packages below are for Simplified Chinese (SC); install every font file in each archive so the real weights are available.

| Family | Official download | Package |
|---|---|---|
| Source Han Sans SC | [Adobe SC OTF package, v2.005R](https://github.com/adobe-fonts/source-han-sans/releases/download/2.005R/09_SourceHanSansSC.zip) | Static OTF weights |
| Inter | [Inter desktop package, v4.1](https://github.com/rsms/inter/releases/download/v4.1/Inter-4.1.zip) | Desktop fonts |
| Source Han Serif SC | [Adobe SC OTF package, v2.003R](https://github.com/adobe-fonts/source-han-serif/releases/download/2.003R/09_SourceHanSerifSC.zip) | Static OTF weights |
| Source Serif 4 | [Adobe desktop package, v4.005R](https://github.com/adobe-fonts/source-serif/releases/download/4.005R/source-serif-4.005_Desktop.zip) | Desktop fonts |

On macOS, install with Font Book or place the font files in `~/Library/Fonts`; on Windows, use **Install** from the font file's context menu; on Linux, install under `~/.local/share/fonts` and refresh the font cache. Restart the rendering app, confirm all four families appear, and check Chinese and Latin text plus the required weights before export. The high-contrast display family remains an optional addition.

## Licenses

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
