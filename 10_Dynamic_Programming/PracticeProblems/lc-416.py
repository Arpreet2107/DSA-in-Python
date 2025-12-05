# 📄 partition_equal_subset_sum_416.py — Fully Commented + Test Harness
#!/usr/bin/env python3
# LeetCode 416: Partition Equal Subset Sum
# Time Complexity: O(n * target)
# Space Complexity: O(target)
# Core idea: Subset Sum DP to check if we can form total/2.

def canPartition(nums: list[int]) -> bool:
    """
    Determine if the array can be partitioned into two subsets
    such that the sum of both subsets is equal.

    Steps:
    1. Compute total sum.
    2. If sum is odd → impossible to split equally.
    3. Target = total // 2
    4. Use DP subset sum to check if target is achievable.
    """

    total = sum(nums)

    # If total sum is odd, cannot split into equal halves
    if total % 2 != 0:
        return False

    target = total // 2

    # dp[s] = True if we can form sum s
    dp = [False] * (target + 1)
    dp[0] = True  # sum 0 is always achievable (pick nothing)

    # Iterate through each number
    for num in nums:
        # Traverse backwards to avoid using the same element twice
        for s in range(target, num - 1, -1):
            # If s-num is achievable, s becomes achievable
            if dp[s - num]:
                dp[s] = True

    # Final answer is whether target is achievable
    return dp[target]


# ----- Test Harness -----
if __name__ == "__main__":
    tests = [
        ([1, 5, 11, 5], True),    # 11 = 11 → possible
        ([1, 2, 3, 5], False),    # can't split equally
        ([2, 2, 3, 5], False),
        ([3, 3, 3, 4, 5], True),
        ([1, 1], True),
        ([1, 2, 5], False),
    ]

    for arr, expected in tests:
        result = canPartition(arr)
        status = "PASS" if result == expected else "FAIL"
        print(f"canPartition({arr}) = {result} (expected {expected}) → {status}")
