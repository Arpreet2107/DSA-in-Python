# ✅ 40B. TREE DP — RE-ROOTING (All Nodes Sum of Distances)

# Classic “tree re-rooting”:
# Compute DP for root = 1, then recompute for every other root using parent’s DP.

# Goal:
# For every node, compute sum of distances to all other nodes.

# Steps:

# First DFS → compute subtree sizes + distances from root

# Second DFS → re-root and compute answer for each node
from collections import defaultdict

def sumOfDistancesInTree(n, edges):
    """
    Re-rooting DP:
    ans[u] = sum of distances from node u to all others.

    Step 1: Post-order -> compute subtree sizes + dist sum for root
    Step 2: Pre-order -> rerooting DP to compute for all nodes
    """

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    size = [1] * n        # size[u] = size of subtree
    dp = [0] * n          # dp[u] = sum of distances from u to subtree nodes
    ans = [0] * n

    # First DFS: compute dp[0] + subtree sizes
    def dfs1(u, parent):
        for v in graph[u]:
            if v != parent:
                dfs1(v, u)
                size[u] += size[v]
                dp[u] += dp[v] + size[v]

    # Second DFS: reroot
    def dfs2(u, parent):
        ans[u] = dp[u]
        for v in graph[u]:
            if v != parent:

                # Save original values
                pu, pv = dp[u], dp[v]
                su, sv = size[u], size[v]

                # Remove v subtree effect from u
                dp[u] -= dp[v] + size[v]
                size[u] -= size[v]

                # Add u (as parent) effect into v
                dp[v] += dp[u] + size[u]
                size[v] += size[u]

                dfs2(v, u)

                # Restore (backtracking)
                dp[u], dp[v] = pu, pv
                size[u], size[v] = su, sv

    dfs1(0, -1)
    dfs2(0, -1)

    return ans
