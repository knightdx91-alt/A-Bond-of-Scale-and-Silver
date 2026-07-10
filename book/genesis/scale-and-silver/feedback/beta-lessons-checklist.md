# Beta-Lessons Checklist — run per chapter before finalizing

> Derived from real beta-reader notes on Saeren Book One Ch.1 (Eilidh Locherty, line editor,
> 28 comments; Dana Flanders, developmental, 2 comments), pulled from the author's Google Docs
> 2026-07-08. These are the mistakes readers actually caught. The good news: matching the
> Anne Bishop voice comp (see `voice-dna.md`) already prevents most of them — the voice IS the
> fix, not a constraint fighting it. Run this list as a hard gate alongside `style_check.py`
> and `grammar_check.py`.

## The two biggest notes (both reviewers converged here)

1. **NAME WHAT YOU MEAN — no vague poetic reaches.** Eilidh's single most repeated note:
   "Known what?" · "Knew what?" · "Do we know what symbol?" · "I don't understand 'deep water'"
   · "I'm guessing you are referring to family." If a reader can ask **"what?"** of any
   abstract or poetic phrase, cut it or name the referent. This is exactly the "eats voices"
   class of line we already cut. → Per chapter: scan every figurative/abstract phrase and ask
   "what does this point at?" If it isn't answerable on the page, fix it.

2. **SHOW EMOTION IN THE BODY — don't just name it.** Dana: "go to each emotional scene and
   make sure you don't just name the emotion, but describe how she feels it in her body —
   fingers tingle, stomach drop, body feels light." This is Bishop's #1 trait and already the
   core voice rule. → Per chapter: at every emotional beat, is the feeling carried by the
   body/behavior, not just stated? No "she felt sad / a wave of grief."

## Line-craft checks (Eilidh's specific catches)

3. **No ambiguous character emotion** (Dana): early chapters especially — is it grief or just
   a sour personality? Make the *cause* clear through action, not mood-coloring. No room for
   ambiguity while the MC is being introduced.
4. **Split over-packed sentences.** "This sentence is doing a lot in one breath — tighten it."
   "We don't need to say everything." → Find the 3 longest sentences per scene; split at least
   one unless it's deliberately load-bearing. (Bishop median ≈ 13 words.)
5. **No dangling modifiers.** "'grey stone' left the sentence without a clear subject." → Every
   opening modifier must attach to a clear subject. `grammar_check.py --languagetool` catches
   many.
6. **Dialogue attribution is unambiguous.** Eilidh flagged confusion repeatedly: who said this?
   put it on its own line; don't double a name; don't have a character use another's name
   unnaturally (a mother saying the father's given name) — pick "her father" vs "Leon" and
   HOLD it. → Every line of dialogue: can the reader tell who's speaking without rereading?
7. **Concrete image over vague one.** "the wax" → "its wax seal"; "eyes" → "gaze." → Prefer the
   specific noun.
8. **Mark every time/scene jump.** Eilidh: a big unmarked jump between scenes "can be very
   confusing." → Signal each time/place shift explicitly.
9. **Re-read any joke/clever construction once for clarity.** The "character/toast" gag
   confused her ("made me pause over whether 'character' meant the burnt colour, the toast, or
   the joke"). → If a smart reader has to reparse a clever line, rewrite it plain.

## How to use
- Run this AFTER the draft, BEFORE the gate sign-off, every chapter.
- Log any recurring offender in `feedback/style-flags.md`.
- Items 1, 2, 4, 6 are the highest-frequency — check them hardest.

## Pipeline fingerprints to watch (from the book-evaluator, Ch.1–2) — ENFORCE every chapter
These are habits the pipeline repeats across chapters (they compound into a detectable
fingerprint). The Writer/Disruptor/Editor must actively watch them, not just fix in place:
1. **Philosophical / "coffee-mug" asides: ≤ 1 per chapter.** The aphoristic summarizing line
   ("a promise is only a wall"; "a price... does not get lighter for being itemized"). The
   author dislikes these (flowery/clever). Ration hard; prefer to cut.
2. **Do not re-unpack an established world rule.** The first chapter that states a rule (e.g.
   the acoustics "a room that eats a sound") OWNS it; later chapters use it without re-explaining.
3. **Vary chapter endings per POV.** No two Amelia chapters may close on the same
   "alone, resolved, rehearsing the escape plan in the dark" image. Retire any one-use simile
   after a single appearance (e.g. "the way her mother taught her the treaty" — used once, done).
4. **Close logic seams in tense beats** — if a POV character's power/scent/etc. should be
   noticeable to another character, give one clause of cover for why it isn't.

## Per-POV device budget (added 2026-07-08 — voice-wear control)
5. **Ration each POV's signature devices and retire verbatim self-phrases — for EVERY POV, not
   just Amelia.** Enforce `voice-dna.md §4b` and log usage per POV: `feedback/amelia-voice-ledger.md`
   and `feedback/korvan-voice-ledger.md` (every new POV gets its own ledger). A signature that fires
   every chapter at the same rate becomes formula (AI-fingerprint + reader skim). Let the signature
   EVOLVE with the character; use the POV's other registers (wonder/warmth/humor/anger), not just
   the default mode.
   - **Book-wide retirements** (pipeline tics that leak across all POVs + narration): **"never once"**
     is retired manuscript-wide. Any phrase the style/rhythm checks flag as a shared cross-chapter
     n-gram is retired the same way, for everyone.
