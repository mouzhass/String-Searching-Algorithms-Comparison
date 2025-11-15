def build_lps(pattern):
    """
    Build the LPS (longest prefix that is also suffix) array.
    Example: pattern = "ababaca"
    """
    m = len(pattern)
    lps = [0] * m

    j = 0  # length of previous longest prefix-suffix

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    return lps


def search(text, pattern):
    """
    Return all starting indices where pattern occurs in text.
    """
    n = len(text)
    m = len(pattern)

    if m == 0:
        return list(range(n + 1))

    lps = build_lps(pattern)
    matches = []

    i = 0  # index for text
    j = 0  # index for pattern

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:   # full match
                matches.append(i - j)
                j = lps[j - 1]

        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches