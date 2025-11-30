# 🔥 LeetCode 503 — Next Greater Element II (Circular Array)
# ✅ Problem Summary

# Given a circular array nums, you must find the next greater element for each index.

# You look to the right for the first larger number

# Since the array is circular, if you reach the end, continue from the start

# If no greater number exists → return -1

# 🧠 Intuition — How to handle circular array?

# For Next Greater Element in a normal array, we use a Monotonic Stack.

# But here, the array wraps around.

# 🔥 Trick:

# Traverse the array twice (simulate circular behavior):
# nums = [1, 2, 1]

# Extended traversal indexes:
# 0 1 2 0 1 2
# Use i % n to wrap around

# Maintain a decreasing stack storing indexes whose next greater element we haven't found yet

# Time Complexity → O(n)
# Space Complexity → O(n)
class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        
        # Result array initialized with -1 (default if no greater element found)
        result = [-1] * n
        
        # Stack will store indices of nums[] whose next greater we haven't found yet
        stack = []
        
        # Traverse array twice to simulate circular array
        for i in range(2 * n):
            current = nums[i % n]   # Circular index using modulo
            
            # If current number is greater than the number at stack top index
            # Then current is the next greater element
            while stack and nums[stack[-1]] < current:
                top_index = stack.pop()     # Pop index
                result[top_index] = current # Update its next greater
            
            # Only push indices from the FIRST pass
            if i < n:
                stack.append(i)
        
        return result
