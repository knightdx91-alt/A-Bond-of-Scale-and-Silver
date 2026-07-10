#!/usr/bin/env python3
"""
Build a reflowable EPUB 3 of *A Bond of Scale and Silver* (no external deps).

Source: manuscript/full-manuscript.md (title / author / CHAPTER X / title / body).
Output: delivery/production/A-Bond-of-Scale-and-Silver.epub

Includes: cover image, nav (EPUB3) + NCX (EPUB2 fallback), title page, copyright,
dedication, and one XHTML document per chapter. Scene breaks ("* * *") are rendered
as centered dividers. Validates structurally (correct mimetype-first zip, container,
OPF manifest/spine, nav). Kindle/Apple/Kobo + IngramSpark ebook channel compatible.
"""
import os, re, html, zipfile, datetime, uuid

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "manuscript", "full-manuscript.md")
COVER = os.path.join(ROOT, "delivery", "cover", "front-cover-post-peleos.png")
OUT = os.path.join(ROOT, "delivery", "production", "A-Bond-of-Scale-and-Silver.epub")

BOOK_TITLE = "A Bond of Scale and Silver"
AUTHOR = "Post Peleos"
YEAR = "2026"
LANG = "en"
DEDICATION = "For all the ones that were told to hide themselves from the world. We see you."
BOOK_UUID = "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_DNS, "abondofscaleandsilver.postpeleos"))


def esc(t):
    return html.escape(t, quote=False)


