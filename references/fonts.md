# Fonts

Read only when installing, embedding, or licensing fonts. No font binaries are bundled; the license shipped with the actual file governs.

- **Embedding prefers static TTF, not OTF/CFF.** Presentation engines often embed TrueType but not CFF-based OpenType, and variable fonts are unreliable. Embed where the format and license allow, then open the delivered file on the target machine; a PDF subset does not prove the PPTX carries the font. The Source Han packages below are static OTF: they serve rendering and PDF, while a PPTX that must carry its faces needs a static TrueType build.
- **Install** with Font Book or `~/Library/Fonts` on macOS, **Install** on Windows, or `~/.local/share/fonts` and a font-cache refresh on Linux; restart the renderer and confirm families, scripts, and real weights before export.

| Family | Official package | License |
|---|---|---|
| Source Han Sans SC | [Adobe SC OTF, v2.005R](https://github.com/adobe-fonts/source-han-sans/releases/download/2.005R/09_SourceHanSansSC.zip) | [OFL 1.1](https://github.com/adobe-fonts/source-han-sans/blob/master/LICENSE.txt) |
| Source Han Serif SC | [Adobe SC OTF, v2.003R](https://github.com/adobe-fonts/source-han-serif/releases/download/2.003R/09_SourceHanSerifSC.zip) | [OFL 1.1](https://github.com/adobe-fonts/source-han-serif/blob/master/LICENSE.txt) |
| Inter | [Desktop, v4.1](https://github.com/rsms/inter/releases/download/v4.1/Inter-4.1.zip) | [OFL 1.1](https://github.com/rsms/inter/blob/master/LICENSE.txt) |
| Source Serif 4 | [Desktop, v4.005R](https://github.com/adobe-fonts/source-serif/releases/download/4.005R/source-serif-4.005_Desktop.zip) | [OFL 1.1](https://github.com/adobe-fonts/source-serif/blob/release/LICENSE.md) |
| Bodoni Moda | [Google Fonts](https://github.com/google/fonts/tree/main/ofl/bodonimoda) | [OFL 1.1](https://github.com/google/fonts/blob/main/ofl/bodonimoda/OFL.txt) |
| Noto Sans SC, fallback | [Google Fonts](https://github.com/google/fonts/tree/main/ofl/notosanssc) | [OFL 1.1](https://github.com/google/fonts/blob/main/ofl/notosanssc/OFL.txt) |
| Noto Serif SC, fallback | [Google Fonts](https://github.com/google/fonts/tree/main/ofl/notoserifsc) | [OFL 1.1](https://github.com/google/fonts/blob/main/ofl/notoserifsc/OFL.txt) |

OFL allows commercial documents and full or subset embedding without making the document OFL; redistributing font files requires the license and notices; modified fonts stay OFL and respect reserved names ([OFL FAQ](https://openfontlicense.org/ofl-faq/)). A newly chosen font does not inherit these terms: for PPT check its [embedding flags](https://learn.microsoft.com/en-us/typography/opentype/spec/os2#fstype), for print its embedded subsets and missing glyphs.

At adoption, record the font and installation name, file version, source, license, embedding and redistribution terms, date, and replacement.
