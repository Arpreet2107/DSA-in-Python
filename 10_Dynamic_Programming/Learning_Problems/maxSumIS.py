# ✅ 9. Maximum Sum Increasing Subsequence (MSIS)
# Problem

# Find the maximum sum of any strictly increasing subsequence.

# ✔ DP – O(n²)
def maxSumIS(nums):
    """
    Maximum Sum Increasing Subsequence (MSIS)
    
    dp[i] = maximum sum ending at index i
    
    For each i:
        Look at all j < i
        If nums[j] < nums[i], you can extend the subsequence.
    """

    n = len(nums)
    dp = nums[:]   # dp[i] = sum including nums[i] itself initially

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:          # valid increasing condition
                dp[i] = max(dp[i], dp[j] + nums[i])

    return max(dp)
