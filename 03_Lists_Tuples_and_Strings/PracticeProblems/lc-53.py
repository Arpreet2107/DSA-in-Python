# 🧩 Problem — LeetCode 53: Maximum Subarray
# 📝 Problem Statement
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.
# Example:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4] 
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution:
    def maxSubArray(self,nums:list[int])-> int:
        curr_sum = 0# initialize current sum to 0
        max_sum = nums[0]# initialize max sum to the first element of the list
        for i in range(len(nums)):# iterate through the list
            curr_sum += nums[i]# add the current element to the current sum
            if curr_sum > max_sum:# update max sum if current sum is greater
                max_sum = curr_sum # update max sum
            if curr_sum < 0:# reset current sum to 0 if it becomes negative
                curr_sum = 0# reset current sum
        return max_sum# return the maximum subarray sum
# Example usage:    
nums = [-2,1,-3,4,-1,2,1,-5,4]
sol = Solution()
result = sol.maxSubArray(nums)
print(result)  # Output: 6
