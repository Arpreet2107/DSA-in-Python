# 🧩 LeetCode 1431: Kids With the Greatest Number of Candies
# 📘 Problem Statement

# You are given an array candies and an integer extraCandies, where:

# candies[i] represents the number of candies the i-th kid has.

# extraCandies is the number of extra candies you can give to any kid.

# Return a boolean array result of the same length as candies where:

# result[i] is True if, after giving the i-th kid all the extraCandies, they have the greatest number of candies among all kids, otherwise False.

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandies = max(candies)  # Find the maximum number of candies any kid has
        ans = []  # Initialize the answer list
        for i in candies: #Iterate through each kid's candies
            if i + extraCandies >= maxCandies: #Check if the kid can have the greatest number of candies
                ans.append(True)  # If yes, append True to the answer list
            else:
                ans.append(False) # If n0, append False to the answer list
        return ans  # Return the final answer list

# Example usage:
solution = Solution()
print(solution.kidsWithCandies([2,3,5,1,3], 3))  # Output: [True, True, True, False, True]
print(solution.kidsWithCandies([4,2,1,1,2], 1))  # Output: [True, False, False, False, False]
print(solution.kidsWithCandies([12,1,12], 10))    # Output: [True, False, True]
print(solution.kidsWithCandies([5,6,2,3,1], 3))   # Output: [True, True, False, False, False]
