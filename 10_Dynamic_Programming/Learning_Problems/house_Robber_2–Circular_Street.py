# ✅ House Robber II – Circular Street (Leetcode #213)
# Logic

# First and last houses are adjacent → cannot rob both.

# So solve two cases:
# 1️⃣ Rob houses from 0 to n-2
# 2️⃣ Rob houses from 1 to n-1
# Take max of both.
def rob2(nums):
    """
    House Robber II:
    The houses are arranged in a circle.
    
    Solution = max(
        rob first to second-last,
        rob second to last
    )
    """

    if len(nums) == 1:
        return nums[0]

    def rob_linear(arr):
        prev2, prev1 = 0, 0
        for money in arr:
            prev2, prev1 = prev1, max(prev1, prev2 + money)
        return prev1

    # Case 1: Include first house, exclude last
    case1 = rob_linear(nums[:-1])

    # Case 2: Exclude first, include last
    case2 = rob_linear(nums[1:])

    return max(case1, case2)
