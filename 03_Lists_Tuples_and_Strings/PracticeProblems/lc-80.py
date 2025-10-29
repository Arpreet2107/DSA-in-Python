# 🧩 Problem — LeetCode 80: Remove Duplicates from Sorted Array II
# 📝 Problem Statement
# You are given a sorted integer array nums.
# Your task is to remove duplicates in-place such that each unique element appears at most twice, and return the number of unique elements left.
# The relative order of the elements should remain the same.
# You must solve it without using extra space (O(1) space).

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)# length of the input list
        if n<= 2:# if the length of the list is less than or equal to 2, return the length
            return n # no duplicates to remove
        start = 1# pointer to track the position of unique elements
        for i in range(2,n):# iterate through the list starting from the third element
            if nums[i] != nums[start-1]:# check if the current element is different from the element two positions before
                start += 1# move the pointer to the next position
                nums[start] = nums[i]# update the position with the current unique element
        return start + 1# return the count of unique elements
    
