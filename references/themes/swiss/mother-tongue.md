# Swiss — the mother tongue

Swiss structure with heavy and thin typography. The grid, asymmetry, and objectivity of the International Typographic Style, set for Chinese and Latin, with two typographic modes and a free choice of display lineage. It is the base of this theme because it is a grammar, not a look: it governs the relations between things rather than their decoration, so it can host other modernist movements without becoming costume. Every Swiss dialect inherits this file and changes only what it names.

## Lineage

The theme's dialects come from the movement's own history; knowing it lets you borrow a system rather than a surface.

- **Roots, 1920s**: the Bauhaus and De Stijl; Lissitzky and Rodchenko; Tschichold's *Die neue Typographie* (1928). Dialects: bauhaus, constructivist. Neurath and Arntz's Isotype turned statistics into pictograms: isotype.
- **Zurich and Basel, 1950s–60s**: Müller-Brockmann, Lohse, Vivarelli, and Neuburg's *Neue Grafik*; Ruder and Hofmann at Basel; Akzidenz, Univers, Helvetica. This is the mother tongue. Gerstner's *Designing Programmes* and Lohse's concrete art made design a system of permutations: programme.
- **Systems, Ulm and after**: Max Bill and Otl Aicher at Ulm; Lufthansa; Munich 1972. Dialect: public-info.
- **Export**: Vignelli and Unimark gave corporate and editorial discipline (editorial); Crouwel and Total Design in Amsterdam built type from the grid itself (gridnik); Kamekura, Tanaka, and later Hara in Japan joined the grid to emptiness and a single mark (tokyo); Brodovitch's *Harper's Bazaar* set type against photography (fashion); the photo-essay and *Sachfotografie* made the photograph a fact (documentary).
- **Rebellion and after**: Weingart in Basel, Greiman, Emigre broke the rules from inside (swiss-punk). Brutalist is today's honest-structure strand; bento is the product era's module grid.

## The grammar

- **Grid first.** Six shared tracks carry most layouts, so a 4 + 2 split meets the same gutter lines as a 3 + 3; twelve columns subdivide when needed. Margins, gutter, and baseline are fixed before anything is placed. White space is structure.
- **Asymmetry.** Flush left, ragged right; hierarchy by unequal spans. Centering needs a reason.
- **Weight follows size.** A size step brings its weight with it. Never pick a weight independently of the size band.
- **Surfaces carry complete palettes.** Paper, soft, dark, and accent fields each reset every foreground role, so nesting dark in paper or paper in dark stays readable.
- **Rules, not boxes.** A 2 px rule opens (a table, an index, a figure); hairlines separate; a thin ink rule closes. No plates, shadows, rounded corners, or tinted panels behind text.
- **Text never shrinks to fit.** When content does not fit, edit the words, choose another layout, or add a page.
- **One decisive move per unit**, and a rhythm across units: close reading, a turn, a burst. A few units speak a variation (see [variations](variations.md)).

## Type

Typographic quality here does not come from the typeface. It comes from four habits:

- **Restraint**: at most three faces, each with one role (display, text, labels and numbers). A face without a role goes.
- **Steps, not slopes**: few levels with wide gaps. At most three levels on a unit; adjacent levels at least about 1.25× apart; display to body around 4–7× (112 over 16). Because weight follows size, each step differs in both size and blackness.
- **Rhythm**: on a unit, one extreme scale contrast while everything else steps back; across units, close reading, a turn, a burst, with no grammar running more than two units.
- **Consistency**: a role keeps one size and one weight for the whole deliverable, so the reader learns the pattern and a deliberate break reads as deliberate.

The mother tongue fixes how size, weight, and spacing relate, not which typeface. The display face is chosen per deliverable from the content, the dialect, or the brand. Three lineages all belong here:

- **Grotesque, heavy**: the original Swiss voice (Akzidenz, Univers, Helvetica, and their heirs). Objective, structural.
- **Sans, thin at large sizes**: the later evolution, from Kenya Hara's restraint to Apple's hairline headlines. Quiet, precise, expensive.
- **Serif, high contrast**: Didone and heavy Song or Ming faces for fashion, editorial, and culture. Gravity and drama.

Whatever the face: body in a sans with full CJK coverage, labels and numbers in a neutral sans with good figures, at most three faces in one deliverable.

### Two modes

Weight follows size. A size step brings its weight with it; never pick a weight independently of the band. A deliverable runs in one mode and may switch for a section as a variation.

| Band | Size (px, A4 print) | Heavy mode · emphasis | Thin mode | Leading |
|---|---|---|---|---|
| Colossal · giant · hero | 280 · 196 · 112 | 900 | 200 | 1.0 |
| Display | 64 | 900 | 200 | 1.12 |
| H1 | 46 | 700 · 900 | 250 | 1.25 |
| H2 | 32 | 700 · 900 | 300 | 1.25 |
| H3, term | 24 | 600 · 800 | 400 | 1.25 |
| Lead | 20 | 600 · 800 | 400 | 1.6 |
| Body | 16 | 400 · 600 | 400 | 1.75 (CJK); serif reading text 1.5 |
| Small | 14 | 500 · 700 | 500 | 1.6 |
| Key | 13 | 600 · 800 | 600 | 1.6 |
| Aux: captions, labels, page numbers | 11 (print only; 12 minimum on screen) | 600 · 800 | 600 | 1.25–1.6 |

