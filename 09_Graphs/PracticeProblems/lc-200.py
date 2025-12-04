# ✅ LeetCode 200: Number of Islands — Python Solution (Fully Explained)
# Problem Summary

# You are given a 2D grid of 1s (land) and 0s (water).
# An island is formed by connecting adjacent lands horizontally or vertically.
# Return how many islands are in the grid.
# ✅ How This Works (Short Explanation)
# 1. Scan the grid

# Each time we see an unvisited 1, that means a new island.

# 2. DFS Flood Fill

# Convert that entire island into 0s so we don’t count it again.

# Only 4-direction movement is allowed.

# 3. Count how many times DFS is triggered

# Each trigger = 1 island.

# Time Complexity

# O(M × N) — every cell is visited once.

# Space Complexity

# O(M × N) worst-case recursion stack.
class Solution:
    def numIslands(self, grid):
        # Count rows (height) and columns (width) of the grid
        rows = len(grid)
        cols = len(grid[0])

        # This variable will count how many islands we discover
        islands = 0

        # A helper function to perform DFS and mark visited land
        def dfs(r, c):
            # Check boundaries: if out of grid → stop recursion
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            # If cell is water or already visited → stop recursion
            if grid[r][c] == "0":
                return
            
            # Mark current land as visited by converting "1" → "0"
            grid[r][c] = "0"

            # Move in all 4 possible directions
            dfs(r + 1, c)     # down
            dfs(r - 1, c)     # up
            dfs(r, c + 1)     # right
            dfs(r, c - 1)     # left

        # Loop through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If we find land → this is a new island
                if grid[r][c] == "1":
                    islands += 1      # count the island
                    dfs(r, c)         # wipe out the whole island with DFS

        # Return the total number of islands found
        return islands
