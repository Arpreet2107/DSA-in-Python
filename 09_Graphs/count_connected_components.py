# ⭐ 5. COUNT NUMBER OF CONNECTED COMPONENTS
# ✅ Definition

# A connected component is a group of nodes where every node is reachable from any other node within the same group.

# Example:
# If the graph has components:

# Component 1 → A, B, C

# Component 2 → D, E

# Then number of connected components = 2
# 🌟 Advantages

# Helps determine graph structure

# Useful in network clustering, region detection

# Used to check if graph is fully connected

# ⚠️ Limitations

# Expensive for large graphs

# Requires full traversal
def count_connected_components(graph):
    visited = set()
    count = 0

    # Helper DFS function
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    # Check every node in graph
    for node in graph:
        if node not in visited:
            count += 1            # New component found
            dfs(node)            # Explore the entire component

    return count

