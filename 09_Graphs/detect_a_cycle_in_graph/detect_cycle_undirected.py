# ⭐ A. Detect Cycle in Undirected Graph (Using DFS)
# ⭐ Mechanism

# Visit nodes using DFS

# Track the node from which you came (parent)

# If you encounter a previously visited node that is not the parent → Cycle Exists
def detect_cycle_undirected(graph):
    visited = set()

    def dfs(node, parent):
        # Mark current node as visited
        visited.add(node)

        # Check all adjacent nodes
        for neighbor in graph[node]:
            if neighbor not in visited:
                # Recur for unvisited neighbor
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                # Found a cycle (visited neighbor ≠ parent)
                return True

        return False

    # Check all components
    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True

    return False