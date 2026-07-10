# Voice DNA — A Bond of Scale and Silver

> Executable, enforceable voice spec. The Writer writes FROM this; Dialogue Polish and
> Hook Craft check AGAINST it; the Disruptor enforces the anti-pattern budget; the
> Editor/Evaluator hold the line. Genre: adult epic/political fantasy romance, dual close-third.
>
> **REV 2 (2026-07-08) — voice comp set to ANNE BISHOP, *The Black Jewels Trilogy*.**
> The register below is derived from the real text (analysis in
> `feedback/voice-comps-black-jewels.md`). We capture Bishop's *craft traits*, not her
> world-words or tics — this is the author's voice written in Bishop's register, not a
> pastiche. This rewrite also strips the three cut motifs and lowers the figurative ceiling
> per the author's "plainer, fewer metaphors" note.

---

## 0. THE ONE-LINE TARGET

**Plain sentences, deep POV, feeling shown through the body, menace and heat carried by
restraint — not by ornament.** If a line is doing something clever with an image, it is
probably wrong. Say the thing. Let the content and the character's head do the work.

---

## 1. GLOBAL NARRATIVE VOICE (Bishop-derived)

- **POV/tense:** Close third, past tense, **one POV per chapter** (the named character).
  Deep — we live inside that head; the narration thinks in the character's terms. Braided
  A/K chapters (see outline) use hard section breaks, never mid-scene head-hops.
- **Sentence construction:** **Direct and declarative by default.** Bishop writes "Daemon
  concentrated on breathing." "He felt her coming." "Fear hammered at him." Subject-verb,
  concrete, unshowy. Vary length deliberately: stack a few longer sentences, then land a
  short one for impact. The short punch after the long build is a signature move — use it.
