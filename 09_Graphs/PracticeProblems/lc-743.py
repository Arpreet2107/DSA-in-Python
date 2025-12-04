# ✅ LeetCode 743: Network Delay Time — Python Solution (Fully Explained)
# Problem Summary

# You are given a list of travel times as directed edges in a graph:
# t = [u, v, w] meaning from node u to node v it takes w time.

# You must find how long it takes for all nodes to receive the signal that starts from node k.

# If some node cannot be reached → return -1.

# This is a classic single-source shortest path problem → Dijkstra’s Algorithm.

# 🔍 Explanation
# 1️⃣ Build Graph

# We convert times into adjacency list for easier traversal.

# 2️⃣ Use Dijkstra’s Algorithm

# A min-heap always picks the next node with the shortest distance.

# Once a node’s shortest path is fixed, we store it in dist.

# 3️⃣ Final Answer

# If some node was never reached → return -1

# Otherwise → return the maximum time among all shortest times.
# ⏱️ Time Complexity
# O(E log V)


# Because each edge is processed once and heap operations cost log V.

# 💾 Space Complexity
# O(V + E)

import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        # Create adjacency list for graph:
        # graph[u] = list of (v, w) meaning u -> v with cost w
        graph = {i: [] for i in range(1, n + 1)}

        # Fill adjacency list with edges
        for u, v, w in times:
            graph[u].append((v, w))

        # Min-heap (priority queue) for Dijkstra
        # Stores (current_distance, node)
        min_heap = [(0, k)]

        # Dictionary to store the shortest known time to reach each node
        dist = {}

        # Run Dijkstra’s algorithm
        while min_heap:
            # Pop the node with the smallest current distance
            time, node = heapq.heappop(min_heap)

            # If we already visited this node, skip
            if node in dist:
                continue

            # Record the shortest time to reach this node
            dist[node] = time

            # Explore neighbors
            for nei, wt in graph[node]:
                # If neighbor not visited, push new cost to heap
                if nei not in dist:
                    heapq.heappush(min_heap, (time + wt, nei))

        # If not all nodes were reached, return -1
        if len(dist) != n:
            return -1

        # The answer is the maximum time among all shortest times
        return max(dist.values())
