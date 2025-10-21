# 🧩 LeetCode 9: Palindrome Number
# 📘 Problem Statement

# Given an integer x, return true if x is a palindrome, and false otherwise.

# An integer is a palindrome when it reads the same forward and backward.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x # Copy of x to manipulate
        rev = 0# Initialize reversed number to 0
        while temp > 0:# Loop until all digits are processed
            r = temp % 10# Get the last digit
            temp //= 10# Remove the last digit
            rev = rev * 10 + r# Build the reversed number
        return rev == x# Check if reversed number is equal to original number
# Example usage:
solution = Solution()
print(solution.isPalindrome(121))  # Output: True
print(solution.isPalindrome(-121)) # Output: False
print(solution.isPalindrome(10))   # Output: False
print(solution.isPalindrome(12321))# Output: True