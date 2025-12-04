# ⭐ 2. BREADTH-FIRST SEARCH (BFS)
# ✅ Definition

# BFS is a graph traversal technique that explores nodes level by level starting from a given source node.

# It uses a queue (FIFO) to store nodes to be visited.

# 🎯 Purpose

# BFS is mainly used for:

# Finding shortest path in an unweighted graph

# Checking graph connectivity

# Level-order traversal

# Detecting cycles in undirected graphs

# Solving problems like flooding, minimum moves, bipartite check
# 🌟 Advantages

# Finds shortest path in unweighted graphs

# Guaranteed to visit nodes closest to the start first

# Detects connected components

# Good for level-by-level exploration

# ⚠️ Limitations

# Requires more memory than DFS (queue usage)

# Not suitable for deep graphs

# Slow for very dense graphs
from collections import deque

def bfs(graph, start):
    # Create a queue for BFS
    queue = deque()
    
    # Add starting node to the queue
    queue.append(start)
    
    # Keep track of visited nodes
    visited = set()
    visited.add(start)

    # BFS works until queue becomes empty
    while queue:
        # Remove the front node from queue
        node = queue.popleft()
        
        # Print or process the visited node
        print(node, end=" ")

        # Explore all neighbors of current node
        for neighbor in graph[node]:
            # Visit only unvisited nodes
            if neighbor not in visited:
                visited.add(neighbor)   # Mark neighbor as visited
                queue.append(neighbor)  # Add to queue for future exploration
