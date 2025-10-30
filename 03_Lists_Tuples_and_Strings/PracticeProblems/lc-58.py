# 🧩 Problem — LeetCode #58: Length of Last Word
# Question:
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()# Remove leading and trailing spaces
        n = len(s)# Get the length of the trimmed string
        i = -1# Start from the end of the string
        while i >= (-1*n) and s[i]!=" ":# Traverse backwards until a space is found
            i-=1# Move to the previous character
        i+=1# Adjust index to the start of the last word
        i*=-1# Convert to positive length
        return i# Return the length of the last word
# Example Usage:
solution = Solution()
s = "   fly me   to   the moon  "
result = solution.lengthOfLastWord(s)
print(result)  # Output: 4
