# 🧩 LeetCode 1365. How Many Numbers Are Smaller Than the Current Number
# 📘 Problem Statement

# Given the array nums, for each nums[i], find out how many numbers in the array are smaller than it.
# That is, for each nums[i], you need to count the number of valid j such that j != i and nums[j] < nums[i].

# Return the answer as an array.

class Solution:
    def smallerNumbersThanCurrent(self, nums:list[int]) -> list[int]:
        ans = []
        for i in nums:
            c=0
            for j in nums:
                if j<i:
                    c+=1
            ans.append(c)
        return ans            
    #Example usage:
sol = Solution()
print(sol.smallerNumbersThanCurrent([8,1,2,2,3]))  # Output: [4,0,1,1,3]
print(sol.smallerNumbersThanCurrent([6,5,4,8]))    # Output: [2,1,0,3]
print(sol.smallerNumbersThanCurrent([7,7,7,7]))    # Output: [0,0,0,0]