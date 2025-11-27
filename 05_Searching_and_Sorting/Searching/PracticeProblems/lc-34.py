# ✅ LeetCode 34 — Find First and Last Position of Element in Sorted Array
# Problem Summary

# You are given a sorted array (nums) and a target.
# Return the first and last index where the target appears.

# Example:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3, 4]

# If the target is not found, return [-1, -1].

# 🔍 Key Insight

# We must do two binary searches:

# 1️⃣ First Binary Search → Find First Occurrence

# Whenever we find target:

# Continue searching left side (because maybe an earlier occurrence exists)

# 2️⃣ Second Binary Search → Find Last Occurrence

# Whenever we find target:

# Continue searching right side (because maybe a later occurrence exists)

# This ensures:

# O(log n) time

# No linear scanning

# 🧠 Why Binary Search Twice?

# Because in a sorted array with duplicates:

# First occurrence ≠ last occurrence

# But binary search can quickly lock onto boundaries by biasing left/right
class Solution:
    def searchRange(self, nums, target):

        # Helper function to find first or last position
        def findPosition(findFirst):
            left, right = 0, len(nums) - 1
            pos = -1  # default: not found

            while left <= right:
                mid = (left + right) // 2

                # Case 1: Found target
                if nums[mid] == target:
                    pos = mid  # record position

                    # If searching for first position → move left
                    if findFirst:
                        right = mid - 1
                    # If searching for last position → move right
                    else:
                        left = mid + 1

                # Case 2: Target is larger → go right
                elif nums[mid] < target:
                    left = mid + 1

                # Case 3: Target is smaller → go left
                else:
                    right = mid - 1

            return pos

        # First occurrence
        first = findPosition(True)
        # Last occurrence
        last = findPosition(False)

        return [first, last]
