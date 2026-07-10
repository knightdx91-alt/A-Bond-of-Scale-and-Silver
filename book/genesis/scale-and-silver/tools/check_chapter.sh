#!/usr/bin/env bash
# Consolidated per-chapter gate runner for A Bond of Scale and Silver.
# Usage: bash tools/check_chapter.sh <chapter-number>
# Runs EVERY gate a finalized chapter must pass, so none is ever skipped:
#   1. style_check   (too-flowery: simile/em-dash/adverb + cross-chapter n-grams)
#   2. grammar_check (HARD: doubled words, spacing, a/an; + long-sentence report)
#   3. rhythm_check  (flat triplets / unsanctioned anaphora)
#   4. show_tell     (too-descriptive: filter/abstraction; chapter row + book heavies)
#   5. voice_wear    (per-POV device calcification / retired phrases)
#   6. word floor    (>= 5000 words)
# Genesis Floor >= 8.5 (book-evaluator) and the PACING check are judgement gates —
# this script prints a reminder; they are not mechanical.
set -uo pipefail
cd "$(dirname "$0")/.." || exit 2
N="${1:?usage: check_chapter.sh <chapter-number>}"
CH="manuscript/chapters/chapter-${N}.md"
[ -f "$CH" ] || { echo "no such chapter: $CH"; exit 2; }

line() { printf '\n=== %s ===\n' "$1"; }

line "1. STYLE (too-flowery)";      python3 tools/style_check.py 2>&1 | grep -iE "Ch *${N}\b|CEILING|RESULT"
line "2. GRAMMAR (hard)";           python3 tools/grammar_check.py 2>&1 | grep -iE "chapter-${N}\.md:|^RESULT|RESULT:"
line "3. RHYTHM";                   python3 tools/rhythm_check.py 2>&1 | grep -iE "chapter-${N}\.md|TOTAL"
line "4. SHOW/TELL (too-descriptive) — chapter row + any book-wide heavies for this ch"
python3 tools/show_tell_check.py 2>&1 | grep -E "chapter *wds|chapter-${N}\.md"
line "5. VOICE-WEAR";               python3 tools/voice_wear_check.py 2>&1 | grep -iE "\[.*\].*ch |RESULT"
line "5b. METAPHOR/SENTENCE-SHAPE (Bishop: figurative load + long-sentence %)"
python3 tools/metaphor_check.py 2>&1 | grep -E "wds|^ *${N} " | head -2
python3 tools/metaphor_check.py "$N" >/dev/null 2>&1 || echo "   ^ over a Bishop ceiling (FIG>4.0/1k or LONG>18% of sentences) — split/trim"
line "6. WORD FLOOR (>=5000)";      wc -w "$CH"
line "JUDGEMENT GATES (not mechanical — do these by hand every chapter)"
printf '  [ ] Genesis Floor >= 8.5 (book-evaluator, 7 dims) -> evaluations/chapter-%s-eval.md\n' "$N"
printf '  [ ] PACING check vs neighbors (length band, dialogue share, emotional slot, hook)\n'
printf '  [ ] update feedback/progress.md + feedback/pov-map.txt\n'
