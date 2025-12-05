# 🎒 0/1 Knapsack using DP — Tabulation
# Goal

# Maximize value such that weight ≤ capacity.
# 0/1 Knapsack using DP (Bottom-Up)

def knapsack(weights, values, capacity):
    n = len(weights)

    # Create DP table with (n+1) rows and (capacity+1) columns
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Loop through all items
    for i in range(1, n + 1):
        # Current weight and value
        w = weights[i - 1]
        v = values[i - 1]

        # Try all possible capacities
        for cap in range(1, capacity + 1):
            
            # If item fits in current capacity
            if w <= cap:
                # Choice: take it OR skip it
                dp[i][cap] = max(
                    v + dp[i - 1][cap - w],  # Take item
                    dp[i - 1][cap]           # Skip item
                )
            else:
                # Item can't fit → skip it
                dp[i][cap] = dp[i - 1][cap]

    # Last cell holds max value
    return dp[n][capacity]

# Example usage
weights = [1, 2, 3]
values = [10, 15, 40]
capacity = 5
print(knapsack(weights, values, capacity))  # Output: 55
