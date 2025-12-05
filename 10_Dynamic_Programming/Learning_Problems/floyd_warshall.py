# ✅ 47. Floyd-Warshall (DP on Matrix)
# Floyd-Warshall → All-Pairs Shortest Paths
def floyd_warshall(matrix):
    """
    matrix[i][j] = weight from i → j (INF if no edge)
    """
    n = len(matrix)
    dist = [row[:] for row in matrix]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Example
INF = 10**9
matrix = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]
print(floyd_warshall(matrix))
