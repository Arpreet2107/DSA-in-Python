# 5️⃣ Prim's Algorithm
# Definition & Purpose

# Definition: Greedy algorithm building an MST by starting from an arbitrary node and repeatedly adding the cheapest edge that connects the growing tree to a new vertex.
# Purpose: Efficient MST for graphs; works well with adjacency lists + priority queue.

# Mechanism

# Start with any node in MST-set.

# Use a min-heap keyed by edge weight to pick smallest outgoing edge to the outside set.

# Add chosen node and update candidate edges.
# Advantages

# Efficient: 
# O(ElogV) with heap.

# Good for dense and sparse graphs; starting node flexible.

# Limitations

# Needs connectivity (graph must be connected).

# Greedy choice is local; though for MST it's correct, still limited to tree generation (not suitable for other global constraints).
import heapq                                      # import heapq for priority queue

def prim(adj, start):
    # adj: dict node -> list of (neighbor, weight) pairs
    # start: starting node for MST
    mst_edges = []                                  # list to store edges included in MST
    visited = set()                                 # set of nodes already included in MST
    heap = []                                       # min-heap of candidate edges (weight, from, to)
    visited.add(start)                              # include start node
    # push all edges from start into heap
    for v, w in adj[start]:                          # iterate neighbors of start
        heapq.heappush(heap, (w, start, v))          # push tuple (weight, u, v)

    while heap and len(visited) < len(adj):         # continue until MST spans all nodes
        w, u, v = heapq.heappop(heap)                # pop smallest edge
        if v in visited:                             # if target already in MST skip
            continue                                  # skip and continue
        visited.add(v)                               # add new node to MST
        mst_edges.append((u, v, w))                  # record edge in MST
        for to, wt in adj[v]:                         # add new candidate edges from v
            if to not in visited:                     # only for nodes not yet visited
                heapq.heappush(heap, (wt, v, to))     # push candidate edge

    return mst_edges                                 # return list of MST edges
