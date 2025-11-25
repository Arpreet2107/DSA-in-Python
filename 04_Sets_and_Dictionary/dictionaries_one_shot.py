# ============================================================
#            🟨 COMPLETE PYTHON DICTIONARY OPERATIONS
# ============================================================

# -------------------- DICTIONARY CREATION --------------------
d1 = {"name": "Arpreet", "age": 20}
d2 = dict(city="Pune", pin=411014)
d3 = dict([("a", 1), ("b", 2)])               # list of tuples
d4 = {}                                       # empty dictionary
d5 = dict.fromkeys(["id", "price"], 0)        # same value assigned to keys

# -------------------- ACCESSING ELEMENTS --------------------
name = d1["name"]                              # direct access (KeyError if missing)
age = d1.get("age")                            # safe access → returns None
city = d1.get("city", "Not Found")             # default value if missing

# -------------------- ADDING / UPDATING ELEMENTS --------------------
d1["email"] = "test@gmail.com"                 # add key-value
d1.update({"age": 21})                         # update existing
d1.setdefault("gender", "Male")                # add ONLY if key missing

# -------------------- REMOVING ELEMENTS --------------------
d1.pop("age")                                  # remove key & return value
d1.popitem()                                   # removes last inserted pair
del d1["name"]                                 # delete using 'del'
d1.clear()                                     # removes everything

# -------------------- DICTIONARY METHODS --------------------
keys = d2.keys()                               # view object of keys
values = d2.values()                           # view of values
items = d2.items()                             # view of (key, value)

# -------------------- CHECK MEMBERSHIP --------------------
if "city" in d2:
    print("City exists")

if "salary" not in d2:
    print("Salary does not exist")

# -------------------- COPYING --------------------
copy_dict = d2.copy()                          # shallow copy
deep_copy_dict = d2.copy()                      # same for simple dicts

# -------------------- MERGING DICTIONARIES --------------------
dA = {"a": 1, "b": 2}
dB = {"b": 100, "c": 3}
merged = dA | dB                                # Python 3.9+ (new dictionary)
dA |= dB                                        # update dA with dB

# -------------------- DICTIONARY COMPREHENSION --------------------
squares = {x: x*x for x in range(5)}            # 0:0 ... 4:16
even_dict = {x: "even" for x in range(10) if x % 2 == 0}

# -------------------- NESTED DICTIONARY --------------------
student = {
    "name": "Arpreet",
    "subjects": {
        "math": 95,
        "science": 90
    }
}

# accessing nested values
math_marks = student["subjects"]["math"]

# -------------------- ITERATING --------------------
for key in d2:
    print(key)

for key, value in d2.items():
    print(key, value)

# -------------------- DICTIONARY UNPACKING --------------------
def func(a, b, c):
    print(a, b, c)

d_unpack = {"a": 10, "b": 20, "c": 30}
func(**d_unpack)                                # passes dictionary values as arguments

# -------------------- USING DICTIONARY AS A COUNTER --------------------
text = "hello world"
counter = {}

for ch in text:
    counter[ch] = counter.get(ch, 0) + 1        # counting frequency

# -------------------- USING SETDEFAULT IN NESTED DICTS --------------------
data = {}
data.setdefault("users", []).append("Arpreet")  # auto-create list and append

# -------------------- SORTING DICTIONARIES --------------------
sorted_by_key = dict(sorted(dA.items()))        # sort by key
sorted_by_value = dict(sorted(dA.items(), key=lambda x: x[1]))

# -------------------- DICTIONARY LENGTH --------------------
length = len(d1)

# -------------------- CHECKING ALL KEYS / VALUES --------------------
all_keys = list(d1.keys())
all_values = list(d1.values())

# -------------------- REVERSING A DICTIONARY --------------------
rev = {v: k for k, v in d3.items()}             # values become keys
