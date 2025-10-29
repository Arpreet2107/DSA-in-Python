# 💡 Problem Statement:
# Given an array nums, return the running sum of nums.
# The running sum is defined as:
# runningSum[i] = sum(nums[0] + nums[1] + ... + nums[i])
# 🧩 Example
# Input:
# nums = [1, 2, 3, 4]
# Output:
# [1, 3, 6, 10]
# Explanation:
# runningSum[0] = 1
# runningSum[1] = 1 + 2 = 3
# runningSum[2] = 1 + 2 + 3 = 6
# runningSum[3] = 1 + 2 + 3 + 4 = 10

def runningSum(self,nums:list[int]) -> list[int]:# function to calculate the running sum of a list
    n = len(nums)# length of the input list
    ans = []# initialize an empty list to store the running sums
    ans.append(nums[0])# append the first element of nums to ans
    for i in range(1,n):# iterate from the second element to the last element
        x = (ans[i-1] + nums[i])# append the sum of the previous running sum and the current element to ans
        ans.append(x)
    return ans 
# Example usage:
nums = [1, 2, 3, 4]
print(runningSum(None, nums))  # Output: [1, 3, 6, 10]

