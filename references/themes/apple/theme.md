# Apple — the gallery marketing language

Apple's public marketing language as apple.com and the launch keynotes speak it now, in the Liquid Glass era: the product as a sculpture on a solid field, one claim per field, the interface retreating until it is invisible. Not the Human Interface Guidelines, which govern product interfaces.

**The name is the instruction.** A model already knows apple.com, and knows Notion, Linear or Stripe from their sites, design systems and a thousand imitations. A work is named *Apple + Notion style*, and the name carries the look. This file adds only what a name does not: how a brand joins Apple, where models go wrong, and the corner they cannot draw.

## Use

| Choose | From | Written into DESIGN.md |
|---|---|---|
| The name: Apple + a brand, or Apple alone | How a brand joins Apple; the industry routes, the input picks the brand | Title and Overview, the invocation |
| The field | Fields | Layout, Grid system |
| The surface, when the deliverable is a deck, a shop or a long read | Keynote, Store, Editorial; then the delivery surface in Routes | Layout, Forms |
| Bento, when many features must read in one glance | [Bento](dialects/bento.md) | Forms or Variations |
| The corrections and values that apply | Corrections, Values | Do's and Don'ts, Tokens |
| The contour | Continuous corner | Shapes, Tokens |

Going wide means different brands on this subject, Apple alone among them, not different colours of one page.

## Fields

*Gallery* — one product per tile, full bleed, the stack centred; *Utility grid* — hairline cards three to five across, for shops and comparison; *Editorial column* — one centred column of about 980 px; *Slide field* — 16:9, one thesis per slide.

## How a brand joins Apple

- **A brand the user names governs; otherwise you choose one.** The industry follows the claim, the brand the input's kind, and the choice is written into the name and said; Apple alone stays among the roughs. The subject's own brand is never its hand: that is its own site, not Apple's turn on it.
- **Apple is the base.** One lead per screen; the product or its proof at gallery scale; the change of ground as the divider, visible at thumbnail; weight as hierarchy; one accent.
- **The signature anchors; the name fills in.** Each brand line names what a designer would name first — its ground, its one colour, its hero, its type — and what it overturns in Apple; the rest stays Apple. Values come from your knowledge of the brand, tested against its line; a remembered value that contradicts the line is wrong.
- **The brand's accent replaces Apple blue whole:** link, CTA, focus ring, dark-ground link.
- **The surface governs structure; the brand governs look.** Store keeps its cards under any brand; the brand keeps its buttons and type on any surface.
- **Form is borrowed, never the message.** A brand's selling points, marks, illustrations and photographs stay its own.
- **The claim picks the industry, not the category.** Subtraction is Minimalist; a mechanism with a figure, Engineering; craft and heritage, Luxury; a workflow, Developer; a life lived with the object, Consumer; an object sold by photograph and price, Showroom.

| Industry | The input | Brands, one governing |
|---|---|---|
| [Developer](dialects/developer.md) | Software: a platform, tool, workflow, database, canvas or workspace | Vercel, Linear, Supabase, Figma, Notion |
| [Finance](dialects/finance.md) | Money: payments, banking, transfers, consumer finance, exchanges | Stripe, Mercury, Wise, Revolut, Coinbase |
| [Showroom](dialects/showroom.md) | A physical object, range or configurator | Tesla, SpaceX, DJI |
| [AI](dialects/ai.md) | Intelligence: an assistant, model or studio | Claude, xAI, Mistral |
| [Consumer](dialects/consumer.md) | A life: a wearable, sport product, marketplace or home | Oura, Nike, Airbnb |
| [Luxury](dialects/luxury.md) | Craft and heritage: fashion, leather, jewellery, watches, beauty | Burberry, Hermès, Chanel, Louis Vuitton |
| [Minimalist](dialects/minimalist.md) | Subtraction: an everyday product, home object, stationery, audio | Braun, MUJI, Bang & Olufsen |
| [Engineering](dialects/engineering.md) | A mechanism or performance figure | Dyson, Teenage Engineering, Vitsoe |

| Surface or method | The trigger |
|---|---|
| [Keynote](dialects/keynote.md) | A presented deck |
| [Store](dialects/store.md) | A shop or configurator |
| [Editorial](dialects/editorial.md) | A long read or environment story |
| [Bento](dialects/bento.md) | Many features in one glance, on any industry or surface |

