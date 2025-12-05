# 17.2 Total Ways to Make Change (Coin Change II – Leetcode #518)

# Infinite supply, but order does not matter.
def coinChange_totalWays(coins, amount):
    """
    Coin Change II:
    Count total number of ways to make 'amount'.
    Unlimited coins, order does NOT matter.
    
    dp[j] = ways to make sum j
    """

    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] += dp[j - coin]

    return dp[amount]
