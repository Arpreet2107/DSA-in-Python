# 📌 5️⃣ Johnson’s Algorithm (All-Pairs Shortest Path)
# Definition & Purpose

# Johnson’s Algorithm finds all-pairs shortest paths (APSP) in a weighted graph (including negative weights).
# It is much faster than Floyd–Warshall when the graph is sparse.

# Core Idea & Mechanism

# Johnson’s algorithm uses:

# Bellman–Ford

# Detects negative cycles

# Computes potential values: h(v) for every vertex

# Reweighting edges

# New weight:

# 𝑤′(𝑢,𝑣)=𝑤(𝑢,𝑣)+ℎ(𝑢)−ℎ(v)

# Ensures all edges become non-negative

# Run Dijkstra from every vertex
# Advantages

# ✔ Works with negative weights
# ✔ Very efficient for sparse graphs
# ✔ Faster than Floyd–Warshall for most real-world graphs

# Limitations

# ❌ Cannot work with negative weight cycles
# ❌ More complex than Floyd–Warshall
import heapq

def bellman_ford(graph, source, V):
    # Initialize distances with infinity
    dist = {v: float('inf') for v in graph}
    dist[source] = 0

    # Relax edges V-1 times
    for _ in range(V - 1):
        for u in graph:
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    # Detect negative weight cycle
    for u in graph:
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                return None  # Negative cycle found

    return dist


def dijkstra(graph, source):
    pq = [(0, source)]
    dist = {v: float('inf') for v in graph}
    dist[source] = 0

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist


def johnsons_algorithm(graph):
    V = len(graph)

    # Step 1: Add a dummy node Q
    graph['Q'] = [(v, 0) for v in graph if v != 'Q']

    # Step 2: Run Bellman-Ford from Q
    h = bellman_ford(graph, 'Q', V + 1)
    if h is None:
        raise Exception("Negative cycle detected. Johnson's algorithm cannot proceed.")

    # Remove dummy node
    del graph['Q']

    # Step 3: Reweight edges
    new_graph = {}
    for u in graph:
        new_graph[u] = []
        for v, w in graph[u]:
            new_w = w + h[u] - h[v]
            new_graph[u].append((v, new_w))

    # Step 4: Run Dijkstra from every vertex
    all_pairs = {}
    for u in new_graph:
        dist = dijkstra(new_graph, u)

        # Convert distances back to original weights
        for v in dist:
            dist[v] = dist[v] - h[u] + h[v]

        all_pairs[u] = dist

    return all_pairs
