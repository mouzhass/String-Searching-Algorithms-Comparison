def build_bad_char_table(pattern):
    table = {}                     # stores last index of each char
    for i, ch in enumerate(pattern):
        table[ch] = i              # update with latest position
    return table


def search(text, pattern):
    n = len(text)
    m = len(pattern)
    comparisons = 0

    if m == 0:
        return [], comparisons

    bad = build_bad_char_table(pattern)
    matches = []

    i = 0   # starting index in text

    # slide pattern across text
    while i <= n - m:
        j = m - 1  # compare from right side of pattern

        # move left until mismatch or full match
        while j >= 0:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j -= 1

        if j < 0:
            matches.append(i)      # full match found
            i += 1                 # shift by 1
        else:
            # compute how far to shift based on mismatched character
            mismatched_char = text[i + j]
            last_occ = bad.get(mismatched_char, -1)
            shift = max(1, j - last_occ)
            i += shift             # skip ahead

    return matches, comparisons
