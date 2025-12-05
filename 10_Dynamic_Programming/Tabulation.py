# ⭐ 5. Tabulation (Bottom-Up DP)
# ✅ Definition

# Tabulation is a bottom-up DP approach where:

# We solve all subproblems iteratively

# Store answers in a DP table

# Build final result from base cases upward

# ➡️ Iteration + DP Table = Tabulation
# ✔ Advantages

# No recursion

# Usually faster in practice

# Uses predictable indexes

# ❌ Limitations

# Must build full DP table

# May use more memory than needed
# Tabulated Fibonacci (Bottom-Up DP)

def fib(n):
    # Create DP table of size n+1
    dp = [0] * (n + 1)

    # Base cases
    if n > 0:
        dp[1] = 1

    # Fill table iteratively
    for i in range(2, n + 1):
        # Current value is sum of previous two
        dp[i] = dp[i - 1] + dp[i - 2]

    # Final result stored at dp[n]
    return dp[n]

# Example usage
print(fib(10))  # Output: 55
