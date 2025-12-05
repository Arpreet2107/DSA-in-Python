# ✅ 52. Shortest Path in DAG (DP on DAG using Topological Order)
# Shortest Path in Directed Acyclic Graph (DAG)
from collections import defaultdict, deque

def shortest_path_DAG(n, edges, src):
    """
    n     = number of nodes (0 to n-1)
    edges = list of (u, v, w)
    src   = start node
    """

    graph = defaultdict(list)
    indegree = [0] * n

    # Build adjacency list
    for u, v, w in edges:
        graph[u].append((v, w))
        indegree[v] += 1

    # Topological sort
    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v, w in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    # DP Array → distance from src
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0

    # Relax edges in topological order
    for u in topo:
        if dist[u] != INF:
            for v, w in graph[u]:
                dist[v] = min(dist[v], dist[u] + w)

    return dist

# Example
edges = [(0,1,2),(0,2,3),(1,3,4),(2,3,1)]
print(shortest_path_DAG(4, edges, 0))
