"""
Aho–Corasick multi-pattern string search.

Implements:
  - search(text, pattern): single-pattern wrapper using AC (build automaton for [pattern])
  - search_with_stats(text, pattern): same as above, with comparisons (approx. char steps)
  - run_single(text, pattern): convenience wrapper that times a single run
  - run_multi(text, patterns): build automaton once, search all patterns in one pass

"""
