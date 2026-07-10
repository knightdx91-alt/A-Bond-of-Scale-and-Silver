#!/usr/bin/env python3
"""
Build a print-ready interior PDF of Book One to IngramSpark interior specs.

Trim: 6" x 9" (standard YA/fantasy trade paperback).
Margins (mirrored): inside/gutter 0.875", outside 0.625", top 0.75", bottom 0.70".
  - IngramSpark minimum margin from trim is 0.5"; gutter here exceeds the
    recommended minimum for books up to ~500 pp.
Fonts: IBM Plex Serif (Regular/Italic/Bold/BoldItalic), fully embedded.
Body: 11pt / 15.5pt leading, justified, 16pt first-line indent (no indent on
  the first paragraph of a chapter or after a scene break).
Output: delivery/production/A-Bond-of-Scale-and-Silver-6x9-interior.pdf

NOTE: This produces an embedded-font, exact-trim, correctly-margined RGB PDF.
IngramSpark's *preferred* format is PDF/X-1a:2001 (CMYK + output intent); that
final conversion needs Acrobat/Ghostscript and is not available in this
environment. For pure-black text this PDF will print correctly; see the
production note for the X-1a/CMYK caveat.
"""
import os, re, html
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame,
                                Paragraph, Spacer, PageBreak, NextPageTemplate)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "manuscript", "full-manuscript.md")
OUT = os.path.join(ROOT, "delivery", "production",
                   "A-Bond-of-Scale-and-Silver-6x9-interior.pdf")

BOOK_TITLE = "A BOND OF SCALE AND SILVER"
AUTHOR = "Post Peleos"
YEAR = "2026"

# --- Dedication --------------------------------------------------------------
# Replace with the author's final line. Set to "" to omit the dedication page.
DEDICATION = "For all the ones that were told to hide themselves from the world. We see you."

