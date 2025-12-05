# ✅ 26. Edit Distance (Leetcode #72)

# Operations allowed: Insert, Delete, Replace

# DP Relation
# if s1[i] == s2[j]:
#     dp[i][j] = dp[i-1][j-1]
# else:
#     dp[i][j] = 1 + min(
#         dp[i-1][j],    # delete
#         dp[i][j-1],    # insert
#         dp[i-1][j-1]   # replace
#     )
def editDistance(s1, s2):
    """
    Edit Distance (Levenshtein distance)
    dp[i][j] = min edits to convert s1[:i] -> s2[:j]
    """

    n, m = len(s1), len(s2)
    dp = [[0]*(m+1) for _ in range(n+1)]

    # base cases
    for i in range(n+1):
        dp[i][0] = i  # all deletes
    for j in range(m+1):
        dp[0][j] = j  # all inserts

    for i in range(1, n+1):
        for j in range(1, m+1):

            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # delete
                    dp[i][j-1],    # insert
                    dp[i-1][j-1]   # replace
                )

    return dp[n][m]
