# 🧩 DSA in Python - Sum of First N Natural Numbers using Recursion
# -----------------------------------------------------------------

# 🧠 Concept:
# The sum of first n natural numbers = 1 + 2 + 3 + ... + n

def sum_n(n):
    # Base Case: sum of first 0 numbers is 0
    if n == 0:
        return 0
    
    # Recursive Case: sum(n) = n + sum(n - 1)
    return n + sum_n(n - 1)

# Example usage
if __name__ == "__main__":
    print("Sum of first 5 natural numbers is:", sum_n(5))
