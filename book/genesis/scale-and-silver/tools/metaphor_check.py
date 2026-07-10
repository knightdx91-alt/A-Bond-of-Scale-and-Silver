#!/usr/bin/env python3
"""
metaphor_check.py — the figurative-load + sentence-shape gate for
A Bond of Scale and Silver (Bishop register).

style_check.py only counts SIMILE markers (like / as if / as though). It is blind to:
  - bare METAPHOR (copular "X was a furnace", "the machine of himself", "gone to silver"),
  - "as ADJ as" similes and appositive image-nouns,
  - Bishop's plain-declarative SENTENCE SHAPE (median ~13 words; the long rolling
    and...and...and sentence is off-comp).

This tool detects figurative language by CONSTRUCTION (not by a bare noun list, which
false-positives on literal use), across six frames, and measures sentence shape.
Heuristic — read flags in context — but it surfaces drift no other gate sees.

Usage:
  python3 tools/metaphor_check.py            # whole book, summary table + flags
  python3 tools/metaphor_check.py <N>        # one chapter, verbose (lists the hits)
Ceilings (Bishop-calibrated; override with flags):
  --max-fig    figurative markers per 1,000 words        (default 6.0)
  --max-long   share of sentences over 40 words, percent (default 18.0)
"""
import re, sys, glob, argparse, statistics

# Vehicle lexicon: nouns that read as a figurative VEHICLE when used as a predicate,
# an "X of himself", an appositive, or a transformation target. Matched only inside a
# figurative frame below — never bare — so literal "the fire", "the stone" don't count.
VEHICLE = (r"furnace|machine|engine|forge|ember|coal|coin|disc|sail|wall|hound|leash|"
           r"beast|monster|weapon|blade|knife|spear|banner|chain|cage|muzzle|glacier|"
           r"ice|storm|tide|current|sea|ocean|well|mirror|mask|armour|armor|veil|"
           r"curtain|key|lock|anchor|road|scar|thread|knot|root|door|gate|shadow|"
           r"stone|iron|fire|flame|wolf|hare|bird|hand|fist|wave|ghost|island|ruin|"
           r"machine|smoke|ash|glass|metal|silver|light|dark|stain|wound|hole")
MATERIAL = r"silver|iron|metal|stone|fire|flame|ash|glass|ice|smoke|dark|light|water"

# "X of himself/herself/itself" possessive-abstraction metaphors. Exclude literal partitives.
LIT = {"length","rest","whole","edge","end","all","one","part","side","most","half",
       "middle","some","much","none","each","either","front","back","top","bottom",
       "size","shape","sort","kind","out","inside","insides","outside","depth","depths"}

FRAMES = {
    "simile-like":  re.compile(r"\b(like|as if|as though)\b", re.I),
    "simile-as-as": re.compile(r"\bas\s+\w+\s+as\s+(a|an|the|his|her|its|any)\b", re.I),
    "of-self":      re.compile(r"\bthe\s+(\w+)\s+of\s+(?:him|her|it)self\b", re.I),
    "copular":      re.compile(r"\b(was|were|is|are|been|become|became|becomes|becoming|"
                               r"seemed|felt like|looked|sounded)\s+(?:a|an|the)\s+("+VEHICLE+r")\b", re.I),
    "turned-into":  re.compile(r"\b(turn(?:ed|s|ing)?|gone|went|going|made it|made him|made her)\s+"
                               r"(?:it |them |her |him |his )?(?:in)?to\s+(?:a |an |the |the same )?("+MATERIAL+r"|"+VEHICLE+r")\b", re.I),
    "appositive":   re.compile(r"(?:,|—)\s+(?:a|an)\s+("+VEHICLE+r")\s+(?:of|with|in|that)\b", re.I),
}

def sentences(t):
    t = re.sub(r"\s+", " ", t)
    return [s for s in re.split(r"(?<=[.!?])\s+", t) if len(s.split()) > 1]

def clean(raw):
    t = re.sub(r"^#.*$", "", raw, flags=re.M)
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    return t.replace("*", "")

def scan(path):
    t = clean(open(path).read()); wc = len(t.split())
    hits, by = [], {}
    for name, rx in FRAMES.items():
        if name == "of-self":
            ms = [m for m in rx.findall(t) if m.lower() not in LIT]
        else:
            ms = rx.findall(t)
        by[name] = len(ms); hits += [(name, m) for m in ms]
    fig = sum(by.values())
    S = sentences(t); L = [len(s.split()) for s in S] or [0]
    over = [s for s in S if len(s.split()) > 40]
    return dict(wc=wc, by=by, fig=fig, hits=hits,
                fig1k=round(1000*fig/wc, 1) if wc else 0,
                med=int(statistics.median(L)), mean=round(statistics.mean(L), 1),
                nlong=len(over), plong=round(100*len(over)/len(S), 1) if S else 0,
                longest=sorted(over, key=lambda s: -len(s.split()))[:3])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter", nargs="?")
    ap.add_argument("--max-fig", type=float, default=6.0)
    ap.add_argument("--max-long", type=float, default=18.0)
    a = ap.parse_args()
    files = sorted(glob.glob("manuscript/chapters/chapter-*.md"),
                   key=lambda x: int(re.findall(r"\d+", x)[0]))
    if a.chapter:
        files = [f for f in files if re.findall(r"\d+", f)[0] == str(a.chapter)]
    print(f"{'ch':>3} {'wds':>5} {'fig/1k':>6} {'siml':>4} {'asas':>4} {'ofsf':>4} "
          f"{'copl':>4} {'into':>4} {'appo':>4} {'med':>4} {'mean':>5} {'%>40w':>6}  flags")
    fails = 0
    for f in files:
        n = int(re.findall(r"\d+", f)[0]); d = scan(f); b = d["by"]
        fl = []
        if d["fig1k"] > a.max_fig:  fl.append(f"FIG {d['fig1k']}>{a.max_fig}")
        if d["plong"] > a.max_long: fl.append(f"LONG {d['plong']}%>{a.max_long}")
        if fl: fails += 1
        print(f"{n:>3} {d['wc']:>5} {d['fig1k']:>6} {b['simile-like']:>4} "
              f"{b['simile-as-as']:>4} {b['of-self']:>4} {b['copular']:>4} "
              f"{b['turned-into']:>4} {b['appositive']:>4} {d['med']:>4} {d['mean']:>5} "
              f"{d['plong']:>6}  {'  '.join(fl) if fl else '-'}")
        if a.chapter:
            for name in ("of-self","copular","turned-into","appositive"):
                hh = [m for nm, m in d["hits"] if nm == name]
                if hh: print(f"   {name:11}: " + ", ".join(f'"{x}"' for x in hh))
            print("   3 longest sentences (split unless load-bearing):")
            for s in d["longest"]:
                print(f"     [{len(s.split())}w] {s[:88]}…")
    print("\nRESULT:", "clean." if not fails else f"{fails} chapter(s) over a ceiling.")
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
