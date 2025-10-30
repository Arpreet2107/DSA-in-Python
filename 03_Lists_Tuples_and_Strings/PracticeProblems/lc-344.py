# 🧩 Problem — LeetCode 344: Reverse String
# 📝 Problem Statement:
# Write a function that reverses a string in-place.
# You are given a list of characters s.
# You must modify the input array directly (i.e., without creating another array) and do it using O(1) extra memory.

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1

        while i < j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp  # You forgot to assign s[j]
            i += 1
            j -= 1   
# Example Usage:
solution = Solution()
s = ["h", "e", "l", "l", "o"]
solution.reverseString(s)
print(s)  # Output: ["o", "l", "l", "e", "h"]
    