# fib509.py — line-by-line commented, readable, production-friendly
#!/usr/bin/env python3
# fib509.py
# LeetCode 509: Fibonacci Number
# This file implements a fast iterative solution (O(n) time, O(1) space)
# and includes a small test harness for local verification.

def fib(n: int) -> int:
    """
    Return the n-th Fibonacci number.
    Fibonacci sequence:
      F(0) = 0
      F(1) = 1
      F(n) = F(n-1) + F(n-2) for n >= 2
    We implement an iterative solution to avoid recursion depth and to be optimal in space.
    """
    # If n is 0, the answer is 0 by definition.
    if n == 0:
        return 0  # base case: F(0) = 0

    # If n is 1, the answer is 1 by definition.
    if n == 1:
        return 1  # base case: F(1) = 1

    # prev holds F(i-2) initially set to F(0) = 0
    prev = 0  # F(0)
    # curr holds F(i-1) initially set to F(1) = 1
    curr = 1  # F(1)

    # Loop from 2 up to n (inclusive) computing successive Fibonacci numbers.
    # On each iteration:
    #   next_val = F(i-1) + F(i-2)
    #   then shift prev <- curr, curr <- next_val
    for i in range(2, n + 1):
        # compute next Fibonacci number
        next_val = prev + curr  # F(i) = F(i-1) + F(i-2)
        # shift for next iteration
        prev = curr             # new F(i-2) becomes old F(i-1)
        curr = next_val         # new F(i-1) becomes F(i)
        # (loop continues until i == n)

    # After loop, curr holds F(n)
    return curr


# ------ Simple test harness (runs when file executed directly) ------
if __name__ == "__main__":
    # Some sample inputs & expected outputs to quickly verify the function:
    tests = [
        (0, 0),  # F(0) -> 0
        (1, 1),  # F(1) -> 1
        (2, 1),  # F(2) -> 1
        (3, 2),  # F(3) -> 2
        (4, 3),  # F(4) -> 3
        (5, 5),  # F(5) -> 5
        (10, 55) # F(10) -> 55
    ]

    # Loop through tests, run fib(), and print results neatly
    for n, expected in tests:
        result = fib(n)  # call the implemented function
        status = "PASS" if result == expected else "FAIL"
        # Print the test case, expected, result, and status
        print(f"fib({n}) = {result}  (expected: {expected}) -> {status}")
