def search(text, pattern):
    matches = []          # list of all match positions
    comparisons = 0       # number of character comparisons made
    n = len(text)
    m = len(pattern)

    # no work needed for empty pattern
    if m == 0:
        return matches, comparisons

    # try matching the pattern starting at each position in the text
    for i in range(n - m + 1):
        j = 0

        # compare characters of pattern with text
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:   # stop if mismatch
                break
            j += 1

        # if we matched all characters, record this position
        if j == m:
            matches.append(i)

    # return where matches occurred and how many comparisons were done
    return matches, comparisons
