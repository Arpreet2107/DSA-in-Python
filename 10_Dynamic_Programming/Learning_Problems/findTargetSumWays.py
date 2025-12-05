# ✅ 15. Target Sum (Leetcode #494)

# We need to assign + or - to numbers so they sum to target.

# Convert to subset sum problem:

# Let

# P = sum of positive numbers  
# N = sum of negative numbers  
# P - N = target  
# P + N = total_sum  


# After solving:

# P = (total_sum + target) // 2


# Now count subsets with sum P.
def findTargetSumWays(nums, target):
    """
    Target Sum = Count ways to assign + or - to reach target.

    Convert to:
        Count subsets with sum = (total + target) // 2
    """

    total = sum(nums)

    # if conversion impossible:
    if (total + target) % 2 != 0 or (total + target) < 0:
        return 0

    S = (total + target) // 2

    dp = [0] * (S + 1)
    dp[0] = 1

    for num in nums:
        for j in range(S, num - 1, -1):
            dp[j] += dp[j - num]

    return dp[S]
