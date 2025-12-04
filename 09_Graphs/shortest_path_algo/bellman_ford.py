# Bellman-Ford
# Definition & Purpose

# Definition: Bellman-Ford computes single-source shortest paths even when edges can be negative; it detects negative cycles reachable from the source.
# Purpose: Use when negative edge weights exist or you need negative cycle detection.

# Mechanism

# Relax all edges 
# 𝑉
# −
# 1
# V−1 times (where V = number of vertices).

# If any edge can be relaxed further in the Vth pass → negative cycle exists.
# Advantages

# Handles negative weights.

# Detects negative cycles.

# Limitations

# Slower: 
# 𝑂(𝑉𝐸)
# Not suitable for large graphs when performance matters.
def bellman_ford(nodes, edges, source):
    # nodes: iterable of all nodes in the graph
    # edges: list of tuples (u, v, w) representing directed edge u->v with weight w
    # source: start node
    dist = {node: float('inf') for node in nodes}   # initialize distances to infinity
    dist[source] = 0                                 # distance to source is 0
    prev = {node: None for node in nodes}            # predecessor dict for path reconstruction

    for _ in range(len(nodes) - 1):                  # repeat V-1 times
        updated = False                              # track if any relaxation happened
        for u, v, w in edges:                        # iterate all edges
            if dist[u] != float('inf') and dist[u] + w < dist[v]:  # check relaxation condition
                dist[v] = dist[u] + w                # update distance for v
                prev[v] = u                          # update predecessor
                updated = True                       # mark that we updated at least once
        if not updated:                              # if no updates in this pass
            break                                    # distances have converged early

    # check for negative-weight cycles
    for u, v, w in edges:                            # one more pass to detect cycles
        if dist[u] != float('inf') and dist[u] + w < dist[v]:  # if relax still possible
            return None, None                         # negative cycle detected; return None to indicate failure

    return dist, prev                                 # no negative cycles; return results
