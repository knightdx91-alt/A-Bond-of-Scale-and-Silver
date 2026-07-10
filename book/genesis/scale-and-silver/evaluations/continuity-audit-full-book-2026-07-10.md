# Continuity Audit — Full Book (A Bond of Scale and Silver)

**Date:** 2026-07-10
**Scope:** Full-manuscript sweep, chapters 1–29 (151,724 words)
**Mode:** Post-completion consistency pass (no `ENTITY_STATE.yaml` present; databases built from the text)
**Prior continuity audits found:** none (per-chapter evals/pacing only)

**Total issues:** 12 — **Critical: 0 | Warning: 5 | Minor: 4** (plus 3 verified-clean notes)

## RESOLUTION STATUS (applied 2026-07-10, all gate-clean)
- **WARN-001 (force 40 vs 4,000) — FIXED.** Ch.15 now plants the muster: the forty-strong banquet
  train came down, in the weeks since the war-banner went up, into a gathered war-host four thousand
  strong (the clans answered the call on the march home). Ch.19 Selwyn reframed to "forty in the
  chief's own train alone, and a host behind it" — the forty is now explicitly a subunit.
- **WARN-002 (chief: dragon "didn't exist") — FIXED.** Ch.22 reframed so the chief's shock is
  *whose* the real dragon is, not *whether* one exists: "a real one crossed the sky over my own camp
  and woke four thousand of my people to it… and it's my own boy." (Ch.21's line was about the
  *witch*, not the dragon — already consistent, left as-is.)
