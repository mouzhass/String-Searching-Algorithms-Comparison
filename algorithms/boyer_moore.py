"""Boyer–Moore string search.

Implements:
  - search(text, pattern): return list of match start indices
  - search_with_stats(text, pattern): return matches + comparison count
  - run_single(text, pattern): convenience wrapper that times a single run
  - run_multi(text, patterns): repeat single-pattern search for multiple patterns
"""