
# ⚡ 8. Jump Game I (Leetcode #55)
# Problem

# Return true if you can reach last index.

# ✔ Greedy Best Solution
def canJump(nums):
    """
    Jump Game I:
    Greedy approach: keep track of the farthest you can reach.
    """

    farthest = 0

    for i, jump in enumerate(nums):
        if i > farthest:      # cannot reach this position
            return False

        farthest = max(farthest, i + jump)

    return True
