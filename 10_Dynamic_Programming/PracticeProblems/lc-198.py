# 📄 house_robber_198.py — Fully Commented + Test Harness
#!/usr/bin/env python3
# LeetCode 198: House Robber
# Time Complexity: O(n)
# Space Complexity: O(1)
# We use a dynamic programming approach with two variables.

def rob(nums: list[int]) -> int:
    """
    Return the maximum amount of money that can be robbed without robbing
    any two adjacent houses.

    Recurrence:
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    We optimize space by storing only dp[i-1] (prev1) and dp[i-2] (prev2).
    """

    # prev2 = dp[i-2] (max robbed until two houses behind)
    prev2 = 0

    # prev1 = dp[i-1] (max robbed until previous house)
    prev1 = 0

    # Loop through each house's money
    for amount in nums:
        # Either rob this house (prev2 + amount)
        # Or skip it (prev1)
        current = max(prev1, prev2 + amount)

        # Shift dp values for next iteration
        prev2 = prev1
        prev1 = current

    # prev1 holds dp[n-1], the final answer
    return prev1


# ----- Small test harness (runs only when executed directly) -----
if __name__ == "__main__":
    tests = [
        ([1,2,3,1], 4),     # rob houses 1 and 3 → 1+3 = 4
        ([2,7,9,3,1], 12),  # rob houses 2 and 3 → 7+9 = 16? No → 2+9+1=12 is best
        ([2,1,1,2], 4),     # rob 2 + 2
        ([5], 5),
        ([], 0)
    ]

    for arr, expected in tests:
        result = rob(arr)
        status = "PASS" if result == expected else "FAIL"
        print(f"rob({arr}) = {result} (expected {expected}) → {status}")
