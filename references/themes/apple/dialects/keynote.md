# Apple + Keynote style — the presented deck

**Invocation:** Make work as a launch deck is made: one thesis per slide, live text over a calm zone, one dominant image per slide; never a tile shrunk onto a slide, never text baked into a picture.

The launch keynotes, from the stage reveal to the feature walkthrough. Spoken in Apple, it keeps the tile rhythm and the single blue, and lets the slide field replace the web tile: a tile becomes one slide, a sequence of tiles becomes a sequence of scenes.

- **One thesis, one slide.** The title states the slide's claim in one sentence; the body proves it or shows it, and nothing else on the slide competes with it.
- **Text stays live.** Titles, notes and body copy are editable text over the image, never rendered into it. The image keeps 25–35% of its frame calmer than the hero area, and critical content stays inside the central 80%, clear of the outer 8%.
- **One dominant subject per slide.** A cover, a divider, a concept visual, a comparison plate, a data backdrop, a workflow plate or a closing poster; a slide that needs two heroes is two slides.
- **Builds order attention, nothing else.** A build reveals the lead, then the support, then the action; a transition is a cut, except a field turn, which is a change of ground. Motion on a slide explains the reveal and then stops: no element animates for its own sake, no transition is applied to every slide by default, and a reduced-motion version of the deck is a static sequence of the same slides, not a different deck.
- **Sizes follow the slides surface.** Title at the slide-title step, body at the body step, nothing below the surface floor; distance sets size, and size sets the word count, so a slide is reflowed before copy is cut or a slide is added. On a 13.33 by 7.5 in slide those steps are: cover title 72 pt at 600, leading 1.05; body-slide title 54 pt at 600, leading 1.10; body 20 pt at 400, leading 1.47; caption 14 pt at 400; fine print 12 pt at 400; a display number at 90 pt or above at 600, label beneath. These are the dialect's translation of the web ramp for projection distance — the title class from the tile headline, the body class from the web body, enlarged — not apple.com px values copied onto a slide, and they are a floor: a slide that cannot hold its thesis at these steps is two slides, not smaller type. The first test of this dialect proved the point: a 44 pt title on a 13.33 in slide read as a default document heading, not a launch title, and the steps were raised after that render.

**Hands in this school.** One governs; the others visit as single moves.
- **The keynote presenter — the launch stage.** Reveal one idea at a time, at the largest size the room allows; the next slide is a new scene, not a continuation. Suits presentations, pitches and announcements. Never: a slide the audience must read while the speaker talks.
- **The gallery hand — the product pages.** Photograph the subject as a sculpture on a solid field, then place the live title in the calm zone the photograph leaves. Suits covers, dividers and exhibit slides. Never: a photograph crowded by overlay copy.
- **The data hand — the keynote numbers slide.** One number at display size, its label beneath, its context in one quiet line. Suits data and proof slides. Never: a chart that needs a legend to be read.

**Master edition rules.** Internal padding is never zero: text never touches its box edge, and title boxes are taller than their type with clearance for descenders, because a wrapped display title must get a taller box and the body below it must move. Number groups sit mid-frame, spaced down the slide, never stranded at the top. Cover structures vary across a set: repeating one cover structure is a weakness, not a system. Fonts are named, never embedded, so spacing is buffered against substitution shifting line breaks, and a figure that overflows in one renderer is checked in the other renderer as well.

**Alignment and accent, restated.** A centred container is never centred text: body copy on a slide stays flush left, ragged right, and only a cover title may centre. When a hand governs, its single accent replaces every Apple blue role for that work. Body, leads, captions, card names and prices are flush left, ragged right, in every surface and format; only a hero, vista or cover headline may centre.

**continuous corner:** A hand may choose square forms; every nonzero radius uses Apple continuous corner. Radius sets size, not contour. Nested corners share their centre and subtract the gap from the outer radius for the inner one. Use the theme's native API or continuous corner path; plain circular rounding and a superellipse are forbidden. Write this construction into the standalone DESIGN.md.

**Apple keeps:** the tile rhythm as a slide sequence, the single blue for links and actions, SF Pro Display for titles and SF Pro Text for body, the single product shadow, the parchment and near-black fields.

**Test:** Project the deck: every slide reads from the back of the room in one glance, and removing the image leaves a title that still states one claim.

**Caricature:** a webpage screenshot on a slide; text baked into a full-page picture; bullet walls; a transition on every slide; a chart with a legend, a grid and a gradient.
