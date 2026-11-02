# Tools

The masters worked with real material: photographs taken for the job, metal type, offset proofs, chosen stock. Name what your hand used, then reach for the nearest real equivalent. A tool you lack becomes an honest placeholder, never an imitation drawn in code.

## See

| Tool | Does |
|---|---|
| `scripts/render.py page.html [dir]` | One PNG per `.unit`, and the text a reader sees. Needs Playwright. |
| `scripts/contact.py out.png [--row label] img…` | A contact sheet, every unit at one height. Needs Pillow. |
| `scripts/measure.py DESIGN.md img…` | Ground and accent share of each render. Needs Pillow. |
| `scripts/preview.py DESIGN.md` | A token catalog and type proof, in Latin and CJK. |

Without Playwright, see the render any way the environment allows; a page never looked at is not done.

## Check

| Tool | Does |
|---|---|
| `scripts/factcheck.py brief.md seen.txt` | Every backticked fact present verbatim; typographic changes and numbers not in the brief flagged. |
| `scripts/folio-check.py DESIGN.md [export…]` | The skeleton complete, no placeholders, contrast held; the export uses only declared colors and faces, no banned charts, no copy tells. |
| `npx @google/design.md lint DESIGN.md` | Google's lint, where npm is reachable; otherwise report it unverified. |
| `scripts/extract.py file.pptx\|file.html` | A skeleton drafted from an artifact's real colors, faces and sizes, for critique. |

## Make

- **Generators** (`scripts/generators/`): Isotype rows, ledgers, programme fields, as SVG.
- **Code** for anything with a rule: grids, constructed letters, series, dot screens, diagrams. An algorithmic move is computed, never imitated.
- **Helpers**, where the environment allows: parallel directions and critics on a lighter model.

## Material

- **Photographs:** the person's own first; then the subject's own archive, site or press kit; then Wikimedia Commons or Openverse, license checked and credited. Search the subject's world, never "premium".
- **Generated images:** when a photograph is impossible and atmosphere is the job. The master and the work go verbatim into the prompt; the image is declared, never evidence.
- **3D:** a modelling tool such as Blender, when an object must be made; declared as rendering.
- **Nothing at all:** a labeled placeholder at the right size and crop, reported.

## Fonts

Faces come from the hand's lineage first, then from what can be installed and licensed. No binaries are bundled.

- **Web:** Google Fonts are allowed; confirm in the render that the face loaded.
- **Local:** install, restart the renderer, confirm families, scripts and real weights before export.
- **Embedding:** static TTF over CFF or variable; open the delivered file on the target machine.
- **CJK:** a face matching the Latin in density, apparent size and baseline; Source Han or Noto, SC/TC/JP/KR as the locale requires (OFL 1.1).
- **Licensing:** OFL allows commercial use and embedding; redistributing files needs the license. Otherwise check `fsType` and the terms.
- **Record** face, version, source, license and fallback in the skeleton.
