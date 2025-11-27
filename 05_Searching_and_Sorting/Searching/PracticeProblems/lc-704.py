# ✅ LeetCode 704 — Binary Search (Explanation)
# Problem-
# You are given a sorted array nums and a target value.
# You must return the index of target if it exists, otherwise return -1.
# ❗ Key Observations
# The array is sorted, so Binary Search is the optimal method.
# Binary Search works in O(log n) time.
class Solution:
    def search(self, nums, target):
        # Step 1: Initialize two pointers for the search range
        left = 0                      # left pointer at beginning
        right = len(nums) - 1         # right pointer at end
        
        # Step 2: Continue searching while left pointer does not cross right pointer
        while left <= right:
            
            # Step 3: Find the middle index
            mid = (left + right) // 2  # // ensures integer division
            
            # Step 4: Check if the mid element is the target
            if nums[mid] == target:
                return mid             # Found the target, return its index
            
            # Step 5: If mid element is smaller, target is in the right half
            elif nums[mid] < target:
                left = mid + 1         # Move left pointer to narrow the range
            
            # Step 6: If mid element is larger, target is in the left half
            else:
                right = mid - 1        # Move right pointer to narrow the range
        
        # Step 7: Target not found
        return -1
