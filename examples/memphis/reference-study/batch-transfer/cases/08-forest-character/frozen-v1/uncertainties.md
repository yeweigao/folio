# Decisions not specified by DESIGN.md

- The 900 × 1200 page uses a yellow upper field of 800 px and a blue information field of 400 px. The left checkerboard column is 252 px wide, with a 126 px cell that also forms the upper crossbar.
- The brand occupies the yellow space above the crossbar. “After Hours” uses a single line within the main yellow field; the soft character remains the largest continuous foreground form.
- Pink is assigned to the character, checkerboard light squares, and vertical date capsule. Black forms the dark checkerboard squares, masthead, pupils, and trunk. Event information is white on blue.
- The body is three overlapping horizontal ellipses. Unequal eye sizes and unequal pupil positions supply character; no additional facial features are inferred.
- The date reads from bottom to top in its own rounded capsule. Time, venue, and body copy remain horizontal. The four semantic body lines retain the exact supplied wording.
- The year is fully visible in the lower left. The tree uses a native zigzag polygon and a rectangular trunk. The full fixed facts are visible instead of using the optional cropping allowance.
- Study Sans (Inter) at weights 400, 700, and 900 is used for the live typography. The provided font utility embeds all six supplied font faces as subsets; unused faces remain available in the SVG stylesheet.

# Verification

- Parsed the standalone SVG successfully at 900 × 1200.
- Compared all seven editable text elements with the supplied facts; every string matches, including punctuation and the complete paragraph.
- Confirmed six embedded WOFF2 font faces, no raster images, and no external asset URLs.
- Rendered with local headless Chrome through Playwright; all three used Study Sans weights loaded from the embedded fonts. Visually inspected the full-size image and a 225 × 300 thumbnail.
- Browser text line boxes extend slightly beyond the viewport for the header and year, but the actual rendered glyphs are fully visible: logo ink bounds [290, 20, 601, 106]; year ink bounds [35, 1103, 281, 1181]. Pixel checks also recorded the exact ink bounds in structural-qa.json.
- Preserved the first complete SVG, generator, and decisions record under first-complete/ before local QA. No artwork changes were made after that preservation.
- No independent aesthetic evaluation is claimed.
