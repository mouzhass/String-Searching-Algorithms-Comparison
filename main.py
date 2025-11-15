import time
from algorithms.naive import search as naive_search
from algorithms.kmp import search as kmp_search
from algorithms.boyer_moore import search as bm_search
from algorithms.aho_corasick import search as aho_search

def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    text_file = input("Enter text file: ")
    text = load_file(text_file)

    pattern_file = input("Enter pattern file (one pattern per line): ")
    patterns = load_file(pattern_file).splitlines()

    print(f"\nLoaded {len(patterns)} pattern(s).")

    # SINGLE-PATTERN MODE
    if len(patterns) == 1:
        print("Mode: SINGLE-PATTERN SEARCH")

        p = patterns[0]

        print("\n--- Single Pattern Search ---")

        # Naive
        t0 = time.time()
        m = len(naive_search(text, p))
        t1 = time.time()
        print("Naive:", m, "matches,", (t1 - t0) * 1000, "ms")

        # KMP
        t0 = time.time()
        m = len(kmp_search(text, p))
        t1 = time.time()
        print("KMP:", m, "matches,", (t1 - t0) * 1000, "ms")

        # Boyer-Moore
        t0 = time.time()
        m = len(bm_search(text, p))
        t1 = time.time()
        print("Boyer-Moore:", m, "matches,", (t1 - t0) * 1000, "ms")

    # MULTI-PATTERN MODE
    else:
        print("Mode: MULTI-PATTERN SEARCH")

        print("\n--- Multi-Pattern Search ---")

        # Aho-Corasick
        t0 = time.time()
        ac_res = aho_search(text, patterns)
        t1 = time.time()
        total = sum(len(v) for v in ac_res.values())
        print("Aho-Corasick:", total, "matches,", (t1 - t0) * 1000, "ms")

        # KMP repeated
        t0 = time.time()
        total = 0
        for p in patterns:
            total += len(kmp_search(text, p))
        t1 = time.time()
        print("KMP xN:", total, "matches,", (t1 - t0) * 1000, "ms")

        # Boyer-Moore repeated
        t0 = time.time()
        total = 0
        for p in patterns:
            total += len(bm_search(text, p))
        t1 = time.time()
        print("Boyer-Moore xN:", total, "matches,", (t1 - t0) * 1000, "ms")



if __name__ == "__main__":
    main()
