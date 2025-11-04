# algorithms/aho_corasick.py
# Purpose: Multi-pattern search in one pass using trie + failure links.
# Structures:
#   - Node: children dict, fail pointer, output list of pattern IDs.
# Functions:
#   - build_automaton(patterns) -> root, preprocess_stats
#   - search_multi(text, patterns) -> dict[pat_id -> positions]
#   - search_multi_with_stats(...) -> adds comparisons, pre_ms, search_ms
# Preprocessing:
#   - Insert all patterns into trie; mark outputs at terminal nodes.
#   - BFS to set fail links; merge outputs from fail nodes.
# Search loop:
#   - For each char: follow fail links until a child exists; step; emit outputs.
# Metrics:
#   - Count transitions/comparisons while following fails.
#   - Time preprocessing and search separately.
# Edge cases: empty/duplicate patterns, overlapping matches.
# Tests: shared prefixes (he, she, his, hers), subset patterns, overlaps.
