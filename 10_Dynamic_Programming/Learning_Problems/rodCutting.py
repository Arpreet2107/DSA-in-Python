# ✅ 20. Rod Cutting (Unbounded Knapsack Variant)

# Given rod length n and prices for each piece length, find max revenue.
def rodCutting(prices, n):
    """
    Rod Cutting:
    Convert to Unbounded Knapsack:
    
    lengths = [1, 2, 3, ..., n]
    values = prices[]
    
    dp[length] = max profit for length
    """

    dp = [0] * (n + 1)

    for length in range(1, n + 1):  # item sizes
        for rod in range(length, n + 1):
            dp[rod] = max(dp[rod], dp[rod - length] + prices[length - 1])

    return dp[n]
