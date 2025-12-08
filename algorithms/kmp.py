def build_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    j = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    return lps


def search(text, pattern):
    n = len(text)
    m = len(pattern)
    comparisons = 0

    if m == 0:
        return [], comparisons

    lps = build_lps(pattern)
    matches = []

    i = 0
    j = 0

    while i < n:
        comparisons += 1
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                matches.append(i - j)
                j = lps[j - 1]
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches, comparisons
