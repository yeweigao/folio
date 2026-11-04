# Tea identity — four structural line tasks

## Facts

Identity: `岩序`, `YANXU`, `品牌视觉概念`, `概念样张`.

Page A: `岩，是触感与光线。`, `序，是一次冲泡的节奏。`.

Page B: `目录`; four consecutive chapters `A1`, `品牌设计`, `04—10`; `B2`, `包装设计`, `11—14`; `C3`, `海报设计`, `15`; `D4`, `字体系统`, `16`.

Page C: `名称先被看见`; label content `岩序`, `YANXU`, `岩骨`, `风味联想 / 焙火与熟果`, `冲泡提示 / 详见行动路径`, `概念茶样`; annotation `先认出你要泡哪一款茶。`.

Page D: `给动作一个顺序，给浸泡一点等待。`; process `温器`, `投茶`, `注水`, `浸泡`, `出汤`; state labels `动作`, `等待`; note `顺序示意，不表示时长`.

## Reader and outcome

Make four 1920 × 1080 read-alone portfolio pages for a Chinese-speaking design client, using one coherent restrained typographic system. Chinese leads and English identifies. Use the supplied local Inter and Noto Sans SC font files. Use white #FFFFFF, charcoal #161815, moss #67735F, optional paper #F5F3ED and secondary text #646860. Do not add product claims, years, quantity, brewing parameters or extra sections. The work is a concept identity, not a marketed product.

The assignment is specifically to make line a major compositional material. Replacing it with an ordinary table, header underline, four equal cards or stock timeline does not fulfill the assignment. Text remains live. No photographs are needed for this focused test; the flat label on C is a native typographic specimen.

## Page tasks

- **A — Relate two regions.** The identity and the two source phrases must form one composition across an open field. Make the material side and the reading/preparation side feel connected while preserving a substantial interval. A screen has no physical fold: do not fabricate a spine. The leading line should give the groups their relationship and positioning.
- **B — Common origin, four entries.** Show four chapters unfolding in order from a common whole. Let the line organize where entries are suspended and how the open space is divided. Keep lookup immediate and keep the field open. A ruled list alone is insufficient.
- **C — One exact target.** Exhibit a readable flat label and use the leading line to bring attention to its product name 岩骨. Keep brand name, flavor association and preparation hint legible and outside the annotation's interference. The reader must know precisely what was marked, rather than just see a decorative diagonal.
- **D — Order plus state.** Make the five preparation steps a connected passage. 温器、投茶、注水、出汤 are actions; 浸泡 is waiting. Let the leading line itself carry that distinction in addition to order. Distances are not elapsed time and height is not amount. Explain the distinction briefly using the supplied labels and note.

## Common implementation contract

Create four independent HTML files A.html, B.html, C.html, D.html. Put the leading line's geometry and its nodes/rings/branches in an SVG group with `data-editorial-line="lead"`. Keep all reading text outside that group, including any text visually inside a ring. Give it no label that reveals the experimental arm. Ordinary page rules may remain separate.

Create PNGs A.png through D.png. Also create A-off.png through D-off.png from the same layout with only `[data-editorial-line="lead"]` hidden; keep every text, position, color and other object unchanged. This is a removal test, not an alternate design. If the main line is absent or cannot be separated from text, report the failure instead of staging the result.

## Evaluation, fixed before generation

First check facts, reading, overlap and concept honesty. Then compare the complete and line-removed views for each task. Score 0–3 for each axis, never line count:

1. **Relationship:** 0 absent/incorrect; 1 mostly described by labels; 2 visible in the line; 3 line makes the specific relationship immediately legible.
2. **Compositional work:** 0 ornamental; 1 a divider beside a complete layout; 2 it visibly anchors groups or divides the field; 3 it organizes the principal composition and removal materially weakens that organization.
3. **Construction and reading:** 0 interference/disconnection; 1 material imprecision; 2 connected and readable; 3 exact endpoints/nodes/clearance with no reading interference.

Give visual quality separately as a qualitative comment. A variation may satisfy the line task yet be aesthetically weaker. State ties and limitations. This is a small targeted test, not evidence of general superiority.
