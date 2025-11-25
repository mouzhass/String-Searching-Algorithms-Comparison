# String-Searching-Algorithms-Comparison
A Python-based project that implements and compares four classic string-searching algorithms — Naive, KMP, Boyer-Moore, and Aho-Corasick — from scratch. The program evaluates their performance on texts of varying lengths and pattern counts, measuring metrics like execution time and match frequency.

# Algorithms 
1. Naive Search

  What it does:
  Looks for the pattern by checking every single spot in the text, one by one.

  Simple explanation:
  “Does the pattern start here? No? Move one step and try again.”

  Good for:
  Small texts, 
  Easy to understand, 
  Worst performance on big files
  

2. KMP (Knuth–Morris–Pratt)

  What it does:
  Searches faster by remembering what it already matched, so it doesn’t re-check the same letters.

  Simple explanation:
  “If I see a mismatch, I already know where to jump next.”

  Why it’s faster:
  It uses a helper table (LPS) to skip ahead instead of restarting.

  Good for:
  When the pattern repeats (like “abababab”), 
  More efficient than Naive
  

3. Boyer–Moore

  What it does:
  Searches from right to left and skips big chunks of text when it finds a mismatch.

  Simple explanation:
  “Start from the end of the pattern. If something doesn’t match, JUMP AHEAD.”

  Why it’s fast:
  It often jumps many characters at once instead of checking every position.

  Good for:
  Long patterns, 
  Big text files, 
  Natural English text

  

4. Aho–Corasick

  What it does:
  Finds many patterns at the same time (like apple, banana, orange, melon all at once).
  
  Simple explanation:
  “Build a big map of all the patterns, then scan the text one time.”
  
  Why it’s amazing:
  It only goes through the text once, no matter how many patterns you have.
  
  Good for:
  Multiple search words, 
  Huge logs / documents, 
  Fast multi-pattern searching, 
