# 2️⃣ Dijkstra's Algorithm
# Definition & Core Purpose

# Definition: Dijkstra finds shortest path distances from a single source to all vertices in a graph with nonnegative edge weights.
# Core purpose: Efficient SSSP for nonnegative weights; often used in road/network routing.

# Principle / Mechanism

# Maintain a priority queue (min-heap) of candidate nodes keyed by current best distance.

# Repeatedly pick node with smallest tentative distance, relax its outgoing edges, and update neighbors.

# Once a node is popped from the heap the first time, its shortest distance is final.
# Advantages

# Efficient: 
# 𝑂((𝑉+𝐸)log⁡𝑉) 
# O((V+E)logV) with binary heap and adjacency lists.

# Works well for sparse graphs.

# Produces shortest path tree and distances.

# Limitations

# Cannot handle negative edge weights.

# Performance depends on heap implementation — Fibonacci heap gives better theoretical bounds but heavier in practice.
import heapq                                      # import heapq for min-heap operations

def dijkstra(adj, source):
    # adj: dict mapping node -> list of (neighbor, weight) pairs
    # source: starting node
    dist = {}                                      # dictionary to store shortest known distances
    for node in adj:                               # initialize distances to infinity for all nodes
        dist[node] = float('inf')                  # assign infinity initially
    dist[source] = 0                               # distance to source is 0
    prev = {node: None for node in adj}            # predecessor dictionary for path reconstruction
    heap = []                                      # initialize empty heap list
    heapq.heappush(heap, (0, source))              # push tuple (distance, node) for the source
    visited = set()                                # visited set to avoid reprocessing finalized nodes

    while heap:                                    # loop until there are no candidate nodes
        d, u = heapq.heappop(heap)                 # pop node with smallest tentative distance
        if u in visited:                           # skip if node already finalized
            continue                                # continue to next iteration
        visited.add(u)                             # mark node as finalized
        for v, weight in adj[u]:                    # iterate over neighbors and edge weights
            alt = d + weight                       # compute alternative path distance via u
            if alt < dist[v]:                      # if found shorter path to neighbor
                dist[v] = alt                      # update shortest distance
                prev[v] = u                        # update predecessor for v
                heapq.heappush(heap, (alt, v))     # push updated tentative distance to heap

    return dist, prev                               # return distances and predecessors for path recovery
