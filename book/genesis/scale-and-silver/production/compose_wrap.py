#!/usr/bin/env python3
"""
Compose the full print cover WRAP (back + spine + front) for *A Bond of Scale and Silver*.

Layout (6x9 trim, full bleed 0.125"):
  [left bleed][ BACK 6" ][ SPINE ][ FRONT 6" ][right bleed]   x  [top/bottom bleed]

Spine width is page-count x paper factor. Default: IngramSpark CREAM 50# = 0.0025"/page.
At 448 pp -> 1.12" spine. Change PAGES / PPI_FACTOR if the stock differs.

Front art = delivery/cover/front-cover-post-peleos.png (the decided front); its ~100px
white bottom strip is cropped so the dark art bleeds. Back-cover copy from editorial/back-cover.md.

Output: delivery/production/A-Bond-of-Scale-and-Silver-wrap-6x9.pdf  (RGB; convert to
PDF/X-1a CMYK with the same gs pipeline as the interior — see PRODUCTION-PLAYBOOK §4/§5).
"""
import os
from PIL import Image
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.colors import Color, HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Frame

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONT = os.path.join(ROOT, "delivery", "cover", "front-cover-post-peleos.png")
OUT = os.path.join(ROOT, "delivery", "production", "A-Bond-of-Scale-and-Silver-wrap-6x9.pdf")
TMP = os.path.join(ROOT, "delivery", "production", "_front-bleed.png")

# --- dimensions ---
TRIM_W, TRIM_H, BLEED = 6.0, 9.0, 0.125
PAGES = 448
PPI_FACTOR = 0.0025            # IngramSpark cream 50#  (white 50# = 0.002252)
SPINE = PAGES * PPI_FACTOR     # 1.12"
FULL_W = 2 * TRIM_W + SPINE + 2 * BLEED
FULL_H = TRIM_H + 2 * BLEED
SAFE = 0.375                   # keep text this far inside the trim

# --- palette (sampled from the cover) ---
BG = HexColor("#050A11")
SILVER = HexColor("#DCE2EC")
GREY = HexColor("#AEB8C6")
EMBER = HexColor("#C9A25A")

FONT_DIR = "/mnt/skills/examples/canvas-design/canvas-fonts"
pdfmetrics.registerFont(TTFont("Plex", f"{FONT_DIR}/IBMPlexSerif-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Plex-It", f"{FONT_DIR}/IBMPlexSerif-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Plex-Bd", f"{FONT_DIR}/IBMPlexSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Plex-BdIt", f"{FONT_DIR}/IBMPlexSerif-BoldItalic.ttf"))
# reportlab declares a default base-14 Helvetica slot even when unused; override it to an
# embedded TTF so the RGB proof carries zero non-embedded fonts (the X-1a is clean either way).
pdfmetrics.registerFont(TTFont("Helvetica", f"{FONT_DIR}/IBMPlexSerif-Regular.ttf"))


def prep_front():
    """Crop the white bottom strip so the dark art can bleed off-trim."""
    im = Image.open(FRONT).convert("RGB")
    w, h = im.size
    # find first mostly-white row from the bottom going up
    def rowwhite(y):
        return sum(1 for x in range(0, w, 10) if sum(im.getpixel((x, y))) > 720) / (w / 10)
    cut = h
    y = h - 1
    while y > int(h * 0.85) and rowwhite(y) > 0.5:
        cut = y; y -= 1
    im = im.crop((0, 0, w, cut))
    im.save(TMP)
    return TMP


def draw_cover_fit(c, img_path, x, y, w, h):
    """Place image to COVER the (x,y,w,h) rect (scale-to-fill, center-crop)."""
    im = Image.open(img_path)
    iw, ih = im.size
    target = w / h
    src = iw / ih
    if src > target:            # image wider -> crop sides
        new_w = int(ih * target); off = (iw - new_w) // 2
        box = (off, 0, off + new_w, ih)
    else:                       # image taller -> crop top/bottom
        new_h = int(iw / target); off = (ih - new_h) // 2
        box = (0, off, iw, off + new_h)
    crop = im.crop(box)
    tmp = img_path + ".fit.png"
    crop.save(tmp)
    c.drawImage(tmp, x * inch, y * inch, w * inch, h * inch)
    return tmp


