# 🧩 LeetCode 1281: Subtract the Product and Sum of Digits of an Integer
# 📘 Problem Statement

# Given an integer n, return the difference between the product of its digits and the sum of its digits.

class Solution:
    def substractProductAndSum(self, n: int) -> int:
        temp = n # Copy of n to manipulate
        sum_ = 0# Initialize sum to 0
        product = 1# Initialize product to 1
        while temp > 0:# Loop until all digits are processed
            r = temp % 10# Get the last digit
            temp //= 10# Remove the last digit
            sum_ += r# Add digit to sum
            product *= r# Multiply digit to product
        return product - sum_# Return the difference between product and sumx``
    
# Example usage:
solution = Solution()
print(solution.substractProductAndSum(234))  # Output: 15
print(solution.substractProductAndSum(4421)) # Output: 21
print(solution.substractProductAndSum(123))  # Output: 0
print(solution.substractProductAndSum(999))  # Output: 972