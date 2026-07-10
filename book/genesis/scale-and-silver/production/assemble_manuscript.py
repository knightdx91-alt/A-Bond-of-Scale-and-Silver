#!/usr/bin/env python3
"""Assemble manuscript/full-manuscript.md from manuscript/chapters/chapter-*.md.

Adapted for *A Bond of Scale and Silver* (29 chapters). Book-specific vs. the
Saeren reference script:
  - 29 chapters; headings are "# Chapter <word|digit> — <Title>" (em-dash).
    Ch.14/15/16 use digits in-file; we normalize every chapter label to WORDS.
  - Title page: A BOND OF SCALE AND SILVER / a novel (standalone; no series line).
  - Scene breaks in-file are a mix of "*", "\\*", "---", and dash runs; all are
    normalized to a single centered "* * *".
  - Strips markdown "#" heads and HTML comments; collapses 4+ blank-line runs.
"""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH_DIR = os.path.join(ROOT, "manuscript", "chapters")
OUT = os.path.join(ROOT, "manuscript", "full-manuscript.md")

TITLE = "A BOND OF SCALE AND SILVER"
SERIES = "a novel"

NUMWORDS = {
    1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE", 6: "SIX", 7: "SEVEN",
    8: "EIGHT", 9: "NINE", 10: "TEN", 11: "ELEVEN", 12: "TWELVE",
    13: "THIRTEEN", 14: "FOURTEEN", 15: "FIFTEEN", 16: "SIXTEEN",
    17: "SEVENTEEN", 18: "EIGHTEEN", 19: "NINETEEN", 20: "TWENTY",
    21: "TWENTY-ONE", 22: "TWENTY-TWO", 23: "TWENTY-THREE",
    24: "TWENTY-FOUR", 25: "TWENTY-FIVE", 26: "TWENTY-SIX",
    27: "TWENTY-SEVEN", 28: "TWENTY-EIGHT", 29: "TWENTY-NINE",
}

HEAD_RE = re.compile(r"^#\s*Chapter\s+.+?\s+[—–-]\s+(.+?)\s*$", re.I)


def is_scene_break(line):
    s = line.strip()
    if not s:
        return False
    if re.fullmatch(r"\\?\*(\s*\*)*", s):       # *  \*  * *  * * *
        return True
    if re.fullmatch(r"[—–-]{3,}", s):            # --- or dash runs
        return True
    return False


def parse_chapter(path, num):
    lines = open(path, encoding="utf-8").read().splitlines()
    title = None
    body_start = 0
    for idx, ln in enumerate(lines):
        m = HEAD_RE.match(ln)
        if m:
            title = m.group(1).strip()
            body_start = idx + 1
            break
    if title is None:
        raise SystemExit(f"chapter {num}: could not parse heading in {path}")

    body = []
    for ln in lines[body_start:]:
        if re.match(r"^\s*<!--", ln):
            continue
        if re.match(r"^\s*\[END OF CHAPTER", ln, re.I):
            continue
        if ln.lstrip().startswith("#"):          # drop stray markdown heads
            continue
        body.append(ln)

    # normalize scene breaks and collapse blank runs
    out = []
    blanks = 0
    for ln in body:
        if is_scene_break(ln):
            while out and out[-1].strip() == "":
                out.pop()
            out.append("")
            out.append("* * *")
            out.append("")
            blanks = 0
            continue
        if ln.strip() == "":
            blanks += 1
            if blanks <= 1:
                out.append("")
            continue
        blanks = 0
        out.append(ln.rstrip())

    while out and out[0].strip() == "":
        out.pop(0)
    while out and out[-1].strip() == "":
        out.pop()

    label = f"CHAPTER {NUMWORDS[num]}"
    return f"{label}\n\n{title}\n\n" + "\n".join(out)


def main():
    paths = {}
    for p in glob.glob(os.path.join(CH_DIR, "chapter-*.md")):
        m = re.search(r"chapter-(\d+)\.md$", p)
        if m:
            paths[int(m.group(1))] = p
    nums = sorted(paths)

    parts = [f"{TITLE}\n\n{SERIES}\n"]
    for n in nums:
        parts.append(parse_chapter(paths[n], n))

    text = "\n\n\n".join(parts) + "\n"
    open(OUT, "w", encoding="utf-8").write(text)

    wc = len(re.findall(r"\S+", text))
    print(f"wrote {OUT}")
    print(f"chapters: {len(nums)} ({nums[0]}..{nums[-1]})")
    print(f"assembled word count: {wc}")


if __name__ == "__main__":
    main()
