# ✅ 22. Maximum Ribbon Cut (Max number of pieces)

# You can cut infinite pieces from ribbon of length n.
def maxRibbonCut(n, lengths):
    """
    Maximum Ribbon Cut:
    Max number of pieces we can cut from length n.
    
    dp[x] = max pieces to form length x
    """

    dp = [-1] * (n + 1)
    dp[0] = 0

    for length in lengths:
        for x in range(length, n + 1):
            if dp[x - length] != -1:  # valid
                dp[x] = max(dp[x], dp[x - length] + 1)

    return dp[n]
