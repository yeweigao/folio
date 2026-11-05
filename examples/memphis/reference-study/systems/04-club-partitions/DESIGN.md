# Club Partitions · black seams and clipped curves

A system for club programs whose lineups and facts alternate with large, interlocking colour fields.

> Use alone: read Overview and Images, then construct Layout from W × H. S = 1000 is the reference short side; scale token values by the actual S ÷ 1000. Compute sizes derived from a region in that region. Recompose longer content before changing a reading size. One unit has one lead; use the Forms and final visual checks below.

## Overview
Memphis-inflected partition study, observed hand — Build a black-seamed field in which hard information rectangles and clipped, unlike curves push against each other; never fill a neutral page with isolated motif windows. Authorship and original typefaces are unverified.
World: Keep coarse black seams, paper reading bays, substantial blue and orange-red fields, and mixed curved/diagonal contacts across a program. Each piece supplies its own lead, group lengths, number of bays and contour arrangement. A different subject becomes groups of named information interleaved with the same pressured field; the source's particular positions are not a template.
Method: Group the content first and size clean rectangles for the longest lines. Join their boundaries into a stepped partition skeleton. In the remaining connected field, cut a broad arc, oppose it with a diagonal wedge, then pinch or open a black negative gap. Let these operations determine each new contour instead of repeating one wave. Add type after the graphic and reading regions are resolved.
Amplitude: Keep bold colour and large black/paper reversals. A quiet unit reduces the number of contacts while retaining their scale and the uninterrupted reading bays.
Anti-reference: A full-width title masthead above a gallery of unrelated geometric cards.

## Images
Draw native vector contours and live type; use solid fills and boolean cuts. No photographic role is required. A graphic field meets a partition edge or trim rather than floating inside a card. Uniformly scale a contour before clipping it; preserve the arc-to-straight-edge or lobe-to-gap contact that gives it its identity. Rebuild the arrangement for a new aspect ratio. Source images are study evidence, never production artwork; credit any separately commissioned imagery in that piece's brief.

## Layout
Grid system: Hierarchical — derive rectangular bays from the content, with two or three unequal vertical tracks and staggered horizontal breaks. A reading bay spans roughly 0.35–0.65 W; change its span or line breaks for long names. In landscape, place more bays alongside one another; in portrait, stagger more rows; in square, distribute the turn across both axes. No axis has a prescribed source coordinate.
Use the ink field as the shared gutter and outer seam, with the `seam` token as its usual width. A seam can open into a larger black negative region; never draw a second border around every bay. Reading and graphic bays alternate along at least one axis, and at least one colour/curve construction reaches trim. If a title expands, let a partition or colour contact continue beside it so the title remains part of the field.
Inset visible letter ink from the seam by at least `inset`. Separate a label from its associated names by half that label's line height; separate unrelated reading groups by at least one body line height. Preserve each named group as a unit. Allocate surplus area to extending a graphic field or a deliberate paper pause, not to stretching text or inventing information.

## Typography
Use Study Sans 700 for the `lead`, `names`, `facts` and `label` roles, Study Sans 400 for `body`, paired with Study CJK at the same role weight. These are the licensed Inter/Noto Sans SC study aliases recorded in [fonts.json](../../assets/fonts.json), not identified original faces. Embed fresh glyph subsets for new content.
Give the lead level to either the title or the primary named group, according to the brief; the other groups use the lower steps. Names are heavy, ordinary-width sans serif with close but separate lines. Keep figures in the same family and weight as their role. Labels are compact and secondary. The `body` token is the smallest reading size. For either language, break a long lead into semantic lines or enlarge its bay; never horizontally squeeze glyphs or shrink all facts to preserve a contour.

## Colors
`paper` is the uninterrupted reading ground and the bright half of black/paper negative forms. `ink` carries seams, large gaps and all text on paper or `red`; paper text may reverse on ink. `blue` and orange-red `red` form substantial, opposing graphic fields rather than tiny accents; retain both when colour is used. A colour can cross a partition through a contour, but must not tint an unrelated reading group to imply a new category.
Small labels touching blue use paper, including labels attached to a blue graphic field. Use only the text/ground combinations in `pairs`; coloured shapes need not satisfy reading contrast. Do not substitute black small text on blue.

