# Brief — event poster, second evening (Bells and Silence)

Skeleton: DESIGN.md beside this file (Ensemble Lumen concert posters, Müller-Brockmann musica viva with Gerstner's programme).

## Facts

- `Ensemble Lumen`
- `Bells and Silence`
- `Saturday 23 January 2027`
- `19:30`
- `Tonhalle Zürich, Kleiner Saal`
- `Arvo Pärt — Cantus in Memory of Benjamin Britten`
- `John Cage — 4′33″`
- `Pauline Oliveros — Bye Bye Butterfly`
- `CHF 25 / 15 reduced`
- `ensemble-lumen.ch`

## Reader and outcome

Passers-by in tram shelters and foyers, reading from three metres in one to three seconds. Outcome: they register an Ensemble Lumen evening, Bells and Silence, a Saturday in January at 19:30 in the Kleiner Saal, and keep ensemble-lumen.ch for price and tickets.

## The idea

On this surface, Pärt's mensuration canon (one descending line in five voices, each half as fast as the last, all falling toward the bell's A) becomes the field, and the paper the slower voices have not yet crossed is the silence.

## The rule

Twelve rows (bars) by twelve tracks (scale steps); track 0 is low A, track 11 top E; the line E D C B A G F E D C B A.

- Voice v = 0..4 holds each note 2^v bars and enters at bar v. At bar t >= v it stands on step s = min(11, floor((t - v) / 2^v)), cell (t, 11 - s); the last step is held.
- Lower stave of (t, c): ink iff a voice stands on c at bar t.
- Upper stave: blue iff c = 0, every row: the bell's A, the one traced element.
- Both halves sound once, bar 11 track 0, joining into a full cell. Result: 39 ink and 12 blue half-cells.

Display is 125 px: the title at 161 px is 1126 px wide against the 880 px measure; at 125 it is 874. Facts and programme share one first baseline (programme pushed down 13 px). Gaps of one stave (33 px) between field, caption, title and block.

## Assumptions and gaps

- A diagram of the canon's proportions, not a transcription: one step per bar for the fastest voice, twelve bars of over a hundred, one line per voice.
- Structure taken from the Wikipedia article on the Cantus, not the score; violas, cellos and basses entering one bar apart is assumed. Cells check against the rule, not the printed notes.
- The bell does not toll every bar; the blue column is its pitch as reference.
- Cage and Oliveros are programme text only.
- Host Grotesk loads from Google Fonts; offline the 125 px title may not measure 874 px.
