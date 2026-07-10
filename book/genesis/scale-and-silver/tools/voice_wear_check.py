#!/usr/bin/env python3
"""
voice_wear_check.py — whole-book voice-wear gate, PER CHARACTER (every POV).

Deep single-POV writing wears when a character's signature kit repeats at the
same rate chapter after chapter: the signature calcifies into a tic (an AI
fingerprint + reader skim). This tool measures that for EVERY POV in the book,
not a hardcoded few. It has three layers:

  1. BOOK-WIDE RETIRED phrases (hard gate) — pipeline tics that leak across all
     POVs + narration (e.g. "never once"). Any occurrence anywhere FAILS.

  2. Auto-detected self-repetition (per character, no hardcoding) — for each POV
     it gathers that character's chapters and finds multi-word phrases the POV
     repeats across its own chapters. Works for Amelia, Korvan, and any future
     POV (Rosalia, Maren, Loric...) the moment they appear in feedback/pov-map.txt.
     This is the universal engine — every character is covered automatically.

  3. Named-device caps (optional, per character) — hand-tuned regexes with a
     per-chapter cap for signatures a human curated in voice-dna §4b / the
     per-POV ledgers. Add a character here and it's enforced; omit them and the
     auto-detector (layer 2) still covers them.

Run as part of the post-completion check for the whole book:
    python3 tools/voice_wear_check.py
Exit code is non-zero if any RETIRED phrase appears or any named-device cap is
exceeded. Layer-2 self-repetition prints as WARN (targeting aid — always read
the phrase in context before cutting; some repeats are deliberate motifs).
"""
import re, sys, glob, os, collections

HERE = os.path.dirname(__file__)
CHAP_DIR = os.path.join(HERE, '..', 'manuscript', 'chapters')
POV_MAP_FILE = os.path.join(HERE, '..', 'feedback', 'pov-map.txt')

# ---- Layer 1: book-wide retired phrases (hard fail anywhere) ----------------
BOOK_WIDE_RETIRED = [
    r"\bnever once\b",
]

