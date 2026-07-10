# Evaluation: Chapter 1 — "Contraband"
**Evaluator:** book-evaluator | **Date:** 2026-07-08
**Book:** A Bond of Scale and Silver | **Genre:** Adult romantasy | **Voice comp:** Anne Bishop (Black Jewels)
**Word count:** 5,032 | **POV:** Amelia (close third)

---

## RE-EVALUATION (Round 3 — post SHOW-vs-TELL convert-pass, 2026-07-09)

**Trigger:** whole-book show→scene pass (commit `7b68a96`, "render filter verbs, clear last flags").
**Scope of what actually changed in Ch.1** (verified against `git diff 47da337 7b68a96`): the pass was
**light-touch and improving, not destructive.** Three kinds of edit, all benign:
1. **Filter-verb removed (real show-vs-tell win):** ¶27 opener "It was a strange thing to be, *she had
   decided long ago*, a secret…" → "It was a strange thing to be, a secret…". A telling filter clause cut;
   the observation now stands as direct perception.
2. **Retired tics swapped, not new tell added:** the book-wide retired "**never once**" and the capped
   "**twenty years**" were recast in place ("all her life", "every year since", "since the day she was born",
   "in all that time", "years"). No meaning lost, no reflection paragraph inserted, no scene removed.
3. **No new coda, no new abstraction.** Word count 5,032 → 5,074 (+42, from the recasts). No paragraph was
   converted from scene to summary; the HARD-RULE (add scene not reflection when short) was not tripped
   because nothing was padded.

**Show-vs-tell is EQUAL-OR-BETTER, confirmed mechanically:**
`python3 tools/show_tell_check.py 1` → filter **7.3**/1k (warn ≥9.0), abstract **5.5** (warn ≥6.0),
named-emotion **0.0**, dialogue **19.6%** (warn <8%). **Zero flags.** The one net change to the filter
count is downward (¶27 clause removed). Gates: `style_check` **clean**, `grammar_check` **RESULT: clean**.

**Result: HOLDS the ≥8.5 gate. Genesis Floor 8.5 | Average 8.5 | Casual 8.5. No regression introduced.**

| Dimension | R2 | R3 | Note |
|-----------|----|----|------|
| Originality | 8.5 | 8.5 | Hook untouched. |
| Theme | 8.5 | 8.5 | Unchanged; texture intact. |
| Characters | 8.5 | 8.5 | Laugh + warm-Queen canon intact; the recasts do not touch character beats. |
| Prose & Voice | 8.5 | 8.5 | Marginally cleaner (one filter clause gone, two tics retired). Not 9.0 — no new stopping-sentence tier; a couple of load-bearing long sentences remain (¶27, ¶117) and are correctly left alone. |
| Pacing | 8.5 | 8.5 | Sentence-rhythm variation from R2 preserved; nothing lengthened into a sag. |
| Emotion | 8.5 | 8.5 | Body-rebel (laugh, wet eyes, waking blood) untouched. |
| World-building | 8.5 | 8.5 | De-catechized treaty from R2 preserved. |
| **FLOOR** | **8.5** | **8.5** | **PASSES.** |
| **AVERAGE** | **8.5** | **8.5** | |

**Tomorrow Test (re-run):** unchanged — BOTH anchors survive intact: the Queen's "*I made you out of
nothing and love and spite… and no one will ever, ever be permitted to know it*" (¶59, QUOTE) + the silver
girl in the grey gown at the forbidden window (¶129–131, IMAGE). ANCHOR EXISTS.

**Four-reader spot-check (delta only):** Devourer/Critic/Hostile/Casual verdicts from R2 stand; the pass
changed no event, dialogue, or POV boundary, so no reader-facing surface moved. The Critic's one prior
lapse (the omniscient POV break) was already fixed in R2 and remains fixed — the ending still sits inside
Amelia's perception ("the first stranger she would ever walk up to as a stranger. She did not know whose
face it would be," ¶131). No new hostile-reader hole opened.

**Regression scan — NONE found.** The pass did not: strip a shown body-beat into a named emotion; add a
"here's what it meant" coda; pad a short spot with reflection; break tense or POV; or re-inflate a retired
phrase (`voice_wear` retirements held). The only directional movement is a small improvement (filter -1,
tics retired). **Floor confirmed 8.5. Cleared to remain finalized.**

**BIAS CHECK:** produced by the same system that wrote the prose; confidence in the 8.5s requires external
validation. This re-score is a narrow no-regression confirmation of a mechanical pass, not a fresh full
re-read verdict — the substantive craft judgments are inherited from the R2 evaluation below and were
re-verified against the current text.

---

