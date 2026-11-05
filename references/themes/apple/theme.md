# Apple style — the gallery marketing language

Apple's public marketing language, as spoken on apple.com, in product launches and in keynote decks: a photography-first gallery in which the product is shown as a sculpture on a solid field, and the interface retreats until it is invisible. The mother tongue is the latest Apple style, not a history of Apple styles: what Apple does now, in the Liquid Glass era, is the school, and earlier Apple looks — skeuomorphism, aqua, early flat — are not dialects of it. Its sources are the apple.com homepage, store and product pages, the product launch keynotes, and the slides practice built from them (an 8-page deck made with live text and separate photographs, not baked images). This is a reading of that public language, not Apple's official guidance: Apple's official system for product interfaces is the Human Interface Guidelines, and this theme does not replace it. It governs marketing and presentation surfaces, so it hosts other kinds of content without becoming a costume. Every dialect inherits this file and replaces only the rules it names.

## Sources and standing

Apple publishes no generic brand handbook for apple.com. What exists officially is two different things, and this theme never confuses them: the Human Interface Guidelines, which govern product interfaces with semantic tokens and no fixed hex values, and the marketing compliance guides, which govern only badges, product images and trademarks for third parties — never colours, sizes or spacing. Everything in this file that looks like a web token — the hex values, the px type ramp, the 18 px card radius — is community measurement of apple.com, not an Apple specification, and must be cited that way in any work that uses it.

Three tiers of evidence, in order of trust. First, official principle: the HIG on hierarchy, semantic colour, materials, motion and accessibility, and the compliance red line in Anti-patterns. Second, measured web values, where at least two independent measurements agree: the VoltAgent apple DESIGN.md (self-labelled alpha, the fullest single file), the display-dev/visualize CSS-bundle trace, and the open-oh-my-design Playwright computed-style check — their intersection is what the Color and Type sections below are built from. Third, single-source or author-defined choices, which this file keeps only where a system needs a decision and labels as its own: the editorial lead at 24 px / 300, the slide calm zone of 25–35%, and any spacing a dialect names without a measured source.

Where the sources disagree, the file follows the measured intersection and says so at the point of use: blue is four roles, not one colour; the hero is 56 px at tile level and larger only for a full-bleed launch hero; web tracking is negative while native tracking follows the system curve. Tile colours change with the product season, so before a work is published, re-check the live apple.com CSS for the tiles it copies. The research behind this section was index-level, dated 2026-11-04, and was followed the same day by a live browser check of apple.com US (homepage, iPhone 18 Pro, MacBook Pro, Apple Watch Series 12): that check confirmed the partial-gradient, product-linked glow and rounding rules below, and corrected the alternation rule — product overview pages stay on one ground rather than alternating per section. Exact CSS gradient stops and radii were not measured in that check, so any radius beyond the ladder below is a visual estimate, not a specification.

A second study the same day, on how other companies copy and vary this language, corrected two more readings in this file. First, Bento is a community label, not an Apple invention: Apple popularised the grid after September 2022, the word comes from the bento box, and a Microsoft Metro first-use claim is still disputed — so the Bento dialect is written as a community name for an Apple surface, never as Apple's own system name. Second, the mother tongue's real chain is hero, then feature chapters, then specifications (first as tiles, then as a full table), then purchase: the long page, the dense footnotes and the comparison table are part of the mother tongue, not exceptions to it. "Colour echo" is likewise a community shorthand, not an Apple-named rule: the measured fact is that colour on the page comes from the product itself, and a headline colours only its core word. What that study contributes to this theme is the lineage of a page form, never the companies' content priorities: their selling points — parameter-first density, reliability narratives, price-led selling, platform stories — are theirs, not rules to copy, and Bento borrows only the grid structure while the subject keeps its own message. Their pages were checked only at index level unless a dialect says otherwise.

## Use

Read it once in full, then choose. Each choice is written into the skeleton; what is not chosen holds as house grammar unless a dialect names it.

| Choose | From | Written into DESIGN.md |
|---|---|---|
| The school: Apple alone, or one dialect | Dialects, by the surface | Overview, the invocation |
| The governing hand | The dialect's hands; with none, the hands below | Overview, Method |
| The field system | Grammar, the roster | Layout, Grid system |
| How groups separate and connect | Tile alternation, or a hairline inside a utility grid | Layout, Shapes |
| A method per reader need | Methods | Forms |
| How images are made | Images, and the hand's materials | Images |
| The breaks, where the content turns | Variations | Variations |
| The test and the caricature | The dialect file; with none, Anti-patterns | Do's and Don'ts |

Going wide means different hands on this subject, not different looks. The test and the caricature also go to the reviewers.

## Dialects

