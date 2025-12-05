# 🟦 LeetCode 516 — Longest Palindromic Subsequence
# Approach: Dynamic Programming (Bottom-Up)

# We build a DP table where:

# dp[i][j] = LPS length inside substring s[i : j+1]

# Transition:

# If characters match → dp[i][j] = 2 + dp[i+1][j-1]

# Otherwise → dp[i][j] = max(dp[i+1][j], dp[i][j-1])

# Time: O(n²)
# Space: O(n²)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        We use dynamic programming to compute the length of the
        longest palindromic subsequence in the string.
        """

        n = len(s)

        # Create a dp table of size n x n initialized to 0
        # dp[i][j] stores the LPS length in substring s[i..j]
        dp = [[0] * n for _ in range(n)]

        # Every single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1

        # Fill the table for lengths from 2 to n
        # We fill from bottom → top because dp[i][j] depends on dp[i+1][j-1]
        for length in range(2, n + 1):        # substring length
            for i in range(n - length + 1):   # starting index
                j = i + length - 1            # ending index

                # Case 1: Characters match
                if s[i] == s[j]:
                    # If i+1 <= j-1, should use dp inside; otherwise both chars form length 2
                    dp[i][j] = 2 + (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)

                else:
                    # Case 2: Characters do not match
                    # Take max of:
                    # 1) removing left char → dp[i+1][j]
                    # 2) removing right char → dp[i][j-1]
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # dp[0][n-1] contains the answer for the whole string
        return dp[0][n - 1]
