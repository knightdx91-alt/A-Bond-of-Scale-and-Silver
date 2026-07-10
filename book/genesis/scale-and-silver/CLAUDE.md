# CLAUDE.md — A Bond of Scale and Silver

Per-book playbook. A fresh Claude Code session should read this first, then `STATE.yaml` and
`feedback/progress.md`. (Book slug `scale-and-silver`, was `rosalia`.)

> **REPO + BRANCH (2026-07-10):** This book's home is the standalone repo
> `knightdx91-alt/A-Bond-of-Scale-and-Silver`; work on **`main` only** (see root `CLAUDE.md` branch
> policy). The copy in `The-Saeren-Chronicles` is FROZEN. **`feedback/progress.md` → "▶ RESUME HERE"
> is the live pick-up point.** Book COMPLETE (29 ch) and **PRODUCTION + PACKAGING COMPLETE** (interior
> PDF 448 pp + X-1a, front matter + dedication, cover wrap, EPUB, editorial package — all on `main`).
> Only pre-print-order author/asset decisions remain (paper stock, ISBNs/barcode, printer ICC).

## What this is
A **genesis-from-idea** project: build a NEW ~150k-word **ADULT romantasy** from the author's
story bible (`research/story-bible.md`, pulled from Google Drive "Rosalia"), using the adapted
**Best Seller Studio** pipeline. There is NO original prose draft — the architect built
foundation + outline + voice-dna; next is the chapter loop.

**Voice comp = Anne Bishop, *The Black Jewels Trilogy*** (plain declarative prose, deep POV,
emotion shown in the body, menace/heat by restraint, dangerous-devoted lead). See `voice-dna.md`
+ `feedback/voice-comps-black-jewels.md`, and run `feedback/beta-lessons-checklist.md` per chapter.
Full settled decisions live in `STATE.yaml` (`resolved_author_decisions_2026_07_08`).

Git identity (so commits show verified):
```
git config user.email noreply@anthropic.com
git config user.name Claude
```

