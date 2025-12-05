# ✅ 40A. POST-ORDER DP ON TREES (Subtree Sum Example)

# Compute subtree sum for each node using DFS.
from collections import defaultdict

def subtree_sum(n, edges, values):
    """
    Post-order DP on tree.
    Compute sum of values in subtree of each node.
    """

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    res = [0] * (n + 1)

    def dfs(node, parent):
        total = values[node]
        for nei in graph[node]:
            if nei != parent:
                total += dfs(nei, node)
        res[node] = total
        return total

    dfs(1, -1)   # assuming 1 is root
    return res
