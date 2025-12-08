def search(text, pattern):
    matches = []
    comparisons = 0
    n = len(text)
    m = len(pattern)

    if m == 0:
        return matches, comparisons

    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1

        if j == m:
            matches.append(i)

    return matches, comparisons