# Cover — concept mockups

Front-cover **concept mockups** for *A Bond of Scale and Silver*, generated in-repo (self-contained
HTML/SVG rendered with headless Chromium; fonts: IBM Plex Serif + Young Serif). These are directional
concepts to react to and iterate on — not a substitute for a final illustrated/stock cover if the
author wants photographic or painted art.

Built to the direction in `editorial/cover-brief.md` (cold moon-silver + charcoal night, restrained
blood-red, dragon iconography over illustration, weighty serif title, no clinch/no roaring-dragon).

## Concept A — moon + rising dragon-scale field
`concept-A-front-1600x2560.png` — generator: `concept-A_make_cover.py`
- **Hero:** cold full moon (the "silver" — Amelia's hair / the full moon).
- **Foreground:** a field of dragon **scales** rising from shadow (the "scale" — Korvan the dragon);
  one deliberate **blood-red** scale = the blood-magyk note / the one marked among the many.
- **Type:** *A BOND OF · Scale & Silver · a novel*, silver-to-ember gradient serif. Author line is a
  **placeholder** (no author name is set in the repo — all `[Author Name]`).
- Size: 1600×2560 (ebook / KDP ratio). For print, re-render at 6×9 + full-bleed wrap (see below).

## To regenerate / tweak
```
python3 concept-A_make_cover.py            # writes cover.html
/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless --no-sandbox --disable-gpu \
  --force-device-scale-factor=1 --window-size=1600,2560 --screenshot=out.png "file://$PWD/cover.html"
```

## Files
- `front-cover-post-peleos.png` — the decided final front (1600×2263). Has an ~87px white strip
  at the very bottom (below the author line).
- `front-cover-post-peleos-clean.png` — same art with that white strip cropped (1600×2176), so the
  dark art bleeds edge-to-edge. Use this as the canonical front/ebook asset; the wrap builder crops
  the white strip on the fly from the original, so either source produces the same front panel.

## Status (2026-07-10)
- **Author name** — set: **Post Peleos** (on the final front `front-cover-post-peleos.png`).
- **Print wrap** — ✅ BUILT. `production/compose_wrap.py` lays out back + spine + front on one
  full-bleed (0.125") 6×9 canvas → `delivery/production/A-Bond-of-Scale-and-Silver-wrap-6x9.pdf`
  (+ `-X1a.pdf` CMYK). Spine **1.120"** @ 448 pp cream 50# (change `PPI_FACTOR` for white stock).
  Back copy from `editorial/back-cover.md`; ISBN-barcode quiet-zone box included.
- **CMYK** — ✅ wrap + interior both converted to PDF/X-1a (CMYK-only, GTS_PDFX intent).
- **Ebook** — ✅ the front cover is embedded in the EPUB (`A-Bond-of-Scale-and-Silver.epub`).
- **Before print order** — confirm paper stock, assign ISBNs, drop the printer's real barcode into
  the wrap box, re-verify spine on IngramSpark's calculator (see PRODUCTION-PLAYBOOK §5).
