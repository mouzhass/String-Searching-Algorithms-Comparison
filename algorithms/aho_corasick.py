from collections import deque

class Node:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.output = []


def build_automaton(patterns):
    root = Node()

    # Build Trie
    for pid, pat in enumerate(patterns):
        node = root
        for ch in pat:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.output.append(pid)

    # Build Failure Links
    queue = deque()

    for node in root.children.values():
        node.fail = root
        queue.append(node)

    while queue:
        current = queue.popleft()

        for ch, nxt in current.children.items():
            queue.append(nxt)

            f = current.fail
            while f is not None and ch not in f.children:
                f = f.fail

            nxt.fail = f.children[ch] if f and ch in f.children else root
            nxt.output += nxt.fail.output

    return root


def search(text, patterns):
    root = build_automaton(patterns)
    node = root
    comparisons = 0

    results = {i: [] for i in range(len(patterns))}

    for i, ch in enumerate(text):
        comparisons += 1

        while node is not None and ch not in node.children:
            node = node.fail

        if node is None:
            node = root
            continue

        node = node.children[ch]

        for pat_id in node.output:
            start_index = i - len(patterns[pat_id]) + 1
            results[pat_id].append(start_index)

    return results, comparisons