Alone, the mother tongue suits material that shows one thing: a product, a feature, a launch. An industry dialect is a named movement that overturns a few of its rules across the whole work; choose at most one industry dialect, or none. Surface choices and the Bento method are independent axes described below. It is named Apple + <name> style — Apple + Bento style, Apple + Keynote style — so the school and the branch are read in one name, the way Swiss names its dialects. Dialects are other makers' transformations of this school, not Apple's own history: a community designer, a template, or another company takes the mother tongue and changes it — in type, colour, density, imagery or grid — and the dialect names that change, what it keeps from Apple, and who made the turn. A company or community page is cited as the transformer, never as a model to copy wholesale. A work picks one from each axis, not one total — that is why the original four never won as dialects, and where they now belong. Axis one, dialect, by industry: the industry dialect governs, and a brand inside that industry is the governing hand, chosen by the input's sub-type — a deployment takes Vercel, a workflow takes Linear, a payment takes Stripe, a car takes Tesla, a trench takes Burberry, an everyday product takes MUJI, a motor takes Dyson — the way a Swiss dialect picks an artist as its governing hand. Where two dialects could claim one input, the claim decides, not the product category alone: subtraction with no mechanism is Minimalist, a mechanism with a figure is Engineering, craft with heritage is Luxury, a workflow is Developer, a life lived with the object is Consumer. Axis two, surface, by deliverable: Keynote for a presented deck, Store for a shop or configurator, Editorial for a long read. Surfaces are not competing dialects; they combine with any industry dialect, so a developer tool launch deck is Developer plus Keynote, and a finance pricing page is Finance plus Store. Axis three, grid method, by feature count: Bento is not a dialect at all, it is a layout method that visits any dialect or surface for a unit with many features to show in one glance — tiles sized by importance, one claim per tile, specs as small posters. Bento never won as a dialect because its trigger is a layout need, not a subject identity; as a method it is chosen whenever the input has many features, whatever the industry.

When axes conflict, precedence is structure versus look, not dialect versus surface. The surface governs structure — the slide field, the card grid, the centred column, the sequence of units — and the dialect and its brand hand govern look — ground, accent, type voice, button shape, decoration. Where they meet on one element, the hand wins on that element and the surface keeps its structure: a Linear work on a Store surface keeps Store cards and chips, but its buttons stay rectangular, not pill; a Tesla work on a Keynote surface keeps one thesis per slide, but its buttons stay small squares, not pill. Four exceptions found in the full 20-world test are now rules, not workarounds. Keynote's one number applies per slide, not per work: a Finance or AI figure set may take one unit, with figures on a shared baseline, one decisive figure in accent and the rest muted, rather than being forced into successive one-number slides when comparison is the point. Editorial's vista is the dialect's proof field, not necessarily a photograph: where the subject has no photograph — an AI material, a Finance dashboard, a Developer interface — that proof goes full-bleed with one headline and at most one action, and atmosphere still carries the argument. Bento visits Showroom only on range units: a range page may tile many objects, one object and one price per tile, but Bento never visits a single-object hero unit, where Showroom's one photograph per screen governs. Store's card image slot takes the dialect's proof, not necessarily a photograph: an interface, a dashboard, a material card or a photograph, at the same crop and in the same card structure, and where there is no price the card's second line takes a plan, a figure or an action rather than inventing a price. Three rules found in the supplementary 12-world test are now rules, not workarounds. Accent replacement is whole, not partial: when a brand hand governs, its single accent replaces every Apple blue role for that work — link, filled CTA, focus ring, and dark-ground link — and Apple blues retire for that work; a hand accent sitting beside Apple blue is two accents, not a hand. Editorial's vista has three kinds, not two: a photographic vista, a proof-field vista, and a diagram vista — a section, cutaway or technical diagram at full-bleed with one headline and at most one action, where the mechanism itself is the atmosphere; a diagram vista must be readable as a diagram, not a rendered explosion. Bento is an index, not proof: a Bento unit may show many claims at a glance, but a claim that appears only in a Bento tile, nowhere else in the work and with no checkable number, label or figure on the tile itself, is unproven; each tile's claim must be provable in a following unit, or the tile itself must carry its check. A brand dialect file therefore writes the philosophy of the turn, not its values: no hex, no size, no radius and no weight is specified there, and the agent draws values from its own knowledge of the chosen brand, checked against that brand's philosophy; a value that contradicts the philosophy is wrong even if it matches a remembered brand detail. Only a brand whose signature is single and strong earns a hand; a brand whose philosophy cannot be stated without its values is not given one. A dialect governs form only — layout, hierarchy, density — never the subject's message: what another company chooses to sell on is its own, and is not borrowed with the form. Open the one in play before drawing.

Master edition rules, found across dialects and formats in the master works, are now rules, not workarounds. Internal padding is never zero: every text shape carries internal padding of at least 0.3 cm, and a shape whose text touches its box edge is unfinished; a shape carrying no text, such as a hairline rule, needs no inset. Title boxes are taller than their type and clear descenders: a wrapped display title gets a taller box and the body below it moves, and a detail image, card or body line never overlaps title descenders. Number groups sit mid-frame, number, label and context spaced down the unit, never stranded at the top. An image is cropped to its slot and to its subject: a hero source is scaled uniformly and re-cropped if it clips the product, a cover claim sits in a calm light zone and is shortened until it reads over light ground, a product-surface crop shows the screen interior only, and a diagram source is cropped tight to the diagram, never left with wide margins that shrink the mechanism. Image scope follows the slot: a slot too narrow for a system shows part of the system on the cover and the whole system on the proof unit, and a portrait crop of a landscape source reads as a detail, never as a complete source — the complete source belongs on a proof unit. A placeholder is not proof: an abstract placeholder-bar interface, a reused image at a new crop presented as a second proof, or a diagram that cannot be read as a diagram proves nothing; reuse is declared, and proof must be readable. Where tabular setting is unavailable, it is never claimed from the file: figures align in a right-aligned column so decimals line up, as the fallback. Fonts are named, never embedded, so spacing is buffered against substitution shifting line breaks, and a figure that overflows in one renderer is checked in the other renderer as well. Cover structures vary across a set: repeating one cover structure, right-half hero after right-half hero, is a weakness, not a system. These rules hold in every format — deck, flyer, website, and world — and a format that cannot hold one of them is reworked, not exempted.

