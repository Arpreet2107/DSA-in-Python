# # # ✅ LeetCode 88. Merge Sorted Array — Explanation
# # # Problem Summary

# # # You are given two sorted arrays:

# # # nums1 of size m + n, where the last n places are empty (filled with 0)

# # # nums2 of size n

# # # You must merge nums2 into nums1 so that nums1 becomes a single sorted array.

# # # Important:
# # # You must do this in-place inside nums1, without returning anything.

# # # 🔥 Best Method: Two Pointer From END
# # # Why from the end?

# # # Because nums1 has empty space at the end:

# # # nums1: [1,2,3,0,0,0]
# # #                    ↑ space to fill
# # # nums2: [2,5,6]


# # # If we start merging from the front, we will overwrite valid numbers.
# # # So, we merge from the back, placing the largest elements at the end.

# # # 🎯 Define Three Pointers

# # | Pointer          | Meaning                      |
# # | ---------------- | ---------------------------- |
# # | `p1 = m - 1`     | Last filled element in nums1 |
# # | `p2 = n - 1`     | Last element in nums2        |
# # | `p  = m + n - 1` | Last position in nums1       |
# 🧠 Time Complexity: O(m + n)
# 💾 Space Complexity: O(1) — In-place
class Solution:
    def merge(self, nums1, m, nums2, n):
        # p1 -> last real element in nums1 (index m-1)
        p1 = m - 1
        
        # p2 -> last element in nums2 (index n-1)
        p2 = n - 1
        
        # p -> last index in nums1 (index m+n-1)
        p = m + n - 1
        
        # Run until either p1 or p2 is exhausted
        while p1 >= 0 and p2 >= 0:
            
            # Compare the largest remaining elements of both arrays
            if nums1[p1] > nums2[p2]:
                # If nums1's element is larger, place it at index p
                nums1[p] = nums1[p1]
                p1 -= 1   # Move p1 backward
            else:
                # Otherwise place nums2's element at index p
                nums1[p] = nums2[p2]
                p2 -= 1   # Move p2 backward
            
            p -= 1   # Move p backward for next placement
        
        # If nums2 still has remaining elements, copy them
        # (If p1 has remaining, they are already in correct place)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
