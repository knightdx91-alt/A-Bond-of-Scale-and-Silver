# Rosalia — Style-Flag Tracker

Running log of what the style gate (`tools/style_check.py`) keeps flagging, so we can
spot patterns instead of fixing the same thing chapter after chapter.

## Rules
- **Em-dashes: max 4 per chapter** (absolute). Enforced by `--max-emdash 4` (the default).
- **Simile/metaphor markers: ≤ 4.0 per 1,000 words.**
- **No NEW repeated 4–6 word phrase across chapters** (deliberate motifs go in the ALLOWLIST).
- **Verbal tics: ≤ 6.0 per 1,000 words** for any single tic word.

## How to use this file
After each `python3 tools/style_check.py` run, log anything flagged below.
- If a phrase is flagged **3+ times** and it's a *deliberate* recurring motif → promote it to
  the ALLOWLIST in `tools/style_check.py` (and note it here).
- If a phrase/tic is flagged repeatedly and is **NOT** deliberate → it's an unconscious tic;
  add it to the "watch / kill" list so the writer/disruptor stops reaching for it.

## Approved motifs (in ALLOWLIST — intentional, do NOT "fix")
- "only what everyone saw"
- "eats voices"
- "survive to fight later"  (the Chief's creed)

## Frequently-flagged phrases (count → disposition)
_(none logged yet — populate during the chapter loop)_

| Phrase / tic | Times flagged | In chapters | Deliberate? | Disposition |
|---|---|---|---|---|
| "pressed flat and cold over his heart" | 2 | 21, 22 | echo | RECAST Ch.22 → "flat and cold against his heart" (2026-07-10). Ch.21 keeps origin. |
| "hunters grew old and the world forgot" | 2 | 21, 22 | echo | RECAST Ch.22 → "the hunting men aged out and the world stopped remembering him". Ch.21 keeps origin. |
| "a hundred miles of nothing" | 3 | 21, 22 | echo | RECAST both Ch.22 → "a hundred empty miles" / "the empty folds". Ch.21 keeps origin. |
| "under a writ that wanted" | 3 | 21, 22 | echo | RECAST both Ch.22 → "kept that way by the writ that hunted her" / "a writ that would keep her whole". Ch.21 keeps origin. |
| "the fire went up between them" | 3 | 22 (intra) | motif | KEPT ONE (¶109) as sanctioned; varied the other two (flared/settled; flame threw shadows). 2026-07-10. |

### Sanctioned Ch.21→Ch.22 mirrors (deliberate reveal-chapter resonances — do NOT "fix")
The Ch.22 reveal is written to deliberately recall the Ch.21 ford. The following shared
phrases are intentional echoes and are allowlisted-by-intent (kept as one-way callbacks;
the 5 above were the ones the eval judged too-verbatim and were recast/thinned):
"whale-iron in the alder", "man's for the ten seconds", "came sideways in the meat",
"be counted among the falling", "the black under the world", "bright head going small on",
"the air with both arms", "a foot of water", "standing on a rock", "the reasonable man had".

## Sanctioned deliberate mirrors (NOT tics — do not flag in voice-wear passes)
- **"did not do things that came to nothing"** — Ch.21 uses it as a father→Amelia MIRROR that
  Korvan explicitly notices in-text (the chief's is a wall/won't-look-back; Amelia's is its
  breaking/does-the-futile-thing "with her whole self"). Phrasing varies (he/she) and the two do
  opposite work. Keep as intentional resonance; the only other "came to nothing" hit (Ch.10) is a
  different construction. (logged 2026-07-09)

## Sanctioned plant/payoff echoes (do NOT flatten in de-tic / n-gram passes)
- **Ch.20 → Ch.28 "the power would be equal / was equal; she would not / was not; not yet."**
  Ch.20 ¶91 (child-save reflection) plants the skill-gap: "The power would be equal to such a wound
  and she would not, not yet." Ch.28 ¶151 (Selwyn dies in the ford) pays it off: "The power was
  equal to it. She was not. Not yet." This is the book's best-engineered echo — it converts
  Selwyn's death from a plot-timed event into a planted inevitability. DELIBERATE; keep both.
  (logged 2026-07-10, per Floor re-eval Fix #5.)
- **Ch.29 "twenty-two days" ×2 (¶3 opener + ¶25 crowning)** — the aftermath's time-frame bookend.
  Sanctioned; NOT a tic to thin. (logged 2026-07-10, per Floor re-eval Fix #5.)

## Watch / kill list (unconscious tics to avoid)
_(none yet)_

## Ch.29 sanctioned bookend callbacks (2026-07-10) — final chapter
Ch.29 deliberately closes "in conversation with" Ch.1 and reprises Ch.28's closing imagery
(per the Ch.29 handoff brief). These cross-chapter n-grams are SANCTIONED, not accidental:
- Ch.1 bookends: "beeswax and old stone", "whisper at four parts in ten", "a locked room three
  floors up", "way iron wheels changed their note", "heard across a bright room", "matter that
  it's true the truth" (Rosalia's Ch.1 line, re-heard as Amelia's ruling).
- Ch.28 closing-image reprises: "would go on after all" (the river/falls refrain), "in a red
  ford", "the one dark eye", "told the blood to stay / staying where she told", "alive on the two
  sides", "war off a folding table" (the grey man's fixed identifier), "of the two still hands".
Accidental verbatim lifts from Ch.28 were recast: river-flat register tag, "reading exactly this",
"whole grotesque sum", "no one on the whole field who would ever see", "man who had made every
death", "silver-haired woman standing", "measure the faces the way".
