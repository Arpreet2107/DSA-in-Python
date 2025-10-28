# =====================================================
# 🧩 LISTS IN PYTHON — ALL OPERATIONS (ONE SHOT)
# =====================================================

import copy

# ✅ Creating Lists
fruits = ["apple", "banana", "cherry"]
numbers = [4, 1, 7, 3, 9]
mixed = [10, "hello", True, 3.14]

print("\n--- Creating Lists ---")
print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed:", mixed)

# ✅ len() → number of elements
print("\nLength of fruits list:", len(fruits))


# ✅ Accessing elements using indexing
print("First fruit:", fruits[0])
print("Last fruit using negative index:", fruits[-1]) # Negative indexing

# ✅ Slicing
print("\n--- Slicing ---")
print("First two fruits:", fruits[0:2])
print("All fruits except first:", fruits[1:])
print("Alternate fruits:", fruits[::2])

# ✅ Adding Elements
fruits.append("mango") # adds to the end
print("After append:", fruits)

fruits.extend(["grape", "kiwi"]) # adds multiple elements
print("After extend:", fruits)

fruits.insert(2, "orange") # adds at index 2
print("After insert:", fruits)

# ✅ Removing Elements
fruits.remove("banana") # removes first occurrence of value
print("After remove:", fruits)

popped_item = fruits.pop() # removes last element and returns it
print("Popped Item:", popped_item)
print("After pop:", fruits)

# ✅ clear() → removes all elements
temp = [1, 2, 3]
temp.clear()
print("After clear:", temp)

# ✅ min(), max(), sum()
print("Min in numbers:", min(numbers))
print("Max in numbers:", max(numbers))
print("Sum of numbers:", sum(numbers))

# ✅ count() → returns number of times an element appears
nums = [1, 2, 2, 3, 3, 3]
print("Count of 3:", nums.count(3))

# ✅ index() → returns index of first occurrence
print("Index of first 7 in numbers:", numbers.index(7))

# ✅ sort() → sorts list in ascending order (modifies original list)
numbers.sort()
print("Sorted numbers (ascending):", numbers)

# ✅ sort(reverse=True) → descending order
numbers.sort(reverse=True)
print("Sorted numbers (descending):", numbers)

# ✅ copy() & deepcopy()
copy_fruits = fruits.copy()
deep_copy_nested = copy.deepcopy([[1, 2], [3, 4]])
print("\nCopied list:", copy_fruits)
print("Deep copy (nested):", deep_copy_nested)

# ✅ count(), index()
nums = [1, 2, 2, 3, 3, 3]
print("\nCount of 3:", nums.count(3))
print("Index of first 7:", numbers.index(7))

# ✅ sort(), reverse(), sorted()
numbers.sort()
print("\nSorted (ascending):", numbers)
numbers.sort(reverse=True)
print("Sorted (descending):", numbers)
numbers.reverse()
print("Reversed (in-place):", numbers)
print("New sorted list (without changing original):", sorted(numbers))

# ✅ del keyword
del fruits[0] # delete first element
print("\nAfter deleting first element:", fruits)
# ✅ Iterating through List
for fruit in fruits:
    print("Fruit:", fruit)

# ✅ Iteration & enumerate()
print("\n--- Iteration ---")
for index, fruit in enumerate(fruits):
    print(f"Index {index} -> {fruit}")

# ✅ Checking membership
print("Is 'apple' in fruits?", "apple" in fruits)
print("Is 'papaya' not in fruits?", "papaya" not in fruits)

# ✅ List concatenation (+)
list1 = [1, 2, 3]
list2 = [4, 5]
merged = list1 + list2
print("Merged List:", merged)

# ✅ Repetition (*)
print("Repeat list1 three times:", list1 * 3)

# ✅ Nested Lists
nested = [[1, 2], [3, 4], [5, 6]]
print("Nested List:", nested)
print("Access 4 from nested list:", nested[1][1])

# ✅ List Comprehension
squares = [x**2 for x in range(1, 6)]
print("\nSquares using comprehension:", squares)

# ✅ any() and all()
bools = [True, True, False]
print("\nany(bools):", any(bools)) # True if any True
print("all(bools):", all(bools)) # True only if all True

# ✅ zip() → combine multiple lists
names = ["A", "B", "C"]
marks = [90, 85, 95]
combined = list(zip(names, marks))
print("\nZipped list:", combined)

# ✅ list() constructor
from_tuple = list((1, 2, 3))
from_string = list("hello")
print("\nFrom tuple:", from_tuple)
print("From string:", from_string)

# ✅ map() and filter()
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
even = list(filter(lambda x: x % 2 == 0, nums))
print("\nSquared using map:", squared)
print("Even numbers using filter:", even)