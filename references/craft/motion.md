# Motion

Motion explains a change of state or carries one deliberate expressive moment. Scattered fade-ups, floating backgrounds, parallax, and letter-by-letter fly-ins easily compete with the content. Often the right amount is none.

## Legitimate jobs

State change (open, close, switch, loaded), feedback (press, validate, drop), continuity (an item expanding into its detail), focus (the current step), or an expressive moment the subject earns. Name the job before adding motion.

## Timing

| Action | Duration | Easing |
|---|---|---|
| Press, hover | 100–150 ms | ease-out |
| Open, close | 150–200 ms | ease-out |
| Page or section change | 200–300 ms | cubic-bezier(0.2, 0, 0, 1) |
| Large movement | ≤ 400 ms | ease-in-out |
| Exit | 100–150 ms | ease-in |

Distance sets duration: under 24 px, 100–150 ms; up to 200 px, 200–300 ms; beyond, 300–400 ms. Stagger 20–40 ms per item for at most five items; six or more appear together. At most two moving elements on screen at once.

## Implementation that stays smooth

Prefer `transform` and `opacity`; name each transitioned property rather than `all`. Content stays available without animation. Under `prefers-reduced-motion`, remove nonessential movement and preserve state changes instantly or with a brief fade. If motion stutters, simplify it.

## Slides and video

In decks, cuts by default; a build controls the order of attention, with charts establishing axes before series. No decorative fly-ins, bounces, cubes, or blinds. Video is pausable, captioned when it carries speech, and never the only carrier of essential information; generated footage must not pose as documentary evidence.
