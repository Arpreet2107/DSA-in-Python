# ⭐ B. Detect Cycle in Directed Graph (Using DFS + Recursion Stack)
# ⭐ Advantages

# Essential for preventing deadlocks

# Detects infinite loops

# Fundamental in topological sorting

# ⚠️ Limitations

# Recursive DFS can overflow

# Harder for large directed graphs
def detect_cycle_directed(graph):
    visited = set()
    recursion_stack = set()

    def dfs(node):
        visited.add(node)
        recursion_stack.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in recursion_stack:
                # Found cycle in directed graph
                return True

        recursion_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False

