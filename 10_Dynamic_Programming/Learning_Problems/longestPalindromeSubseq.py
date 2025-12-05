# ✅ 32. Longest Palindromic Subsequence (LPS)

# LPS = LCS(s, reverse(s))

# ✔ DP — O(n²)
def longestPalindromeSubseq(s):
    """
    LPS using standard DP:
    dp[i][j] = LPS length in s[i...j]
    """

    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Single characters = length 1 palindrome
    for i in range(n):
        dp[i][i] = 1

    # Fill from shorter to longer substrings
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]
