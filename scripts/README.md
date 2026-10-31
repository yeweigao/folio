# Scripts

Stdlib-only Python 3; no installs. They exist so a Folio claim can fail.

| Script | Does | Borrowed from |
|---|---|---|
| `folio-check.py DESIGN.md [export...]` | Deterministic gates: DESIGN.md completeness, component contrast, off-token colors/faces in a .pptx/.html export, banned pie/doughnut charts | impeccable's detector idea; Google's lint for the token layer |
| `preview.py DESIGN.md [out-dir]` | Generates preview.html, preview-dark.html and tokens.css from the tokens | VoltAgent awesome-design-md's per-file previews |
| `extract.py deck.pptx\|page.html [out.md]` | Drafts a DESIGN.md from an artifact's real colors, faces and sizes — the evidence base for Critique mode | design-md-chrome / Stitch extract-design-md |

Google's own checks stay Google's: `npx @google/design.md lint DESIGN.md`,
`diff` for post-lock changes, `export --format css-tailwind|dtcg` for web work.

| `measure.py DESIGN.md thumb.png...` | Field shares from rendered thumbnails: paper ≥ 50%, accent ≤ 10% (statement 20%); needs Pillow | theme grammar, made measurable |
| `generators/isotype.py` | Isotype rows as SVG: equal symbols, remainders cut | signature card: Isotype |
| `generators/ledger.py` | A ledger as SVG: decimal-aligned, hairline opens, ink rule closes | craft, Data |
| `generators/programme.py` | A programme field as SVG from a declared cycle | signature card: Programme series |

The preview doubles as the type proof sheet: every type token is set with
Latin, CJK, figures, and punctuation at its real size.
