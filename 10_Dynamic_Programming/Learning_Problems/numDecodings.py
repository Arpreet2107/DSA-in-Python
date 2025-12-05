# ⚡ 7. Decode Ways (Leetcode #91)
# Problem

# Given digits "123", count number of possible decodings (A=1..Z=26).

# ✔ DP (Important Interview Problem)
def numDecodings(s: str) -> int:
    """
    Decode Ways:
    Count number of ways to decode digits to A-Z.

    dp[i] = number of ways to decode substring s[:i]
    """

    if not s or s[0] == "0":
        return 0

    n = len(s)
    dp0, dp1 = 1, 1   # dp[0] = dp[1] = 1 for valid string

    for i in range(1, n):
        temp = 0

        # Single digit decode
        if s[i] != "0":
            temp += dp1

        # Two digit decode
        if 10 <= int(s[i-1:i+1]) <= 26:
            temp += dp0

        dp0, dp1 = dp1, temp

    return dp1
