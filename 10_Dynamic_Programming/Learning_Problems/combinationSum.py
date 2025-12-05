# ✅ 16. Combination Sum Variants

# I will give the three most important variants.

# 16.1 Combination Sum I (Leetcode #39)

# Numbers can be used unlimited times.
def combinationSum(candidates, target):
    """
    Combination Sum I:
    Each number can be chosen unlimited times.
    Use backtracking to explore.
    """

    res = []
    candidates.sort()

    def backtrack(start, remain, path):
        if remain == 0:
            res.append(path[:])
            return
        if remain < 0:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, remain - candidates[i], path)  # i not i+1 because reuse allowed
            path.pop()

    backtrack(0, target, [])
    return res
