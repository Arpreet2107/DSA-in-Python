# ✅ 19. Unbounded Knapsack (Items can be taken unlimited times)
# DP – exactly like 0/1 knapsack but forward loop for weights
def unboundedKnapsack(weights, values, W):
    """
    Unbounded Knapsack (infinite supply of each item)
    
    dp[w] = maximum value achievable with weight limit w
    
    Unlike 0/1 Knapsack, we iterate weights 'forward'
    to allow unlimited reuse of the same item.
    """

    dp = [0] * (W + 1)

    for i in range(len(weights)):
        wt = weights[i]
        val = values[i]

        for w in range(wt, W + 1):
            dp[w] = max(dp[w], dp[w - wt] + val)

    return dp[W]
