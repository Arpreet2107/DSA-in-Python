# 🧩 Problem — LeetCode 80: Remove Duplicates from Sorted Array II
# 📝 Problem Statement
# You are given a sorted integer array nums.
# Your task is to remove duplicates in-place such that each unique element appears at most twice, and return the number of unique elements left.
# The relative order of the elements should remain the same.
# You must solve it without using extra space (O(1) space).

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if n<= 2:
            return n 
        start = 1
        for i in range(2,n):
            if nums[i] != nums[start-1]:
                start += 1
                nums[start] = nums[i]
        return start + 1
    
