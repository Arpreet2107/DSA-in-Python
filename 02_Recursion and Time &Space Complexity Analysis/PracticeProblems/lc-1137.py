# 1137. N-th Tribonacci Number
# 🧩 Problem Statement
# The Tribonacci sequence Tn is defined as follows: 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.
# Example 1:
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
# Example 2:
# Input: n = 25
# Output: 1389537

#Iterative case(efficient than the recursive approach)
class Solution:
    def tribonacci(self, n: int) -> int:
        #base case
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        t0,t1,t2 = 0,1,1
        for _ in range(3, n+1):
            t3 = t0 + t1 + t2
            t0, t1, t2 = t1, t2, t3
        return t2

#recursive approach(less efficient due to overlapping subproblems)
    def recursive_tribonacci(self, n: int) -> int:
        #base case
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        #recursive case
        return self.recursive_tribonacci(n-1) + self.recursive_tribonacci(n-2) + self.recursive_tribonacci(n-3)
    # Example usage
if __name__ == "__main__":
    sol = Solution()
    n = 25
    print(f"The {n}th Tribonacci number (iterative) is:", sol.tribonacci(n))
    print(f"The {n}th Tribonacci number (recursive) is:", sol.recursive_tribonacci(n))