# # 📌 9️⃣ DAG Shortest Path Algorithm
# # Definition & Purpose

# # For Directed Acyclic Graphs, shortest paths are easy because no cycles exist.

# # Mechanism

# # Perform Topological Sort

# # Relax edges in topo order

# # Runs in: O(V + E)
# Advantages

# ✔ Fastest for DAGs
# ✔ Works for negative weights
# ✔ Very clean algorithm

# Limitations

# ❌ Only works for DAGs
# ❌ Not applicable to general graphs
def topo_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neigh, _ in graph[node]:
            if neigh not in visited:
                dfs(neigh)
        stack.append(node)

    for v in graph:
        if v not in visited:
            dfs(v)

    return stack[::-1]  # Return reversed stack


def dag_shortest_path(graph, source):
    order = topo_sort(graph)

    # Initialize distances
    dist = {v: float('inf') for v in graph}
    dist[source] = 0

    # Relax edges in topological order
    for u in order:
        if dist[u] != float('inf'):
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    return dist
