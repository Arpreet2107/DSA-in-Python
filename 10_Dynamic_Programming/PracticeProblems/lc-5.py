# # ✅ LeetCode 5 — Longest Palindromic Substring (Python + Full Explanation)
# # 🧠 Problem Summary

# # Given a string s, return the longest palindromic substring inside it.

# # 🟦 🔥 Fully Commented Python Code (Line-by-Line Explained)
# 🧠 Explanation (Simple & Crystal Clear)
# ✔ What is a palindrome?

# A string that reads the same forward & backward
# Example: "abba", "racecar"

# ✔ Why expand around center?

# Instead of checking all substrings (O(n³)), we check palindromes centered at every index → O(n²).

# For each index:

# Expand for odd length: center at i

# Expand for even length: center at i & i+1

# Keep expanding while letters match.

# ✔ Why does this work?

# Because every palindrome has a center (either a single char or a pair).
# We just explore every possible center.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        We find the longest palindrome by expanding around each index.
        A palindrome can be:
        1) Odd length: center at one character   (e.g., "racecar")
        2) Even length: center between two chars (e.g., "abba")
        """

        # If the string has length 0 or 1, return it immediately
        if len(s) <= 1:
            return s

        # Helper function to expand around the given left and right pointers
        def expand(left: int, right: int) -> str:
            # Expand while inside bounds and characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # When mismatched, substring (left+1 ... right-1) is the palindrome
            return s[left + 1:right]

        # Variable to store the best palindrome found so far
        longest = ""

        # Try expanding around every index in the string
        for i in range(len(s)):

            # Case 1: Odd-length palindrome (center at i)
            odd_pal = expand(i, i)

            # Case 2: Even-length palindrome (center between i and i+1)
            even_pal = expand(i, i + 1)

            # Select the longest among odd, even, and previous answer
            if len(odd_pal) > len(longest):
                longest = odd_pal
            if len(even_pal) > len(longest):
                longest = even_pal

        return longest