| Industry dialect | The input | Brands as hands, one governing per work |
|---|---|---|
| [Apple + Developer style](dialects/developer.md) | Software: a platform, tool, workflow, database, canvas or workspace | Vercel, Linear, Supabase, Figma, Notion |
| [Apple + Finance style](dialects/finance.md) | Money: payments, banking, transfers, consumer finance, exchanges | Stripe, Mercury, Wise, Revolut, Coinbase |
| [Apple + Showroom style](dialects/showroom.md) | A physical object, range or configurator | Tesla, SpaceX, DJI |
| [Apple + AI style](dialects/ai.md) | Intelligence: an assistant, model or studio | Claude, xAI, Mistral |
| [Apple + Consumer style](dialects/consumer.md) | A life: a wearable, sport product, marketplace or home | Oura, Nike, Airbnb |
| [Apple + Luxury style](dialects/luxury.md) | Craft and heritage: fashion, leather, jewellery, a watch, premium beauty | Burberry, Hermès, Chanel, Louis Vuitton; Tiffany, Cartier, Rolex, Dior as visitors |
| [Apple + Minimalist style](dialects/minimalist.md) | Subtraction: an everyday product, home object, stationery, audio | Braun, MUJI, Bang & Olufsen; Aesop as visitor |
| [Apple + Engineering style](dialects/engineering.md) | A mechanism or performance figure: airflow, a motor, a kit, a modular system | Dyson, Teenage Engineering, Vitsoe; Braun as visitor |

| Surface, picked alongside the dialect | The deliverable | What it governs |
|---|---|---|
| [Apple + Keynote style](dialects/keynote.md) | A presented deck | One thesis per slide; live text over a calm zone, never baked into the image; the tile becomes one slide |
| [Apple + Store style](dialects/store.md) | A shop or configurator | Utility cards on a hairline grid; chips, prices and comparison; density rises, the gallery rhythm stays |
| [Apple + Editorial style](dialects/editorial.md) | A long read or environment story | Light weights and long leads; photographic atmosphere carries the argument; the tile opens into a vista |

| Grid method, visiting any dialect or surface | The trigger | What it governs |
|---|---|---|
| [Apple + Bento style](dialects/bento.md) | Many features to show in one glance | Tiles sized by importance, one claim per tile; specs as small posters, never table rows; the homepage grid rhythm |

## Examples

Each example is one world with its own DESIGN.md, so a maker can build another piece of the same world from that file alone. An industry dialect writes philosophy; surface and method files may specify construction values. The example merges those choices and carries concrete Tokens YAML, including checked text/ground pairs and the continuous corner contour. Example values are authored for fictional worlds, not measured specifications of the named brand. Examples live under `references/themes/apple/examples/` and are included in the repository's skeleton release checks. No Apple product, brand product, photograph, logo or font file is used in any example.

| Example | Dialect and hand | Subject |
|---|---|---|
| [Mother tongue](examples/mother-tongue/DESIGN.md) | Apple alone | Lumen, a small home speaker |
| [Developer](examples/developer/DESIGN.md) | Developer, Vercel hand | Relay, a deployment platform |
| [Finance](examples/finance/DESIGN.md) | Finance, Stripe hand | Ledger, a payments product for small shops |
| [Showroom](examples/showroom/DESIGN.md) | Showroom, Tesla hand | Volt, a small electric car |
| [AI](examples/ai/DESIGN.md) | AI, Claude hand | Fern, a writing assistant |
| [Consumer](examples/consumer/DESIGN.md) | Consumer, Oura hand | Pebble, a wellness ring |
| [Luxury, Hermès hand](examples/luxury/DESIGN.md) | Luxury | Atelier, a leather house |
| [Luxury, Burberry hand](examples/luxury-burberry/DESIGN.md) | Luxury | Highland, a British outerwear house |
| [Luxury, Chanel hand](examples/luxury-chanel/DESIGN.md) | Luxury | Noir, a timeless fashion house |
| [Luxury, Louis Vuitton hand](examples/luxury-louis-vuitton/DESIGN.md) | Luxury | Voyager, a flagship leather house |
| [Minimalist, Braun hand](examples/minimalist/DESIGN.md) | Minimalist | Mono, a small radio |
| [Minimalist, MUJI hand](examples/minimalist-muji/DESIGN.md) | Minimalist | Plain, everyday products |
| [Minimalist, Bang & Olufsen hand](examples/minimalist-bang-olufsen/DESIGN.md) | Minimalist | Sound, minimal audio |
| [Engineering, Dyson hand](examples/engineering/DESIGN.md) | Engineering | Aero, an airflow fan |
| [Engineering, Teenage Engineering hand](examples/engineering-teenage-engineering/DESIGN.md) | Engineering | Kit, a small instrument |
| [Engineering, Vitsoe hand](examples/engineering-vitsoe/DESIGN.md) | Engineering | Shelf, a modular shelving system |

