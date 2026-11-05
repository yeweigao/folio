# Read-access inventory

## Supplied inputs
- `input/DESIGN.md` — read fully, unchanged.
- `input/brief.md` — read fully.
- `input/TECHNICAL.md` — read fully.
- `input/embed_fonts.py` — read fully and executed for font embedding only.
- `input/fonts/` — directory listing.
- `input/fonts/Inter-700.ttf` — font metrics.
- The embedding tool read `Inter-400.ttf`, `Inter-700.ttf`, `Inter-900.ttf`, `Archivo-variable.ttf`, `NotoSansSC-variable.ttf`, and `Oswald-700.ttf` within `input/fonts/`.

## Own output
- `output-v1/generate.py`, `raw.svg`, `poster.svg`, `self-check.js`, `self-check.json`, and `preview.png`; preserved first-complete copies.

## Generic installed tools/libraries
- `/private/tmp/folio-memphis-tools/bin/python`, Python standard library, fontTools and its font subsetting/compression dependencies.
- `/opt/homebrew/bin/node`, Node standard library.
- `/Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright` and runtime dependencies.
- `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome` for local rendering.
- Standard shell commands used for the case's own output files.

No parent folders, original references, previous artifacts, other cases, skills, external AGENTS files, or other agents were read or consulted.
