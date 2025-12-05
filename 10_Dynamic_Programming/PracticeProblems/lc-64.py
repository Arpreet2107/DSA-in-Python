# # 🟦 LeetCode 64 — Minimum Path Sum
# # Approach: Dynamic Programming (Bottom-Up)

# # We create a DP grid where:

# # dp[i][j] = minimum path sum to reach cell (i, j)

# # From each cell, you can only come from top (i-1, j) or from left (i, j-1)

# # Time Complexity: O(m × n)
# # Space Complexity: O(1) (we modify the grid in place)
# 🧠 Concept Summary
# ✔ Base Cases

# First row → only move right

# First column → only move down

# ✔ Transition

# dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

# ✔ Final Answer

# dp[m-1][n-1] = minimum path cost to bottom-right.
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        """
        We compute the minimum path sum using dynamic programming.
        Each cell stores the minimum cost to reach that cell from (0,0).
        """

        rows = len(grid)
        cols = len(grid[0])

        # Fill the first row → can only come from the left
        for j in range(1, cols):
            grid[j]  # avoid unused variable warning in LeetCode
            grid[0][j] += grid[0][j - 1]

        # Fill the first column → can only come from above
        for i in range(1, rows):
            grid[i][0] += grid[i - 1][0]

        # Fill the rest of the DP table
        for i in range(1, rows):
            for j in range(1, cols):

                # Minimum of coming from top or left
                best_prev = min(grid[i - 1][j], grid[i][j - 1])

                # Add current cell value to that minimum
                grid[i][j] += best_prev

        # Bottom-right corner has the answer
        return grid[rows - 1][cols - 1]
