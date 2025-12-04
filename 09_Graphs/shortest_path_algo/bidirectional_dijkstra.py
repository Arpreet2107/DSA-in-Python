# 📌 6️⃣ Bidirectional Dijkstra Algorithm
# Definition & Purpose

# Instead of running Dijkstra from the source to destination, this algorithm runs:

# One Dijkstra from source → forward

# Another from goal → backward

# They meet in the middle → reducing search space.
# Advantages

# ✔ Much faster than normal Dijkstra
# ✔ Reduced search space
# ✔ Good for large road networks

# Limitations

# ❌ More code complexity
# ❌ Only works for non-negative weights

import heapq

def bidirectional_dijkstra(graph, start, goal):

    # Forward search PQ
    f_pq = [(0, start)]
    # Backward search PQ
    b_pq = [(0, goal)]

    # Distance maps for forward & backward
    f_dist = {start: 0}
    b_dist = {goal: 0}

    # Visited sets
    f_visited = set()
    b_visited = set()

    # Best answer seen so far
    best = float('inf')

    while f_pq and b_pq:

        # ---------- Forward Search ----------
        f_cost, f_node = heapq.heappop(f_pq)
        if f_node in f_visited:
            continue
        f_visited.add(f_node)

        if f_node in b_visited:
            best = min(best, f_dist[f_node] + b_dist[f_node])

        for neigh, w in graph[f_node]:
            new_cost = f_dist[f_node] + w
            if neigh not in f_dist or new_cost < f_dist[neigh]:
                f_dist[neigh] = new_cost
                heapq.heappush(f_pq, (new_cost, neigh))

        # ---------- Backward Search ----------
        b_cost, b_node = heapq.heappop(b_pq)
        if b_node in b_visited:
            continue
        b_visited.add(b_node)

        if b_node in f_visited:
            best = min(best, b_dist[b_node] + f_dist[b_node])

        for neigh, w in graph[b_node]:
            new_cost = b_dist[b_node] + w
            if neigh not in b_dist or new_cost < b_dist[neigh]:
                b_dist[neigh] = new_cost
                heapq.heappush(b_pq, (new_cost, neigh))

        # Stop when frontiers meet
        if best < float('inf'):
            return best

    return best
