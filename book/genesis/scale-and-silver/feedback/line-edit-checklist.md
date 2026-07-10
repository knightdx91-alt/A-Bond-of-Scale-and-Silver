# Line-Edit Checklist — A Bond of Scale and Silver

Consolidated from the Crucible Novel Editor references (forsonny/The-Crucible-Writing-System-For-Claude)
and this book's own calibrated gate tools. Use as the lens for the whole-book line pass.

## A. Sentence-level craft (Crucible line-editing guide)
- [ ] **Filter words** — cut distancing verbs: *felt, saw, heard, noticed, realized, wondered, thought, seemed, appeared* (drop into direct experience).
- [ ] **Weak verb + adverb** → single strong verb ("walked quickly" → "strode"). NB: adverbs are *allowed* in this book's Bishop voice, but not as a crutch for a weak verb.
- [ ] **Passive voice** → active, unless the receiver/formality is the point.
- [ ] **Redundancy** — "shrugged her shoulders" → "shrugged"; "nodded her head" → "nodded".
- [ ] **Show vs tell** — replace emotional declarations with concrete physical detail.
- [ ] **Dialogue tags** — default to said/asked; fancy tags → action beats.
- [ ] **Stage direction** — trim choreography; keep only meaningful movement.
- [ ] **Sentence variety** — alternate short/long; no monotone runs.

## B. Polish pass (Crucible polish-techniques)
- [ ] Opening line hooks, sets tone, grounds POV.
- [ ] Closing line creates momentum / leaves an image or question — NOT a tidy summary
      (watch the "narrated-meaning" scene-end tic flagged in the sister book).
- [ ] Sensory balance (sight/sound/touch/smell/taste) — not all visual.
- [ ] Paragraph length varied; white space used for emphasis.
- [ ] Transitions smooth (spatial / temporal / logical / echo).
- [ ] Read-aloud test per chapter.
- [ ] Pet phrases not overused (see tool flags below).

## C. Copy-edit (Crucible copy-editing-standards)
- [ ] Tense consistency; POV consistency.
- [ ] Character/place name spelling constant; invented terms capitalized as names, lowercase when generic.
- [ ] Number formatting (spell 1–9, numerals 10+).
- [ ] Dialogue punctuation; scene-break/chapter formatting uniform.
- [ ] Homophones: its/it's, their/there/they're, affect/effect, lie/lay, who/whom.
- [ ] Magic-system costs applied uniformly.

## D. This book's deterministic gates (must stay clean)
Run `python3 tools/style_check.py` + the individual checkers. Ceilings:
- simile/"like/as if/as though" ≤ 3.0 /1k words
- em-dash ≤ 10 /chapter
- adverb (-ly) ≤ 20 /1k (allowed, capped)
- no NEW repeated 4–6 word n-gram across chapters (motif allowlist empty by design)
- verbal tics under ceiling (just/suddenly/somehow/seemed/slightly/felt like/for a long moment/as if…)
- show_tell_check, rhythm_check, voice_wear_check clean

## E. Voice fidelity
- [ ] Matches `voice-dna.md` (Anne Bishop / Black Jewels comp) throughout.
