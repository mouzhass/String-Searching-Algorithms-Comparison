import time
from algorithms.naive import search as naive_search
from algorithms.kmp import search as kmp_search
from algorithms.boyer_moore import search as bm_search
from algorithms.aho_corasick import search as aho_search

def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# Available test files
TEXT_FILES = {
    "1": ("single_text.txt", "Small file for single-pattern testing"),
    "2": ("multi_text.txt", "Medium file with multiple repeated words"),
    "3": ("big_text.txt", "Large repeated-text file for performance"),
    "4": ("big_text_50000.txt", "50,000-word performance file"),
    "5": ("big_text_100k_words.txt", "100,000-word performance file")
}

PATTERN_FILES = {
    "1": ("single_pattern.txt", "One pattern -> tests Naive/KMP/BM"),
    "2": ("multi_patterns.txt", "Multiple patterns -> tests Aho-Corasick"),
    "3": ("big_patterns.txt", "Patterns used for big performance test")
}

def choose_file(options, file_type):
    print(f"\n=== Select a {file_type} file ===")
    for key, (filename, description) in options.items():
        print(f"{key}. {filename:<25} - {description}")

    while True:
        choice = input("Enter choice: ").strip()
        if choice in options:
            filename, description = options[choice]
            print(f"\nSelected {file_type}: {filename} ({description})")
            return filename
        else:
            print("Invalid selection. Try again.")

def run_search():
    # User selects files
    text_file = choose_file(TEXT_FILES, "text")
    pattern_file = choose_file(PATTERN_FILES, "pattern")

    text = load_file(text_file)
    patterns = load_file(pattern_file).splitlines()

    print(f"\nLoaded {len(patterns)} pattern(s).")


    print("\n=== SEARCH RESULTS ===")

    # NAIVE (always single-pattern logic)
    t0 = time.time()
    if len(patterns) == 1:
        naive_matches = len(naive_search(text, patterns[0]))
    else:
        naive_matches = sum(len(naive_search(text, p)) for p in patterns)
    t1 = time.time()
    print("Naive(Single-Pattern):         ", naive_matches, "matches,", (t1 - t0) * 1000, "ms")

    # KMP
    t0 = time.time()
    if len(patterns) == 1:
        kmp_matches = len(kmp_search(text, patterns[0]))
    else:
        kmp_matches = sum(len(kmp_search(text, p)) for p in patterns)
    t1 = time.time()
    print("KMP:                           ", kmp_matches, "matches,", (t1 - t0) * 1000, "ms")

    # BOYER-MOORE
    t0 = time.time()
    if len(patterns) == 1:
        bm_matches = len(bm_search(text, patterns[0]))
    else:
        bm_matches = sum(len(bm_search(text, p)) for p in patterns)
    t1 = time.time()
    print("Boyer-Moore:                   ", bm_matches, "matches,", (t1 - t0) * 1000, "ms")

    # AHO-CORASICK (ONLY IF MULTI-PATTERN)
    if len(patterns) > 1:
        t0 = time.time()
        ac_res = aho_search(text, patterns)
        t1 = time.time()
        ac_total = sum(len(v) for v in ac_res.values())
        print("Aho-Corasick(Multi-Pattern):   ", ac_total, "matches,", (t1 - t0) * 1000, "ms")


def main():
    while True:
        print("\n============================")
        print("  STRING SEARCHING MENU")
        print("============================")
        print("1. Run a search")
        print("2. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            run_search()
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
