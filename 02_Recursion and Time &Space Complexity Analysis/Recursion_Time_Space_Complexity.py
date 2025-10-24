# 🧩 DSA in Python - Time and Space Complexity Analysis (Recursion)
# ------------------------------------------------------------------

# 🧠 Concept:
# Time Complexity → Measures how fast an algorithm runs as input size increases.
# Space Complexity → Measures how much memory an algorithm uses.

# Let's compare three recursive functions we've learned:
# 1️⃣ say_hello(n)
# 2️⃣ factorial(n)
# 3️⃣ fibonacci(n)

# --- Example 1: say_hello(n) ---
# say_hello calls itself once per step → Total calls = n
# ✅ Time Complexity = O(n)
# ✅ Space Complexity = O(n)  (because n recursive calls on stack)

def say_hello(n):
    if n == 0:
        return
    say_hello(n - 1)

# --- Example 2: factorial(n) ---
# factorial(n) = n * factorial(n-1)
# Each call makes exactly one recursive call until base case.
# ✅ Time Complexity = O(n)
# ✅ Space Complexity = O(n)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# --- Example 3: fibonacci(n) ---
# fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
# Each call makes two recursive calls → exponential growth.
# ✅ Time Complexity = O(2^n)
# ✅ Space Complexity = O(n)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# --- Example usage ---
if __name__ == "__main__":
    n = 5
    print(f"say_hello({n}) => O(n) time, O(n) space")
    print(f"factorial({n}) => {factorial(n)} | O(n) time, O(n) space")
    print(f"fibonacci({n}) => {fibonacci(n)} | O(2^n) time, O(n) space")
