# Web

A page is read, scrolled, clicked, used by keyboard, and loaded on a slow phone. It is not a tall poster.

## Starting system

- Content = min(1440, viewport − 2 × max(24 px, 5vw)); 12 columns, 24 gutters: 1296 wide at a 1440 viewport, capped at 1440 from 1600.
- Columns collapse where the content breaks, around 1024 / 768 / 480; reflow to 320 CSS px; tables and maps may scroll within their own region.
- Text 16–20 px, leading 1.5–1.7, measure ≤ 65ch (CJK 25–35); H1 starts at 40–80 px. A graphic word or number takes the scale its composition needs, reflowing at smaller viewports.
- Tokens: ground, text, emphasis, muted, line, focus. The theme sets radius, depth, and palette.

## Principles

- **The first screen shows the thing, not a hero formula.** What this is, one supporting sentence, one leading action, and the real product, number, or tool. Reading and application screens follow their own tasks.
- **Sections follow tasks, not threes.** Repeat a structure only where it aids comparison or navigation.
- **Proof is real or absent.** Only real quotes and permitted logos.
- **Content is visible by default, not revealed on scroll.** One orchestrated moment at most.
- **Applications are dense by design, not decorated.** Tables, filters, and states are normal; quiet 1 px borders are legitimate; rows start at 40 px; empty, loading, and error states are designed.
- **Access is the floor, not a feature.** Visible focus, semantic headings, alt text, reduced motion, reserved image space.

## Where pages go generic

| The template move | Instead |
|---|---|
| A hero formula unrelated to the task | The subject, its proof, and a clear next action |
| Icon, title, two lines, in threes | Sections shaped by their tasks |
| Fade-up on everything | Content already there |
| Surface effects competing with content | Separation where needed; expression from the chosen theme |
| "Learn more" | A verb and an object |

## Done means

- Opened at 1440, 768, and 320 CSS px in a real browser, at enlarged text, and by keyboard.
