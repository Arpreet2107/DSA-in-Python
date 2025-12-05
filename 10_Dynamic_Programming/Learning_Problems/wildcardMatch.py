# ✅ 29. Wildcard Matching (? and *)

# ? → matches any 1 character
# * → matches any sequence (even empty)
def wildcardMatch(s, p):
    """
    Wildcard Matching:
    s = text, p = pattern
    ? matches one character
    * matches any sequence
    """

    n, m = len(s), len(p)
    dp = [[False]*(m+1) for _ in range(n+1)]

    dp[0][0] = True

    # if pattern starts with *, it can match empty string
    for j in range(1, m+1):
        if p[j-1] == "*":
            dp[0][j] = dp[0][j-1]

    for i in range(1, n+1):
        for j in range(1, m+1):

            if p[j-1] == s[i-1] or p[j-1] == "?":
                dp[i][j] = dp[i-1][j-1]

            elif p[j-1] == "*":
                dp[i][j] = dp[i-1][j] or dp[i][j-1]

            else:
                dp[i][j] = False

    return dp[n][m]
