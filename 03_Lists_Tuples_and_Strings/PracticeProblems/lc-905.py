# 🧩 LeetCode 905 — Sort Array by Parity
# 📝 Problem Statement
# Given an integer array nums,
# move all even integers to the beginning of the array followed by all the odd integers.
# You can return any array that satisfies this condition.

class Solution:
    def sortArrayByParity(self,nums:list[int])-> int:
        n = len(nums)# length of the input list
        start = 0# pointer to track the position to place the next even number
        for i in range(n):# iterate through the list
            if nums[i] % 2 == 0:# check if the current element is even
                temp = nums[i]# store the current even element
                nums[i] = nums[start]# swap the current element with the element at the start pointer
                nums[start] = temp# place the even element at the start pointer
                start += 1# move the start pointer to the next position
        return nums# return the modified list
# Example usage:
nums = [3,1,2,4]
sol = Solution()
result = sol.sortArrayByParity(nums)
print(result)  # Output: [2,4,3,1] or any other valid arrangement