- **WARN-003 (Amelia's capture unresolved) — FIXED.** Ch.23 opening now bridges it: she dropped the
  three Crown escorts non-lethally (slowed their hearts to a faint, explicitly held at the edge and
  did NOT go over — preserving Ch.24 as her first *kill*) and held her own torn thigh shut on the
  road (pays off the Ch.20 heal-a-vessel mechanic).
- **WARN-004 (Maren's transit) — FIXED.** Ch.28 now bridges it: word came down the coast that the
  Queen had ridden to the head of the war to find her daughter; Maren left the fish-house to reach
  her (Amelia woke to the empty gate and understood).
- **MINOR-001 (Maren tenure) — FIXED.** Ch.2 "eighteen years" → "nineteen years" (matches Ch.11/17).
- **MINOR-002 (blood vial) — FIXED.** Ch.23 now "the empty vial cold against her breast, dry these
  two weeks, the last of her mother" (consistent with Ch.12 "vial dry").
- **WARN-005 (roan gelding) — ACCEPTED as a deliberate Book-Two seed; logged, not changed.**
- **MINOR-003 (Selwyn's betrothal) & MINOR-004 (Della) — ACCEPTED as open threads / sequel seeds
  (omissions, not contradictions); logged for Book Two, manuscript left as-is.**
- Post-fix gates: grammar clean, metaphor/sentence-shape clean, style within ceilings, voice-wear
  clean, rhythm unchanged, no new cross-chapter n-grams, all touched chapters ≥5,000 words.
  Whole book now 152,116 words.

**META / FOURTH-WALL NARRATION: NONE.** Confirmed by full read + grep. The prose never
addresses "the reader," never refers to itself as a book/story/chapters non-diegetically, and never
uses "as we saw / in this tale / two chapters ago." Every occurrence of "the tale/the story" is the
in-world rumour/propaganda (legitimate). The recurring device "he was collecting the moments a
person carries, tonight" and similar are close-third narration, not fourth-wall. The mechanical grep
result is confirmed by hand.

---

## CANON GUARDRAILS — VERIFIED CLEAN

- **magyk spelling:** only "magyk" appears (Ch.7, Ch.15); zero instances of "magic." ✓
- **Silver hair (Amelia):** consistent every appearance; the cold near-grey moon-silver, never
  "silver-blonde." ✓
- **No sexual violence:** both explicit scenes (Ch.18, Ch.26) fully consensual; the "protection"
  courtesies (Ch.5) and worst acts are handled with the camera cut, as required. ✓
- **Atlantis / dragon-memory:** Atlantis is named once, situationally, in Loric's Ch.7 dialogue
  (vampires "came off the boats out of Atlantis") — not a lore-dump. The dragon ancestral memories
  (Ch.15, 16, 21, 22, 27) concern the dragons' own history (warm sky / red-sky massacre / hiding
  under the mountain) and never link to Atlantis. ✓
- **Chief knows the bond genuine (Ch.8); chief LEARNS the dragon on-page in Ch.22 and never
  re-learns it (Ch.29 he plainly knows).** ✓
- **Blood-magyk mechanics are internally consistent:** stop/hold hearts (Ch.13 spares 7; Ch.24
  kills 6; Ch.28 kills Loric); heal by holding a single torn vessel shut (Ch.20 child; Ch.28 Selwyn);
  and the deliberately tragic limit — the power CANNOT save a body "a war had opened" (Ch.28: fails
  for the Queen, is refused for Maren) but holds one clean vessel easily. Ch.20 also correctly flags
  healing as the "near neighbour" of vampire-making. No contradiction across Ch.13/20/24/28. ✓
- **Reader-only reveal — Queen dies never knowing Loric's name (Ch.28):** intact. The Queen never
  looks at or names Loric; she dies with her face to Amelia. (Note: the Queen's canon name "Rosalia"
  is never spoken in the text at all — this is not an error and actually reinforces the motif.) ✓
- **Korvan late first shift on the first full moon after coming-of-age (Ch.15):** ✓ (Ch.12 is a
  near-shift fever/foreshadow, not the shift). War-declaration order (Ch.7 reveal → Ch.8 declaration
  → Ch.9 cage-reason expires) is consistent. "Twenty-two days after the Elver" (Ch.29) contradicts
  nothing; the climactic battle is at the Elver falls-crossing (Ch.27–28). ✓
- **Whale-iron "two nets"** (silver-hunt for Amelia + dragon-hunt for Korvan): set up Ch.19,
  developed Ch.21/25, paid off Ch.27. ✓

---

## WARNING ISSUES

### [WARN-001] Shifter force size contradicts itself: "forty" vs "four thousand"
- **Audit:** World / Character-location scale
- **Chapters:** 3, 4, 10, 11, 19 (forty) vs 15, 16, 22 (four thousand)
- **Description:** The retinue is repeatedly "forty shifters and one boy" (Ch.3 line 107), "forty
  men's fires" (Ch.4), and Amelia hides among "forty men" (Ch.10 line 63, Ch.11 line 17). As late as
  the descent, Selwyn says "There's forty of us in the train alone" (Ch.19 line 21). But the *same
  camp a mile down the fold* is "a camp of four thousand" (Ch.15 line 107/119) and the dragon wakes
  "four thousand people" (Ch.16), carried into Ch.22 ("four thousand people he had put on a road").
  The intimate mechanics of Ch.10–12 (a vampire hidden in one of a few grain carts; a single named
  sentry, Fenn, walking one ring) read like ~40, not an army of 4,000, and no muster from 40 → 4,000
  is ever depicted.
- **Evidence:**
  - Ch.10:63 "smelling forty men who would tear me apart on sight"
  - Ch.19:21 "There's forty of us in the train alone."
  - Ch.15:119 "it would be a thing four thousand people had watched with their own eyes"
  - Ch.16 "the camp's alarm-bell, waking four thousand people to the fact of him"
- **Suggested fix:** Decide whether the returning banquet retinue (~40) and a mustered war-host
  (~4,000) are distinct bodies and make it explicit — e.g., show/say the clans gathered to the
  chief on the road home so that by the mountain the "train" of 40 sits inside a host of thousands.
  Alternatively pick one scale. Keep "forty" for the intimate hiding scenes only if the 4,000 is
  clearly a separate, later-gathered host camped nearby.
- **Cascade risk:** If you resolve to a large host earlier, re-check the Ch.10–12 hiding logistics
  (one grain cart, one sentry) and WARN-002 below.

### [WARN-002] Chief treats the dragon as "a thing that didn't exist" (Ch.21–22) after a real dragon was seen by his own host (Ch.16) and reported nationwide (Ch.17)
- **Audit:** Information flow / who-knows-what-when
- **Chapters:** 16, 17 vs 21, 22
- **Description:** In Ch.16 a real dragon flies over the chief's camp; the alarm-bell wakes the
  whole host and "the whole grey valley turned up and saw." Ch.17 confirms the sighting reaches even
  the distant castle ("a dragon came off a mountain… seen by hundreds"). Yet in Ch.21 the chief says
  he "painted a dragon on that cloth to make the whole country afraid of a thing that didn't exist,"
  and Ch.22 repeats "I have spent a season praying no one would learn it didn't [exist], and here it
  comes down the sky and it's my own boy." The Ch.22 reveal (chief genuinely discovering the dragon
  is Korvan) is canon-correct and works — but the framing that the dragon is a *non-existent*
  invention is hard to square with a real one having flown over his own army days earlier. Even
  without knowing it is Korvan, the chief already knows a real dragon exists.
- **Evidence:**
  - Ch.16 "waking four thousand people to the fact of him… the whole grey valley — turned up, and saw"
  - Ch.17:11 "A dragon… In the dawn, three days back. Hundreds saw it."
  - Ch.21:19 "I painted a dragon on that cloth to make the whole country afraid of a thing that
    didn't exist"
  - Ch.22:81 "praying no one would learn it didn't, and here it comes down the sky and it's my own boy"
- **Suggested fix:** Reframe the chief's lines so the shock is *"the dragon is my son,"* not *"a
  dragon is real."* e.g. "I painted a dragon to scare them — and then a real one crossed my dawn and
  I have dreaded ever since what it meant. I never once dreamed it was you." Preserves the emotional
  reveal while removing the "didn't exist / praying no one learns it doesn't" contradiction.
- **Cascade risk:** Ties to WARN-001 (whose camp/host saw it). None to the Ch.22 discovery beat,
  which stays intact under the reframe.

### [WARN-003] Amelia's capture (Ch.21) is never resolved before she is free at Dunmoor (Ch.23); leg wound silently gone
- **Audit:** Information flow / character-location
- **Chapters:** 21 → 23/24
- **Description:** Ch.21 ends with Amelia shot through the thigh with a quarrel and led south on
  foot by three Crown men toward "a Crown post… the road to the capital," worth a purse taken alive.
  Ch.23 opens with her walking freely into Dunmoor, and by Ch.24 she stands, kneels, walks back
  uphill and climbs with no limp and no reference to the wound. Her escape from the three captors is
  never shown or mentioned, and the thigh wound is never addressed (she can self-heal per Ch.20, but
  it is never stated). A reader will ask "how did she get free, and what happened to her leg?"
- **Evidence:**
  - Ch.21:147 "she let a hunter's hand close on her arm and got up onto her good leg to walk where
    he pointed… walking south toward the ford and the crowd and the road to the capital."
  - Ch.23:5 "Amelia came into it from the north with her hood up… walking the way she had learned
    to walk on the road."
- **Suggested fix:** Add a short bridge (a paragraph in Ch.23's opening or a line of Amelia's
  reflection) covering how she left the three men — she can stop hearts, so a spared/dispatched
  escort is easy to justify — and one clause acknowledging she held her own leg-wound shut on the
  road (paying off Ch.20's heal-a-vessel mechanic).
- **Cascade risk:** Low. Reinforces her agency; harmonises with the blood-magyk healing rule.

### [WARN-004] Maren's transit from Amelia's side (Ch.26 fish-house) to the Queen's side at the Crown high command (Ch.28) is unexplained
- **Audit:** Character-location / information flow
- **Chapters:** 26 → 28
- **Description:** Maren travels east *with Amelia* (Ch.24–25) and is with her at the fish-house the
  night before the battle (Ch.26: "a second shape behind it that stopped at the broken gate"). In
  Ch.28 she is suddenly "at her mother's shoulder" inside the Crown host's high command on the far
  (east) bank — the enemy centre — dying beside the Queen. The text hand-waves it ("Maren had not
  stayed in the low country. Maren had gone to the Queen. Of course she had."), but the logistics —
  leaving Amelia between the fish-house and the battle, crossing to the opposing host, and reaching
  the Queen at the high knot within roughly a day — are neither shown nor plausibly bridged.
- **Evidence:**
  - Ch.26:11 "a second shape behind it that stopped at the broken gate and did not come on."
  - Ch.28:15 "at her mother's shoulder, one step back, in a servant's grey… was Maren. Maren had
    gone to the Queen. Of course she had."
- **Suggested fix:** Plant the departure — a line in Ch.26/27 where Maren tells Amelia she is going
  to find the Queen (and why), and a clause in Ch.28 accounting for how she reached the royal party
  (e.g., the Queen's own approach to the front made contact possible). Even one sentence closes the
  gap and makes the reunion-in-death land rather than jar.
- **Cascade risk:** Low; strengthens the Ch.28 double-death.

### [WARN-005] The chief's roan gelding — heavily-flagged mystery, never paid off
- **Audit:** Plot-thread / Chekhov's gun
- **Chapters:** 3 (setup), 8/10/12/15 (the roan reappears as an ordinary animal)
- **Description:** Ch.3 spends multiple paragraphs on "the horse his father would not ride," framed
  as "the single crack in a man who was otherwise all one weathered piece," a thing Korvan "worried
  at his whole childhood." This is a deliberate, emphasised mystery. It is never explained or paid
  off within Book One (Korvan later simply handles/rides the roan). It reads like an intentional
  sequel seed, but as-is it is a flagged setup with no in-book payoff.
- **Evidence:** Ch.3:61 "A man's allowed one thing he doesn't explain… the single crack in a man
  who was otherwise all one weathered piece."
- **Suggested fix:** If it is a Book-Two seed, that is fine — log it as a deliberate open thread so
  it is not lost. If not, either land a glancing payoff or dial back the Ch.3 emphasis so it reads as
  pure character texture rather than a promise.
- **Cascade risk:** None.

---

## MINOR ISSUES

### [MINOR-001] Maren's tenure: "eighteen years" vs "nineteen years"
- **Chapters:** 2 vs 11/17
- Ch.2:77 "had never in eighteen years let the second one slip"; Ch.11/17 repeatedly "nineteen
  years" ("kept that girl alive for nineteen years"). Amelia is 20. Pick one figure (nineteen is used
  twice and fits Amelia's age better).

### [MINOR-002] The Queen's-blood vial: described as containing blood in Ch.23 though established dry by Ch.12
- **Chapters:** 12 → 23
- Ch.12:87 "The vial dry two days now." Ch.11 had it "down to a mouthful." But Ch.23:115 "her
  mother's blood cold in a vial against her breast" implies blood still inside. If she keeps the
  empty vial as a keepsake, phrase it that way ("the empty vial… the last of her mother"); as
  written it reads as still-full.

### [MINOR-003] Selwyn's betrothal set up (Ch.3), never resolved
- **Chapters:** 3
- Ch.3:35 Selwyn is "betrothed to a girl in the high steadings he'd met twice and did not love and
  could not get out of." His life is otherwise burned down (name spent, follows Korvan, nearly dies,
  "mending" in Ch.29), but the dreaded marriage is dropped without a nod. A single later clause would
  close it; otherwise it is a small orphaned setup.

### [MINOR-004] "Della" opens the book prominently, then vanishes
- **Chapters:** 1 (11 years in service, the bolt-slider) → only a memory in Ch.24
- Not an error (she is a castle servant left behind when Amelia flees), but given her weight in Ch.1
  the total absence of her fate after the exposure/flight is a small loose end. Optional: one line of
  Amelia wondering after Della would close the emotional loop.

---

## TRACKING NOTES (for the Editor / Book Two)

- **Character names/spellings:** stable throughout — Amelia, Korvan, Selwyn, Loric, Maren (surname
  "Vesk," Ch.9), Bricc, Fenn, Harl, Doran, Bret, Enna (deer-clan), Tam, Wren, Della, Bess, Bram,
  Verrin, Corenne. No spelling drift detected.
- **The Queen** is never personally named in-text (canon "Rosalia" unused). Intentional-friendly:
  supports the "died never knowing his name / the unnamed sovereign" register.
- **Timeline spine (coherent):** banquet Ch.1–7 → war declared/leave Ch.8 → journey home + Amelia
  joins Ch.10 → burned village Ch.12 → split to herd-station Ch.13 → first shift (full moon) Ch.15 →
  dragon seen Ch.16 → shieling Ch.18 → descent/ford Ch.19–21 → chief learns dragon Ch.22 → Dunmoor
  Ch.23–24 → to the falls Ch.25–26 → Elver battle Ch.27–28 → coronation +22 days Ch.29.
- **Information-flow spine (clean except WARN-002/003):** only Amelia and Korvan know Korvan is the
  dragon through Ch.21 (Selwyn is deliberately kept ignorant in Ch.19); chief learns Ch.22; the wax
  decree (Ch.23) publicly makes Amelia the acknowledged heir, grounding the Ch.28 succession.
