# 🧩 Problem — LeetCode 1672: Richest Customer Wealth
# 📝 Problem Statement
# You are given a 2D list accounts where:
# accounts[i][j] represents the amount of money the i-th customer has in the j-th bank.
# Return the wealth that the richest customer has.
# A customer’s wealth is the sum of money across all their bank accounts.

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        ans = 0
        for account in accounts:
            ans = max(ans,sum(account))
        return ans

# Example usage:
accounts = [[1,2,3],[3,2,1]]
sol = Solution()
result = sol.maximumWealth(accounts)
print(result)  # Output: 6