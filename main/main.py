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
    "4": ("big_text_50000.txt", "Biggest test to get best results for time")
}

PATTERN_FILES = {
    "1": ("single_pattern.txt", "One pattern -> tests Naive/KMP/BM"),
    "2": ("multi_patterns.txt", "Multiple patterns -> tests Aho-Corasick"),
    "3": ("big_patterns.txt", "Patterns used for big performance test")
}

def choose_file(options, file_type):
    print(f"\n=== Select a {file_type} file ===")
    for key, (filename, description) in options.items():
        print(f"{key}. {filename:<20} - {description}")

    while True:
        choice = input("Enter choice: ").strip()
        if choice in options:
            filename, description = options[choice]
            print(f"Selected {file_type}: {filename} ({description})")
            return filename
        else:
            print("Invalid selection. Try again.")

def run_search():
    # User selects files from menu
    text_file = choose_file(TEXT_FILES, "text")
    pattern_file = choose_file(PATTERN_FILES, "pattern")

    text = load_file(text_file)
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

        # KMP xN
        t0 = time.time()
        total = 0
        for p in patterns:
            total += len(kmp_search(text, p))
        t1 = time.time()
        print("KMP xN:", total, "matches,", (t1 - t0) * 1000, "ms")

        # Boyer-Moore xN
        t0 = time.time()
        total = 0
        for p in patterns:
            total += len(bm_search(text, p))
        t1 = time.time()
        print("Boyer-Moore xN:", total, "matches,", (t1 - t0) * 1000, "ms")

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
