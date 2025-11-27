# 🔥 LeetCode 33 — Search in Rotated Sorted Array
# Problem Summary

# You are given a sorted array that is rotated at some pivot, for example:

# Original: [0,1,2,4,5,6,7]
# Rotated : [4,5,6,7,0,1,2]


# You must search for target and return its index,
# or return -1 if it doesn’t exist.

# 🧠 Core Idea

# Even after rotation, one half of the array is ALWAYS sorted.

# At every mid, one of these is true:

# ✔ Left half is sorted:

# nums[left] ≤ nums[mid]

# ✔ Right half is sorted:

# nums[mid] ≤ nums[right]

# This allows us to decide which half to search.

# 🔍 Binary Search Logic (Very Important)
# Step 1 — Check which half is sorted

# We use the property of sorted arrays to eliminate half of the search space.

# Step 2 — Check if target lies inside the sorted half

# If yes → move into that half
# If not → search the other half

# This is repeated until we find the target or pointers cross.
class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        # Modified binary search for rotated arrays
        while left <= right:
            mid = (left + right) // 2

            # Case 1: Found the target
            if nums[mid] == target:
                return mid

            # Case 2: Left half is sorted
            if nums[left] <= nums[mid]:
                # Check if target is within this sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Case 3: Right half is sorted
            else:
                # Check if target lies inside this sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        # Not found
        return -1
