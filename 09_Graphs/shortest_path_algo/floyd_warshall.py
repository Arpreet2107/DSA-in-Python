# Floyd-Warshall
# Definition & Purpose

# Definition: Floyd-Warshall computes all-pairs shortest paths (APSP) using dynamic programming; works with negative weights but not with negative cycles.
# Purpose: APSP when you need distances between every pair of nodes.

# Mechanism

# Iterative DP: for each intermediate k, update dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]).
# Advantages

# Simple to implement; returns APSP.

# Handles negative weights (but not negative cycles).

# Limitations

# 𝑂(𝑛^3)time, memory 𝑂(𝑛^2) — expensive for large n.
def floyd_warshall(nodes, edges):
    # nodes: list of nodes (indexable)
    # edges: list of tuples (u, v, w)
    n = len(nodes)                                   # number of nodes
    index = {node: i for i, node in enumerate(nodes)}# map node -> index
    # initialize distance matrix with infinities
    dist = [[float('inf')] * n for _ in range(n)]    # n x n matrix of infinities
    for i in range(n):                               # distance from node to itself is 0
        dist[i][i] = 0                               # set diagonal to zero

    for u, v, w in edges:                            # fill initial distances from edges
        i, j = index[u], index[v]                    # convert nodes to indices
        dist[i][j] = min(dist[i][j], w)              # set edge weight (handle multiple edges)

    # main triple loop
    for k in range(n):                               # for each intermediate node k
        for i in range(n):                           # for each source node i
            for j in range(n):                       # for each destination node j
                # check if going through k gives shorter path i->j
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]  # update with shorter path

    return dist                                      # return the matrix of shortest distances
