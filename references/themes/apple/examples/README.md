# Apple examples — the pieces

Each world holds its `DESIGN.md` and three pieces made from it alone, on three reading tasks and three surfaces, with new content — never a redraw of the world's own product page. Each piece keeps its `brief.md`, responsive `.html` page, and the `preview.png` that was looked at; declared local assets sit beside it.

- **Surface forms, recomposed for web:** Keynote leads with one launch claim; Store and Bento organize product choice; Editorial carries a reading sequence. Keep the intended desktop composition, then recompose down to 320 px without scaling a fixed canvas.
- **Text is live HTML;** faces come from the world's Tokens. No real Apple or branded product photography, logos or font files.
- **Every invented image or drawn object is declared once per piece.** The proof is a readable interface, figure, section, diagram or comparison.
- **Every nonzero radius uses the shared contour:** load `../../_shared/continuous-corner.js`, mark the shape `data-cc="18"` with `data-cc-fill` and `data-cc-stroke`, or `data-cc-clip` for media; give `[data-cc]` `position:relative; isolation:isolate` and `.cc-bg{position:absolute;left:0;top:0;z-index:-1;pointer-events:none}`.
- **Web reflows, never scales the artboard.** Keep the desktop composition at its native format, then recompose at narrower widths so every claim, proof and action fits from 1440 px down to 320 px.
- **Static compositions, motion where it earns the move.** The artwork does not drift or reveal itself on scroll. Real controls may use brief transform/opacity feedback or a state-change transition (100–300 ms); `prefers-reduced-motion` removes transitional motion while preserving the state. Shared control, local-light and contact-shadow tokens live in `_shared/apple-interactions.css`.

**The eye refuses here:** cream as a default; black plus one vermilion; a face chosen by reflex instead of from Tokens; tracked uppercase kickers, 01/02/03, mono labels, hairlines over a split footer; an oversized numeral with no claim; KPI trios; a navy close; a literal pictogram of the subject; equal cards with equal claims. A brand's signature that names one of these is not a default.

Render with `scripts/render.py`, then open each page at 1440, 768 and 320 px and by keyboard; hold the folder to the floors with `scripts/release-check.py`; judge sameness across worlds on a contact sheet, eight to a row.

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
