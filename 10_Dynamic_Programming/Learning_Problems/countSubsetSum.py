# ✅ 14. Count Subset Sum (Count total subsets whose sum = target)
# DP – Count ways, not boolean
def countSubsetSum(nums, target):
    """
    Count Subset Sum:
    Count how many subsets sum exactly to `target`.

    dp[j] = number of ways to form sum j
    """

    dp = [0] * (target + 1)
    dp[0] = 1  # one way: empty subset

    for num in nums:
        # Traverse backwards (to avoid recomputation issues)
        for j in range(target, num - 1, -1):
            dp[j] += dp[j - num]

    return dp[target]
