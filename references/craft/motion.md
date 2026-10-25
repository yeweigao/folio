# Motion

Motion explains a change of state; it does not perform. Scattered fade-ups on every block, floating backgrounds, parallax, and letter-by-letter fly-ins are among the quickest signs of a generated page. One well-orchestrated moment does more than twenty small ones, and often the right amount is none.

## Legitimate jobs

State change (open, close, switch, loaded), feedback (press, validate, drop), continuity (an item expanding into its detail), and focus (the current step). Anything else is decoration and goes.

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

Animate only `transform` and `opacity`; name each transitioned property rather than `all`. Content is visible without JavaScript and without the animation. Under `prefers-reduced-motion`, motion becomes instant or a fade of ≤ 100 ms. Below 30 fps, remove the animation.

## Slides and video

In decks, cuts by default; a build only to control the order of attention, one per slide; charts reveal axes before series. No fly-ins, bounces, cubes, or blinds. Video only from real footage: muted, pausable, captioned, its first frame a usable poster, never the only carrier of information.
