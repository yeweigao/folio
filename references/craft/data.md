# Data

A chart answers a question; a reference table supports lookup. Name that task before drawing either. AI charts fail by decoration: donuts, gauges, rainbow series, legends, chart cards, and numbers that are invented to look impressive.

## Question decides the chart

| Question | Use | Not |
|---|---|---|
| Which is bigger | Horizontal bars (long labels), columns (short) | Pie, donut, 3D |
| How it changed over time | Line; area when magnitude from zero or part-to-whole matters | Dual y-axes, oversmoothing |
| How it is distributed | Histogram, box plot, strip plot | A lone average |
| Whether two things relate | Scatter, with care about any fit | Correlation sold as cause |
| What it is made of | Stacked or 100% bar | Pie, treemap without real hierarchy |
| How far from a baseline | Diverging bar, zero in the middle | Gauge |
| How uncertain | Error bars, interval bands | Bare points |
| Many small groups | Small multiples | Twelve lines in one plot |

## Honest geometry

- Bars start at zero; a cut axis is marked and explained. Lines may be cut but show their range, so 1% does not look like a crash.
- One scale per axis; avoid dual y-axis overlays. For time series with different units, use aligned panels or index each to a stated base. A scatter plot's x and y axes may measure different quantities.
- At most five gridlines, thinner than the data (screen: data 2 px, grid 1 px; print: 1–1.5 pt and 0.5–0.75 pt); 3–5 axis ticks; bar gaps no wider than bars.
- Order by size or logic, not alphabet, unless lookup is the task.

## Labels and color

- Label series names and end values directly; no legend when labels fit. One annotation per chart, one thin line and one sentence.
- Argument titles state the finding ("Enrollment rose three years running, but growth halved in 2026"); lookup charts and tables use descriptive titles. Fixed copy stays unchanged.
- Units on the axis title or first tick; source, period, and definition under the chart, sized for the surface and viewing distance.
- One accent color for the series or finding that matters; reference data may keep equal emphasis. Ink at 100 / 62 / 38% is a starting palette, not a contrast guarantee: measure the composite. Aim for at most five distinguishable series; split crowded plots without dropping required categories. Sequential data uses one hue's steps; diverging data two hues with paper at the midpoint; never red-green as the only difference.

## Tables

Open horizontal rules by default; add vertical separators or subtle row striping only when they aid lookup. Colored cells encode a mapped status. Numbers right-aligned on the decimal; units in the header; percentages and absolutes in separate columns; totals set apart by a rule or space. Reference tables keep stable column widths, order, and repeated headers.

## Numbers that hold up

Keep required source precision; for derived values, show only the precision a decision needs (32.4%, not 32.417%). Percent and percentage points are different. Rates name their denominator (3.2%, 32 of 1,000). Forecasts are dashed and labeled with their assumptions. Missing data is not zero. Demo numbers say `illustrative`, as visibly as real ones, with the arithmetic shown.

## Dashboards

For a narrative dashboard: one main metric, one trend, one breakdown, in reading order. Monitoring views may give peers equal weight and repeat a stable layout. Each metric carries value, baseline, period, source, and direction of change. State is encoded in text, shape, and color together. Design empty, loading, and error states too.
