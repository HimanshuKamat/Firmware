# Exports

The full-resolution files exported fine in Canva, but this cloud environment's network policy blocks
`export-download.canva.com`, so they could not be saved into this folder.

To get them:
- **Open the Canva design** "Cozy Spooky Corner – Pip's Pumpkin Moon Party (8x8 Colouring Book)" in the
  "Halloween Colouring Book" folder: Share → Download → PDF Print (whole book) or PNG (all pages, zipped).
- Or allow `export-download.canva.com` under the environment's Network access settings and ask Claude to re-run
  the export; files will then land here as `cozy-spooky-corner.pdf` and `png/page-01.png` … `page-42.png`.

`storyboard-preview.pdf` in this folder is a local, low-resolution preview (cover, belongs-to page,
then the 40 story pages four to a page) so you can read the story flow. It is not print quality.

## cozy-spooky-corner-print.pdf (professional edition, built locally)
20 pages, 8 x 8 in, no bleed, all fonts embedded: front cover · belongs-to · colour test page · 16 story pages with a
"Colour idea" sample in the top-right corner · back cover (KDP: bottom-right 2 x 1.2 in barcode zone left clear).
Built by `v2/build_pdf.py` from the Canva artwork previews (line art upscaled and re-thresholded to
crisp black/white, ~290 dpi printed). Text, frames and the colour-test circles are vector.
Known limitation: the front and back cover pictures come from small previews (600 px / 200 px),
so they print soft. Swap in full-resolution Canva downloads before a commercial print run.
