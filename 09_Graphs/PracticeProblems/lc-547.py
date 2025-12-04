# ✅ LeetCode 547 — Number of Provinces
# 🔍 Problem Summary

# You are given an n x n matrix isConnected, where:

# isConnected[i][j] = 1 → city i and city j are directly connected

# isConnected[i][j] = 0 → no direct connection

# A province is a group of cities directly or indirectly connected.

# You must return how many connected components exist.

# ✅ Approach

# This is simply the number of connected components in an undirected graph, represented using an adjacency matrix.

# We can solve it using:

# ✔ Depth-First Search (DFS)

# Treat each row/column as a node

# Explore all reachable nodes

# Count how many times DFS starts → number of provinces

# Time Complexity: O(n²)
# Space Complexity: O(n)

# 🧩 Explanation Summary

# Loop through every city.

# If it's not visited, start DFS.

# DFS explores all cities connected directly or indirectly.

# After DFS completes, we found one full province.

# Count it and continue.
class Solution:
    def findCircleNum(self, isConnected):
        # Number of cities
        n = len(isConnected)

        # A set to keep track of visited cities
        visited = set()

        # DFS function to explore all cities connected to 'city'
        def dfs(city):
            # Mark the current city as visited
            visited.add(city)

            # Loop through all possible neighboring cities
            for neighbor in range(n):
                # Check if there's a connection AND the neighbor is not visited
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    # Recursively explore the connected neighbor
                    dfs(neighbor)

        # Count of total provinces (connected components)
        provinces = 0

        # Iterate through every city
        for city in range(n):
            # If the city is not visited, it starts a new province
            if city not in visited:
                dfs(city)          # Explore the full connected region
                provinces += 1     # Increment province count

        # Return total provinces found
        return provinces
