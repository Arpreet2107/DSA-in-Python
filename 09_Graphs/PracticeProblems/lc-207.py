# 🎓 LeetCode 207 — Course Schedule
# Problem Summary

# You're given:

# numCourses = number of courses labeled 0..n-1

# prerequisites = list of edges [a, b] meaning:
# to take course a, you must first complete course b

# ➡️ Determine if it's possible to finish all courses
# ➡️ This is the same as checking if the directed graph has a cycle

# 🧠 Best Solution: Kahn’s Algorithm (Topological Sorting)

# If a cycle exists → you cannot complete all courses.

# If you can produce a topological ordering → all courses can be taken.
# 🔍 Explanation of the Logic
# 1️⃣ Build Graph

# Each prerequisite defines a directed edge:
# prereq → course

# 2️⃣ Track In-Degree

# in_degree[i] = number of prerequisites course i still needs.

# 3️⃣ Start with In-Degree 0 Nodes

# These courses can be taken immediately.

# 4️⃣ BFS Processing

# Remove a course

# Decrease the in-degree of neighbors

# When a neighbor becomes 0 in-degree → add it to queue

# 5️⃣ Detect Cycle

# If not all courses are processed → the graph has a cycle.

# ⏱️ Time Complexity
# O(V + E)


# because we visit all courses and all prerequisite edges.

# 💾 Space Complexity
# O(V + E)


# for graph + queue + in-degree list.
from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Step 1: Build adjacency list graph
        graph = {i: [] for i in range(numCourses)}
        
        # Step 2: Build in-degree array
        # in_degree[i] = number of prerequisites for course i
        in_degree = [0] * numCourses
        
        # Fill graph and in-degree
        for course, prereq in prerequisites:
            graph[prereq].append(course)   # prereq -> course
            in_degree[course] += 1         # one more requirement for 'course'
        
        # Step 3: Queue for all nodes with in-degree 0 (no prerequisites)
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        # Count of processed courses
        processed = 0
        
        # Step 4: Perform BFS (Kahn’s Algorithm)
        while queue:
            # Remove a course with no prerequisites
            curr = queue.popleft()
            processed += 1
            
            # Reduce in-degree of all dependent courses
            for neighbor in graph[curr]:
                in_degree[neighbor] -= 1
                
                # If a course now has no prereqs, push to queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If all courses processed → no cycle → possible to finish
        return processed == numCourses
