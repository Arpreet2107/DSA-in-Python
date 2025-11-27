# # # ✅ LeetCode 75 — Sort Colors
# # 🎯 Problem Summary

# # You are given an array nums containing only:

# # 0 → Red

# # 1 → White

# # 2 → Blue

# # You must sort the array in-place, without using library sort.
# # Final output must be: all 0’s, then 1’s, then 2’s.
# ✅ BEST APPROACH — Dutch National Flag Algorithm (One-Pass, O(1) space)

# We maintain 3 pointers:
# | Pointer | Meaning                           |
# | ------- | --------------------------------- |
# | `low`   | region where 0's should be placed |
# | `mid`   | current element being inspected   |
# | `high`  | region where 2's should be placed |


class Solution:
    def sortColors(self, nums):
        # Three pointers:
        # low  -> position to place next 0
        # mid  -> current element
        # high -> position to place next 2
        low, mid, high = 0, 0, len(nums) - 1

        # Process until mid passes high
        while mid <= high:

            # Case 1: Element is 0 -> should go to the beginning
            if nums[mid] == 0:
                # Swap nums[mid] with nums[low]
                nums[low], nums[mid] = nums[mid], nums[low]
                # Move both pointers forward
                low += 1
                mid += 1

            # Case 2: Element is 1 -> already in correct region
            elif nums[mid] == 1:
                mid += 1

            # Case 3: Element is 2 -> should go to the end
            else:
                # Swap nums[mid] with nums[high]
                nums[high], nums[mid] = nums[mid], nums[high]
                # Move only high backward
                # Do NOT move mid because swapped element may be 0/1/2
                high -= 1

        # nums is now sorted in-place
        return nums
