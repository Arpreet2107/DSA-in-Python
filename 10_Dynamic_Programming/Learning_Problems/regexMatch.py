# ✅ 30. Regular Expression Matching (. and *)

# . → matches one char
# * → means "zero or more of previous character"
def regexMatch(s, p):
    """
    Regular Expression Matching like Leetcode #10.
    '.' -> matches any single char
    'x*' -> zero or more of 'x'
    """

    n, m = len(s), len(p)
    dp = [[False]*(m+1) for _ in range(n+1)]

    dp[0][0] = True

    # handle patterns like x* or a*b* matching empty string
    for j in range(2, m+1):
        if p[j-1] == "*":
            dp[0][j] = dp[0][j-2]

    for i in range(1, n+1):
        for j in range(1, m+1):

            if p[j-1] == s[i-1] or p[j-1] == ".":
                dp[i][j] = dp[i-1][j-1]

            elif p[j-1] == "*":
                dp[i][j] = dp[i][j-2]  # zero occurrences

                if p[j-2] == s[i-1] or p[j-2] == ".":
                    dp[i][j] = dp[i][j] or dp[i-1][j]  # use one more occurrence

            else:
                dp[i][j] = False

    return dp[n][m]
