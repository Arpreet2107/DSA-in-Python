# 🧩 LeetCode 326. Power of Three
# 📘 Problem Statement
# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three if there exists an integer x such that:
# 𝑛 == 3^𝑥

class Solution:
    #iterative approach
    def isPoweOfThree(self,n:int)-> bool:
        if n <= 0:#negative numbers and zero are not powers of three
            return False
        while n % 3 == 0:#check if n is divisible by 3 and not zero
            n //= 3#divide n by 3
        return n == 1#if n becomes 1, then it is a power of three
    #recursive approach
    def recursive_isPowerOfThree(self,n:int)-> bool:
        #base case
        if n <= 0:#negative numbers and zero are not powers of three
            return False
        if n == 1:#if n is 1, it's a power of three
            return True
        if n % 3 != 0:#if n is not divisible by 3, it's not a power of three
            return False
        #recursive case
        return self.recursive_isPowerOfThree(n // 3)#divide n by 3 and check again
    
    # Example usage
if __name__ == "__main__":
    sol = Solution()
    n = int(input("Enter an integer to check if its a power of three or not:"))
    print(f"Is {n} a power of three?:", sol.isPoweOfThree(n))
    print(f"Is {n} a power of three? (recursive):", sol.recursive_isPowerOfThree(n))