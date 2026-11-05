# Decisions not specified by the authority

- The four main rows are TAIPEI / DESIGN / WEEK / 2027. Their visible cap height is 210 px, their visible width is 840 px, and their horizontal scale differs to retain a common left and right edge. This is a display-only proportion adjustment.
- Inter 900 (Study Sans) is the single heavy display face. Inter 400 and 700 carry the reading facts without horizontal scaling.
- The A in TAIPEI carries a green/purple diagonal division. Three colored bars are clipped to the E in DESIGN. A true orange circle replaces the zero's visible shape in 2027. No reference-specific positions were available.
- The paper field beneath the four title rows holds the five categories on the left and the date, website, organizer, and partner on the right. The brief did not supply role labels or logos, so the organizer and partner remain plain names in the stated order.
- The DESIGN.md supplies approximate relationships rather than a required mathematical grid. The chosen cap size keeps four full-width walls while leaving the fixed facts readable at 22–36 px.
- The year is stored as the complete live text “2027”; its zero is graphically substituted with an editable native circle, as allowed by the geometric-letter brief. The rest of every fixed fact is visible live text.

# Input discipline

The unchanged input/DESIGN.md is the sole aesthetic authority. No references, prior artworks, other cases, existing drawing code, or additional skills were read. The font utility was used only to embed font subsets.

# Verification

Rendered in headless Chrome at 900 × 1200; document.fonts reports loaded and six embedded font faces are present. The own preview was visually inspected at full dimensions. Static XML checks confirm all 13 fixed facts appear in live text nodes, the required dimensions, and no raster image elements. The first completed SVG is preserved separately and is byte-identical to poster.svg; no artwork changes followed self-QA. Browser measurements are stored in qa.json and static checks in verification.json. Organizer and partner roles remain implied by their supplied order, without added labels.
