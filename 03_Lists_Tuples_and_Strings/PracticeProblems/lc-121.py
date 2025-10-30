# 🧩 Problem — LeetCode 125: Valid Palindrome
# 📝 Problem Statement:
# Given a string s, determine if it is a palindrome, considering only 
# alphanumeric characters (letters and numbers) and ignoring cases (uppercase/lowercase).

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if char.isalnum():          # keep only letters and digits
                cleaned += char.lower() # convert to lowercase
        
        return cleaned == cleaned[::-1] # compare with reverse
# Example usage:
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(solution.isPalindrome("race a car"))                      # Output: False