def main():
    front = prep_front()
    c = canvas.Canvas(OUT, pagesize=(FULL_W * inch, FULL_H * inch))

    # 1) whole canvas dark (so any bleed/gaps match the art)
    c.setFillColor(BG)
    c.rect(0, 0, FULL_W * inch, FULL_H * inch, fill=1, stroke=0)

    # panel x-origins (inches from left)
    back_x0 = BLEED
    spine_x0 = BLEED + TRIM_W
    front_x0 = BLEED + TRIM_W + SPINE

    # 2) FRONT art — cover the front trim + right/top/bottom bleed
    fit = draw_cover_fit(c, front, front_x0, 0.0,
                         TRIM_W + BLEED, FULL_H)

    # 3) SPINE text (rotated -90, reading top-to-bottom). Vertical baseline offset so
    #    the glyphs sit centered across the 1.12" spine width.
    spine_cx = (spine_x0 + SPINE / 2) * inch
    vshift = 5  # points: nudge baseline to optical center of the spine width
    # title, biased toward the TOP (front) half of the spine
    c.saveState()
    c.translate(spine_cx, (FULL_H / 2 + 1.3) * inch)
    c.rotate(-90)
    c.setFillColor(SILVER)
    c.setFont("Plex-Bd", 15)
    c.drawCentredString(0, vshift, "A BOND OF SCALE AND SILVER")
    c.restoreState()
    # author name, near the BOTTOM (back) end of the spine, well clear of the title
    c.saveState()
    c.translate(spine_cx, (BLEED + SAFE + 0.55) * inch)
    c.rotate(-90)
    c.setFillColor(GREY)
    c.setFont("Plex-It", 12)
    c.drawCentredString(0, vshift, "Post Peleos")
    c.restoreState()

    # 4) BACK panel text
    back_left = (back_x0 + SAFE) * inch
    back_width = (TRIM_W - 2 * SAFE) * inch
    tag = ParagraphStyle("tag", fontName="Plex-BdIt", fontSize=13, leading=17,
                         textColor=SILVER, alignment=TA_CENTER, spaceAfter=16)
    hook = ParagraphStyle("hook", fontName="Plex-It", fontSize=11.5, leading=16,
                          textColor=SILVER, alignment=TA_CENTER, spaceAfter=12)
    para = ParagraphStyle("para", fontName="Plex", fontSize=10.5, leading=15,
                          textColor=GREY, alignment=TA_LEFT, spaceAfter=9)
    closing = ParagraphStyle("closing", fontName="Plex-It", fontSize=10.5, leading=15,
                             textColor=SILVER, alignment=TA_CENTER, spaceBefore=4, spaceAfter=12)
    comps = ParagraphStyle("comps", fontName="Plex-Bd", fontSize=10, leading=14,
                           textColor=EMBER, alignment=TA_CENTER)

    flow = [
        Paragraph("Two hunted things, one road, and a war that ends at a crown neither of them wanted.", tag),
        Paragraph("She was born to be a secret. The world is about to make her a war.", hook),
        Paragraph("Amelia has never been allowed outside. The first vampire born&#8212;not made&#8212;in a "
                  "thousand years, she is her mother the Queen&#8217;s cherished, forbidden secret: a girl "
                  "with blood magyk that should not exist, kept behind a bolt because her very existence "
                  "could shatter the treaty that holds three peoples apart. She wants one thing the world "
                  "will never grant her&#8212;to be seen.", para),
        Paragraph("Then a grief-poisoned schemer unveils her before both courts, and the war begins.", para),
        Paragraph("On the run at last, Amelia crosses paths with Korvan, the shifter chief&#8217;s outcast "
                  "son&#8212;a late shifter whose first change makes him the one creature more hunted than "
                  "she is: a dragon out of dead legend, a clan of one. Thrown together on a brutal road with "
                  "the war closing behind them, two exiles learn each other. But the bond they choose is not "
                  "fated, and being finally seen will cost Amelia everything she loves.", para),
        Paragraph("A dark, adult romantasy of dangerous devotion, chosen love, and the terrible price of the truth.", closing),
        Paragraph("For readers of Carissa Broadbent, Danielle L. Jensen, and Anne Bishop.", comps),
    ]
    # frame spans from above the barcode zone up to the top safe line
    barcode_h, barcode_w = 1.2, 2.0
    frame_bottom = (BLEED + SAFE + barcode_h + 0.25) * inch
    frame_top = (FULL_H - BLEED - SAFE) * inch
    f = Frame(back_left, frame_bottom, back_width, frame_top - frame_bottom,
              leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, showBoundary=0)
    f.addFromList(flow, c)

    # 5) barcode placeholder (white box, quiet zone) bottom-right of the back panel
    bx = (spine_x0 - SAFE - barcode_w) * inch
    by = (BLEED + SAFE) * inch
    c.setFillColor(Color(1, 1, 1))
    c.rect(bx, by, barcode_w * inch, barcode_h * inch, fill=1, stroke=0)
    c.setFillColor(Color(0.45, 0.45, 0.45))
    c.setFont("Plex", 7)
    c.drawCentredString(bx + barcode_w * inch / 2, by + barcode_h * inch / 2 - 3,
                        "ISBN barcode area")

    c.showPage()
    c.save()
    # cleanup temp fit file (keep _front-bleed for inspection? remove both)
    for t in (TMP, front + ".fit.png"):
        try: os.remove(t)
        except OSError: pass
    print("wrote", OUT)
    print(f"spine = {SPINE:.3f}\"  full canvas = {FULL_W:.3f}\" x {FULL_H:.3f}\"  ({PAGES}pp, cream 50#)")


if __name__ == "__main__":
    main()
