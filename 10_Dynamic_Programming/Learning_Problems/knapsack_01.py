# ✅ 18. 0/1 Knapsack (Classic DP)

# Each item can be taken 0 or 1 time.
# Maximize total value without exceeding max weight W.
def knapsack_01(weights, values, W):
    """
    0/1 Knapsack:
    
    dp[w] = maximum value with weight limit w.

    Traverse backwards to avoid reusing items.
    """

    n = len(weights)
    dp = [0] * (W + 1)

    for i in range(n):
        wt = weights[i]
        val = values[i]
        
        for w in range(W, wt - 1, -1):
            dp[w] = max(
                dp[w],               # don't take item
                dp[w - wt] + val     # take item
            )

    return dp[W]
