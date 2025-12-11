def build_lps(pattern):
    m = len(pattern)
    lps = [0] * m     # longest prefix-suffix lengths
    j = 0             # length of current prefix match

    # build lps by expanding/shrinking prefix matches
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]       # fall back to shorter prefix

        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j          # store prefix length

    return lps


def search(text, pattern):
    n = len(text)
    m = len(pattern)
    comparisons = 0

    if m == 0:
        return [], comparisons

    lps = build_lps(pattern)
    matches = []

    i = 0   # index in text
    j = 0   # index in pattern

    # scan through the text
    while i < n:
        comparisons += 1

        if text[i] == pattern[j]:     # characters match
            i += 1
            j += 1

            if j == m:                # full match found
                matches.append(i - j)
                j = lps[j - 1]        # continue from lps
        else:
            if j > 0:
                j = lps[j - 1]        # shift using lps
            else:
                i += 1                # move forward in text

    return matches, comparisons
