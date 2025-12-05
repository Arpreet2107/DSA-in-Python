# ⚡ Jump Game II (Leetcode #45)
# Problem

# Minimum number of jumps to reach last index.

# ✔ Greedy with Level BFS Logic
def jump(nums):
    """
    Jump Game II:
    Greedy:
        - end marks the end of current jump range
        - farthest is the farthest reachable index
    """

    jumps = 0
    end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])

        # When we reach end of current jump range
        if i == end:
            jumps += 1
            end = farthest   # extend to next range

    return jumps