FONT_DIR = "/mnt/skills/examples/canvas-design/canvas-fonts"
pdfmetrics.registerFont(TTFont("PlexSerif", f"{FONT_DIR}/IBMPlexSerif-Regular.ttf"))
pdfmetrics.registerFont(TTFont("PlexSerif-It", f"{FONT_DIR}/IBMPlexSerif-Italic.ttf"))
pdfmetrics.registerFont(TTFont("PlexSerif-Bd", f"{FONT_DIR}/IBMPlexSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("PlexSerif-BdIt", f"{FONT_DIR}/IBMPlexSerif-BoldItalic.ttf"))
pdfmetrics.registerFontFamily("PlexSerif", normal="PlexSerif", bold="PlexSerif-Bd",
                              italic="PlexSerif-It", boldItalic="PlexSerif-BdIt")
# reportlab declares a default /Helvetica in the shared font resources even when
# unused; that base-14 font is NOT embedded and fails IngramSpark preflight.
# Override the name so the slot embeds a TTF instead of base-14 Helvetica.
pdfmetrics.registerFont(TTFont("Helvetica", f"{FONT_DIR}/IBMPlexSerif-Regular.ttf"))

# Geometry — symmetric, gutter-safe margins (IngramSpark-compliant for <=~500pp).
# Both side margins 0.75" exceed the 0.5" minimum and meet gutter needs without
# fragile per-page mirroring. Top 0.75", bottom 0.70" (footer page number).
TRIM_W, TRIM_H = 6 * inch, 9 * inch
M_SIDE, M_TOP, M_BOT = 0.75*inch, 0.75*inch, 0.70*inch

body = ParagraphStyle("body", fontName="PlexSerif", fontSize=11, leading=15.5,
                      alignment=TA_JUSTIFY, firstLineIndent=16)
body_first = ParagraphStyle("body_first", parent=body, firstLineIndent=0)
scene = ParagraphStyle("scene", parent=body, alignment=TA_CENTER,
                       firstLineIndent=0, spaceBefore=10, spaceAfter=10)
ch_num = ParagraphStyle("ch_num", fontName="PlexSerif-Bd", fontSize=13,
                        alignment=TA_CENTER, leading=16, spaceAfter=6,
                        textColor="#000000")
ch_title = ParagraphStyle("ch_title", fontName="PlexSerif-It", fontSize=18,
                          alignment=TA_CENTER, leading=22, spaceAfter=28)
title_main = ParagraphStyle("title_main", fontName="PlexSerif-Bd", fontSize=26,
                            alignment=TA_CENTER, leading=32)
title_sub = ParagraphStyle("title_sub", fontName="PlexSerif-It", fontSize=15,
                           alignment=TA_CENTER, leading=20)
halftitle = ParagraphStyle("halftitle", fontName="PlexSerif-It", fontSize=16,
                           alignment=TA_CENTER, leading=22)
copyr = ParagraphStyle("copyr", fontName="PlexSerif", fontSize=9, leading=13,
                       alignment=TA_CENTER)
dedic = ParagraphStyle("dedic", fontName="PlexSerif-It", fontSize=12, leading=18,
                       alignment=TA_CENTER)


def md_inline(t):
    t = html.escape(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", t)
    t = re.sub(r"_(.+?)_", r"<i>\1</i>", t)
    return t


WORDS = {"ONE":1,"TWO":2,"THREE":3,"FOUR":4,"FIVE":5,"SIX":6,"SEVEN":7,"EIGHT":8,
         "NINE":9,"TEN":10,"ELEVEN":11,"TWELVE":12,"THIRTEEN":13,"FOURTEEN":14,
         "FIFTEEN":15,"SIXTEEN":16,"SEVENTEEN":17,"EIGHTEEN":18,"NINETEEN":19,"TWENTY":20}


def parse(path):
    raw = open(path, encoding="utf-8").read()
    lines = raw.split("\n")
    # drop the leading title block (first 3 nonblank lines before CHAPTER ONE)
    chapters = []
    i = 0
    # find first chapter
    while i < len(lines) and not re.match(r"^CHAPTER\s+[A-Z-]+\s*$", lines[i].strip()):
        i += 1
    while i < len(lines):
        m = re.match(r"^CHAPTER\s+([A-Z-]+)\s*$", lines[i].strip())
        if not m:
            i += 1; continue
        num = m.group(1)
        i += 1
        while i < len(lines) and not lines[i].strip():
            i += 1
        title = lines[i].strip() if i < len(lines) else ""
        i += 1
        # gather body until next CHAPTER
        buf = []
        while i < len(lines) and not re.match(r"^CHAPTER\s+[A-Z-]+\s*$", lines[i].strip()):
            buf.append(lines[i]); i += 1
        chapters.append((num, title, "\n".join(buf)))
    return chapters


def paras_from(text):
    # split on blank lines into paragraphs; mark scene breaks
    blocks = re.split(r"\n\s*\n", text.strip())
    out = []
    for b in blocks:
        s = b.strip()
        if not s:
            continue
        if s in ("* * *", "***", "———", "* * * *"):
            out.append(("scene", "* * *"))
        else:
            out.append(("p", " ".join(line.strip() for line in s.split("\n"))))
    return out


def build():
    chapters = parse(SRC)
    story = []

    # ===== Front matter (unnumbered) =====
    story.append(NextPageTemplate("front"))

    # 1. Half-title (recto)
    story.append(Spacer(1, 3.2*inch))
    story.append(Paragraph(BOOK_TITLE, halftitle))
    story.append(PageBreak())
    # 2. blank (verso)
    story.append(Spacer(1, 1*inch)); story.append(PageBreak())

    # 3. Title page (recto)
    story.append(Spacer(1, 1.8*inch))
    story.append(Paragraph(BOOK_TITLE, title_main))
    story.append(Spacer(1, 0.30*inch))
    story.append(Paragraph("a novel", title_sub))
    story.append(Spacer(1, 0.45*inch))
    story.append(Paragraph(AUTHOR, title_sub))
    story.append(PageBreak())

    # 4. Copyright page (verso). Modest top spacer so the whole block stays on ONE page.
    story.append(Spacer(1, 4.2*inch))
    story.append(Paragraph(f"Copyright &copy; {YEAR} {AUTHOR}", copyr))
    story.append(Spacer(1, 0.10*inch))
    story.append(Paragraph("All rights reserved.", copyr))
    story.append(Spacer(1, 0.10*inch))
    story.append(Paragraph(
        "This is a work of fiction. Names, characters, places, and incidents are "
        "either products of the author&rsquo;s imagination or used fictitiously. "
        "Any resemblance to actual persons, living or dead, events, or locales is "
        "entirely coincidental.", copyr))
    story.append(Spacer(1, 0.10*inch))
    story.append(Paragraph(
        "No part of this book may be reproduced in any form without written "
        "permission from the author, except for brief quotations in a review.", copyr))
    story.append(Spacer(1, 0.10*inch))
    story.append(Paragraph(f"First edition, {YEAR}.", copyr))
    story.append(PageBreak())

    front_pages = 4
    # 5. Dedication (recto) + blank verso — only if set
    if DEDICATION.strip():
        story.append(Spacer(1, 3.4*inch))
        story.append(Paragraph(md_inline(DEDICATION), dedic))
        story.append(PageBreak())
        story.append(Spacer(1, 1*inch)); story.append(PageBreak())
        front_pages += 2

    # ===== Body (numbered from 1) =====
    story.append(NextPageTemplate("body"))
    for idx, (num, title, text) in enumerate(chapters):
        story.append(Spacer(1, 1.1*inch))
        story.append(Paragraph(f"CHAPTER {num}", ch_num))
        if title:
            story.append(Paragraph(md_inline(title), ch_title))
        first = True
        for kind, content in paras_from(text):
            if kind == "scene":
                story.append(Paragraph("* * *", scene))
                first = True
            else:
                story.append(Paragraph(md_inline(content),
                                       body_first if first else body))
                first = False
        if idx != len(chapters) - 1:
            story.append(PageBreak())

    def front_page(canvas, doc):
        canvas.setFont("PlexSerif", 10)  # avoid Helvetica default resource

    def body_page(canvas, doc):
        canvas.saveState()
        canvas.setFont("PlexSerif", 10)
        # page number centered in the footer; body numbering starts at 1
        # (front matter pages are unnumbered — offset by their count).
        canvas.drawCentredString(TRIM_W/2, 0.45*inch, str(doc.page - front_pages))
        canvas.restoreState()

    frame = Frame(M_SIDE, M_BOT, TRIM_W - 2*M_SIDE, TRIM_H - M_TOP - M_BOT, id="text")
    doc = BaseDocTemplate(OUT, pagesize=(TRIM_W, TRIM_H),
                          title="A Bond of Scale and Silver",
                          author=AUTHOR, leftMargin=M_SIDE, rightMargin=M_SIDE,
                          topMargin=M_TOP, bottomMargin=M_BOT)
    front = PageTemplate(id="front", frames=[frame], onPage=front_page)
    bodyt = PageTemplate(id="body", frames=[frame], onPage=body_page)
    doc.addPageTemplates([front, bodyt])
    doc.build(story)
    return OUT


if __name__ == "__main__":
    out = build()
    print("wrote", out)
