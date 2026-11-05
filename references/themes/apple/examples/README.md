# Apple examples — the works

Each folder here holds one world's `DESIGN.md` (unchanged) and, beside it, the
pieces made from it. The Swiss theme keeps three unrelated pieces under each
skeleton plus a shared transfer poster; this folder follows the same shape.
Every world gets three pieces, on three different reading tasks, with new
content — not a redraw of the world's own product page.

## The workflow these pieces were made under

1. `SKILL.md` — Philosophy and Routes. `references/themes/apple/theme.md` in
   full, the world's industry dialect, the Keynote / Store / Editorial surface
   file, Bento where a grid is called for, and the matching delivery surface in
   `references/surfaces/`.
2. `references/design-md.md` for the brief form and the transfer test;
   `references/craft.md` for type, copy, data and imagery; `references/tools.md`
   for seeing and checking; `references/review.md` for the floors and the eye.
3. A `brief.md` beside every piece, with `## Facts` (every fixed string in
   backticks, verbatim), reader and outcome, the idea as
   "*the subject* becomes *the device*", a sequence per unit and the gaps.
4. The piece, then a render looked at, `scripts/factcheck.py`, and
   `scripts/release-check.py` holds the whole folder to the floors.
5. A critic / judge pass on the rendered set; kept points fixed and re-rendered.

No `DESIGN.md` was rewritten for this set. A difference that would hold for
every piece belongs in the skeleton, not in a brief.

## Shape of a piece

```
<world>/<slug>/brief.md
<world>/<slug>/<surface>-<slug>.html      one self-contained .unit
<world>/<slug>/preview.png                the render looked at
```

- Fixed-size `.unit`, one per HTML: Keynote 1600 × 900, Store / Bento
  1440 × 1000, Editorial 1200 × 1600, poster 1000 × 1414. Recompose for the
  format; do not scale a slide down into a page.
- Live HTML text. Google Fonts are allowed; faces come from the world's Tokens.
  No Apple product, brand product, photograph, logo or font file.
- Every drawn object is an illustrative stand-in, declared in a caption with
  `Illustrative render, not a photograph`. Illustration never poses as proof:
  the proof is a readable interface, figure, section, diagram or comparison.
- Every non-zero radius uses the shared continuous-corner path. Load it with
  `<script src="../../_shared/continuous-corner.js"></script>` and mark the
  shape:

  ```html
  <div data-cc="18" data-cc-fill="#ffffff" data-cc-stroke="#e0e0e0"> … </div>
  ```

  `data-cc` is the radius from the skeleton's ladder; `data-cc-clip` applies
  the same path as a clip to a media container. The helper draws fill, stroke
  and clip from one path, fitted to the shape's real dimensions. Plain CSS
  `border-radius`, `rect rx` and superellipses are forbidden. Every `[data-cc]`
  element needs `position:relative; isolation:isolate` and the `.cc-bg` rule:

  ```css
  [data-cc]{position:relative;isolation:isolate}
  .cc-bg{position:absolute;left:0;top:0;z-index:-1;pointer-events:none}
  ```

- Body, leads, captions, card names and prices are flush left, ragged right.
  Only a hero, vista or cover headline may centre. A centred container is not
  centred text.
- One accent replaces every Apple blue role when a hand governs. Blue is four
  roles in the mother tongue, never one variable.
- Text shapes carry real internal padding; title boxes clear descenders;
  number groups sit mid-frame with number, label and context spaced down.
- Reduced-motion state: these are static pages, so nothing animates.

## What the eye refuses here

Warm cream as a default; black plus one vermilion; Newsreader, IBM Plex, Jost,
Inter by reflex (use the world's Tokens); tracked uppercase kickers, 01/02/03,
monospace labels, hairlines over a split footer; oversized numerals as a hero
with no claim; KPI trios; a navy closing slide; a literal pictogram of the
subject; a wall of equal cards with equal claims; a gradient wallpaper, glass
panels, fake grain, fake 3D, glowing outlines; text baked into an image; a
bullet wall; a centred body paragraph; a price larger than the product name;
a second accent; a shadow on a card, button or text; weight 500; body at 16 px.

## See and check

One command, from anywhere:

```
/Users/apple/.workbuddy/binaries/python/envs/default/bin/python /Users/apple/Documents/GitHub/folio/scripts/release-check.py
```

Render one piece (write `preview.png` from `<stem>-01.png`):

```
/Users/apple/.workbuddy/binaries/python/envs/default/bin/python /Users/apple/Documents/GitHub/folio/scripts/render.py /Users/apple/Documents/GitHub/folio/references/themes/apple/examples/mother-tongue/quiet-hour/slide-quiet-hour.html /Users/apple/Documents/GitHub/folio/references/themes/apple/examples/mother-tongue/quiet-hour/render
```

A contact sheet over the whole set — every piece labelled `world/slug`,
eight to a row so the rhythm and the sameness across worlds can be judged:

```
args=(); for f in /Users/apple/Documents/GitHub/folio/references/themes/apple/examples/*/*/preview.png; do args+=("$(basename "$(dirname "$(dirname "$f")")")/$(basename "$(dirname "$f")")=$f"); done
/Users/apple/.workbuddy/binaries/python/envs/default/bin/python /Users/apple/Documents/GitHub/folio/scripts/contact.py /Users/apple/Documents/GitHub/folio/references/themes/apple/examples/contact.png --height 300 --cols 8 "${args[@]}"
```

## The pieces

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
