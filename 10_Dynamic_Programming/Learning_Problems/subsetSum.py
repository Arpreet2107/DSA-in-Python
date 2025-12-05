# ✅ 12. Subset Sum Problem – DP | O(n * sum)

# Return True if any subset sums to target.
def subsetSum(nums, target):
    """
    Subset Sum: return True if some subset sums to target.
    
    dp[i][j] = using first i numbers, can we make sum j?
    Optimized to 1-D DP:
        dp[j] = whether we can make sum j
    """

    dp = [False] * (target + 1)
    dp[0] = True    # empty set can form sum 0

    for num in nums:
        # Traverse backwards to avoid overwriting
        for j in range(target, num - 1, -1):
            if dp[j - num]:
                dp[j] = True

    return dp[target]
