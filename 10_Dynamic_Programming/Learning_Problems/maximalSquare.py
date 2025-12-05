# ✅ 38. Maximal Square (Largest Square of 1's)

# Given a binary matrix, find area of the largest 1-square.

# ✔ DP Relation

# dp[i][j] = min(top, left, topleft) + 1 when cell == 1.
def maximalSquare(matrix):
    """
    Find largest square of 1's.
    dp[i][j] = size of largest square ending at (i,j)
    """

    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]

    max_side = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1' or matrix[i][j] == 1:

                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    ) + 1

                max_side = max(max_side, dp[i][j])

    return max_side * max_side       # area
