# ✅ 31. Palindromic Substrings

# Count all palindromic substrings in a string.

# ✔ Expand Around Center — O(n²)
def countSubstrings(s):
    """
    Count all palindromic substrings.
    Expand around each index for odd/even length palindromes.
    """

    def expand(l, r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count

    total = 0
    for i in range(len(s)):
        total += expand(i, i)       # odd
        total += expand(i, i + 1)   # even

    return total