Each example shows all three surfaces — Keynote slide, Store card, Editorial opener — as Forms, and Bento grid as a Variation, so the surface and grid axes are described inside every world rather than requiring a separate example per combination. The earlier master-edition audit and the scope of later schema and continuous corner checks are recorded in [AUDIT.md](AUDIT.md).

## Hands of the mother tongue

With no dialect, one governs and the others visit as single moves; with a dialect, its hands govern and these only visit. Each is a way of working, not a look.

- **The apple.com gallery — the product pages and homepage.** Photograph the subject as a sculpture on a solid field before anything is written. Stack one product per tile, alternate the field light and dark, and let the colour change be the only divider. Set one headline, one line of tagline, and at most two small actions per tile. Suits launches, products and features. Never: a tile that carries two products, or chrome that competes with the photograph.
- **Jony Ive — the industrial design studio.** Reduce the subject to its material and its silhouette. Remove everything that does not change how the object is held, seen or used, and let the remaining form carry the meaning. Suits objects, hardware and anything with a physical form. Never: a decorative detail that explains nothing about the object.
- **The keynote presenter — the launch stage.** Reveal one idea at a time, at the largest size the room allows. One slide, one sentence, one image; the next slide is a new scene, not a continuation. Suits presentations, pitches and announcements. Never: a slide the audience must read while the speaker talks.

## Grammar

- **The tile comes before placement.** A unit is one full field, edge to edge, in one ground; tiles stack with no gap, and the change of ground is the divider. On the homepage that change alternates light and dark across tiles; on a product overview page the sequence may stay on one ground — black — from hero to comparison, and forcing an alternation per section breaks it. Alternation is a homepage rhythm, not a rule for every surface.
- **One field system per work, chosen by name.** The tile system chosen silently is a default, not a decision.
  - *Gallery*: one product per tile, centred stack, full-bleed field. For launches and heroes.
  - *Utility grid*: white cards on a hairline grid, three to five across. For shops, accessories and comparison.
  - *Editorial column*: one centred column, about 980 px on the web, for long reading. For stories and reports.
  - *Slide field*: 16:9, one thesis per slide, critical content inside the central 80%, nothing critical in the outer 8%. For decks.
- **The stack centres.** Tiles and headlines centre; body copy on a slide or a page stays left-aligned. Centring a body paragraph needs a reason.
- **A centred container is not centred text.** A centred column, a centred stack and a centred axis describe where the container sits, never how text aligns inside it. Headlines on a hero, a vista or a Keynote cover may centre; body, leads, captions, card names and prices stay flush left, ragged right, in every surface — Keynote body slides, Store cards, and Editorial columns alike. A centred body paragraph, a centred Store card, and a centred Editorial lead are the same error, and the anti-patterns list names it for that reason. Where a surface needs a different alignment, the surface file must name it; a builder's template never supplies one by default.
- **Fields, not boxes.** Group by a change of ground; inside a light or dark field, no floating cards, shadows or plates, except the utility grid, where cards carry a hairline and an 18 px radius.
- **A field resets every foreground.** Each ground carries a complete palette: ink, muted, link and action, all checked against that ground alone.
- **One module, few axes.** One centred axis per tile; base unit 8 px, structural layout snapping to 8 / 12 / 16 / 20 / 24 px; 80 px of air inside a tile on the web, 64 px above a headline and 48–64 px below it; the nearest content to a product image is at least 40 px away. Gaps are measured between visible ink or image edges, never between text-box edges: headline, tagline and actions form one reading group, and the product stands apart from it. Containers: reading text about 980 px, a product grid about 1440 px, a tile full-bleed; a utility card carries 24 px of padding, a button 8–11 px vertically by 15–22 px horizontally.
- **Two densities, one grammar.** The marketing face is one tile, one idea, at the air above. The store, support and footer faces are a second, denser tool mode — tighter spacing, more controls, more cards in a row — and they do not break the grammar, they use it harder; the Store dialect governs them. Never flatten the two into one density, and never quote a percentage of white space as an Apple rule: the 53% figure found in one author's checklist is invented, not measured.
- **Radius is a ladder; continuous corner is the contour.** Full-bleed fields 0, small elements 5 px, tool buttons 8 px, medium elements 11 px, store cards 18 px, primary actions and choice chips fully rounded up to the available half-height. These values select size, never a circular arc. Every nonzero radius uses continuous corner as specified below. A radius outside this ladder needs a reason, and a card radius quoted as a 12–18 px range is a secondary generalisation, not a measured value. Homepage promo tiles are sharp and full-bleed, separated by a white gutter; product-page gallery and feature cards are larger continuous corner containers, whose size is a visual estimate rather than a measured CSS value. The mother tongue's primary actions are fully rounded; a governing hand may keep square controls. A square remains square; every rounded control retains continuous corner.
- **Recompose before shrinking.** A long title is recomposed within the hierarchy, never shrunk below its declared role to preserve empty space; a slide that cannot hold its thesis at its size is two slides, not a smaller title.
- **Furniture earns its place by function.** A near-black nav bar locates, a frosted sub-nav names the product and holds the buy action, a caption ties evidence to source, a price states a consequential quantity. The nav bar is 44 px high with quiet 12 px links; the sub-nav is 52 px high, parchment at 80% with backdrop blur.

