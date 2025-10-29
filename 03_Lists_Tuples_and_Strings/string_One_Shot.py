# ====================================================
# 🧠 STRING OPERATIONS IN PYTHON — COMPLETE ONE-SHOT 
# =====================================================

# ======================================
# 1️⃣ STRING CREATION, LENGTH, INDEXING
# ======================================
# Strings are immutable sequences of characters.
# You can access individual characters using indexes.
s = "Hello World"
print("Original String:", s)
print("Length:", len(s))                   # length of string
print("First Character:", s[0])            # indexing starts from 0
print("Last Character (Negative Indexing):", s[-1])  # -1 means last element

# ======================================
# 2️⃣ SLICING
# ======================================
# Extract substring using [start:end:step]
print("\n📘 STRING SLICING:")
print("s[0:5] →", s[0:5])     # characters 0 to 4
print("s[6:] →", s[6:])       # from 6th index to end
print("s[:5] →", s[:5])       # from start to 4th index
print("s[::-1] →", s[::-1])   # reversed string
print("s[::2] →", s[::2])     # every 2nd character

# ======================================
# 3️⃣ CASE CONVERSION METHODS
# ======================================
# Changing the letter case of strings
text = "  python programming is fun!  "
print("\n📗 CASE METHODS:")
print("Original:", repr(text))
print("upper() →", text.upper())             # converts to uppercase
print("lower() →", text.lower())             # converts to lowercase
print("capitalize() →", text.capitalize())   # capitalizes first letter
print("title() →", text.title())             # capitalizes first letter of every word
print("swapcase() →", text.swapcase())       # swaps uppercase/lowercase
print("casefold() →", "Straße".casefold())   # aggressive lower() for comparison

# ======================================
# 4️⃣ STRIP, REPLACE, COUNT, FIND, INDEX
# ======================================
# Cleaning and searching text
print("\n📙 COMMON STRING METHODS:")
print("strip() →", text.strip())                          # removes spaces from both ends
print("replace('fun', 'awesome') →", text.replace("fun", "awesome"))  # replaces substring
print("count('n') →", text.count('n'))                     # counts occurrences of 'n'
print("find('Python') →", text.find("Python"))             # returns index or -1
print("rfind('n') →", text.rfind('n'))                     # finds last occurrence 
print("index('programming') →", text.index("programming")) # same as find() but raises error if not found
print("rindex('is') →", text.rindex("is"))                 # last index of substring

# ======================================
# 5️⃣ STARTSWITH & ENDSWITH
# ======================================
# Used for pattern checking
print("\n📘 STARTSWITH / ENDSWITH:")
phrase = "Machine Learning with Python"
print("startswith('Machine') →", phrase.startswith("Machine"))
print("endswith('Python') →", phrase.endswith("Python"))

# ======================================
# 6️⃣ SPLIT & JOIN
# ======================================
# split() breaks a string into list; join() combines list into string
print("\n📗 SPLIT & JOIN:")
words = phrase.split()
print("split() →", words)
print("'-'.join(words) →", "-".join(words))

# ======================================
# 7️⃣ STRING JUSTIFICATION
# ======================================
# Aligning text in formatted outputs
print("\n📙 JUSTIFY METHODS:")
msg = "Python"
print("ljust(15, '-') →", msg.ljust(15, '-'))  # left align with '-'
print("rjust(15, '-') →", msg.rjust(15, '-'))  # right align with '-'
print("center(15, '*') →", msg.center(15, '*'))# center align

# ======================================
# 8️⃣ MEMBERSHIP & COMPARISON
# ======================================
# Checking existence or comparing strings
print("\n📘 MEMBERSHIP & COMPARISON:")
a, b = "apple", "banana"
print("'app' in a →", 'app' in a)         # True if substring exists
print("'z' not in b →", 'z' not in b)     # True if not found
print("a == b →", a == b)                 # equality check
print("a < b (lexicographical) →", a < b) # alphabetic order comparison

# ======================================
# 9️⃣ STRING CHECK METHODS
# ======================================
# Used to check the type of content inside strings
print("\n📗 STRING CHECK METHODS:")
check = "Python3"
print("isalnum() →", check.isalnum())           # letters or digits only
print("isalpha() →", "Python".isalpha())        # alphabets only
print("isdigit() →", "123".isdigit())           # digits only
print("islower() →", "python".islower())        # all lowercase
print("isupper() →", "PYTHON".isupper())        # all uppercase
print("isspace() →", "   ".isspace())           # spaces only
print("istitle() →", "Python Is Fun".istitle()) # title case check
print("isascii() →", "Hello".isascii())         # ASCII characters only
print("isdecimal() →", "123".isdecimal())       # decimal digits
print("isidentifier() →", "variable_name".isidentifier()) # valid variable name
print("isprintable() →", "Hello!".isprintable()) # printable characters only

# ======================================
# 🔟 STRING FORMATTING
# ======================================
# Formatting dynamic text using different techniques
print("\n📙 STRING FORMATTING:")
name, age = "Arpreet", 22
print("f-string →", f"My name is {name} and I am {age}.")     # modern way
print("format() →", "My name is {} and I am {}.".format(name, age))  # positional
print("% formatting →", "My name is %s and I am %d." % (name, age))  # old-school
print("format_map() →", "{name} is {age} years old.".format_map({'name': 'Arpreet', 'age': 22}))  # mapping dict

# ======================================
# 11️⃣ PREFIX & SUFFIX REMOVAL
# ======================================
# Removes fixed prefix/suffix from strings
print("\n📘 PREFIX & SUFFIX REMOVAL:")
word = "unbelievable"
print("removeprefix('un') →", word.removeprefix("un"))
print("removesuffix('able') →", word.removesuffix("able"))

# ======================================
# 12️⃣ TRANSLATION & ENCODING
# ======================================
# Used for encryption, text encoding, or replacing patterns
print("\n📗 TRANSLATION & ENCODING:")
table = str.maketrans("aeiou", "12345")      # create translation table
translated = "Hello World".translate(table)   # replace vowels with numbers
print("maketrans() + translate() →", translated)

encoded = "Python".encode("utf-8")            # convert to bytes
print("encode('utf-8') →", encoded)
print("decode('utf-8') →", encoded.decode("utf-8"))  # decode back to string

# ======================================
# 13️⃣ ITERATION & IMMUTABILITY
# ======================================
# Strings are immutable, cannot modify in-place
print("\n📙 ITERATION & IMMUTABILITY:")
for ch in "DATA":    # iterate through string
    print(ch, end=" ")
print()

try:
    s[0] = 'h'       # will raise error
except TypeError as e:
    print("Error (immutability):", e)

# ======================================
# 14️⃣ ADVANCED & MISCELLANEOUS
# ======================================
# Extra helpful utilities for text processing
print("\n📘 ADVANCED METHODS:")
print("expandtabs() →", "Hello\tWorld".expandtabs(10))  # tab to spaces
print("splitlines() →", "Line1\nLine2\nLine3".splitlines())  # split by newlines
print("zfill(10) →", "42".zfill(10))                   # pad numbers with zeros

# ======================================
# 🧩 SUMMARY
# ======================================
print("\n✅ String operations covered →")
print("Creation, Indexing, Slicing, Concatenation, Methods, Split/Join,")
print("Formatting, Comparison, Iteration, Immutability, Advanced methods")
print("All helper methods like encode(), decode(), translate(), maketrans(),")
print("rfind(), rindex(), rjust(), ljust(), format_map(), casefold(),")
print("removeprefix(), removesuffix(), and all is*() methods included ✅")

# =============================================================
# END OF FILE
# =============================================================
