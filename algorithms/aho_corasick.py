from collections import deque

class Node:
    def __init__(self):
        self.children = {}   # outgoing edges (trie transitions)
        self.fail = None     # failure link
        self.output = []     # which patterns end here


def build_automaton(patterns):
    root = Node()

    # Build the Trie
    for pid, pat in enumerate(patterns):
        node = root
        for ch in pat:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.output.append(pid)   # pattern ends at this node

    # Build Failure Links
    queue = deque()

    # root's children fail back to root
    for node in root.children.values():
        node.fail = root
        queue.append(node)

    # BFS to assign failure links deeper in the trie
    while queue:
        current = queue.popleft()

        for ch, nxt in current.children.items():
            queue.append(nxt)

            f = current.fail
            # follow failure links until a match for ch is found
            while f is not None and ch not in f.children:
                f = f.fail

            # set fail link: either the matching child or root
            nxt.fail = f.children[ch] if f and ch in f.children else root

            # inherit output patterns from the fail node
            nxt.output += nxt.fail.output

    return root


def search(text, patterns):
    root = build_automaton(patterns)
    node = root
    comparisons = 0

    # store list of matches for each pattern
    results = {i: [] for i in range(len(patterns))}

    # scan the text once
    for i, ch in enumerate(text):
        comparisons += 1

        # follow fail links until a valid child is found
        while node is not None and ch not in node.children:
            node = node.fail

        # if fell all the way to None, restart at root
        if node is None:
            node = root
            continue

        node = node.children[ch]

        # record all patterns that end here
        for pat_id in node.output:
            start_index = i - len(patterns[pat_id]) + 1
            results[pat_id].append(start_index)

    return results, comparisons
