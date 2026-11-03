# Memphis · the tile system

A kit of flat primitives, some drawn from the subject's own forms, tiled whole across one square module in clashing hues, with the type set as a block among the blocks.

> Use alone: read Overview and Images before any value; build the grid from your format by Layout. Tokens are at S = 1000 (S, the format's short side) and scale by S ÷ 1000, except a size the file derives from the format or a span, which is computed, never scaled. Content in one language takes that language's sizes. A unit carries one form, or a lead form with a quiet one beneath. Check the piece against Do's and Don'ts.

## Overview

Memphis, as its graphics are made now, after Sottsass and Du Pasquier's laminates (1978–87): draw a kit of flat primitives, some abstracted from the subject's own forms, tile one square module field whole in clashing hues, and set the type as a block among the blocks; never a kit that would fit any subject, never pattern behind reading text.

World: any content, on any surface: decks, posters, covers, identities, merchandise. Serious content is translated, not refused: the clash marks its parts honestly, and its facts stay on solid blocks. Every piece keeps the module, the palette, the base kit, the faces and its field shapes; each brings its subject tiles and its words.

Method:
1. Draw the kit: six base tiles, and two to four drawn from the subject, its outlines abstracted onto the module as Ikko Tanaka abstracted a motif.
2. Choose the field: one shape per unit (an L, a band, a column, a corner); a series keeps its shapes.
3. Tile it whole: one tile per cell, never the same ground beside or above; the subject tiles where the eye lands first, at the field's corner or end.
4. Merge cells for the type block, on one solid hue.
5. Set the facts on solid blocks of whole cells.

Amplitude: full in the field, quiet in the blocks.

Anti-reference: a generic flower-and-star kit; squiggle confetti; an 80s pastel palette; CSS objects with shadows.

## Images

Computed: the kit, drawn flat on the module. A real photograph may fill a block of whole cells, framed by tiles. Characters and illustrations are hand-made, or generated and declared; never drawn in code.

## Layout

Grid system: Modular — one square tile; every block is whole tiles.

S = min(W, H); tile M = S ÷ 8. Columns and rows are the whole tiles that fit; the remainder is one solid band at the foot (portrait) or the right edge (landscape). The field runs to the trim. Field shapes: an L (three columns down one side, two rows along the foot), a band (one or two rows across), a column (two or three columns down one side), a corner (two by two to three by three). Every cell outside the field belongs to a solid block that carries type; no cell is empty by accident.

## Typography

- **League Spartan** (OFL, variable 100–900): the title as a hairline line (200) over black lines (800) at one size, the largest line filling the type block's width; facts 800 at 64; body 500 at 30; labels 500 at 26.
- **Noto Sans SC** (OFL): titles 900, body 500; never smaller than the Latin it translates.
- Inset 0.3 M inside a block; flush left; no tracking; tabular figures. Nothing read below 26.

## Colors

- **Cobalt `#2D3A9E`, rose `#E8124F`, orange `#F47A20`.** Tiles, the type block and fact blocks; a hue that names a category keeps it everywhere.
- **Cream `#FCE6B4` and white `#FFFFFF`.** Tiles and quiet blocks.
- **Ink `#141414` (primary).** Type on orange, cream and white; the foot band.
- White on cobalt and rose; ink on everything else. Emphasis is a block's hue or size, never a new colour.

## Shapes

Flat; no outline, shadow or gradient. One figure per tile, its edges on the tile's quarters, turned by 90°. Base kit: quarter disc, half disc, disc, four-petal flower, star, rounded cross, leaf, arch, four-by-four checker, stripes. A subject tile follows the same rules and joins the kit before use.

## Forms

- **Cover:** an L field, the title block, the facts on solid blocks.
- **Statement:** one sentence in the type block, the field a column.
- **Exhibit:** a photograph or one subject tile at two by two, framed by the field.
- **Data:** each value on its own block, the figure at fact size; a quantity may be a count of whole tiles, never a tile's size or pattern.
- **Sequence and comparison:** a band of tiles marks the order, one tile above each step's block; comparisons side by side on one row.
- **Reference and close:** body text on cream blocks; the next action on a rose block.

## Variations

- **Pixel Chinese.** The Chinese title in an open pixel face (Fusion Pixel or Ark Pixel, OFL) at display size only; once per series.
- **Isometric volume** (Peter Shire). One unit's figure built as a volume of clashing parts in isometric projection, the type on its faces.
- **Night field.** The ground blocks in ink, the tiles unchanged.

## Do's and Don'ts

- **Look before delivering:** render it, see it full size and as a thumbnail. A kit that would fit any subject, two neighbours on one ground, text on a pattern, a cell nobody placed: faults.
- **Floors:** facts verbatim and live; every pair in Tokens holds its contrast.
- **Test:** swap in another subject's content, and the kit no longer fits; remove the clash and the tiling, and the character goes.
- **Caricature:** a generic flower-and-star kit on any subject; squiggle confetti; Memphis as wallpaper behind a Swiss page.

## Tokens

```yaml
colors:
  primary: "#141414"
  neutral: "#FFFFFF"
  cream: "#FCE6B4"
  cobalt: "#2D3A9E"
  rose: "#E8124F"
  orange: "#F47A20"
typography:
  title: { fontFamily: "League Spartan, Noto Sans SC, sans-serif", fontSize: 104, fontWeight: 800, lineHeight: 0.98 }
  title-light: { fontFamily: "League Spartan, Noto Sans SC, sans-serif", fontSize: 104, fontWeight: 200, lineHeight: 0.98 }
  fact: { fontFamily: "League Spartan, Noto Sans SC, sans-serif", fontSize: 64, fontWeight: 800, lineHeight: 1 }
  body: { fontFamily: "League Spartan, Noto Sans SC, sans-serif", fontSize: 30, fontWeight: 500, lineHeight: 1.35 }
  label: { fontFamily: "League Spartan, Noto Sans SC, sans-serif", fontSize: 26, fontWeight: 500, lineHeight: 1.3 }
spacing:
  tile: 125
  inset: 38
pairs:
  ink-on-white: { backgroundColor: "{colors.neutral}", textColor: "{colors.primary}" }
  ink-on-cream: { backgroundColor: "{colors.cream}", textColor: "{colors.primary}" }
  ink-on-orange: { backgroundColor: "{colors.orange}", textColor: "{colors.primary}" }
  white-on-cobalt: { backgroundColor: "{colors.cobalt}", textColor: "{colors.neutral}" }
  white-on-rose: { backgroundColor: "{colors.rose}", textColor: "{colors.neutral}" }
```

## Record

Folio version: 1.1.0. Template version: 14. Date: 2026-11-03.
Pieces: the-grid/brief.md, made from an earlier version of this file (primitives clad in laminate on slabs); it does not show the tile system.
