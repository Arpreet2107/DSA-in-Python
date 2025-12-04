# # 📌 7️⃣ Dial’s Algorithm
# # Definition & Purpose

# # Dial’s Algorithm solves shortest paths faster when:

# # Edge weights are non-negative integers

# # The maximum weight is small (e.g., ≤ 20)

# # Uses bucket arrays instead of priority queues.
# Advantages

# ✔ O(V + E) — faster than Dijkstra
# ✔ Perfect for integer-weight graphs
# ✔ Easy bucket-based design

# Limitations

# ❌ Only works for non-negative integer weights
# ❌ Large max-weight → too many buckets
from collections import deque

def dials_algorithm(graph, source, max_weight):
    # Number of buckets needed
    buckets = [deque() for _ in range(max_weight * len(graph) + 1)]

    # Initialize distances
    dist = {v: float('inf') for v in graph}
    dist[source] = 0

    # Put source into bucket 0
    buckets[0].append(source)

    # Current bucket index
    idx = 0

    while idx < len(buckets):
        # If current bucket empty → move to next
        if not buckets[idx]:
            idx += 1
            continue

        # Get a node
        u = buckets[idx].popleft()

        # Explore neighbors
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                old_dist = dist[v]
                dist[v] = dist[u] + w

                # Add to appropriate bucket
                buckets[dist[v]].append(v)

        idx += 0  # Stay on same bucket until empty

    return dist
