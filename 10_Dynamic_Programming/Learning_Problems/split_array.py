# ✔ 50. Split Array Largest Sum (Binary Search on Answer)
# Split Array into k parts minimizing the maximum subarray sum
def split_array(nums, k):
    def can(mid):
        pieces = 1
        cur = 0
        for x in nums:
            if cur + x > mid:
                pieces += 1
                cur = x
                if pieces > k:
                    return False
            else:
                cur += x
        return True

    lo, hi = max(nums), sum(nums)

    while lo < hi:
        mid = (lo + hi) // 2
        if can(mid):
            hi = mid
        else:
            lo = mid + 1

    return lo

print(split_array([7,2,5,10,8], 2))
