# ✅ 5. House Robber I (Leetcode #198)
# Problem

# You cannot rob two adjacent houses.
# Return maximum money you can rob.
def rob(nums):
    """
    House Robber I:
    You cannot rob two adjacent houses.

    dp[i] = max(
        dp[i-1],             # skip this house
        dp[i-2] + nums[i]    # rob this house
    )
    """

    n = len(nums)
    if n == 1:
        return nums[0]

    prev2 = 0       # dp[i-2]
    prev1 = nums[0] # dp[i-1]

    for i in range(1, n):
        rob_current = prev2 + nums[i]
        skip_current = prev1
        current = max(rob_current, skip_current)

        # shift window
        prev2 = prev1
        prev1 = current

    return prev1