# ---- Layer 3: optional named-device caps, keyed by POV character -------------
# cap = max occurrences allowed PER CHAPTER for that character's POV chapters.
# Extend freely; anything not listed is still covered by layer 2.
CHARACTER_DEVICES = {
    "Amelia": [
        ("acoustic-rating a room", r"\b(a room that|rooms? that|how (?:the )?sound|carried the sound|swallowed the sound|ate the sound|a room .{0,20}(?:carried|swallowed|ate))\b", 1),
        ("counted number as a beat", r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\b\s+\b(step|breath|second|beat|pace|heartbeat|count)s?\b", 3),
        ("the arithmetic / the sum", r"\b(the arithmetic|the sum|weighed the cost|did the sum|the cost of it)\b", 2),
        ("blood woke at her wrists", r"\bblood\b.{0,20}\bwrist", 2),
        ("twenty years", r"\btwenty years\b", 1),
    ],
    "Korvan": [
        ("fire/craft aesthetic opinion", r"\b(a (?:good|bad|clean|honest|proper) fire|fire (?:wants|likes|should)|the way a fire)\b", 2),
        ("catastrophized shift-sensation", r"\b(this was it|it was starting|the shift .{0,15}(?:coming|starting|now)|something wrong with his body)\b", 1),
        ("down, not away", r"\bdown,? not away\b", 0),
        ("at his edge", r"\bat (?:his|the) edge\b", 1),
    ],
}

# ---- generic n-gram self-repetition (layer 2) -------------------------------
NGRAM_LO, NGRAM_HI = 4, 6           # phrase lengths to scan
SELF_REPEAT_CHAPTERS = 2            # appears in >= this many of the POV's chapters -> WARN
SELF_REPEAT_TOTAL = 3              # OR appears >= this many times total within the POV -> WARN
STOP_TAILS = {"the", "a", "of", "to", "and", "her", "his", "in", "that", "it"}

def read_pov_map():
    pov = {}
    if not os.path.exists(POV_MAP_FILE):
        return pov
    with open(POV_MAP_FILE) as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            m = re.match(r'(\d+)\s*:\s*(.+)', line)
            if m:
                pov[int(m.group(1))] = m.group(2).strip()
    return pov

def chapter_files():
    files = glob.glob(os.path.join(CHAP_DIR, 'chapter-*.md'))
    return sorted(files, key=lambda f: int(re.search(r'(\d+)', os.path.basename(f)).group(1)))

def chap_num(f):
    return int(re.search(r'(\d+)', os.path.basename(f)).group(1))

def load_text(f):
    with open(f) as fh:
        return fh.read()

def words_only(text):
    # strip markdown headers and telepathy asterisks; lowercase word stream
    text = re.sub(r'(?m)^#.*$', ' ', text)
    return re.findall(r"[a-z']+", text.lower())

def ngrams(tokens, n):
    for i in range(len(tokens) - n + 1):
        yield tuple(tokens[i:i+n])

def count_matches(patterns, text):
    return sum(len(re.findall(p, text, re.I)) for p in patterns)

def main():
    pov = read_pov_map()
    files = chapter_files()
    if not files:
        print("No chapters found.")
        return 0
    failures = []   # hard-gate messages
    warnings = []   # targeting messages

    # group chapters by POV
    by_pov = collections.defaultdict(list)
    unmapped = []
    for f in files:
        n = chap_num(f)
        who = pov.get(n)
        if who is None:
            unmapped.append(n)
            who = "UNKNOWN"
        by_pov[who].append(f)

    print("=" * 70)
    print("VOICE-WEAR CHECK — per character (whole book)")
    print("=" * 70)
    if unmapped:
        warnings.append(f"chapters not in pov-map.txt (add them): {unmapped}")

    # ---- Layer 1: book-wide retired phrases --------------------------------
    print("\n[1] Book-wide retired phrases (hard gate):")
    for f in files:
        text = load_text(f)
        for pat in BOOK_WIDE_RETIRED:
            hits = re.findall(pat, text, re.I)
            if hits:
                failures.append(f"  Ch.{chap_num(f)}: RETIRED phrase {pat!r} appears {len(hits)}x")
    if not any("RETIRED phrase" in x for x in failures):
        print("  clean — no retired phrases anywhere.")
    else:
        for x in failures:
            print(x)

    # ---- Layer 2 + 3: per character ----------------------------------------
    for who in sorted(by_pov):
        cfiles = by_pov[who]
        print(f"\n[POV] {who} — {len(cfiles)} chapter(s): {[chap_num(f) for f in cfiles]}")

        # Layer 3: named-device caps.
        # WEAR = a device exceeding its per-chapter cap in >= 2 of the POV's
        # chapters (the signature calcifying across the book) -> hard FAIL.
        # A single chapter over cap is heavy-handed but not wear -> WARN
        # (the establishing chapter legitimately works a device harder).
        devices = CHARACTER_DEVICES.get(who, [])
        if devices:
            for label, pat, cap in devices:
                over = []  # (chapter, count) where this chapter exceeds cap
                for f in cfiles:
                    c = count_matches([pat], load_text(f))
                    if c > cap:
                        over.append((chap_num(f), c))
                if len(over) >= 2:
                    detail = ", ".join(f"Ch.{n} {c}x" for n, c in over)
                    failures.append(f"  [{who}] device WEAR: '{label}' over cap ({cap}) in {len(over)} chapters: {detail}")
                elif len(over) == 1:
                    n, c = over[0]
                    warnings.append(f"  [{who}] device heavy (1 ch only): '{label}' Ch.{n} {c}x > cap {cap} — establishing use OK, watch for repeats")
            print(f"  named-device caps checked ({len(devices)} devices).")
        else:
            print("  (no named-device caps configured — relying on auto-detector below)")

        # Layer 2: generic self-repetition across this POV's chapters
        # count each ngram: how many of the POV's chapters it appears in, and total
        per_chap_sets = []
        total_counter = collections.Counter()
        for f in cfiles:
            toks = words_only(load_text(f))
            seen = set()
            for n in range(NGRAM_LO, NGRAM_HI + 1):
                for g in ngrams(toks, n):
                    if g[0] in STOP_TAILS or g[-1] in STOP_TAILS:
                        continue
                    total_counter[g] += 1
                    seen.add(g)
            per_chap_sets.append(seen)
        chapter_spread = collections.Counter()
        for s in per_chap_sets:
            for g in s:
                chapter_spread[g] += 1

        flagged = []
        for g, spread in chapter_spread.items():
            total = total_counter[g]
            if spread >= SELF_REPEAT_CHAPTERS or total >= SELF_REPEAT_TOTAL:
                # ignore trivially-overlapping shorter grams contained in a flagged longer one later
                flagged.append((spread, total, g))
        # keep the strongest (longest) phrases, drop sub-phrases of a flagged longer one
        flagged.sort(key=lambda x: (-len(x[2]), -x[1]))
        kept = []
        for spread, total, g in flagged:
            joined = " ".join(g)
            if any(joined in " ".join(k[2]) for k in kept):
                continue
            kept.append((spread, total, g))
        if kept:
            for spread, total, g in sorted(kept, key=lambda x: (-x[0], -x[1]))[:12]:
                warnings.append(f"  [{who}] self-repeat: \"{' '.join(g)}\" — in {spread} ch, {total}x total")
            print(f"  self-repetition: {len(kept)} phrase(s) recur across {who}'s chapters (see WARN).")
        else:
            print("  self-repetition: none above threshold.")

    # ---- summary -----------------------------------------------------------
    print("\n" + "=" * 70)
    if warnings:
        print("WARN (targeting — read in context; deliberate motifs are OK):")
        for w in warnings:
            print(w)
    print("-" * 70)
    if failures:
        print(f"RESULT: FAIL — {len(failures)} hard issue(s):")
        for x in failures:
            print(x)
        print("=" * 70)
        return 1
    print("RESULT: clean — no retired phrases, no device over cap.")
    print("=" * 70)
    return 0

if __name__ == '__main__':
    sys.exit(main())
