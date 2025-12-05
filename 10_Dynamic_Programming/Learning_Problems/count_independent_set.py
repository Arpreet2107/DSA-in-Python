# ✅ 43. COUNT OF INDEPENDENT SET IN TREE (TREE DP)

# An Independent Set:
# No two adjacent nodes are chosen.

# DP State

# dp[node][0] = ways when node is not chosen
# dp[node][1] = ways when node is chosen

# Transitions:

# If chosen → children cannot be chosen

# If not chosen → children can be chosen or not
from collections import defaultdict
MOD = 10**9 + 7

def count_independent_set(n, edges):
    """
    Count independent sets in a tree.
    """

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    dp = [[0, 0] for _ in range(n)]

    def dfs(node, parent):
        dp[node][0] = 1  # not chosen
        dp[node][1] = 1  # chosen

        for nei in graph[node]:
            if nei == parent:
                continue

            dfs(nei, node)

            # not chosen → child can be chosen or not
            dp[node][0] = (dp[node][0] * (dp[nei][0] + dp[nei][1])) % MOD

            # chosen → child cannot be chosen
            dp[node][1] = (dp[node][1] * dp[nei][0]) % MOD

    dfs(0, -1)

    # Either chosen or not at root
    return (dp[0][0] + dp[0][1]) % MOD
