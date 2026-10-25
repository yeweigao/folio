# web

A web page is read, scrolled, clicked, used by keyboard, and loaded on a slow phone. It is not a tall poster.

## Grid

- Content = min(1440, viewport − 2 × max(24 px, 5vw)); 12 columns, 24 gutters. At a 1440 viewport, content 1296 (columns 86); from 1600 up, content caps at 1440 (columns 98).
- Breakpoints 390 / 768 / 1024 / 1440; columns collapse 12 → 8 → 6 → 4 and stay identifiable.
- Text 16–20 px, leading 1.5–1.7, measure ≤ 65ch (CJK 25–35). H1 up to 80 px; a display word or number up to 112 px, treated as a graphic.
- Tokens: paper, ink, accent, muted, line, focus. The theme sets radius and depth; in the Swiss theme, radius 0 (true circles stay circles) and no shadows, with depth from 1 px lines, fields, and space.

## Where web pages go generic

| The template move | Instead |
|---|---|
| Small colored eyebrow, centered headline, subline, gradient button, three feature cards, logo wall | A flush-left headline that states what this is, one supporting sentence, one action; the first screen shows the real product, a real number, or something to use |
| Every section: icon, title, two lines, repeated in threes | Six to nine sections, one idea each, each in the form its content needs |
| Testimonials and "trusted by" invented to fill space | Only real quotes and logos with permission; otherwise leave the section out |
| Fade-up on every element as it scrolls in | Content visible by default; one orchestrated moment at most |
| Purple-to-blue gradient, glass panels, glow | Paper, ink, one accent; texture from real images |
| "Learn more" buttons | A verb and an object: "Book a visit", "Download the report" |

The first screen at 1280 × 800 shows the headline (≤ 2 lines), one sentence (≤ 12 words or 30 characters), and one primary action. Fewer than 80 words above the fold. One primary call to action per page; secondary actions look secondary.

## Pages and applications

Pages are for reading and have a claim, rhythm, and one call to action. Application screens are for work: dense tables, filters, and states are normal, and quiet 1 px borders are legitimate. Design the empty, loading, and error states, not only the perfect full screen. Tables: numbers right-aligned, units in headers, rows at least 40 px.

## Quality floor

Responsive down to 390 with no horizontal scroll; visible 2 px focus on every control; semantic headings in order; alt text; reduced motion respected; images sized to avoid layout shift. These are expected, not features.

## Done means

- Opened at 1440, 768, and 390 in a real browser; walked through by keyboard.
- No invented social proof, no AI-generated people or products presented as real.
