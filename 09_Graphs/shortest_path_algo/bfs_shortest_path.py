# 📌 8️⃣ BFS as a Shortest Path Algorithm (for unweighted graphs)
# Definition & Purpose

# If every edge has equal weight, the shortest path is simply the path with the fewest edges → BFS solves this efficiently.
# Advantages

# ✔ Fastest: O(V + E)
# ✔ Works for all unweighted graphs
# ✔ Very simple

# Limitations

# ❌ Only for equal-weight edges
# ❌ Cannot handle weighted graphs
from collections import deque

def bfs_shortest_path(graph, start):
    # Queue for BFS
    q = deque([start])

    # Distance dictionary
    dist = {start: 0}

    while q:
        node = q.popleft()

        for neigh in graph[node]:
            if neigh not in dist:
                dist[neigh] = dist[node] + 1  # Each edge = 1 weight
                q.append(neigh)

    return dist
