# ✅ LeetCode 844: Backspace String Compare
# 🔍 Problem Summary

# You are given two strings s and t.

# # means backspace → it deletes the character before it.

# Return True if both strings become equal after processing all backspaces.

# 🧠 Intuition

# You can solve it with:

# Approach 1 — Stack (Simple & Clear)

# Traverse each string.

# Use a stack.

# If character is normal → push it.

# If character is # → pop last character (if stack not empty).

# At the end compare both stacks.

# 💡 Time: O(n)
# 💡 Space: O(n)
# 🧠 Approach 2 — Two Pointers (Optimized)

# Traverse backward counting backspaces, skipping characters accordingly.

# 💡 Time: O(n)
# 💡 Space: O(1)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        # Helper function to process a string and apply backspaces
        def build(final_string):
            stack = []  # Stack to construct the processed string
            
            for char in final_string:
                if char != '#':
                    # Normal character → push into stack
                    stack.append(char)
                else:
                    # Backspace → delete last character if exists
                    if stack:
                        stack.pop()
            
            return stack  # Returns list representing final string

        # Process both strings using stack method
        final_s = build(s)
        final_t = build(t)

        # Compare both results
        return final_s == final_t
