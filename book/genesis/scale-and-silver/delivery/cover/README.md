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

## Still open (per cover-brief §production)
- **Author name** — needed before finalizing type.
- **Print wrap** — spine width from **444 pp** × chosen paper stock, then lay out back + spine + front
  on one full-bleed (0.125") canvas at 6×9. Back-cover copy is ready in `editorial/back-cover.md`.
- **CMYK** — convert the final print cover to PDF/X-1a (same pipeline as the interior).
- **Ebook** — 2560×1600 px RGB per KDP (this mockup is already at that ratio).
