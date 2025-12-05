# ✅ 17. Coin Change – Two Problems
# 17.1 Minimum Coins (Leetcode #322)

# Return minimum number of coins to make target amount.
def coinChange_minCoins(coins, amount):
    """
    Coin Change (Min Coins):
    Classic DP:
    dp[x] = minimum coins to make sum x
    """

    INF = float("inf")
    dp = [INF] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != INF else -1
