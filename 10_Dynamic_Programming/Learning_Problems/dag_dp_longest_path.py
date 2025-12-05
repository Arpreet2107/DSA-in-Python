# ✅ 45. DAG DP (Topological Order + DP)

# Classic longest path in a DAG.

# Steps:

# 1️⃣ Build graph
# 2️⃣ Compute indegree
# 3️⃣ Topological order (Kahn)
# 4️⃣ DP along topo order
from collections import defaultdict, deque

def dag_dp_longest_path(n, edges):
    """
    Longest path in DAG using topological sort + DP.
    """

    graph = defaultdict(list)
    indegree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    # Topological order
    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for nei in graph[u]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    # DP array
    dp = [0] * n

    for u in topo:
        for v in graph[u]:
            dp[v] = max(dp[v], dp[u] + 1)

    return max(dp)
