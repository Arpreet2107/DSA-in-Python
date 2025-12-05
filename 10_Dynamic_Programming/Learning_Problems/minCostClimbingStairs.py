# ⚡ 6. Minimum Cost Climbing Stairs (Leetcode #746)
# Problem

# From step i you can climb to i+1 or i+2.
# Minimum cost to reach the top.

# ✔ DP Approach
def minCostClimbingStairs(cost):
    """
    Minimum Cost Climbing Stairs:
    dp[i] = cost to reach step i.

    We want min(dp[n], dp[n-1])
    """

    n = len(cost)
    dp0, dp1 = 0, 0   # base dp[-1], dp[0]

    for i in range(n):
        new_dp = cost[i] + min(dp0, dp1)

        dp0 = dp1
        dp1 = new_dp

    return min(dp0, dp1)
