# ✅ 41. TREE DIAMETER (Longest Distance Between Any Two Nodes)

# We use Two DFS method:

# 1️⃣ DFS from any node → find farthest node A
# 2️⃣ DFS from A → farthest node B
# Distance (A,B) = diameter
from collections import defaultdict, deque

def tree_diameter(n, edges):
    """
    Compute diameter of a tree using 2 DFS.
    """

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def bfs(start):
        """
        Returns (farthest_node, distance_to_that_node)
        """
        visited = {start}
        q = deque([(start, 0)])
        far_node, far_dist = start, 0

        while q:
            node, dist = q.popleft()
            if dist > far_dist:
                far_dist = dist
                far_node = node

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, dist + 1))

        return far_node, far_dist

    # First BFS → find one endpoint of diameter
    a, _ = bfs(0)
    # Second BFS → find actual diameter
    b, diameter = bfs(a)

    return diameter
