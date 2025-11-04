# algorithms/boyer_moore.py
# Purpose: Right-to-left checks with Bad-Character + Good-Suffix shifts.
# Functions:
#   - build_bad_char(pattern) -> dict[char -> last_index]
#   - build_good_suffix(pattern) -> shift array
#   - search(text, pattern) -> list[int]
#   - search_with_stats(text, pattern) -> dict (matches, comparisons, pre_ms, search_ms)
# Preprocessing:
#   - Bad-char table: last occurrence per char (default -1).
#   - Good-suffix table: standard two-phase computation of shifts.
# Search loop:
#   - Align at s, compare from j = m-1 down to 0.
#   - On match: record s; shift by good_suffix[0].
#   - On mismatch: shift = max(bad_char_shift, good_suffix_shift).
# Metrics:
#   - Count equality checks (include final mismatch check).
#   - Time preprocessing and search separately.
# Edge cases: m==0, m==1, chars absent from pattern.
# Tests: random vs repetitive patterns; compare with Naive/KMP outputs.
