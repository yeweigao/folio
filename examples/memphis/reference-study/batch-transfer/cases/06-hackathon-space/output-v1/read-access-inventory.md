# Read-access inventory

## Case inputs read in full
- input/DESIGN.md
- input/brief.md
- input/TECHNICAL.md
- input/embed_fonts.py

## Font files read
- input/fonts/Oswald-700.ttf — measured headline advances and embedded by the supplied utility.
- input/fonts/Inter-400.ttf — embedded by the supplied utility.
- input/fonts/Inter-700.ttf — embedded by the supplied utility.
- input/fonts/Inter-900.ttf — embedded by the supplied utility.
- input/fonts/Archivo-variable.ttf — embedded by the supplied utility.
- input/fonts/NotoSansSC-variable.ttf — embedded by the supplied utility.

## Directory names inventoried, without reading other file contents
- The case directory: searched only for brief.md, TECHNICAL.md, embed_fonts.py, and input/fonts/**.
- input/fonts/: inventoried filenames. License texts and FolioPixelStudy.woff2 were not opened.
- A first attempt at the case-root brief.md returned “No such file or directory”.

## Generic tools and libraries used
- /private/tmp/folio-memphis-tools/bin/python and its Python standard library, fontTools, and brotli dependencies.
- /opt/homebrew/bin/node.
- /Users/vicoye/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright and its generic dependencies.
- /Applications/Google Chrome.app/Contents/MacOS/Google Chrome and its normal runtime resources.

## Own output read
- output-v1/generate.py, output-v1/raw.svg, output-v1/poster.svg, output-v1/render.js, and output-v1/poster.png.

No parent files, references, other cases, other agents' outputs, old artwork/code, skill files, or AGENTS.md files were read.
