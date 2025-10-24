# 🧩 LeetCode 231. Power of Two
# 📘 Problem Statement

# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two if there exists an integer x such that:
# 𝑛 = 2^𝑥
class Solution:
    def isPowerOfTwo(self, n : int)-> bool:
        while n % 2 == 0 and n != 0:#check if n is divisible by 2 and not zero
            n //= 2#divide n by 2
        return n == 1#if n becomes 1, then it is a power of two
    #recursive approach
    def recursive_isPowerOfTwo(self, n: int) -> bool:
        #base case
        if n <= 0:#negative numbers and zero are not powers of two
            return False
        if n == 1 or n % 2 != 0:#if n is 1, it's a power of two; if n is odd and greater than 1, it's not
            return False
        #recursive case
        return self.recursive_isPowerOfTwo(n // 2)#divide n by 2 and check again
# Example usage
if __name__ == "__main__":
    sol = Solution()
    n = int(input("Enter an integer to check if its a power of two or not:"))
    print(f"Is {n} a power of two?:", sol.isPowerOfTwo(n))
    print(f"Is {n} a power of two? (recursive):", sol.recursive_isPowerOfTwo(n))