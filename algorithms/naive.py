def search(text, pattern):
    matches = []
    n = len(text)
    m = len(pattern)

    if m == 0:
        return list(range(n + 1))

    for i in range(n - m + 1):
        ok = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                ok = False
                break
        if ok:
            matches.append(i)

    return matches