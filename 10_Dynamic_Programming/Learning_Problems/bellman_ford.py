
# ✅ 46. Bellman-Ford (DP on Edges)
# Bellman-Ford Algorithm → Detects Negative Cycles + Shortest Paths
def bellman_ford(n, edges, src):
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0

    # Relax all edges n-1 times
    for _ in range(n-1):
        updated = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break

    # Detect negative cycle
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return "Negative Cycle Detected"

    return dist

# Example
edges = [(0,1,5),(1,2,-2),(2,3,3),(3,1,1)]
print(bellman_ford(4, edges, 0))
