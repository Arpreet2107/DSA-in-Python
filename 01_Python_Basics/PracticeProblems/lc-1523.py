# 🧩 LeetCode 1523. Count Odd Numbers in an Interval Range
# 📘 Problem Statement
# Given two non-negative integers low and high, return the count of odd numbers between them (inclusive).

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        #Method 1: Using arithmetic properties
        return (high + 1) // 2 - low // 2
        #Method 2: Using conditional checks
        if low % 2 == 0 and high % 2 == 0:
            return (high - low) // 2
        else:
            return (high - low) // 2 + 1
# Example usage:
sol = Solution()  
print(sol.countOdds(3, 7))  # Output: 3
print(sol.countOdds(8, 10)) # Output: 1
