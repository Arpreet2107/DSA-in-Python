# ============================================================
#                 🟦 COMPLETE PYTHON SET OPERATIONS
# ============================================================

# -------------------- SET CREATION --------------------
s1 = {1, 2, 3, 4}                    # normal set
s2 = set([1, 2, 3, 3])               # duplicates removed → {1, 2, 3}
s3 = set("hello")                    # set of characters

# -------------------- ADDING ELEMENTS --------------------
s1.add(10)                           # add single element
s1.update([20, 30])                  # add multiple elements
s1.update({40, 50})                  # add elements from another set
s1.update("abc")                     # add from iterable

# -------------------- REMOVING ELEMENTS --------------------
s1.remove(2)                         # removes element, errors if missing
s1.discard(100)                      # removes element, NO error if missing
removed_item = s1.pop()              # remove & return RANDOM element
s1.clear()                           # remove ALL elements

# -------------------- COPY --------------------
copy_set = s1.copy()                 # shallow copy of set

# -------------------- MEMBERSHIP TESTING --------------------
if 3 in {1,2,3}:
    print("3 found in set")

if 10 not in {1,2,3}:
    print("10 not found")

# -------------------- MATHEMATICAL SET OPERATIONS --------------------
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union_set = A | B                    # UNION: {1,2,3,4,5,6}
inter_set = A & B                    # INTERSECTION: {3,4}
diff_set = A - B                     # DIFFERENCE: {1,2}
sym_diff = A ^ B                     # SYMMETRIC DIFFERENCE: {1,2,5,6}

# Using functions
A.union(B)
A.intersection(B)
A.difference(B)
A.symmetric_difference(B)

# -------------------- IN-PLACE SET OPERATIONS --------------------
C = {1, 2, 3}
D = {3, 4}

C.update(D)                          # C = C ∪ D
C.intersection_update(D)             # C = C ∩ D
C.difference_update(D)               # C = C - D
C.symmetric_difference_update(D)     # C = C ^ D

# -------------------- SET RELATIONS --------------------
X = {1, 2}
Y = {1, 2, 3}

X.issubset(Y)                        # True
Y.issuperset(X)                      # True
X.isdisjoint({4,5})                  # True (no common elements)

# -------------------- LENGTH & OTHER OPERATIONS --------------------
length = len(A)                      # size
maximum = max(A)                     # largest value
minimum = min(A)                     # smallest value

# -------------------- SET COMPREHENSION --------------------
squares = {x*x for x in range(5)}    # {0,1,4,9,16}

# -------------------- FROZENSET (IMMUTABLE SET) --------------------
fs = frozenset([1, 2, 3])            # immutable version of set
# fs.add(4) → ERROR (cannot modify frozen set)
