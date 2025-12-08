def build_bad_char_table(pattern):
    table = {}
    for i, ch in enumerate(pattern):
        table[ch] = i
    return table


def search(text, pattern):
    n = len(text)
    m = len(pattern)
    comparisons = 0

    if m == 0:
        return [], comparisons

    bad = build_bad_char_table(pattern)
    matches = []

    i = 0

    while i <= n - m:
        j = m - 1

        while j >= 0:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j -= 1

        if j < 0:
            matches.append(i)
            i += 1
        else:
            mismatched_char = text[i + j]
            last_occ = bad.get(mismatched_char, -1)
            shift = max(1, j - last_occ)
            i += shift

    return matches, comparisons
