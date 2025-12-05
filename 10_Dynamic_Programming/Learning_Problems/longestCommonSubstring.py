# ✅ 25. Longest Common Substring

# (LCS substring, not subsequence → must be contiguous)

# DP Formula

# If characters match:

# dp[i][j] = 1 + dp[i-1][j-1]


# Else:

# dp[i][j] = 0

# Implementation
def longestCommonSubstring(s1, s2):
    """
    Longest Common Substring (must be contiguous)
    dp[i][j] = length of longest suffix ending at s1[i-1], s2[j-1]
    """

    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    max_len = 0
    end = 0  # ending index in s1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end = i
            else:
                dp[i][j] = 0

    return s1[end - max_len : end]  # actual substring
