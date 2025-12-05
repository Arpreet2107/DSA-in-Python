# ✅ LeetCode 322 — Coin Change (Python + Full Explanation)
# 🧠 Problem Summary

# Given an array coins[] and an amount, return the minimum number of coins needed to make that amount.
# If it is not possible, return -1.
# ✅ 📝 Explanation (Simple & Clear)
# DP Definition

# dp[x] = minimum coins needed to make x.

# Initialization

# dp[0] = 0 (0 coins to make 0)

# All other values initially set to large number (amount + 1)

# Transition

# For every amount i:

# dp[i] = min(dp[i], 1 + dp[i - coin])


# Because:

# We choose coin coin

# Remaining amount becomes i - coin

# So 1 coin + best answer for remaining amount

# Final Answer

# If dp[amount] was updated → return it

# Else → return -1
class Solution:
    def coinChange(self, coins, amount):
        """
        We want the minimum number of coins needed to make 'amount'.
        This is a classic Unbounded Knapsack DP problem.
        """

        # Edge case: if amount is 0, we need 0 coins
        if amount == 0:
            return 0

        # Create a DP array where dp[x] = minimum coins required to make x
        # Initialize with a large value (amount + 1) since this is more than worst case
        dp = [amount + 1] * (amount + 1)

        # Base case: 0 coins needed to make amount 0
        dp[0] = 0

        # Loop through every amount from 1 to 'amount'
        for curr_amount in range(1, amount + 1):

            # Try every coin
            for coin in coins:

                # Check only if coin value ≤ current amount
                if coin <= curr_amount:

                    """
                    dp[curr_amount - coin] gives the min coins needed to make the
                    remaining amount after choosing this coin.

                    We add +1 because we are using one coin (the current coin).
                    """

                    dp[curr_amount] = min(dp[curr_amount], 1 + dp[curr_amount - coin])

        # If dp[amount] is still amount+1, it means amount cannot be formed
        return dp[amount] if dp[amount] != amount + 1 else -1
