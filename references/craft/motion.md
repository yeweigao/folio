# Motion

Motion explains a change of state or carries one earned expressive moment. AI motion fails by ornament: scattered fade-ups, parallax, floating backgrounds, letter-by-letter fly-ins. Often the right amount is none.

- **Motion has a job, not a habit.** State change, feedback, continuity, focus, or one expressive moment the subject earns. Name it first.
- **Distance sets duration, not taste.**

| Action | Duration | Easing |
|---|---|---|
| Press, hover | 100–150 ms | ease-out |
| Open, close | 150–200 ms | ease-out |
| Section change | 200–300 ms | cubic-bezier(0.2, 0, 0, 1) |
| Large movement | ≤ 400 ms | ease-in-out |
| Exit | 100–150 ms | ease-in |

- **Few things move, not many.** At most two at once; stagger 20–40 ms for up to five items, then all together.
- **Content never waits for motion.** Animate `transform` and `opacity`, never `all`; under `prefers-reduced-motion`, keep state changes and drop the rest; if it stutters, simplify.
- **Decks cut, not fly.** A build orders attention, axes before series; no bounces, cubes, or blinds.
- **Video is a carrier, not the only one.** Pausable, captioned when it speaks; generated footage never poses as documentary.
