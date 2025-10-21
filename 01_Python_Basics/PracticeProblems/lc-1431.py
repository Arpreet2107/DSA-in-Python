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
    