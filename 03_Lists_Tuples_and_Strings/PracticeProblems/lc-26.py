# 🧩 Problem — LeetCode 26: Remove Duplicates from Sorted Array
# 📝 Problem Statement

# You are given a sorted array nums.
# Your task is to remove duplicates in-place such that each unique element appears only once.

# You must modify the array without using extra space and return the number of unique elements.

class Solution:
    def removeDuplicates(self,nums:list[int])->int:# function to remove duplicates from a sorted list
        n = len(nums)# length of the input list
        start = 0# pointer to track the position of unique elements
        for i in range(1,n):# iterate through the list starting from the second element
            #unique elements 
            if nums[i] != nums[start]:# check if the current element is different from the last unique element
                start += 1# move the pointer to the next position
                nums[start] = nums[i]# update the position with the current unique element
        return start + 1# return the count of unique elements

#Example usage:
nums = [1,1,2]
sol = Solution()
length = sol.removeDuplicates(nums)
print(length)  # Output: 2
