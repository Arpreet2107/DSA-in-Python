# 🧩 Problem — LeetCode 121: Best Time to Buy and Sell Stock
# 📝 Problem Statement
# You are given an array prices where prices[i] is the price of a stock on day i.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve.
# If no profit can be made, return 0.

class Solution:
    def maxProfit(self, prices:list[int])-> int:
        min_price =  prices[0]# initialize the minimum price to the first day's price
        profit=0# initialize the maximum profit to 0
        for i in range(1,len(prices)):# iterate through the list of prices
            curr_profit = prices[i]- min_price# calculate the current profit by subtracting the minimum price from the current day's price
            if curr_profit > profit:# update the maximum profit if the current profit is greater
                profit = curr_profit# update maximum profit
            min_price = min(min_price, prices[i])# update the minimum price if the current day's price is lower
        return profit 
# Example usage:
prices = [7,1,5,3,6,4]
sol = Solution()
result = sol.maxProfit(prices)
print(result)  # Output: 5