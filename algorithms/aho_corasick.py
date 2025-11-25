"""
   Build the Aho–Corasick automaton:
   1. Build a trie of all patterns.
   2. Build failure links using BFS.
   """

from collections import deque

class Node:
    def __init__(self):
        self.children = {}   # edges: character → next node
        self.fail = None     # failure link (where to go on mismatch)
        self.output = []     # which patterns end at this node


def build_automaton(patterns):
    root = Node()

    # 1. Build Trie
    for pid, pat in enumerate(patterns):
        node = root
        for ch in pat:
            # Create new node if path doesn't exist
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.output.append(pid)   # mark this node as end of pattern


    # 2. Build Failure Links (BFS)
    queue = deque()

    # Root’s children fail back to root
    for node in root.children.values():
        node.fail = root
        queue.append(node)

    # BFS over all nodes
    while queue:
        current = queue.popleft()

        # Check each outgoing edge
        for ch, nxt in current.children.items():
            queue.append(nxt)

            # Follow fail links until we find a node that has this character
            f = current.fail
            while f is not None and ch not in f.children:
                f = f.fail

            # Set the fail link
            nxt.fail = f.children[ch] if f and ch in f.children else root

            # Inherit output patterns from fail link
            nxt.output += nxt.fail.output

    return root


def search(text, patterns):
    root = build_automaton(patterns)
    node = root

    # Prepare result lists
    results = {i: [] for i in range(len(patterns))}

    # Walk through the text
    for i, ch in enumerate(text):

        # Follow fail links if mismatch
        while node is not None and ch not in node.children:
            node = node.fail

        # If we fell off the root, restart from root
        if node is None:
            node = root
            continue

        # Follow the matching child
        node = node.children[ch]

        # Record all patterns that end here
        for pat_id in node.output:
            start_index = i - len(patterns[pat_id]) + 1
            results[pat_id].append(start_index)

    return results
