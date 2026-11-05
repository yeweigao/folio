# Audit — Apple theme, after the master-edition reverse iteration

Scope: theme.md, all files under dialects/, and all files under examples/ in this folder only. Evidence: the master works approved by the user — 16 master PPT decks, the master Flyer and Website page, and the master 32-world page — not the earlier test cards. Method: every file read, and the checks below verified by grep over the files as they stand after Stages 1–4, plus release-check after each stage.

## Checks

### (a) Alignment — PASS, after a fix found by this audit

Rule: a centred container is never centred text; body, leads, captions, card names and prices are flush left, ragged right, in every surface and format; only a hero, vista or cover headline may centre.

- The audit first found the rule stated only in theme.md and in the Store and Editorial surface files, and silent in every industry dialect file and every example file. Silence was the original bug: a builder reading only a dialect file and an example had no alignment sentence to follow, and centred the body.
- Fixed in this audit: an alignment sentence was added to all 12 dialect files and to the Layout section of all 16 example files. Grep now finds "flush left" in all 12 dialect files, all 16 example files, and theme.md.
- Remaining note: the rule is now stated everywhere, but a future builder could still centre a body by copying a hero template. The rule's presence is verified; its enforcement in a future build is not.

### (b) Accent replacement — PASS by substance, with seven stated exceptions

Rule: a governing hand's single accent replaces every Apple blue role for that work, and Apple blues retire for that work.

- The exact phrase is present in all 12 dialect files, in theme.md, and in 9 example files.
- The other 7 example files state the same rule by substance, and forcing the exact phrase into them would be false: mother-tongue has no governing hand, so no replacement applies; developer's chromatic event is a hero-scale gradient verb, not a flat accent beside blue; minimalist, minimalist-muji and minimalist-bang-olufsen carry no chromatic accent, so no accent is introduced; luxury-chanel carries black as its action, not a chromatic accent; luxury-louis-vuitton carries photography as its chromatic event, with a neutral or dark action treatment.
- No example states two accents, and no example keeps Apple blue beside its hand's accent.

### (c) Vista, three kinds — PASS

Rule: an Editorial vista is one of three kinds — photographic, proof-field, or diagram — each full-bleed with one headline and at most one action, and a diagram vista must be readable as a diagram.

- Theme.md and the Editorial surface file define the three kinds. All 16 example files name their kind in their Three-rules section: photographic in 10 (mother-tongue, showroom, consumer, luxury, luxury-burberry, luxury-chanel, luxury-louis-vuitton, minimalist, minimalist-muji, minimalist-bang-olufsen), proof-field in 4 (developer, finance, ai, engineering-teenage-engineering), diagram in 2 (engineering, engineering-vitsoe).
- Industry dialect files do not restate the three kinds; they defer to the Editorial surface. That is silence, not contradiction, and is recorded here rather than hidden.

### (d) Bento, index not proof — PASS

Rule: a Bento unit is an index, never proof; each tile's claim is provable in a following unit, or the tile itself carries its checkable number, label or figure.

- Stated in theme.md, in the Bento method file, and in all 16 example files. No example claims a Bento-only proof.

### (e) Values in dialect files — PASS for industry dialects and for this iteration; ONE OPEN ITEM for surface files

- Grep over the 8 industry dialect files finds no hex value and no digit-plus-unit value (no px, pt, or cm pattern). The blocks added in Stages 2 and 4 contain no digits at all, verified by script.
- OPEN ITEM, listed plainly, not hidden: the three surface files in the same folder do contain values from before this iteration — Store (card hairline, radius and padding in px), Editorial (lead and column sizes in px, weights as numbers), and Keynote (slide steps in pt, weights as numbers). These are surface specifications, not industry philosophy, and they were not removed in this iteration, because removing them would change surface specifications without a decision. The audit therefore does NOT claim a clean pass on check (e) as written for the whole dialects/ folder. The decision needed is: either scope the philosophy-only rule to industry dialect files, or move surface values out of surface files. Until that decision is made, this item stays open.

### (f) Examples table — PASS

- Theme.md's Examples table links 16 DESIGN.md files, and all 16 files exist under examples/. No table link is broken, and no example folder is unlisted.

