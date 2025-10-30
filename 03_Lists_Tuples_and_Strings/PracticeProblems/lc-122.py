# 🧩 Problem — LeetCode 122: Best Time to Buy and Sell Stock II
# 📝 Problem Statement
# You are given an array prices where
# prices[i] = price of a stock on the i-th day.
# You can buy and sell the stock multiple times — but:
# You must sell before buying again.
# You can make as many transactions as you like.
# Return the maximum profit you can achieve.

class Solution:
    def maxProfit(self, prices:list[int])-> int:
        profit = 0# initialize the maximum profit to 0
        n = len(prices)# length of the input list
        for i in range(n-1):# iterate through the list of prices
            if prices[i+1] > prices[i]:# check if selling on the next day is profitable
                profit += prices[i+1]- prices[i]# add the profit from this transaction
        return profit# return the total maximum profit
# Example usage:
prices = [7,1,5,3,6,4]
sol = Solution()
result = sol.maxProfit(prices)
print(result)  # Output: 7
