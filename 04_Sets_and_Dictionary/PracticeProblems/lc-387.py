# This script finds the index of the first non-repeating character in a string.
# It defines a Solution class with method firstUniqChar and a main() that reads input and prints the result.

from typing import Dict  # import typing helper for type annotations

class Solution:
    # Define a method that returns the index of the first unique character in s, or -1 if none.
    def firstUniqChar(self, s: str) -> int:
        freq: Dict[str, int] = {}                 # Create an empty dictionary to store character frequencies.
        for ch in s:                              # Iterate over each character in the input string.
            if ch not in freq:                    # If the character is not yet in the dictionary,
                freq[ch] = 1                      # set its count to 1.
            else:                                 # Otherwise (the character is already present),
                freq[ch] += 1                     # increment its count by 1.

        # After counting, loop over the string by index to preserve order.
        for i in range(len(s)):                   # i will be each index from 0 to len(s)-1
            if freq[s[i]] == 1:                   # If the character at index i has frequency 1,
                return i                          # return this index immediately (first unique).
        return -1                                 # If no unique character found, return -1.

def main() -> None:
    """
    main() reads a string from stdin, calls the solution, and prints the result.
    Usage:
      - Run the script and type the string when prompted.
      - Or pipe/redirect input: echo "leetcode" | python3 first_unique_char.py
    """
    # Prompt the user to enter a string. Using input() keeps the script simple and interactive.
    # If you prefer no prompt (for automated testing), replace input() with sys.stdin.readline().strip()
    s: str = input("Enter string: ").rstrip("\n")  # Read one line of input and strip trailing newline.

    solver = Solution()               # Create an instance of the Solution class.
    result = solver.firstUniqChar(s)  # Call the method with the user's string and store the result.

    # Print a user-friendly message with the index result.
    # You can change this to just print(result) if you need machine-readable output only.
    if result != -1:
        print(f"First non-repeating character: '{s[result]}' at index {result}")
    else:
        print("-1  (no non-repeating character found)")

# This Python idiom ensures main() runs only when the script is executed directly,
# and not when the file is imported as a module in another script.
if __name__ == "__main__":
    main()
