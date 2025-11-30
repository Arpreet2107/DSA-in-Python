# 🔥 LeetCode 496 — Next Greater Element I
# ✅ Problem Summary

# You are given two arrays:

# nums1 is a subset of nums2

# For each element in nums1, you must find its next greater element in nums2

# The next greater element is the first element to the right that is greater

# If no such element exists → return -1

# 🧠 Intuition

# The problem becomes easy if we notice:

# For each number in nums2, we want to know its next greater element

# We can compute this using a Monotonic Decreasing Stack

# 🔹 Why Monotonic Stack?

# We traverse nums2

# Keep a stack of numbers in decreasing order

# If current number is greater than the top of the stack:
# → it is the next greater element

# Pop from stack and map that popped value to the current number

# This gives O(n) efficiency.
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # Dictionary to store: number -> next greater number
        next_greater = {}

        # Stack to maintain decreasing order
        stack = []

        # Traverse nums2 to fill the next_greater map
        for num in nums2:

            # While the current number is greater than the stack top
            # It means current number is the next greater element
            while stack and num > stack[-1]:
                top = stack.pop()
                next_greater[top] = num
            
            # Push current number into stack
            stack.append(num)

        # Numbers left in stack have no next greater element
        for remaining in stack:
            next_greater[remaining] = -1
        
        # Build answer for nums1 using the prepared dictionary
        return [next_greater[num] for num in nums1]
