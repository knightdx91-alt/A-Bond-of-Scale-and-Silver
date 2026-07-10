#!/usr/bin/env python3
"""
show_tell_check.py — draft-time show-vs-tell gate for the whole book.

The pipeline's standing failure mode: when a chapter runs short of the word
floor, the easy fill is REFLECTION (a character explaining what a moment meant)
instead of SCENE (dialogue, physical action, sensory event). That reads as
telling, and it compounds into "too descriptive / not enough showing." The
book-evaluator keeps catching it downstream, at polish. This catches it at draft.

It measures four telling-signals per chapter and flags the worst paragraphs so
you can convert them to scene BEFORE the gate, not after:

  1. DIALOGUE SHARE — % of words inside quotes. Very low = a chapter with no
     one talking, usually pure interiority. (Not a hard rule; set-pieces run low.)
  2. FILTER VERBS — "he felt / knew / realized / understood / saw / noticed /
     sensed / thought / seemed / was aware." These narrate an experience at one
     remove instead of rendering it. Rate per 1,000 words.
  3. ABSTRACTION / MEANING-MARKERS — "it was the kind/sort/shape/thing of...",
     "the fact that", "which was", "meant that", "the truth was", plus aphoristic
     present-tense generalizations ("a man could...", "the way you..."). This is
     the narrated-meaning tic.
  4. NAMED EMOTION — "felt grief/relief/shame/fear/..." (naming the feeling
     instead of showing it in the body). Bishop's #1 rule is the opposite.

It also flags SCENE-END CODAS: the last paragraph of a scene/chapter that is
pure interiority (no dialogue, no concrete action) — the "here's what it all
meant" summary that should usually be cut or dramatized.

HEURISTIC, not truth. A flagged paragraph might be earned Bishop deep-POV shown
in the body — read it before cutting. The point is a draft-time smoke alarm.

Thresholds (per 1,000 words) are advisory WARN lines, tuned to this book's
Bishop register (deep POV legitimately runs some interiority):
    filter verbs   > 9.0     -> heavy
    abstraction    > 6.0     -> heavy
    named emotion  > 2.5     -> heavy
    dialogue share < 8%      -> note (single-POV set-piece; check it earns it)
A chapter with 2+ heavies is worth a convert-to-scene pass.

Usage:
    python3 tools/show_tell_check.py                 # whole book, summary + flags
    python3 tools/show_tell_check.py 8               # one chapter, verbose
"""
import re, sys, glob, os

HERE = os.path.dirname(__file__)
CHAP_DIR = os.path.join(HERE, '..', 'manuscript', 'chapters')

FILTER = re.compile(r"\b(felt|feel|feels|knew|know(?:s)?|realized|realize|understood|"
                    r"understand(?:s)?|noticed|notice(?:s)?|sensed|sense(?:s)?|thought|"
                    r"seemed|seem(?:s)?|was aware|were aware|found (?:that|himself|herself)|"
                    r"could tell|watched (?:himself|herself))\b", re.I)

ABSTRACT = re.compile(
    r"\bit was the (?:kind|sort|shape|thing|whole|way|only|worst|first|most)\b"
    r"|\bthe (?:fact|truth|thing|shape|whole) (?:that|of|was|is)\b"
    r"|\bwhich was\b|\bmeant that\b|\bwhat it meant\b|\bthe point (?:was|of)\b"
    r"|\bthat was the (?:shape|thing|whole|truth|point|part)\b"
    r"|\bthe (?:kind of|sort of) (?:thing|man|woman|person|look)\b"
    r"|\bfor the first time\b|\bnot because\b.*\bbut because\b", re.I)

# aphoristic present-tense generalization ("a man could...", "the way you...", gnomic)
APHORISM = re.compile(
    r"\b(a man|a woman|a person|a chief|a girl|a boy|a queen|you)\b\s+"
    r"(?:could|will|would|does|do|learns?|learn|is|are|never|always|has to|must)\b", re.I)

NAMED_EMO = re.compile(
    r"\b(felt|feeling|feel|with)\s+(?:a\s+|the\s+|only\s+|pure\s+|)?"
    r"(grief|relief|shame|fear|joy|anger|rage|love|dread|sorrow|terror|"
    r"guilt|despair|hope|longing|panic|pity)\b", re.I)

# concrete-action signal: past-tense physical verbs (rough) — used to judge codas
ACTION = re.compile(r"\b(stood|sat|walked|turned|ran|reached|took|pulled|pushed|"
                    r"dropped|lifted|struck|threw|caught|stepped|knelt|rose|leaned|"
                    r"put|set|held|grabbed|opened|closed|moved|crossed|handed|"
                    r"looked|touched|drew|shoved|kicked|climbed|fell|knocked)\b", re.I)

