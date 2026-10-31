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
- **Content is visible by default, not revealed on scroll.**
- **Applications are dense by design.** Tables, filters, and states are normal; quiet 1 px borders are legitimate; rows start at 40 px; empty, loading, stale, and error states are designed.
- **Interface words name the action.** Buttons are verb plus object; errors say what happened, how to fix it, and what was lost, without apology; empty states say what will appear; dangerous confirmations state the consequence.
- **Access is the floor.** Visible focus, semantic headings, alt text, reduced motion, reserved image space.

## Motion

Often the right amount is none. AI motion fails by ornament: scattered fade-ups, parallax, floating backgrounds, letter-by-letter fly-ins.

- **Name the job first:** state change, feedback, continuity, focus, or one expressive moment the subject earns.
- **Distance sets duration:**

| Action | Duration | Easing |
|---|---|---|
| Press, hover | 100–150 ms | ease-out |
| Open, close | 150–200 ms | ease-out |
| Section change | 200–300 ms | cubic-bezier(0.2, 0, 0, 1) |
| Large movement | ≤ 400 ms | ease-in-out |
| Exit | 100–150 ms | ease-in |

- **Few things move.** At most two at once; stagger 20–40 ms for up to five items, then all together.
- **Content never waits for motion.** Animate `transform` and `opacity`, never `all`; under `prefers-reduced-motion`, keep state changes and drop the rest; if it stutters, simplify.
- **Video is a carrier, not the only one.** Pausable, captioned when it speaks; generated footage never poses as documentary.

## Done means

- Opened at 1440, 768, and 320 CSS px in a real browser, at enlarged text, and by keyboard.