- **Heavy mode**: weight rises with size; emphasis adds 200 within the band, capped at 900. Suits a heavy grotesque or a heavy serif.
- **Thin mode**: weight falls as size grows, while small text stays at 500–600 so it holds on the page. Emphasis comes from size and position, never from bolding. Suits a sans with real hairline weights.
- A high-contrast Didone is set at its display weight in either mode; its contrast does the work weight would.
- Use real font files for every weight; never let the renderer synthesize bold.
- Numbers share the text's ladder and weight; tabular figures only in figure columns.
- Tracking: −0.04em for type cropped at an edge or at hero size; −0.02em for display and terms; 0 for text; +0.12em only for kickers and running heads.
- Measure about 34 characters for CJK body (about 65 Latin). A Latin technical term beside a Chinese heading is set at H3 in the accent.

## Color

The mother tongue fixes roles and relationships, not hues. The values come from the project's brand when there is one, otherwise from the subject's own world (a school's crest, a material, a place, a season), so no two deliverables share a palette by default. Choose the accent first; derive everything else from paper, ink, and accent.

| Role | Relationship | Use |
|---|---|---|
| Paper | The lightest ground: white on screen; in print, the stock itself | reading ground, ≥ 50% of the area |
| Soft | Paper shifted a few steps toward the accent's temperature, barely tinted | a quieter second field |
| Ink | Near-black, never pure black; may lean toward the accent's temperature | text, rules, structure |
| Muted | Ink lightened until it just holds 4.5:1 on paper and on soft, tinted toward the paper | secondary text, captions |
| Line | A grey about 1.3–1.5:1 against paper | hairlines only, never text |
| Dark | A near-black field; its text white, its muted text at least 7:1, its line clearly visible | full-bleed turns |
| Accent | One saturated hue; as text it holds 4.5:1 on paper, as a field it takes white or ink at 4.5:1 | emphasis: the kicker, the current item, the "now" tick, a dimension, a term |
| Accent on dark | The accent lightened until it holds 4.5:1 on the dark field | emphasis inside dark turns |
| Signal | Optional second ink, clearly different from the accent in hue and lightness; never used for text | route markers, a programme field, one flag |

The ground is paper by default. A whole unit set on the accent or the dark field is a turn: the roles swap (accent becomes the ground, paper becomes the type) and the three-role discipline still holds. Four surfaces (paper, soft, dark, accent) each carry a complete set of foreground roles. The accent stays near a tenth of the area (a fifth on a statement unit); the signal is rarer still. Greys are declared once as tokens and never invented per component.

## Images

Swiss photography is a fact: *Sachfotografie*, shown edge to edge or cut by a hard horizontal line, with no plate, shadow, radius, or scrim beyond what legibility needs. Geometry, diagrams, maps, and pictograms are native to the mother tongue.

Illustration belongs when it explains (a process, a mechanism, a scientific subject, a story that is itself the content of a children's book) and is drawn in the grammar of the page: flat, one consistent line weight, one style for the whole deliverable, built on the grid, colored only from the palette's roles. What stays out is illustration as filler: clip art, mascots added for friendliness, floating blob people, emoji, and icon sets that repeat what the text already says.

## Space and rules

Baseline 28 px on A4 (scale it with the surface). Spacing moves in baseline fractions: ¼, ½, 1, 1½, 2, 3, 4, 6 lines (7 / 14 / 28 / 42 / 56 / 84 / 112 / 168 px). Rules: hairline 1 px, rule 2 px, heavy 8 px.

## Furniture

Functional devices that become a deliverable's motif. Choose one or two and keep them.

- **Kopfzeile**, a meta row on six tracks (series · topic · number … page) over a 2 px rule; **Fusszeile**, a foot line on a hairline.
- **Verzeichnis**, numbered rows on hairlines for contents, rules, steps, credits.
- **Kennzahl**, a figure with its unit at a third of its size and a label, hung from a 2 px rule.
- **Zeitachse**, one 2 px axis with a tick per item and a single accent tick for now.
- **Bemassung**, a dimension line with end ticks and a value that stays real text.
- **Bildlegende**, a caption on six tracks: figure number | text across four | credit. **Abbildung** numbers lead captions in ink.
- **Tabelle**, opened by 2 px, separated by hairlines, closed by a thin ink rule. En-dash lists. One small accent square as a functional mark, never ornament.
- **Visible grid**, column fields or baselines drawn on purpose in the accent at 8–32%.

## Layout repertoire

Split 3 + 3; sidebar 4 + 2; offset 2 + 4; marginalia (note 1 : passage 3, paired row by row); hanging labels; comparison pairs sharing rows; chronology; photo essay 4 + 2; contact sheet in threes; bounded masonry; stagger; typographic (title across, aside 2, main 4); timeline; stair (*Treppe*, each line stepping one track right). With photographs: picture on top, type below (*Bild oben, Schrift unten*); bleed bottom, side, or outer edge; full bleed with a caption bar; overlay; a panorama across a spread. Choose by the unit's form, never by habit.

## Picture it

*Illustration, not a template.* A white A4 page: a Kopfzeile across the top; the title at 46 px, weight 700, over four tracks; a lead at 20 px, weight 600; body at 16 in two tracks of prose; a Kennzahl, "92%", hanging from a 2 px rule in the sixth track. Eight pages later a chapter opens in thin mode: one word at 196 px at weight 200, cropped by the right edge, on the soft field.

## The caricature and the habit

Asked for "Swiss style", models produce grey minimal skin: Helvetica, plenty of white, every page at one volume, no scale extreme, a red square as decoration. The opposite trap is this theme's own habit: "white page, black type, one red, hairlines" is now a default look for anything "designed". Use it when the brief chose it; let the furniture, the type mode, and the decisive move come from the content.
