# ✔️ 33B. Count Palindromic Partitions

# Count all ways to partition string into palindromes.
def countPalindromePartitions(s):
    """
    Count all palindrome partitioning ways.
    dp[i] = number of ways to partition s[0...i]
    """

    n = len(s)

    # Precompute palindrome table
    isPal = [[False]*n for _ in range(n)]
    for i in range(n):
        isPal[i][i] = True
    for length in range(2, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and (length == 2 or isPal[i+1][j-1]):
                isPal[i][j] = True

    dp = [0] * (n + 1)
    dp[0] = 1   # empty string = 1 way

    for i in range(1, n + 1):
        for j in range(i):
            if isPal[j][i-1]:
                dp[i] += dp[j]

    return dp[n]
