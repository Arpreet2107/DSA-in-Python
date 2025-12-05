# ✅ 44. LCA-BASED DP (Binary Lifting + Distance Queries)

# We compute:

# parent[k][u] = 2ᵏ-th ancestor

# depth[u]

# LCA(a,b) in O(logN)
from collections import defaultdict
import math

def build_lca(n, edges):
    """
    Preprocess tree for LCA using Binary Lifting.
    """

    LOG = math.ceil(math.log2(n))
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    parent = [[-1] * n for _ in range(LOG)]
    depth = [0] * n

    def dfs(root=0):
        stack = [(root, -1)]
        while stack:
            u, p = stack.pop()
            parent[0][u] = p
            for v in graph[u]:
                if v != p:
                    depth[v] = depth[u] + 1
                    stack.append((v, u))

    dfs()

    # Precompute ancestors
    for k in range(1, LOG):
        for v in range(n):
            if parent[k-1][v] != -1:
                parent[k][v] = parent[k-1][parent[k-1][v]]

    def lca(a, b):
        """Return LCA of nodes a and b."""
        if depth[a] < depth[b]:
            a, b = b, a

        # Lift a up
        diff = depth[a] - depth[b]
        for k in range(LOG):
            if diff & (1 << k):
                a = parent[k][a]

        if a == b:
            return a

        # Jump both up until parents differ
        for k in reversed(range(LOG)):
            if parent[k][a] != parent[k][b]:
                a = parent[k][a]
                b = parent[k][b]

        return parent[0][a]

    return lca, depth, parent