### continuous corner

Use one contour term: **continuous corner**. This rule governs rounded cards, controls, media clips and nested containers; it does not round a shape whose declared radius is zero. Radius and contour are separate decisions. Carry the contour, radius and inset relationship into each standalone DESIGN.md's Shapes and Tokens, so a maker without this theme can reproduce them.

Copy this line into a visual brief:

> 圆角用 Apple continuous corner：直边处曲率为 0、到角中最大，肩部在约 1.53R 内完成（路径为拟合，非解析 G2；Figma corner smoothing 60%）；嵌套同心，内半径 = max(0, 外半径 − 间距)；禁用普通 circular border-radius，禁用超椭圆 squircle。

The contour is geometry, not an API. In units of R, measured inward from the corner, one corner is two endpoints and three cubic segments:

```
A  (0, 1)
C  (0, .96) (0, .82) (.07491, .63149)
C  (.16906, .37282) (.37282, .16906) (.63149, .07491)
C  (.86841, 0) (1.08849, 0) (1.52866, 0)
B  (1.52866, 0)
```

A is where the straight edge ends and B is where the next one begins, so the shoulder consumes 1.52866R of each side and the flat remaining on a side of length w is w − 2 × 1.52866R. Reach for this path, not for the nearest preset:

| Target | Build it as |
|---|---|
| Native Apple | `RoundedRectangle(cornerRadius: R, style: .continuous)`; on a layer, `cornerRadius` with `cornerCurve = .continuous` |
| SVG, canvas, HTML | this path, drawn once and reused for fill, stroke and `clip-path` |
| Slide deck or PPTX | a freeform shape from the same path; a rounded-rectangle preset is a circular arc |
| Figma | radius R with corner smoothing 60% |

Fit the radius before drawing: R = min(R, h/2, w/(2 × 1.52866)); if that reaches zero the shape is square. Fill, border and media clip share the one path — a container whose fill is continuous and whose image is a circular crop is two contours, not one. Plain CSS `border-radius`, SVG `rect rx`, a rounded-rectangle preset, `corner-shape: squircle` and a mathematical superellipse are not substitutes: the first three are circular arcs, the last two another curve family. At large R or on a narrow shape, fit the contour and inspect the delivered edge.

- **Nested corners:** align the centres and use inner radius = outer radius − gap. If the gap reaches the outer radius, the inner corner is square; never use a negative radius or reuse the outer radius on the inner shape. Check the visible gap through the shoulder, not only along the straight edge. An inset panel that shares no corner centre is its own shape, not a nested corner.

The construction and the 1.52866R extent are this project's supplied implementation brief, not an Apple-published formula; Figma's 60% smoothing is a design approximation of the same intent, not a guarantee of identical native geometry. Apple documents the native style as continuous curvature, so prefer the platform implementation where the delivery format has one.

The three-cubic path above is a fit of the native contour, not an analytic G2 spline. `exports/apple-continuous-corner/` measured it at 99.80% mask intersection against native rendering, and `scripts/corner-check.py` shows what that means: the two joins where a straight edge meets a shoulder carry no curvature step, while the two joins inside the shoulder are C0 within about 2.5° of tangent. At control, card and tile sizes that is invisible; at poster scale, inspect the shoulder enlarged. State the intent as continuous curvature in a deliverable, never as proven G2 — and never swap a circular arc in to "clean up" the internal join.