- **Measured sentence-length target (from Bishop's real text):** median ~13 words; **~38% of
  sentences ≤ 10 words**; only ~8% run long (30+). Keep the mix short-dominant. Opening a
  sentence with *And* / *But* is fine and Bishop-common (~5%). **Avoid semicolons** — Bishop
  almost never uses them (0.2/1k); use a period.
- **Vocabulary level:** 5–6/10. Grounded and clear; reach for the precise word, never the
  ornamental one. Court chapters lean half a notch formal; road chapters half a notch plain.
- **Interiority:** Heavy, but rendered as **plain thought**, not purple narration. Show the
  character reasoning, dreading, wanting — in their own register. No metacognition ("she
  realized she was realizing").
- **Emotion:** **Shown through the body and action, almost never named.** Held breath,
  locked hands, a heart "remembering its rhythm," someone bracing to stay upright. The reader
  feels it because the body does. Do NOT report emotional temperature ("a wave of grief
  washed over her").
- **Menace / intensity:** Carried by **restraint and implication.** Bishop's most chilling
  lines are the quietest ("When the time came, the bed would be his."). Understate the threat;
  let the cold sit in a short, flat sentence. Intensity comes from content and control, never
  from adjectives or exclamation.
- **Figurative language:** **Rare and simple.** When Bishop reaches, it's plain ("a rabbit to
  Daemon's fox") and roughly once a scene. Never the clever, self-admiring image (the cut
  "eats voices" kind). See the hard ceiling in §4.
- **Humor:** Dry, character-located (Korvan's deflection; Karla-style banter among the
  supporting cast). Absent in the crisis and grief beats.

### VOICE UNDER PRESSURE (how the prose breaks)
- **Amelia under overload → FLATTER, tighter, clinical.** Sentences shorten; she counts and
  measures harder; affect numbs. The reader feels the dissociation by the absence of
  feeling-words.
- **Korvan under overload → syntax FRAGMENTS, the body takes over.** Sentences break; physical
  sensation floods; humor vanishes; tense can lurch present for a beat.
- **Loric under (rare) overload → the courtesy cracks for one line, then over-controls.** The
  grief surfaces as something other than rage and is buried mid-sentence.

---

## 2. THE DANGEROUS-BUT-DEVOTED ENGINE (Korvan, Bishop's Daemon technique)

The author wants the Daemon dynamic: **lethal to the world, gentle with the one person.**
Bishop builds it with a specific split — do the same for Korvan the dragon:

- **Actions toward Amelia are tender and controlled;** the *narration* carries the cold,
  dangerous undertone. The gentleness is real; the danger is always felt underneath it.
- **The danger is literal and earned** (he is the dragon, the weapon both sides want) — never
  posturing. He is genuinely capable of terrible things; the restraint is a choice, and the
  reader sees the leash.
- **Restraint is the tension.** In heat and in violence, the held-back is hotter/scarier than
  the released. Bishop: "he had taken them farther than he had meant to."
- **AGENCY GUARDRAIL:** Amelia is dangerous in her own right (blood magyk, a hunted survivor
  who makes her own calls). She is never rescued-passive to his protector. Both dangerous,
  both devoted. This is what keeps the dynamic out of the damsel cliché.

---

## 3. HEAT & DARKNESS REGISTER (author-set 2026-07-08)

**Heat — Bishop voice, back-half explicit (a deliberate step past the comp):**
- Everywhere: Bishop's sensual, body-and-breath, deeply-emotional build. Heat comes from
  rhythm (her stacked "Kissed her until… Kissed her until…" escalation), deep POV, and the
  dangerous-devoted restraint.
- The **back-half consensual scenes go more graphic than Bishop herself writes** — modern
  explicit — but stay in deep POV, stay emotionally loaded, and keep the restraint-tension.
  Never mechanical, never anatomical-for-its-own-sake.
- **Placement (author-set 2026-07-08, commercial spicy cadence):** TWO explicit scenes — the
  first at **Ch.18 (~62%)** once the forced-proximity bond turns real, the second, higher-stakes,
  at the **reunion Ch.26 (~90%)**. Earned by the arc; matches current bestseller placement.

**Darkness — dark intensity, NO sexual violence:**
- Go dark through the war, grief, the hunt, the cost, Loric's grief-horror.
- **Cut the camera on the worst acts.** Bishop models this — her abuse content lands through
  restraint and aftermath ("He couldn't say the word 'rape.'"), never on-page spectacle. Do
  the same: the horror lives in the silence after and the character's reaction.
- **No sexual violence content** in this book (author decision). No graphic torture.

---

## 4. ANTI-PATTERN BUDGET (per 1,000 words — Disruptor enforces; ties to style_check.py)

- **Explanatory/analytical similes (the #1 AI fingerprint): ≤ 2 / 1,000.** Lowered from 3 —
  Bishop is plainer than that. Combined simile+metaphor markers must hold **≤ 3.0 / 1,000**.
- **Clever/ornamental images: target 0.** The cut "eats voices" line is the type specimen. If
  an image makes a smart reader pause to admire or decode it, kill it.
- **Em-dashes: ≤ 9–10 per chapter (author-set 2026-07-08).** Raised from the prior pipeline's strict 4
  toward the Bishop comp (she runs ~18/chapter); we take the middle path. Still prefer the
  period where either works.
- **Adverbs: ALLOWED (correction).** Bishop uses `-ly` adverbs freely (~15/1k) and adverb
  dialogue tags heavily ("said quietly," "asked mildly"). The author's "less flowery" note is
  about METAPHOR/ORNAMENT, not adverbs. Use adverbs naturally, including in dialogue tags
  (~1 per scene is fine, more if earned); just don't let them replace a shown action where the
  action is stronger.
- **Semicolons: avoid** (Bishop 0.2/1k). Use a period.
- **"As if / almost as though": ≤ 1 / 1,000.**
- **Metacognitive narration: ≤ 0.25 / 1,000** (effectively avoid).
- **Emotional-temperature reports ("a wave of X washed over"): ≤ 0.25 / 1,000** (avoid; show
  via body).
- **No repeated 4–6 word tag phrases across chapters.** The three old motifs ("only what
  everyone saw," "eats voices," "survive to fight later") are **CUT** — say each idea once, in
  its own words. (They are removed from the style_check ALLOWLIST.)
- **Lore-dump guard:** dragon ancestral memory surfaces at most once per chapter, ≤ ~80 words,
  always situational. Never a paragraph of history.

---

## 4b. PER-POV DEVICE BUDGET & VOICE EVOLUTION (added 2026-07-08 — voice-wear control)

Deep single-POV + a strong voice card makes the signature devices calcify into formula by the
third chapter of a POV. Measured across Amelia Ch.1/2/5: "twenty years" appeared **14×** and
"never once" **14×**, and the acoustic-rating device fired **twice in one chapter**. That is the
signature turning into a tic. Enforce these caps per chapter, like the anti-pattern budget, and
log usage in `feedback/amelia-voice-ledger.md`.

**AMELIA — per-chapter device caps:**
- **Acoustic-rating a room:** ≤1, and NOT every chapter — skip it entirely in ~1 of every 3.
  Reserve it for a load-bearing use (e.g. the fountain that hides the garden meeting).
- **Explicit counted number as a beat:** ≤3, and vary *what* she counts.
- **"the arithmetic / the sum / weighed the cost" framing:** ≤2.
- **"blood woke at her wrists" (magyk tell):** ≤2, and vary the phrasing.
- **RETIRED / rationed repeat-phrases** (ledger-tracked): "never once" → RETIRED (use *never / not
  once /* recast); "twenty years" ≤1/chapter; "spent her (whole) life", "first time in her life",
  "leave no mark", "make herself small(er)", "the cold working/clear part" — vary every time,
  never verbatim across chapters.

**KORVAN — same discipline (measured Ch.3/4):** fire/craft opinion ≤2/chapter; "catastrophizes a
body sensation as the shift" ≤1/chapter; deflective jokes fine but not every beat. RETIRED: "down,
not away" (his suppression tag). "at his edge" (spatial self-locating tag) → thinned/varied, ≤1.
Log usage in `feedback/korvan-voice-ledger.md`.

**BOOK-WIDE RETIREMENTS (all POVs + narration — these are pipeline tics, not one character's
voice):** **"never once"** is RETIRED across the whole manuscript, not just Amelia. It was a
book-wide habit (Amelia 14×, Korvan/Selwyn 7×). Every POV and the narration use *never / not once /
had never* or recast the line. Any construction that the style/rhythm checks flag as a shared
cross-chapter n-gram is retired book-wide the same way — the per-POV caps above are on top of this,
not instead of it.

**VOICE EVOLUTION — the real fix (don't repeat, DEVELOP):** a signature must change *meaning* as
the character changes. Amelia's counting/arithmetic begins as cage-survival; as she goes hidden →
hunted → choosing → Queen it must bend — she counts different things, under different pressure, or
the strongest beats are when she *stops* counting / cannot make the sum come out. The acoustic
obsession should shift from "can I be overheard" (fear) toward new meaning. Korvan's fire-mastery
shadows the dragon; his catastrophizing pays off when the shift is finally real. Grow each
signature across the arc; do not loop it.

**USE THE OTHER REGISTERS:** each POV has more than one mode. Amelia is not only cold-clinical-
measuring — she has wonder (the "my lady" rapture), warmth (mother, Maren), dry humor, anger.
Rotate registers so the cold-counting mode is not the default in every scene.

---

## 5. PER-CHARACTER VOICE CARDS

#### Amelia (POV)
- **Vocabulary band:** Educated, precise; she counts and measures. Spatial/architectural words
  leak in ("carried," "swallowed," "registered," "interval").
- **Syntax fingerprint:** Balanced, controlled; completes her thoughts. Under stress she
  *shortens* — clipped, clinical.
- **Rhythm:** Measured statements; few questions aloud (she answers them internally).
- **Verbal tics:** Quantifies ("three steps," "a half-second too long"); rates rooms by how
  sound travels; rations warmth.
- **Never says:** Slang, crude oaths, anything sloppy; never says "magic" (always **magyk**).
- **Appearance:** Silver hair — cold, near-grey in low light; the moonlit look of the first
  natural-born vampire. Do NOT use "silver-blonde" (a different project's character).

#### Korvan (POV)
- **Vocabulary band:** Plain, concrete, physical; craft words (fire, rope, grip, weight).
- **Syntax fingerprint:** Action-first; short clauses under stress, run-ons when excited or
  deflecting; talks to animals and objects.
- **Rhythm:** Questions and asides; jokes to dodge — until the dragon, when the humor thins.
- **Verbal tics:** Strong opinions on doing-things-right (esp. fire); catastrophizes sensation.
- **Never says:** Court formality; abstraction for its own sake; anything bloodless.
- **Dangerous-devoted note:** see §2 — tender in action to Amelia, cold undertow in narration.

#### Loric (antagonist, in-scene)
- **Vocabulary band:** Mild, reasonable, civic; the language of fairness and questions.
- **Syntax fingerprint:** Soft interrogatives and permissions; never declarative threats.
- **Rhythm:** Patient, even; lets silence do the work.
- **Verbal tics:** Disclaims agency ("I'm only asking"); phrases accusations as questions.
  (The old fixed catchphrase is cut — vary the wording each time.)
- **Never says:** A direct demand; never raises his voice; never names what he wants.

#### The Chief
- **Vocabulary band:** Weathered, rural-proverbial.
- **Syntax fingerprint:** Long pauses (rendered as beats), then short verdicts; answers
  sideways, with weather and proverbs.
- **Verbal tics:** Deflects hard truths into the landscape. (No fixed repeated creed-phrase.)
- **Never says:** An apology; the word "afraid."

#### The Queen (ROSALIA)
- **Two registers.** To the WORLD: imperial, exact, cold-elegant; imperative mood, instructs,
  never asks. **To AMELIA: warm, doting, unguarded** (author-set 2026-07-08) — Amelia is the
  miracle she never believed she could have. With her daughter she explains, pleads, jokes,
  touches; the command drops away. The tragedy is a loving mother who must still cage her child.
- **Physical:** her touch is vampire-cool but the warmth behind it is real — never render the
  coolness as emotional coldness toward Amelia.
- **Never says (to the world):** "Please." With Amelia, all bets off — she begs if she must.

#### Selwyn (support)
- **Syntax fingerprint:** States the obvious as if it's hard-won wisdom; hedges.
- **Verbal tics:** "Here's the thing" before saying nothing; hoards/lists objects.

#### Maren (support — Amelia's keeper, the human the Queen won't feed on)
- **Syntax fingerprint:** Speaks in negatives and double-negatives; says what she *won't* say.
- **Verbal tics:** Recounts the silver when afraid.

---

## 6. VOICE DIFFERENTIATION MATRIX (cover-the-name test)

| Character | Sharpest distinguisher | Contrast vs nearest |
|-----------|------------------------|---------------------|
| Amelia | Quantifies + rates acoustics; controlled, completes thoughts | vs Queen: Amelia measures *space*; Queen commands *people* |
| Korvan | Fire/craft opinions; body-first; deflective jokes | vs Selwyn: Korvan has real competence; Selwyn fakes wisdom |
| Loric | Disclaims agency; questions & permissions, never demands | vs Chief: Loric is soft to manipulate; Chief is soft to endure |
| The Chief | Proverbs; sideways via weather | vs Loric: Chief deflects to *land*; Loric deflects to the room |
| The Queen | Imperative mood; instructs, never asks | vs Amelia: no questions, no measuring — pure command |
| Selwyn | Obvious-as-wisdom; hoards | vs Korvan: no real expertise behind the certainty |
| Maren | Speaks in negatives; counts silver when afraid | vs everyone: only character who defines by refusal |

No two share a sharpest marker. Amelia/Queen (closest pair, both formal) split by *measuring
vs commanding* and *questions vs none*.

---

## 7. BENCHMARK SAMPLES (to write next, as the measuring sticks)
- **`sample-01-amelia-controlled.md`** — court register: plain, measured, rationed warmth.
- **`sample-02-korvan-breaking.md`** — road register under pressure: fragmented, body-flood.
- **`sample-03-dangerous-devoted.md`** — a Korvan/Amelia beat showing the §2 split (tender
  action, cold undertow), calibrated to the Bishop dynamic.
- **`sample-04-heat-backhalf.md`** — the explicit register (Bishop build + past-comp graphic),
  deep POV, restraint-tension, earned.
