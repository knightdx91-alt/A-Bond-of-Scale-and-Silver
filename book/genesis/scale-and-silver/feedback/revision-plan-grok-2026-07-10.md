# Developmental Revision Plan — "Surgical Pacing Pass" (2026-07-10)

**Trigger:** external cross-model read from **Grok** (first genuinely independent market read).
**Author decisions (2026-07-10):** (1) **STAY adult romantasy** (do NOT reposition as literary
fantasy); (2) do the **surgical pacing pass**, NOT the ruthless 20–30% cut.

## Why surgical, not ruthless (the reasoning, so a fresh session doesn't re-litigate)
- Grok judged the book against **trad/commercial literary fantasy** (90–110k, DAW/Orbit). The
  author has chosen **romantasy**, where **150k is within band** and the interiority/slow-burn is
  a feature the audience wants (our beta Devourer/Devoted personas *loved* it).
- A 30% cut (~46k) can't be done by trimming prose — it means merging/deleting scenes and dropping
  threads = a **different book**. A 20% cut (~31k) changes the experience but not the arc.
- **What Grok is RIGHT about, regardless of genre:** (a) the **first 50–100 pages sag** ("reaction
  mode by Ch.10"); (b) **specific motifs are hammered every chapter** and fatigue the reader;
  (c) **Della/Maren blur**; (d) the **gift's cost/limits** need to bite so the "never a person"
  break is truly expensive. Fix these WITHOUT gutting the voice.
- **Target landing:** ~135–145k (a ~6–12% trim), faster front, **same story + voice**.

## The four workstreams

### 1. Accelerate Ch.1–9 (the core fix — "reaction mode by Ch.10")
Goal: get Amelia **deciding/acting** sooner and cut contemplative dwell. Every early chapter must
advance plot OR character in a NEW direction (no chapter that only re-states her cage).
- **Ch.1 (5,027w):** keep the mother/daughter weight (it works — Grok praised it). Tighten the
  longest reflection stretches; get to the *decision to escape* seed faster. Trim ~200–350w.
- **Ch.2 (5,002w):** servants'-passages tour is atmospheric but slow — compress the walk; keep the
  "being no one is a skill" turn. Trim ~250–400w.
- **Ch.3–4 (Korvan, ~5k each):** these establish Korvan; keep but tighten camp interiority.
- **Ch.5 (5,190w):** the banquet "among people" — highest mirror/count density; compress her
  processing of the crowd, keep the sensory first-contact. Trim ~250–400w.
- **Ch.6 (garden) / Ch.7 (TP1, "Heads I Win"):** protect the plot turns; trim lead-in dwell.
- **Ch.8–9 (war declared / escape):** these are the propulsion — make sure the escape *lands*
  sooner and the stakes escalate; least cutting here, most acceleration.
- **Consider merging** two of the thinnest/most-static early chapters if a clean seam exists
  (candidate: a Ch.3↔4 or Ch.5-adjacent merge) — ONLY if it doesn't break a POV alternation beat.
  Default is tighten-in-place; merge only on a clear win.

### 2. Thin the over-hammered motifs (per-chapter caps — not elimination)
Keep each motif as signature, but stop hammering it every chapter. Suggested ceilings per chapter:
- **"must not be seen / being seen / unseen":** ≤1 explicit statement per chapter (it's the theme —
  let scenes carry it, don't re-narrate it). Hotspots: Ch.6 (×4), Ch.1/7 (×3).
- **counting / "count":** keep as characterization but cut filler instances. Hotspots: Ch.1 (×10),
  Ch.2/5/9 (×7). Aim ≤4–5 meaningful uses/chapter.
- **acoustics / "rate a room" / "parts in ten":** ≤1 per chapter (voice-wear already caps
  'acoustic-rating a room'; extend the discipline).
- **mirror / glass / reflection:** Ch.5 has ×6 — thin to ~2.
- **beeswax / cold stone:** Ch.2 ×4 — thin to ~2; it's a bookend motif (Ch.1↔Ch.29), keep it rare
  so it stays potent.
- **"the sum / arithmetic":** SANCTIONED characterization (see style-flags.md) — do NOT strip, but
  don't add; Ch.1 ×4 is fine.
Re-run `voice_wear_check.py` + `style_check.py` after; the point is *cross-chapter* fatigue, which
the tools only partly catch — read for it.

### 3. Sharpen Della vs. Maren (they blur — "loyal/knowing/tragic")
- **Della** = the childhood-nurse warmth, domestic, inside the castle, quiet grief; her love is
  tactile/practical (dressing, the laundry stair). Give her ONE distinct verbal/physical tell.
- **Maren** = the court-still servant, dry, counts buttons, the one the Queen won't feed on; her
  love is strategic/withholding, "the grammar that never tells you straight." Already more distinct
  in the back half — push the front-half Della scenes to NOT read like Maren.
- Action: one differentiating beat each in their early appearances; ensure diction differs.

### 4. Harden the gift's cost/limits (avoid deus-ex; make "never a person" expensive)
- The heat-drain gift must have a **named, consistent limit** so it can't feel like a convenient
  tool. The Selwyn ford death (Ch.28) already establishes "power vast, but untrained/too green to
  catch a fast wound" — seed that limit EARLIER (Ch.2 ritual, Ch.5, Ch.11 near-break) so it pays off.
- The "never a person" rule: make an early breach-temptation carry a concrete stakes-cost, not just
  emotional weight. Ch.11 (the near-reach for Korvan) is the anchor — make sure it's felt as danger.

## Per-chapter discipline (unchanged from house rules)
For each chapter touched: read → cut/tighten/accelerate → `bash tools/check_chapter.sh <N>` clean
(grammar/style/metaphor/rhythm/show-tell/voice-wear/word-floor ≥5,000... **NOTE:** if a surgical
cut drops a chapter below the 5,000 floor, that's acceptable HERE by author intent (we are trimming
on purpose) — log it, don't pad it back with reflection) → verify no new cross-chapter n-gram →
commit per chapter. Hold all canon guardrails. Keep the two explicit scenes (Ch.18, Ch.26) and the
three couple beats (Ch.21 open, Ch.24 yearning, Ch.29 claim) intact.

## Order of execution
Ch.1 → Ch.2 → ... → Ch.9 (front act first — highest ROI), then re-measure total word count and the
motif density book-wide, then decide if Ch.10–17 need a lighter thinning pass. Re-run the beta panel
+ (ideally) another external read after the front-act pass.

## Status
- [x] Ch.1  - [x] Ch.2  - [x] Ch.3  - [x] Ch.4  - [x] Ch.5  - [x] Ch.6  - [x] Ch.7  - [ ] Ch.8  - [ ] Ch.9
  - Ch.7 note: reviewed, NO cut. Protected TP1 (the exposure). The 'seen' motif here is
    the load-bearing irony (want-granted-as-catastrophe), the lead-in 'one more look'
    repetition is a deliberate drumbeat, and the blood-magyk restraint beat seeds workstream 4.
    No non-load-bearing dwell found; forcing a trim would damage the front-act payoff.
  - Ch.8 note: reviewed, NO cut. Propulsion chapter (war declared, father's 'bearable door'
    creed, the shame-of-relief). Already 4982w (under floor) and flagged least-cutting; the
    relief/shame passage is characterization, not cage-dwell. Tight and forward-driving.
  - Ch.9 note: reviewed, NO cut. Propulsion payoff (mother/daughter inherit-vs-choose argument
    = the book's thematic seed; the Maren gate scene, already distinct via spoon-counting; the
    first-sky landing = the cage-arc's earned catharsis). Already 5021w; least-cutting per plan.
- [x] #3 Della vs Maren — Della's tell locked in Ch.1 (nurse's endearment 'lamb' + existing
      bedside-soft voice / slowly-slid bolt / cheek-touch), which Ch.24 already calls back to;
      Maren stays the dry counter (spoons/buttons) who never says it straight. They never co-appear;
      axis = touch+spoken-warmth (Della) vs count+withheld (Maren). Diction confirmed distinct.
- [x] #4 Gift cost/limit — SEEDED in the Ch.2 ritual: the mother names the asymmetry (taking is
      easy/fast — a candle, a fish, a man go out by degrees; holding a life IN, 'catching a fast
      wound before it empties', is the slow craft of ~a thousand years she hasn't the hours for —
      'Strength stops. Only craft catches, and craft is only time'). Directly pays off the Ch.28
      Selwyn total-loss ('strength to command the blood, not yet the craft to catch it in time').
      Worded to avoid a verbatim cross-chapter n-gram (kept the conceptual echo, not the phrase).
- [x] Mid-book (Ch.10–17) thinning DONE (author-requested). Light surgical cuts of genuine
      restatement in Ch.10 (−57, doubled 'instinct already decided'), Ch.11 (−35, near-break
      meaning-coda), Ch.13 (−20, doubled 'waiting for him to be afraid'), Ch.14 (−31, 'can't
      reconcile the two halves' pile-up), Ch.15 (−44, re-explained 'can't argue a dragon').
      Ch.12/16/17 reviewed and PROTECTED (no cut): Ch.12 & Ch.16 are dense/essential (Ch.16
      already had a de-tic pass); Ch.17 is Maren's chapter whose high 'count' density IS her
      signature (workstream #3) and was already tightened once. Each cut gate-clean, committed
      per chapter. Mid-book total change ~−187w; book still well within band.
- [x] Beta panel ROUND 7 + Genesis Floor re-eval ROUND 3 DONE (judging the full surgical pacing pass).
      Beta: the two conservative anchors ROSE on genuine structural closes — Critic 8.0→8.5 (over-
      narrated front + convenient gift both closed at sentence level), Hostile 7.5→8.0 (gift now has a
      governor seeded early/honored late), Casual 7.5→8.0 (front stopped asking to wade;
      Della/Maren now distinct); Devourer 9, Devoted 9.5 held (no collateral to the interiority).
      No new blocking item. Floor re-eval: ALL touched chapters PASS ≥8.5, Ch.2 & Ch.5 STRENGTHENED,
      zero regression, anti-AI pattern density reduced (style 614→609). Reports:
      evaluations/review/beta-reader-panel-round7.md + genesis-floor-re-eval-2026-07-10-round3.md.
      Panel's operative call: STOP cutting (fat exhausted without going cold). Optional ~1hr: the
      "a year" ×3 idioms (Ch.11/25) + one whale-iron anchor line (Ch.21). External human beta = the
      one remaining non-pipeline validation.
- [ ] (deferred, optional) External human romantasy beta read (the only non-pipeline validation left).