### (g) Release check — PASS

- Release check passed after Stage 1, after Stage 2, after Stage 3, and after this audit's fixes: 64 files routed, release check PASS, at the final state. Changes in this iteration stayed inside references/themes/apple/ only; no file outside that folder was touched.

## Conflicts resolved, and conflicts that text alone does not fix

- Relay gradient and mono: resolved in text. The Developer dialect file and the Developer example now require a gradient verb at hero scale only (never wallpaper, never button or card) and mono for technical labels only (never body), and state that an abstract placeholder-bar interface is not proof because proof must be readable. This resolves the conflict between the DESIGN intent and the master PPT brief, which imposed a single flat accent and Inter throughout.
- NOT fixed by text: the master Relay deck itself still does not follow that restored intent — it was built under the conflicting brief, its proof interfaces are abstract placeholder bars, and its 84 pt number shape carries overflow warnings verified only in LibreOffice rendering, not in PowerPoint. The next master rebuild of Relay must follow the restored DESIGN, or the conflict will recur in the work even though the files now agree.
- Image reuse: declared, not hidden. Several master decks reuse one image at a different crop or scale across slides (Atelier detail, Kit detail, Shelf hero). The DESIGN and dialect files now require reuse to be declared; a reused image is a second use, not a second proof.
- Tabular figures: not claimed. OfficeCLI has no tabular-numerals property, so no file in this theme claims tabular setting from an OfficeCLI deck; the fallback is a right-aligned figure column so decimals line up.
- Fonts: named, never embedded. Serif display is a substitute where a DESIGN calls for a serif overturn (Fern, Pebble, the four Luxury decks); spacing is buffered against substitution shifting line breaks.
- Cover variety: a set-level weakness, not fixed by a rule alone. Most master covers use right-half heroes; only Relay, Aero, Pebble and Volt use full-bleed covers. The theme now states that repeating one cover structure is a weakness, but a future set must still be checked for variety, not assumed varied because the rule exists.

## Verdict

Pass with one open item: check (e) for surface files. Every other check passes as stated above, with the Relay deck limitation and the cover-variety weakness recorded as limitations, not as passes.


## Integration update — 2026-11-05

The philosophy-only constraint now explicitly applies to industry dialects; surface and method files may carry construction values. This resolves the scope decision in item (e), rather than deleting the Store, Keynote and Editorial specifications.

The 16 standalone examples now use the repository's Tokens YAML schema, declare reference scale and grid, name their method and record template versions. Concrete colour and portable font choices added here are authored example values, not recovered brand specifications. The supplied continuous corner brief, native API choices, nested radius relation and vector-export requirements are present in the theme and standalone examples; all 12 dialect/surface/method files route that contour into new skeletons.

Release-check now includes theme-local examples: 37 total skeletons pass structural and declared text/ground contrast checks. This does not validate newly generated geometry, font substitution or rendered visual quality; no new rendered sample, independent transfer or old/new/no-skill comparison was made for this integration update. The master-deck limitations above remain historical observations, not claims that these documentation changes fixed those decks.


## Native contour render check — 2026-11-05

A local validation sheet was rendered from actual macOS SwiftUI `RoundedRectangle(cornerRadius: R, style: .continuous)` paths, covering six radius steps, narrow and saturated controls, a nested R56/R44 pair with inset 12, and the card radii and palettes of all 16 example skeletons. The six rendered panels were inspected; circular and n=4 superellipse controls were explicitly labelled as rejected alternatives. Local output is under `exports/apple-continuous-corner/`.

Nine native Quartz / Chromium SVG threshold-mask comparisons reached at least 99.80% intersection over union at 2× scale. The sampled native shoulder extent was 1.528665R. The nested pair's dense-path gap was approximately 11.83–12.02 reference pixels for a declared inset of 12. These checks establish this native contour and its SVG export; they do not prove identical Figma geometry or analytical G2 continuity at every internal cubic approximation join.

The old Apple master decks, flyer and website source files were not found in the local workspace or searched artifact locations. The user subsequently confirmed that the old works had been deleted. This check therefore renders new geometry specimens, not those original works; no original-work rerender is claimed. Font choices, source photography and full composition of those old works have not been revalidated.
