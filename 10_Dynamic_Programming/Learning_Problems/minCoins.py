# ✅ 21. Minimum Coin Change (Min Coins to Make Amount)

# (Different from Coin Change – total ways)
def minCoins(coins, amount):
    """
    Minimum number of coins to make 'amount'.
    Unbounded Knapsack (minimization).
    
    dp[x] = minimum coins needed to make amount x
    """

    INF = float('inf')
    dp = [INF] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != INF else -1