## Install the agents (fresh environment)
```
git clone https://github.com/felipelobomotta-blip/best-seller-studio /tmp/bss
cp /tmp/bss/agents/*.md ~/.claude/agents/
# Also install 4 skill-based roles as agents (add tools/model frontmatter):
#   entity-tracker, continuity-guardian (skills/optional/*/SKILL.md)
#   dialogue-polish, hook-craft        (skills/deprecated/*/SKILL.md)
# Frontmatter to prepend to each:
#   ---
#   name: <name>
#   description: <from SKILL.md>
#   tools: Read, Write, Edit, Grep, Glob, Bash
#   model: opus
#   maxTurns: 40
#   ---
```
Note: in some environments the Agent tool can't dispatch these named subagents. If so,
run ONE general-purpose agent that performs each role itself by reading ~/.claude/agents/*.md.

## Project layout
```
book/genesis/<slug>/
├── STATE.yaml                 # READ FIRST — project state, word/style gates, canon
├── research/                  # staged source: original-draft.txt + roadmap/bible/etc.
├── manuscript/chapters/       # chapter-1.md ... chapter-N.md (the book)
├── evaluations/               # per-chapter eval reports + continuity audits
├── feedback/progress.md       # exact resume point
└── tools/style_check.py       # style gate (edit ALLOWLIST for this book's motifs)
```

## How to continue
1. `cd book/genesis/<slug>` and read `STATE.yaml` and `feedback/progress.md`.
2. `ls manuscript/chapters/` and `git log --oneline` to find the last finalized chapter.
3. Produce the next chapter IN ORDER. Locate its material in `research/original-draft.txt`
   and REVISE/EXPAND to the roadmap beats — do not invent from scratch. Match the locked
   Ch.1 voice if one exists. Run each chapter through: write → dialogue-polish → hook-craft
   → disruptor → **pacing check** → evaluate → quality gate.
4. Commit per chapter: `git add -A && git commit -m "genesis: finalize chapter N"`.

## Quality gates (ALL must pass before a chapter is "done")

> **RUN THEM ALL WITH ONE COMMAND — do this every chapter, no exceptions:**
> ```
> bash tools/check_chapter.sh <N>
> ```
> It runs style (too-flowery), grammar (hard), rhythm, show/tell (too-descriptive — chapter
> row AND book-wide heavies), voice-wear, **metaphor/sentence-shape**, and the word floor, and
> prints a checklist reminder for the two judgement gates (Genesis Floor ≥ 8.5 and the pacing
> check). Never eyeball a subset.
>
> **Metaphor + sentence-shape gate (`tools/metaphor_check.py`).** `style_check.py` only counts
> SIMILE markers (like / as if / as though); it is blind to bare METAPHOR ("the furnace of himself",
> "a black coin") and to Bishop's plain SENTENCE SHAPE. This tool measures combined figurative load
> (≤4.0/1k) and the share of sentences over 40 words (≤18% — Bishop is clipped; the long rolling
> and…and…and sentence is off-comp). Ch.1 benchmark ≈11% long; if a chapter drifts toward ~25%, do a
> sentence-splitting pass (split the longest, vary openers so you don't trade long-sentences for
> anaphora). Legacy Ch.5/11/12 predate this tool and still sit over the long-% ceiling.
> For show/tell, read BOTH the chapter summary row (the `flags` column) AND the book-wide
> "top telling-heavy paragraphs" list — a chapter can pass the row while still owning a heavy
> paragraph worth a convert-to-scene pass.

- **Genesis Floor ≥ 8.5** (book-evaluator); below → book-editor polish loop (max 5).
- **PACING CHECK — required after EVERY chapter.** Assess pacing in context of neighbors:
  scene-vs-summary balance (sag/rush?), dialogue share, the emotional-arc slot (right high/low
  for its place — see foundation.md), hook-and-pull, and chapter length vs. adjacent chapters
  (no chapter >2× another). Log a one-line verdict in `evaluations/` + `feedback/progress.md`;
  fix via book-editor/disruptor BEFORE finalizing.
- **Style check** — `python3 tools/style_check.py` clean (calibrated to Bishop): simile ≤3/1k,
  **em-dash ≤ 10 per chapter**, adverbs ALLOWED (≤20/1k — Bishop uses them; do NOT strip),
  no NEW cross-chapter repeated phrase (ALLOWLIST is empty by design — no motifs), tics under
  ceiling. Avoid semicolons.
- **Grammar gate (HARD)** — `python3 tools/grammar_check.py` must report `RESULT: clean`.
- **Rhythm** — `python3 tools/rhythm_check.py` (no flat triplets / unsanctioned anaphora);
  `tools/tic_report.py` reports overused constructions.
- **Beta-lessons** — run `feedback/beta-lessons-checklist.md` per chapter (name the referent;
  show emotion in the body; split over-packed sentences; unambiguous dialogue attribution).
- **Log every flag** in `feedback/style-flags.md`; if a phrase is flagged 3+ times, add it to a
  "watch / kill" list (there are no deliberate motifs to promote in this book).

## Show-vs-tell gate (run EVERY chapter — the pipeline's standing weakness)
The recurring drift in this book is **telling over showing**: when a chapter is short of the word
floor, the easy fill is a REFLECTION paragraph (the POV explaining what a moment meant) instead of
new SCENE. It compounds into "too descriptive." Catch it at draft time:
```
python3 tools/show_tell_check.py            # whole book
python3 tools/show_tell_check.py N          # one chapter, verbose
```
- Watch **filter-verb rate** (he felt/knew/realized/understood/saw), **abstraction/meaning-markers**,
  **named-emotion**, and **dialogue share**. 2+ heavies on a chapter = do a **convert-to-SCENE pass**.
- **HARD RULE when a chapter is short: add SCENE — a line of dialogue, a physical action, a sensory
  beat — NEVER a reflection paragraph.** Same word count, real showing.
- **Ration scene-end codas.** Do not close a scene on a "here's what it all meant" summary; end on
  image, action, or a line of dialogue. Show emotion in the body (Bishop rule), don't name it.

## Whole-book completion check (run after the last chapter is finalized)
Before the book is called done, run the book-wide **voice-wear gate** over the full manuscript —
it measures signature-device calcification PER CHARACTER (every POV, not a hardcoded few):
```
python3 tools/voice_wear_check.py            # exits non-zero on real wear
```
- Keep `feedback/pov-map.txt` current (one `chapter: character` line each) — the tool uses it to
  group chapters by POV, so every character is covered automatically as new POVs appear.
- **Hard FAIL** = a book-wide retired phrase anywhere (e.g. "never once"), or a named signature
  device (voice-dna §4b) exceeding its per-chapter cap in **≥2 chapters** of one POV (calcification).
- **WARN** = a device heavy in a single (usually establishing) chapter, or an auto-detected phrase
  a POV self-repeats across its own chapters. Read each in context — deliberate motifs are fine;
  cut the accidental ones. Per-POV ledgers: `feedback/{amelia,korvan}-voice-ledger.md`.

## Recurring craft mistakes — NEVER repeat (read before drafting every chapter)

Ported from an earlier calibration (reviewer Eilidh Locherty's line-edit + Dana Flanders'
developmental notes; see `feedback/beta-lessons-checklist.md`), adapted for this adult/Bishop
book. The root habit to avoid: **prose that serves atmosphere at the expense of the reader's
plain comprehension.** The fix is Bishop's register — clarify without flattening.

**A. Structural / over-narration (the big one):**
1. **Over-packed sentences** — find the 3 longest sentences per scene and SPLIT at least one
   unless deliberately load-bearing (Bishop median ≈ 13 words). "We don't need to say everything."
2. **Vague poetic reaches** — every "she knew / something / deep water"-type phrase must name
   what it refers to, or be cut. If a reader can ask "knew WHAT?", fix it. (Beta note #1.)
3. **Cleverness over clarity** — any joke/wordplay gets one plain re-read; if a smart reader has
   to reparse it, rewrite it.
4. **Unmarked scene/time jumps** — signal every time/place jump explicitly.
5. **Name emotion → SHOW it in the body instead** (Bishop's #1 trait; beta note #2). Held breath,
   locked hands, a dropped stomach — not "a wave of grief."

**B. Line-craft tics:**
6. **Tense drift** — hold the tense (simple-past vs past-perfect).
7. **Connective monotony** — don't lean on `then`/`while`; vary.
8. **Adverbs are ALLOWED (Bishop)** — but where a shown action is clearly stronger than an
   `-ly` tell, prefer the action. Do NOT blanket-strip adverbs.
9. **Agreement & dangling modifiers** — every opening modifier attaches to a clear subject.
10. **Dialogue attribution** — decide "Korvan" vs "her father" and HOLD it; never double a name;
    make every speaker unambiguous.

**MECHANICAL GATE (enforced, not just intended):** per chapter, alongside `style_check.py`:
- `python3 tools/grammar_check.py` → must report `RESULT: clean` (doubled words, space-before-
  punctuation, a/an — exits non-zero on any). It also reports the 3 longest sentences (use for A.1).
- Optional tier 2 (tense/agreement/dangling via LanguageTool, non-gating):
  `python3 tools/grammar_check.py --file manuscript/chapters/chapter-N.md --languagetool`.

## Word floor
Finished book ≥ `manuscript_min_words` (see STATE.yaml). Verify:
`wc -w manuscript/chapters/chapter-*.md`. If short, expand the thinnest chapters.

## Canon guardrails (settled author decisions — never violate)
- Spelling is **magyk** (not magic) for the in-world power.
- **Vampires** descend from Atlanteans (a failed disease-cure experiment); feudal "protection"
  pact over humans; ruled by a **Queen** with **blood magyk**.
- **The Queen's name is ROSALIA** (Amelia's mother). "Rosalia" is a CHARACTER name, not the
  world/series name; the book's title is *A Bond of Scale and Silver*.
- **Amelia has SILVER HAIR** (cold near-grey; do NOT use 'silver-blonde') and is **NOT a
  victim** — strong inherited blood magyk; hunted because dangerous/valuable, never rescued.
- **Korvan** is dangerous-but-devoted (Bishop's Daemon technique): lethal as the dragon, gentle
  with Amelia; the narration carries the cold undertone while his actions are tender.
- **Shifters**: human until the first full moon AFTER their coming-of-age; first shift assigns
  them to their animal's clan; ancestral memory trickles in **situationally** (never one info
  dump); all clans under a single **chief**. Most shift on time; **late/anomalous shifters are
  rare and stigmatized** — Korvan is one.
- **The Treaty**: no NEW vampires may be made; silent on natural-born vampires (thought impossible).
- **Amelia**: Queen's daughter, first natural-born vampire in millennia, inherited blood magyk;
  hidden her whole life; want = to exist openly. No proof exists she's born vs made.
- **Korvan**: chief's son, **~19-20**, a rare LATE shifter still UNSHIFTED at the banquet (an
  outsider ache, not a teenager); first shift on the journey home (calendar coincidence, NOT
  magically triggered) → a **dragon**, a clan of one.
- **Loric**: shifter whose father the Queen killed in the last war; motive is emotional (wants
  the Queen to SUFFER); cannot be bought; exposes Amelia publicly so the chief loses either way.
- **CATEGORY (recat 2026-07-08):** **ADULT romantasy** (was NA). Leads ~19-22. Heat =
  **explicit/spicy, TWO scenes** (Ch.18 ~62% + reunion Ch.26 ~90%), earned. **Dark intensity but
  NO sexual violence** — cut the camera on the worst acts (Bishop models this).
- **Structure (reworked 2026-07-08):** single ~150k novel; **FORCED PROXIMITY + court cutaways**
  (leads earn each other on the road; Queen/Maren carry the court thread), under 4 anti-Twilight/
  R&J guardrails (bond = shared exile not fated-mates; war's cause on Loric not their love; adult
  register no damsel; proximity adversarial + costly). Amelia's cage-reason EXPIRES at the war
  declaration. Dragon memory does NOT link to Atlantis; the Queen does NOT remember killing
  Loric's father.

## Author decisions — RESOLVED (see STATE.yaml resolved_author_decisions_* for the full list)
- Korvan: only child, mother dead. Chief KNOWS the bond was genuine (allows the propaganda).
  Korvan carries the garden meeting ALONE. Maren confirmed. See STATE.yaml for the 2026-07-08 rework.

## Status (update as you go)
- **2026-07-10 — ✅ PRODUCTION + PACKAGING COMPLETE (all on `main`).** Cover decided
  (`delivery/cover/front-cover-post-peleos.png` + `…-clean.png`). Interior assembled + built:
  `A-Bond-of-Scale-and-Silver-6x9-interior.pdf` (**448 pp**) + PDF/X-1a CMYK, fonts embedded. Front
  matter added (half-title, title page w/ **Post Peleos**, copyright, **dedication**: "For all the ones
  that were told to hide themselves from the world. We see you."). Full cover **wrap** built (spine
  1.120" @ 448 pp cream 50#) + X-1a. **EPUB 3** built + validated. Editorial package incl.
  `beta-reader-pitch.md`. Standalone; no series line; no in-interior heat advisory. Build scripts:
  `production/{build_pdf,build_epub,compose_wrap,assemble_manuscript}.py`. Remaining = pre-print-order
  author/asset calls only (paper stock → spine factor; ISBNs + real barcode; printer ICC). See
  `production/PRODUCTION-PLAYBOOK.md` + `feedback/progress.md`.
- **2026-07-10 — ✅ BOOK ONE COMPLETE + FULLY AUDITED. ALL 29 of 29 chapters FINALIZED (Ch.1–29,
  every Genesis Floor ≥ 8.5). 152,116 words** (clears the 140k floor and the 150k target). Climax +
  resolution done: Ch.27 'Outlasted (I)' [K] (avg 8.86), Ch.28 'Outlasted (II)' [A] (avg 8.71) —
  Loric outlasted, Queen Rosalia + Maren die in one blow, reader-only reveal (Queen dies never
  knowing his name), Amelia takes the throne; Ch.29 'What We Choose' [A, K coda] (avg 8.86, 5 dims
  at 9.0) — coronation as want-granted-new-cage w/ the Ch.1 bookend, inherit-vs-choose resolved via
  two concrete rulings, Korvan claims the dragon as his own ('the clan of one is now two'), residue
  un-bowed. Canon guardrails held throughout. **WHOLE-BOOK AUDITS DONE:** continuity-guardian pass
  (0 critical, 5 warning + 4 minor — all 5 warnings + 2 minor contradictions FIXED gate-clean; roan
  gelding / Selwyn betrothal / Della accepted as deliberately-open threads); voice-consistency audit PASS
  (Bishop register + POV differentiation hold Ch.1–29); META/fourth-wall narration confirmed NONE.
  Reports in `evaluations/`. **NEXT (all OPTIONAL / non-blocking):** reassemble full-manuscript.md +
  PDF; book-packager editorial package + formatting; resolve the deliberately-open threads only if a sequel is ever pursued (standalone; none planned). See
  `feedback/progress.md`.
- **(history) 2026-07-10 — DRAFTING, 27 of 29 chapters FINALIZED (Ch.1–27, all Genesis Floor ≥ 8.5).**
  Manuscript **~141,433 words** (already over the 140k floor with 2 chapters left). Both explicit
  scenes done: Ch.18 (first) and Ch.26 'The Reunion' (author-expanded 2026-07-10 to be more explicit
  and DISTINCT from Ch.18 in both acts and aftercare; Floor 8.5/avg 8.79). Climax pt 1 **Ch.27
  'Outlasted (I)' [K]** finalized (Floor 8.5/avg 8.86, Casual 9.0): role-swap (Amelia unseen, Korvan
  the loud shape), the dragon ENDURES not wins, the chief's 'survive to fight later' creed weaponized,
  Selwyn falls (fate unknown), ends mid-climax with Amelia face-to-face with Loric.
  **NEXT: Ch.28 'Outlasted (II)' [Amelia] — CLIMAX PT 2 (final beat):** contain/stop Loric by
  OUTLASTING not argument (canon); pay the named cost in one blow — the Queen (Rosalia) AND Maren both
  die; reader-only reveal the Queen dies NEVER knowing Loric's name; Amelia left the throne as
  Rosalia's natural-born heir. THEN **Ch.29 'What We Choose' [A, K coda]** — aftermath, Amelia takes
  the throne ('the clan of one is now two'). Full Ch.28 handoff brief + resume point in
  `feedback/progress.md`; per-chapter scores/notes in `STATE.yaml`. Run `bash tools/check_chapter.sh N`
  every chapter, then the Genesis Floor eval + pacing check before finalize.
- **(history) 2026-07-08 — DRAFTING, 7 of 29 chapters finalized (all Genesis Floor ≥ 8.5).** Ch.1 'Contraband' [A],
  Ch.2 'The Servants' Passages' [A], Ch.3 'Unshifted' [K], Ch.4 'The Man Who Only Asks' [K],
  Ch.5 'Among People' [A], Ch.6 'The Garden' [K], Ch.7 'Heads I Win' [A — **TP1**, Floor 8.5/avg 8.9].
  All mechanical gates clean (style/grammar/rhythm/voice-wear); both POV voices established;
  cover-the-name holding. **~35,250 words so far.** **NEXT: Ch.8 'What a Reasonable Man Does' [K]** —
  chief declares war rather than face the challenge; Korvan folded into suspicion; they leave for home
  (closes the front act, ~28%). See `feedback/progress.md` for the exact resume point and Ch.8 beats.
  - **New this session:** `tools/voice_wear_check.py` — whole-book, per-character voice-wear gate
    (reads `feedback/pov-map.txt`; run it as part of the post-completion check). Per-POV ledgers:
    `feedback/{amelia,korvan}-voice-ledger.md`. "never once" retired book-wide. Ch.6 needed a pacing
    polish (round 2); Ch.4 needed a pacing round 2 earlier; all others passed round 1.
- **2026-07-08 — RE-ARCHITECTURE COMPLETE.** Title *A Bond of Scale and Silver*; ADULT romantasy;
  Bishop voice comp; forced-proximity outline rebuilt; beta-lessons + Bishop mechanics baked in;
  full pipeline installed on this branch from `knightdx91-alt/book-pipeline`. **No prose yet.**
  **NEXT:** author review of the outline, then draft Chapter 1 under the gates (Bishop voice,
  beta-lessons-checklist, style_check em-dash≤10, grammar_check clean, ≥5,000w, Genesis Floor ≥8.5),
  chapters SEQUENTIAL.
