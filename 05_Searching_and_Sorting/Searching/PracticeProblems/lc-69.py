# 🧮 LeetCode 69 — Sqrt(x)
# Problem

# Given a non-negative integer x, return the integer part of √x.

# You must NOT use built-in sqrt().

# Example:
# x = 8 → √8 ≈ 2.82 → return 2

# 🔥 Why Binary Search?

# We want the largest integer m such that:

# m * m <= x


# The square root grows monotonically, so binary search fits perfectly.

# Search space = [0 … x].

# 🔍 Binary Search Logic

# Maintain two pointers:

# left = 0
# right = x


# At each mid:

# ✔ Case 1: mid * mid == x

# Exact square → return mid

# ✔ Case 2: mid * mid < x

# mid is too small → move to the right:
# left = mid + 1
# and record it as a possible answer

# ✔ Case 3: mid * mid > x

# mid is too large → move left:
# right = mid - 1

# At the end:
# right will contain the floor of √x.
class Solution:
    def mySqrt(self, x):
        # Edge cases
        if x == 0 or x == 1:
            return x

        left, right = 0, x
        ans = 0  # will store the floor of sqrt(x)

        # Binary search on the range [0, x]
        while left <= right:
            mid = (left + right) // 2

            # If mid^2 equals x → exact sqrt
            if mid * mid == x:
                return mid

            # If mid^2 is smaller → move right
            elif mid * mid < x:
                ans = mid          # mid is a potential answer
                left = mid + 1     # try to find larger value

            # If mid^2 is larger → move left
            else:
                right = mid - 1

        # Return the integer part of sqrt(x)
        return ans