Sources: [SwiftUI continuous](https://developer.apple.com/documentation/swiftui/roundedcornerstyle/continuous), [CALayer cornerCurve](https://developer.apple.com/documentation/quartzcore/calayer/cornercurve), [Figma corner smoothing](https://help.figma.com/hc/en-us/articles/360050986854-Adjust-corner-radius-and-smoothing).

## Type

SF Pro is Apple's proprietary face, on Apple devices by the system stack. Off Apple devices, Inter is the substitute: tighten tracking by a further 0.01 em at display sizes and tighten body leading from 1.47 to 1.44, because Inter runs wider and taller than SF Pro. Never claim SF Pro is installed where it is not, and never host SF Pro font files as a web font: on the web the stack is `-apple-system, system-ui`, and the licence for SF Pro covers Apple-platform interface mockups, not web distribution.

- **Display has one lineage, two optical sizes.** SF Pro Display at 20 px and above, SF Pro Text below; the boundary is unbreakable, because the faces are engineered for those sizes. On native surfaces the same split is 20 pt and above versus below, and the HIG's native steps are the reference there, not the web px values: iOS body 17 pt, large title 34 pt, macOS body 13 pt — the two platforms' bodies are not interchangeable.
- **The weight ladder is 300 / 400 / 600 / 700, and 500 is deliberately absent.** Marketing headlines sit at 600; 700 is an emphasis state, not a default and not a ban — a checker that fails any weight of 700 or above is stricter than Apple itself. Body is always 400, strong inline 600; 300 appears only at large sizes, as an airy cue.
- **The ramp, measured on the web.** Hero 56 px at 600, leading 1.07, tracking −0.28 px; tile headline 40 px at 600, leading 1.10; lead 28 px at 400, leading 1.14; tagline 21 px at 600, leading 1.19; body 17 px at 400, leading 1.47, tracking −0.374 px; body-strong 17 px at 600, leading 1.24; captions 14 px, tracking −0.224 px; fine print 12 px, tracking −0.12 px; a large button 18 px at the rare weight 300; a dense footer link 17 px at leading 2.41, which is a footer exception, never a global leading. Body is 17 px, not 16 px: the extra pixel sets the reading pace.
- **The hero has two sizes, and the file says which.** 56 px is the tile-level hero, confirmed by two independent measurements. A full-bleed launch hero may go to the 80 px class, but that value comes from other pages and breakpoints, and there is no single hero size across the whole site — a work that quotes one hero size for every page will be wrong on half of them.
- **Tracking splits by surface.** On the web, tracking tightens as size grows, as the ramp above shows. On native surfaces, do not hard-code tracking at all: the system curve is tightest at 17–20 pt (−0.43 / −0.45) and returns positive at 28 pt (+0.38) and 34 pt (+0.40), back to 0 at 80 pt and above. Copying the web's negative tracking into an app is a migration error, in either direction.
- **Chinese type is measured, not matched.** The Chinese web stack, read from apple.com.cn source, is `SF Pro SC, SF Pro Display, SF Pro Icons, PingFang SC, Helvetica Neue, Helvetica, Arial, sans-serif`. SF Pro SC is an unpublished Chinese customisation — its han glyphs run smaller than PingFang SC and its full-width punctuation runs at 0.5–0.6 of character width, tuned for mixed Chinese and Latin setting. Four hard rules follow, all source-verified: keep a product name unbroken with a non-breaking space; protect end-of-line words from orphaning with `nowrap`; control line breaks explicitly by breakpoint, in the manner of a small-screen-only break; and correct end-of-line punctuation visually, by about 0.5 em, so it sits centred rather than hanging. Mixed Chinese and Latin takes a space between the two scripts. Latin and Chinese share the ramp by weight and leading, never by forcing their letterforms to match.
- **Chinese density is set by purpose, not by one body style.** Chinese carries more information per character than Latin, so dense Chinese body copy needs more air, not less: information-dense Chinese stays at weight 400 with generous leading and paragraph spacing doing the separation, while the airy weight 300 is reserved for large atmospheric lines and never for dense body copy. Weight and leading together are the density control — a dense Chinese paragraph set tight and light is unreadable, however correct its size.

## Color

- **Roles:** ground, ink, muted, link, action, dark (a change of register), signal (never a second hue). Colour is assigned by role, never by a single variable: a file that defines one `--apple-blue` has already made the classic error.
- **One accent, four blues, each with a job.** Links on a light ground #0066cc; filled CTAs and the focus ring #0071e3; links on a dark ground #2997ff; and, on native surfaces only, the system blue, measured around #007aff and varying by system version. Writing #0071e3 as "the brand colour" collapses the CTA into the link and is wrong; the focus colour and the link colour are different tokens from different stylesheets, and the dark-ground link is a third.
- **The ground covers almost everything; the accent is a pill, a link, a focus ring.** A full accent field is a variation, and a blue background with white text is not a field.
- **The accent comes from the system, and the colour comes from the product.** The system blues above are the only action colours. Everything else bright on the page is drawn from the product itself, never invented for the layout: a tile may carry one colour taken from its own product or photograph, and a product line's own colour — Apple Music's red, for one — is that product's, never the system's. The earlier black-white-grey-only reading of Apple is out of date: current product pages are bright with product colour, and the discipline is in how little of it is used, not in its absence.
- **A headline colours only its core word, never the whole headline.** Where a headline takes colour, it takes it on the word that names the technology or the feeling, and the rest stays ink or white; a fully coloured headline, and a rainbow headline, are both decoration. Colour in a headline echoes the product — the screen, the case, the sensor — and a colour with no product behind it is a mistake.
- **Gradient text is partial, on dark, and rare.** The live form is a technology sub-line in gradient on a black ground while the main headline above it stays solid white — homepage MacBook Pro's PROLED XDR Display line, gold through pale to blue, is the observed case — and the same line on the product page itself runs solid white. Gradient is a homepage-tile treatment for one sub-line, not a headline system: a page that gradients every headline has misunderstood the exception.
- **Diffusion is a product glow, never a background wash.** Soft colour diffusion on current Apple pages is always tied to the product: the green glow spreading from a Watch sensor, a translucent orb carrying a rippling multi-colour wave for Siri, a spectrum fan behind a watch silhouette, a small neon glow at a phone's buttons. There are no pastel orbs and no full-page pastel washes as page backgrounds; grounds stay solid black or parchment, and a diffuse blob with no product behind it is decoration, not Apple.
- **A light accent never inks the ground.** Blue on parchment stays a link or a pill, never a wash.
- **Grounds, by surface, not by one dark.** White #ffffff, parchment #f5f5f7, pearl #fafafc for secondary buttons; near-black product tiles #272729, #2a2a2c and #252527 in micro-steps; pure black #000000 for video and photograph void; the global nav in near-black, measured #161617 in one CSS trace and rendered black in another, so the nav is specified as near-black, not as a single hex to defend. Ink #1d1d1f does double duty: it is the text colour on light grounds, and, on a dark buy strip, the ground itself.
- **Muted greys, from the same trace.** Secondary text #6e6e73, tertiary and footnote text #86868b; both come from the same stylesheet and agree across two sources. An older sampling's #7a7a7a is a different page or period, and is not preferred where the two agree.
- **Hairlines and chips, measured.** A store card's hairline is 1 px; the divider tone is #f0f0f0, the hairline tone #e0e0e0, and a choice chip's neutral tone #d2d2d7, used at about 64% alpha.

## Images

- **A photograph serves the subject, not a mood.** The product as sculpture: on a solid field, full-bleed or in a panel, at the highest resolution available, its silhouette intact.
- **One shadow, and only on the product.** `rgba(0, 0, 0, 0.22) 3px 5px 30px` under a product render resting on a surface. Never on cards, buttons or text; elevation elsewhere comes from a change of ground or a frosted bar.
- **Crop preserves the silhouette.** A product is scaled, never cropped to fit; a lifestyle image may crop, and then only inside a container rounded on the system ladder, normally the 18 px card step. A container radius quoted as a range is not a measured value.
- **Icons are out of scope.** This theme does not design icons: no custom icon is drawn here, and no icon rule is given. A work that needs an icon takes it from its own source, unchanged; it does not invent one in this style.
- **On slides, the image stays an asset, not a page.** One dominant subject, one support layer, one background atmosphere; 25–35% of the frame stays calmer than the hero area so live text has a zone; titles, notes and body copy are never baked into the image. A full-page picture with baked text is not an Apple slide, it is a poster of one.
- **A hero product dominates, and its field matches its ground.** On a cover or hero slide the product stands at least half the frame tall — a thumbnail in the middle of an empty slide is not minimal, it is unfinished. A photograph's own field must match the slide's ground, or the photograph must go full-bleed; a light-grey photo rectangle floating on a white slide, or a white rectangle on a dark slide, breaks the field rule and reads as a pasted box, however correct its colours are.
- **Drawing is native when it explains:** flat, one line weight, on the field; a diagram keeps few node types and deliberate connectors.

## Motion and material

Motion explains information; it never decorates, and it never runs on every element at once. A claim that every visible element must animate directly contradicts the official principle, and this file rejects it.

- **Motion starts where the user is.** An animation begins from the element's current on-screen value, inherits the user's gesture velocity, and can be interrupted and reversed at any point; a hard cut between states is a failure, not a simplification. The spring language for this comes from the 2018 fluid-interfaces talk, as transcribed by the community: damping near critical (about 1.0, no overshoot) and a response time around 0.4 s are the transcribed values, not HIG text, and are cited as such.
- **Duration is a range, not a rule.** A commonly quoted 300–800 ms window for interface motion is a summary, not an official value; use it as a sanity range and never as a specification.
- **Glass is a functional layer, not a look.** Liquid Glass belongs only where a control floats over content — navigation, tab bars, toolbars, floating controls — in its regular form by default, and in its clear form only over rich media, where bright content takes a dark scrim of about a third. Content layers — lists, cards, media containers — take a standard material or a solid ground. Glass has no colour of its own; its colour comes from what sits behind it, and tint is reserved for a single primary action. Transparency tiers quoted as 40–95% are community transcriptions, not HIG numbers.
- **The marketing exception is scroll, not animation.** A product page's scroll narrative — a sticky field, a pre-rendered image sequence stepped by scroll position, interpolated transforms — is driven by the reader's scroll, and it is the one place where motion is continuous. It is not a licence for ambient animation elsewhere.
- **Reduced motion is a real surface.** Where a user asks for reduced motion, displacement, scale and parallax become a fade or a static state, and a scroll narrative gets a static alternative. A work with no reduced-motion state is unfinished.

## Methods

Cite a cell by name with its method: the work, the move as an imperative, its parameters, one ban.

| The reader must | Text | Image | Data | Space and frame |
|---|---|---|---|---|
| Find the lead | **Tight headline**; one claim at 600, tracking tightened | **Hero product** on a solid field, at gallery scale | **One number alone** on a quiet field | **Tile pulse**: a change of ground marks the new lead |
| See the groups | **One tile, one product**; tagline, then at most two actions | **Tile alternation**: light, dark, light | **Utility grid**: shared card, shared hairline | **Field change**, never a border, between groups |
| Follow the order | **Tile sequence**: light hero, dark tile, light utility, dark tile, parchment close | **Reveal**: one scene per slide, in scene order | **Comparison strip**: variants in one row, shared scale | **Slide field**: one thesis per slide, in thesis order |
| Compare | **Split tile**: parchment against near-black, one signal in blue | **Comparison strip**: same crop, same scale, direct labels | **Shared baseline**; blue only for the decisive signal | **Two fields side by side**, one ground each |
| Tell figure from ground | **Figure–ground** by value: ink on parchment, white on near-black | **Silhouette** against a solid field | **Reference band** in the field's muted tone | **Knockout**: white type on a dark field, never outlined |
| Know where they are | **Nav bar**: 44 px near-black, quiet 12 px links | **Caption** under the photograph | **Price** beside the name, in body size | **Frosted sub-nav**: product name left, buy action right |
| Feel the change | **Field turn**: the ground changes, the type does not | **Vista**: a photographic field replaces the product | **Scale jump**: one number at display size | **Dark turn**: a near-black tile resets the sequence |
| Feel the edge | **Full bleed**: the field meets the trim | **Bleed photograph**: the image meets the trim | **Data-ink**: no gridline that carries no value | **Trim-connected panel**: the image touches one edge |

- **Cells combine; they do not compete.** Reference units stay quiet.
- **A series is generated, not decorated unit by unit.** The same tile, the same accent hierarchy and the same type ramp repeat across cover, divider, body and close.

## Variations

A variation breaks the grammar on one unit, where the content turns. Each is stated with its magnitude and its keep condition. One break per unit; reading text is never the experiment; a variation repairs nothing.

**Breaking the tile**

| Variation | What it does | Keep | Lineage |
|---|---|---|---|
| Dark turn | One whole unit on a near-black field | Complete foreground roles on that ground | The homepage dark tile |
| Vista turn | A photographic field replaces the product field | One headline, one action, no competing detail | The environment page |
| Utility turn | Tiles become hairline cards in a grid | One card system per unit; no shadows | The store and accessories grid |
| Pill turn | One action becomes a full pill in action blue | One pill per unit as the primary action | The Learn more / Buy pair |

**Breaking the centred stack**

| Variation | What it does | Keep | Lineage |
|---|---|---|---|
| Left-anchored slide | Title and body flush left, image right | One thesis; the calm zone stays on the text side | Keynote body slides |
| Split comparison | Two fields side by side, parchment against near-black | One signal in blue; both sides share a scale | The comparison strip |
| Oversized numeral | One number at display size, label beneath | The number is the claim, not decoration | Keynote data slides |

**Breaking the quiet field**

| Variation | What it does | Keep | Lineage |
|---|---|---|---|
| Product shadow | The single system shadow under a render | Only on the product, never on chrome | Product photography |
| Frosted bar | A translucent bar with backdrop blur over content | Only for nav and sticky buy actions | The sub-nav and sticky bar |
| Light-weight lead | Body at weight 300 at 24 px and above | Large sizes only; reading text stays at 400 | The environment lead |

## Anti-patterns

House preferences; a brief, a brand or a dialect may override them.

- **The caricature:** frosted glass everywhere; a gradient wallpaper; blue on everything; a pill button for every sentence; a stock photograph as hero; text baked into an image.
- A centred body paragraph; a logo wall; three equal cards with equal claims.
- KPI tiles with no lead and no label; numbers on unordered content; a giant word with no claim. A number tile with a lead and a label is not this error — Bento uses one.
- Two whole dialects on one unit.
- Gradient wallpapers and full-page pastel washes, glass panels, fake grain, fake 3D, gold or glowing outlines. A partial gradient sub-line on black and a product-linked glow are allowed; a gradient as the page itself is not.
- A second accent colour; a blue background used as a field; link blue on a dark ground, or sky blue on a light one.
- Borders on tiles; rounded corners on full-bleed fields; shadows on cards, buttons or text.
- Circular rounding or a mathematical superellipse used in place of continuous corner; identical inner and outer radii on nested containers; fill, border and image clip using different contours.
- Weight 500 anywhere; body at 16 px; headlines at 700 by default.
- **The measurement errors this file exists to prevent:** one `--apple-blue` for link, CTA and focus; a single hero size quoted for every page; web tracking copied into a native app, or native tracking hard-coded at all; a 53% white-space figure or a 12–18 px card-radius range presented as Apple values; a ban on weight 700 presented as Apple's rule; motion on every element; white space treated as a score, so a thin page passes and a dense store page fails.
- **The compliance red line.** This theme is a style reproduction inspired by apple.com, never an Apple specification. A work made from it must not use the Apple logo, Apple's product photographs, SF Pro font files, or apple.com's CSS, buttons or navigation elements as supplied. A badge or a product bezel, where one is genuinely needed, comes only from Apple's official marketing resources, used exactly as supplied — a badge no smaller than 40 px on screen with a quarter of its height as clear space, one per layout and subordinate to the maker's own mark; a product image no smaller than 200 px on screen, never cropped, covered or given a reflection or shadow.
- **The accessibility floor.** Body text at 4.5:1 against its ground, large text and meaningful graphics at 3:1; touch targets at least 44 by 44 points on native surfaces, 44 px on the web; information never carried by colour alone; a reduced-motion state, as in Motion and material. On native surfaces, Dynamic Type is the system's job — body text scales up to about three times its base size — and a design that breaks at large text sizes is unfinished.

**Test:** with colour removed, the tile rhythm still reads and each tile still holds one product and one claim; with the photograph removed, the headline alone still states one claim.

**Corner check:** inspect the rendered contour at delivery size and enlarged: the straight edge must enter the shoulder without a curvature jump; nested gaps must remain visually even through the turn. Confirm `.continuous` in native source, or inspect the exported continuous corner path and its clip in other formats. A correct radius number alone does not establish the contour. On a delivered path, `scripts/corner-check.py` measures it: curvature at every segment junction, so a step is a number rather than an impression.
