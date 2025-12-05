# ⭐ 4. Memoization (Top-Down DP)
# ✅ Definition

# Memoization is a top-down DP approach where:

# You write a recursive solution

# Store results of subproblems in a dictionary or array

# Reuse stored results instead of recalculating

# ➡️ Recursion + Cache = Memoization
# ✔ Advantages

# Easy recursive style

# Avoids redundant recalculation

# Faster than plain recursion

# ❌ Limitations

# Uses recursion → risk of recursion limit error

# Requires extra dictionary space
# Memoized Fibonacci (Top-Down DP)

# Dictionary used to remember computed values
memo = {}

def fib(n):
    # If result already exists, return it (avoid recomputation)
    if n in memo:
        return memo[n]

    # Base cases for fibonacci
    if n <= 1:
        return n

    # Recursive computation with memoization
    # Store result to avoid future recalculations
    memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]

# Example usage
print(fib(10))  # Output: 55
