# Whole-Book Line Edit — Findings (2026-07-10)

Lens: `feedback/line-edit-checklist.md` (Crucible editor references + this book's calibrated gates).
Method: ran the full `tools/` suite across all 29 chapters + read the two explicit scenes in full.

## 1. Deterministic gates — status
| Check | Result |
|---|---|
| Simile / "like·as if·as though" per 1k | **Clean** — every chapter ≤ 3.0 ceiling (peaks Ch.7/8/10/13 = 3.0) |
| Em-dash per chapter | **Clean** — max 9 (Ch.18/19), ceiling 10 |
| Adverb (-ly) per 1k | **Clean** — max 11.3 (Ch.7), ceiling 20 (allowed, Bishop) |
| Metaphor / sentence-shape | **Clean** — figurative load & long-% within ceilings |
| Grammar | **Clean** — 0 errors; only LONG-SENTENCE notes (Ch.27/28/29) |
| Voice-wear (per POV) | **Clean** — no retired phrase, no device over cap |
| Show/tell | Row-clean; book-wide heavies listed below |
| Rhythm | 23 flags, clustered Ch.28/29 (anaphora) |
| Tics | Spikes Ch.27 (3.8/1k), Ch.18/21/28 (2.1–2.3/1k) |
| Repeated phrases | 634 n-gram flags — the main finding (below) |

## 2. Real findings (the line edit's actual to-do)

### 2a. Phrase echoes — climax cluster (Ch.25–29)
The n-gram check is dominated by incidental repetition in the battle/climax run, not the
front act. Recurring construction tics to vary:
- **"the [adj] thing / the thing that…"** — "the loudest thing," "the strongest thing on,"
  "a thing that happened," "the thing that told," "reach of the thing."
- **"the whole [X]"** — "the whole east bank," "the whole of the weapon," etc.
- **battlefield geography** repeated verbatim: "roar of the falls / roar of the water,"
  "on the high ground," "on the west/east bank," "top to bottom," "two irons in him."
- **Deliberate bookend echoes (KEEP)** — Ch.1↔29: "beeswax and old stone," "four parts in ten,"
  "a locked room three floors up," "iron wheels changed their note." These are intentional
  and should NOT be flattened.

### 2b. Tic spikes
- **Ch.27 (3.8/1k)** — highest in book; review filler in the battle prose.
- Ch.18 / 21 / 28 (2.1–2.3/1k) — secondary.

### 2c. Anaphora runs (rhythm) — Ch.28 L31 (×4), Ch.29 L93 (×5 "She did not…/He did not…")
Bishop uses anaphora, but the climax leans on it; break the longest runs.

### 2d. Long sentences — Ch.27/28/29 have 73–108-word rolling "and…and…and" sentences.
On-comp Bishop is clipped. Split the worst 1–2 per chapter (grammar_check lists them).

### 2e. Show/tell book-wide heavies (convert-to-scene candidates, not errors)
Ch.1 ¶12, Ch.4 ¶1, Ch.12 ¶27, Ch.16 ¶25, Ch.20 ¶52, Ch.5 ¶41, Ch.6 ¶27 — filter-verb /
abstraction-heavy paragraphs; several are scene-end "narrated-meaning" codas (the flagged tic).

### 2f. Filter words (Crucible line-guide) — spot pass needed
"felt / knew / saw / watched / realized" appear as distancing verbs in reflective beats
(esp. Ch.18/26 interiority). Not systemic, but a targeted pass would tighten deep-POV.

## 3. Cross-scene echo between the two explicit scenes (Ch.18 ↔ Ch.26)
Structurally well-differentiated (Ch.18 = he leads; Ch.26 = she leads) — good. But near-verbatim
lines survive and read as copy, not callback:
- "the too-much warmth she had lain a plank away from for weeks and told herself she did not want"
  (Ch.18 ¶79) ≈ "the dragon-heat she had kept a plank's width from for weeks in a shieling and
  told herself she did not want" (Ch.26 ¶69).
- "the whole cold length of her" (both); "the one warm place on all her cold body" (both).
- "Your heart's too quick / you'll wear it out" — **deliberate callback, KEEP** (she flags it herself).
Recommend varying the plank's-width line in Ch.26.

## 4. Sex scenes — publisher-POV assessment
See §"Publisher read" in chat summary. Verdict: **appropriate for the book's stated category
(ADULT romantasy, explicit), on-trend, consensual, character-integrated — NOT "too much."** The
only action item is positioning (must be marketed/queried as adult 18+, adult spicy comps), not
content reduction. Optional strategic softening only if widening to open-door-but-not-graphic
lists.

---

## 5. EXECUTED (2026-07-10) — fixes applied, all gates re-verified clean
Per-chapter commits on `scale-and-silver`:
- **Ch.27** — reduced "bank" saturation 20→13 (varied to Crown host / crossing / shore where the
  east/west parallel wasn't load-bearing); tic density **3.8→2.6/1k**; split two 78–80w sentences;
  varied the repeated "standards hung dead in the windless" image (kept Ch.28's, it's the plot beat).
- **Ch.28** — broke the anaphora peak in L31 (score 4→3); split the 95w and 85w sentences.
- **Ch.29** — split the 108w expository opener. **Kept** the L93 "She had held…" grief litany
  (deliberate anaphora, emotional peak, tied to the "no one sees her cry" canon).
- **Ch.26** — reworked the near-verbatim "plank's width… told herself she did not want" clause so it
  no longer copies Ch.18.

**Deliberately NOT changed** (deliberate motifs / natural collocation, per checklist §E + CLAUDE.md):
- Character/thematic motifs kept: "the cold measuring part of her" (Amelia's interiority), "a person
  standing in a room" (core theme), "foot of the poor man's water/ford" (crossing motif), the Ch.1↔29
  bookend echoes, the Ch.19 "three days up a mountain" devotion refrain, "your heart's too quick /
  you'll wear it out" (self-flagged callback).
- The ~630 style_check n-gram flags are dominated by ordinary-English collocation across a 152k-word
  book ("first time in her life", "stood in front of"); chasing them flattens natural prose. Left as-is.

Result after pass: style densities all under ceiling; voice-wear / metaphor / grammar clean; word
floor 152,116. No developmental or copy-edit (spelling/canon) errors surfaced — the earlier
continuity + voice audits already cleared those.

---

## 6. Front-act show-vs-tell pass (2026-07-10) — Ch.1–9
Triggered by an external editorial review (chapters 1–9 read closely; 10–29 were inferred from
commit notes, not read — its back-half ratings are guesses). Its one specific craft target (the
Ch.1 household-love paragraph) matched our own `show_tell_check` #1 heavy. Fixes:
- **Ch.1 ¶12** — trimmed abstract framing of the household-love summary, kept every concrete
  anecdote + the Ch.1↔29 "locked room three floors up" bookend. 4.5/310w → 3.5/264w.
- **Ch.8 ¶46** — cut the "narrated-meaning" thesis coda + a confusing line; ends on the concrete
  image now. 8.5/209w → 6.5/160w (book's heaviest front-act para).
- **Ch.8 ¶25** — broke the closing telling-pile-up (dropped the "know…knew" filter stack). 5.5→4.5.
- **Ch.3 ¶40** — cut the meta-frame about how memories arrive; drops straight into the swim memory.
- **Ch.5 ¶41 / Ch.6 ¶57** — cut telling frames/codas; both off the ≥4 list.
Left as earned (interiority / scene-setting, not defects): Ch.8 ¶46 emotional core, Ch.3 ¶40
thematic memory, Ch.4 ¶1 scene-setting opener, Ch.7 ¶48 (largely scene). Gates clean throughout.

## 7. Real back-half read (2026-07-10) — substitute for the blocked cross-model opinion
The Gemini/Grok second-opinion skills can't run here (no `gemini_review.sh` in repo, no
GEMINI_API_KEY/XAI_API_KEY). Instead I close-read 7 of the 12 back-half chapters in full
(18, 23, 24, 26, 27, 28, 29 — the spine + both explicit scenes + climax + resolution).
- **Quality is genuinely high and consistent** — the pasted reviewer's 8.6–9.1 back-half scores were
  unearned guesses, but they were not wrong: the craft holds. Standouts: Ch.24 ("hidden and seen are
  the same wall"; the Ch.13-mercy inversion), Ch.23 (Loric's father-laugh; the Crown-seal-as-killing-
  stroke irony), Ch.28 (indifference-as-defeat). Canon holds in every chapter read (silver hair,
  magyk, dragon situational, no sexual violence).
- **One substantive continuity/craft note for the author (NOT yet actioned):** the **Ch.23→24 hinge**.
  Ch.23 ends with Amelia resolving the "seen = caged" epiphany and turning **south, toward the
  capital**. Ch.24 opens with her a mile south, then **reversing north** to Dunmoor, re-articulating
  the same epiphany to justify the new direction. Defensible as a deliberate false-start/refinement
  (south = being saved by mother = another cage → she corrects *where* she'll declare herself), but
  the epiphany is delivered at both ends of the break and the direction-flip can read as a reversal.
  Author call: keep as intentional beat, or trim Ch.23's final paragraph so the full realization
  lands once (in Ch.24). Flagging, not fixing — it touches story intent.

  **RESOLVED (2026-07-10, author chose Fix A — "clean handoff"):** Ch.23 now owns the *diagnosis*
  (seen = caged, done with both) and ends undirected — cut the spelled-out "stand up in the one
  place it all turns on…" plan and the contradicting "turned south, toward the capital" line;
  ends on "And she began to walk." Ch.24 keeps the epiphany + the *choice* (legs default south =
  rescue → she overrides north to Dunmoor). Also fixed a geography slip in Ch.23 ¶119 (Loric had
  been listed among the things *south*; he's at her back in Dunmoor to the north). Removed the
  duplicated "began to walk faster" chapter-end echo as a bonus. Ch.23 re-gated clean
  (grammar/style/metaphor/rhythm), 5,191w.

## 8. De-tic pass — whole-book (2026-07-10, beta-panel fix #1)
Beta-reader panel's #1 consensus fix: scene-end narrated-thesis tic + cross-POV repeated
phrasing breaking POV differentiation. Addressed the named repeaters:
- **"looking back was a hand reached out for a thing…"** (~6×, Korvan/Amelia/chief) — kept the
  Ch.21 anchor (where the creed is explicitly linked between characters) and VARIED the rest
  (Ch.19, 21:149, 22, 23, 25). It's a deliberate shared creed, so varied not killed.
- **"it was not nothing" / "she held to that"** doublings — kept origins (Ch.14 chief dialogue,
  Ch.16 Amelia dialogue), removed same-paragraph doublings in Ch.15/24/28; "she held to that"
  now sits only within Amelia POV (no cross-POV bleed).
- **"both are true and they don't cancel"** — de-quoted the Ch.29 ¶97 memory so the ¶99 dialogue
  payoff lands once; kept Ch.16 origin.
- **"the sum / arithmetic"** — JUDGMENT CALL: left substantially intact. Close reading shows this
  is deliberate, signposted characterization (Amelia's signature that Korvan consciously inherits —
  "He did the sum then. Her sum"; "the arithmetic voice, come into his mouth at last" — and the
  chief's own pragmatism). It's a load-bearing arc, not unconscious bleed. Only thinned one
  same-paragraph doubling (Ch.22 ¶79). NOT gutted.

Gates after pass: style densities under ceiling, grammar/metaphor/voice-wear clean, 151,930 words.
Still OPEN from the panel (need author steer — plot/structure/positioning): feeding-arc payoff (#2),
timeline consistency (#3), Selwyn cost / power-limit seeding (#4), positioning/couple-page-time (#5).

## 9. Beta fixes #2 (feeding) + #3 (timeline) — 2026-07-10
Author decisions: #2 = "account for it (recalibrate)"; #3 = "compress to weeks."
- **#3 Timeline — compressed to weeks.** The book is internally consistent on a ~6–8 week scale
  (six days / three weeks / a fortnight / six weeks / "twenty-two days after the Elver"); only
  Ch.25 (7×) and Ch.26 (12×) asserted "a year." Converted every literal "a year" in those two
  chapters to the weeks scale; kept the ache with two deliberate "worn like a year" / "every week
  of it had felt like a year" similes. Also corrected the "a whole year" I'd introduced in the
  earlier Ch.26 plank-echo fix.
- **#2 Feeding — accounted for + recalibrated.** The Ch.12 goat already established she survives on
  ANIMALS (never a person = the rule). Recalibrated Ch.11's contingency so it points at that
  resolution (get her to a non-person heartbeat fast; if none, run) rather than an unfired
  "decide what you do to me" put-her-down catastrophe. Added a back-half acknowledgment at Ch.23
  (dry-vial-two-weeks) closing the loop: she's held the never-a-person line on the road's dying
  animals (hare/ewe/gull), at cost, "the first thing she'd kept whole by her own will."
Gates clean (grammar/metaphor/voice-wear); avoided the retired phrase "never once"; 152,067 words.
STILL OPEN (authorial): #4 Selwyn cost / power-limit seeding; #5 positioning / couple page-time.

## 10. Beta round-2 + follow-up fixes (2026-07-10, later)
Re-ran beta panel post-revision → `evaluations/review/beta-reader-panel-round2.md` (scores held/rose;
feeding RESOLVED, tic IMPROVED, timeline IMPROVED). Then:
- Ch.29 time over-referencing thinned ("twenty-two days" → one anchor; "three weeks" clash removed).
- Ch.27 stray "a year" (Selwyn) → "said all along". Other ~10 "a year" hits reviewed = life/hyperbole
  idioms, left intact (swapping would flatten voice).
- Ch.17 lightly tightened (one redundant interiority reiteration; chapter is load-bearing, not gutted).
- **Beta #4 (author: let Selwyn die):** Ch.28 save → "wound too open to hold" (embodies the power-limit,
  removes the plot-timed save); Ch.29 → death report + ruling beat. Selwyn DEAD; Book-2 betrothal seed void.
- **Beta #5 (author: keep romantasy + add couple page-time):** new mid-book togetherness beat at Ch.19
  shieling pre-dawn (~330w, non-explicit per the two-explicit-scenes canon). Book now 152,584 words.
- "did the sum" deliberately NOT thinned further (signposted characterization + Ch.28 payoff).
OPEN: optional Floor re-eval on Ch.19/28/29 (changed canon); production track; book-packager.

## 11. Canon correction — Amelia's power is vast; the failure is INEXPERIENCE (2026-07-10)
Author note: blood magyk is genuinely powerful (that's WHY the court feared her once they learned she
carried the Queen's magyk). Amelia COULD eventually save a wound like Selwyn's — she just hasn't the
Queen's centuries of practice. Reworked the Ch.28 Selwyn death from an ABSOLUTE power-limit ("wounds
too open to hold") to a SKILL/experience gap: the power comes, enormous and more than enough, but she
has held it barely a season and lacks the craft to catch a wide fast bleed in time; her mother would
have held him with two fingers. "The power was equal to it. She was not. Not yet." Ties to her arc
(immense inherited power, untrained) and keeps the fear justified. Ch.29 death report neutralized
("the boy went out under her hands regardless"). Gates clean; book 152,762.

## 12. Power-canon cohesion sweep (2026-07-10)
Checked every passage that describes Amelia's power/limits against the corrected canon (power VAST +
feared; real limit = INEXPERIENCE not a ceiling; separately, blood magyk acts on blood/bodies, not
inanimate "weight"). Findings:
- Ch.2 (training) — CONSISTENT: built on practice (flame/fish/cold); rule = chosen discipline vs how
  EASY taking is; power framed as feared. No change.
- Ch.20 (saves a dying child's bleed) — the key precedent: power EXCEEDS the law ("the law had not
  been the edge of her power; a fence her mother built well short of the edge"). CONSISTENT and load-
  bearing (proves she CAN hold a bleed → Selwyn is a scale/skill failure, not a domain one). Fixed one
  over-absolute line (¶83) to scope it: "for everything she had yet asked of it, the difficulty had
  only ever been in the deciding and not in the doing" (was "…never in the doing" — which would clash
  with Selwyn being beyond her untrained craft).
- Ch.24 (stops six hearts) — CONSISTENT: "a small precise motion" = the ACT is precise, not the power
  small; explicitly "a girl learning a craft" (reinforces skill). No change.
- Ch.28 ¶31 ("no power over weight at all") — CONSISTENT: domain boundary (can't stop flying iron),
  distinct from the Selwyn skill-gap. Left intact.
- Ch.13/15/16 — CONSISTENT (fish-control lesson; magnitude "deep-red gathering of blood magyk"; rule
  as self-built discipline). No change.
Net: canon now coheres — she can heal/hold blood (Ch.20 child), her power outstrips the law, and
Selwyn dies because a wide/fast wound outstrips her UNTRAINED craft, not her power.

## 13. Beta round-3 follow-ups (2026-07-10)
Round-3 panel (evaluations/review/beta-reader-panel-round3.md): scores rose/held again (Hostile 6→7,
Critic 6.5→7, Devourer 8→8.5); Selwyn/power-limit gap RESOLVED and dropped out of the problem tier.
Genesis Floor re-eval caught + fixed a Ch.28 below-floor bug (Selwyn-death not propagated to ¶167/169/171
— now corrected; Ch.28 back to Floor 8.5). Then, from the R3 fix list:
- **#3 skill-gap seam — DONE.** Seeded in Ch.20 (¶91): even in the ease of the child-save she feels the
  edge — the tear was small/slow enough for an unschooled hand; a faster/wider wound would run out before
  she had the craft; "the power would be equal to such a wound and she would not, not yet." Sets up Ch.28.
- **#5 Maren's own stroke — DONE (as continuity fix).** Maren ALREADY has a distinct death (Ch.28 ¶83–91,
  the button-count, forbidding the save). Fixed the ¶155 line I'd introduced that wrongly lumped her with
  the Queen as "too fast" — now three distinct deaths: Queen (iron, too fast), Maren (had time, FORBADE the
  reach), Selwyn (tried, couldn't — untrained craft). Tightens the power-canon too.
- **#4 "a year" mop — NO CHANGE NEEDED.** Residuals are the 2 deliberate "like a year" similes + one true
  life-cadence idiom ("one word in a year"). All intentional.
- **#1 back-half de-tic — partial.** Varied the new Ch.19 beat's "did the sum". Left the rest of "did the
  sum" (deliberate signature + Ch.28 counting-fails payoff); scene-end-thesis thinning is at diminishing
  returns per R3 ("reduced again").
OPEN (authorial): #2 POSITIONING call (romantasy vs epic fantasy; one more couple beat optional — Ch.19
proved the lever). Book 153,026 words; all gates green.
