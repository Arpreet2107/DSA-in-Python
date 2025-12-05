# ✅ 4. Climbing Stairs (Leetcode #70)
# Problem

# You can climb either 1 step or 2 steps at a time.
# How many distinct ways to climb n stairs?

# # ✔ Best Approach: DP (Fibonacci Logic)
def climbStairs(n: int) -> int:
    """
    Climbing Stairs - Count number of ways to reach the top.
    You can climb 1 step or 2 steps at a time.
    
    DP relation:
        dp[i] = dp[i-1] + dp[i-2]
    
    Reason:
        - From step i-1 take one step
        - From step i-2 take two steps
    """
    
    # Base cases:
    if n == 1:
        return 1
    if n == 2:
        return 2

    # Initialize first 2 Fibonacci-like values
    prev2, prev1 = 1, 2  

    # Build dp from 3 to n
    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1
