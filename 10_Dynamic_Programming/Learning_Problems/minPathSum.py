# ✅ 35. Minimum Path Sum
def minPathSum(grid):
    """
    Minimum sum path from top-left to bottom-right.
    dp[i][j] = min sum to reach cell (i, j)
    """

    m, n = len(grid), len(grid[0])

    dp = [[0]*n for _ in range(m)]
    dp[0][0] = grid[0][0]

    # First row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # First column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Internal cells
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[-1][-1]
