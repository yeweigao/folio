# Data

A chart is an argument, not a container. If you cannot say which judgment the reader should change after seeing it, do not draw it. AI charts fail by decoration: donuts, gauges, rainbow series, legends, chart cards, and numbers that are invented to look impressive.

## Question decides the chart

| Question | Use | Not |
|---|---|---|
| Which is bigger | Horizontal bars (long labels), columns (short) | Pie, donut, 3D |
| How it changed over time | Line; area only for cumulative totals | Dual axis, oversmoothing |
| How it is distributed | Histogram, box plot, strip plot | A lone average |
| Whether two things relate | Scatter, with care about any fit | Correlation sold as cause |
| What it is made of | Stacked or 100% bar | Pie, treemap without real hierarchy |
| How far from a baseline | Diverging bar, zero in the middle | Gauge |
| How uncertain | Error bars, interval bands | Bare points |
| Many small groups | Small multiples | Twelve lines in one plot |

## Honest geometry

- Bars start at zero; a cut axis is marked and explained. Lines may be cut but show their range, so 1% does not look like a crash.
- One unit per chart; never two axes. For two units, two charts on a shared baseline, or index both to 100.
- At most five gridlines, thinner than the data (screen: data 2 px, grid 1 px; print: 1–1.5 pt and 0.5–0.75 pt); 3–5 axis ticks; bar gaps no wider than bars.
- Order by size or logic, not alphabet, unless lookup is the task.

## Labels and color

- Label series names and end values directly; no legend when labels fit. One annotation per chart, one thin line and one sentence.
- Titles state the finding ("Enrollment rose three years running, but growth halved in 2026"), not the topic ("Enrollment 2024–2026").
- Units on the axis title or first tick; source, period, and definition under the chart at 12–14 px.
- One accent color for the one series or finding that matters; everything else ink at 100 / 62 / 38%. At most five categories; sequential data in one hue's steps; diverging data in two hues with paper at the midpoint; never a rainbow, never red-green as the only difference.

## Tables

Open horizontal rules, no verticals, no zebra stripes, no colored cells unless they encode a mapped status. Numbers right-aligned on the decimal; units in the header; percentages and absolutes in separate columns; totals set apart by a rule or space.

## Numbers that hold up

Keep only the precision a decision needs (32.4%, not 32.417%). Percent and percentage points are different. Rates name their denominator (3.2%, 32 of 1,000). Forecasts are dashed and labeled with their assumptions. Missing data is not zero. Demo numbers say `illustrative`, as visibly as real ones, with the arithmetic shown.

## Dashboards

One main metric, one trend, one breakdown, in reading order. Each metric carries value, baseline, period, source, and direction of change, set as a typographic ledger with hairlines rather than a wall of tiles. State is encoded in text, shape, and color together. Design empty, loading, and error states too.
