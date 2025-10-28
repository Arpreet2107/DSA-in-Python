# =============================================================
# 🔥 Understanding Subarrays, Subsequences & Slicing in Python
# =============================================================

from itertools import combinations

# ======================================
# 🧠 1️⃣ PRINTING ALL SUBARRAYS (Continuous segments)
# ======================================
def print_all_subarrays(arr):
    print("\n📘 ALL SUBARRAYS (Continuous Parts):")
    n = len(arr)
    for start in range(n):
        for end in range(start + 1, n + 1):
            print(arr[start:end])

# ======================================
# 🧠 2️⃣ PRINTING ALL SUBSEQUENCES (Not necessarily continuous)
# ======================================
def print_all_subsequences(arr):
    print("\n📗 ALL SUBSEQUENCES (Non-continuous allowed):")
    n = len(arr)
    subsequences = []
    
    # Using itertools.combinations to generate all subsequences of all lengths
    for length in range(1, n + 1):
        for combo in combinations(arr, length):
            subsequences.append(list(combo))
    
    for seq in subsequences:
        print(seq)

# ======================================
# 🧠 3️⃣ SLICING DEMONSTRATION (Python Built-in)
# ======================================
def slicing_demo(arr):
    print("\n📙 SLICING DEMO:")
    print("Original Array:", arr)
    
    print("arr[1:4]  →", arr[1:4])       # slice from index 1 to 3
    print("arr[:3]   →", arr[:3])        # slice from start to index 2
    print("arr[2:]   →", arr[2:])        # slice from index 2 to end
    print("arr[::2]  →", arr[::2])       # step = 2 (skip alternate)
    print("arr[::-1] →", arr[::-1])      # reverse the array using slicing

# ======================================
# 🧩 MAIN DRIVER FUNCTION
# ======================================
if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print("Original Array:", arr)

    # ✅ Print all subarrays
    print_all_subarrays(arr)

    # ✅ Print all subsequences
    print_all_subsequences(arr)

    # ✅ Demonstrate slicing
    slicing_demo(arr)