def paragraphs(text):
    text = re.sub(r'(?m)^#.*$', '', text)
    return [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]

def has_dialogue(p):
    return '"' in p or '“' in p or '”' in p

def wc(s):
    return len(re.findall(r"\S+", s))

def analyze(text):
    paras = paragraphs(text)
    words = wc(text)
    dwords = sum(len(d.split()) for d in re.findall(r'"([^"]*)"', text))
    filt = len(FILTER.findall(text))
    abst = len(ABSTRACT.findall(text)) + len(APHORISM.findall(text))
    emo  = len(NAMED_EMO.findall(text))
    r = lambda n: 1000.0 * n / words if words else 0
    # per-paragraph tell-score for flagging
    scored = []
    for i, p in enumerate(paras):
        if has_dialogue(p):
            continue
        pw = wc(p)
        if pw < 40:
            continue
        f = len(FILTER.findall(p)); a = len(ABSTRACT.findall(p)) + len(APHORISM.findall(p))
        e = len(NAMED_EMO.findall(p)); act = len(ACTION.findall(p))
        # interiority density minus concrete grounding
        score = (f + a + 1.5*e) - 0.5*act
        coda = (i == len(paras)-1) or (i < len(paras)-1 and not has_dialogue(paras[i+1]) and False)
        scored.append((score, i, pw, f, a, e, act, coda, p))
    return dict(words=words, dialogue=100.0*dwords/words if words else 0,
               filter=r(filt), abstract=r(abst), emo=r(emo), scored=scored,
               ncodas=sum(1 for s in scored if s[7]))

TH = dict(filter=9.0, abstract=6.0, emo=2.5, dialogue=8.0)

def heavies(m):
    h = []
    if m['filter']   > TH['filter']:   h.append('filter')
    if m['abstract'] > TH['abstract']: h.append('abstract')
    if m['emo']      > TH['emo']:      h.append('emo')
    return h

def main():
    files = sorted(glob.glob(os.path.join(CHAP_DIR, 'chapter-*.md')),
                   key=lambda f: int(re.search(r'(\d+)', os.path.basename(f)).group(1)))
    one = sys.argv[1] if len(sys.argv) > 1 else None
    if one:
        files = [f for f in files if re.search(r'(\d+)', os.path.basename(f)).group(1) == one]
    print("="*78)
    print("SHOW-vs-TELL CHECK  (rates per 1,000 words; heuristic smoke alarm)")
    print(f"  WARN lines: filter>{TH['filter']}  abstract>{TH['abstract']}  "
          f"named-emotion>{TH['emo']}  dialogue<{TH['dialogue']}%")
    print("="*78)
    print(f"{'chapter':12} {'wds':>5} {'dlg%':>5} {'filter':>7} {'abstr':>6} {'emo':>5}  flags")
    worst = []
    for f in files:
        m = analyze(open(f).read())
        h = heavies(m)
        flag = ",".join(h) if h else "-"
        if m['dialogue'] < TH['dialogue']:
            flag += (" " if flag != "-" else "") + f"[dlg {m['dialogue']:.0f}%]"
        n = os.path.basename(f)
        mark = "  <<" if len(h) >= 2 else ""
        print(f"{n:12} {m['words']:5} {m['dialogue']:5.1f} {m['filter']:7.1f} "
              f"{m['abstract']:6.1f} {m['emo']:5.1f}  {flag}{mark}")
        for s in m['scored']:
            worst.append((s[0], n, s))
    # top offending paragraphs, book-wide
    print("\nTop telling-heavy paragraphs (convert to scene, or cut the coda):")
    worst.sort(key=lambda x: -x[0])
    for score, n, s in worst[:12 if not one else 20]:
        _, i, pw, fN, aN, eN, act, coda, p = s
        tag = "CODA " if coda else "     "
        snip = re.sub(r'\s+', ' ', p)[:120]
        print(f"  {tag}{n} ¶{i:<3} score {score:4.1f} (filter {fN} abstr {aN} emo {eN} action {act}, {pw}w)")
        print(f"        {snip}…")
    print("\nGuidance: 2+ heavies on a chapter = do a convert-to-SCENE pass "
          "(dialogue / physical action / sensory beat), not more reflection.")
    print("A CODA paragraph that is pure interiority usually wants cutting or "
          "dramatizing — end scenes on image/action/line, not on 'what it meant.'")

if __name__ == '__main__':
    main()
