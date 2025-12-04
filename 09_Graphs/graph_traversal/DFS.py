# ⭐ 3. DEPTH-FIRST SEARCH (DFS)
# ✅ Definition

# DFS is a traversal technique that explores as deep as possible before backtracking.

# Uses a stack (explicitly) or recursion (implicitly).

# 🎯 Purpose

# DFS is used for:

# Detecting cycles

# Finding connected components

# Topological sorting

# Solving puzzles (mazes, backtracking)

# Pathfinding in decision trees
# 🌟 Advantages

# Uses less memory than BFS in many cases

# Works well for deep exploring

# Best for cycle detection

# Simple implementation

# ⚠️ Limitations

# May get stuck in deep recursion (stack overflow)

# Does NOT guarantee shortest path

# Difficult in very large graphs
# ✅ Recursive DFS
def dfs_recursive(graph, node, visited=None):
    # Initialize visited set if not provided
    if visited is None:
        visited = set()

    # Mark the current node as visited
    visited.add(node)
    print(node, end=" ")

    # Explore all unvisited neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


# ✅ Iterative DFS (using stack)
def dfs_iterative(graph, start):
    # Create an explicit stack
    stack = [start]
    
    # Visited set to track visited nodes
    visited = set()

    while stack:
        # Pop last added node
        node = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            # Add neighbors to stack (LIFO)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)