# ✅ 37. Dungeon Game (Hard, DP from bottom-right)

# Hero starts at (0,0) and must reach (m−1,n−1).
# Health must never drop ≤ 0.

# ✔ Solution: Reverse DP — O(m×n)
def calculateMinimumHP(dungeon):
    """
    Dungeon Game - Minimum HP required at start.
    Work backwards from the princess cell.

    dp[i][j] = minimum HP needed to ENTER cell (i,j)
    """

    m, n = len(dungeon), len(dungeon[0])

    # dp with padding + infinity
    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

    # To reach princess, before final cell you need at least 1 HP
    dp[m][n - 1] = dp[m - 1][n] = 1

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):

            # Minimum health needed AFTER this cell
            need_after = min(dp[i + 1][j], dp[i][j + 1])

            # Net health required to enter this cell
            dp[i][j] = max(1, need_after - dungeon[i][j])

    return dp[0][0]
