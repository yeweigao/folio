# Family — a master DESIGN.md and its overrides

Borrowed from ui-ux-pro-max's Master + Overrides pattern, in Folio's terms.
A family is a set of deliverables that share one system: a report series,
a course, a product's decks and handbook.

- **The master** is a locked DESIGN.md kept with the family, not with any
  one deliverable. It holds the system once: tokens, grid, faces, method
  habits, the dialect, and the floors as adopted.
- **A deliverable** records its master in Record (name and version) and
  writes under Overrides only what differs: a token value, a surface's
  sizes, a unit the master did not foresee — each with its reason.
- **Precedence:** floors > master > override. An override never silently
  contradicts the master; a contradiction is either a master change or it
  does not ship.
- **Upgrading the master** follows SKILL.md's floor on shared systems: new
  version, a change note, one dense and one sparse deliverable rechecked
  against it, the previous master kept.
- folio-check runs on master + override merged: read the master first,
  apply the override's token values, then check.