## RE-EVALUATION (Round 2 — post-polish, 2026-07-08)

**Result: PASSES ≥8.5 gate. Genesis Floor 8.5 | Average 8.5 | Casual 8.5.**

All four polish notes were executed and each is text-verified, not just claimed:

| Prior finding | Status | Evidence in revised text |
|---|---|---|
| Deep-POV break (¶131–133) — IMPORTANT | **RESOLVED** | Ending now sits inside Amelia's own perception: "was the first stranger she would ever walk up to as a stranger. She did not know whose face it would be." No omniscient Korvan trail, no author future-tease. |
| Over-packed sentences (beta #4) — VIOLATION | **RESOLVED** | ¶31 split with short punches ("The bodice sat close. The skirt fell the way water falls... Obedient."); ¶79 blood/stillness split into three; ¶117 "not-being" sentence split. Short-dominant rhythm now present — this is the reading-speed variation the chapter previously lacked. |
| Philosophical asides (#16) | **RESOLVED** | "only luggage" → "It was not a sign. It was only a thing she carried" (¶41); "a room with a bolt on it" → "Their love was the lock on her door" (¶121). Both plainer. |
| Treaty catechism (exposition) | **RESOLVED** | ¶87 folds recitation into prose and adds a felt beat: "Her mother's fingers moved slowly in her hair while she spoke, keeping time." Exposition now carries a second speed; the load-bearing reveal (¶89–91) is kept clean. |

### Revised Genesis Score

| Dimension | R1 | R2 | Why it moved (or held) |
|-----------|----|----|------------------------|
| Originality | 8.5 | 8.5 | Unchanged — hook untouched. |
| Theme | 8.5 | 8.5 | Unchanged; echo-chamber risk still present but non-capping. |
| Characters | 8.5 | 8.5 | Unchanged; the laugh and warm-Queen canon intact. |
| Prose & Voice | 8.5 | **8.5** | Held, but now *clean* rather than flagged: register pulled toward the Bishop short-punch spec, both ornamental asides gone, POV break gone. Not 9.0 — a few long sentences remain (¶27, ¶117) and median still runs above Bishop's ~13. |
| Pacing | 8.0 | **8.5** | **Earned raise.** Split sentences create genuine acceleration/deceleration (the "reading-speed design" lever), and the ¶87 felt beat breaks the reflection with a second speed. Value shift and end-hook already strong; the missing element (register variation) is now present. |
| Emotion | 8.5 | 8.5 | Unchanged; body-rebel + emotional-surprise intact. |
| World-building | 8.0 | **8.5** | **Earned raise.** De-catechizing + felt beat convert the treaty from a visible Q&A device into disguised, felt exposition. The essential fact still lands once, cleanly. |
| **FLOOR** | **8.0** | **8.5** | **PASSES gate.** |
| **AVERAGE** | **8.36** | **8.5** | |

**Anti-inflation note:** only Pacing and World-building were raised, and only because a specific,
citable craft element was added (sentence-rhythm variation; disguised exposition + felt beat).
Prose held at 8.5 rather than climbing to 9.0 — the fixes removed *flaws*, they did not add a
new stopping-sentence tier. No dimension was raised merely because "the note was addressed."

**CVI (updated):** CVI-Launch ≈ 8.6; CVI-Legacy ≈ 8.0.

### Residual issues (all non-blocking — polish, not gate)
1. **Still a single quiet interior scene, ~5k words.** Momentum is carried by voice, not event.
   Fine for a literary-leaning romantasy opening, but **Ch.2 must deliver external movement** or
   the two-chapter run reads static.
2. **A couple of long sentences survive** (¶27, ¶117) — deliberately load-bearing and within
   Bishop's rare-long allowance. Do NOT split further or the rhythm flattens.
3. **Thematic density remains high** — held below the echo-chamber cap by real texture; ensure
   Ch.2–3 add non-thematic life so the pattern doesn't harden into a fingerprint.
4. **Voice-under-pressure register** (Amelia → flatter/clinical under overload, per voice-dna) is
   still not *demonstrated* at her peak. Not a Ch.1 requirement; the first real overload beat in a
   later chapter should show it.

**Verdict (R2): PASS.** Floor 8.5, Casual 8.5. Cleared for finalize.

---

## (Round 1 evaluation retained below for trajectory)

## HEADLINE
**CVI-Launch:** 8.4 | **CVI-Legacy:** 8.0 | **Genesis Floor:** 8.0 | **Genesis Average:** 8.36
**Engagement Type:** Empathy (primary) / Fascination (secondary) / Intellectual (tertiary)
**Gate result: FAILS ≥8.5 Genesis Floor.** Floor held by Pacing (8.0) and World-building (8.0).
**Divergence Alert:** none >2.0. But note the inverse of the usual romantasy risk — this opening is craft-rich and momentum-light, the opposite of an airport thriller. The commercial engine here is *voice seduction*, not plot pull.

## Genesis Score

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | 8.5 | "The most transgressive act available to her was to want, very much, to go to a party." (¶39) — the contraband-existence hook, accusation-as-weapon seeded via the treaty-with-a-hole | — |
| Theme | 8.5 | "she would rather be seen once and pay for it than be adored forever and never once exist" (¶121) — seen-vs-safe / inherit-vs-choose embodied, not stated | Thematic-echo-chamber *risk* noted (see Prose); saved from 7.5 cap by genuine texture (owl-whistling, honey pears, linen-girls' sweethearts) |
| Characters | 8.5 | The wrong laugh (¶71–73); the Queen "I made you out of nothing and love and spite" (¶59); Della's "I'm not meant to have views on anything, and I've had them for forty years" (¶17) | Chaos partly MEDIATED (narrator analyzes Amelia — "Amelia, who read everything") rather than inhabited; would cap 8.0 if the laugh + waking blood didn't land as inhabited. Held at 8.5 |
| Prose & Voice | 8.5 | "and a breath too late to be company" (¶31); "she looked like something a story would warn you about" (¶37); "being no one" (¶47) — genuine close-the-book sentences | See VOICE FINDING below — register drifts OFF its own Bishop spec (long-sentence-dominant, not short-punch); philosophical asides present. Absolute quality high; spec-adherence is the flaw |
| Pacing | 8.0 | Value shift is real and internal: resignation → resolve ("She was not going to keep staying," ¶119). End hook strong (¶131–135) | Single quiet interior scene, 5k words, no register variation/acceleration passages; momentum is voice-carried only |
| Emotion | 8.5 | Body rebel present: the involuntary laugh + wet eyes (¶73); "her blood was doing the thing it did when she was frightened... a low warmth rising in her wrists" (¶79). Emotional surprise = wrong laugh at tenderness | — |
| World-building | 8.0 | Treaty delivered as mother-daughter catechism (¶87–93); "a vampire who is born, rather than made" | Exposition is a Q&A recitation — effective and framed as a steadying ritual, but it IS the info-delivery vehicle; slightly on-the-nose |
| **FLOOR** | **8.0** | | |
| **AVERAGE** | **8.36** | | |

## CVI-Launch Breakdown
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 7.5/10 | One scene, no chapter-internal variety; carried by voice, not hooks-per-page. Strong end hook. |
| Tomorrow Test | 2 anchors (QUOTE + IMAGE) | "made you out of nothing and love and spite" (quote) + the silver girl in the grey gown at the forbidden window (image) |
| Casual Reader | 8.5/10 | Voice is immediately immersive; the "girl who has never been in a room with people" premise lands in 3 pages |
| Shareability (quote/plot/emotional) | 4/3/4 | Strong pull-quotes; plot barely moved yet; the mother scene is textable ("this book's opening GUTTED me") |
| Concept Pitch | yes | "A queen's secret vampire daughter, hidden her whole life, decides to walk into the one room she was forbidden — a party" |
| Human Closeness | yes | ~90% intimate two-hander (mother/daughter, keeper/girl) |

CVI-Launch ≈ (7.5×.2)+(7×.2)+(8.5×.2)+(8.1×.2)+(10×.1)+(10×.1) ≈ **8.4**

## Anti-AI Scan (20 Patterns)
- **#3 Rule of three:** minor — "the stillness and the languages and the recitation" (¶115). <0.5/1k. Minor.
- **#11 Explanatory extension:** present — "a room that eats a sound has to put it somewhere" (¶25) unpacks its own metaphor; "one clear note sounding in another room" (¶61) is extended. ~0.4/1k. Under the 6-instance / 0.8-per-1k Commercial cap. Minor, watch.
- **#12 Binary negation opener:** present — "Not because Amelia was a secret from her. Because Amelia was a secret from..." (¶5); "It was not ordinary." (¶35); "It was not nothing." (¶27). ~0.6/1k. Moderate — flag.
- **#16 Philosophical asides:** present — "Some things a person carries are not signs. They are only luggage." (¶41); "love had turned out to be a room with a bolt on it" (¶121). Coffee-mug-extractable. ~0.4/1k. Flag — this is the pattern most at odds with the Bishop restraint spec.
- **#18 Thematic echo chamber:** partial — the acoustics, counting, the dress-for-trying-on, the arithmetic ALL point at seen/hidden. Texture exists but is thin. Watch.
- Patterns #1, #2, #4 (em-dash), #5, #6, #7, #8, #9, #10, #13, #14, #15, #17, #19, #20: Clear or negligible.
**Total flags (Commercial thresholds):** ~5 patterns at low/moderate density = **CLEAN band (0-8)**. Numerically fine. The *qualitative* concern is that #12/#16 are precisely the ornamental-reflection habits the Bishop spec exists to suppress.

## Beta-Lessons Check
- **#1 Name the referent:** PASS — figurative reaches consistently name their target ("the thing that looks like laughing when a person has run entirely out of the other options").
- **#2 Emotion in the body:** PASS — strong (laugh, wet eyes behind the hand, blood waking in the wrists).
- **#4 Split over-packed sentences:** **VIOLATION.** This is the chapter's clearest beta-lesson breach. ¶27, ¶41, ¶113, ¶127 stack multiple long clauses well past Bishop's ~13-word median. The prose is winding-literary, not short-punch declarative.
- **#6 Dialogue attribution:** PASS — unambiguous throughout.
- **#8 Mark scene jumps:** N/A (single continuous scene).

## VOICE FINDING (benchmark-critical)
This chapter is being used as the voice benchmark for the whole book, so this matters most.

The prose is genuinely beautiful — but it is **not the voice the spec commissions.** voice-dna.md §1 mandates plain declarative Bishop register: median ~13 words, ~38% of sentences ≤10 words, short-dominant, the "short punch after the long build." This chapter is the *opposite* — long-breath, subordinate-clause-dominant, luxuriant (closer to Marilynne Robinson than Anne Bishop). It reaches for the ornamental image and the philosophical aside that §0 and §4 explicitly forbid ("If a line is doing something clever with an image, it is probably wrong").

Second, **a hard deep-POV break.** ¶131: "among them, just then coming down out of the cold hills with his father's men and no idea in the world that she existed, was a young man with no animal in him..." Amelia cannot know this. The narrator steps out of her head into omniscience to trail the love interest. voice-dna.md §1 mandates "one POV per chapter... we live inside that head." This is the single cleanest craft error in the chapter. ¶133 ("That was the mercy of it...") compounds it with an authorial future-tease.

If Chapter 1 is the ruler every later chapter is measured against, the ruler is currently mis-set: later chapters written to *this* register will run long, ornate, and asides-heavy, and will drift from the Bishop comp the whole project is built on. Recommend the author consciously decide: keep this richer register as the true voice (and update voice-dna.md), OR pull Ch.1 toward the plainer spec. They cannot both be canon.

## Character Chaos Check
- Irrelevant thought / unprompted memory: **present** — the beeswax-and-cold-stone smell arriving unbidden (¶41)
- Cognitive distortion: mild — the "not-being" she is asked to perform, turned over analytically
- Failed emotional management: **present** — the involuntary laugh she "could not call back" (¶73)
- Voice under pressure: **partial** — the body breaks (laugh, blood waking), BUT the *prose* does not go flatter/tighter/clinical as voice-dna §"Voice Under Pressure" specifies for Amelia's overload. At her peak overload the sentences stay lush. Register-under-pressure is not yet demonstrated.

## Secondary Character Chaos
- **The Queen (Rosalia):** has her own moment — the hands going still at the waist (¶61), the wet eyes the court fears (¶93). A person, not a prop. Warm-with-Amelia canon honored perfectly.
- **Della:** independent life and voice ("forty years" of forbidden opinions). A person, not a function.
No secondary-as-function flag.

## The Tomorrow Test
**What the reader remembers:** the Queen's "I made you out of nothing and love and spite, and you are the best thing I have ever done, and no one will ever, ever be permitted to know it" — and the wrong, ringing laugh.
**Anchor type:** BOTH (QUOTE + IMAGE)
**Verdict:** ANCHOR EXISTS (2). +0.5 to CVI-Launch applied.

## Reader Reports
**The Devourer:** Held by voice, but nervous — nothing *happens* except a dress and a conversation. Would keep going for the end-hook promise (shifters, three nights, a plan) but wants the plot to move in Ch.2.
**The Critic:** Delighted. Underlines "a breath too late to be company," "being no one," the whole mother speech. Would note the omniscient intrusion at the end as a lapse in an otherwise disciplined POV.
**The Hostile:** Challenges ¶131 — "how does Amelia know a boy is riding out of the hills right now?" Also: the treaty exposition is a touch convenient as a mother-daughter recitation. Would question whether a girl this analytical would only *now*, at 20, notice the cage.
**The Casual Reader:** Buys it. The premise is legible in three pages and the voice feels expensive. "A girl who's never been in a room with people" is a hook they'd repeat to a friend.
**The Devoted Reader (active — romantasy/series):** Adopts it. Would clock the two silvers seed (hair here; moon later), the "clan of one" foreshadow in Amelia's aloneness, the fountain/acoustics setup. Re-read rewards are being planted deliberately.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|-------|----------|--------|---------|--------|---------|----------|
| Low external momentum | flag | — | — | mild | — | SHOULD FIX |
| POV break ¶131 | — | flag | flag | — | — | IMPORTANT |
| Register off Bishop spec | — | flag | — | — | flag | IMPORTANT (benchmark) |
| Treaty exposition slightly on-nose | — | — | flag | — | — | INVESTIGATE |

## Revision Recommendations (Ranked)
| Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|----------|-------------|-----------------|-------------|-------------------|--------------|
| ¶131–133 | Voice / Logic (POV) | Narrator leaves Amelia's head to follow Korvan riding out of the hills and to tease "the last of the mercy" | Breaks the one-POV-per-chapter deep-third the whole voice spec is built on; Amelia cannot know this | Keep the forward charge inside Amelia's knowledge — end on HER plan and HER awake blood at the window. If a Korvan seed is wanted, make it something she could plausibly sense/hear (a horn, hooves on the road she counts), not omniscient narration | **Yes** — "no omniscient trailing of other POVs; hooks stay inside the POV character's knowledge" |
| Whole chapter | Style / Voice | Long, subordinate-clause-dominant sentences; ~well above Bishop's 13-word median; short-punch move rare | The benchmark chapter sets a register the spec forbids; later chapters will inherit the drift | Decide the true voice with the author. If holding the Bishop spec: split the 3 longest sentences per scene (¶27, ¶41, ¶127), and add short-punch landings after the long builds | **Yes** (if spec held) |
| ¶41, ¶121 | Style | Philosophical asides ("only luggage"; "love... a room with a bolt on it") | Pattern #16; exactly the clever/ornamental line §0/§4 kill | Keep the strongest ONE; convert the other to a plain shown beat | No |
| ¶87–93 | Exposition | Treaty delivered as recite-it-back catechism | Info-delivery is visible as a device | Keep the ritual framing (it's good) but trim one exchange and let a beat of it surface as Amelia's felt dread rather than recitation | No |
| Chapter momentum | Pacing | One quiet interior scene, no acceleration passage | Devourer/Casual momentum thin for a commercial opening | Add one micro-beat of concrete present-tense sensory action (a sound from below she mis-reads, the bolt, a near-interruption) to break the reflection and vary reading speed | No |

### Fix order: Logic/Character (POV break) → Voice/register decision → Exposition → Prose asides → Pacing

## Strengths to PRESERVE
- The mother scene — warm-imperious Queen canon nailed; "made you out of nothing and love and spite."
- The wrong laugh as emotional-surprise anchor and body-rebel — do not touch.
- The acoustics/counting habit as characterization (rates rooms, counts carriages/seconds) — distinctive, seeded for payoff.
- Silver hair planted plainly per outline; contraband-existence premise legible fast.
- Della as a real person with her own forty-year interior life.

## PATH TO 8.5 (mandatory — Floor 8.0)
- **Pacing 8.0 → 8.5 requires:** ONE concrete present-tense sensory beat that interrupts the reflection and creates a second speed. Best site: between ¶109 and ¶111 (mother gone, before the long sit) — a sound from the hall below that Amelia mis-reads through her acoustics habit, forcing a beat of alertness before she settles into the plan. This adds reading-speed variation the chapter currently lacks and gives the Devourer a pulse. Also fold the ¶131 omniscient hook back into Amelia's own hearing (hooves on the road she counts) so the end-hook lands as her perception, sharpening the final question rather than narrating it.
- **World-building 8.0 → 8.5 requires:** de-catechize the treaty. Cut one Q&A exchange in ¶87–93 and let the single load-bearing fact ("a vampire who is born, rather than made — the treaty says nothing") arrive once, plainly, as Amelia's felt realization, with the rest carried by her dread rather than her recital. Exposition disguised as feeling reads as world, not lecture.

## VERDICT
**POLISH.** Genesis Floor 8.0 (Pacing + World-building), Casual 8.5. Craft is above the genre bar and the emotional/character work is excellent, but the chapter misses the ≥8.5 gate on momentum and exposition — and, most importantly for a *benchmark* chapter, drifts off its own Bishop voice spec and commits one hard deep-POV break. Fix the POV break and settle the register question first; those are the load-bearing edits.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis). The register-vs-spec finding in particular is a judgment call the author should adjudicate directly.
