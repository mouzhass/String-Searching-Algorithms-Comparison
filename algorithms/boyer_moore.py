
def build_bad_char_table(pattern):
    """
    For each character in the pattern, store its last index.
    Example: pattern = "abcab"
    table['a'] = 3
    table['b'] = 4
    table['c'] = 2
    """
    table = {}
    for i, ch in enumerate(pattern):
        table[ch] = i
    return table


def search(text, pattern):
    n = len(text)
    m = len(pattern)

    if m == 0:
        return list(range(n + 1))

    bad = build_bad_char_table(pattern)
    matches = []

    i = 0  # shift of pattern over text

    while i <= n - m:
        j = m - 1  # start comparing from the end

        # move left while characters match
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            # full match
            matches.append(i)
            i += 1  # shift by 1 (simple version)
        else:
            # mismatch — compute shift
            mismatched_char = text[i + j]
            last_occ = bad.get(mismatched_char, -1)
            shift = max(1, j - last_occ)
            i += shift

    return matches
