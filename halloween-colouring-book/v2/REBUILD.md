# Professional edition – build state & how to resume

Canva design: **Cozy Spooky Corner – Professional Edition (8x8, 20 pages)** (`DAHXK8HIE_4`).
The Canva connection expired mid-build, before the layout edits were saved, so that design may
show only a blank page. All generated artwork is already saved in your Canva account (see media IDs below),
so rebuilding is just layout - no new image generation needed.

## Page plan (20 pages)
1 Front cover (colour) · 2 This book belongs to · 3-18 story pages 1-16 · 19 Colour test page · 20 Back cover (colour)

## Story page layout (768 x 768 px = 8 x 8 in)
- Story text: top 44, left 40, width 510 - bold 24 px, plum #4A2D5E
- Colour-idea frame: rounded square 160 px at top 24 / left 574, fill #FFF6E8, orange #F08A24 4 px stroke
- Coloured sample image: 140 px at top 34 / left 584; label "Colour idea" below (15 px bold italic orange)
- Line art: 524 px square at top 212 / left 122 (all margins >= 0.33 in)

## Files
- `story_v2.py` – the 16 pages, their narration and which v1 line art each uses
- `story_ops_0.json`, `story_ops_8.json` – exact Canva operations for story pages 1-8 and 9-16
- `misc_ops.json` – belongs-to page, colour-test page, back cover, front cover settings
- `fmt_ops.json` – text styling (locator IDs are specific to the lost transaction; regenerate after re-adding text)

## Coloured "colour idea" samples (Canva media IDs, page order)
MAHXK3rZ6To MAHXK-20300 MAHXKwzTwjo MAHXKwuEg7U MAHXKxd7gXU MAHXK1rYvMQ MAHXK1ru1Rg MAHXK-NbYgw
MAHXKzKPOZ8 MAHXKyY4j7U MAHXK9kNavc MAHXKxoypXU MAHXKwJj7yA MAHXKzy-F-c MAHXK1lFqv8 MAHXKz_4S4o
Back cover art: MAHXK2Dcsvg · Front cover art: MAHXKVtUXEg · Belongs-to line art: MAHXKdbTkMI

## Status: rebuilt and saved in Canva

The 20-page professional edition is now saved in Canva as design `DAHXK8HIE_4`, in the "Halloween Colouring Book" folder (`FAHXKU1vixA`).
- Edit link: https://www.canva.com/d/qOT33kNXcs7Nbou
- Page order: front cover, belongs-to, colour test, 16 story pages, KDP back cover (art mirrored and barcode zone kept clear).
- Ops used: `c_a.json` (story 1-8), `c_b.json` (story 9-16), `c_c.json` (belongs, test, back cover) and `c_fmt.json` (text styles and back-art flip).
- For a sharp print file, download from Canva: Share -> Download -> PDF Print. The local `export/cozy-spooky-corner-print.pdf` is built from 200px previews, so its colour covers are soft.
