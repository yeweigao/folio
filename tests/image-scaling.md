# Native picture scaling audit

Regression for `scripts/imagecheck.py`, using the real error found during the 岩序 portfolio work. This checks source-crop/frame geometry, not visual authorship. Run from the repository root when the local artifacts are available:

```sh
python3 scripts/imagecheck.py exports/yanxu-line-world/revision-1/岩序-品牌视觉概念.pptx
python3 scripts/imagecheck.py exports/yanxu-line-world/岩序-品牌视觉概念-v2.pptx
```

Expected: the first exits 1, flagging pages 02, 06 and 08; the second exits 0, checking all six native pictures without flags or review omissions. On 2026-11-04 the old anisotropy was 51.463%, 4.457% and 4.457%; repaired pictures were below 0.002%. The old helper used frame dimensions as source dimensions; this audit reads the embedded raster independently.

Small generated PNG/JPEG/GIF fixtures also verify decoded dimensions; a copied native picture with a non-default destination fill rectangle must be reported for review rather than accepted. Those checks passed on the same date. Unsupported vector media, EXIF-bearing JPEGs, non-default fills and grouped transforms are review cases. A matching aspect ratio says nothing about crop quality, subject identity or the rendered export's other transformations.

The real decks stay in ignored local exports; the readable example and previews are in `examples/swiss/`. No binary fixture is required to use the skill.
