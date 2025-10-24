class Solution:
    def fib(self, n:int) -> int:
        #base case
        if n == 0 or n == 1: 
            return n 
        #recursive case
        return self.fib(n-1) + self.lib(n-2)
# Example usage
if __name__ == "__main__":  
    sol = Solution()
    n = 5
    print(f"The {n}th Fibonacci number is:", sol.fib(n))