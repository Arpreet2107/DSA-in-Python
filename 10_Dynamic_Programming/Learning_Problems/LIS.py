# ✔ 49. LIS (Binary Search O(n log n))
# Longest Increasing Subsequence O(n log n)
import bisect

def LIS(nums):
    tail = []

    for x in nums:
        idx = bisect.bisect_left(tail, x)
        if idx == len(tail):
            tail.append(x)
        else:
            tail[idx] = x

    return len(tail)

print(LIS([10,9,2,5,3,7,101,18]))
