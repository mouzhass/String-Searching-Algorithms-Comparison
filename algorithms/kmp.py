# algorithms/kmp.py
# Purpose: Linear-time single-pattern search via prefix (pi) table.
# Functions:
#   - build_pi(pattern) -> list[int], preprocess_comparisons
#   - search(text, pattern) -> list[int]
#   - search_with_stats(text, pattern) -> dict (matches, comparisons, pre_ms, search_ms)
# Preprocessing:
#   - Compute pi[i] = length of longest proper prefix == suffix for pattern[:i+1].
# Search loop:
#   - Maintain j (matched prefix). On mismatch, fall back j = pi[j-1].
#   - On full match, record start, set j = pi[j-1].
# Metrics:
#   - Count comparisons in both pi-build and search.
#   - Time preprocessing and search separately.
# Edge cases: empty pattern, highly repetitive inputs.
# Tests: parity with Naive on diverse inputs; tricky fallback cases.
