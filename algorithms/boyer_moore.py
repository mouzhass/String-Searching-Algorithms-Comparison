"""
   Build a table that tells us the last position
   of each character in the pattern.
   Example: pattern = "abcab"
     'a' -> 3
     'b' -> 4
     'c' -> 2
   """

def build_bad_char_table(pattern):
    table = {}
    for i, ch in enumerate(pattern):
        table[ch] = i   # store last index of ch
    return table


def search(text, pattern):
    n = len(text)
    m = len(pattern)

    if m == 0:
        return list(range(n + 1))

    bad = build_bad_char_table(pattern)
    matches = []

    i = 0  # current alignment of pattern on text

    while i <= n - m:
        j = m - 1  # start comparing from the right end

        # move left while characters match
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        #full match
        if j < 0:
            matches.append(i)
            i += 1   # simple shift after match
        else:
            # mismatch — compute how far to shift
            mismatched_char = text[i + j]
            last_occ = bad.get(mismatched_char, -1)

            # shift so the mismatched char lines up with its last occurrence
            shift = max(1, j - last_occ)
            i += shift

    return matches
