# Progress — A Bond of Scale and Silver

> Book slug: `scale-and-silver` (was `rosalia`). Last updated 2026-07-10 (production/packaging session).
> Read `STATE.yaml` first, then this file.

---

## ▶ RESUME HERE — PRODUCTION + PACKAGING COMPLETE (2026-07-10)

The book is complete (29 ch, all Floor ≥ 8.5, ~152.9k assembled words) AND the full production +
packaging track is DONE, all on `main`. Nothing is blocking; what remains are author/asset decisions
before a print order.

**Delivered this session (all committed + pushed to `main`):**
- **Cover** — decided front `delivery/cover/front-cover-post-peleos.png` (+ `…-clean.png`, white
  bottom-strip cropped, 1600×2176, the canonical front/ebook asset).
- **Interior** — `manuscript/full-manuscript.md` reassembled (29 ch) → `production/build_pdf.py` →
  `delivery/production/A-Bond-of-Scale-and-Silver-6x9-interior.pdf` (**448 pp**) + PDF/X-1a CMYK.
  Fonts embedded (Plex subsets only), body paginates from 1.
- **Front matter** — half-title, title page (title / "a novel" / **Post Peleos**), copyright page,
  and the **dedication**: *"For all the ones that were told to hide themselves from the world. We see
  you."* Author decisions applied: standalone (no series line), no in-interior heat advisory.
- **Cover wrap** — `production/compose_wrap.py` → `…-wrap-6x9.pdf` (+ X-1a CMYK). Spine **1.120"** @
  448 pp cream 50# (`PPI_FACTOR` param → white stock = 0.002252). Back = `editorial/back-cover.md`
  copy + comps + ISBN-barcode quiet-zone box; spine = title + author.
- **EPUB** — `production/build_epub.py` → `delivery/production/A-Bond-of-Scale-and-Silver.epub`
  (EPUB 3, structurally validated: mimetype-first, well-formed XML, all links resolve, cover + nav +
  front matter + 29 chapters).
- **Editorial** — `editorial/beta-reader-pitch.md` added (spoiler-light recruiting pitch + short and
  one-liner DM versions). Existing `logline`/`synopsis`/`back-cover`/`comps`/`query` unchanged.

**OPEN before a print order (author/asset decisions only — not code):**
1. Confirm **paper stock** (cream vs white 50#) → sets the spine factor; rebuild wrap if white.
2. Assign **print + ebook ISBNs**; drop the printer's **real barcode** into the wrap's quiet-zone box.
3. For a strict CMYK proof, swap the generic `default_cmyk.icc` for the printer's target ICC
   (US Web Coated SWOP / IngramSpark-specified) and re-run the X-1a conversions.
4. Optional: KDP 2560×1600 ebook cover; a one-command "rebuild-all" script; Floor re-eval Ch.19/28/29.

Full production checklist: `production/PRODUCTION-PLAYBOOK.md` (Quick status). Older revision-pass
resume notes are preserved below for history.

---

## (history) ▶ SURGICAL PACING PASS (front act DONE 2026-07-10)

**FRONT-ACT PASS COMPLETE (Ch.1–9).** Trims landed in Ch.1–6 (each committed, gate-clean):
Ch.1 −91, Ch.2 −29, Ch.3 −51, Ch.4 −28, Ch.5 −149, Ch.6 −48 — all removing genuine restatement/
circling (age recaps, duplicated triads/codas, event-recaps), never scene or voice. Ch.7 (TP1
exposure), Ch.8 (war declared), Ch.9 (escape) reviewed and DELIBERATELY LEFT INTACT: plot-turn/
propulsion chapters the plan says to protect, already tight and at/under floor, no non-load-bearing
dwell. Per-chapter rationale in the plan doc's Status section. Book total now **153,423w** (still
well within the romantasy band; the surgical philosophy meant light cuts — the prose had little fat).
Ch.5 dropped under the 18% long-sentence ceiling (was a legacy over-ceiling chapter).

**▶ DECISION FORK (author): what next?** (1) light Ch.10–17 thinning pass — motif re-measure shows
mid-book motifs are mostly thematic/deliberate (Ch.17's high "count" = Maren's signature spoon-
counting), so any pass would be light; (2) re-run the beta panel + external read now that the front
act is faster; or (3) call the surgical pass done. **MID-BOOK (Ch.10–17) THINNING DONE (author-requested, committed):** light surgical restatement
cuts in Ch.10/11/13/14/15 (~−187w total); Ch.12/16/17 reviewed and PROTECTED (dense/essential;
Ch.17's high 'count' is Maren's signature). Per-chapter rationale in the revision-plan Status section.
Book total ~153.5k (the Ch.2 gift-seed add offsets the trims) — well within the romantasy band.

**#3 (Della/Maren) + #4 (gift cost) DONE (author-chosen, committed):** Ch.1 gave Della the nurse's
'lamb' + locked her existing bedside/slow-bolt/touch signature (Ch.24 already calls back); Maren stays
the dry counter. Ch.2 ritual now seeds the gift's LIMIT — 'taking is easy; holding a life in, catching a
fast wound before it empties, is the slow craft of a thousand years' — paying off the Ch.28 Selwyn
total-loss. Remaining plan items are the two DEFERRED ones below (mid-book thinning / beta re-run).

---

**PLAN: `feedback/revision-plan-grok-2026-07-10.md`.**
- **Trigger:** external **Grok** read (first independent market read): strong prose/character/world,
  but **overwritten + slow front act, motif repetition, Della/Maren blur, gift needs harder cost.**
  Aligns with our own known weakness (early-act pacing; the scene-end tic we already swept).
- **Author decisions (2026-07-10):** (1) **STAY adult romantasy** (do NOT reposition to literary
  fantasy, though Grok + our beta Critic both read it that way); (2) do the **SURGICAL pass, NOT the
  ruthless 20–30% cut** (a 30% cut = a different book; 150k is in-band for romantasy).
- **Target:** accelerate **Ch.1–9**, thin over-hammered motifs (per-chapter caps), sharpen
  **Della vs Maren**, harden the **gift's cost/limits**. Landing ~135–145k, same story + voice.
- **Execution order:** Ch.1 → Ch.9 first (front act = highest ROI), per-chapter discipline
  (read → cut/accelerate → `check_chapter.sh` clean → no new n-gram → commit). Word floor may be
  intentionally breached by trimming here — log, don't pad. Keep the 2 explicit scenes + 3 couple
  beats intact. Then re-measure and decide on a lighter Ch.10–17 thinning; re-run beta + external read.
- **Progress checklist lives in the plan doc's Status section.**

---

## (prior) post-completion revision session (2026-07-10)

### 0. Where the book LIVES now (important)
- **Source of truth = the standalone repo `knightdx91-alt/A-Bond-of-Scale-and-Silver`, on `main`.**
  All work happens here now. The old copy inside `knightdx91-alt/The-Saeren-Chronicles`
  (`book/genesis/scale-and-silver/`) is **FROZEN** — see its `MOVED.md`; do not edit it.
- **BRANCH POLICY (absolute):** work only on `main`; never create a branch or PR unless the author
  explicitly asks in that session. Enforced by the top of the root `CLAUDE.md` + the SessionStart
  hook (`.claude/hooks/session-start.sh` switches to `main`). If a session launches on a
  `claude/...` branch, switch back to `main`.
- Full writing pipeline is vendored here: `.claude/agents/` (12 book-* agents),
  `.claude/commands/` (gemini/grok second-opinion — need API keys to run), `book/genesis/
  _reviewer-skills/` (beta-reader-panel etc.), `_template/`, `new_book.sh`, `tools/apodictic`.

### 1. Revision work DONE this session (all committed + gate-clean; book still 29 ch, all Floor ≥ 8.5)
Current word count **152,067**. Gates green throughout (grammar / style / metaphor-shape / rhythm /
show-tell / voice-wear). Detailed log: `feedback/line-edit-findings-2026-07-10.md`; checklist:
`feedback/line-edit-checklist.md`.
1. **Whole-book line edit** — climax (Ch.25–29) phrase-echo/tic/long-sentence cleanup; front-act
   (Ch.1–9) show-vs-tell tightening (Ch.1 household para, Ch.8 relief coda, etc.).
2. **Ch.23→24 hinge — Fix A** (author-approved): Ch.23 ends undirected on the diagnosis; Ch.24 owns
   the choice; removed the south/north contradiction + a ¶119 geography slip.
3. **Beta-reader panel run** (5 adult-romantasy personas) → `evaluations/review/beta-reader-panel.md`.
   Scores 5.0–8.5. Consensus fixes = the four below.
