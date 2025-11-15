from collections import deque

class Node:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.output = []   # list of pattern IDs


def build_automaton(patterns):
    """
    Build trie + failure links.
    Return the root node.
    """
    root = Node()

    # 1. Build trie
    for pid, pat in enumerate(patterns):
        node = root
        for ch in pat:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.output.append(pid)

    # 2. Build failure links using BFS
    queue = deque()

    # Root's children fail to root
    for node in root.children.values():
        node.fail = root
        queue.append(node)

    # BFS
    while queue:
        current = queue.popleft()

        for ch, nxt in current.children.items():
            queue.append(nxt)

            # Follow fail links to find a matching transition
            f = current.fail
            while f is not None and ch not in f.children:
                f = f.fail

            nxt.fail = f.children[ch] if f and ch in f.children else root
            nxt.output += nxt.fail.output

    return root


def search(text, patterns):
    """
    Return dictionary: pattern_id -> list of start positions.
    """
    root = build_automaton(patterns)
    node = root

    results = {i: [] for i in range(len(patterns))}

    for i, ch in enumerate(text):
        # Follow fail links if needed
        while node is not None and ch not in node.children:
            node = node.fail

        if node is None:
            node = root
            continue

        node = node.children[ch]

        # Record matches
        for pat_id in node.output:
            start_index = i - len(patterns[pat_id]) + 1
            results[pat_id].append(start_index)

    return results