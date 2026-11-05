# Apple examples — the pieces

Each world holds its `DESIGN.md` and three pieces made from it alone, on three reading tasks, with new content — never a redraw of the world's own product page. Each piece keeps its `brief.md`, one self-contained `.html` unit, and the `preview.png` that was looked at.

- **Formats, recomposed, never scaled:** Keynote 1600 × 900; Store and Bento 1440 × 1000; Editorial 1200 × 1600; poster 1000 × 1414.
- **Text is live HTML;** faces come from the world's Tokens. No Apple or brand product, photograph, logo or font file.
- **Every drawn object is a stand-in,** captioned `Illustrative render, not a photograph`. The proof is a readable interface, figure, section, diagram or comparison.
- **Every nonzero radius uses the shared contour:** load `../../_shared/continuous-corner.js`, mark the shape `data-cc="18"` with `data-cc-fill` and `data-cc-stroke`, or `data-cc-clip` for media; give `[data-cc]` `position:relative; isolation:isolate` and `.cc-bg{position:absolute;left:0;top:0;z-index:-1;pointer-events:none}`.
- **Static pages;** nothing animates.

**The eye refuses here:** cream as a default; black plus one vermilion; a face chosen by reflex instead of from Tokens; tracked uppercase kickers, 01/02/03, mono labels, hairlines over a split footer; an oversized numeral with no claim; KPI trios; a navy close; a literal pictogram of the subject; equal cards with equal claims.

Render with `scripts/render.py`; hold the folder to the floors with `scripts/release-check.py`; judge sameness across worlds on a `scripts/contact.py` sheet, eight to a row.

| World | Pieces |
|---|---|
| mother-tongue | quiet-hour (Keynote), graphite (Store), aluminium (Editorial) |
| ai | deleted-sentence (Keynote), word-allowance (Store), draft-and-final (Editorial) |
| developer | eight-seconds (Keynote), team-plans (Bento), preview-link (Editorial) |
| finance | quarter-close (Keynote), fee-tiers (Bento), journey (Editorial) |
| consumer | sleep-report (Keynote), ring-sizing (Bento), one-night (Editorial) |
| showroom | per-charge (Keynote), configure (Store), one-road (Editorial) |
| luxury | the-making (Keynote), the-range (Bento), the-workshop (Editorial) |
| luxury-burberry | rain-test (Keynote), trench-series (Store), weather (Editorial) |
| luxury-chanel | one-jacket (Keynote), collection (Bento), archive (Editorial) |
| luxury-louis-vuitton | eight-stitches (Keynote), three-sizes (Bento), from-the-whole (Editorial) |
| minimalist | one-knob (Keynote), three-models (Bento), inside (Editorial) |
| minimalist-muji | one-sheet (Keynote), three-things (Bento), cut-open (Editorial) |
| minimalist-bang-olufsen | quietest-setting (Keynote), three-surfaces (Store), one-sheet (Editorial) |
| engineering | airflow-section (Keynote), filter-range (Bento), air-path (Editorial) |
| engineering-teenage-engineering | taken-apart (Keynote), kit-contents (Bento), signal-states (Editorial) |
| engineering-vitsoe | one-module (Keynote), configurations (Bento), disassembled (Editorial) |

All subjects, events, prices and figures are fictional and say so on the piece.
