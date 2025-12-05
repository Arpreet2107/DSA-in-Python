# ✅ 48. Traveling Salesman Problem – Bitmask DP (TSP)
# TSP using DP + Bitmask
def tsp(cost):
    n = len(cost)
    ALL = 1 << n

    dp = [[10**18] * n for _ in range(ALL)]

    dp[1][0] = 0   # start at node 0 with mask 000...001

    for mask in range(ALL):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v):
                    continue
                dp[mask | (1 << v)][v] = min(
                    dp[mask | (1 << v)][v],
                    dp[mask][u] + cost[u][v]
                )

    full_mask = ALL - 1
    ans = min(dp[full_mask][i] + cost[i][0] for i in range(n))
    return ans

# Example
cost = [
    [0,20,42,35],
    [20,0,30,34],
    [42,30,0,12],
    [35,34,12,0]
]
print(tsp(cost))
