class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Set to store characters in current window (no duplicates allowed)
        char_set = set()

        # Left pointer of the sliding window
        left = 0
        
        # Maximum length of substring without repeating characters
        max_length = 0

        # Right pointer moves through the string
        for right in range(len(s)):

            # If a duplicate is found, remove characters from left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1  # shrink window

            # Add the new character into the window
            char_set.add(s[right])

            # Update the longest length
            max_length = max(max_length, right - left + 1)

        return max_length


# ------------------ MAIN FUNCTION ------------------
def main():
    s = input("Enter a string: ")
    
    sol = Solution()
    result = sol.lengthOfLongestSubstring(s)

    print("Length of longest substring without repeating characters:", result)


# Run main when executed directly
if __name__ == "__main__":
    main()
