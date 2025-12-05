# ✅ 11. Frog Jump (Japanese Student Problem) – DP

# Frog is on stone 0 and wants to reach stone n−1.
# Allowed moves:

# jump 1 stone → cost = |h[i] − h[i−1]|

# jump 2 stones → cost = |h[i] − h[i−2]|

# ✔ DP solution
def frogJump(heights):
    """
    Frog Jump (Japanese Student Problem)
    
    dp[i] = minimum cost to reach stone i
    frog can jump from:
      - i-1 (cost = abs(h[i] - h[i-1]))
      - i-2 (cost = abs(h[i] - h[i-2]))
    """

    n = len(heights)
    dp = [0] * n

    # Base cases
    dp[0] = 0
    dp[1] = abs(heights[1] - heights[0])

    for i in range(2, n):
        jump_one = dp[i-1] + abs(heights[i] - heights[i-1])
        jump_two = dp[i-2] + abs(heights[i] - heights[i-2])
        dp[i] = min(jump_one, jump_two)

    return dp[-1]

