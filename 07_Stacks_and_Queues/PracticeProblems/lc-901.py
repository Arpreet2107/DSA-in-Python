# 📈 LeetCode 901 — Online Stock Span
# ✅ What the problem asks

# You will get a stream of stock prices one by one.

# For each price, return the stock span, meaning:

# How many consecutive previous days (including today) had a price ≤ today’s price?

# Example:

# Price = 100 → span 1

# Prices = [100, 80, 60, 70, 60, 75, 85]

# Spans = [1, 1, 1, 2, 1, 4, 6]

# 🧠 Key Insight — Use a Monotonic Stack

# We use a stack of pairs:

# (price, span)


# For each new price:

# Pop while the stack top price ≤ current price

# Add up all the popped spans (because current price dominates them)

# Push (current_price, total_span) back to stack

# This ensures:

# Each price is pushed & popped once

# O(1) average time per query

# O(n) total
class StockSpanner:

    def __init__(self):
        # Stack will store pairs: (price, span)
        # Monotonic decreasing stack (top has smallest prices)
        self.stack = []

    def next(self, price: int) -> int:
        # Start with span = 1 (the current day itself)
        span = 1

        # Pop all smaller or equal prices from stack
        # because their span contributes to today's span
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]  # Add the popped element's span
            self.stack.pop()           # Remove it
        
        # Push current price and its computed span
        self.stack.append((price, span))
        
        return span
