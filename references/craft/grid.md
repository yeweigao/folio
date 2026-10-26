# Grid

The grid fixes how things relate before deciding what they look like. Without one, AI layouts fall back to equal thirds and centered stacks.

- **The grid is solved from the format, not picked from a preset.** Content = n × column + (n − 1) × gutter; column k starts at margin + k × (column + gutter). Each surface file holds its numbers.
- **Tracks are construction lines, not columns to fill.** Six tracks start most work: 3 + 3 makes peers, 4 + 2 priority, a full span interrupts. Subdivide to twelve only for an alignment the content needs; an unused track is not a vacancy.
- **Asymmetry carries priority, not novelty.** Unequal spans for a lead; equal spans for real peers. Never invent priority to avoid symmetry.
- **Axes are few and visible, not many and accidental.** Two or three vertical axes, repeated; image edges, title starts, captions, and sources share them.
- **Space comes from one module, not from the eye.** Half within a group, one between peers, two between sections. Rules and image edges sit on the module; baselines follow leading.
- **Alignment is optical, not arithmetic.** Round and pointed forms overshoot; quotes and points hang; large titles compensate for side bearing.
- **Breakpoints are where content breaks, not device names.** Reflow to 320 CSS px; on a canvas, groups form by distance and connectors run orthogonally.

| Reading need | Composition | Invariant |
|---|---|---|
| Compare peers | 3 + 3, criteria in shared rows | Row alignment, units, scales |
| Read with evidence | 4 + 2 or 2 + 4 | Text and evidence share an anchor |
| Annotate | Narrow note track beside the reading column | Each note beside its passage |
| Argue | Claim, one exhibit, implication | One left axis, claim before evidence |
| Survey | Contact sheet | Comparable crops, aligned caption baselines |
| Carry a brand | A unit derived from the actual mark | Its proportions and clear space |
