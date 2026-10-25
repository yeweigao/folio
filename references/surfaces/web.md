# web

A web page is read, scrolled, clicked, used by keyboard, and loaded on a slow phone. It is not a tall poster.

## Grid

- Content = min(1440, viewport − 2 × max(24 px, 5vw)); 12 columns, 24 gutters. At a 1440 viewport, content 1296 (columns 86); from 1600 up, content caps at 1440 (columns 98).
- Collapse columns as the content requires, for example 12 → 8 → 6 → 4 around 1024 / 768 / 480; support reflow down to 320 CSS px.
- Text 16–20 px, leading 1.5–1.7, measure ≤ 65ch (CJK 25–35). H1 up to 80 px; a display word or number up to 112 px, treated as a graphic.
- Tokens: paper, ink, accent, muted, line, focus. The theme sets radius and depth; in the Swiss theme, radius 0 (true circles stay circles) and no shadows, with depth from 1 px lines, fields, and space.

## Where web pages go generic

| The template move | Instead |
|---|---|
| Small colored eyebrow, centered headline, subline, gradient button, three feature cards, logo wall | A flush-left headline that states what this is, one supporting sentence, one action; the first screen shows the real product, a real number, or something to use |
| Every section: icon, title, two lines, repeated in threes | Sections follow the content's tasks; repeat a structure when it helps comparison or navigation |
| Testimonials and "trusted by" invented to fill space | Only real quotes and logos with permission; otherwise leave the section out |
| Fade-up on every element as it scrolls in | Content visible by default; one orchestrated moment at most |
| Purple-to-blue gradient, glass panels, glow | Paper, ink, one accent; texture from real images |
| "Learn more" buttons | A verb and an object: "Book a visit", "Download the report" |

For a marketing page, the first screen explains the offer and presents a useful next action; aim for a short headline and supporting sentence. One action leads; secondary actions look secondary. Reading and application screens follow their own tasks, not this hero structure.

## Pages and applications

Reading pages organize an argument or support lookup; they do not need an invented call to action. Application screens support work: dense tables, filters, and states are normal, and quiet 1 px borders are legitimate. Design empty, loading, and error states. Tables keep numbers right-aligned and units in headers; interactive rows start at 40 px, with density fitted to the input method.

## Quality floor

Reflow ordinary content down to 320 CSS px without horizontal scrolling. Tables or maps may scroll within their own region when two-dimensional layout is necessary. Keep visible keyboard focus, semantic headings, appropriate alt text, reduced-motion support, and reserved image space. These are expected, not features.

## Done means

- Opened at 1440, 768, and 320 CSS px in a real browser; checked at enlarged text sizes and walked through by keyboard.
- No invented social proof, no AI-generated people or products presented as real.
