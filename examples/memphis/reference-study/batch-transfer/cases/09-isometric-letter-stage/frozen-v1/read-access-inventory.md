# Read-access inventory

## Input contents read

- `input/DESIGN.md` — entire file.
- `input/brief.md` — entire file.
- `input/TECHNICAL.md` — entire file.
- `input/embed_fonts.py` — entire file; executed unchanged.
- `input/fonts/Oswald-700.ttf` — glyph metrics and outlines, plus embedding.
- `input/fonts/Inter-400.ttf` — embedding utility.
- `input/fonts/Inter-700.ttf` — embedding utility.
- `input/fonts/Inter-900.ttf` — embedding utility.
- `input/fonts/Archivo-variable.ttf` — embedding utility.
- `input/fonts/NotoSansSC-variable.ttf` — embedding utility.

## Directory names listed only

- `input/fonts/` via `rg --files`; other listed fonts and license contents were not opened.

## Own output read

- `output-v1/generate.py`, `raw.svg`, `poster.svg`, and `preview.png` during generation and self-QA.
- Own output copied into `output-v1/first-complete/` to preserve the first complete artifact.

## Generic runtime / libraries

- Python standard library, fontTools, Brotli through `/private/tmp/folio-memphis-tools/bin/python`.
- Node standard library and the provided Playwright package.
- Google Chrome for local rendering and font inspection.

## Unavailable-path attempts

- Initial attempts to open case-root `brief.md`, `TECHNICAL.md`, and `embed_fonts.py` returned file-not-found; the supplied files were then opened under `input/`.
- Initial listing of `output-v1/` returned file-not-found before creating the own-output directory.

No parent files, reference artwork, old drawing code, other cases, other agents' files, skill files, or on-disk AGENTS files were opened.
