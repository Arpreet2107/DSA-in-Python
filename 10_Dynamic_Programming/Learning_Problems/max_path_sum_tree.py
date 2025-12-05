# ✅ 42. MAXIMUM PATH SUM IN TREE

# Applies to general tree (not necessarily binary tree).

# Path can start & end anywhere.

# DP Idea

# For each node:

# best downward path = max child contribution

# best full path = sum of top 2 children + node value
from collections import defaultdict

def max_path_sum_tree(n, edges, values):
    """
    Maximum path sum in any general tree.
    """

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    max_sum = float('-inf')

    def dfs(node, parent):
        nonlocal max_sum

        best_down_1 = 0
        best_down_2 = 0

        for nei in graph[node]:
            if nei == parent:
                continue

            down = dfs(nei, node)

            # Keep two highest downward paths
            if down > best_down_1:
                best_down_2 = best_down_1
                best_down_1 = down
            elif down > best_down_2:
                best_down_2 = down

        # Max path passing through node
        max_sum = max(max_sum, values[node] + best_down_1 + best_down_2)

        # Return best downward path
        return values[node] + best_down_1

    dfs(0, -1)
    return max_sum
