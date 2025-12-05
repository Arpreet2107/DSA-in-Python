# 16.3 Combination Sum IV (Leetcode #377 – Count number of combinations)

# Order matters (1+2 and 2+1 are different).
def combinationSum4(nums, target):
    """
    Combination Sum IV:
    Count ways to form the target.
    Order matters = dp forward approach.
    """

    dp = [0] * (target + 1)
    dp[0] = 1

    for t in range(1, target + 1):
        for num in nums:
            if num <= t:
                dp[t] += dp[t - num]

    return dp[target]
