# Phase 2: Style test results

Canva tool used: `generate-image` (square 1:1). Pages were placed full-bleed in the Canva design
**"Cozy Spooky Corner – Style Test"** (design `DAHXJwZi_rk`, 2 pages) and exported as 2400 x 2400 px PNG
(8 in at 300 dpi). The export itself succeeded. However, this cloud environment's network policy
blocks `export-download.canva.com`, so the full-resolution PNGs could not be saved locally. All checks
below use Canva's returned previews (600 px for A, 200 px for B–D).

## Prompt variants
| ID | Wording focus |
|----|---------------|
| A | Shared style block from PLAN.md (thick bold outlines, no grey/shading, kawaii, full scene) |
| B | "Simple bold colouring page… very thick black marker outlines, all lines the same heavy weight, like a fat felt-tip pen… few large rounded shapes, big open white spaces, no tiny details, no small repeated objects" |
| C | "Bold and easy colouring book illustration, black outline vector line art, thick uniform stroke…" |
| D | Short prompt: "colouring book page, black and white line art, thick outlines, no shading, white background…" |

## Measurements (same 200 px previews, witch's kitchen unless noted)
| Variant | Colour present | Ink coverage | Enclosed white regions | Tiny regions (hard to colour) |
|---------|----------------|--------------|------------------------|-------------------------------|
| A witch | none | 17.8 % | 212 | **85** |
| A ghost | none | 15.5 % | 90 | 20 |
| **B witch** | none | 21.0 % | **82** | **4** |
| C witch | none | 22.1 % | 202 | 51 |
| D witch | none | 19.6 % | 143 | 43 |

At 600 px, variant A's line width measures about 0.7 mm (witch) to 1.0 mm (ghost) at the 8 in print size.
That is thin for a "bold" colouring book, where 1.5–2.5 mm is typical.

## Verdict
- **True black & white line art?** Yes, for every variant. There is no colour and no grey shading.
  The only grey pixels are antialiasing on line edges.
- **Outlines thick enough?** Not with A, C or D: they come out as fine to medium lines. **B** gives
  visibly heavier, more uniform lines.
- **Shading / solid black?** No shading. A's ghost page has small solid-black bats in the bunting and
  on a cupcake. They're minor, but they break the "no solid black" rule.
- **Colourable?** A's witch page is too fussy, with herb bunches, sweets in jars and floorboards.
  A's ghost page is acceptable. **B** is by far the most colourable.
- **Best prompt: B.** Its weakness is that it is a bit sparse (fewer props) and it added a rounded border frame.
  It still reads as a full scene, but it is less rich than the Coco-Wyo-like density you described.

Recommendation for Phase 3: use B's line and detail wording, list 4–6 props per scene so pages stay
full, and add "no border frame, no solid black fills".
