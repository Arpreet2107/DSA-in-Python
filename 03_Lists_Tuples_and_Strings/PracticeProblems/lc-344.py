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
        i = 0# Initialize the start pointer
        j = len(s) - 1# Initialize the end pointer

        while i < j:# Loop until the two pointers meet
            temp = s[i]# Store the value at the start pointer
            s[i] = s[j]# Assign the value at the end pointer to the start pointer
            s[j] = temp  # Assign the stored value to the end pointer
            i += 1# Move the start pointer forward
            j -= 1   # Move the end pointer backward
# Example Usage:
solution = Solution()
s = ["h", "e", "l", "l", "o"]
solution.reverseString(s)
print(s)  # Output: ["o", "l", "l", "e", "h"]
    