The [example collection](examples/) holds one world per brand used; [its README](examples/README.md) lists the pieces.

## Corrections

A model reaches for safety; Apple wins by conviction.

- **Scale is the argument, not the risk.** The largest true thing on the unit is the claim; a model's instinct to shrink, grey and empty is the failure Apple exists to correct.
- **The hero is an object, not an icon.** It has light, material and weight; where the drawing cannot give it that, the frame goes closer or the proof takes its place.
- **A move repeated is a template.** Any tile, block or split that appears on every unit has stopped meaning; the turn comes where the content turns.
- **The ground is chosen, not defaulted.** Apple's grounds, or the brand's; never the warm paper, gradient or blue a model supplies by habit.
- **Every mark is read.** Captions, labels and rules exist for the reader or not at all.
- **Centre the stage, not the text.** Hero, vista and cover headlines may centre; everything read stays flush left.
- **Glass and motion serve controls and change, not mood.** Liquid Glass floats controls over content; motion explains a change and stops; reduced motion gets a still.

## Values

Measured on apple.com, where models are confidently wrong.

- **Blue is four roles:** link on light `#0066cc`, CTA and focus `#0071e3`, link on dark `#2997ff`, native system blue about `#007aff`. A hand's accent replaces all four.
- **Grounds:** white, parchment `#f5f5f7`, near-black tiles, black for photographic void; ink `#1d1d1f`; muted `#6e6e73`, `#86868b`. Colour beyond them comes from the product, one per tile; a headline colours only its core word; gradient text is one sub-line on black; a glow spreads from the product, never across the page.
- **Type:** weights 300 / 400 / 600 / 700, never 500; headlines 600, body 400 at 17 px, 300 only at large sizes; tile hero 56 / 600 / 1.07, a launch hero up to the 80 px class. The system face through `-apple-system, system-ui`, never as a file; Inter stands in for it alone, display tracking a further −0.01 em. A brand's voice takes the nearest open face of its own lineage. The web tightens tracking as size grows; native never hard-codes it.
- **Chinese:** Noto Sans SC off Apple; product names unbroken, no orphaned line-end word, line-end punctuation pulled back about 0.5 em (`text-spacing-trim`), a space between Chinese and Latin (`text-autospace`), dense Chinese at 400 with generous leading.
- **Hairline:** `#d2d2d7` on light; on dark, white at low alpha, never the light value.
- **One shadow,** under the product at rest: `rgba(0,0,0,.22) 3px 5px 30px`.

## Continuous corner

Every nonzero radius, pills and chips included, takes Apple's continuous corner, which no preset draws. Square forms stay square; full-bleed fields have no radius; primary actions and chips are fully rounded; a store card is 18. Radius sets size; the contour is this curve:

```
M 0 1.52866
C 0 1.08849  0 .86841  .07491 .63149
C .16906 .37282  .37282 .16906  .63149 .07491
C .86841 0  1.08849 0  1.52866 0
```

One corner, inward from the corner point, in units of R; the shoulder spends 1.52866R of each side.

- **Build:** natively `RoundedRectangle(style: .continuous)` or `cornerCurve = .continuous`; elsewhere this path, for SVG, canvas, `clip-path` and slide freeforms; Figma at 60% smoothing. `border-radius`, `rect rx`, presets and superellipses are other curves.
- **Fit:** R is at most half the shorter side. A side shorter than 3.05732R shortens its shoulder to half the side, easing toward the native saturated form, whose first cubic runs from (0, 1) through (0, .96) and (0, .82); `examples/_shared/continuous-corner.js` draws it.
- **One path** for fill, stroke, media clip and focus ring; nested corners share centres, inner R = max(0, outer R − gap). A single-file page inlines the helper.

## The red line

A style after apple.com, never Apple's: no Apple logo, product photograph, system font file, or apple.com CSS, buttons or navigation. A badge or bezel comes only from Apple's marketing resources, unaltered.

**Test:** cover the brand name — the page still reads as Apple + that brand, not as Apple alone or as the brand alone. Remove colour — each tile still holds one lead and one claim. Thumbnail the set — the volume changes where the content turns.
