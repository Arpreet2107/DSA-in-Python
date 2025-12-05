# ✅ 24. Longest Common Subsequence (LCS)

# Classic DP problem.
# 24.1 LCS – Length Only (DP Table)
def lcs_length(s1, s2):
    """
    Longest Common Subsequence (LCS) length.
    
    dp[i][j] = LCS of s1[:i] and s2[:j]
    """

    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if s1[i - 1] == s2[j - 1]:   # characters match
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:                       # skip one character
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]
