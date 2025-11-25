# -------------------- HASHING OPERATIONS --------------------

# Python's built-in hash() function
print(hash("Arpreet"))               # hashing a string
print(hash(12345))                   # hashing an integer
print(hash(-98765))                  # hashing a negative integer
print(hash(12.34))                   # hashing a float
print(hash(True))                    # hashing a boolean
print(hash((1, 2, 3)))               # hashing an immutable tuple
print(hash(frozenset([1, 2, 3])))    # hashing a frozenset (hashable set)
print(hash(b"hello"))                # hashing bytes

# ---------------------------------------
# IMMUTABLE vs MUTABLE
# ---------------------------------------

# Immutable objects → hashable
hash("hello")
hash((1, 2, 3))
hash(frozenset([4, 5, 6]))

# Mutable objects → not hashable
# hash([1, 2, 3])             # ❌ TypeError
# hash({"a": 1})              # ❌ TypeError
# hash(set([1, 2]))           # ❌ TypeError

# ---------------------------------------
# CHECK IF AN OBJECT IS HASHABLE
# ---------------------------------------
def is_hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False

print(is_hashable("Arpreet"))        # True
print(is_hashable([1,2,3]))          # False

# ---------------------------------------
# USING HASHING IN SETS (internally used)
# ---------------------------------------
s = {10, 20, 30}
print(10 in s)                       # hashing + equality check

# ---------------------------------------
# USING HASHING IN DICTIONARIES (internally used)
# ---------------------------------------
d = {"name": "Arpreet", "age": 20}
print(d["name"])                     # key is hashed → index found

# ---------------------------------------
# HASH OF A USER-DEFINED CLASS (DEFAULT)
# ---------------------------------------
class A:
    pass

a = A()
print(hash(a))                       # default hash based on object ID

# ---------------------------------------
# CUSTOM OBJECT HASHING
# ---------------------------------------
class Student:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name

    def __hash__(self):
        return hash((self.roll, self.name))   # combine attributes

    def __eq__(self, other):
        return self.roll == other.roll and self.name == other.name

s1 = Student(1, "Arpreet")
s2 = Student(1, "Arpreet")

print(hash(s1))
print(hash(s2))
print(s1 == s2)                                # True

# ---------------------------------------
# COLLISION EXAMPLE (FORCED)
# ---------------------------------------
class X:
    def __hash__(self):
        return 1                               # same hash for all

x1, x2, x3 = X(), X(), X()
myset = {x1, x2, x3}
print(len(myset))                              # 3 elements (handled by chaining)

# ---------------------------------------
# HASH COLLISION IN DICTIONARIES (INTERNAL)
# ---------------------------------------
d = {}
d[1] = "A"
d[1.0] = "B"                                    # 1 and 1.0 have same hash
print(d)                                        # {1: 'B'}

# ---------------------------------------
# HASH MODULO OPERATION (used in real hash tables)
# ---------------------------------------
h = hash("Arpreet")
index = h % 10                                  # bucket index for table size 10
print(index)

# ---------------------------------------
# PERFECT HASHING DEMO (no collision)
# ---------------------------------------
keys = ("a", "b", "c")
perfect_hash = {k: i for i, k in enumerate(keys)}
print(perfect_hash)

# ---------------------------------------
# DOUBLE HASHING (concept demo)
# ---------------------------------------
def h1(key):
    return hash(key) % 10

def h2(key):
    return 7 - (hash(key) % 7)

key = "Arpreet"
print("Primary hash:", h1(key))
print("Secondary (step) hash:", h2(key))
