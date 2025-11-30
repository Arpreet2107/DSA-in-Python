# ✅ LeetCode 20: Valid Parentheses
# Problem Statement

# Given a string s containing just the characters '(' , ')' , '{' , '}' , '[' , ']',
# determine if the input string is valid.

# A string is valid if:

# Open brackets must be closed by the same type of brackets.

# Open brackets must be closed in the correct order.
# LeetCode 20: Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to hold opening brackets
        stack = []

        # Mapping of closing brackets to opening brackets
        pair = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        # Traverse each character in the string
        for ch in s:
            # If it's an opening bracket, push to stack
            if ch in "([{":
                stack.append(ch)
            else:
                # If stack is empty OR top of stack does not match, invalid
                if not stack or stack[-1] != pair[ch]:
                    return False
                # If matched, pop the opening bracket
                stack.pop()

        # If stack is empty → all brackets properly closed
        return len(stack) == 0


# ---------------- MAIN FUNCTION (For running locally) ----------------

if __name__ == "__main__":
    sol = Solution()

    # Test cases
    test_cases = [
        "()",        # True
        "()[]{}",    # True
        "(]",        # False
        "([)]",      # False
        "{[]}",      # True
        "((()))",    # True
        "((())"      # False
    ]

    for s in test_cases:
        print(f"Input: {s}, Is Valid? {sol.isValid(s)}")
