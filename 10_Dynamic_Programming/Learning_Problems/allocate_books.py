# ✔ 51. Allocate Books / Painters Partition (Same as above)
# Allocate Books Problem
def allocate_books(pages, students):
    if students > len(pages):
        return -1

    def can(mid):
        needed = 1
        cur = 0
        for p in pages:
            if cur + p > mid:
                needed += 1
                cur = p
                if needed > students:
                    return False
            else:
                cur += p
        return True

    lo, hi = max(pages), sum(pages)

    while lo < hi:
        mid = (lo + hi) // 2
        if can(mid):
            hi = mid
        else:
            lo = mid + 1

    return lo

print(allocate_books([12, 34, 67, 90], 2))
