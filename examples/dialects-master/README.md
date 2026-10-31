# Dialect master examples — nine dialects, one evening

One fictional public programme (a lecture evening about the grid
itself — no product, no brand, nothing to sell; `content.md` is the
fixed source) set nine times: once in each Swiss dialect, at full
strength, each as a poster with its own locked `DESIGN.md` and
generated `preview.html`.

Open `index.html` for the contact sheet. Each folder holds
`poster.html` (the render), `DESIGN.md` (the lock: tokens, governing
hand, signature line, the dialect's test), and `preview.html` (the
token catalog). Every DESIGN.md passes `scripts/folio-check.py` with
its poster, and Google's `@google/design.md` lint at 0 errors /
0 warnings (verified 2026-10-31 for v0.5.1).

## Why the content is held still

A dialect example with its own bespoke content proves nothing: the
content does the work and the dialect takes the credit. Held still,
the nine posters differ only in design — which is the claim a dialect
makes. The facts are identical and exact in all nine (the grid evening:
three talks, a foyer exhibition, one date, one hall), including the
"Illustrative example" line each poster carries.

## What was borrowed, and from whom

This set deliberately copies the strongest moves found in the
2026-10-31 survey of other design skills:

- **One content × many systems** — the organising idea of
  VoltAgent/awesome-design-md (the same page specified under dozens of
  brand systems), inverted: here one system shows its nine dialects.
- **Named settings beside every render** — taste-skill's dials. Each
  DESIGN.md records its parameters as numbers (rotation −6°, overprint
  slipped 4px, planes in declared proportions), so "Punk" is a setting,
  not a mood.
- **The caricature printed next to the example** — impeccable's
  anti-pattern discipline, which Folio already keeps in its dialect
  files; each DESIGN.md's Do's and Don'ts repeats the ruled-out
  caricature so a reader can check the render against it.
- **A lint-clean spec per example** — Google's design.md format and
  CLI: the example is not a picture of a system, it is the system,
  machine-checked.

## Using the set

When a direction names a dialect, render the hardest unit beside the
matching poster here before choosing (SKILL.md step 5): the poster is
what "full strength" means for that dialect, and the recognition test
at Inspect is judged against it — would this unit be mistaken for the
example's dialect, or only for the mother tongue with decorations?

## The blind test (v0.5.2)

These files claim to be master-level demos, so they were tested the
hard way: fresh agents, each permitted to read **only its one
DESIGN.md** — nothing else in this skill, no reference render — rebuilt
all nine posters. Every blind render was recognisably its dialect with
the labels covered; the strongest (Swiss Brutal, Ulm) converged with
the references nearly line for line. The test's real yield was the
agents' contradiction lists: token-versus-prose sizes, zone arithmetic
that did not close, facts a build spec silently truncated. Each is
fixed in the current files. The lesson the set now teaches: a DESIGN.md
earns "master-level" only when a stranger with nothing else can build
the work from it — system, composition, and facts alike.
