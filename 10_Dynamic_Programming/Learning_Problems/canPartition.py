# ✅ 13. Equal Partition (Partition Equal Subset Sum)
# If array can be split into two subsets with equal sum.

# ✔ Reduce to subset sum = total_sum // 2
def canPartition(nums):
    """
    Equal Partition problem:
    Check if array can be divided into 2 equal-sum subsets.
    
    Condition:
        total_sum must be even
        then check subset sum for total_sum // 2
    """

    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[target]
