# =====================================================
# 🧩 TUPLES IN PYTHON — ALL OPERATIONS (ONE SHOT)
# =====================================================

from collections import namedtuple
import sys

# ✅ Creating Tuples
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ("apple", "banana", "cherry")
mixed_tuple = (1, "hello", 3.14, True)

print("Tuple1:", tuple1)
print("Tuple2:", tuple2)
print("Mixed Tuple:", mixed_tuple)

# ✅ Length of tuple
print("Length of tuple1:", len(tuple1))

# ✅ Accessing elements (Indexing)
print("First element:", tuple1[0])
print("Last element (Negative Index):", tuple1[-1])

# ✅ Slicing (like lists)
print("First three elements:", tuple1[:3])
print("Elements from index 2 to 4:", tuple1[2:5])
print("Alternate elements:", tuple1[::2])
print("Reversed tuple:", tuple1[::-1])

# ✅ count() → counts occurrences of an element
sample = (1, 2, 2, 3, 3, 3)
print("Count of 3:", sample.count(3))

# ✅ index() → returns index of first occurrence
print("Index of first 2:", sample.index(2))

# ✅ Concatenation (+)
tuple3 = (6, 7, 8)
merged = tuple1 + tuple3
print("Merged Tuple:", merged)

# ✅ Repetition (*)
print("Repeated Tuple:", tuple2 * 2)

# ✅ Membership Testing (in, not in)
print("Is 3 in tuple1?", 3 in tuple1)
print("Is 10 not in tuple1?", 10 not in tuple1)

# ✅ Iteration
print("Iterating through tuple1:")
for item in tuple1:
    print(item, end=" ")
print()

# ✅ Unpacking Tuples
person = ("Arpreet", 22, "CSE")
name, age, branch = person
print(f"Name: {name}, Age: {age}, Branch: {branch}")

# ✅ Nested Tuples
nested = ((1, 2), (3, 4), (5, 6))
print("Nested Tuple:", nested)
print("Access element 4:", nested[1][1])

# ✅ Tuple Comparison
print("(1, 2, 3) < (1, 2, 4)?", (1, 2, 3) < (1, 2, 4))

# ✅ any() & all()
bool_tuple = (True, True, False)
print("any(bool_tuple):", any(bool_tuple))  # True if any element is True
print("all(bool_tuple):", all(bool_tuple))  # True if all elements are True

# ✅ enumerate() → iterate with index
for index, value in enumerate(tuple2):
    print(f"Index {index}: {value}")

# ✅ Tuple as Dictionary Key (Immutable property)
points = {(1, 2): "A", (3, 4): "B"}
print("Accessing dictionary using tuple key:", points[(1, 2)])

# ✅ min(), max(), sum()
nums = (10, 20, 5, 15)
print("Min:", min(nums))
print("Max:", max(nums))
print("Sum:", sum(nums))

# ✅ Using sorted() (returns list, not tuple)
sorted_nums = sorted(nums)
print("Sorted tuple as list:", sorted_nums)

# ✅ Convert between list and tuple
list_from_tuple = list(tuple1)
tuple_from_list = tuple(list_from_tuple)
print("List from Tuple:", list_from_tuple)
print("Tuple from List:", tuple_from_list)

# ✅ Memory efficiency of tuples vs lists
list_ex = [1, 2, 3, 4, 5]
tuple_ex = (1, 2, 3, 4, 5)
print("Size of list:", sys.getsizeof(list_ex), "bytes")
print("Size of tuple:", sys.getsizeof(tuple_ex), "bytes")

# ✅ Named Tuple (from collections)
Student = namedtuple("Student", ["name", "age", "roll"])
s1 = Student("Arpreet", 22, 22052804)
print(f"NamedTuple - Name: {s1.name}, Roll: {s1.roll}")

# ✅ Tuple comprehension equivalent (actually returns a generator)
gen = (x**2 for x in range(5))
print("Generator from tuple comprehension equivalent:", list(gen))
