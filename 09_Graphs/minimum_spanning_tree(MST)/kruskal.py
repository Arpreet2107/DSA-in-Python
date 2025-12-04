# 6️⃣ Kruskal's Algorithm
# Definition & Core Purpose

# Definition: Greedy algorithm that builds MST by sorting all edges by weight and adding them in ascending order if they don’t create a cycle (checked via Union-Find).
# Purpose: Natural MST algorithm especially when edges are easily sortable (edge list available).

# Mechanism

# Sort edges by weight.

# Iterate edges; add edge if it connects two different components (Union-Find check).

# Stop when V-1 edges added.
# Advantages

# Very simple conceptually; works well when graph represented as edge list.

# Efficient: sorting dominates 

# O(ElogE) (≈ O(ElogV)).

# Union-Find is fast (amortized inverse-Ackermann).

# Limitations

# Requires sorting all edges — heavy if edges huge but unavoidable for Kruskal.

# Needs union-find data structure.
def kruskal(nodes, edges):
    # nodes: iterable of nodes
    # edges: list of tuples (u, v, w) for undirected graph
    parent = {}                                      # parent map for union-find
    rank = {}                                        # rank map for union-find (for union by rank)

    # initialize union-find sets
    for node in nodes:                               # for each node
        parent[node] = node                          # set parent to itself
        rank[node] = 0                               # initial rank zero

    def find(x):                                     # find with path compression
        if parent[x] != x:                           # if x is not its own parent
            parent[x] = find(parent[x])              # recursively find root and compress path
        return parent[x]                             # return representative

    def union(x, y):                                 # union by rank
        rx, ry = find(x), find(y)                    # find roots of x and y
        if rx == ry:                                 # already in same set
            return False                             # union did not happen (would form cycle)
        if rank[rx] < rank[ry]:                      # attach smaller rank under larger rank
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx                          # choose one root
            rank[rx] += 1                            # increment rank if equal
        return True                                  # union successful

    # sort edges by weight ascending
    edges_sorted = sorted(edges, key=lambda e: e[2])  # sort by weight
    mst = []                                         # list to collect MST edges

    for u, v, w in edges_sorted:                      # iterate sorted edges
        if union(u, v):                               # if union succeeds, edge connects different components
            mst.append((u, v, w))                     # include edge in MST
        if len(mst) == len(parent) - 1:               # if we already have V-1 edges, MST is complete
            break

    return mst                                        # return the list of edges in MST
