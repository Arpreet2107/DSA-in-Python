# ✅ 27. Shortest Common Supersequence (SCS Length)

# The shortest string that contains both strings.

# Formula
# SCS length = n + m - LCS
def scs_length(s1, s2):
    """
    Shortest Common Supersequence length = n + m - LCS
    """

    # Compute LCS length first
    n, m = len(s1), len(s2)
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    LCS = dp[n][m]
    return n + m - LCS
