# ✅ 34B. Unique Paths II (With Obstacles)
def uniquePathsWithObstacles(grid):
    """
    Obstacles = 1, empty = 0
    If obstacle found, cell becomes 0 ways.
    """

    m, n = len(grid), len(grid[0])
    dp = [[0]*n for _ in range(m)]

    # Start
    if grid[0][0] == 1:
        return 0
    dp[0][0] = 1

    # Fill first row
    for j in range(1, n):
        dp[0][j] = 0 if grid[0][j] == 1 else dp[0][j-1]

    # Fill first column
    for i in range(1, m):
        dp[i][0] = 0 if grid[i][0] == 1 else dp[i-1][0]

    # General DP
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]
