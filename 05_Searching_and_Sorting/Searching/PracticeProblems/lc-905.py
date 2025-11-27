# ✅ LeetCode 905 — Sort Array By Parity
# 🧠 Problem Summary

# You are given an integer array nums.

# Return a new array where:

# All even numbers come first

# All odd numbers come after

# Order within evens and odds does NOT matter

# ✅ Approach 1 — Two Pointer Method (Most Common & Optimal)
# 💡 Logic

# Maintain two pointers:

# left starting from the beginning.

# right starting from the end.

# While left < right:

# If nums[left] is odd → swap with nums[right] and decrease right.

# Else (it’s even) → move left forward.

# ✔ In-place
# ✔ O(n) time
# ✔ O(1) space

class Solution:
    def sortArrayByParity(self, nums):
        # Two-pointer approach
        # left -> scans from beginning
        # right -> scans from the end
        left, right = 0, len(nums) - 1

        # Continue until both pointers cross
        while left < right:

            # If left is odd, swap with right
            if nums[left] % 2 == 1:
                # Swap odd number to the end
                nums[left], nums[right] = nums[right], nums[left]
                # Move right pointer backward
                right -= 1

            else:
                # If nums[left] is even, it's correctly placed
                left += 1

        # The array is now sorted by parity
        return nums
# ✅ Approach 2 — Extra List (Simplest, but uses extra space)

# class Solution:
#     def sortArrayByParity(self, nums):
#         evens = []
#         odds = []

#         for num in nums:
#             if num % 2 == 0:
#                 evens.append(num)
#             else:
#                 odds.append(num)

#         # Even numbers first, then odd numbers
#         return evens + odds

