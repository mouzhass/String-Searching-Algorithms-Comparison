import time
import matplotlib.pyplot as plt
from algorithms.naive import search as naive_search
from algorithms.kmp import search as kmp_search
from algorithms.boyer_moore import search as bm_search
from algorithms.aho_corasick import search as aho_search


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


# Step 1: Choose a file from menu
def choose_file(options, file_type):
    print(f"\n=== Select a {file_type} file ===")
    for key, (filename, description) in options.items():
        print(f"{key}. {filename:<30} - {description}")

    while True:
        choice = input("Enter choice: ").strip()
        if choice in options:
            filename, description = options[choice]
            print(f"\nSelected {file_type}: {filename} ({description})")
            return filename
        else:
            print("Invalid selection. Try again.")


# Step 2: Load a file
def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# Step 3: Run one algorithm and time it
def run_algorithm(algorithm_name, search_function, text, patterns):
    """Run a single algorithm and return its results"""

    print(f"Running {algorithm_name}...")

    # Start timer
    start_time = time.perf_counter()

    # Run the algorithm
    total_matches = 0
    total_comparisons = 0

    for pattern in patterns:
        matches, comparisons = search_function(text, pattern)
        total_matches += len(matches)
        total_comparisons += comparisons

    # End timer
    end_time = time.perf_counter()
    time_ms = (end_time - start_time) * 1000

    return total_matches, total_comparisons, time_ms


# Step 3: Create bar charts
def create_plots(results):
    """Make 2 charts showing execution time and comparisons"""

    # Get data from results
    algorithm_names = []
    comparison_counts = []
    times = []

    for name, matches, comparisons, time_ms in results:
        algorithm_names.append(name)
        comparison_counts.append(comparisons)
        times.append(time_ms)

    # Create 2 side-by-side charts
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Algorithm Performance Comparison', fontsize=18, fontweight='bold')

    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']

    # Chart 1: Execution Time
    bars1 = ax1.bar(algorithm_names, times, color=colors[:len(algorithm_names)],
                    edgecolor='black', linewidth=1.5, alpha=0.8)
    ax1.set_title('Execution Time', fontsize=14, fontweight='bold', pad=15)
    ax1.set_ylabel('Time (milliseconds)', fontsize=12, fontweight='bold')
    ax1.tick_params(axis='x', rotation=45, labelsize=11)
    ax1.tick_params(axis='y', labelsize=11)
    ax1.grid(axis='y', alpha=0.3, linestyle='--')

    # Add value labels on bars
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                 f'{height:.2f}',
                 ha='center', va='bottom', fontsize=10, fontweight='bold')

    # Chart 2: Comparisons
    bars2 = ax2.bar(algorithm_names, comparison_counts, color=colors[:len(algorithm_names)],
                    edgecolor='black', linewidth=1.5, alpha=0.8)
    ax2.set_title('Character Comparisons', fontsize=14, fontweight='bold', pad=15)
    ax2.set_ylabel('Number of Comparisons', fontsize=12, fontweight='bold')
    ax2.tick_params(axis='x', rotation=45, labelsize=11)
    ax2.tick_params(axis='y', labelsize=11)
    ax2.grid(axis='y', alpha=0.3, linestyle='--')

    # Add value labels on bars
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                 f'{int(height):,}',
                 ha='center', va='bottom', fontsize=10, fontweight='bold')

    plt.tight_layout()

    # Save and show
    filename = f'results_{time.strftime("%Y%m%d_%H%M%S")}.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"\nChart saved as: {filename}")
    plt.show()


# Step 4: Main program
def main():
    print("="*50)
    print("STRING SEARCH ALGORITHM COMPARISON")
    print("="*50)

    # Ask user to select files from menu
    text_file = choose_file(TEXT_FILES, "text")
    pattern_file = choose_file(PATTERN_FILES, "pattern")

    # Load the files
    print("\nLoading files...")
    text = load_file(text_file)
    patterns = load_file(pattern_file).splitlines()
    patterns = [p.strip() for p in patterns if p.strip()]

    print(f"Text: {len(text)} characters")
    print(f"Patterns: {len(patterns)}")

    # Store results here
    results = []

    # Run each algorithm
    print("\n" + "="*50)

    # 1. Naive
    matches, comps, time_ms = run_algorithm("Naive", naive_search, text, patterns)
    results.append(("Naive", matches, comps, time_ms))

    # 2. KMP
    matches, comps, time_ms = run_algorithm("KMP", kmp_search, text, patterns)
    results.append(("KMP", matches, comps, time_ms))

    # 3. Boyer-Moore
    matches, comps, time_ms = run_algorithm("Boyer-Moore", bm_search, text, patterns)
    results.append(("Boyer-Moore", matches, comps, time_ms))

    # 4. Aho-Corasick (only if multiple patterns)
    if len(patterns) > 1:
        print("Running Aho-Corasick...")
        start_time = time.perf_counter()
        ac_results, comparisons = aho_search(text, patterns)
        end_time = time.perf_counter()

        total_matches = sum(len(matches) for matches in ac_results.values())
        time_ms = (end_time - start_time) * 1000

        results.append(("Aho-Corasick", total_matches, comparisons, time_ms))

    # Print results table
    print("\n" + "="*50)
    print("RESULTS:")
    print("="*50)
    print(f"{'Algorithm':<15} {'Matches':<10} {'Comparisons':<15} {'Time (ms)'}")
    print("-"*50)

    for name, matches, comps, time_ms in results:
        print(f"{name:<15} {matches:<10} {comps:<15,} {time_ms:.4f}")

    print("="*50)

    # Create the charts
    print("\nGenerating charts...")
    create_plots(results)

    print("\nDone!")


if __name__ == "__main__":
    main()