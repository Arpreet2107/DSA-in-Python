# ✅ 36. Cherry Pickup (Hard, Grid DP + Backtracking)

# Best solution: DP on two people moving together
# State: (r1, c1, r2, c2) → use optimized state (r1, c1, r2)
# Time: O(n³)
def cherryPickup(grid):
    """
    Hard problem:
    Two people starting at (0,0) moving down/right to (n-1,n-1)
    Maximize cherries collected.
    DP with state: (r1, c1, r2) since c2 = r1 + c1 - r2
    """

    n = len(grid)
    from functools import lru_cache

    @lru_cache(None)
    def dp(r1, c1, r2):
        c2 = r1 + c1 - r2

        # invalid positions
        if r1 >= n or c1 >= n or r2 >= n or c2 >= n:
            return -float('inf')

        # thorn cells
        if grid[r1][c1] == -1 or grid[r2][c2] == -1:
            return -float('inf')

        # destination
        if r1 == n-1 and c1 == n-1:
            return grid[r1][c1]

        cherries = grid[r1][c1]
        if (r1, c1) != (r2, c2):     # don't double count
            cherries += grid[r2][c2]

        # next moves: (down/right for both persons)
        best = max(
            dp(r1+1, c1, r2+1),
            dp(r1+1, c1, r2),
            dp(r1, c1+1, r2+1),
            dp(r1, c1+1, r2)
        )

        return cherries + best

    ans = dp(0, 0, 0)
    return max(ans, 0)
