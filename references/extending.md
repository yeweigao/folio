# Extending Folio

For editing the skill, not for making a deliverable.

## Laws

- **A line earns its place in a test, or it goes.** Run the old version, the new one and no skill on the same fixed briefs (`tests/`), judged blind. Removing a line is a normal result.
- **Write only what models do not already do.**
- **Names carry methods.** A master enters the library as a way of working: first move, tools and materials, procedure, one ban.
- **Knowledge lives where a choice is made:** a roster, a card, a table row, a test.
- **Tools, not conclusions.** A rule a machine can check goes into `scripts/`.
- **Only floors are hard.** The rest is the author's eye, held by review.
- **Principles in the files, history in git.** No instances, anecdotes or version notes inside the rules; dated measurements live only in review.md's list.

## Contracts

- **Dialect** (`references/themes/<theme>/dialects/<name>.md`): invocation; four lines correcting the mother tongue; three or four hands, each as process, tools and material, with what it suits and one ban; what Swiss keeps; test; caricature. Proven by a skeleton in `examples/` and a second piece made from it alone.
- **Hand:** work and date, first move, tools and materials, what it suits, one ban.
- **Signature card:** construction, parameters, test, caricature; proven by a build from the card alone.
- **Grid system:** construction, material, discipline; proven by a build where it visibly governs.
- **Client-language row:** the phrase, the dials, the translation as parameters, Folio's keeping.
- **Surface:** reader conditions, size floors, starting values, "Done means".
- **Theme:** `theme.md` with hands, grammar, grid roster, methods, variations, anti-patterns, and its dialects.
- **Gate:** added to `folio-check.py` when a floor breaks in a test; deterministic, stdlib only.

## Releases

- The version lives in SKILL.md's frontmatter; README mirrors it.
- `python3 scripts/release-check.py` passes: versions agree, every example skeleton passes folio-check, every example piece passes factcheck.
- A change to SKILL.md, the theme or a dialect ships with a test against the previous version and no skill; the CHANGELOG states the result and what remains unproven.
