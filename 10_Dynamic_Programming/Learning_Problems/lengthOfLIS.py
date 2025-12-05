# ✅ 10. Longest Increasing Subsequence (LIS) – O(n² DP)
def lengthOfLIS(nums):
    """
    LIS using simple DP: O(n^2)
    
    dp[i] = length of LIS ending at index i
    """

    n = len(nums)
    dp = [1] * n     # each number alone forms LIS of length 1

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:           # valid increasing
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
