# 🧩 DSA in Python - Factorial using Recursion
# --------------------------------------------

# 🧠 Concept:
# Factorial of n (written as n!) is the product of all positive integers ≤ n.
# Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

def factorial(n):
    # Base Case: factorial(0) = 1
    if n == 0:
        return 1
    
    # Recursive Case: n! = n * (n-1)!
    return n * factorial(n - 1)

# Example usage
if __name__ == "__main__":
    print("Factorial of 5 is:", factorial(5))

