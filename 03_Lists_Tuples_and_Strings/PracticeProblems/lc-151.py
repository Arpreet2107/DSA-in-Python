# 🔢 Problem:
# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters.
# The words in s are separated by one or more spaces.
# Return a string of the words in reverse order, concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words.

class Solution:
    def reverseWords(self, s: str) -> str:
        s = (s.strip()).split()# Split the string into words after stripping leading/trailing spaces
        s.reverse()# Reverse the list of words
        return " ".join(s)# Join the reversed words with a single space
        
# Example Usage:
solution = Solution()
s = "  hello world  "
result = solution.reverseWords(s)
print(result)  # Output: "world hello"
