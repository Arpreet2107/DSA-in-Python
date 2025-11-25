# Function inside a Solution class to check if two strings are anagrams
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: If the lengths are not the same, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Step 2: Create a frequency dictionary to count characters of string s
        freq = {}

        # Step 3: Count occurrences of each character in string s
        for i in s:
            if i not in freq:      # If character not present in dictionary
                freq[i] = 1        # Initialize its count to 1
            else:
                freq[i] += 1       # Otherwise, increment its count

        # Step 4: Decrease frequency for characters from string t
        for i in t:
            if i not in freq:      # If any char of t is missing in s dictionary → Not anagram
                return False
            else:
                freq[i] -= 1       # Reduce its frequency

        # Step 5: After processing, all values must be zero for a valid anagram
        for i in freq.values():
            if i != 0:             # If any character count is not zero → Not anagram
                return False

        # Strings are anagrams
        return True


# ---------------------- MAIN FUNCTION ----------------------
def main():
    # Input strings
    s = input("Enter first string: ")
    t = input("Enter second string: ")

    # Create object of Solution class
    sol = Solution()

    # Call the isAnagram method and store result
    result = sol.isAnagram(s, t)

    # Print output
    if result:
        print("Yes, the strings are anagrams.")
    else:
        print("No, the strings are not anagrams.")


# Execute main only when file is run directly
if __name__ == "__main__":
    main()
