# Apple + Store style — the shop and configurator

**Invocation:** Make work as a shop is made: white utility cards on a hairline grid, chips for choices, a price beside every name, one buy action per card; never a gallery tile forced to sell, never chrome that outshouts the product.

The apple.com store, the product buy pages and the accessories grid. Spoken in Apple, it keeps the single blue and the type ramp, and lets density rise: the field becomes a grid, the tile becomes a card, and comparison becomes the work.

- **Cards, not tiles.** White cards on parchment, a 1 px hairline, an 18 px radius, 24 px of padding; the product image takes the top of the card at a square crop, the name and price sit below it in body size.
- **Chips for choices.** A pill per option, thumbnail plus label plus price difference; the selected chip carries a 2 px focus-blue border and nothing else changes.
- **Comparison is shared scale.** Variants in one row, same crop, same scale, direct labels; the decisive difference alone takes the blue.
- **The buy action stays put.** A frosted sticky bar holds the running price on the left and the buy pill on the right, so the action is never hunted for.

**Hands in this school.** One governs; the others visit as single moves.
- **The configurator hand — the buy page.** Lay out every choice as a chip, every consequence as a price, and let the buyer build the product by choosing, not by reading. Suits configurators, options and bundles. Never: a choice hidden behind a paragraph.
- **The accessories hand — the grid.** One square crop per product, one name, one price, one link; the grid does the selling, the card does not decorate. Suits catalogues and accessory ranges. Never: a card with two products, or a product without a price.
- **The gallery hand — the product pages.** One hero tile above the grid, to remind the buyer what the product is before the choices begin. Suits store landings. Never: a hero that repeats the grid.

**Master edition rules.** Internal padding is never zero inside cards: card text never touches a card edge. On the web a store unit is left text with right image, price row plus total, with card names and prices flush left. A card that repeats a photograph at a new crop declares the reuse; a reused image is a second use, not a second proof.

**Alignment and accent, restated.** Card names and prices stay flush left inside their cards; a centred container is never centred text. When a hand governs, its single accent replaces every Apple blue role for that work. Body, leads, captions, card names and prices are flush left, ragged right, in every surface and format; only a hero, vista or cover headline may centre.

**continuous corner:** A hand may choose square forms; every nonzero radius uses Apple continuous corner. Radius sets size, not contour. Nested corners share their centre and subtract the gap from the outer radius for the inner one. Use the theme's native API or continuous corner path; plain circular rounding and a superellipse are forbidden. Write this construction into the standalone DESIGN.md.

**Apple keeps:** the single blue for links, chips and the buy action, SF Pro Text for names, prices and labels, the parchment ground, the single product shadow on the render inside the card.

**Test:** Cover the prices: the grid still reads as one range of one product family; cover the photographs: name, price and choice still let a buyer decide.

**Caricature:** a discount banner in red; a star rating as decoration; a card with a shadow, a badge and a gradient; a configurator that needs a manual; a price in a larger size than the product name.