4. **De-tic pass (beta #1)** — varied cross-POV repeaters: "looking back was a hand reached out…"
   (kept Ch.21 anchor), "it was not nothing"/"she held to that" doublings, Ch.29 "don't cancel".
   KEPT "the sum/arithmetic" (deliberate, signposted characterization, not bleed).
5. **Feeding thread (beta #2 — "account for it")** — Ch.11 recalibrated (points at the animal
   resolution, not an unfired "put me down"); Ch.23 acknowledgment added (she survives on the road's
   dying animals, never a person, at cost).
6. **Timeline (beta #3 — "compress to weeks")** — converted the stray "a year" in Ch.25/26 to the
   book's weeks scale (kept 2 "felt like a year" similes), THEN thinned the "weeks" drumbeat that
   over-correction created in Ch.25/26.
7. **Production knowledge migrated** — `production/PRODUCTION-PLAYBOOK.md` + `production/reference/`
   (PDF interior specs, the font-embed + RGB→PDF/X-1a CMYK fixes, wrap/cover learnings, build tools).

### 2. Beta round-2 + follow-up fixes — DONE (2026-07-10, later in session)
Re-ran the beta panel after the fixes above → `evaluations/review/beta-reader-panel-round2.md`
(scores held/rose: Hostile 5→6, Casual 6.5→7, Critic 6→6.5, Devourer 8, Devoted 8.5; feeding RESOLVED,
tic IMPROVED, timeline IMPROVED). Then cleared the remaining actionable items:
- **Ch.29 time over-referencing** — DONE. "twenty-two days" thinned to TWO deliberate anchors (¶3
  opener + ¶25 grave/crown — the bookending frame, sanctioned per Floor re-eval Fix #5, NOT one);
  ¶73 → "at the Elver", ¶83 → "your mother barely in the ground", ¶99 "three weeks" clash removed.
- **Ch.27 stray "a year"** (Selwyn) — DONE → "said all along". (Reviewed the other ~10 "a year" hits:
  the rest are life/hyperbole idioms — "worth a year's wages", "in a year of being reasonable" — left
  intact; swapping them would flatten voice, same over-correction lesson as "weeks".)
- **Ch.17 tighten** — DONE (one redundant "banner / not a who" interiority reiteration trimmed; the
  chapter is dense-but-load-bearing, not flabby — did not gut the council scene).
- **Beta #4 — Selwyn — AUTHOR CHOSE: let the death stand.** DONE. Ch.28 save reworked so the wound is
  "too open to hold" (she reaches him and cannot) — this both honors the choice AND embodies the
  power-limit the panel wanted seeded (no convenient stranger-save; the arithmetic is now total loss).
  Ch.29 ¶65 reworked from "mending" to a death report + a ruling beat. **Selwyn is now DEAD** →
  Book-Two betrothal seed (MINOR-003) is VOID (could become a Book-2 grief thread instead).
- **Beta #5 — POSITIONING — AUTHOR CHOSE: keep romantasy + add couple page-time.** DONE. Added a new
  mid-book togetherness beat at the Ch.19 shieling pre-dawn (Korvan POV, ~330w, NON-explicit to respect
  the two-explicit-scenes canon; deepens the bond, seeds the separation ache). Comps stay ADULT
  romantasy / Anne Bishop (NOT McKillip/Priory/YA).

### 3. ▶ NEXT — open items (pick up here)
**Ch.29 Selwyn continuity RESOLVED (2026-07-10):** the Floor re-eval
(`evaluations/review/genesis-floor-re-eval-2026-07-10.md`) flagged Ch.29 BELOW FLOOR (8.0) because
¶57 and ¶93 still carried the OLD save-succeeded ford arithmetic ("staying where she told it to
stay" / "it had held") after Selwyn's death was reworked in Ch.28. Both passages recast to the
total-loss ledger (power vast but too green to catch it in time) per Fix #1, sentence shapes kept,
neither cut. Gates re-run clean (grammar clean; style 618 = unchanged baseline, no new flag;
metaphor 15.8% <40w under ceiling; word floor 5,327). Ch.19/Ch.28 already verified PASS in the
re-eval. A round-3 beta panel is optional after any further changes.

**All Floor re-eval fixes CLEARED (2026-07-10):** Fix #1 (above) + Fix #2 (Ch.28 ¶151 "held"→"used
it barely a season"), Fix #4 (Ch.20 ¶91 70-word sentence split; sharpens the Ch.28 payoff echo),
Fix #5 (Ch.20→Ch.28 seed/payoff echo + Ch.29 "twenty-two days"×2 logged as SANCTIONED in
`style-flags.md`). Plus the beta timeline note: Ch.25 "not ten words of him in a year" → "since the
garden" (removes the one literal-year residue on the compressed timeline).

**Beta-panel developmental items ACTIONED (2026-07-10) — POSITIONING = ROMANTASY (author call):**
- **2b scene-end "narrated-thesis" de-tic pass** — converted the worst scene-end meaning-statements
  to image/action (panel's #1 craft lift): Ch.28 ¶111 ("The touch was only tidying" cut, lands on the
  hill-loss fact), Ch.24 ¶121 ("Hidden and seen were the same wall" → chains going home behind her),
  Ch.15 ¶99 ("it was not nothing / his father said as much" → the dragon's head resting in her hand),
  Ch.23 ¶121 (seen/caged "same thing" → a cold decision), Ch.21 ¶139 ("whole of the cost" → flying
  north with nothing to pay it but distance). Net: style baseline 618→615 (three flagged repeats
  removed, zero new). **Second batch (full sweep):** Ch.4 ¶63 (kindness-as-menace close → Korvan
  rubbing the cold off his neck), Ch.12 ¶103 (Orry's shame → getting up to warm his hands elsewhere),
  Ch.23 ¶39 ("whole of it / thing she'd carry" → made herself watch, the only thing left to give),
  Ch.28 ¶171 chapter-end ("nothing she could hold at all" → "and neither of them crossed"). **The
  paragraph-END narrated-thesis tic is now effectively CLEARED** — an automated recheck leaves only
  image-landings, remembered dialogue, and false positives (9 scene-ends converted total; style 615).
- **2a couple page-time (kept the ROMANTASY pitch)** — added TWO non-explicit togetherness/claim beats
  (canon holds: only two explicit scenes, Ch.18 + Ch.26): (1) **Ch.21 open** — a pre-dawn cold-camp
  beat the night before the ford ambush (Korvan POV), last calm before the separation, seeds the ache;
  (2) **Ch.29 coronation-evening** — a physical-claim kiss ("Mine" / "Hers") before the bittersweet
  "two banks of the same water" close, honouring the theme without turning it HEA. Both gate-clean;
  new n-grams varied out; book now **153,579 words**.
- **Ch.22–25 separation-trough yearning beat ADDED (2026-07-10):** per beta R5's top optional lever,
  added a brief bodily-yearning beat to the Ch.24 close (Amelia POV) — her body wanting Korvan (the
  heat at her back in hut/shieling/cold-camp, his careful hands), the physical want that turns her
  east toward reunion. Fresh diction (no Ch.21 echo), gate-clean, voice-wear clean ("never once"
  avoided), zero new n-gram, book 614 style baseline. Bridges into Ch.25's Korvan open (cross-POV).
- **STILL OPEN (author):** an optional deeper
  pass on mid-paragraph (not scene-end) interior meaning-statements; and the bias-check caveat
  (self-generated 9.0s want a human/external read). The scene-END tic sweep is complete.

**Still-open production track (non-blocking):**
- Adapt + run `production/reference/assemble_manuscript.py` (extend to 29 ch, this title) →
  `manuscript/full-manuscript.md`; adapt + run `build_pdf.py`; **verify fonts embedded**; convert to
  PDF/X-1a CMYK (needs gs/Acrobat); derive page count → design wrap at full bleed with correct spine;
  add front/back matter; separate EPUB build. See `production/PRODUCTION-PLAYBOOK.md`.
- `book-packager` editorial package (logline/synopsis/query/cover) — for ADULT romantasy.

**Book-Two seeds still logged (from the completion audit):** roan gelding (WARN-005), Selwyn's
betrothal (MINOR-003), Della's fate (MINOR-004) — deliberate open threads awaiting author intent.

---

### ✅ BOOK ONE COMPLETE + FULLY AUDITED (2026-07-10)
- **Whole-book audits done this session (all reports in `evaluations/`):**
  1. **Continuity-guardian full-book pass** (`continuity-audit-full-book-2026-07-10.md`) — 0 critical,
     5 warning, 4 minor. **All 5 warnings + 2 minor contradictions FIXED, gate-clean:** WARN-001
     force-size (Ch.15 muster plant + Ch.19 "forty" as subunit); WARN-002 chief's Ch.22 reveal
     reframed to "it's my own boy" (not "a dragon is real"); WARN-003 Amelia's capture/escape bridge
     in Ch.23 (drops escorts non-lethally — preserves Ch.24 first-kill — + self-heals leg per Ch.20);
     WARN-004 Maren's transit to the Queen (Ch.28); MINOR-001 tenure 18→19y (Ch.2); MINOR-002 empty/
     dry vial (Ch.23). **Accepted as Book-Two seeds / open threads (not changed):** WARN-005 roan
     gelding, MINOR-003 Selwyn's betrothal, MINOR-004 Della's fate.
  2. **Voice-consistency audit** (`voice-consistency-audit-2026-07-10.md`) — **PASS.** Bishop register
     holds Ch.1→29; Amelia/Korvan distinct at the narration level (no destructive braided bleed);
     back-half figurative decline judged earned, not thinning. One WARNING = deliberate device-
     convergence (no fix). Standing Book-Two rule logged: keep Korvan's fire/body-first cognition
     primary in his own chapters.
  3. **Meta / fourth-wall narration: NONE** (mechanical grep + full human read both confirm).
- **Post-audit numbers:** 29 chapters, **152,116 words**, every chapter Genesis Floor ≥ 8.5, all
  mechanical gates green (grammar / style / metaphor-shape / rhythm / show-tell / voice-wear),
  canon guardrails intact.
- **NEXT — all OPTIONAL / non-blocking:** (a) reassemble `full-manuscript.md` + build PDF;
  (b) `book-packager` editorial package (logline/synopsis/query/cover) + ebook/print formatting;
  (c) the deliberately-open threads (the roan gelding, Selwyn's betrothal, and
  Della are logged deliberate seeds awaiting author intent).

### (superseded) ✅ BOOK ONE COMPLETE (2026-07-10) — all 29 chapters finalized
- **Ch.29 "What We Choose" [A, with K coda]** FINALIZED: 5,236 words. FINAL CHAPTER. Genesis Floor
  **8.5 / avg 8.86** (5 dims at 9.0 — Originality/Theme/Characters/Prose/Emotion; Casual 9.0) — eval
  `evaluations/chapter-29-eval.md`, PASS. Mechanical gates green (grammar clean; %>40w 16.4; fig
  1.1/1k; em-dash 1; voice-wear clean; show/tell clean; word floor met). Post-eval: trimmed one
  restated-thesis clause from the final paragraph so the bare "The clan of one is now two." line
  stands alone and the book ends on image, not summary. Pacing PASS (5,236 vs Ch.28 5,055, in-band;
  throne scene has healthy dialogue, interior coda near-zero — correct final-resolution deceleration).
- **What Ch.29 delivers:** aftermath 22 days on. Amelia crowned — the Ch.1 bookend (locked room at
  four-parts-in-ten / beeswax-and-cold-stone / "heard across a bright room") pays off as
  want-granted-as-new-cage. Inherit-vs-choose resolved through two concrete rulings (refuses the
  succession proclamation; spares the west bank + Loric's nine). Korvan coda rejects "the Queen's
  dragon," claims the shape as his own authored place, chosen-not-fated; chief's swim-creed payoff;
  "The clan of one is now two." Residue un-bowed (Rosalia/Maren ungrieved-away; the truth never
  mattered). Selwyn alive/mending. Canon clean; sequel runway, not cliffhanger.
- **WHOLE-BOOK NUMBERS:** 29 chapters, **151,724 words** (over the 140k floor and the 150k target),
  every chapter Genesis Floor ≥ 8.5. `voice_wear_check.py` over the full manuscript: **clean**.
- **NEXT — all OPTIONAL / non-blocking:** (a) whole-book QA + `continuity-guardian` sweep over all
  29 (final polish/consistency); (b) reassemble `full-manuscript.md` + rebuild PDF; (c)
  `book-packager` editorial package (logline/synopsis/query/cover) + ebook/print formatting;
  (d) the deliberately-open threads (standalone; no sequel planned).

### Resume point (2026-07-10, superseded) — Ch.28 FINALIZED (CLIMAX COMPLETE), start Ch.29 (LAST chapter, aftermath)
- **Ch.28 "Outlasted (II)" [Amelia]** FINALIZED: 5,055 words. Climax part 2 / final beat. Genesis
  Floor **8.5 / avg 8.71** (Characters/Prose/Emotion 9.0; Casual 9.0) — eval
  `evaluations/chapter-28-eval.md`, PASS. Mechanical gates green: grammar clean; metaphor/sentence
  clean (%>40w 15.0, fig 1.0/1k, no flags); em-dash 4, simile 0.8/1k; voice-wear clean; word floor
  met. One post-eval anaphora run trimmed (broke a "She had not..." triple). Pacing PASS (5,055 vs
  Ch.27 5,462, in-band; ~18% dialogue correct for an interior climax finale; catastrophic-loss +
  hollow-crown slot lands; hook pulls to Ch.29). `feedback/pov-map.txt` updated (28: Amelia).
- **What Ch.28 does (for the Ch.29 writer):** Single-location, single-POV (Amelia), her clinical
  dissociative voice-under-pressure. She reaches Loric at the high knot and **outlasts, does not
  argue** — gives him only silence, keeps her eyes on her mother. **Named cost, one blow:** a flat
  whale-iron cast (Loric's own war-engine) crosses the crown of the hill and kills the **Queen
  (Rosalia) AND Maren** together (Maren had gone east with Amelia, then to the Queen; camera cut on
  the strike). **Reader-only reveal delivered:** the Queen dies with her whole attention on Amelia
  (almond cakes / "you're always cold"), never looks at Loric, never learns his name or the why —
  his life's work defeated by her indifference. **Loric's grief cracks once** ("No... She never
  even—") then buries it forever; Amelia stills his heart **after** the deathbed already beat him,
  so the kill is deliberate anticlimax ("the touch was only tidying"). **Selwyn: ALIVE but costly**
  — she holds his single torn vessel shut (the one thing her magyk CAN do), the grotesque
  arithmetic being that it saved a stranger and was useless/refused for the two she loved. **Throne
  planted:** the quiet men kneel, the eldest names her "Majesty," she orders the standards lowered
  and the frames stopped — war **redirected, not undone**. **Korvan left down-but-alive** in the
  ford wreck, his one dark eye up the hill on her — the two kept alive on opposite banks for the
  Ch.29 coda.
- **Ch.29 "What We Choose" [A, with K coda] — LAST CHAPTER — must:** aftermath. **Amelia takes the
  throne** (first natural-born vampire Queen, the contraband girl ruling openly) — the want granted
  AND a new cage: finally seen, more alone than ever, having paid in her mother and Maren. She
  inherits the crown but **chooses** how to wear it (inherit vs choose, resolved). **Korvan coda:**
  he claims the dragon as his own authored place — not "the Queen's dragon" (a slot) but hers by
  choice, and she his; two outsiders now at the centre they were exiled from. **"The clan of one is
  now two."** A world redrawn (a natural-born Queen, a living dragon), arc complete, sequel runway.
  Residue: unsettled by how little truth mattered; the crown sits on the girl no one was allowed to
  see. Keep it in-band (~5,000w), gates green, canon held (magyk, silver hair, dragon situational,
  no Atlantis dump). **After Ch.29:** run the whole-book completion checks — `voice_wear_check.py`
  over the full manuscript, confirm word floor, then optional reassemble `full-manuscript.md` + PDF.

### Resume point (2026-07-10, superseded) — Ch.27 FINALIZED, start Ch.28 (climax pt 2, final beat)
- **Ch.27 "Outlasted (I)" [Korvan]** FINALIZED: 5,474 words. Climax part 1. Genesis Floor **8.5 /
  avg 8.86** (5 dims at 9.0; Casual 9.0) — eval `evaluations/chapter-27-eval.md`, PASS. All
  mechanical gates green: grammar clean; metaphor/sentence-shape clean (%>40w 7.1 vs 18 ceiling,
  longest sentence 78w after the split, fig 1.3/1k); style em-dash 1, simile 0.5/1k, adverb 2.6/1k;
  rhythm 0-flagged; voice-wear clean; show/tell no row flags (emo 0.0). **Pacing check PASS**
  (in-band vs neighbors 5.0k–5.8k; battle-appropriate dialogue share ~10%; correct climax-cost
  slot; strong hook/pull). Applied the eval's non-blocking polish (split the 124w fall-into-fire
  sentence; varied one of the 'two irons in' repeats).
- **What Ch.27 does (for the Ch.28 writer):** the battle joins at the Elver crossing (two hosts,
  the falls). Korvan + Amelia SWAP roles from Ch.21: he becomes the LOUD SHAPE (goes up in the
  open, draws Loric's whole whale-iron net onto himself, absorbs and endures — does NOT blitz to
  victory), so Amelia can be the unseen one who crosses the ground to Loric. **Subversion delivered:**
  the dragon does not win the day, it BUYS TIME; and the chief's endure/outlast creed Korvan spent
  the book rejecting is turned into his sharpest weapon, on purpose ("his exact thing... and it
  isn't surrender this time"). **Cost begun:** two whale-irons in him (flank + torn wing), the
  dragon brought down onto the east bank (turned bringing-low into going-to-ground). **Named ally
  falls: SELWYN** — hit by a flat whale-iron cast into the shifter front, goes under the ford water
  reaching up; Korvan holds the line and does NOT come down for him (the weaponized creed with
  teeth; mirror of Amelia on the shelf, Ch.21). **Left open for Ch.28:** Selwyn's fate UNKNOWN
  (gravely hit, not confirmed dead); Loric is NOT yet contained. Ends mid-climax: Amelia has
  reached Loric (hood back, arm's length, his empty hands open), Korvan pinned 100ft down a slope,
  two live frames still cranking. **Fire-pedantry re-read reward paid** (his green-stick/seasoned-oak
  opinions turn grotesque against real dragonfire).
- **Ch.28 "Outlasted (II)" [Amelia] must:** contain/stop Loric (outlasted, not argued — canon);
  pay the named cost — **Queen (Rosalia) AND Maren both die**; reader-only reveal the Queen dies
  never knowing Loric's name; Amelia left the throne (natural-born heir). Resolve Selwyn's fate.
  Chief is now a knowing dragon-secret-holder (since Ch.22). Then Ch.29 aftermath.

### Resume point (2026-07-10, superseded) — Ch.26 finalized, start Ch.27
- **Ch.26 "The Reunion" [K+A braided]** finalized: 5,812 words, Genesis Floor **8.5 / avg 8.79**
  (Casual 9.0; re-evaluated 2026-07-10 after the expansion). The reunion + the book's SECOND
  explicit scene (~90% heat). **Author-directed rewrite + expansion (2026-07-10):** the sex was
  reworked so it no longer mirrors the Ch.18 first scene, in acts AND aftercare.
  - **Acts (she-led, expanded):** extended oral on him (licks his length, deep-throat, his fist in
    her hair holding her head down, her fighting for breath, off and back down) → she strips and
    climbs on top, slowly takes him in and savours the feel and rides to her own finish → he turns
    her and takes her from behind for the hard finish (the leash he held in Ch.18 finally slips).
    Ch.18 by contrast was he-led (his mouth/hand → missionary), a half-starved cold-thaw. Inversion
    is thematically motivated in-text ("I was frozen half to death… furious I didn't get to do it
    properly").
  - **Aftercare (rewritten distinct from Ch.18):** two new beats — the strangeness of peace
    (nothing to guard against after a year on the run) and the cold-into-heat exchange — instead of
    Ch.18's "dark cost / chose it eyes open / the large word unsaid" reflection. Kept: name GIVEN,
    the sum set down (image-led, aphoristic coda cut in the polish pass).
  - Canon clean (magyk; silver-hair/dangerous-not-victim — she authors the choice; won't-feed;
    dragon fully down, "None of the dragon anywhere in it. Only the man"; no sexual violence; no
    Atlantis lore-dump). All mechanical gates green (grammar clean, voice-wear clean, em-dash 5,
    simile 1.4/1k, rhythm 0-flagged, word floor met). Pacing in-band; the reunion two-hander is the
    correct emotional high before the climax. Ch.18↔26 act-AND-aftercare echoes cleared.
  - Non-blocking Prose softeners noted in the eval (hold floor at 8.5 not 9.0): three long rolling
    `and…and` sentences in the explicit passages (%>40w ~15.5% vs Ch.1 ~11%) + two narrated-meaning
    codas. Optional split/trim pass. Eval: `evaluations/chapter-26-eval.md`.
- **NEXT: Ch.27–28 (the two-beat climax)** — the war at the crossing. Ch.27/28 are the only
  remaining chapters (29 planned total). Draft under the usual per-chapter discipline.

## Where we are (2026-07-09)

**Phase: DRAFTING. Ch.1-14 finalized (all Genesis Floor >= 8.5), ~70,400 words. Act II underway.
show_tell_check.py + voice_wear_check.py standing gates. Next draft: Ch.15 "The First Full Moon"
[Korvan] — TP2, the first shift into a DRAGON, Amelia the only witness.**

### Resume point (2026-07-09) — Ch.14 done, start Ch.15
- **Ch.14 "Let Go So You'd Learn to Swim" [Korvan]** finalized: 5,073 words, Genesis Floor **8.5 /
  avg 8.64** (Characters 9.0, Emotion 9.0, Casual ~9/10). The emotional hinge before TP2: the Ch.3
  swim memory pays off as the chief's whole creed (the hand is what drowns you, not the water; he
  let Korvan go under on purpose, and the war is the same gesture writ large). The argument REFUSES
  to resolve (Korvan can't find where the man is wrong, can't agree he's right — "never going to add
  up"). Korvan snaps viciously at Selwyn (the garden secret corroding him); Selwyn names the mechanism
  ("you're doing your father's thing") and refuses the exit, supplies the game trail + the grey mare.
  Korvan gives Selwyn the "you did just exactly what one of ours does" line he'd wanted his whole
  life. Chief gives help disguised as refusal ("I will fail, on purpose, to look toward that
  mountain"). Shift SEEDED: the closing flutter "a slow deep turn not like any of the times before,"
  misread as grief; full moon "come round to full, or near it." Note: heavy repeated-phrase cleanup
  was needed (the chief's creed deliberately reprised Ch.8 — ~50 cross-chapter echoes broken to keep
  style_check clean, since the ALLOWLIST is empty by design).
- **Ch.15 beats (outline, TP2 ~50%):** Korvan POV. On the first full moon after his birthday he
  shifts — into a DRAGON — calendar coincidence, NOT magically triggered, with AMELIA THE ONLY
  WITNESS. Clan of one; no elders, no traditions. First trickle of dragon ancestral memory
  (situational, NOT Atlantis-linked — hold canon). The silver moon. Register = bewilderment and
  grief, NOT power-fantasy: he wanted to belong and became the loneliest thing alive. Subversion:
  the epic dragon reveal is a catastrophe, not a gift. (The dragon comes at/near water — tie to the
  Ch.13 tarn water-beat + the Ch.14 swim memory.)

### (superseded) Resume point (2026-07-09) — Ch.13 done, start Ch.14
- **Ch.13 "Blood Answers" [Amelia]** finalized: 5,028 words, Genesis Floor **8.5 / avg 8.79**
  (Originality/Characters/Emotion/World 9.0, Casual 9/10). The power-awakening TRAP: hunters corner
  them at a black tarn; her blood magyk answers formidable (holds seven hearts at once, "no edge to
  it"); she breaks the "Never a person" vow to save Korvan, then does NOT kill — holds them at the
  edge and sends one back to Loric. The soft leader's subversion: "the more you spare, the more you
  prove him... you let us live and made yourself a fact." Korvan doesn't run ("well-matched pair of
  monsters"). NAME-BEAT kept honest — he never had her name (Ch.10 canon), reaches her with presence
  ("I'm here"), preserving the name-gift for its true payoff. Water-beat seeds Ch.14 shift.
- **Ch.14 beats (outline):** Korvan POV. First SHIFT payoff — the dragon comes at/near water, tied to
  the childhood swim memory (father took his hand off his belly, let him go under to learn to hold
  himself up). Father-son argument (Selwyn/chief); Korvan snaps. He must get Amelia clear before the
  retinue finds her. The late-shifter stigma pays off as awe/terror; a clan of one. Hold: dragon
  memory does NOT link to Atlantis (canon).

### Resume point (2026-07-09) — Ch.9 done, start Ch.10
- **Ch.9 "The Reason Is Gone" [Amelia]** finalized: 5,021 words, Genesis Floor **8.5 / avg 8.7**
  (Characters 9.0, Emotion 9.0, Casual 9/10). The book's agency pivot: cage-reason expires with the
  war; she out-argues the warm-but-controlling Queen, loses (the cage is love, not argument), and
  chooses to flee anyway. Maren's costly yes + "one word in a year." Escape near-miss (spit-boy),
  the Queen's blood-vial (her non-heritable magyk = the one gift she can send), first breath under
  open sky. 45% dialogue (book's highest). Evaluator-flagged scene-end codas fixed — ends on the
  walking, not narrated meaning.
- **Ch.10 beats (outline):** Korvan on the journey home under suspicion (whispers, a child who won't
  look at him, Loric's people painting his bloodline sympathetic). Amelia FINDS him (her active
  risk — crosses enemy ground to reach the one person who saw her as a person, not contraband). His
  costly choice: turn her in (safety/way back to his people) or hide her from his father and the
  retinue — he hides her. Secret now doubled (garden meeting + a living vampire concealed in the
  chief's own train). Subversion: not rescued — she walks into the lion's camp on purpose because
  it's still her best odds; his first big choice damns him further and he makes it anyway.

### Resume point (2026-07-08) — Ch.8 done, start Ch.9
- **Ch.8 "What a Reasonable Man Does" [Korvan]** finalized: 5,012 words, Genesis Floor **8.5** (passed
  round 2 after a Pacing polish — floor was 8.0 on: a relief/shame loop restated 4x, a triple-summary
  soft close, and one real POV bleed reaching into Amelia's Ch.7 knowledge). Fixes: cut the bleed,
  compressed the loop, ended on a forward hook ("The world had gone to enormous trouble to hand him
  an enemy. He was going to find her."), and added a concrete suspicion beat (Har's bedroll) to hold
  the 5,000 floor via convert-don't-cut. Korvan learns what she was and re-reads the garden ("clan of
  one" was literal); chief declares war ("bearable door" creed, KNOWS the bond was clean, buries
  Korvan under the war to protect him); bond/dragon seed = his instincts went QUIET toward her; carries
  the garden secret ALONE. All mechanical gates clean.
- **SHOW-VS-TELL (author flagged 2026-07-08 — RESOLVED for the front act):** built
  `tools/show_tell_check.py` (draft-time gate: filter-verb rate, abstraction markers, named-emotion,
  dialogue share; flags telling-heavy paragraphs + codas) and ran a **convert-to-SCENE pass over ALL
  8 drafted chapters**. Filter-verb rate was climbing Ch.1->8 (peaking 11.6/1k at Ch.8); now every
  chapter is under the heavy line (6.0-8.9/1k). Key conversions: Ch.8 narrated "wound between them" ->
  a real Selwyn reconciliation scene; Ch.5 pure-narration banquet -> overheard fragments (adds
  dialogue + plants the "no heir, who does it fall to" irony); Ch.7 Queen's-mask paragraph rendered
  direct (had-seen x3/knew x2 -> shown) + a body beat. All mechanical gates green; all chapters
  >= 5,000w. **STANDING RULE (in CLAUDE.md gates): run show_tell_check every chapter; when short add
  SCENE not reflection; ration scene-end "what it meant" codas; show emotion in the body.**
  Ch.5 (3% dlg) and Ch.7 (7% dlg) remain deliberately interior set-pieces — not forced.
- **Ch.9 beats (from outline.md):** post-exposure; Queen hides Amelia deeper / prepares to send her
  away (reads to the world as guilt); Amelia sees the cage has outlived its reason (treaty already
  broken) and CHOOSES to leave — walking out of love's cell; Maren helps at cost; Loric's hunters
  moving. Subversion: not escaping a villain — walking out of love that is indistinguishable from a
  cage. Amelia POV. No heat.
- **Reminder:** run `tools/voice_wear_check.py` each chapter; keep `feedback/pov-map.txt` current.
  Ch.5 sits at 4 counted-numbers (1-chapter WARN, establishing-heavy) — do not add more of Amelia's
  counting device without trimming, or it re-trips the ≥2-chapter WEAR gate.

### Resume point (2026-07-08) — Ch.7 done, start Ch.8
- **Ch.7 "Heads I Win" [Amelia] — TP1** finalized: 5,024 words, Genesis Floor **8.5** / average **8.9**
  (Characters/Prose/Pacing/Emotion 9.0). Passed round 1; then a light POV + voice-wear polish
  (removed two near-omniscient closing flashes; trimmed the counting register back under the §4b
  cap; varied "five hundred"). The exposure runs on perception alone (moon-silver hair + weaponized
  hall acoustics, the planted inverse of the Ch.5/6 fountain); Queen's warmth -> public mask
  ("I don't know the girl" / "bring the girl to me" = disavowal-as-rescue); NOT-a-victim beat
  (blood magyk wakes, she chooses restraint because using it would prove Loric). All mechanical
  gates clean.
- **Ch.8 beats (from outline.md):** the chief declares war rather than face a challenge he'll lose;
  Korvan, publicly linked to the vampire girl, is folded into suspicion; they leave for home. The
  chief's "reasonableness" was the lever (state the irony). Korvan feels relief it's over, then
  shame at the relief; snaps at Selwyn (small), regrets it. Subversion: the war-declaration is a
  defeat dressed as resolve — everyone loses, exactly as Loric designed. Korvan POV. No heat.
- **Reminder:** run `tools/voice_wear_check.py` each chapter; keep `feedback/pov-map.txt` current.
  Ch.5 sits at 4 counted-numbers (1-chapter WARN, establishing-heavy) — do not add more of Amelia's
  counting device without trimming, or it re-trips the ≥2-chapter WEAR gate.

### Resume point (2026-07-08) — Ch.6 done, start Ch.7
- **Ch.6 "The Garden" [Korvan]** finalized: 5,150 words, Genesis Floor **8.5** (passed round 2 after
  a Pacing polish — floor was 8.0 on a single-tempo sag / 3× restated pull-beat). The pull now arcs
  quiet-notice → near-touch → interrupted by Loric (climax fused with the Ch.7 fuse); a clipped
  dialogue-misfire beat varies tempo AND reinforces cover-the-name (Korvan guesses "runaway political
  bride," nowhere near vampire). All mechanical gates clean (style/grammar/rhythm/voice-wear).
- **NEW TOOL:** `tools/voice_wear_check.py` — whole-book, per-character voice-wear gate (reads
  `feedback/pov-map.txt`; layers = book-wide retired phrases hard-fail, generic per-POV self-repeat
  auto-detect, named-device caps that fail only on ≥2-chapter calcification). Run it as part of the
  post-completion check. Per-POV ledgers: `feedback/{amelia,korvan}-voice-ledger.md`. "never once" is
  retired book-wide.
- **Ch.7 beats (from outline.md):** Loric publicly exposes Amelia at the banquet; accusation engine
  fires (no proof needed); the chief is trapped (declare war or face a challenge he'll lose); the
  Queen's face shows nothing and that nothing is the worst thing. Subversion: being seen — her wish —
  is the catastrophe. Amelia POV. Honor all gates + heat curve (no heat here).

### Settled this session (all committed to `scale-and-silver`)
- **Title:** *A Bond of Scale and Silver* (collision-checked; replaced *Treaty of Blood and Ash*,
  which clashed with Armentrout's *From Blood and Ash*). Scale = Korvan/dragon; Silver = Amelia
  (silver hair + the silver full moon).
- **Category:** ADULT romantasy (was NA). Leads ~19–22. **Explicit/spicy, two scenes** (first
  Ch.18 ~62%, second at the reunion Ch.26 ~90%) — commercial cadence. **Dark intensity, NO
  sexual violence** (cut the camera on the worst acts).
- **Voice comp:** Anne Bishop, *The Black Jewels Trilogy* (studied from the author's epub).
  Register = plain declarative sentences (median ~13 words), deep close-third POV, emotion shown
  through the body, menace/heat by restraint, sparse/simple figurative language, dangerous-but-
  devoted lead (Daemon technique) for Korvan. Adverbs allowed; avoid semicolons; em-dash ≤ 9–10/ch.
  Full spec in `voice-dna.md`; analysis in `feedback/voice-comps-black-jewels.md`.
- **Beta-reader lessons** baked into `feedback/beta-lessons-checklist.md` (from the author's
  Google Docs comments — Eilidh Locherty line-edit + Dana Flanders developmental on Saeren Bk1
  Ch.1). Biggest two: NAME what you mean (no vague reaches), SHOW emotion in the body.
- **Romance backbone:** FORCED PROXIMITY + court cutaways, under 4 anti-Twilight/R&J guardrails.
- **Amelia:** cage-reason EXPIRES at the war declaration (then hides only to survive); **NOT a
  victim** — strong inherited blood magyk, hunted because dangerous/valuable, never rescued.
- **Korvan:** rare late shifter ~19–20; dangerous-devoted dragon; carries the garden secret alone.
- **Chief's failing-body subplot:** CUT. Three old motif phrases: CUT.

### Re-architecture done (committed)
- `foundation.md` and `outline.md` rebuilt around forced proximity. Key beats: meet Ch.6 →
  Amelia SEEKS KORVAN OUT and he hides her from his father Ch.10 → adversarial road (11–14) →
  dragon shift with Amelia present Ch.15 → bond turns real + first explicit scene Ch.18 → torn
  apart when the chief DISCOVERS her Ch.21 (she leaves from power, not captured) → choices (22,24)
  → reunion + second explicit scene Ch.26 → Loric outlasted, climax (27–28, Maren the named cost)
  → close (29). Endpoint unchanged (Loric outlasted, Queen never learns his name).

### Pipeline installed on the branch (committed)
- The branch forked from an unrelated history and lacked the pipeline. Installed the canonical
  pipeline from **`knightdx91-alt/book-pipeline`**: `.claude/agents/` (all 12 book-* agents),
  `.claude/commands/` (`/gemini`, `/grok`), `.claude/settings.json` (apodictic enabled) + hook,
  `tools/apodictic/`, and `grammar_check.py` (template + this book). The branch can now run the
  full chapter loop with all gates and agents.

## Drafting
- **Ch.1 "Contraband" [A] — FINALIZED (5,085 words). Genesis Floor 8.5 — PASS.** All 7 dimensions
  8.5 (Pacing + World-building raised 8.0→8.5 after a polish pass). Mechanical gates clean (simile
  2.8/1k, em-dash 1, adverb 10/1k, grammar clean, rhythm 0). Pacing check PASS. Report:
  `evaluations/chapter-1-eval.md`. Establishes the voice benchmark (plain Bishop register — polished
  AWAY from the richer drift, per author's plainer preference), the warm Queen + fond household, the
  cage + its treaty reason, silver hair, strong blood-magyk (NOT a victim — the fire memory), the
  beeswax seed, the wrong laugh, and her active decision to be seen.

## Residual notes to honor in later chapters (from the evaluator — non-blocking)
1. **Ch.2 must deliver external movement** — don't open with a second static interior 5k scene.
2. Ch.2–3 add **non-thematic texture** so the seen-vs-inherit theme doesn't harden into a fingerprint.
3. A later overload beat should **demonstrate Amelia's voice-under-pressure** (flatter/clinical).

- **Ch.2 "The Servants' Passages" [A] — FINALIZED (5,009 words). Genesis Floor 8.5 — PASS.** All 7 dims 8.5. Blood-magyk training (candle + fish, 'never a person' rule planted), cage-as-muzzle reframe, the shifter near-encounter (external movement + first voice-under-pressure), Maren's debt-vs-love. Evaluator polish applied (rationed philosophical asides, closed the landing logic seam, retired the treaty-ending simile). Report: `evaluations/chapter-2-eval.md`.

- **Ch.3 "Unshifted" [K] — FINALIZED (5,002 words). Genesis Floor 8.5 — PASS.** First Korvan POV; voice-differentiation verdict PASS (strongly) — cover-the-name vs Amelia unambiguous, reads adult not teen. Establishes his cage (late-shifter shame, Tam joke), the chief (only family; weather-proverbs; the roan he won't ride; swim memory), Selwyn (friend not confidant), Loric (kind-as-weapon seed), leg-cramp false alarm; shuttered-village world beat. Fixed a mandatory deep-POV break (cut an omniscient Amelia intrusion at the gate) + rationed asides. Report: `evaluations/chapter-3-eval.md`.

- **Ch.4 "The Man Who Only Asks" [K] — FINALIZED (5,004 words). Genesis Floor 8.5 — PASS (round 2).** Round 1 FAILED at 8.0 (Pacing): Loric's menace was SHOWN well then explained 4x, in a static 2nd-consecutive-Korvan chapter. Fix = tighten (cut the redundant telling to one pass) + spike (the Doran/Bret fight actually breaks into fists; Korvan tends a cresset through the wall scene). The fist-fight doubles as a DRAGON-SEED (his body wants violence on time). Fingerprints fixed (doubled ending removed, 'down not away' retired, castle image varied, Korvan/Amelia body bleed). Builds Loric (kindness-as-weapon), the clans as political body, the 'loses either way' lever. Report: `evaluations/chapter-4-eval.md`.

- **Ch.5 "Among People" [A] — FINALIZED (5,010 words). Genesis Floor 8.5 — PASS (round 1 + polish).** The banquet; the front-of-book momentum accelerator. Evaluator called "Wine, my lady?" the emotional high of the book to date. Lands: the mother-as-glacial-Queen ache, the near-miss (silver hair; magyk offered not taken), the dark-pact human cost (Maren tie-in). Seeds for Ch.6-7: the sound-swallowing fountain (exposure engine), the silver-hair giveaway, the Korvan glimpse. Applied voice-maintenance polish (rationed the acoustic device to the load-bearing fountain use; cut clever asides; varied near-verbatim Ch.1 callbacks) to keep Amelia's voice from calcifying across 3 POV chapters. Report: `evaluations/chapter-5-eval.md`.

## Next step (resume point)
Draft **Ch.6 "The Garden" [K] — the meeting, the heart of the book.** Korvan (escaping his own humiliation at the banquet) finds Amelia at the fountain; they talk; the bond = recognition of shared exile (NOT insta-love — guardrail 1). She names her aloneness (clan-of-one seed). The fountain swallows their words -> Loric will SEE, not hear (the exposure engine, Ch.7). Plant the first ungovernable pull (romance seed). ADULT register, two lonely equals. Korvan's voice; watch Amelia-voice rationing (acoustic device, counting) if any [A] interiority; ≤1 aside; vary ending. Then Ch.7 = TP1 exposure. Gates: Bishop voice, style (em-dash ≤10, simile ≤3), grammar, rhythm, >=5,000 words, book-evaluator >=8.5.

## Ch.15 "The First Full Moon" [K] — FINALIZED (5,016 words). Genesis Floor 8.5 — PASS. (2026-07-09)
TP2 (~50%). Korvan's first shift → **dragon**, Amelia the only witness (calendar coincidence, NOT
magic). The epic reveal written as **catastrophe not gift**: clan of one; the first ancestral memory
trickles in situationally (a lost sky full of his own kind — NOT Atlantis-linked) and shows him the
size of what he lacks, then takes it away. Lifelong "body-sensation-as-shift" tic finally pays off
(the one true flutter). Dangerous-devoted engine + Amelia agency guardrail both held (she doesn't run,
calls up blood magyk, and she is the one who stops him flying by counting the cost — a dragon in the
moon would end every clean story). Swim creed pays off: he holds the wings down on purpose, as his
father held back his hand. Hook: torches on the writ-road → Ch.16.
Gates: style (simile 2.6/1k, em-dash 2, no ceiling), grammar clean, rhythm 0 flagged, show/tell no
heavies, voice_wear clean, ≥5,000w. pov-map updated (15: Korvan). Report: evaluations/chapter-15-eval.md.

### Next step (resume point)
Draft **Ch.16 "The Morning After a Body" [K]** — human again; what the shift means sinks in; the
dragon's flight/shape was seen and rumor races toward Loric. Now Korvan is unmistakably the monster
the propaganda promised and Amelia unmistakably the witch; proximity cuts both ways (each is now the
exact thing the other's people fear). A second, sharper memory-fragment (grief of a dead clan). The
searchers/torches from Ch.15's close are on them. Subversion: no mastery, only consequence. Gates as
usual (Bishop voice, style em-dash≤10/simile≤3, grammar clean, rhythm, show/tell, ≥5,000w, Floor ≥8.5).

## Ch.16 "The Morning After a Body" [K] — FINALIZED (5,082 words). Genesis Floor 8.5 — PASS. (2026-07-09)
The consequence of TP2. Picks up on the rock from Ch.15's close: the reeve's searchers reach them;
the untrained dragon kills a fleeing boy (camera cut on the act — darkness rule); Amelia steps
between the dragon and the crossbows and defuses five armed men with cold restraint, killing none,
holding her "never a person" rule (Ch.2 payoff). Thesis: "She was the witch who held her hand. He
was the monster who could not." Forced flight (animal panic) = the dragon is SEEN by the whole
valley — the thing she begged him not to do; the alarm-bell wakes the camp and rumor now races to
court + Loric. Second ancestral memory = the EXTINCTION of dragonkind (beacon-chain, wings falling;
situational, NOT Atlantis). Revert in the wood; the human aftermath (sick, shaking); Amelia's
unsoftened honesty ("it was you, and you didn't choose it, and both are true and they don't cancel")
and first touch as a man. Korvan asks her to teach him the rule. Hook: the world now knows exactly
what they are.
Gates (via tools/check_chapter.sh 16): style (simile 1.6/1k, em-dash 6, no ceiling), grammar clean,
rhythm 0, show/tell clean (filter 7.1, abstract 5.1 — needed a convert-to-scene pass: expanded the
confrontation/flight/revert as concrete scene, dramatized the extinction memory into images), voice-
wear clean (removed one retired "never once"), 5,082w. pov-map updated (16: Korvan).
Continuity: searchers = reeve's men, kept distinct from the chief's captain Bricc; bolt-wound carries
into the human shoulder; alarm-bell is one continuous event (starts in flight, still tolling at close).
Report: evaluations/chapter-16-eval.md.

### Next step (resume point)
Draft **Ch.17 "Banner" [C] (Queen / Maren, court)** — a COURT-CUTAWAY chapter (POV shifts off Korvan;
Queen Rosalia / Maren). Word of the dragon reaches court; Amelia's magyk + Korvan's dragon are made
into a war-banner — "the vampire witch and her dragon" — by her OWN side. The Queen maneuvers and
every reasonable move feeds Loric. Maren's torn loyalty sharpens; she's made to carry a message that
could damn or save Amelia. Subversion: her own side weaponizes her exactly as her enemies do. NOTE:
new/under-used POV — establish/refresh the court voice; add "17: Queen" (or Maren) to pov-map. Gates
as usual (Bishop voice, style em-dash≤10/simile≤3, grammar clean, rhythm, show/tell, ≥5,000w, Floor ≥8.5).

## VOICE-FIDELITY PASS + new metaphor/sentence gate (2026-07-09)
Added `tools/metaphor_check.py` — style_check only counts SIMILE markers; it was blind to bare
METAPHOR and to Bishop's plain SENTENCE SHAPE. New tool measures combined figurative load (≤4.0/1k)
and share of sentences >40 words (≤18%; Bishop is clipped — Ch.1 benchmark ≈11%). Wired into
check_chapter.sh (gate 5b) and documented in CLAUDE.md.
Finding: Ch.15/16 had drifted to ~25% long rolling and…and…and sentences (highest in the book) —
off-comp for Bishop. Did a sentence-splitting pass on both (split the longest into plain declaratives,
varied openers to avoid trading long-sentences for anaphora) and trimmed clustered ornament metaphors
in Ch.16 (dropped 'sail', 'coin', 'machine'). Result: Ch.15 %>40 25.1→17.6 (fig 2.2), Ch.16
25.1→15.3 (fig 3.6→2.6), both now in the Bishop band; all other gates still clean; word floors held
(5,001 / 5,027). LEGACY: Ch.5 (20.1%), Ch.11 (19.7%), Ch.12 (24.6%) predate the tool and remain over
the long-% ceiling — sweep them on the next revision pass (non-blocking).

## METAPHOR GATE BROADENED + legacy sentence-length sweep (2026-07-09)
Broadened metaphor_check.py to detect figurative language by CONSTRUCTION across six frames
(like/as-if similes, "as ADJ as", "X of himself", copular "was a <vehicle>", "turned/gone to
<material>", appositive image-nouns) instead of a bare ornament list — catches bare metaphor the
old version missed. Finding: with broad detection, NO chapter exceeds the figurative ceiling
(1.0–4.2/1k), so metaphor density is genuinely fine book-wide; the real drift was sentence length.
Swept the three legacy long-sentence offenders to the Bishop band (split longest into plain
declaratives, varied openers to avoid anaphora): Ch.5 20.1→17.9%, Ch.11 19.7→16.9%, Ch.12
24.6→16.7%. Whole book now passes metaphor_check (all <18% long sentences, all under fig ceiling);
rhythm/grammar/show-tell/voice-wear all still clean; word floors held (5,208/5,008/5,030).

## Ch.17 "Banner" [Maren/court] — FINALIZED (5,031 words). Genesis Floor 8.5 — PASS. (2026-07-09)
First solo MAREN POV (court cutaway, ~55%). Dragon news reaches court; the war party (Lord Verrin)
moves to make Amelia a war-banner — "the vampire witch and her dragon" — while Lady Corenne counts
the cost (every reasonable move feeds the grey man). Subversion: her OWN side weaponizes her exactly
as the hunters do — a dead girl is at least a girl; Verrin wants her alive as a *sign*. The Queen
maneuvers to be first to find her own daughter, then sends Maren north with a six-word message —
"you may be seen, cage open" — knowing Maren is both the warning and the arrow that points hunters at
Amelia. Queen stages a public betrayal (loud anger) to cover Maren's leaving. Maren's silver-counting
tic carried exactly from Ch.2/9/11 (verified before drafting — it's MAREN's, not Amelia's).
Gates (check_chapter.sh 17): style (simile 1.6, em-dash 8, no ceiling), grammar clean, rhythm 0,
metaphor/sentence clean (fig 1.8, %>40 12% — plainest chapter yet), voice-wear clean (removed 3
retired "never once"), 5,031w. show/tell: filter 8.5 OK; abstract 6.2 marginally over, ACCEPTED
in-band (deep-POV court interpretation; Ch.9 precedent shipped at 6.6). Drafted short (3,966) then
expanded with SCENE (council counter-voice + departure), not reflection. pov-map: 17: Maren.
New court names: Lord Verrin (war party), Lady Corenne (caution). Report: evaluations/chapter-17-eval.md.

### Next step (resume point)
Draft **Ch.18 "What the Road Made" [K+A braided] — FIRST EXPLICIT SCENE (~62%)**. Deep in forced
proximity the adversarial edge wears through to something real, EARNED by everything survived (not
attraction-at-first-sight). The bond turns genuine and charged; the first full explicit scene lands
here — Bishop's build with a step past her on graphic detail, deep POV, emotionally loaded, the
dangerous-devoted restraint doing the work. Two equals CHOOSING each other (she powerful in her own
right, not led). Dark intensity underneath (what they're becoming, what it will cost). Subversion:
the turn is a DECISION, not a swoon. HEAT PLACEMENT per canon (STATE.yaml/voice-dna §3): explicit,
back-half, restraint-tension; NO sexual violence. Braided K+A POV — hold deep-POV discipline within
each strand. Gates as usual + keep %>40 <18 and fig <4 from the first draft this time.

## Ch.18 "What the Road Made" [K+A braided] — FINALIZED (5,025 words). Genesis Floor 8.5 — PASS. (2026-07-09)
FIRST EXPLICIT SCENE (~62%). Four days of hunted forced proximity (adversarial + costly) wear the
edge through to a chosen turn in a shepherd's hut. Written against romantasy defaults per the 4
anti-cliche guardrails: NOT fated-mates (shared-exile bond), NOT a swoon (the turn is Amelia SETTING
DOWN THE ARITHMETIC — her signature device pays off by being renounced), NOT a rescue (she crosses
the fire, names it, keeps full agency, holds her "never a person" rule hardest on the one she'd break
it for). Dangerous-devoted engine at its clearest (the leash; "sooner die than do her harm"). Too-hot/
too-cold motif (Ch.12) pays off in the flesh. Explicit but emotionally-loaded/restraint-forward per
canon (STATE + voice-dna §3); NO sexual violence (feeding hunger held away from intimacy on purpose).
Dramatic irony braided with Ch.17: Maren walks north with "you may be seen, cage open" while Amelia
has already opened the cage herself. Beats: dawn hare-fight, bracken near-miss, the sound in the dark
("every stone, for the rest of our lives"), sleeping-watch coda.
Gates (check_chapter.sh 18): style (simile 1.6, em-dash 8, no ceiling), grammar clean, rhythm 0,
show/tell clean (filter 8.5, abstract 5.6 — drafted heavy at 12.1/7.0, fixed by rendering the scene +
adding SCENE), metaphor/sentence clean (fig 1.6, %>40 16.8%), voice-wear clean, 5,025w. Drafted short
(3,721) then expanded ~1,300w as scene, not reflection. pov-map: 18: Amelia (braided K+A).
Report: evaluations/chapter-18-eval.md.

### Next step (resume point)
Draft **Ch.19 "A Dragon Can't Hide" [K]** (ACT II-C opens, ~62-72%). Korvan tries to opt out — to be
no one's weapon — and learns a dragon cannot disappear; both sides want or fear him. Loric makes his
first move to claim or destroy the dragon-asset. Selwyn offers plainly to come with him — and Korvan
can't bring anyone where he's going, and can't even say why (the secret still his alone). Subversion:
he declines both confidant and escape and finds the door already shut behind him. Gates as usual, and
KEEP THE DISCIPLINE FROM THE START: draft to >=5,000 words (stop under-writing), plain sentences
(%>40 <18), fig <4, filter <9, then run check_chapter.sh 19.

## Ch.19 "A Dragon Can't Hide" [K] — FINALIZED (6,457 words). Genesis Floor 8.5 / avg 8.71 — PASS. (2026-07-09)
ACT II-C opens. Korvan's opt-out plan (Get her clear / Take himself off / Go small / Want nothing) built
at the open and demolished at the close — a dragon cannot disappear. Amelia (agency intact) sends HIM
down to a drover's steading for food (she is the recognizable one — silver hair, the bounty — and the
deadlier watch; she holds the height). On the byre door: the Queen's smeared-seal writ (the girl, ALIVE,
Ch.14) beside Loric's FIRST MOVE — a sealless, nameless writ paying DOUBLE for the dragon dead and
"brought low, seen, public," so a grieving Queen watches her banner turn to a carcass. Korvan reads the
uncostable emotional motive correctly ("It had costed the grieving out to the copper"). Selwyn tracks the
Ch.14 north-shoulder trail up (3 days, hill-pony) and offers plainly to come — the dramatic-irony engine:
he'd guard Korvan against the dragon, not knowing Korvan IS it, so his offer is to guard the man against
himself, and Korvan cannot say why he refuses. Subversion: declines confidant AND escape; Selwyn hands
him the door-shut truth ("It shut when the dragon crossed the dawn... for everyone who ever stood near
you"). PULL: Korvan's own fresh tracks up the compromised trail lead every knife to Amelia's exposed
rock; he hears horses quartering up the fold; he runs. Sets up Ch.20/21 "Discovered -> torn apart."
Gates (check_chapter.sh 19): style (simile 1.5, adverb 3.9, em-dash 9 — no ceiling), grammar clean,
show/tell clean (filter 5.9, abstract 3.6), metaphor/sentence clean (fig 2.7, %>40 15.7%), voice-wear
clean, 6,457w. 3 rhythm flags = the sanctioned bookended plan-motif anaphora (score 4, well under 18
gate). Blocking mechanical fix cleared: recast the "tide comes up under ice" 5-gram (echoed Ch.18) to
"frost seals a latch in the night." pov-map: 19: Korvan. Report: evaluations/chapter-19-eval.md.
Non-blocking watch (from eval): chapters 18 & 19 are the two longest — keep Ch.20 in the ~5,000-5,400
band; watch the Korvan-POV rhetorical-triad habit so it doesn't calcify.

### Next step (resume point)
Draft **Ch.20 "The Shape of the War" [Court/Amelia]** (~55-65%). The war turns from rumor to front line;
the human cost becomes concrete — Maren's home village named on a casualty list at court. Amelia (still
on the road) does something small, forbidden, and EFFECTIVE to help — and it terrifies her that it
worked; she crosses fully from enduring to ACTING. Plant the logistics that make the Ch.27-28 climax
possible. Subversion: her first action is small and illicit; the success scares her more than failure
would. KEEP IT IN THE ~5,000-5,400 BAND (the back half is trending long). Gates as usual; plain
sentences (%>40 <18), fig <4, filter <9; then run check_chapter.sh 20.

## Ch.20 "The Shape of the War" [Court+Amelia braided] — FINALIZED (5,391 words). Genesis Floor 8.5 / avg 8.86 — PASS. (2026-07-09)
Braided 4-scene chapter (hard breaks), war as ABSTRACTION-BECOMING-A-NAMED-PERSON on both strands.
MAREN strand: reaches muster town Elverford (last bridge before the hill country) — rumor turned to a
front line; the levy called, Verrin's "gift" won, Corenne lost (the Ch.17 long-room machinery ground
out). Gut-punch: a casualty list on the church door, her birth-village MILLBECK read not as names but a
walk down her own childhood lane, every door crossed out, ending on her aunt Sib (earned via her
counting-self; killer detail administrative — "indented to save ink"). AMELIA strand (arc pivot): off
the Ch.19 compromised trail into refugee country, comes on a wain-crash and a bleeding child; reaches
into the blood with her mother's forbidden reach — not to STILL a heart (Ch.13) but to hold a torn
vessel shut, telling the blood to stay. Works with no resistance. The terror is the EASE — her mother's
"law" was a fence built a mile short of her real edge; she stood one decision from the treaty's making-
taboo. She acted BEFORE the arithmetic (signature counting-device subverted by being SKIPPED); crosses
enduring -> willed action. CLIMAX LOGISTICS PLANTED (understated): both strands name the FORD AT
ELVERFORD as the war's convergence point; a grandmother gives Amelia the unwatched OLD SALT ROAD that
crosses the Elver above the ford (the Ch.27-28 route). Ch.21 hook: a silver-haired woman who "gives
life back" is now a rumor running the roads toward Loric.
Eval verdict: PASS, avg 8.86, 5 dims at 9.0 (Prose & Pacing hold the floor at 8.5). Maren/Amelia voices
distinct (cover-the-name passes; Maren counts to REFUSE and speaks in negatives, Amelia counts to
SURVIVE and reasons spatially). Low dialogue (~3.6%) judged JUSTIFIED (both POVs structurally silent:
Maren eavesdropping, Amelia hooded) — not force-converted. Required mechanical fix cleared: recast the
"two was habit / three was surrender" maxim (was 3x across Ch.17+20) — kept only its Ch.17 coinage,
enacted in fresh words in Ch.20. Optional polish applied: cut the restating post-act ¶ (enduring->acting
told), let ¶95 (thesis, earned/interior) + the mud-prints close ("she would do it again") carry it.
Gates (check_chapter.sh 20): style clean (simile 1.3, em-dash 1, 0 semicolons), grammar clean,
metaphor/sentence clean (fig 2.2, %>40 6.3%), voice-wear clean, 5,391w. pov-map: 20: Amelia.
Report: evaluations/chapter-20-eval.md.

### Next step (resume point)
Draft **Ch.21 "Discovered" [K] -> TORN APART** (~65-75%, a TP2-consequence hinge). The hunt closes:
the pair are found (Korvan's back-trail from Ch.19 + the "gives-life-back" rumor from Ch.20 converging).
This is the outline's "TORN APART" beat — Korvan and Amelia are separated (captured/scattered/one drawing
pursuit off the other — writer's call, consistent with Loric's dragon-bounty and the Queen's "alive"
writ pulling them to DIFFERENT captors). First situational DRAGON-MEMORY may trickle here (canon: NOT
Atlantis-linked; never an info-dump). Raise the cost of Ch.18's choice ("every stone in the dark").
Keep the ~5,000-5,400 band. Gates as usual; then run check_chapter.sh 21.

## Ch.21 "Discovered" [K] — TORN APART — FINALIZED (5,600 words). Genesis Floor 8.5 / avg 8.79 — PASS. (2026-07-09)
The TP2-consequence hinge. Now delivers BOTH outline beats. Beat 2 (added this pass, editor):
a father-son RUPTURE on the drove-road — the chief + a mounted clan party (Bricc + riders)
intercept Korvan and Amelia in daylight; the chief sends his men off and confronts his son alone.
The Ch.10/14 doubled secret detonates — not that the bond exists (he privately knew since Ch.14,
per canon) but that a season after "get her off my mountain" the son is STILL sheltering the
silver-haired vampire and walking her toward court, putting both halves of the war-banner (witch
+ dragon) in one place. Verdict: "You've made the lie true, Korvan. And you did it on a drove-road
in the sun." Swim-creed payoff (Ch.14): "I let go of your belly in that river so you'd not drown
reaching for me. So don't reach. Swim." — the hand that steadies is the hand that drowns you, made
literal, and it now RHYMES with Amelia sending Korvan away at the crossing (Korvan sees where she
"learned it"). Amelia keeps full agency: the chief feels her weigh dropping his four men and names
that she CHOOSES not to ("You'd have made a hard daughter") — no damsel. The chief can't be seen
to let them cross the watched ford, so he forces them up onto the poor's shelf above it ("thin
water, no toll, no one who counts") — his last protective act sends them into the trap, landing on
the preserved line: "The salt road was the safe way because everyone used it. That was the thing
that killed it." Chief rides off, gone before the crossing.
Beat 1 (preserved): the whale-iron crossing ambush. Amelia reads the trap, sends Korvan UP/OVER/AWAY
(the iron only reaches the shelf) to draw the hunt off her; a leg-shot triggers his involuntary
shift; he flies west leading the whale-iron crew off her while she lets three men walk her south
alive (hands unclosed — the harder sum). First OUTWAITED-CLAN dragon-memory trickles in the tearing
(¶ mid-chapter): a few went to ground under the mountain and outlasted the hunt — NOT Atlantis-linked;
seeds the climax logic. Ending hook preserved: "...into a country with no one in it to bring him low
and no one in it at all."
MECHANISM-SWAP NOTE (logged per CLAUDE.md): the outline's beat-2 was originally a camp/clan scene;
delivered here as a road interception instead so the geography holds (chief absent from the crossing,
Korvan flees alone). Both prior eval flags cleared (outline deviation retired; long-sentence %>40w
resolved to 10.4%).
Eval verdict: PASS, avg 8.79, 5 dims at 9.0 (Prose & Pacing hold the floor at 8.5), Casual 9/10.
The "did not do things that came to nothing" father/Amelia mirror KEPT as intentional resonance
(logged sanctioned in feedback/style-flags.md).
Gates (check_chapter.sh 21): style clean (simile 1.4/1k, em-dash 1), grammar clean, metaphor/
sentence clean (fig 2.7/1k, %>40w 10.4%), show/tell clean (filter 5.4, abstr 2.7, dialogue 28.2%),
voice-wear clean, rhythm 2 flagged (pre-existing accepted crossing beats). 5,600w. pov-map: 21: Korvan.
Report: evaluations/chapter-21-eval.md (supersedes the pre-revision eval).

### Next step (resume point)
Draft **Ch.22 "Survive to Fight Later" [K] — TP3 for Korvan (~76%)**. Per outline (~line 206): the
chief asks Korvan to be USEFUL — to let the dragon be leveraged. Moral clarity asks him to refuse.
Korvan chooses to ACT where his father only waited, naming a THIRD path (neither the chief's
instrument nor a runaway). Dragon memory trickles the lore that makes it possible (the outwaited-clan
"go to ground / outlast" seed from Ch.21 pays into strategy). The chief is RELIEVED, not betrayed.
Subversion: a quiet handoff — the pragmatist blesses the clarity he couldn't afford. NOTE the Ch.21
geography: Korvan flew off WEST alone into empty country and the chief is back at the ford — Ch.22
must re-stage their contact plausibly (Korvan's arc turns from fleeing to choosing; the father-son
channel reopens after the drove-road rupture). Keep the ~5,000-5,600 band. Gates as usual; then run
check_chapter.sh 22.

## Ch.21 RE-EDIT (2026-07-10) — continuity + canon fix (still Floor 8.5)
Continuity audit (triggered by the added father-son scene) + author ruling ("through Ch.21 only
Amelia and Korvan know Korvan is the dragon"). Three surgical fixes to the drove-road scene:
(1) removed the chief's premature dragon-KNOWLEDGE — he now confronts Korvan ONLY about sheltering
the VAMPIRE ("the one secret I built the whole war to bury, out taking the sun"); the painted
witch-and-dragon banner is explicitly his own INVENTED propaganda, not something he knows his son
embodies. Added a single SILENT unvoiced flicker (his eyes rest a beat past their business on his
late-shifter son, "a second thing he could almost name and could not") that Ch.22 pays off.
(2) CRITICAL war-order fix: "a season ago. I've declared a war since" INVERTED canon (war declared
Ch.8, BEFORE the "get her off my mountain" order in Ch.14) → "a fortnight ago, with a war already
declared." (3) Duration fix: "a season" → "a fortnight" (actual road-clock Ch.14→21 ≈ 10-12 days).
Swim-creed payoff preserved. Gates re-clean (5,674w; grammar clean; long% 10.8%). Canon logged in
STATE.yaml (WHO-KNOWS-KORVAN-IS-THE-DRAGON, 2026-07-10): chief becomes a knowing secret-holder from
Ch.22 on (new leak vector for Ch.23+).

## Ch.22 "Survive to Fight Later" [K] — TP3 — FINALIZED (5,446 words). Genesis Floor 8.5 / avg 8.86 — PASS. (2026-07-10)
Korvan's TP3 (~76%). THREE movements. (1) Three days mostly-dragon in the empty west; on the fourth
he shifts back to a man by a black tarn and does Amelia's cold arithmetic — recognizes that staying
west to "outlast it in the folds" is his FATHER'S door (wait/vanish). Refuses it; turns EAST. (2)
Flies back across a country the war has lit with beacons/muster-fires; learns the dragon is TWO things
(the loud shape AND the cold-stone thing that goes dark and moves between the fires) — a situational
dragon-memory FACET (outwaited-clan seed from Ch.21; NOT Atlantis, in the meat not the mind) — and
crosses a hundred miles unseen to the war-train. (3) Lands half a mile off, folds into a man; the camp
panics; the CHIEF walks up alone with a torch — and LEARNS his son is the dragon LIVE ("here it comes
down the sky and it's my own boy" — reframed as genuine discovery, the certainty landing in the body,
echoing the Ch.21 silent flicker). The chief's pragmatism wakes: asks Korvan to BE USEFUL — fly one
pass over the Crown host at the falls, be the banner made true, save a thousand clan lives ("be the
clan's dragon"). The temptation has teeth (true + offers the belonging the late-shifter always wanted).
Korvan feels it, then thinks of the foot of water at the ford: his father is asking, in the kindest
voice, for the exact thing the whale-iron wanted — the dragon shown/spent/string-pulled. He refuses
the INSTRUMENT and the RUNAWAY, names the THIRD path: go dark, move UNDER the war unseen, cross to the
capital, come up at the hour he chooses and take the CAUSE (Loric) off the board. Subversion delivered:
the chief is RELIEVED not betrayed — admits he's SEEN the clean door the whole war and couldn't afford
it (a chief who spends himself leaves his people leaderless); his son taking the clarity off his hands
is a weight he didn't know he carried. Closes with the swim-creed INVERTED ("Go and do the opposite of
it for once. Go and get the thing back") and Korvan calling the shift by his OWN hand for the first
time (not from fear), turning east toward Amelia. Runway to Ch.23 (Loric/court) + Ch.25-26 reunion.
Eval verdict: PASS, avg 8.86, 5 dims at 9.0 (Prose & Pacing hold the floor at 8.5), Casual 9/10.
(a) father-son contact earned (Korvan comes to him), (b) genuine third-path subversion + agency,
(c) dragon-memory situational/not-Atlantis, (d) Bishop voice/no named emotion, (e) no Ch.18/Amelia
conflict — all confirmed. Ch.21→22 callback phrases recast/logged as sanctioned mirrors
(feedback/style-flags.md + korvan-voice-ledger.md).
Gates (check_chapter.sh 22): style clean (simile 1.1/1k, em-dash 2), grammar clean, metaphor/sentence
clean (fig 1.8/1k, %>40w 17.2%), show/tell clean (filter 6.2, named-emotion 0.0, dialogue 23.7%),
voice-wear clean, rhythm 0 flagged. 5,446w. pov-map: 22: Korvan. Report: evaluations/chapter-22-eval.md.

### Next step (resume point)
Draft **Ch.23 "The Cause of Every Death" [Court — C/A]** (~80%). Per outline (~line 213): Loric
engineers a public moment framing Amelia and Korvan as the CAUSE of every death so far. The Queen
finally acts — and it's the WRONG save, making it worse. Maren's choice comes due; she acts (or
refuses) at a cost, giving Amelia's public ordeal a private human price. Loric, winning, hears his
father's laugh, and it curdles the win. Subversion: truth is offered and changes nothing — the thesis
made literal. NOTE canon (2026-07-10): the chief now knows Korvan is the dragon (Ch.22) — account for
it as a possible leak vector if the court thread touches clan intelligence. Keep the ~5,000-5,600 band.
Court POV (Amelia arriving south / Maren) — confirm the [C/A] blend and log pov-map. Gates as usual;
then run check_chapter.sh 23.

## Ch.23 "The Cause of Every Death" [C/A court] — FINALIZED (5,016 words). Genesis Floor 8.5 / avg 8.86 — PASS. (2026-07-10)
The book's thesis made literal: truth is offered from every side and changes nothing — it even makes
things worse. POV braided with hard section breaks, leading with AMELIA (hooded, arriving south at the
town of Dunmoor) and MAREN (court thread, converged on the road), plus one sanctioned LORIC close-third
flicker (voice-dna's "grief breaks through once, reader sees, no one else"). Logged to pov-map.txt.
Movements: (1) Loric stages a public "reckoning" at the market cross — reads the war's dead aloud and,
without a direct accusation, lets a grieving crowd weld the fortnight of the burnings to the fortnight
the witch and the dragon were seen, handing them a face for their grief. (2) Amelia, in the crowd,
holds the WHOLE truth (the clans raided first, the chief declared the war, Loric lit all of it) and
knows speaking it would change nothing — the crowd came to bury a grief, not to buy a truth. (3) The
Queen "finally acts" and it's the WRONG save: a Crown decree publicly names Amelia her acknowledged
daughter under royal protection — meant to shield her, it confirms in the throne's own wax the one
thing accusation could never prove (the natural-born vampire is real and the Queen's), making the girl
the cause of every death and handing Loric his win. (4) Maren's choice comes due — she crosses the
packed square to put the Queen's true private word in Amelia's ear ("the free part was true before she
ruined it") and is SEIZED for it: the public catastrophe given a private human price. (5) Loric,
winning, hears his dead father's laugh come up out of his own chest and it curdles the win (the Queen
will win or lose without ever learning his name). Runs Amelia to her Ch.24 resolve: not hidden, not
shown, but SEEN on the hour and ground she chooses. Chief-knows-dragon leak vector left untouched.
Eval verdict: PASS, avg 8.86, 5 dims at 9.0 (Prose & Pacing hold the floor at 8.5), Casual 9/10.
Gates (check_chapter.sh 23): style clean (simile 2.4/1k, em-dash 3, adverb 4.0/1k), grammar clean,
metaphor/sentence clean (fig 4.0/1k at ceiling, %>40w 16.9%), show/tell clean (filter 8.2, named-emotion
0.0, dialogue 8.5% — interior-court mode, judged earned by the eval), voice-wear clean, rhythm 2 low
anaphora flags (score 3-4, under fail threshold). 5,016w. pov-map: 23: Amelia (braided C/A + Loric flicker).
Report: evaluations/chapter-23-eval.md. WATCH (non-blocking, next line-pass): split one 90-103w anaphoric
roll (Prose lever) + one concrete sensory beat in the oration middle (Pacing lever); fig/1k sits at the 4.0 ceiling.

### Next step (resume point)
Draft **Ch.24 "Seen on My Own Terms" [A] — TP3 for Amelia** (~83%). Per outline (~line 218): Amelia
STOPS hiding — chooses to be visible deliberately, accepting she'll be misread, denying Loric the
secret he weaponizes. Her blood magyk used BY HER WILL for the first time — now a lethal, defiant act,
not a granted wish. Mirrored against Ch.1 (the contraband/cage open). Subversion: the public reveal is
bleak CONTROL and sacrifice, not triumph. Picks up directly from the Ch.23 Dunmoor square (Maren taken,
the Crown seal read, the crowd handed its face for grief). Keep the ~5,000-5,600 band. Amelia POV; log
pov-map. Gates as usual; then run check_chapter.sh 24.

## Ch.24 "Seen on My Own Terms" [A] — TP3 (Amelia) — FINALIZED (5,005 words). Genesis Floor 8.5 / avg 8.86 — PASS. (2026-07-10)
Amelia's third-act turning point (~83%). Single POV (Amelia); pov-map "24: Amelia". Picks up directly
from the Ch.23 Dunmoor square (Maren seized, Crown seal read). She turns south, then REFUSES both saves —
her mother's Crown-seal rescue (being SHOWN) and Maren's order to flee (being HIDDEN) — and walks back into
Dunmoor. Instead of extracting Maren with her old skill of being no one, she deliberately steps into the
open at the market cross, takes down her hood before four hundred people, and NAMES herself before anyone
can name her ("There's no witch. There's me / I'm real"), denying Loric the hidden-witch SECRET that is his
whole engine (a declared monster, not a discovered one). When his men come she uses her inherited blood
magyk BY HER OWN WILL for the first time — stops six hearts, cold and clinical — the lethal INVERSION of
Ch.13 (held seven, spared them; that mercy now named as the costlier error). SUBVERSION (bleak control, not
triumph): Loric tells her, mildly and correctly, she's done his night's work better than he could — she's
won only the FRAME (the hour and ground of being seen), not the TRUTH (still unprovable), and made herself
the confirmed monster who'll be hunted faster. Maren, freed, doesn't reach back. No catharsis; the
"seen at last" want arrives as a colder cage. DENSE Ch.1 mirror/inversion (almond cakes, winter-water gown,
the slow bolt, "you must not be" -> "I'm real", the blood pressed down her whole life let up and used,
"hidden and seen were the same wall"). Ends turning EAST toward the war and the dragon — yearning runway
into Ch.25. Korvan kept off-page (recalled only as the one stranger who saw her without a frame);
chief-knows-dragon thread left untouched.
Eval verdict: PASS, avg 8.86, 5 dims at 9.0 (Prose & Pacing hold the floor at 8.5), Casual 9/10.
Gates (check_chapter.sh 24): style clean (simile 1.4/1k, em-dash 2, adverb 8.2/1k), grammar clean,
metaphor/sentence clean (fig 1.8/1k — under the 4.0 ceiling, %>40w 15.7%), show/tell clean (filter 7.0,
named-emotion 0.0, dialogue 9.3% — reveal+blood-magyk action, judged earned by eval), voice-wear clean
(agent removed a "never once" x3 hard-fail from its own draft; "twenty years" reduced to 1). 5,005w.
Report: evaluations/chapter-24-eval.md. WATCH (non-blocking, next line-pass): convert the three
narrated-meaning scene-end codas (¶91/121/123 — ¶91 and ¶123 re-state the same "sum"; cut one, land the
other on an image) + split the ¶61 101-word and-roll into two clipped sentences (Prose/Pacing levers toward 9.0).

### Next step (resume point)
Draft **Ch.25 "Toward the Same Fire" [K+A] braided** (~86%). Per outline (~line 226): both leads commit
to the SAME theater of war; the torn-apart threads begin to close the distance. The strongest YEARNING
beats — each moving toward the other and the climax, a NEAR-MISS that cranks the ache (they do NOT reunite
here — that's Ch.26, the explicit payoff). Loric's net tightens on BOTH. Subversion: the book STRETCHES the
distance at the act break instead of rushing them together — the wanting is the engine. Braided K+A POV
(hard section breaks, no head-hop); log pov-map. Continuity: Amelia turning east from Dunmoor (Ch.24);
Korvan gone dark/moving under the war toward the capital+Loric (Ch.22). Keep the ~5,000-5,600 band.
Gates as usual; then run check_chapter.sh 25.

## Ch.25 "Toward the Same Fire" [K+A braided] — FINALIZED (5,468 words). Genesis Floor 8.5 / avg 8.86 — PASS. (2026-07-10)
The convergence chapter that REFUSES convergence. Braided K/A/K, three hard-broken sections, two distinct
voices (differentiation matrix held, no bleed). pov-map "25: Korvan+Amelia (braided)". Korvan, going dark
and crossing under the war as a man to gather news, overhears at a muster-town fire that the silver girl
declared herself and stopped six hearts at Dunmoor — she's no longer a protected "purse" but the
most-hunted thing on the frontier, and she's walking EAST toward the front. He understands in the stomach
that she's walking toward the fire because he's in it, and he's crossing the country because she's walking
into it — each hurling themselves at the deadliest ground because the other will be on it. Amelia, moving
east against the refugee tide with Maren, names to Maren why (the one stranger who saw a person not a use)
and shelters at nightfall in a byre above river-town Kell. She sees the dragon cross the moon, KNOWS it's
him, and could light a signal-fire that would bring him down to her that hour — and REFUSES, because
calling him down makes him the dragon SHOWN, seen by an army, the one thing his whole crossing was to
avoid. From above, Korvan nearly comes down to a single crack of lamplight he can't trust his starved eye
about, and makes himself fly on to keep her unfound, telling himself it wasn't her. SUBVERSION delivered:
the near-miss is not bad luck but a MUTUAL ACTIVE sacrifice out of the same love (the Ch.22/24 "throw the
wanted thing away so it lives" pattern turned literal); dramatic irony (she knew; he never will); ends on
ache not relief, Korvan facing east toward the falls where the next place their roads can meet is the
middle of the fire. Loric's two nets (silver-hunt + whale-iron dark-of-moon crews) tighten toward the same
square mile. No reunion, no explicit scene spent here.
Eval verdict: PASS, avg 8.86, 5 dims at 9.0 (Prose & Pacing hold the floor at 8.5), Casual 8.5 (slightly
under Ch.24's 9 — Korvan crossing is interior/summary-heavy at 7.6% dialogue; doubled near-miss asks the
beat twice). Gates (check_chapter.sh 25): style clean (simile 0.7/1k, em-dash 3, adverb 5.1/1k), grammar
clean, metaphor/sentence clean (fig 1.1/1k, %>40w 11.0%), show/tell clean (filter 7.9, named-emotion 0.0,
dialogue 7.6%), voice-wear clean, rhythm 7 low anaphora flags (score 3-4, under threshold). 5,468w.
Report: evaluations/chapter-25-eval.md. WATCH (non-blocking, next line-pass): trim one of the three
"it had not been her" restatements (¶127); land the ¶131/¶37 codas on image/action not narrated meaning.

### Next step (resume point)
Draft **Ch.26 "The Reunion" [K+A braided] — EXPLICIT PAYOFF** (~90%). Per outline (~line 231): they
REUNITE at the war's edge, no longer the people from the garden, and choose each other DELIBERATELY. The
full open-door/explicit intimacy beat lands HERE (Bishop voice+build with a step past her on graphic
detail — deep POV, emotionally loaded, restraint-tension, earned by the whole arc; the SECOND and most
explicit of the book's two scenes, ~90% heat per STATE.yaml — first was Ch.18). Dangerous-devoted fully
realized: lethal to the world, his hands careful with her. Subversion: NOT romantic-reunion catharsis nor
doomed parting — a clear-eyed MUTUAL CHOOSING, love as a decision by two people with nothing prefab to
inherit it from. Continuity: converges from the Ch.25 near-miss (Amelia at/near Kell moving to the falls;
Korvan east toward the falls) — the reunion is at the WAR'S EDGE, the falls where the climax (Ch.27-28)
will join. NO sexual violence; dark intensity. Braided K+A; log pov-map. Keep ~5,000-5,600 band (may run
to the top of the band given the payoff). Gates as usual; then run check_chapter.sh 26.
