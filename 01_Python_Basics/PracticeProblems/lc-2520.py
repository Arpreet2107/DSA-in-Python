# 🧩 LeetCode 2520. Count the Digits That Divide a Number
# 📘 Problem Statement

# Given an integer num, return the number of digits in num that divide num.

# An integer val divides num if num % val == 0.

class Solution:
    def countDigits(self,num:int) -> int:
        temp = num # Copy of num to manipulate
        ans = 0 # Initialize answer to 0
        while temp > 0: # Loop until all digits are processed
            r = temp % 10# Get the last digit
            if r  != 0 and num % r == 0:# Check if digit divides num
                ans += 1# Increment answer
            temp //= 10# Remove the last digit
        return ans# Return the final count of digits that divide num
    
# Example usage:
solution = Solution()
print(solution.countDigits(121))  # Output: 2
print(solution.countDigits(123))  # Output: 2
print(solution.countDigits(7))    # Output: 1
print(solution.countDigits(1012)) # Output: 3