# 16.2 Combination Sum II (Leetcode #40)

# Numbers can be used once, array may contain duplicates, and combinations must be unique.
def combinationSum2(candidates, target):
    """
    Combination Sum II:
    Each number can be used at most once.
    Must avoid duplicate combinations.
    """

    res = []
    candidates.sort()

    def backtrack(start, remain, path):
        if remain == 0:
            res.append(path[:])
            return
        if remain < 0:
            return

        prev = -1  # to avoid picking same elements at same level
        for i in range(start, len(candidates)):
            if candidates[i] == prev:  # skip duplicates
                continue
            prev = candidates[i]

            path.append(candidates[i])
            backtrack(i + 1, remain - candidates[i], path)
            path.pop()

    backtrack(0, target, [])
    return res
