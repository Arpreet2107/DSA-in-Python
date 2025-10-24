# 🧩 DSA in Python - Recursion Basics
# ----------------------------------

# 🧠 What is Recursion?
# Recursion is when a function calls itself to solve smaller parts of a larger problem.

# Example 1: Simple Recursive Function
def say_hello(n):
    # Base case - stop when n == 0
    if n == 0:
        return
    print("Hello", n)
    say_hello(n - 1)  # Recursive call

# Example usage
if __name__ == "__main__":
    say_hello(3)
