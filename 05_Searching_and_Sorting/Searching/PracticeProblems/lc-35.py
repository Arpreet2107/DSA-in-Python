# ✅ LeetCode 35 — Search Insert Position (Explanation)
# Problem

# You are given a sorted array and a target.
# Return the index where the target is found.

# If the target is not present:

# Return the index where it should be inserted to maintain sorted order.

# ✔ This is a perfect fit for Binary Search

# Because:

# Array is sorted

# We want to find either:

# The exact index of the element

# OR the position where it should go

# Time Complexity: O(log n)

# Because binary search reduces the search range by half each step.

# 🔍 Logic

# While performing binary search:

# If target is smaller than nums[mid] → move right pointer left

# If target is larger than nums[mid] → move left pointer right

# When the loop ends:

# left becomes the correct position to insert target.

# This is a known binary-search property.

# 🧠 Why return left?

# Because after the search:

# Everything before left is smaller than target

# Everything after left is greater than target
# → so left is exactly where target must be placed
class Solution:
    def searchInsert(self, nums, target):
        # Initialize two pointers for binary search
        left = 0
        right = len(nums) - 1
        
        # Perform binary search
        while left <= right:
            # Middle index
            mid = (left + right) // 2
            
            # Case 1: Found target
            if nums[mid] == target:
                return mid
            
            # Case 2: Target is larger → search right half
            elif nums[mid] < target:
                left = mid + 1
            
            # Case 3: Target is smaller → search left half
            else:
                right = mid - 1
        
        # If not found, 'left' is the correct insert position
        return left
