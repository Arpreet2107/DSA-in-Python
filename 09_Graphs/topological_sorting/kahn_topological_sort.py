# 8️⃣ Kahn's Algorithm (for topological sort)
# Definition & Core Purpose

# Definition: Kahn’s algorithm is a BFS-like algorithm for topological ordering. It repeatedly removes nodes of in-degree 0 and appends them to the ordering, updating in-degrees.
# Purpose: Efficient method to produce a topological order and detect cycles (if not all nodes get output).

# Mechanism

# Compute in-degree for all nodes.

# Initialize queue with nodes having in-degree 0.

# Pop node, append to order, reduce in-degree of neighbors; if any neighbor becomes 0, enqueue it.

# If produced order contains all nodes → DAG; else cycle exists.
# Advantages

# Simple and intuitive.

# Detects cycles (if not all vertices are included).

# Linear time: O(V+E).

# Limitations

# Requires computing in-degree (easy).

# Only works on DAGs — will report cycle otherwise.
from collections import deque                          # import deque for efficient queue

def kahn_topological_sort(adj):
    # adj: dict node -> list of neighbors (directed edges from node to neighbors)
    indeg = {node: 0 for node in adj}                  # initialize in-degree map to zero
    for u in adj:                                      # compute in-degrees
        for v in adj[u]:                               # for each neighbor v of u
            indeg[v] = indeg.get(v, 0) + 1             # increment in-degree of v

    q = deque()                                        # queue to hold nodes with indegree 0
    for node in indeg:                                 # enqueue initial zero in-degree nodes
        if indeg[node] == 0:
            q.append(node)

    topo_order = []                                    # list to store topological ordering
    while q:                                           # process until queue empty
        u = q.popleft()                                # pop leftmost node
        topo_order.append(u)                           # append node to ordering
        for v in adj.get(u, []):                       # traverse neighbors of u
            indeg[v] -= 1                              # decrement in-degree of neighbor
            if indeg[v] == 0:                          # if neighbor now has zero in-degree
                q.append(v)                            # enqueue neighbor

    if len(topo_order) != len(indeg):                  # if ordering doesn't include all nodes
        return None                                    # cycle exists; no topological order
    return topo_order                                  # otherwise return topological ordering
