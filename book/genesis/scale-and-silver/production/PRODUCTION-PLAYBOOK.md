# Production Playbook — A Bond of Scale and Silver

Portable print/ebook production knowledge for this book. Distilled from the first full
production run (done on the sister project *The Saeren Chronicles, Book One*); the verbatim
source notes and the build scripts are in `reference/`. **This book's own production has not
been run yet** — STATE.yaml lists "assemble full-manuscript.md + build PDF + packaging" as an
open, non-blocking step. Use this so we don't re-learn the corrections from scratch.

> Adult romantasy ~152k words → expect a substantially higher page count than Saeren's 263 pp
> (that book was ~85k). Re-derive page count from the real build before ordering a cover
> (spine width depends on it — see §5).

## 1. Assembly (before any PDF)
Build a single master first: `manuscript/full-manuscript.md` = title page + all 29 chapters
in order. Use `reference/assemble_manuscript.py` as the base — **adapt before running:**
- Extend `NUMWORDS` to 29 (Saeren's stops at 18).
- Title page → *A BOND OF SCALE AND SILVER* / *a novel* (standalone — no series
  line with author).
- This book's chapter titles live in each file's `# Chapter Twenty-Seven — Outlasted (I)` head;
  the Saeren script pulled titles differently — verify the title-extraction matches our format.
- Normalize scene breaks to a single consistent mark. **Our chapters use `*` / `\*` and `---`
  dividers** — pick one (`* * *`) and convert all, and make sure no stray divider sits stacked
  against a chapter heading.
- Strip markdown `#` heads and any HTML comments from the body; collapse 4+ blank-line runs.
- Sanity: assembled word count will be ~a few hundred below the per-file total (heading lines
  removed) — that's expected, no prose is cut.

## 2. Print interior PDF — specs that passed
Base: `reference/build_pdf.py` (reportlab). Specs proven compliant for IngramSpark/KDP:
- **Trim:** 6" × 9" (432 × 648 pt), exact page size, **no crop marks**.
- **Margins:** Saeren used 0.75" sides / 0.75" top / 0.70" bottom (symmetric, gutter-safe for
  ≤300 pp). **This book will be longer** — for higher page counts bump the **gutter** (inside):
  IngramSpark wants ~0.75"–0.875" inside for 300–500 pp. `build_pdf.py` supports mirrored
  inside/outside margins (0.875" inside / 0.625" outside is the script's default) — prefer
  mirrored margins here because of the thicker book.
- **Body:** IBM Plex Serif 11/15.5, justified, 16 pt first-line indent; **no indent** on a
  chapter's first paragraph or the paragraph after a scene break.
- **Scene breaks:** centered `* * *`. **Chapter heads:** page-break-before.
- **Page numbers:** centered footer; body starts at 1; title page + blank verso unnumbered.
- **No bleed** — correct for a text-only interior (nothing runs off-trim).

## 3. ⚠️ The font-embedding correction (must verify every build)
reportlab defaults some slots to base-14 **Helvetica, which is NOT embedded** and fails
preflight. The fix (already in `build_pdf.py`): register embedded IBM Plex Serif TTFs for
Regular/Italic/Bold/BoldItalic and override the default slot. **After every build, verify zero
non-embedded / base-14 fonts** (Acrobat preflight, or `pdffonts file.pdf` → every font shows
`emb=yes`). This was the single most important interior correction.

## 4. ⚠️ The RGB → PDF/X-1a CMYK correction (the "wrap/PDF" fix)
reportlab emits **RGB**. IngramSpark's *preferred* interior standard is **PDF/X-1a:2001
(CMYK + output intent)**. Text is pure black (0,0,0), so it prints fine, and both IngramSpark
and KDP will accept a standard PDF and convert — but for a guaranteed preflight pass, convert:

- **Ghostscript** (needs a PDF/X def file):
  `gs -dPDFX -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -dProcessColorModel=/DeviceCMYK \
     -sColorConversionStrategy=CMYK -sOutputFile=out-x1a.pdf PDFX_def.ps in.pdf`
- **or** Acrobat Pro → *Save as → PDF/X-1a*.
- **or** let the IngramSpark uploader convert on ingest.

`ghostscript` install is attempted by the SessionStart hook; reportlab/pillow too. If `gs`
isn't present the conversion is a one-step manual finish on a machine that has it.

## 5. Cover / wrap — WRAP BUILT 2026-07-10
Front cover is decided (`delivery/cover/front-cover-post-peleos.png`). The full **wrap** (back +
spine + front on one full-bleed canvas) is built by `compose_wrap.py` →
`delivery/production/A-Bond-of-Scale-and-Silver-wrap-6x9.pdf` (RGB proof) +
`…-wrap-6x9-X1a.pdf` (PDF/X-1a CMYK, verified CMYK-only + GTS_PDFX intent, fonts embedded).
- **Spine = 448 pp × 0.0025"/pp = 1.120"** for **IngramSpark cream 50#** (the fiction default;
  Saeren's exact stock was never recorded, so this matches the "same as Saeren" intent). If the
  stock is actually white 50#, set `PPI_FACTOR = 0.002252` in `compose_wrap.py` (→ ~1.009" spine)
  and rebuild.
- Full canvas **13.370" × 9.250"** (2·6 + 1.12 spine + 0.25 bleed). Front art's ~100px white
  bottom strip is auto-cropped so the dark art bleeds; back carries the `editorial/back-cover.md`
  copy + comps + an ISBN-barcode quiet-zone box; spine has title + author.
- Before ordering: confirm the exact paper stock, drop the printer's real barcode into the box,
  and re-verify the spine against IngramSpark's spine calculator for the final page count.

Legacy `reference/saeren-cover-brief.md` / `saeren-back-cover.md` are Saeren's — format templates only.
Wrap rules that bit us / to respect:
- A **full wrap** = back + spine + front on one canvas, at **full bleed (0.125" all round)** —
  different from the no-bleed interior. Don't reuse interior margins for the cover.
- **Spine width is a function of final page count × paper stock** — you cannot design the wrap
  until §2 produces the real page count. Use the printer's spine-width calculator with the built
  page count and the exact paper (white vs cream, 50# vs 70#).
- Keep text/logos out of the spine-safe and edge-safe zones; barcode area clear on the back.
- Cover art is **CMYK at 300 dpi**; the same RGB→CMYK caveat as §4 applies to the wrap PDF.

## 6. Front/back matter — DONE 2026-07-10
The interior now carries proper front matter, built by `build_pdf.py` (unnumbered; body still
paginates from 1 via a dynamic `front_pages` offset):
- **Half-title** (recto) → blank verso.
- **Title page** (recto): *A BOND OF SCALE AND SILVER* / *a novel* / **Post Peleos**.
- **Copyright page** (verso): © 2026 Post Peleos, all-rights-reserved, standard fiction
  disclaimer, "First edition, 2026". No ISBN/publisher line yet (add when assigned).
- **Dedication** (recto) → blank verso, driven by the `DEDICATION` constant at the top of
  `build_pdf.py` (currently a placeholder — swap in the author's final line and rebuild;
  set it to `""` to drop the dedication page).
- **Content/heat advisory:** author chose NOT to include one in the interior. (A content note
  for the retail *listing metadata* lives in `editorial/back-cover.md`.)
Adding front matter moved the page count 444 → **448 pp** (recompute the spine from 448).
Back-cover copy is in `editorial/back-cover.md` (correct for this book — Amelia/Korvan, standalone).

## 7. EPUB — DONE 2026-07-10
Reflowable **EPUB 3** built by `build_epub.py` (pure-Python, no external deps) from
`full-manuscript.md` → `delivery/production/A-Bond-of-Scale-and-Silver.epub`. Includes the
cover image, EPUB3 `nav` + NCX fallback, title/copyright/dedication front matter, and one
XHTML doc per chapter (scene breaks as centered dividers). Validated: mimetype-first & stored,
all XML well-formed, every manifest/spine/nav/css/image reference resolves. Kindle/Apple/Kobo +
IngramSpark ebook channel compatible. Rebuild after manuscript edits; `DEDICATION` mirrors the
print build.

## Quick status
- [x] **2026-07-12 — REBUILT after style edits (six accidental phrase echoes varied in Ch.22/23/26/27).**
      Reassembled `full-manuscript.md` (153,658 w), rebuilt interior PDF + X-1a. The shortened lines
      reflowed the book **448 → 446 pp**. Interior verified: only subsetted IBM Plex Serif, zero
      Helvetica. X-1a verified: GTS_PDFX + OutputIntent, DeviceCMYK, 0 DeviceRGB, fonts embedded.
      **⚠️ Spine now 446 × 0.0025" = 1.115" (cream 50#), was 1.120" @ 448 pp — rebuild the wrap
      (`compose_wrap.py`, set page count to 446) before ordering print. EPUB is page-count-independent
      but should be rebuilt too for the prose edits.**
- [x] Adapt + run `assemble_manuscript.py` → `manuscript/full-manuscript.md` (29 ch). **DONE 2026-07-10**
      — adapted script at `production/assemble_manuscript.py` (em-dash headings, WORD numerals to 29,
      scene breaks normalized to `* * *`). Assembled ~154,016 words, 77 scene breaks.
- [x] Adapt + run `build_pdf.py` → interior PDF; **verify fonts embedded** (§3). **DONE 2026-07-10**
      — adapted script at `production/build_pdf.py` (hyphenated CHAPTER regex, title page, output name).
      Output `delivery/production/A-Bond-of-Scale-and-Silver-6x9-interior.pdf`, **448 pp** (post front-matter), 6×9.
      Font check PASS: only subsetted IBM Plex Serif (Reg/It/Bd), 3 embedded programs, **zero Helvetica**.
- [x] Convert to PDF/X-1a CMYK (§4). **DONE 2026-07-10** — `production/PDFX_def.ps` (points at
      `/usr/share/color/icc/ghostscript/default_cmyk.icc`); output
      `delivery/production/A-Bond-of-Scale-and-Silver-6x9-interior-X1a.pdf`. Verified: OutputIntent
      present, GTS_PDFX marker, DeviceCMYK (0 DeviceRGB), fonts still embedded, 448 pp.
      NOTE: `default_cmyk.icc` is a generic profile; for a strict IngramSpark proof swap in the
      printer's target profile (US Web Coated SWOP / the IngramSpark-specified ICC) and re-run.
- [x] Real page count = **448 pp** @ 6×9, 11/15.5 Plex, 0.75" margins (was 444 before front matter
      was added). At 448 pp the symmetric 0.75" inside margin meets IngramSpark's 401–600 pp gutter
      (0.75") — mirrored margins optional. Still open: spine width from **448 pp** × chosen paper
      stock → design wrap at full bleed (§5).
- [x] **Front matter added (§6) 2026-07-10** — half-title, title page (title/"a novel"/Post Peleos),
      copyright page, dedication. **Dedication set** to the author's final line ("For all the ones that
      were told to hide themselves from the world. We see you."). Both PDFs rebuilt + re-verified
      (448 pp, fonts embedded, X-1a CMYK/GTS_PDFX). Back-cover copy: `editorial/back-cover.md`.
- [x] **Full wrap built (§5) 2026-07-10** — `compose_wrap.py` → `…-wrap-6x9.pdf` + `…-wrap-6x9-X1a.pdf`
      (CMYK/GTS_PDFX, fonts embedded). Spine **1.120"** @ 448 pp cream 50#; canvas 13.370×9.250".
- [x] **EPUB built (§7) 2026-07-10** — `build_epub.py` → `A-Bond-of-Scale-and-Silver.epub` (EPUB 3,
      validated structurally; cover + nav + front matter + 29 chapters).
- [ ] **Before ordering print:** confirm the paper stock (cream vs white → spine factor), assign
      print/ebook ISBNs, drop the real barcode into the wrap's quiet-zone box, and re-check the spine
      on IngramSpark's calculator. For a strict CMYK proof, swap the generic `default_cmyk.icc` for the
      printer's target ICC (US Web Coated SWOP / IngramSpark-specified) and re-run the X-1a conversions.
