# Read-access inventory

All project-file content reads were confined to the assigned case.

## Input contents read

- `input/DESIGN.md` — fully read, unchanged.
- `input/brief.md` — fully read, unchanged.
- `input/TECHNICAL.md` — fully read, unchanged.
- `input/embed_fonts.py` — fully read and executed, unchanged.
- `input/fonts/Inter-400.ttf` — read by the font embedding utility.
- `input/fonts/Inter-700.ttf` — read by the font embedding utility.
- `input/fonts/Inter-900.ttf` — read for text measurement and by the font embedding utility.
- `input/fonts/Archivo-variable.ttf` — read by the font embedding utility.
- `input/fonts/NotoSansSC-variable.ttf` — read for text measurement and by the font embedding utility.
- `input/fonts/Oswald-700.ttf` — read by the font embedding utility.

## Directory enumeration

`rg --files .` enumerated only this case. It listed the input filenames, font/license filenames and `input-manifest.json`. No manifest, license or pixel-font contents were opened.

Initial reads attempted the absent case-root filenames `brief.md`, `TECHNICAL.md` and `embed_fonts.py`; the existing files were subsequently read from `input/`.

## Own output read

- `output-v1/generate.py`
- `output-v1/raw.svg`
- `output-v1/poster.svg`
- `output-v1/render.cjs`
- `output-v1/preview.png`

## Generic runtimes and libraries

- `/private/tmp/folio-memphis-tools/bin/python` with Pillow, fontTools, brotli and Python standard libraries.
- `/opt/homebrew/bin/node` and Node standard libraries.
- `/Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright`
- `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`

No parent-folder contents, reference images, previous art/code, other cases, other agents, skills or AGENTS files were read.
