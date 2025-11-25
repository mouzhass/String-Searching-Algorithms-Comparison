"""
    Build the LPS array (Longest Prefix which is also Suffix).
    lps[i] tells us how much of the pattern we can reuse after mismatch.

    Find all starting positions of pattern in text using KMP.
    """
def build_lps(pattern):
    m = len(pattern)
    lps = [0] * m

    j = 0  # length of current matched prefix

    for i in range(1, m):
        # move j back until characters match
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]

        # if they match, extend the prefix
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    return lps


def search(text, pattern):
    n = len(text)
    m = len(pattern)

    if m == 0:
        return list(range(n + 1))

    lps = build_lps(pattern)
    matches = []

    i = 0  # pointer in text
    j = 0  # pointer in pattern

    while i < n:
        # characters match -> move forward
        if text[i] == pattern[j]:
            i += 1
            j += 1

            # entire pattern matched
            if j == m:
                matches.append(i - j)
                j = lps[j - 1]  # continue searching

        else:
            # mismatch: reuse previous prefix
            if j > 0:
                j = lps[j - 1]