## Shapes
Keep square bay corners and a constant coarse seam. Build three related operations: clipped circular/elliptical arcs with radii about 0.25–0.70 S; diagonal wedges whose long edges cross a bay at about 10–35 degrees; and local rounded lobes about 0.08–0.20 S in radius that press into a larger white or black field. These are construction ranges, not a requirement to fit every shape into an equal box.
In a multi-bay unit, use at least two unlike operations: an arc meeting a wedge and/or a convex lobe opposing a concave cut. If there is only one graphic bay, combine the unlike contacts within it. Let a black channel narrow to roughly one to three seam widths before widening into a black field. Clip arcs and wedges at the bay/trim so their continuation is felt; do not close every contour into a self-contained badge. Avoid duplicating the same S-shaped white ribbon in different bays. Use outlines only where a seam or contour contact needs separation; no universal outline, rounded-card or shadow treatment.

## Forms
Cover: fit the title or primary names into a paper/ink bay that participates in the partition field; no detached masthead.
Statement / Opener / Close: use one reading bay and one large opposing cut, reducing contacts rather than shrinking them; no decorative filler.
Exhibit: let one identifiable subject occupy a graphic bay, preserving its silhouette at the crop; no competing miniature subjects.
Collection / Reference: align peer groups to bay edges with stable name/label steps and predictable order; no invented ranking.
Argument / Comparison: give the judgment and evidence separate clean bays, with shared scales and direct labels; no curves through data or colour-only distinctions.
Sequence / Exercise: assign each action or task its own bay or unit in reading order; keep required answers or continuation space clear of contours.

## Variations
Change track widths, row count, lead bay and contour direction with the content. Black/paper negative forms may connect two graphic regions, provided no reading group is invaded. A fact strip may run along any suitable hard edge; its position is not fixed. Quiet turns can use one large arc/wedge contact, while dense turns add bays before reducing reading type.

## Do's and Don'ts
At thumbnail size, read one lead and the stepped black skeleton before small facts. In grayscale, paper bays and the black gaps must still alternate; blue/red alone cannot carry the structure. Check that at least one diagonal or pinched contact interrupts the broad curves, and that the colour fields remain connected to the composition rather than confined to incidental windows. At reading size, verify visible ink clearance and complete group content.
Caricature: coarse borders and bright colours surrounding two copies of the same smooth wave. A changed contour arrangement is welcome; losing the mixed contour grammar is not.

## Tokens

```yaml
colors:
  paper: "#F9F9F6"
  ink: "#000000"
  blue: "#0969F9"
  red: "#FF3A06"
typography:
  lead: { fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 96, fontWeight: 700, lineHeight: 1 }
  names: { fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 60, fontWeight: 700, lineHeight: 1.05 }
  facts: { fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 54, fontWeight: 700, lineHeight: 1.05 }
  label: { fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 24, fontWeight: 700, lineHeight: 1.15 }
  body: { fontFamily: "Study Sans, Study CJK, sans-serif", fontSize: 24, fontWeight: 400, lineHeight: 1.4 }
spacing:
  seam: 11
  inset: 22
pairs:
  ink-on-paper: { backgroundColor: "{colors.paper}", textColor: "{colors.ink}" }
  ink-on-red: { backgroundColor: "{colors.red}", textColor: "{colors.ink}" }
  paper-on-ink: { backgroundColor: "{colors.ink}", textColor: "{colors.paper}" }
  paper-on-blue: { backgroundColor: "{colors.blue}", textColor: "{colors.paper}" }
```

## Record
Folio version: 1.1.0. Template version: 14. Date: 2026-11-05.
Study piece: [partition reconstruction](../../posters/03-tresor.svg).
Transfer: [修订版 v2](../../batch-transfer/cases/04-club-partitions/frozen-v2/poster.png) 由仅持冻结规则、新简报、授权字体及中性嵌字工具的全新上下文独立制作。身份、构成、工艺三项匿名评审均通过；原始评论与解码见 [批量结果](../../batch-transfer/RESULTS.md)。基线输入、规则与各轮作品均保持留存。
Verification: 当前施工正文与冻结 input-v2 逐字相同，仅本 Record 回写结果。已检查固定文字、实际字体、文字对比度、图像与可见裁切，并通过 folio-check。每套仅一份新简报，不代表所有内容、画幅或字形可靠。
