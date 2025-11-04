# algorithms/naive.py
# Purpose: Baseline sliding-window matcher (O(n*m)).
# Functions:
#   - search(text, pattern) -> list[int]
#   - search_with_stats(text, pattern) -> dict (matches, comparisons, time)
# Search loop:
#   - For i in 0..n-m: compare pattern[j] with text[i+j] left→right.
#   - Break on first mismatch; record i on full match.
# Metrics:
#   - Count every char comparison.
#   - Time only the search (no preprocessing).
# Edge cases: empty pattern → match at all positions; pattern longer than text.
# Tests: single hit/miss, multiple and overlapping matches, boundaries.
