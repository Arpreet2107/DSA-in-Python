# ✅ LeetCode 70 — Climbing Stairs (Python, Fully Commented)
# ✔ Problem summary

# You are climbing a staircase.
# You can climb 1 or 2 steps at a time.
# How many distinct ways can you reach the top (n steps)?

# This is exactly the Fibonacci sequence.
#!/usr/bin/env python3
# LeetCode 70: Climbing Stairs
# Time Complexity: O(n)
# Space Complexity: O(1)

def climbStairs(n: int) -> int:
    """
    Returns the number of distinct ways to climb to the top.
    For each step, you can climb either 1 or 2 steps.
    Equivalent to Fibonacci(n+1).
    """

    # If n is 0 or 1, there is only 1 way to climb.
    if n <= 1:
        return 1  # Base cases: 1 way to stand still or take 1 step.

    # prev2 = ways to reach step (i-2)
    prev2 = 1  # Equivalent to dp[0]
    # prev1 = ways to reach step (i-1)
    prev1 = 1  # Equivalent to dp[1]

    # Loop from step 2 up to step n
    for step in range(2, n + 1):
        # The recurrence relation:
        # ways(i) = ways(i-1) + ways(i-2)
        current = prev1 + prev2

        # Shift values for next loop
        prev2 = prev1
        prev1 = current

    # prev1 now contains the answer for step n
    return prev1


# Small test harness (runs only if this file is executed directly)
if __name__ == "__main__":
    tests = [1, 2, 3, 4, 5, 10]

    for t in tests:
        print(f"climbStairs({t}) → {climbStairs(t)}")
