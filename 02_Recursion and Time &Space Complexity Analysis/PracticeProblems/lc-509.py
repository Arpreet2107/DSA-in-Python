# 🧩 Problem Statement

# The Fibonacci numbers are defined as:

# F(0) = 0

# F(1) = 1

# F(n) = F(n−1) + F(n−2), for n > 1

# Return the n-th Fibonacci number.

# 🧠 Logic Behind the Code

# This is a classic recursion problem.

# For each n, we call the function recursively to calculate fib(n-1) and fib(n-2).

# The recursion continues until the base cases are reached:
# when n == 0 or n == 1.
class Solution:
    def fib(self, n:int) -> int:
        #base case
        if n == 0 or n == 1: 
            return n 
        #recursive case
        return self.fib(n-1)+ self.lib(n-2)
# Example usage
if __name__ == "__main__":  
    sol = Solution()
    n = 5
    print(f"The {n}th Fibonacci number is:", sol.fib(n))