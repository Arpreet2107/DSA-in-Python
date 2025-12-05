# ✅ 39. DP on Triangle (Minimum Path Total)

# Classic bottom-up DP.

# ✔ O(n²) Space Optimized solution
def minimumTotal(triangle):
    """
    Bottom-up DP over triangle.
    Each row depends only on the row below it.
    """

    dp = triangle[-1][:]   # start from last row

    for r in range(len(triangle) - 2, -1, -1):
        for c in range(len(triangle[r])):
            # Best of two children directly below
            dp[c] = min(dp[c], dp[c + 1]) + triangle[r][c]

    return dp[0]
