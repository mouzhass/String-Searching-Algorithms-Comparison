def search(text, pattern):
    matches = []
    n = len(text)
    m = len(pattern)

    # Empty pattern matches at every position
    if m == 0:
        return list(range(n + 1))

    #align the pattern at each position in the text
    for i in range(n - m + 1):
        ok = True

        # Compare pattern with the text one character at a time
        for j in range(m):
            if text[i + j] != pattern[j]:
                ok = False
                break

        # If all characters matched, record the position
        if ok:
            matches.append(i)

    return matches
