# 📄 house_robber_213.py — Fully Commented + Test Harness
#!/usr/bin/env python3
# LeetCode 213: House Robber II
# Time Complexity: O(n)
# Space Complexity: O(1)
# The twist: houses are arranged in a circle (first and last cannot both be robbed).

def rob_linear(nums: list[int]) -> int:
    """
    Helper function that solves the House Robber problem in a
    linear arrangement (same as LC 198). Used twice:
    - Once excluding the last house
    - Once excluding the first house
    """
    prev2 = 0  # dp[i-2]
    prev1 = 0  # dp[i-1]

    for amount in nums:
        current = max(prev1, prev2 + amount)
        prev2 = prev1
        prev1 = current

    return prev1


def rob(nums: list[int]) -> int:
    """
    Since the houses are in a circle:
    - We cannot rob both house 0 and house n-1.

    Therefore, we consider two cases:
        1. Rob houses from 0 → n-2 (exclude last house)
        2. Rob houses from 1 → n-1 (exclude first house)

    The final answer = max(case1, case2)
    """

    n = len(nums)

    # If there are no houses
    if n == 0:
        return 0

    # If there is only 1 house
    if n == 1:
        return nums[0]

    # Case 1: Exclude last house
    case1 = rob_linear(nums[:-1])

    # Case 2: Exclude first house
    case2 = rob_linear(nums[1:])

    return max(case1, case2)


# ----- Test Harness -----
if __name__ == "__main__":
    tests = [
        ([2,3,2], 3),       # cannot rob both 2's → rob 3
        ([1,2,3,1], 4),     # linear best is 4
        ([1,2,3], 3),
        ([0,0], 0),
        ([1], 1),
        ([200,3,140,20,10], 340)  # 200 + 140
    ]

    for arr, expected in tests:
        result = rob(arr)
        status = "PASS" if result == expected else "FAIL"
        print(f"rob({arr}) = {result} (expected {expected}) → {status}")
