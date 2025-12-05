# ✅ 23. Fractional Knapsack (Greedy)

# Unlike 0/1 knapsack, here we can take fractions of items.

# Greedy approach (Sort by value/weight ratio)
def fractionalKnapsack(weights, values, W):
    """
    Fractional Knapsack:
    Items can be taken fractionally.
    
    Greedy Strategy:
        Sort items by value/weight ratio (descending)
        Pick as much as possible of highest ratio item.
    """

    items = []
    for w, v in zip(weights, values):
        items.append((v/w, w, v))  # (ratio, weight, value)

    items.sort(reverse=True)  # highest ratio first

    total_value = 0

    for ratio, wt, val in items:
        if W == 0:
            break

        if wt <= W:
            # take whole item
            total_value += val
            W -= wt
        else:
            # take fractional part
            total_value += ratio * W
            W = 0

    return total_value
