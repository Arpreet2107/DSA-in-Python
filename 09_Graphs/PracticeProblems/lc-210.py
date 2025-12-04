# 🎓 LeetCode 210 — Course Schedule II
# Problem Summary

# You are given:

# numCourses = number of courses labeled 0..n-1

# prerequisites list of pairs [a, b] meaning:
# to take course a, you must first complete b

# You must:
# ➡️ Return any valid topological ordering of courses
# ➡️ If no valid ordering exists (cycle present), return []

# ✔️ This is a direct application of Kahn’s Algorithm for topological sorting.
# 🔍 Step-by-Step Explanation
# 1️⃣ Build Graph

# For each prerequisite [a, b], create edge:

# b → a


# Meaning: before taking a, you must first take b.

# 2️⃣ Track In-Degree

# in_degree[a] counts how many prerequisites course a needs.

# 3️⃣ Start with In-Degree 0

# Courses with no prerequisites can be taken immediately.

# 4️⃣ BFS / Kahn’s Algorithm

# Pop a 0-in-degree course

# Add it to the result

# Reduce in-degree of neighbors

# Add newly zero-in-degree neighbors to the queue

# 5️⃣ Cycle Check

# If the result list does NOT contain all courses → cycle exists → return [].

# ⏱️ Time Complexity
# O(V + E)


# (V = numCourses, E = prerequisites)

# 💾 Space Complexity
# O(V + E)
from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        # Step 1: Build the adjacency list for the graph
        # graph[b] = list of courses that depend on b
        graph = {i: [] for i in range(numCourses)}
        
        # Step 2: Build in-degree array
        # in_degree[i] = number of prerequisites for course i
        in_degree = [0] * numCourses

        # Fill adjacency list and in-degree counts
        for course, prereq in prerequisites:
            graph[prereq].append(course)  # Directed edge: prereq -> course
            in_degree[course] += 1        # course has one more prerequisite
        
        # Step 3: Initialize queue with all courses having 0 in-degree
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        # List to store valid topological order
        topo_order = []

        # Step 4: Kahn's Algorithm (BFS style)
        while queue:
            curr = queue.popleft()  # Take a course with no prerequisites
            topo_order.append(curr)

            # Reduce in-degree of all dependent courses
            for neighbor in graph[curr]:
                in_degree[neighbor] -= 1

                # If a dependent course now has no prerequisites, push to queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 5: If we processed all courses, return topo order
        if len(topo_order) == numCourses:
            return topo_order

        # Otherwise, cycle exists → return empty list
        return []
