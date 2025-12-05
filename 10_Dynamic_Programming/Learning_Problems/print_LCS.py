# ✅ 28. Print LCS & Print SCS
# 28A. Print LCS (Actual string)
def print_LCS(s1, s2):
    """
    Return actual Longest Common Subsequence
    """

    n, m = len(s1), len(s2)
    dp = [[0]*(m+1) for _ in range(n+1)]

    # Fill DP
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Backtrack to build LCS
    i, j = n, m
    lcs = []

    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs.append(s1[i-1])
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] >= dp[i][j-1]:
                i -= 1
            else:
                j -= 1

    return "".join(reversed(lcs))