def md_inline(t):
    t = esc(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", t)
    t = re.sub(r"_(.+?)_", r"<em>\1</em>", t)
    return t


def parse(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    chapters = []
    i = 0
    head = re.compile(r"^CHAPTER\s+([A-Z-]+)\s*$")
    while i < len(lines) and not head.match(lines[i].strip()):
        i += 1
    while i < len(lines):
        m = head.match(lines[i].strip())
        if not m:
            i += 1; continue
        num = m.group(1); i += 1
        while i < len(lines) and not lines[i].strip():
            i += 1
        title = lines[i].strip() if i < len(lines) else ""
        i += 1
        buf = []
        while i < len(lines) and not head.match(lines[i].strip()):
            buf.append(lines[i]); i += 1
        chapters.append((num, title, "\n".join(buf)))
    return chapters


def chapter_html(num, title, text):
    blocks = re.split(r"\n\s*\n", text.strip())
    parts = []
    first = True
    for b in blocks:
        s = b.strip()
        if not s:
            continue
        if s in ("* * *", "***", "———", "* * * *"):
            parts.append('<p class="scene">* * *</p>')
            first = True
            continue
        s = " ".join(ln.strip() for ln in s.split("\n"))
        cls = ' class="first"' if first else ""
        parts.append(f"<p{cls}>{md_inline(s)}</p>")
        first = False
    body = "\n".join(parts)
    head = f'<p class="chnum">CHAPTER {esc(num)}</p>'
    if title:
        head += f'\n<h1 class="chtitle">{md_inline(title)}</h1>'
    else:
        head += ""
    return XHTML.format(title=esc(f"Chapter {num}"), body=head + "\n" + body)


XHTML = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en" xml:lang="en">
<head><meta charset="utf-8"/><title>{title}</title>
<link rel="stylesheet" type="text/css" href="../css/style.css"/></head>
<body>
{body}
</body>
</html>
"""

CSS = """@page { margin: 0; }
html, body { margin: 0; padding: 0; }
body { font-family: "Iowan Old Style", "Palatino", Georgia, serif;
       line-height: 1.5; text-align: justify; hyphens: auto;
       padding: 0 1.2em; }
p { margin: 0; text-indent: 1.3em; }
p.first { text-indent: 0; }
p.scene { text-indent: 0; text-align: center; margin: 1.1em 0; letter-spacing: .3em; }
p.chnum { text-indent: 0; text-align: center; font-variant: small-caps;
          letter-spacing: .18em; margin: 3em 0 0.2em; font-weight: bold; }
h1.chtitle { text-indent: 0; text-align: center; font-style: italic; font-weight: normal;
             font-size: 1.5em; margin: 0 0 1.6em; line-height: 1.25; }
/* front matter */
.center { text-align: center; text-indent: 0; }
.cover-wrap { margin: 0; padding: 0; text-align: center; }
.cover-wrap img { max-width: 100%; height: auto; }
.title-main { text-align: center; text-indent: 0; font-size: 2em; font-weight: bold;
              margin: 3em 0 0.3em; line-height: 1.2; }
.title-sub { text-align: center; text-indent: 0; font-style: italic; margin: 0.2em 0; }
.dedication { text-align: center; text-indent: 0; font-style: italic; margin: 6em 1.5em 0; }
.copyright { text-align: center; text-indent: 0; font-size: 0.85em; margin: 0.6em 1.5em; }
.copyright.top { margin-top: 8em; }
"""


def wrap_page(title, body):
    return XHTML.format(title=esc(title), body=body)


def main():
    chapters = parse(SRC)
    now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # ---- front-matter documents ----
    cover_xhtml = wrap_page("Cover",
        '<div class="cover-wrap"><img src="../images/cover.png" alt="Cover"/></div>')
    title_xhtml = wrap_page("Title Page",
        f'<p class="title-main">{esc(BOOK_TITLE)}</p>'
        f'<p class="title-sub">a novel</p>'
        f'<p class="title-sub">{esc(AUTHOR)}</p>')
    copyright_xhtml = wrap_page("Copyright",
        f'<p class="copyright top">Copyright &#169; {YEAR} {esc(AUTHOR)}</p>'
        f'<p class="copyright">All rights reserved.</p>'
        f'<p class="copyright">This is a work of fiction. Names, characters, places, and '
        f'incidents are either products of the author&#8217;s imagination or used '
        f'fictitiously. Any resemblance to actual persons, living or dead, events, or '
        f'locales is entirely coincidental.</p>'
        f'<p class="copyright">No part of this book may be reproduced in any form without '
        f'written permission from the author, except for brief quotations in a review.</p>'
        f'<p class="copyright">First edition, {YEAR}.</p>')
    dedication_xhtml = wrap_page("Dedication",
        f'<p class="dedication">{md_inline(DEDICATION)}</p>') if DEDICATION.strip() else None

    # ---- assemble spine list ----
    docs = []  # (id, filename, xhtml, nav-title-or-None)
    docs.append(("cover", "text/cover.xhtml", cover_xhtml, None))
    docs.append(("titlepage", "text/titlepage.xhtml", title_xhtml, None))
    docs.append(("copyright", "text/copyright.xhtml", copyright_xhtml, None))
    if dedication_xhtml:
        docs.append(("dedication", "text/dedication.xhtml", dedication_xhtml, None))
    for idx, (num, title, text) in enumerate(chapters, 1):
        navtitle = f"Chapter {num.title()}" + (f" — {title}" if title else "")
        docs.append((f"chap{idx}", f"text/chapter-{idx:02d}.xhtml",
                     chapter_html(num, title, text), navtitle))

    # ---- nav.xhtml (EPUB3) ----
    # nav.xhtml lives in OEBPS/, chapters in OEBPS/text/ — link the full relative path
    nav_items = "\n".join(
        f'      <li><a href="{fn}">{esc(nt)}</a></li>'
        for (_id, fn, _x, nt) in docs if nt)
    nav_xhtml = (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<!DOCTYPE html>\n'
        '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en" xml:lang="en">\n'
        f'<head><meta charset="utf-8"/><title>{esc(BOOK_TITLE)}</title></head>\n'
        '<body>\n  <nav epub:type="toc" id="toc"><h1>Contents</h1>\n    <ol>\n'
        + nav_items +
        '\n    </ol>\n  </nav>\n</body>\n</html>\n')

    # ---- toc.ncx (EPUB2 fallback) ----
    navpoints = []
    for order, (_id, fn, _x, nt) in enumerate([d for d in docs if d[3]], 1):
        target = fn  # relative to OEBPS
        navpoints.append(
            f'    <navPoint id="np{order}" playOrder="{order}">\n'
            f'      <navLabel><text>{esc(nt)}</text></navLabel>\n'
            f'      <content src="{target}"/>\n    </navPoint>')
    ncx = (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">\n'
        f'  <head><meta name="dtb:uid" content="{BOOK_UUID}"/>\n'
        '    <meta name="dtb:depth" content="1"/>\n'
        '    <meta name="dtb:totalPageCount" content="0"/>\n'
        '    <meta name="dtb:maxPageNumber" content="0"/></head>\n'
        f'  <docTitle><text>{esc(BOOK_TITLE)}</text></docTitle>\n'
        f'  <docAuthor><text>{esc(AUTHOR)}</text></docAuthor>\n'
        '  <navMap>\n' + "\n".join(navpoints) + '\n  </navMap>\n</ncx>\n')

    # ---- content.opf ----
    manifest = [
        '    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
        '    <item id="css" href="css/style.css" media-type="text/css"/>',
        '    <item id="cover-image" href="images/cover.png" media-type="image/png" properties="cover-image"/>',
    ]
    spine = []
    for (_id, fn, _x, _nt) in docs:
        props = ' properties="svg"' if False else ''
        manifest.append(f'    <item id="{_id}" href="{fn}" media-type="application/xhtml+xml"/>')
        linear = "yes"
        spine.append(f'    <itemref idref="{_id}" linear="{linear}"/>')
    opf = (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="en">\n'
        '  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">\n'
        f'    <dc:identifier id="bookid">{BOOK_UUID}</dc:identifier>\n'
        f'    <dc:title>{esc(BOOK_TITLE)}</dc:title>\n'
        f'    <dc:creator id="creator">{esc(AUTHOR)}</dc:creator>\n'
        f'    <dc:language>{LANG}</dc:language>\n'
        f'    <dc:date>{YEAR}</dc:date>\n'
        f'    <dc:rights>Copyright &#169; {YEAR} {esc(AUTHOR)}. All rights reserved.</dc:rights>\n'
        f'    <meta property="dcterms:modified">{now}</meta>\n'
        '    <meta name="cover" content="cover-image"/>\n'
        '  </metadata>\n'
        '  <manifest>\n' + "\n".join(manifest) + '\n  </manifest>\n'
        '  <spine toc="ncx">\n' + "\n".join(spine) + '\n  </spine>\n'
        '</package>\n')

    container = (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">\n'
        '  <rootfiles>\n'
        '    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>\n'
        '  </rootfiles>\n</container>\n')

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    if os.path.exists(OUT):
        os.remove(OUT)
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        # mimetype MUST be first and STORED (uncompressed)
        z.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", container)
        z.writestr("OEBPS/content.opf", opf)
        z.writestr("OEBPS/nav.xhtml", nav_xhtml)
        z.writestr("OEBPS/toc.ncx", ncx)
        z.writestr("OEBPS/css/style.css", CSS)
        with open(COVER, "rb") as f:
            z.writestr("OEBPS/images/cover.png", f.read())
        for (_id, fn, xhtml, _nt) in docs:
            z.writestr("OEBPS/" + fn, xhtml)
    print("wrote", OUT, f"({len(chapters)} chapters)")


if __name__ == "__main__":
    main()
