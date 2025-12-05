# 28B. Print SCS (Actual string)

# Use LCS to merge both strings.

def print_SCS(s1, s2):
    """
    Print actual Shortest Common Supersequence
    """

    # Step 1: compute LCS dp table
    n, m = len(s1), len(s2)
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Step 2: backtrack and build SCS
    i, j = n, m
    result = []

    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            result.append(s1[i-1])
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                result.append(s1[i-1])
                i -= 1
            else:
                result.append(s2[j-1])
                j -= 1

    # append leftover chars
    while i > 0:
        result.append(s1[i-1])
        i -= 1

    while j > 0:
        result.append(s2[j-1])
        j -= 1

    return "".join(reversed(result))

